---
citation_status: source-needed
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/30-local-python-mesh-install-and-api-check.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: P2 catalog (audit deferred to per-note verification)
---
# Local Python Mesh Install And API Check

Date: 2026-04-13

Purpose:
- record the actual local install status of `OCSMesh` and `oceanmesh`
- record the practical Windows conditions needed to import the Python mesh stacks

## UV Environments

Created local UV virtual environments:
- `E:\AI_ENV\.venvs\ocsmesh`
- `E:\AI_ENV\.venvs\oceanmesh`

Using:
- CPython `3.12.11`

## OCSMesh Result

Install result:
- `ocsmesh` installed successfully with `uv pip install`

Observed imported version:
- `ocsmesh 2.1.0`

Observed core constructor signatures:
- `Raster(path, crs=None, chunk_size=None, overlap=None)`
- `Geom(geom, **kwargs)`
- `Hfun(hfun, **kwargs)`
- `MeshDriver(geom, hfun=None, init_mesh=None, crs=None, engine_name='gmsh', **engine_kwargs)`

Interpretation:
- `OCSMesh` is operational on the current machine
- it is the easiest Python path to run immediately

## oceanmesh Result

### Initial Failure

The first GitHub-source install attempt failed because:
- the build linked against the wrong `vcpkg` root
- the linker could not find `gmp.lib`

Observed bad environment variable:
- `VCPKG_ROOT=C:\Program Files\Microsoft Visual Studio\2022\Professional\VC\vcpkg`

### What Fixed The Linker Problem

Observed working local dependency tree:
- `C:\Users\firesinger\OceanMesh\vcpkg\installed\x64-windows\lib\gmp.lib`
- `C:\Users\firesinger\OceanMesh\vcpkg\installed\x64-windows\lib\mpfr.lib`
- corresponding DLLs under `...\bin`

Working fix:
- set `OCEANMESH_PREFIX=%USERPROFILE%\OceanMesh\vcpkg\installed\x64-windows`

This changed the build to use the correct include/lib paths and the C++ extensions compiled and linked.

### Remaining Install Problem

After the link problem was fixed, the package still failed inside the sandbox during the final UV wheel step with a temporary-file permission error.

Interpretation:
- the `gmp.lib` issue was solved first
- the remaining blocker was a sandboxed temp-directory permission problem during UV's build/editable staging

### Final Install Fix

The package was then installed successfully by:
- copying the source tree to a short local path
- using a short `TMP`, `TEMP`, and `UV_CACHE_DIR`
- setting `OCEANMESH_PREFIX`
- running the editable install outside the sandbox

Installed result:
- `oceanmesh==0+unknown`

### Import Check

For a clean import experience on Windows, one more local fix was added:
- `E:\AI_ENV\.venvs\oceanmesh\Lib\site-packages\sitecustomize.py`

This helper:
- sets `CGAL_BIN` automatically if it is missing
- prepends the same directory to `PATH`

Observed final import result in a fresh process:
- `import oceanmesh` works without manual environment setup
- detected version string: `0+unknown`

Observed import-time requirement:
- `oceanmesh` asserts that `CGAL_BIN` is set on Windows

Observed imported API:
- `Region(extent, crs)`
- `Shoreline(shp, bbox, h0, crs='EPSG:4326', refinements=1, minimum_area_mult=4.0, smooth_shoreline=True, stereo=False)`
- `distance_sizing_function(shoreline, rate=0.15, max_edge_length=None, coarsen=1.0, crs='EPSG:4326')`
- `feature_sizing_function(shoreline, signed_distance_function, r=3, min_edge_length=None, max_edge_length=None, plot=False, crs='EPSG:4326')`
- `enforce_mesh_gradation(grid, gradation=0.15, crs='EPSG:4326', stereo=False)`
- `generate_mesh(domain, edge_length, **kwargs)`
- `generate_multiscale_mesh(domains, edge_lengths, **kwargs)`
- `write_to_fort14(points, cells, filepath, topobathymetry=None, project_name='Created with oceanmesh', flip_bathymetry=False)`

Interpretation:
- `oceanmesh` is now installed and importable on this machine
- the remaining caveat is only that the installed version string is development-style (`0+unknown`) because it came from a local editable source tree

## Practical Local Conclusion

- `OCSMesh` is fully installable right now
- `oceanmesh` is now fully installed and importable with environment fixes
- for `oceanmesh`, the critical Windows variables are:
  - `OCEANMESH_PREFIX`
  - `CGAL_BIN`
