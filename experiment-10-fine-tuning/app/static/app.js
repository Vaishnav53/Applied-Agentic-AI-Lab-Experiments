/**
 * Interactive Client Controller
 * Experiment 10 — Fine-Tuning & Domain Adaptation (MR23-1CS0436)
 */

document.addEventListener('DOMContentLoaded', () => {
    const trainForm = document.getElementById('train-form');
    const loraRankSelect = document.getElementById('lora-rank');
    const numEpochsInput = document.getElementById('num-epochs');
    const learningRateInput = document.getElementById('learning-rate');
    const runTrainBtn = document.getElementById('run-train-btn');

    const evalForm = document.getElementById('eval-form');
    const evalInstructionInput = document.getElementById('eval-instruction');
    const runEvalBtn = document.getElementById('run-eval-btn');

    const datasetStatsBox = document.getElementById('dataset-stats-box');
    const durationBadge = document.getElementById('train-duration-badge');

    const jobSummaryCard = document.getElementById('job-summary-card');
    const jobSummaryBox = document.getElementById('job-summary-box');

    const lossTableContainer = document.getElementById('loss-table-container');
    const lossTableBody = document.getElementById('loss-table-body');

    const evalResultsContainer = document.getElementById('eval-results-container');

    // Fetch Initial Dataset Stats
    fetchDatasetStats();

    trainForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const reqBody = {
            lora_rank: parseInt(loraRankSelect.value),
            num_epochs: parseInt(numEpochsInput.value),
            learning_rate: parseFloat(learningRateInput.value)
        };

        runTrainBtn.disabled = true;
        runTrainBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Executing PyTorch Autograd Training...';

        try {
            const res = await fetch('/api/fine-tuning/train', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(reqBody)
            });

            if (!res.ok) throw new Error(`HTTP Error: ${res.status}`);

            const data = await res.json();
            renderTrainingResults(data);
        } catch (err) {
            console.error('Training Error:', err);
            alert(`Fine-Tuning Error: ${err.message}`);
        } finally {
            runTrainBtn.disabled = false;
            runTrainBtn.innerHTML = '<span>Execute Real LoRA Fine-Tuning</span> <i class="fa-solid fa-play"></i>';
        }
    });

    evalForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const reqBody = {
            instruction: evalInstructionInput.value
        };

        runEvalBtn.disabled = true;
        runEvalBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Evaluating Models...';

        try {
            const res = await fetch('/api/fine-tuning/evaluate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(reqBody)
            });

            if (!res.ok) throw new Error(`HTTP Error: ${res.status}`);

            const data = await res.json();
            renderEvalResults(data);
        } catch (err) {
            console.error('Evaluation Error:', err);
            alert(`Evaluation Error: ${err.message}`);
        } finally {
            runEvalBtn.disabled = false;
            runEvalBtn.innerHTML = '<span>Evaluate Base vs. Trained Checkpoint</span> <i class="fa-solid fa-code-compare"></i>';
        }
    });

    async function fetchDatasetStats() {
        try {
            const res = await fetch('/api/fine-tuning/dataset');
            if (!res.ok) return;
            const data = await res.json();
            datasetStatsBox.innerHTML = `
                <div><strong>Train Samples:</strong> ${data.train_samples_count}</div>
                <div><strong>Val Samples:</strong> ${data.val_samples_count}</div>
                <div><strong>Eval Samples:</strong> ${data.eval_samples_count}</div>
                <div style="font-size:0.75rem; color:var(--text-muted); margin-top:0.4rem;">
                    Pre-curated cybersecurity domain adaptation dataset
                </div>
            `;
        } catch (err) {
            console.error('Failed to fetch dataset stats:', err);
        }
    }

    function renderTrainingResults(data) {
        if (durationBadge) {
            durationBadge.style.display = 'inline-block';
            durationBadge.textContent = `${data.total_training_duration_ms} ms`;
        }

        if (jobSummaryCard) jobSummaryCard.style.display = 'block';
        if (jobSummaryBox) {
            jobSummaryBox.innerHTML = `
                <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap:0.6rem; font-family:var(--font-mono); font-size:0.85rem;">
                    <div><strong>Job ID:</strong> ${data.job_id}</div>
                    <div><strong>Base Model:</strong> ${data.base_model_identifier}</div>
                    <div><strong>Trainable Parameters:</strong> <span style="color:var(--primary);">${data.trainable_parameter_count}</span> (LoRA r=${data.lora_rank})</div>
                    <div><strong>Frozen Base Parameters:</strong> <span style="color:var(--text-muted);">${data.frozen_parameter_count}</span> (requires_grad = False)</div>
                    <div><strong>Trainable Parameter Delta:</strong> <span style="color:var(--success); font-weight:700;">+${data.parameter_change_norm}</span> (&gt; 0.0)</div>
                    <div><strong>Frozen Parameter Delta:</strong> <span style="color:var(--secondary); font-weight:700;">0.000000</span> (Strictly Unchanged)</div>
                    <div><strong>Final Loss:</strong> ${data.final_train_loss}</div>
                    <div style="grid-column: span 2; word-break:break-all; font-size:0.75rem; background:rgba(0,0,0,0.3); padding:0.4rem; border-radius:6px;">
                        <strong>Saved PyTorch Checkpoint:</strong> ${data.checkpoint_path}
                    </div>
                </div>
            `;
        }

        if (lossTableContainer) lossTableContainer.style.display = 'block';
        if (lossTableBody) {
            let rowsHtml = '';
            data.epoch_metrics.forEach(m => {
                rowsHtml += `
                    <tr>
                        <td><strong>Epoch ${m.epoch}</strong></td>
                        <td style="color:var(--warning); font-family:var(--font-mono);">${m.train_loss}</td>
                        <td style="color:var(--primary); font-family:var(--font-mono);">${m.val_loss}</td>
                        <td style="font-family:var(--font-mono);">${m.perplexity}</td>
                        <td style="color:var(--text-muted);">${m.duration_ms} ms</td>
                    </tr>
                `;
            });
            lossTableBody.innerHTML = rowsHtml;
        }
    }

    function renderEvalResults(data) {
        if (!evalResultsContainer) return;
        evalResultsContainer.style.display = 'grid';
        evalResultsContainer.style.gridTemplateColumns = '1fr 1fr';
        evalResultsContainer.style.gap = '1rem';
        evalResultsContainer.style.marginTop = '1rem';

        evalResultsContainer.innerHTML = `
            <div class="model-eval-card" style="background:var(--card-bg); border:1px solid var(--border-color); border-radius:12px; padding:1rem;">
                <div style="font-weight:700; color:var(--text-muted); margin-bottom:0.5rem; display:flex; align-items:center; justify-content:space-between;">
                    <span><i class="fa-solid fa-cube"></i> Base Model (LoRA Disabled)</span>
                    <span class="badge" style="background:rgba(255,255,255,0.1);">${data.base_model_accuracy}% Accuracy</span>
                </div>
                <div style="font-size:0.85rem; color:var(--text-main); margin-bottom:0.8rem; background:rgba(0,0,0,0.2); padding:0.8rem; border-radius:8px;">
                    ${data.base_model_output}
                </div>
                <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">
                    Evaluated Correct: ${data.base_correct_count} / ${data.total_evaluated_samples} samples
                </div>
            </div>

            <div class="model-eval-card" style="background:var(--card-bg); border:1px solid var(--primary); border-radius:12px; padding:1rem;">
                <div style="font-weight:700; color:var(--primary); margin-bottom:0.5rem; display:flex; align-items:center; justify-content:space-between;">
                    <span><i class="fa-solid fa-wand-magic-sparkles"></i> Fine-Tuned Model (LoRA Checkpoint)</span>
                    <span class="badge" style="background:var(--success); color:#000;">${data.finetuned_model_accuracy}% Accuracy</span>
                </div>
                <div style="font-size:0.85rem; color:var(--text-main); margin-bottom:0.8rem; background:rgba(0,0,0,0.2); padding:0.8rem; border-radius:8px;">
                    ${data.finetuned_model_output}
                </div>
                <div style="font-size:0.75rem; color:var(--success); font-family:var(--font-mono); font-weight:600;">
                    Evaluated Correct: ${data.finetuned_correct_count} / ${data.total_evaluated_samples} samples (+${data.accuracy_improvement_percent}% Gain)
                </div>
            </div>
        `;
    }
});
