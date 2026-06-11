---
title: "An Efficient Regional Storm Surge Surrogate Model Training Strategy Under Evolving Landscape and Climate Scenarios"
source: arxiv
arxiv_id: 2511.07269v3
seed: coastal flooding
authors: Ziyue Liu, Mohammad Ahmadi Gharehtoragh, Brenna Kari Losch, David R. Johnson
published: 2025-11-10

link: https://arxiv.org/abs/2511.07269v3
citation_status: draft-unsourced
action: archive
collected: 2026-06-07T00:00:44.637638+00:00
promoted_to: concepts/storm-surge/07-ml-emulators.md  # §7 추가 검토 후보 catalog (미트리아지 pointer)
promoted_date: 2026-06-11
---

## Abstract

Coastal communities face significant risk from storm-induced coastal flooding, which causes substantial societal and economic losses worldwide. Machine learning techniques have increasingly been integrated into coastal hazard modeling, particularly for storm surge prediction, due to advances in computational capacity. However, incorporating multiple projected future climate and landscape scenarios requires extensive numerical simulations of synthetic storm suites over large geospatial domains, resulting in rapidly escalating computational costs. This study proposes a cost-effective training data reduction strategy for machine learning based storm surge surrogate models that enables efficient incorporation of new future scenarios while minimizing computational burden. The proposed strategy reduces training data across three dimensions: grid points, input features, and storm suite size. Reducing the storm suite size for future scenario simulations is highly effective in guiding numerical simulations, yielding substantial reductions in simulation cost. The performance of surrogate models trained on reduced datasets was evaluated using different machine learning algorithms. Results demonstrate that the proposed reduction strategy is robust across different model types. When trained using 5,000 out of 80,000 grid points, 10 out of 12 input features, and 60 out of 90 storms, the total training dataset is reduced to approximately 5% of its original size. Despite this reduction, the trained model achieves a correlation coefficient of 0.94, comparable to models trained on the full dataset. In addition, storm selection methodologies are introduced to support efficient storm set expansion for future scenario analyses.

## Acquisition

- Open Access: download from arXiv link above
- Closed Access: use Sci-Hub suggestion below (manual approval required)
- Sci-Hub URL: https://sci-hub.se/2511.07269v3

## Triage Notes

- source_type: arxiv (primary archive)
- citation_status remains draft-unsourced until full-text verified
- Never auto-promote to verified
