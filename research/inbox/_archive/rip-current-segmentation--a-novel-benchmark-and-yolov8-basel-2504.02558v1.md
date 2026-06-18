---
title: "Rip Current Segmentation: A Novel Benchmark and YOLOv8 Baseline Results"
source: arxiv
arxiv_id: 2504.02558v1
seed: rip current
authors: Andrei Dumitriu, Florin Tatui, Florin Miron, Radu Tudor Ionescu, Radu Timofte
published: 2025-04-03
doi: https://doi.org/10.1109/CVPRW59228.2023.00133
link: https://arxiv.org/abs/2504.02558v1
promoted_to: concepts/rip-currents/01-concept.md
promoted_date: 2026-06-18
citation_status: draft-unsourced
action: archive
collected: 2026-06-16T00:01:45.733167+00:00
---

## Abstract

Rip currents are the leading cause of fatal accidents and injuries on many beaches worldwide, emphasizing the importance of automatically detecting these hazardous surface water currents. In this paper, we address a novel task: rip current instance segmentation. We introduce a comprehensive dataset containing $2,466$ images with newly created polygonal annotations for instance segmentation, used for training and validation. Additionally, we present a novel dataset comprising $17$ drone videos (comprising about $24K$ frames) captured at $30 FPS$, annotated with both polygons for instance segmentation and bounding boxes for object detection, employed for testing purposes. We train various versions of YOLOv8 for instance segmentation on static images and assess their performance on the test dataset (videos). The best results were achieved by the YOLOv8-nano model (runnable on a portable device), with an mAP50 of $88.94%$ on the validation dataset and $81.21%$ macro average on the test dataset. The results provide a baseline for future research in rip current segmentation. Our work contributes to the existing literature by introducing a detailed, annotated dataset, and training a deep learning model for instance segmentation of rip currents. The code, training details and the annotated dataset are made publicly available at https://github.com/Irikos/rip_currents.

## Acquisition

- Open Access: download from arXiv link above
- Closed Access: use Sci-Hub suggestion below (manual approval required)
- Sci-Hub URL: https://sci-hub.se/https://doi.org/10.1109/CVPRW59228.2023.00133

## Triage Notes

- source_type: arxiv (primary archive)
- citation_status remains draft-unsourced until full-text verified
- Never auto-promote to verified
