# Sigma Estimation Pipeline

Steps to estimate the dynamical subject metric Σ from neural data.

1. Load EEG dataset
2. Preprocess signal
3. Reconstruct state space (Takens embedding)
4. Estimate correlation dimension
5. Train predictive model
6. Compute prediction error
7. Estimate:

Ψ = 1/(1 + <E_t>)
C = correlation dimension
F = <E_t^2>

Σ = Ψ · C · exp(-βF)
