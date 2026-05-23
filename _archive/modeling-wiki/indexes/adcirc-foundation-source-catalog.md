# ADCIRC Foundation Source Catalog

Collected on 2026-04-12 for the ADCIRC foundation phase.

## Core Documentation

- ADCIRC documentation hub
  - link: https://adcirc.github.io/adcirc/
  - role: current canonical entry point
  - priority: P1

- Getting Started
  - link: https://adcirc.github.io/adcirc/getting_started/index.html
  - role: build and first-run path
  - priority: P1

- Theory and Formulation
  - link: https://adcirc.github.io/adcirc/theory/index.html
  - role: governing equations and numerical framing
  - priority: P1

- Theory PDF, version 44.xx
  - link: https://adcirc.org/wp-content/uploads/sites/2255/2018/11/adcirc_theory_2004_12_08.pdf
  - role: detailed numerical formulation
  - priority: P1

- Input Files reference
  - link: https://adcirc.github.io/adcirc/technical_reference/input_files/index.html
  - role: file anatomy
  - priority: P1

- Parameter Definitions
  - link: https://adcirc.github.io/adcirc/technical_reference/parameter_definitions/index.html
  - role: fort.14 and fort.15 semantics
  - priority: P1

## Examples and Validation Seeds

- Examples index
  - link: https://adcirc.github.io/adcirc/user_guide/examples/index.html
  - role: official test/example map
  - priority: P1

- Official example problems page
  - link: https://adcirc.org/home/documentation/example-problems/
  - role: legacy example inventory
  - priority: P1

- GitHub test suite
  - link: https://github.com/adcirc/adcirc-testsuite
  - role: reproducible examples and regression tests
  - priority: P1
  - local clone: `raw/code/adcirc/adcirc-testsuite`

## Support and Troubleshooting

- Questions and Support
  - link: https://adcirc.github.io/adcirc/questions_and_support/index.html
  - role: official support channels
  - priority: P1

- ADCIRC FAQ
  - link: https://adcirc.org/home/adcirc-faq/
  - role: practical troubleshooting and setup advice
  - priority: P1

## Code and Release Reality

- GitHub model repository
  - link: https://github.com/adcirc/adcirc
  - role: active source of truth for code and docs migration status
  - priority: P1
  - local clone: `raw/code/adcirc/adcirc`

- GitHub releases
  - link: https://github.com/adcirc/adcirc/releases
  - role: version awareness and recent fixes
  - priority: P1

## Tooling and Automation

- Tools page
  - link: https://adcirc.github.io/adcirc/tools/index.html
  - role: official ecosystem map, especially for mesh and preprocessing choices
  - priority: P1

- fort.14 reference
  - link: https://adcirc.github.io/adcirc/technical_reference/input_files/fort14.html
  - role: canonical definition of the combined mesh, bathymetry, and boundary artifact
  - priority: P1

- Boundary conditions
  - link: https://adcirc.github.io/adcirc/user_guide/model_configuration/boundary_conditions/boundary_conditions.html
  - role: official split between open and flux boundaries and where they are defined
  - priority: P1

- Meteorological forcing overview
  - link: https://adcirc.github.io/adcirc/technical_reference/input_files/meteorological_forcing_overview.html
  - role: official map of forcing families and required file types
  - priority: P1

- NWS parameter
  - link: https://adcirc.github.io/adcirc/user_guide/model_configuration/meteorological_forcing/nws_parameters.html
  - role: canonical family map for meteorological forcing selection
  - priority: P1

- NWS13
  - link: https://adcirc.github.io/adcirc/user_guide/model_configuration/meteorological_forcing/nws13.html
  - role: schema definition for the local `JMA-MSM -> NWS13` forcing branch
  - priority: P1

- Grid development and editing
  - link: https://adcirc.github.io/adcirc/user_guide/tips_and_tricks/grid_dev_edit.html
  - role: official guidance on mesh tool choices and whether to reuse or rebuild meshes
  - priority: P1

- Time varying bathymetry
  - link: https://adcirc.github.io/adcirc/technical_reference/input_files/time_varying_bathymetry.html
  - role: advanced terrain option that should remain separate from the default first bathymetry path
  - priority: P2

- ADCIRCpy
  - link: https://github.com/oceanmodeling/adcircpy
  - role: Python automation for input and run management
  - priority: P2

- ASGS operators guide
  - link: https://github-wiki-see.page/m/StormSurgeLive/asgs/wiki/ASGS-Operators-Guide
  - role: operational automation pattern for ADCIRC plus SWAN
  - priority: P2

## Local Workflow Evidence

- `E:\ADCIRC_essential`
  - link: local workflow directory
  - role: confirms mesh, tidal-boundary, run, and `fort.22.nc` wiring for the current local ADCIRC branch
  - priority: P1

- `E:\numerical_models\adcirc\data\wind\jma`
  - link: local converter build directory
  - role: confirms that `JMA_MSM_Converter.exe` is a PyInstaller-packaged Python GUI project
  - priority: P1

- `E:\numerical_models\adcirc\tools\utilities`
  - link: local utilities directory
  - role: preserves notebook-level forcing conversion logic and local grid helper programs
  - priority: P1

- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6`
  - link: local wide-domain mesh development branch
  - role: current strongest local evidence for the tuned `OceanMesh2D` mesh path, including scripts, outputs, runs, and validation artifacts
  - priority: P1

- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\ocsmesh_test`
  - link: local OCSMesh reconstruction branch
  - role: exploratory Python reimplementation track for wide-domain mesh generation
  - priority: P2

- running `JMA_MSM_Converter.exe` GUI
  - link: local executable interface
  - role: confirms the live raw-data acquisition contract for the local `JMA-MSM -> NWS13` branch
  - priority: P1

## Immediate Selection Candidates

- `adcirc-testsuite` quarter annular or inlet example as first baseline
- theory PDF plus parameter definitions as first fort.15 reading pair
- FAQ stability guidance as first failure-pattern seed
- `wide6` as the first local mesh-baseline evidence branch
