---
title: "StormNet: Improving storm surge predictions with a GNN-based spatio-temporal offset forecasting model"
source: arxiv
arxiv_id: 2604.20688v2
seed: ADCIRC
authors: Noujoud Nader, Stefanos Giaremis, Clint Dawson, Carola Kaiser, Karame Mohammadiporshokooh, Hartmut Kaiser
published: 2026-04-22

link: https://arxiv.org/abs/2604.20688v2
citation_status: draft-unsourced
action: archive
collected: 2026-06-13T00:01:34.062238+00:00
promoted_to: concepts/storm-surge/07-ml-emulators.md#3
promoted_date: 2026-06-15
---

## Abstract

Storm surge forecasting remains a critical challenge in mitigating the impacts of tropical cyclones on coastal regions, particularly given recent trends of rapid intensification and increasing nearshore storm activity. Traditional high fidelity numerical models such as ADCIRC, while robust, are often hindered by inevitable uncertainties arising from various sources. To address these challenges, this study introduces StormNet, a spatio-temporal graph neural network (GNN) designed for bias correction of storm surge forecasts. StormNet integrates graph convolutional (GCN) and graph attention (GAT) mechanisms with long short-term memory (LSTM) components to capture complex spatial and temporal dependencies among water-level gauge stations. The model was trained using historical hurricane data from the U.S. Gulf Coast and evaluated on Hurricane Idalia (2023). Results demonstrate that StormNet can effectively reduce the root mean square error (RMSE) in water-level predictions by more than 70\% for 48-hour forecasts and above 50\% for 72-hour forecasts, as well as outperform a sequential LSTM baseline, particularly for longer prediction horizons. The model also exhibits low training time, enhancing its applicability in real-time operational forecasting systems. Overall, StormNet provides a computationally efficient and physically meaningful framework for improving storm surge prediction accuracy and reliability during extreme weather events.

## Acquisition

- Open Access: download from arXiv link above
- Closed Access: use Sci-Hub suggestion below (manual approval required)
- Sci-Hub URL: https://sci-hub.se/2604.20688v2

## Triage Notes

- source_type: arxiv (primary archive)
- citation_status remains draft-unsourced until full-text verified
- Never auto-promote to verified
