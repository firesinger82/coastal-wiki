---
title: "Flo: A data-driven limited-area storm surge model"
source: arxiv
arxiv_id: 2601.02090v2
seed: storm surge modeling
authors: Nils Melsom Kristensen, Mateusz Matuszak, Paulina Tedesco, Ina Kristine Berentsen Kullmann, Johannes Röhrs
published: 2026-01-05

link: https://arxiv.org/abs/2601.02090v2
citation_status: draft-unsourced
action: archive
collected: 2026-06-07T00:00:43.845061+00:00
promoted_to: concepts/storm-surge/07-ml-emulators.md  # §7 추가 검토 후보 catalog (미트리아지 pointer)
promoted_date: 2026-06-11
---

## Abstract

We present Flo, a data-driven storm surge model, covering the North Sea, Norwegian Sea and Barents Sea. The model is built using the Anemoi framework for creating machine learning weather forecasting systems, developed by the European Centre for Medium-Range Weather Forecasts and partners. The model is based on a graph neural network, and is capable of simulating water level due to atmospheric effects (wind stress and inverse barometer effect, i.e. the non-tidally induced part of the total water level; the residual water level) at a horizontal resolution of 4 km and a temporal resolution of 1 hour with a quality comparable to the numerical model on which it was trained. The model was trained using a dataset consisting of 43 years of atmospheric data from the 3-km Norwegian Reanalysis hindcast for mean sea level pressure and winds, and the NORA-Surge hindcast for water level. Evaluation was done by comparing results from hindcast runs of the Flo model against independent observations of more than 90 water level gauges along the European coast, and against the NORA-Surge hindcast. The evaluation shows that Flo produces hindcasts with accuracy similar to the NORA-Surge hindcast, and it is shown that the model can resolve key physical processes. As the NORA-Surge hindcast used for training does not include data assimilation, Flo is not expected to systematically outperform the numerical model when evaluated against observations. Nevertheless, the present work represents an important step towards complementing traditional physics-based storm surge modelling with machine learning approaches and the framework establishes a strong foundation for future developments, particularly for training storm surge models that offer more flexibility for incorporating observations and other additional data sources.

## Acquisition

- Open Access: download from arXiv link above
- Closed Access: use Sci-Hub suggestion below (manual approval required)
- Sci-Hub URL: https://sci-hub.se/2601.02090v2

## Triage Notes

- source_type: arxiv (primary archive)
- citation_status remains draft-unsourced until full-text verified
- Never auto-promote to verified
