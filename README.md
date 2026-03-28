Dynamical Subject Metric (Σ)

A Dynamical Attractor Metric for the Conscious Subject

A Testable Operational Framework Based on Neural State-Space Invariants

Author: J.G. Urquizu O.
Field: Computational Neuroscience / Complex Systems
Date: March 2026

---

Overview

This repository contains the theoretical framework and computational pipeline for testing the Dynamical Subject Hypothesis.

The central idea is that conscious states may correlate with the presence of a stable reflexive attractor in neural state space.

From this hypothesis we derive an operational scalar metric (Σ) that can be estimated from neural time-series data such as EEG or MEG recordings.

The goal of this project is to provide a replicable framework that allows independent researchers to test whether conscious states correspond to identifiable dynamical invariants in neural activity.

---

Core Hypothesis

H2 — Dynamical Subject Hypothesis

Conscious states are expected to correlate with the presence of a stable reflexive attractor within the neural state space of a cognitive system.

If this is correct, conscious states should exhibit measurable dynamical properties that distinguish them from unconscious states.

---

Operational Metric

The framework defines a scalar indicator:

Σ = Ψ · C · e^(-βF)

where:

Ψ — Predictive Integration
Degree to which the system successfully predicts its own future state.

C — Dynamical Complexity
Correlation dimension of the reconstructed neural attractor.

F — Predictive Free Energy
Average squared prediction error of the internal predictive model.

β is a scaling parameter.

Higher Σ values indicate stronger dynamical coherence associated with conscious states.

---

Testable Prediction

The model generates the following falsifiable prediction:

Σ_awake > Σ_REM > Σ_deep_sleep > Σ_anesthesia

If this ordering is consistently observed across datasets, it would support the hypothesis that conscious states are associated with identifiable dynamical attractor structures in neural activity.

---

Computational Pipeline

The repository implements a reproducible pipeline consisting of the following stages:

1. Data Acquisition

Possible data sources include:

• EEG sleep datasets
• anesthesia recordings
• resting-state EEG

---

2. Preprocessing

Standard neurophysiological preprocessing:

• Bandpass filtering (0.5–120 Hz)
• Artifact removal using ICA
• Channel normalization (z-score)

---

3. State-Space Reconstruction

Neural dynamics are reconstructed using Takens embedding:

X_t = (x_t, x_{t−τ}, x_{t−2τ}, ...)

Parameters:

τ → mutual information minimum
m → false nearest neighbors method

---

4. Attractor Analysis

The following dynamical invariants are estimated:

• Correlation dimension (Grassberger–Procaccia)
• Lyapunov exponent
• entropy measures

---

5. Predictive Modeling

A local predictive model is trained on the neural time series.

Examples:

• autoregressive models
• nonlinear regression
• reservoir computing

Prediction error:

E_t = ||X_{t+1} − X̂_{t+1}||

---

6. Computation of Σ

The subject metric is then computed:

Σ = Ψ C e^(−βF)

---

Repository Structure

dynamical-subject-metric/

README.md

Paper/
    dynamical_subject_metric.pdf

Simulation/
    neural_dynamics_simulation.py

Analysis/
    sigma_estimation_pipeline.py

Data/
    dataset_sources.md

---

Simulation Framework

Before empirical testing, the hypothesis can be explored using simulated neural networks:

dx_i/dt = -x_i + Σ_j W_ij tanh(x_j) + η_i(t)

Networks implementing internal predictive loops are expected to exhibit higher Σ values.

---

Falsification Criteria

The hypothesis is weakened if:

1. Σ does not distinguish conscious from unconscious states.
2. Neural dynamics show no stable attractor structure.
3. Predictive integration does not correlate with consciousness level.

---

Research Goals

This project aims to transform the study of the conscious subject into a quantitative and testable scientific program based on measurable dynamical properties of neural systems.

---

References

Tononi G. (2008)
Consciousness as Integrated Information

Friston K. (2010)
The Free Energy Principle

Breakspear M. (2017)
Dynamic models of large-scale brain activity

Kuramoto Y. (1984)
Chemical Oscillations and Waves

Freeman W. (2000)
Neurodynamics
