---
title: "Damage-TriageFormer: A Foundation-Model Framework for Typology-Based Building Damage Assessment from Mono-Temporal Imagery"
source: arxiv
arxiv_id: 2606.12248v1
seed: NOAA
authors: Yiming Xiao, Yu-Hsuan Ho, Sanjay Thasma, Junwei Ma, Ali Mostafavi
published: 2026-06-10

link: https://arxiv.org/abs/2606.12248v1
citation_status: draft-unsourced
action: archive
collected: 2026-06-14T00:01:23.313459+00:00
---

## Abstract

Decision-relevant building damage assessment is critical for prioritizing resources and recovery after a disaster, yet most automated methods either flatten damage into a single severity scale (no damage, minor, major, destroyed) or require paired pre- and post-event imagery that is often unavailable for emerging hazards. This paper presents Damage-TriageFormer, a single-image, post-event, footprint-conditioned model that produces a damage typology rather than a severity scale. We contribute: (1) DamageTriage-Bench, a new benchmark built from NOAA Emergency Response Imagery across Hurricane Michael (2018), Hurricane Helene (2024), and the 2025 Los Angeles wildfire complex, with five typology classes that distinguish roof damage from structural damage and, within each, partial from total extent; and (2) Damage-TriageFormer, which extends a DINOv3 ViT-L backbone with a Simple Feature Pyramid for higher-resolution instance pooling, a two-stage gated damage head, and an auxiliary severity-regression objective. Our model achieves macro F1 of 0.624 on validation and 0.619 on a held-out stratified test set, performing strongest where operational triage needs it most, with per-class F1 of 0.91 and 0.84 on undamaged buildings and total structural collapse, respectively. While the rare Total Roof Damage class remains difficult due to its limited examples and an inherently ambiguous label boundary, our results show that single-image post-event imagery can support actionable building damage typing, enabling targeted emergency response and resource allocation without a pre-event reference.

## Acquisition

- Open Access: download from arXiv link above
- Closed Access: use Sci-Hub suggestion below (manual approval required)
- Sci-Hub URL: https://sci-hub.se/2606.12248v1

## Triage Notes

- source_type: arxiv (primary archive)
- citation_status remains draft-unsourced until full-text verified
- Never auto-promote to verified
