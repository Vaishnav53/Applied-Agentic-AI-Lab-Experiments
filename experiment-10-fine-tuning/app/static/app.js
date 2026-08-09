/**
 * Interactive Client Controller
 * Experiment 10 — Fine-Tuning for Domain Adaptation (MR23-1CS0436)
 */

document.addEventListener('DOMContentLoaded', () => {
    const trainForm = document.getElementById('train-form');
    const loraRankSelect = document.getElementById('lora-rank');
    const numEpochsInput = document.getElementById('num-epochs');
    const learningRateInput = document.getElementById('learning-rate');
    const runTrainBtn = document.getElementById('run-train-btn');
    const runEvalBtn = document.getElementById('run-eval-btn');

    const welcomeCard = document.getElementById('welcome-card');
    const resultsArea = document.getElementById('results-area');
    const durationBadge = document.getElementById('train-duration-badge');

    const finalValLossVal = document.getElementById('final-val-loss-val');
    const finalPerplexityVal = document.getElementById('final-perplexity-val');
    const accuracyGainVal = document.getElementById('accuracy-gain-val');

    const epochMetricsContainer = document.getElementById('epoch-metrics-container');
    const evalComparisonContainer = document.getElementById('eval-comparison-container');

    fetchDatasetStats();

    trainForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const reqBody = {
            lora_rank: parseInt(loraRankSelect.value, 10) || 16,
            lora_alpha: (parseInt(loraRankSelect.value, 10) || 16) * 2,
            learning_rate: parseFloat(learningRateInput.value) || 0.0002,
            num_epochs: parseInt(numEpochsInput.value, 10) || 3,
            batch_size: 4
        };

        runTrainBtn.disabled = true;
        runTrainBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Simulating LoRA Training Run...';
        welcomeCard.style.display = 'none';
        resultsArea.style.display = 'block';

        try {
            const res = await fetch('/api/train/run', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(reqBody)
            });

            if (!res.ok) {
                throw new Error(`HTTP Error: ${res.status}`);
            }

            const data = await res.json();
            renderTrainingResults(data);
            runEvaluation();
        } catch (err) {
            alert(`Training Run Error: ${err.message}`);
        } finally {
            runTrainBtn.disabled = false;
            runTrainBtn.innerHTML = '<span>Simulate LoRA Training Run</span> <i class="fa-solid fa-play"></i>';
        }
    });

    runEvalBtn.addEventListener('click', () => {
        runEvaluation();
    });

    async function fetchDatasetStats() {
        try {
            const res = await fetch('/api/dataset/stats');
            if (res.ok) {
                const stats = await res.json();
                document.getElementById('stat-train-samples').textContent = stats.train_samples_count || 0;
                document.getElementById('stat-val-samples').textContent = stats.val_samples_count || 0;
                document.getElementById('stat-train-tokens').textContent = stats.estimated_train_tokens || 0;
            }
        } catch (e) {
            console.warn('Dataset stats fetch error:', e);
        }
    }

    function renderTrainingResults(data) {
        durationBadge.style.display = 'inline-block';
        durationBadge.textContent = `${data.total_training_duration_ms} ms`;

        finalValLossVal.textContent = data.final_val_loss;
        finalPerplexityVal.textContent = data.final_perplexity;

        renderEpochMetricsTable(data.epoch_metrics || []);
    }

    function renderEpochMetricsTable(epochs) {
        if (!epochs || epochs.length === 0) {
            epochMetricsContainer.innerHTML = '<p class="subtitle">No epoch metrics recorded.</p>';
            return;
        }

        let html = `
            <table>
                <thead>
                    <tr>
                        <th>Epoch</th>
                        <th>Train Loss</th>
                        <th>Val Loss</th>
                        <th>Perplexity</th>
                        <th>Epoch Time</th>
                    </tr>
                </thead>
                <tbody>
        `;

        epochs.forEach(ep => {
            html += `
                <tr>
                    <td><strong>Epoch ${ep.epoch}</strong></td>
                    <td style="font-family:var(--font-mono); color:var(--success);">${ep.train_loss}</td>
                    <td style="font-family:var(--font-mono); color:var(--secondary);">${ep.val_loss}</td>
                    <td style="font-family:var(--font-mono);">${ep.perplexity}</td>
                    <td style="font-size:0.8rem; color:var(--text-muted);">${ep.duration_ms} ms</td>
                </tr>
            `;
        });

        html += '</tbody></table>';
        epochMetricsContainer.innerHTML = html;
    }

    async function runEvaluation() {
        runEvalBtn.disabled = true;
        runEvalBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Evaluating...';

        try {
            const res = await fetch('/api/eval/run', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    instruction: "Explain how to mitigate CVE-2023-23397 Outlook vulnerability in an enterprise environment.",
                    context_input: "System environment: Windows Server 2019, Microsoft 365 Hybrid."
                })
            });

            if (res.ok) {
                const data = await res.json();
                renderEvalComparisonCards(data);
                accuracyGainVal.textContent = `+${data.accuracy_improvement_percent}%`;
            }
        } catch (e) {
            console.warn('Evaluation error:', e);
        } finally {
            runEvalBtn.disabled = false;
            runEvalBtn.innerHTML = 'Evaluate Query <i class="fa-solid fa-play"></i>';
        }
    }

    function renderEvalComparisonCards(data) {
        let html = `
            <div class="eval-card" style="border-left: 4px solid var(--danger);">
                <div style="font-size:0.85rem; font-weight:700; color:var(--danger); margin-bottom:0.4rem;">
                    <i class="fa-solid fa-cube"></i> Base Model (Un-adapted)
                </div>
                <div style="font-size:0.85rem; color:var(--text-main); margin-bottom:0.75rem;">
                    ${data.base_model_output}
                </div>
                <div style="font-size:0.75rem; font-family:var(--font-mono); color:var(--text-muted);">
                    Accuracy: <strong>${data.base_model_accuracy}%</strong> · Hallucination Rate: <strong>${data.base_model_hallucination_rate * 100}%</strong>
                </div>
            </div>

            <div class="eval-card" style="border-left: 4px solid var(--success);">
                <div style="font-size:0.85rem; font-weight:700; color:var(--success); margin-bottom:0.4rem;">
                    <i class="fa-solid fa-layer-group"></i> Fine-Tuned Model (LoRA Adapted)
                </div>
                <div style="font-size:0.85rem; color:#6ee7b7; margin-bottom:0.75rem;">
                    ${data.finetuned_model_output}
                </div>
                <div style="font-size:0.75rem; font-family:var(--font-mono); color:var(--text-muted);">
                    Accuracy: <strong style="color:var(--success);">${data.finetuned_model_accuracy}%</strong> · Hallucination Rate: <strong style="color:var(--success);">${data.finetuned_model_hallucination_rate * 100}%</strong>
                </div>
            </div>
        `;
        evalComparisonContainer.innerHTML = html;
    }
});
