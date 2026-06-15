---
title: "Toward AI-Driven Digital Twins for Metropolitan Floods: A Conditional Latent Dynamics Network Surrogate of the Shallow Water Equations"
source: arxiv
arxiv_id: 2605.13761v1
seed: USGS
authors: Phillip Si, Yuan Qiu, Omar Sallam, Jeremy Feinstein, Ziang He, Eugene Yan, Peng Chen
published: 2026-05-13

link: https://arxiv.org/abs/2605.13761v1
citation_status: draft-unsourced
action: archive
collected: 2026-06-07T00:01:03.462288+00:00
promoted_to: concepts/storm-surge/07-ml-emulators.md#77
promoted_date: 2026-06-15
---

## Abstract

AI-driven flood digital twins demand fast hydrodynamic surrogates for ensemble forecasting and observation assimilation. Yet even GPU-accelerated two-dimensional shallow water equation (SWE) solvers still require $\sim 55$ minutes per $96$-hour run on a $\sim 4.2$-million-active-cell metropolitan basin (the Des~Plaines River basin at $30\,\mathrm{m}$ resolution), making such workloads prohibitive at native resolution. We present the Conditional Latent Dynamics Network (CLDNet): a low-dimensional latent neural ODE driven by rainfall, paired with a coordinate-based decoder conditioned on static terrain (elevation, slope, Manning roughness) that reconstructs depth and discharge at arbitrary query points. Pointwise decoding decouples memory from grid size and handles irregular watersheds natively, enabling metropolitan-scale training on a single compute node and direct queries at exact gauge coordinates without raster snapping. We evaluate CLDNet on a synthetic $250{,}000$-cell Texas benchmark and on a new Des~Plaines case study of $114$ real-rainfall Stage~IV storms whose reference simulator we validate against United States Geological Survey (USGS) gauges at the April~2013 flood-of-record (Nash--Sutcliffe efficiency $0.57$--$0.94$ on mean-recentered water-surface elevation). CLDNet roughly halves the relative root-mean-squared error of an unconditional baseline, outperforms regular-grid VAE--ConvLSTM and FNO baselines on the Texas benchmark (both presuppose a Cartesian grid and do not apply to the irregular Des~Plaines watershed), reaches a critical success index of $\approx 86\%$ at the $0.5\,\mathrm{m}$ inundation threshold, and produces a full $96$-hour basin-wide forecast in $\sim 29$ seconds -- a $\sim 115\times$ speedup.

## Acquisition

- Open Access: download from arXiv link above
- Closed Access: use Sci-Hub suggestion below (manual approval required)
- Sci-Hub URL: https://sci-hub.se/2605.13761v1

## Triage Notes

- source_type: arxiv (primary archive)
- citation_status remains draft-unsourced until full-text verified
- Never auto-promote to verified
