<<<PAGE 1>>>

## EFDC Model Training

Drew Ackerman, Cardno ENTRIX

September X, 2013

<<<PAGE 2>>>

#### EFDC Model Background

- • Solves the three-dimensional, vertically hydrostatic, free surface, turbulent averaged equations of motions for a variable density fluid
- • Sigma coordinates and Cartesian or curvilinear, orthogonal grid
- • Assumes incompressible flow and hydrostatic pressure distribution with dynamically coupled salinity and temperature transport




<<<PAGE 3>>>

#### EFDC Model Background, Continued

• Simulates:

- • Wetting and drying
- • Simulation of controlled flow structures
- • Vegetation resistance
- • Wave-current boundary layers and wave-induced currents
- • Embedded single port buoyant jet module




<<<PAGE 4>>>

#### EFDC Model Linkage

##### • Provides dynamics for sediment, water quality and toxics fate and transport

###### • Sediment simulations

– Cohesive/non-cohesive, deposition/resuspension, sediment load and bed loads

###### • Water quality

– Eutrophication model, sediment diagenesis

###### • Toxics

– Trace metals/organic hydrocarbons and sediment interactions



<<<PAGE 5>>>

#### EFDC Versions

##### • Tetra Tech version

- • EPA version
- • Original EFDC model by Hamrick
- • Last updated in 2002


##### • Sandia Labs

• Research version

##### • Dynamic Solutions

- • Commercial version with GUI
- • Additional capabilities and support
- • Last updated in 2013




<<<PAGE 6>>>

#### EFDC Application

##### • Original model

• EFDC (EPA) version

##### • Expanded model

- • Dynamic Solutions (without GUI)
- • DOS window
- • Text Editor




<<<PAGE 7>>>

#### Model Configuration

- • Model developed to support hydrodynamic and water quality simulations

- • Stage, temperature, salinity
- • Nutrient transformations, dissolved oxygen kinetics, and eutrophication


- • Focus of this training is temperature and salinity




<<<PAGE 8>>>

## Model Files



<<<PAGE 9>>>

#### File Types

##### • Model control file

• Describes model and sets up its output

##### • Model grid files

• Defines model grid orientation, elevations

##### • Model boundary/input files

• Characterizes what is entering/leaving model domain



<<<PAGE 10>>>

#### Model Files

EFDC.inp Control primary simulation control file SHOW.inp File controlling screen print WQ3DWC.inp Water quality simulation control file



<<<PAGE 11>>>

#### EFDC Model



<<<PAGE 12>>>

#### Model Grid Files

CELL.inp Grid cell type CELLLT.inp Grid cell type CORNERS.inp Corner coordinates for each cell DXDY.inp Grid cell dimensions LXLY.inp Grid cell orientation



<<<PAGE 13>>>

#### Initial Condition Files

BEDBDN.inp Sediment bed bulk density BEDDDN.inp Sediment bed porosity BEDLAY.inp Sediment bed thickness SALT.inp Salinity concentration SEDB.inp Cohesive sediment in sediment bed SEDW.inp Cohesive sediment in water column TEMP.inp Temperature



<<<PAGE 14>>>

#### Boundary/Input Files

CWQSERxx.inp Water quality input files GWMAP.inp Defines groundwater seepage zones GWSEEP.inp Defines groundwater flow rate PSER.inp Time series tide boundary condition QSER.inp Time series flow SDSER.inp Time series cohesive sediment SNSER.inp Time series non-cohesive sediment SSER.inp Time series salinity TSER.inp Time series temperature



<<<PAGE 15>>>

#### Boundary/Input Files, Continued

WQALGG.inp Algal dynamics WQBNENFLX.inp Time series benthic flux WQBENMAP.inp Mapping info for spatial benthic fluxes WQSETL.inp Water quality settling rates WQWCMAP.inp Water quality kinetic zones WSER.inp Time series wind



<<<PAGE 16>>>

#### General File Comments

- • Discuss relevant files to hydrodynamic simulation and model grid
- • Free format


• Sensitive to integer/real numbers

##### • View in Notepad++



<<<PAGE 17>>>

## Model Grid



<<<PAGE 18>>>

#### Model Grid Overview

##### • Need detailed information describing model cells

• Cell orientation and where it is in the world

##### • Current grid has one open boundary to east defining oceanic conditions



<<<PAGE 19>>>

#### Grid Development

##### • Three options

- • GRIDGEN
- • Dynamic Solutions
- • Delft3d




<<<PAGE 20>>>

#### GEFDC

##### • Original model grid generation program

- • Define boundary points
- • Define model grid type
- • Specify grid relaxation parameters
- • Cartesian, curvilinear


##### • DOS and text based

• Outputs image of grid in DXF format



<<<PAGE 21>>>

#### Dynamic Solutions

- • More flexible grid generation

• Cartesian, curvilinear

- • Use geographic files to help define grid boundary
- • Can import other grids to EFDC grids


• Deflt RGFGrid, Grid95, SEAGRID



<<<PAGE 22>>>

#### Delft3d RGFGrid

- • Intuitive GUI
- • Good online support
- • Active user community
- • Online training videos




<<<PAGE 23>>>

#### LTPR EFDC Model Grid

##### • Lower Tar Pamlico River

- • 6 sigma coordinate layer models
- • 593 horizontal cells




<<<PAGE 24>>>

#### LTPR EFDC Model Grid



<<<PAGE 25>>>

## Grid Files



<<<PAGE 26>>>

#### EFDC Grid Files

##### • Model consists of a series of quadrilateral cells

• Orthogonal and curvilinear

##### • Files define cells

- • Location
- • Orientation
- • Shape


CELL.inp Grid cell type CELLLT.inp Grid cell type CORNERS.inp Coordinates for each cell DXDY.inp Grid cell dimensions LXLY.inp Grid cell orientation



<<<PAGE 27>>>

#### CELL.inp



<<<PAGE 28>>>

1 0

1 1

- 1
- 2


1 2 3 4 5 6 7 8 9

- 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0

- 12 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9

- 11 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9

- 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 9 9 5 9 9 5 5 5 5 5 5 5 5 5 5 5 5 5

- 9 0 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 8 0 9 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7 0 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 5 5 5 5 5 6 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 5 5 5 5 5 5 5 5 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 9 9 9 9 9 9 9 9 9 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

1 3

1 4

1 5

1 6

1 7

1 8

- 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0

35 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 34 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 33 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 9 9 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 32 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 31 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 9 9 9 9 9 9 9 9 9 5 9 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 30 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 9 9 5 5 5 5 5 5 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 29 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 5 5 5 5 5 5 5 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 28 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 5 5 5 5 5 5 5 5 5 5 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 27 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 9 5 5 5 9 9 9 9 9 9 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 26 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 9 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 25 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 24 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 23 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 22 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 21 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 5 5 5 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 20 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 19 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 18 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 5 5 5 5 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 17 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 5 5 5 5 5 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 16 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 5 5 5 5 5 5 5 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 15 0 0 0 0 0 0 0 0 0 0 0 0 9 9 9 0 0 0 0 0 9 9 9 9 9 9 9 9 9 9 9 5 5 5 5 5 5 5 5 9 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 14 0 0 0 0 0 0 0 9 9 9 9 9 9 5 9 9 9 9 9 9 9 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 13 0 0 9 9 9 9 9 9 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 12 9 9 9 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 11 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 10 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

9 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 8 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 9 5 5 5 5 5 5 5 5 5 5 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 7 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 6 5 5 5 5 5 9 9 5 5 5 5 9 9 5 5 5 5 5 5 5 5 5 9 9 9 5 5 9 5 9 9 9 9 9 9 9 9 9 9 9 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 5 5 5 5 5 9 9 9 9 9 9 9 9 9 9 9 9 5 5 9 9 9 9 9 0 9 9 9 9 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 4 9 5 5 5 9 0 0 0 0 0 0 0 0 0 0 9 9 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 9 9 5 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

- 2 0 9 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0












| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |


i

<<<PAGE 29>>>

#### Grid Numbering



<<<PAGE 30>>>

#### CORNERS.inp



<<<PAGE 31>>>

#### DXDY.inp



<<<PAGE 32>>>

#### LXLY.inp



<<<PAGE 33>>>

## Initial Conditions



<<<PAGE 34>>>

#### Initial Condition Files

- • Specify model conditions at start of the simulation
- • Focus on salinity and temperature


BEDBDN.inp Sediment bed bulk density BEDDDN.inp Sediment bed porosity BEDLAY.inp Sediment bed thickness SALT.inp Salinity concentration SEDB.inp Cohesive sediment in sediment bed SEDW.inp Cohesive sediment in water column TEMP.inp Temperature



<<<PAGE 35>>>

#### Model Layers

##### • Sigma (σ-stretched) layers

- • Layers expand and contract
- • Like an accordion


- 1

- 2

- 3

- 4

- 5

- 6


##### • 6 layers defined for the model

• Lowest number on bottom



<<<PAGE 36>>>

#### SALT.inp



<<<PAGE 37>>>

#### TEMP.inp



<<<PAGE 38>>>

## Boundary Files



<<<PAGE 39>>>

#### Boundary/Input Files

ASER.inp Atmospheric condition file CWQSERxx.inp Water quality input files GWMAP.inp Defines groundwater seepage zones GWSEEP.inp Defines groundwater flow rate PSER.inp Time series tide boundary condition QSER.inp Time series flow SDSER.inp Time series cohesive sediment SNSER.inp Time series non-coheisve sediment SSER.inp Time series salinity TSER.inp Time series temperature WQALGG.inp Algal dynamics WQBNENFLX.inp Time series benthic flux WQBENMAP.inp Mapping info for spatial benthic fluxes WQSETL.inp Water quality settling rates WQWCMAP.inp Water quality kinetic zones WSER.inp Time series wind

<<<PAGE 40>>>

## Atmospheric Conditions



<<<PAGE 41>>>

#### Atmospheric Conditions

- • Describe atmospheric conditions
- • Processes affected
- • Heating
- • Dissolved oxygen
- • Rainfall
- • Wet deposition of nutrients
- • Photosynthesis




<<<PAGE 42>>>

#### Atmospheric condition input file: ASER.inp

##### • Define environmental conditions

- • Atmospheric pressure
- • Dry air temperature
- • Relative humidity
- • Rainfall
- • Evaporation
- • Solar radiation
- • Fraction cloud cover




<<<PAGE 43>>>

#### ASER.inp



<<<PAGE 44>>>

#### Wind input file: WSER.inp

##### • Wind conditions

- • Speed
- • Direction




<<<PAGE 45>>>

#### WSER.inp



<<<PAGE 46>>>

## Tidal Boundary



<<<PAGE 47>>>

#### Pressure time series: PSER.inp

- • Define seaward tidal condition at the “open boundary”
- • Three options
- • Define elevations (current model configuration for calibration and validation years)
- • Define model tidal harmonics
- • Use regression models based on stage at Washington (used to set up 2007 and 2008)




<<<PAGE 48>>>

#### Define Elevations

- • Current model configuration
- • Can capture storm surges
- • Need good local monitoring information for simulation period
- • Need time series for entire simulation period
- • Utilize monitoring data to define absolute or relative water surface elevation




<<<PAGE 49>>>

#### PSER.inp

MPSER TCPSER TAPSER RMULADJ ADDADJ

Number of data points Multiplying conversion factor changing the input time units to seconds Additive time adjustment Multiplying conversion Additive conversion



<<<PAGE 50>>>

#### Define Harmonics

- • Modeled data from other sources

• JTides, ACRIC model

- • Estimate tidal harmonics for different constituents

- • M2, S2, N2, K2, O1, K1, Q1, M4, M6
- • http://www.unc.edu/ims/ccats/tides/tides.htm


- • Extrapolate observed stage at Washington to open boundary condition at the estuary mouth

• Based on lag time and distance (Xu et al, 2008)

- • Can model any period once defined


• More computationally efficient



<<<PAGE 51>>>

#### Model Card 14/15



<<<PAGE 52>>>

#### Model Card 17/18



<<<PAGE 53>>>

## Surface Flow Inputs



<<<PAGE 54>>>

#### QSER.inp

- • Flow time series
- • Define flows into/out of model

- • River/stream flows
- • Point sources
- • Return flows


- • 19 identified sources in the model




<<<PAGE 55>>>

#### QSER Flows

- NS = 1, Greenville + GUC WTP Intake
- NS = 2, Chicod Creek flow (cfs)
- NS = 3, Grindle Creek flow (cfs)
- NS = 4, Tranters Creek flow (cfs)
- NS = 5, Greenville WWTP Flow (cfs)
- NS = 6, Washington WWTP Flow (cfs)
- NS = 7, Belhaven WWTP Flow (cfs)
- NS = 8, PCPS WWTP Flow (cfs)
- NS = 9, Chocotowing
- NS = 10, Blounts
- NS = 11, Durham
- NS = 12, South
- NS = 13, Goose
- NS = 14, Bath
- NS = 15, Pungo Creek
- NS = 16, Pantego
- NS = 17, Pungo Canal
- NS = 18, GUC WTP Raw Water Withdrawal Rate (cms)
- NS = 19, GUC WTP Return Rate (cms)


<<<PAGE 56>>>

#### Sources



<<<PAGE 57>>>

#### QSER.inp

MQSER TCQSER TAQSER RMULADJ ADDADJ

Number of data points Multiplying conversion factor changing the input time units to seconds Additive time adjustment Multiplying conversion Additive conversion



<<<PAGE 58>>>

## Groundwater



<<<PAGE 59>>>

#### Groundwater Flows

- • Different flows into model grid
- • Define zones and constant inflow rates


• 4 zones with 2 inflow rates (m/d)



<<<PAGE 60>>>

#### GWMAP.inp



<<<PAGE 61>>>

#### GWSEEP.inp



<<<PAGE 62>>>

## Temperature and Salinity



<<<PAGE 63>>>

#### SSER.inp

MCSER TCCSER TACSER RMULADJ ADDADJ

Number of data points Multiplying conversion factor changing the input time units to seconds Additive time adjustment Multiplying conversion Additive conversion



<<<PAGE 64>>>

#### TSER.inp

MCSER TCCSER TACSER RMULADJ ADDADJ

Number of data points Multiplying conversion factor changing the input time units to seconds Additive time adjustment Multiplying conversion Additive conversion



<<<PAGE 65>>>

## EFDC Input Files



<<<PAGE 66>>>

#### EFDC Control File

- • Main control file: EFDC.inp
- • Controls

- • Grid definitions
- • Inputs
- • Time steps
- • Output
- • Model calibration parameters


- • Arranged in “cards”




<<<PAGE 67>>>



<<<PAGE 68>>>



<<<PAGE 69>>>



<<<PAGE 70>>>



<<<PAGE 71>>>



<<<PAGE 72>>>



<<<PAGE 73>>>



<<<PAGE 74>>>



<<<PAGE 75>>>



<<<PAGE 76>>>



<<<PAGE 77>>>



<<<PAGE 78>>>



<<<PAGE 79>>>



<<<PAGE 80>>>



<<<PAGE 81>>>

## Model Execution



<<<PAGE 82>>>

#### Simulations on Citrix Server

- • Run EFDC model on appserver.ncwater.org server
- • Same log in information as with OASIS modeling




<<<PAGE 83>>>

#### Virtual Desktop

Logging onto the Citrix server allows for virtual desktop access to the model



<<<PAGE 84>>>

#### Virtual Desktop



<<<PAGE 85>>>

#### Model Simulation

Run model from icon on desktop

- • Runs base case model
- • D:\Tar_users\dackerman\EFDCBaseCase




<<<PAGE 86>>>

## Scenario Development



<<<PAGE 87>>>

#### Example Scenarios and Required Input Changes

- • Alteration of conditions for a pre-developed year
- • Development of a new simulation year
- • Simulation of sea level rise
- • Simulation of potential impacts of climate change




<<<PAGE 88>>>

### Alteration of Conditions for a Pre-developed Year

- • Potential model years include 2001, 2003, 2007, 2008
- • Key parameters/factors could be altered

- • Flow
- • Temperature
- • Salinity


- • Files to change


##### • QSER.INP • TSER.INP • SSER.INP



<<<PAGE 89>>>

#### Development of a New Simulation Year

- • Key parameters/factors

• Flow, temperature, salinity, boundary conditions, atmospheric conditions, initial conditions

- • Files to change

• QSER.INP, TSER.INP, SSER.INP, ASER.INP, WSER.INP, PSER.INP, TEMP.INP, SALT.INP, DXDY.INP

- • It will be important to process all data to develop accurate representation of new conditions
- • This will be a significant effort to undertake




<<<PAGE 90>>>

#### Simulation of Sea Level Rise

- • Key parameters/factors

• Boundary conditions, initial conditions

- • Files to change

• TSER.INP, SSER.INP, TEMP.INP, SALT.INP, DXDY.INP, PSER.INP, EFDC.INP

- • Requires changing seawater elevation but also salinity and temperature




<<<PAGE 91>>>

- Simulation of Potential Impacts of Climate Change
- • Potentially hotter/cooler or dryer/wetter conditions
- • Key parameters/factors

• Flow, temperature, salinity, boundary conditions, atmospheric conditions, initial conditions

- • List files to change

• QSER.INP, TSER.INP, SSER.INP, ASER.INP, WSER.INP, PSER.INP, TEMP.INP, SALT.INP, DXDY.INP, EFDC.INP

- • Climate change will impact terrestrial and oceanic conditions


• There will be a large degree of uncertainty and care should be taken with these simulations



<<<PAGE 92>>>

## Model Scenario Runs



<<<PAGE 93>>>

#### Scenario Simulations on Server

Copy EFDCBaseCase directory into a new directory Modify input files in new directory Run simulation in new directory



<<<PAGE 94>>>

## Model Output



<<<PAGE 95>>>

#### EFDC Output

- • EFDC example output file
- • Copy post-processing files (PostProc.exe) into directory where simulation was run
- • Copy post-processing Excel file (PostProcessing.xlsx) onto your computer




<<<PAGE 96>>>

###### Citrix Server

Your local computer



<<<PAGE 97>>>

#### Data from EFDC Output

• Post-process results on server

• Will speed up download times (output files are large)

• Copy “PostProc.exe” into scenario folder on the server

• From \EFDC_PostProcessing



<<<PAGE 98>>>

#### Data from EFDC Output

- • Extract data from salinity and temperature output files

- • 16 stations specified in EFDC.INP file

– Card 87

- • SALTSxx.out and TEMTSxx.out


- • Run the executable file to write a file that averages the top, middle, and bottom two layers (temperature and salinity)
- • Double click on PostProc.exe
- • To generate TempSalt.csv




<<<PAGE 99>>>

#### Example model output

adfdfafafaf

> werwreqwrewre afdafasfdasfdas

> adffasfdasfafdsa



<<<PAGE 100>>>

#### Calculate Percentiles

• Steps to calculate percentiles

- 1. Double click “PostProc.exe”
- 2. Open PostProcessing.xlsx on your computer
- 3. Copy TempSalt.csv from the scenario folder to your computer
- 4. Open TempSalt.csv in EXCEL
- 5. Select columns B through J and copy
- 6. Paste into Cell B1 in the “Data Import” tab
- 7. Results are shown in “Temp Salt Percentiles”




<<<PAGE 101>>>

Open TempSalt.csv in EXCEL and paste those columns into Columns “B” through “J”

PostProcessing.xlsx

Percentiles for the top two layers, middle two layers, and bottom two layers are calculated in the “Temp Salt Percentiles” tab



<<<PAGE 102>>>

#### Temp Salt Percentiles



<<<PAGE 103>>>

## Additional Model Post Processing



<<<PAGE 104>>>

#### Advanced Model Post Processing

- • Requires model user to write post processing code • FORTRAN, C++, BASIC, Python, Matlab
- • Will require more knowledge of model output structure than has been presented here




<<<PAGE 105>>>

## Issues with direct linkage to the OASIS model



<<<PAGE 106>>>

#### Constraints to Linking the LTPR Model to the OASIS Model

- • LTPR model has been set up for four specific years

• Headwater flows, open boundary condition, atmospheric conditions, withdrawals, and discharges

- • OASIS model is a time-series model developed for a longer period
- • Changes to the LTPR model must be hard wired into input files

• Cannot read output files from OASIS directly

- • Running additional years with the LTPR model will require reconfiguring the model boundary and forcing files




<<<PAGE 107>>>

# Questions?



