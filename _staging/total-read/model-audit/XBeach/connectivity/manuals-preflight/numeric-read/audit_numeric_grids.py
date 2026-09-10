#!/usr/bin/env python3
"""Exhaustively parse the seven previously-partial numeric files and plot full fields."""
import hashlib
import json
import math
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/xbeach-mpl-cache")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
REPO = Path(__file__).resolve().parents[7]
BASE = REPO / "models/XBeach/raw/manuals/examples/Wong2016"
CASES = {
    "Bijleveld_nonh_s5": ["bed.dep", "x.grd", "y.grd"],
    "Bijleveld_surfbeat_s200": ["bed.dep", "x.grd", "y.grd", "chezy.txt"],
}


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def parse_params(path):
    values = {}
    raw_lines = path.read_text(errors="strict").splitlines()
    for lineno, line in enumerate(raw_lines, 1):
        body = line.split("%", 1)[0].strip()
        if "=" not in body:
            continue
        key, value = (x.strip() for x in body.split("=", 1))
        values[key] = {"value": value, "line": lineno, "raw": line}
    return values


def numeric_file(path):
    # loadtxt fails on any nonnumeric token or ragged row, so success covers every token.
    a = np.loadtxt(path, dtype=np.float64, ndmin=2)
    finite = np.isfinite(a)
    q = np.quantile(a[finite], [0, .01, .25, .5, .75, .99, 1]).tolist()
    vals, counts = np.unique(a, return_counts=True)
    unique_top = sorted(zip(counts.tolist(), vals.tolist()), reverse=True)[:12]
    with path.open("rt", errors="strict") as f:
        widths = [len(line.split()) for line in f]
    return a, {
        "path": path.relative_to(REPO).as_posix(),
        "sha256": digest(path),
        "bytes": path.stat().st_size,
        "rows": int(a.shape[0]),
        "columns": int(a.shape[1]),
        "numeric_tokens": int(a.size),
        "all_rows_same_width": len(set(widths)) == 1,
        "nonfinite_count": int((~finite).sum()),
        "negative_count": int((a < 0).sum()),
        "zero_count": int((a == 0).sum()),
        "unique_value_count": int(vals.size),
        "quantiles_min_p01_p25_p50_p75_p99_max": q,
        "most_frequent_values_count_then_value": unique_top,
    }


def geometry(x, y):
    hi = np.hypot(np.diff(x, axis=1), np.diff(y, axis=1))
    hj = np.hypot(np.diff(x, axis=0), np.diff(y, axis=0))
    dxdi = np.diff(x, axis=1)[:-1]
    dydi = np.diff(y, axis=1)[:-1]
    dxdj = np.diff(x, axis=0)[:, :-1]
    dydj = np.diff(y, axis=0)[:, :-1]
    jac = dxdi * dydj - dxdj * dydi
    return {
        "x_extent": [float(x.min()), float(x.max())],
        "y_extent": [float(y.min()), float(y.max())],
        "i_edge_length_min_median_max": [float(hi.min()), float(np.median(hi)), float(hi.max())],
        "j_edge_length_min_median_max": [float(hj.min()), float(np.median(hj)), float(hj.max())],
        "zero_i_edges": int((hi == 0).sum()),
        "zero_j_edges": int((hj == 0).sum()),
        "cell_jacobian_min_median_max": [float(jac.min()), float(np.median(jac)), float(jac.max())],
        "negative_jacobian_cells": int((jac < 0).sum()),
        "zero_jacobian_cells": int((jac == 0).sum()),
        "jacobian_sign_consistent": bool(np.all(jac > 0) or np.all(jac < 0)),
    }


def plot_case(name, arrays):
    has_chezy = "chezy.txt" in arrays
    fig, axes = plt.subplots(2, 3 if has_chezy else 2, figsize=(16 if has_chezy else 12, 9), constrained_layout=True)
    axes = np.asarray(axes).ravel()
    bed, x, y = arrays["bed.dep"], arrays["x.grd"], arrays["y.grd"]
    im = axes[0].imshow(bed, origin="lower", aspect="auto", cmap="terrain")
    axes[0].set_title("bed.dep: every cell, index space")
    fig.colorbar(im, ax=axes[0], shrink=.75)
    stepj = max(1, x.shape[0] // 30); stepi = max(1, x.shape[1] // 30)
    axes[1].plot(x[::stepj].T, y[::stepj].T, color="C0", alpha=.45, linewidth=.35)
    axes[1].plot(x[:, ::stepi], y[:, ::stepi], color="C1", alpha=.45, linewidth=.35)
    axes[1].set_aspect("equal", adjustable="box"); axes[1].set_title("x/y geometry (sampled grid lines)")
    axes[2].hist(bed.ravel(), bins=100); axes[2].set_yscale("log"); axes[2].set_title("bed value distribution (all cells)")
    axes[3].scatter(x.ravel()[::max(1,x.size//100000)], bed.ravel()[::max(1,bed.size//100000)], s=.1, alpha=.2)
    axes[3].set_title("bed against x (uniform index sample)"); axes[3].set_xlabel("x")
    if has_chezy:
        ch = arrays["chezy.txt"]
        im = axes[4].imshow(ch, origin="lower", aspect="auto", cmap="viridis")
        axes[4].set_title("chezy.txt: every cell, native 2642x3486")
        fig.colorbar(im, ax=axes[4], shrink=.75)
        vals, counts = np.unique(ch, return_counts=True)
        axes[5].bar([str(v) for v in vals], counts); axes[5].set_yscale("log")
        axes[5].set_title("Chezy values (all cells)"); axes[5].tick_params(axis='x', rotation=45)
    fig.suptitle(name)
    out = HERE / f"{name}-spatial-review.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out


audit = {"method": {
    "numeric_parse": "numpy.loadtxt(float64) over every textual token; ragged/nonnumeric data fail",
    "integrity": "raw-file SHA-256 recomputed by streaming every byte",
    "visualization": "imshow of every field cell (display rasterization may aggregate pixels), all-cell histograms, sampled x/y grid lines",
    "claim_boundary": "machine exhaustive token parsing plus whole-field visual review; not a claim that a person/LLM separately eyeballed every numeric literal",
}, "source_evidence": {
    "manual_friction_format": {
        "path": "models/XBeach/raw/manuals/readthedocs/en/latest/_sources/numerical_implementation.rst.txt",
        "sha256": digest(REPO / "models/XBeach/raw/manuals/readthedocs/en/latest/_sources/numerical_implementation.rst.txt"),
        "lines": "1253-1259",
        "observation": "bedfricfile is documented as spatially varying and in the same format as bathymetry",
    },
    "manual_friction_units": {
        "path": "models/XBeach/raw/manuals/readthedocs/en/latest/_sources/xbeach_manual.rst.txt",
        "sha256": digest(REPO / "models/XBeach/raw/manuals/readthedocs/en/latest/_sources/xbeach_manual.rst.txt"),
        "lines": "1104-1132",
        "observation": "typical Chezy C is stated in m^(1/2)/s and Manning n in s/m^(1/3)",
    },
    "snapshot_grid_and_friction_reader": {
        "initialize_path": "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/initialize.F90",
        "initialize_sha256": digest(REPO / "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/initialize.F90"),
        "bathymetry_sign_lines": "240-249",
        "bedfric_read_lines": "991-1001",
        "params_path": "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90",
        "params_sha256": digest(REPO / "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90"),
        "grid_param_lines": "150-190",
        "bedfric_param_lines": "680-730",
    },
}, "cases": {}}

for case, names in CASES.items():
    root = BASE / case
    params_path = root / "params.txt"
    params = parse_params(params_path)
    arrays, files = {}, {}
    for name in names:
        arrays[name], files[name] = numeric_file(root / name)
    nx, ny = int(params["nx"]["value"]), int(params["ny"]["value"])
    expected = [ny + 1, nx + 1]
    grid_shapes = {n: files[n]["rows"] == expected[0] and files[n]["columns"] == expected[1] for n in ("bed.dep", "x.grd", "y.grd")}
    relation = {
        "params_sha256": digest(params_path),
        "params_evidence": {k: params[k] for k in ("depfile", "posdwn", "nx", "ny", "xfile", "yfile", "bedfriction")},
        "expected_node_array_shape_ny_plus_1_by_nx_plus_1": expected,
        "bed_x_y_shape_matches_params": grid_shapes,
    }
    if "bedfriccoef" in params: relation["bedfriccoef"] = params["bedfriccoef"]
    if "bedfricfile" in params:
        relation["bedfricfile"] = params["bedfricfile"]
        relation["bedfricfile_shape_matches_grid"] = arrays["chezy.txt"].shape == arrays["bed.dep"].shape
        relation["bedfricfile_shape_observed"] = list(arrays["chezy.txt"].shape)
        active = arrays["chezy.txt"][:ny + 1, :nx + 1]
        av, ac = np.unique(active, return_counts=True)
        relation["snapshot_line_reader_consumed_window"] = {
            "rows": [1, ny + 1], "columns_per_row": [1, nx + 1],
            "unique_values_count_then_value": sorted(zip(ac.tolist(), av.tolist()), reverse=True),
            "observation": "initialize.F90 reads nx+1 values on each of ny+1 records; surplus columns and rows are not assigned to the model array",
        }
    audit["cases"][case] = {"files": files, "params_relation": relation, "grid_geometry": geometry(arrays["x.grd"], arrays["y.grd"]), "figure": plot_case(case, arrays).name}

(HERE / "numeric-audit.json").write_text(json.dumps(audit, indent=2) + "\n")
receipts = []
for case, c in audit["cases"].items():
    for name, f in c["files"].items():
        receipts.append({
            "path": f["path"], "sha256": f["sha256"], "read_status": "complete-machine-parse-and-whole-field-visual-review",
            "scope": audit["method"]["claim_boundary"], "numeric_tokens_parsed": f["numeric_tokens"],
            "method_artifact": str((HERE / "numeric-audit.json").relative_to(REPO)), "figure": c["figure"],
        })
with (HERE / "numeric-read-receipts.jsonl").open("w") as out:
    for r in receipts: out.write(json.dumps(r) + "\n")
print(json.dumps({"files": len(receipts), "tokens": sum(r["numeric_tokens_parsed"] for r in receipts), "output": str(HERE)}, indent=2))
