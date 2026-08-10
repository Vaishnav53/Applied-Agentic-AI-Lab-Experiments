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

    const evalForm = document.getElementById('eval-form');
    const evalInstructionInput = document.getElementById('eval-instruction');
    const runEvalBtn = document.getElementById('run-eval-btn');

    const durationBadge = document.getElementById('train-duration-badge');
    const datasetStatsBox = document.getElementById('dataset-stats-box');

    const jobSummaryCard = document.getElementById('job-summary-card');
    const jobSummaryBox = document.getElementById('job-summary-box');

    const lossTableContainer = document.getElementById('loss-table-container');
    const lossTableBody = document.getElementById('loss-table-body');

    const evalResultsContainer = document.getElementById('eval-results-container');

    fetchDatasetStats();

    trainForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const rank = parseInt(loraRankSelect.value, 10) || 8;
        const reqBody = {
            lora_rank: rank,
            lora_alpha: rank * 2,
            learning_rate: parseFloat(learningRateInput.value) || 0.01,
            num_epochs: parseInt(numEpochsInput.value, 10) || 5,
            batch_size: 4
        };

        runTrainBtn.disabled = true;
        runTrainBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Executing Real LoRA Training...';

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
            console.error('Training error:', err);
            alert(`Training Error: ${err.message}`);
        } finally {
            runTrainBtn.disabled = false;
            runTrainBtn.innerHTML = '<span>Execute Real LoRA Fine-Tuning</span> <i class="fa-solid fa-play"></i>';
        }
    });

    evalForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        runEvaluation();
    });

    async function fetchDatasetStats() {
        try {
            const res = await fetch('/api/dataset/stats');
            if (res.ok) {
                const data = await res.json();
                datasetStatsBox.innerHTML = `
                    <div><strong>Train Samples:</strong> ${data.train_samples_count || 4}</div>
                    <div><strong>Val Samples:</strong> ${data.val_samples_count || 2}</div>
                    <div><strong>Domain:</strong> Cybersecurity Operations</div>
                    <div><strong>Task Type:</strong> Instruction Tuning & Classification</div>
                `;
            }
        } catch (e) {
            console.warn('Dataset stats error:', e);
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
                <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap:0.6rem; font-size:0.85rem;">
                    <div><strong>Job ID:</strong> ${data.job_id}</div>
                    <div><strong>Status:</strong> <span class="badge status-badge">${data.training_status}</span></div>
                    <div><strong>Base Model:</strong> ${data.base_model_identifier}</div>
                    <div><strong>Model Name:</strong> ${data.model_name}</div>
                    <div><strong>Frozen Parameters:</strong> ${data.frozen_parameter_count}</div>
                    <div><strong>Trainable LoRA Params:</strong> <strong style="color:var(--primary);">${data.trainable_parameter_count}</strong></div>
                    <div><strong>Parameter Change Norm (Δθ):</strong> <strong style="color:var(--success);">${data.parameter_change_norm}</strong></div>
                    <div><strong>Final Val Loss / Perplexity:</strong> ${data.final_val_loss} / ${data.final_perplexity}</div>
                </div>
                <div style="margin-top:0.6rem; font-size:0.8rem; color:var(--text-muted); word-break:break-all;">
                    <strong>Checkpoint Artifact Saved:</strong> <code>${data.checkpoint_path}</code>
                </div>
            `;
        }

        if (lossTableContainer) lossTableContainer.style.display = 'block';
        if (lossTableBody) {
            let rowsHtml = '';
            (data.epoch_metrics || []).forEach(m => {
                rowsHtml += `
                    <tr>
                        <td>Epoch ${m.epoch}</td>
                        <td>${m.train_loss}</td>
                        <td>${m.val_loss}</td>
                        <td>${m.perplexity}</td>
                        <td>${m.duration_ms} ms</td>
                    </tr>
                `;
            });
            lossTableBody.innerHTML = rowsHtml;
        }
    }

    async function runEvaluation() {
        const instr = evalInstructionInput.value.trim() || "Explain how to mitigate CVE-2023-23397 Outlook vulnerability in an enterprise environment.";
        runEvalBtn.disabled = true;
        runEvalBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Evaluating Checkpoint...';

        try {
            const res = await fetch('/api/eval/run', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ instruction: instr, context_input: "System environment: Windows Server 2019, Microsoft 365 Hybrid." })
            });

            if (res.ok) {
                const data = await res.json();
                renderEvalComparison(data);
            }
        } catch (e) {
            console.error('Eval error:', e);
        } finally {
            runEvalBtn.disabled = false;
            runEvalBtn.innerHTML = '<span>Evaluate Base vs. Trained Checkpoint</span> <i class="fa-solid fa-code-compare"></i>';
        }
    }

    function renderEvalComparison(data) {
        if (!evalResultsContainer) return;
        evalResultsContainer.style.display = 'grid';
        evalResultsContainer.innerHTML = `
            <div class="result-card">
                <div class="card-header">
                    <h3><i class="fa-solid fa-cube"></i> Base Model (LoRA Adapter Disabled)</h3>
                </div>
                <div class="card-body">
                    <p style="font-size:0.85rem; margin-bottom:0.6rem;">${data.base_model_output}</p>
                    <div style="font-size:0.8rem; color:var(--text-muted);">
                        <strong>Accuracy:</strong> ${data.base_model_accuracy}% · <strong>Hallucination Rate:</strong> ${(data.base_model_hallucination_rate * 100).toFixed(1)}%
                    </div>
                </div>
            </div>

            <div class="result-card highlight-card">
                <div class="card-header">
                    <h3><i class="fa-solid fa-sliders"></i> Fine-Tuned Model (LoRA Adapter Loaded)</h3>
                </div>
                <div class="card-body">
                    <p style="font-size:0.85rem; margin-bottom:0.6rem; color:var(--text-main);">${data.finetuned_model_output}</p>
                    <div style="font-size:0.8rem; color:var(--success);">
                        <strong>Accuracy:</strong> ${data.finetuned_model_accuracy}% (+${data.accuracy_improvement_percent}%) · <strong>Hallucination Rate:</strong> ${(data.finetuned_model_hallucination_rate * 100).toFixed(1)}%
                    </div>
                </div>
            </div>
        `;
    }
});
