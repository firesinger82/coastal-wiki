---
title: "Improvements to the post-processing of weather forecasts using machine learning and feature selection"
source: arxiv
arxiv_id: 2604.19340v1
seed: JMA
authors: Kazuma Iwase, Tomoyuki Takenawa
published: 2026-04-21

link: https://arxiv.org/abs/2604.19340v1
citation_status: draft-unsourced
action: archive
collected: 2026-06-12T00:05:48.812516+00:00
---

## Abstract

This study aims to develop and improve machine learning-based post-processing models for precipitation, temperature, and wind speed predictions using the Mesoscale Model (MSM) dataset provided by the Japan Meteorological Agency (JMA) for 18 locations across Japan, including plains, mountainous regions, and islands. By incorporating meteorological variables from grid points surrounding the target locations as input features and applying feature selection based on correlation analysis, we found that, in our experimental setting, the LightGBM-based models achieved lower RMSE than the specific neural-network baselines tested in this study, including a reproduced CNN baseline, and also generally achieved lower RMSE than both the raw MSM forecasts and the JMA post-processing product, MSM Guidance (MSMG), across many locations and forecast lead times. Because precipitation has a highly skewed distribution with many zero cases, we additionally examined Tweedie-based loss functions and event-weighted training strategies for precipitation forecasting. These improved event-oriented performance relative to the original LightGBM model, especially at higher rainfall thresholds, although the gains were site dependent and overall performance remained slightly below MSMG.

## Acquisition

- Open Access: download from arXiv link above
- Closed Access: use Sci-Hub suggestion below (manual approval required)
- Sci-Hub URL: https://sci-hub.se/2604.19340v1

## Triage Notes

- source_type: arxiv (primary archive)
- citation_status remains draft-unsourced until full-text verified
- Never auto-promote to verified
