/**
 * Interactive Client Controller
 * Experiment 11 — Model Optimization Experiment (MR23-1CS0436)
 */

document.addEventListener('DOMContentLoaded', () => {
    const optForm = document.getElementById('opt-form');
    const baseModelSelect = document.getElementById('base-model');
    const targetHardwareSelect = document.getElementById('target-hardware');
    const runOptBtn = document.getElementById('run-opt-btn');

    const welcomeCard = document.getElementById('welcome-card');
    const resultsArea = document.getElementById('results-area');
    const durationBadge = document.getElementById('opt-duration-badge');

    const vramChampionVal = document.getElementById('vram-champion-val');
    const throughputChampionVal = document.getElementById('throughput-champion-val');

    const profilesCardsContainer = document.getElementById('profiles-cards-container');
    const synthesisBox = document.getElementById('synthesis-box');

    optForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const reqBody = {
            base_model_name: baseModelSelect.value,
            target_hardware: targetHardwareSelect.value
        };

        runOptBtn.disabled = true;
        runOptBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Executing Optimization Benchmark...';
        welcomeCard.style.display = 'none';
        resultsArea.style.display = 'block';

        try {
            const res = await fetch('/api/optimization/benchmark', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(reqBody)
            });

            if (!res.ok) {
                throw new Error(`HTTP Error: ${res.status}`);
            }

            const data = await res.json();
            renderOptimizationResults(data);
        } catch (err) {
            alert(`Optimization Benchmark Error: ${err.message}`);
        } finally {
            runOptBtn.disabled = false;
            runOptBtn.innerHTML = '<span>Execute Optimization Benchmark</span> <i class="fa-solid fa-bolt"></i>';
        }
    });

    function renderOptimizationResults(data) {
        durationBadge.style.display = 'inline-block';
        durationBadge.textContent = `${data.evaluation_duration_ms} ms`;

        vramChampionVal.textContent = data.vram_reduction_champion;
        throughputChampionVal.textContent = data.throughput_champion;

        renderProfilesCards(data.profiles || []);
        synthesisBox.textContent = data.optimization_synthesis || 'No synthesis recorded.';
    }

    function renderProfilesCards(profiles) {
        if (!profiles || profiles.length === 0) {
            profilesCardsContainer.innerHTML = '<p class="subtitle">No profiles recorded.</p>';
            return;
        }

        let html = '';
        profiles.forEach(prof => {
            const m = prof.metrics;
            html += `
                <div class="profile-card">
                    <div>
                        <div class="profile-header">
                            <i class="fa-solid fa-layer-group"></i> ${prof.level_name}
                        </div>
                        <div style="font-size:0.8rem; color:var(--primary); font-weight:600; margin-bottom:0.3rem;">
                            Technique: ${prof.technique}
                        </div>
                        <div style="font-size:0.85rem; color:var(--text-main); margin-bottom:0.75rem;">
                            ${prof.description}
                        </div>
                    </div>
                    <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap:0.4rem; font-size:0.75rem; border-top:1px solid var(--border-color); padding-top:0.6rem; font-family:var(--font-mono);">
                        <div>Model Size: <strong>${m.file_size_gb} GB</strong></div>
                        <div>VRAM Footprint: <strong style="color:var(--secondary);">${m.vram_usage_gb} GB</strong></div>
                        <div>Latency: <strong>${m.latency_ms} ms</strong></div>
                        <div>Throughput: <strong style="color:var(--success);">${m.throughput_tokens_sec} tok/s</strong></div>
                        <div style="grid-column: span 2;">Quality Retention: <strong style="color:var(--primary);">${m.quality_retention_percent}%</strong></div>
                    </div>
                </div>
            `;
        });

        profilesCardsContainer.innerHTML = html;
    }
});
