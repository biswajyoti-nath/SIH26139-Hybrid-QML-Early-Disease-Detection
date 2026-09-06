#!/bin/bash
echo "Starting WDBC Ablation..."
uv run python3 -m backend.core.cv_experiment_runner experiments/configs/exp_t103b_ablation_wdbc.json
echo "WDBC Ablation finished. Starting Parkinsons Ablation..."
uv run python3 -m backend.core.cv_experiment_runner experiments/configs/exp_t103b_ablation_parkinsons.json
echo "Parkinsons Ablation finished."
