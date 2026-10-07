

{0}------------------------------------------------

# **EFDC+ Theory**

**Version 12** 

{1}------------------------------------------------

This document has been published by: DSI LLC

Address: 110 W. Dayton Street #202, Edmonds, WA-98020, USA.

Website: <https://dsi.llc> Email: [info@dsi.llc](mailto:info@dsi.llc) Phone: +1 425 728 8440

Please cite this document as follows:

DSI LLC. 2024. EFDC+ Theory, Version 12. Published by DSI LLC, Edmonds WA. Available at [https://](https://www.eemodelingsystem.com/wp-content/Download/Documentation/EFDC_Theory_Document_Ver_12.pdf) [www.eemodelingsystem.com/wp-content/Download/Documentation/EFDC](https://www.eemodelingsystem.com/wp-content/Download/Documentation/EFDC12_Theory_Document.pdf) Theory Document Ver 12.pdf

{2}------------------------------------------------

## Acknowledgement

DSI, LLC would like to acknowledge the contributions of numerous authors to the Environmental Fluid Dynamics Code Plus (EFDC+) Theory Document. The first version of the Theory Document was published by Dr. John Hamrick in 1992, with the release of the Environmental Fluid Dynamics Code (EFDC). After joining Tetra Tech, Dr. Hamrick added several enhancements to EFDC, along with documentation. Kyeong Park, along with several other authors, added the initial version of the CE-QUAL-ICM (ICM) kinetics for eutrophication, with accompanying documentation. Craig Jones added the initial SEDiment dynamics algorithms as developed by Ziegler, Lick, and Jones (SEDZLJ) implementation, along with separate documentation. Jeff Ji added Rooted Plant Epiphytes Module (RPEM) to EFDC and developed separate documentation, Finally, Scott James contributed to a number of other code and documentation enhancements. Of course, EFDC source code has been publicly available since the early 2000s, so there have been numerous other contributors, resulting in a large number of versions of EFDC.

Over the years, DSI has significantly expanded the original code, now referred to as EFDC+, improving its speed, stability, and accuracy and integrating it into a complete modeling package for hydrodynamics, sediment transport, toxics transport, and eutrophication. DSI has assembled many of the various theory documents and has developed an updated single comprehensive theory document for EFDC+.

Since 2009, the engineers at DSI have been the primary contributors to the updates and maintenance of this document. The primary DSI authors in this effort have been Paul Craig, Thomas Mathis, Tran Duc Kien, Jeffrey Jung, Kester Scandrett, and Anurag Mishra. These authors have brought their in-depth knowledge and careful documentation of all aspects of EFDC+ to the preparation and maintenance of this document, for the benefit of all EFDC+ users.

We would also like to express our acknowledgments to the EFDC+ user community who have provided us with multiple feedbacks that have helped shape EFDC+.

{3}------------------------------------------------

## Contents

|   |     | List of Abbreviations                                                    | ix |
|---|-----|--------------------------------------------------------------------------|----|
| 1 |     | INTRODUCTION                                                             | 1  |
|   | 1.1 | Development History<br>                                                  | 1  |
|   | 1.2 | EFDC+ Advancements<br>                                                   | 2  |
|   | 1.3 | Enhancements to EFDC+ since EEMS10.3<br>                                 | 4  |
|   | 1.4 | EFDC+ Overview<br>                                                       | 5  |
|   | 1.5 | Conclusion<br>                                                           | 7  |
|   |     |                                                                          |    |
| 2 |     | HYDRODYNAMICS                                                            | 8  |
|   |     | 2.0.1<br>Overview<br>                                                    | 8  |
|   | 2.1 | Governing Equations<br>                                                  | 8  |
|   |     | 2.1.1<br>Horizontal and Vertical Coordinate Systems<br>                  | 9  |
|   |     | 2.1.2<br>Basic Hydrodynamic Equations<br>                                | 10 |
|   |     | 2.1.3<br>Equation of State<br>                                           | 13 |
|   |     | 2.1.4<br>Vertical Turbulent Closure<br>                                  | 14 |
|   |     | 2.1.5<br>Horizontal Turbulence Closure<br>                               | 16 |
|   | 2.2 | Boundary Conditions and External Forcings<br>                            | 16 |
|   |     | 2.2.1<br>Bottom Friction<br>                                             | 16 |
|   |     | 2.2.2<br>Vegetation<br>                                                  | 17 |
|   |     | 2.2.3<br>Wind Forcings<br>                                               | 19 |
|   |     | 2.2.4<br>Wave Action<br>                                                 | 21 |
|   |     | 2.2.5<br>Local Wind-Generated Waves<br>                                  | 23 |
|   |     | 2.2.6<br>Harmonic Forcings<br>                                           | 25 |
|   |     | 2.2.7<br>Hydraulic Structures<br>                                        | 26 |
|   |     | 2.2.8<br>Propeller Wash<br>                                              | 30 |
|   | 2.3 | Numerical Solution for the Equations of Motion<br>                       | 32 |
|   | 2.4 | Computational Aspects of the Three Time Level External Mode Solution<br> | 37 |
|   | 2.5 | Computational Aspects of the Three-Time Level Internal Mode Solution<br> | 42 |
|   | 2.6 | Vertical Layering Options<br>                                            | 46 |
|   |     | 2.6.1<br>Standard Sigma (SIG) Approach<br>                               | 46 |
|   |     | 2.6.2<br>Sigma-Zed Approach (SGZ)<br>                                    | 47 |
|   | 2.7 | Near-Field Discharge Dilution and Mixing Zone Analysis<br>               | 48 |
|   |     | 2.7.1<br>Shear-Induced Entrainment<br>                                   | 49 |
|   |     | 2.7.2<br>Forced Entrainment<br>                                          | 50 |
|   |     | 2.7.3<br>Model Implementation<br>                                        | 50 |
|   | 2.8 | Conclusion<br>                                                           | 52 |
|   |     |                                                                          |    |

{4}------------------------------------------------

CONTENTS EFDC+ Theory

| 3 |     | CONSERVATIVE CONSTITUENTS TRANSPORT<br>53                                         |
|---|-----|-----------------------------------------------------------------------------------|
|   | 3.1 | Introduction<br><br>53                                                            |
|   | 3.2 | Basic Equation of Advection-Diffusion Transport<br><br>53                         |
|   | 3.3 | Numerical Solution for Transport Equations<br><br>54                              |
| 4 |     | DYE MODULE<br>57                                                                  |
|   | 4.1 | Decay<br><br>57                                                                   |
|   |     |                                                                                   |
|   | 4.2 | Age of Water<br><br>58                                                            |
| 5 |     | TEMPERATURE AND HEAT TRANSFER<br>59                                               |
|   | 5.1 | Surface Heat Exchange<br><br>60                                                   |
|   |     | 5.1.1<br>Full Heat Balance<br><br>60                                              |
|   |     | 5.1.2<br>COARE 3.6 Bulk Algorithm<br><br>61                                       |
|   |     | 5.1.3<br>Equilibrium Temperature<br><br>62                                        |
|   | 5.2 | Short Wave Radiation<br><br>63                                                    |
|   |     | 5.2.1<br>One-band Light Attenuation Model<br><br>63                               |
|   |     | 5.2.2<br>Two-band Light Attenuation Model<br><br>64                               |
|   |     | 5.2.3<br>Water Quality Linked Light Attenuation<br><br>64                         |
|   | 5.3 | Bed Heat Exchange<br><br>66                                                       |
|   | 5.4 | Ice Formation and Melt<br><br>67                                                  |
|   |     | 5.4.1<br>Heat Balance<br><br>67                                                   |
|   |     | 5.4.2<br>Ice Surface Temperature<br><br>68                                        |
|   |     | 5.4.3<br>Freezing Temperature<br><br>68                                           |
|   |     |                                                                                   |
|   |     | 5.4.4<br>Ice Melt at Air/Water Interface<br><br>69                                |
|   |     | 5.4.5<br>Ice Growth/Melt at Bottom of Ice<br><br>69                               |
|   |     | 5.4.6<br>Solar Radiation at Bottom of Ice<br><br>69                               |
|   | 5.5 | Water Volume Evaporative Losses<br><br>70                                         |
| 6 |     | SEDIMENT TRANSPORT<br>72                                                          |
|   | 6.1 | Introduction<br><br>72                                                            |
|   | 6.2 | Suspended Sediment Transport<br><br>72                                            |
|   |     | 6.2.1<br>Governing Equations for Suspended Sediment Transport<br><br>72           |
|   |     | 6.2.2<br>Numerical Solution<br><br>74                                             |
|   | 6.3 | EFDC Sediment Transport Module<br><br>77                                          |
|   |     | 6.3.1<br>Non-Cohesive Sediment<br><br>77                                          |
|   |     | 6.3.2<br>Cohesive Sediments<br><br>88                                             |
|   |     | 6.3.3<br>Consolidation of Mixed Cohesive and Non-Cohesive Sediment Beds<br><br>92 |
|   | 6.4 | SEDZLJ Sediment Transport Module<br><br>95                                        |
|   |     | 6.4.1<br>Background<br><br>95                                                     |
|   |     |                                                                                   |
|   |     | 6.4.2<br>Bed Shear Stress<br><br>97                                               |
|   |     | 6.4.3<br>Erosion Rate<br><br>98                                                   |
|   |     | 6.4.4<br>Suspended Load<br>104                                                    |
|   |     | 6.4.5<br>Bedload<br>105                                                           |
|   |     | 6.4.6<br>Bed Armoring<br>107                                                      |
| 7 |     | CHEMICAL FATE AND TRANSPORT<br>110                                                |
|   | 7.1 | Development Overview<br>111                                                       |
|   | 7.2 | Basic Equations<br>111                                                            |
|   |     |                                                                                   |

{5}------------------------------------------------

CONTENTS EFDC+ Theory

|    | 7.3  | Chemical Partitioning<br>113                                                        |     |
|----|------|-------------------------------------------------------------------------------------|-----|
|    | 7.4  | Water Column Chemical Transport and Boundary Conditions<br>115                      |     |
|    |      | 7.4.1<br>Numerical Solution to the Water Column Chemical Transport Equations<br>118 |     |
|    | 7.5  | Sediment Bed Chemical Processes<br>121                                              |     |
|    |      | 7.5.1<br>Bedload Transport<br>123                                                   |     |
|    |      | 7.5.2<br>Numerical Solution to the Bed Chemical Process Equations<br>123            |     |
|    | 7.6  | Chemical Loss Terms<br>127                                                          |     |
|    |      | 7.6.1<br>Bulk Degradation<br>127                                                    |     |
|    |      | 7.6.2<br>Biodegradation<br>128                                                      |     |
|    |      | 7.6.3<br>Volatilization<br>128                                                      |     |
| 8  |      | EUTROPHICATION                                                                      | 135 |
|    | 8.1  | Water Column Eutrophication Formulation<br>138                                      |     |
|    |      | 8.1.1<br>Model State Variables<br>138                                               |     |
|    |      | 8.1.2<br>Conservation of Mass Equation<br>141                                       |     |
|    |      | 8.1.3<br>Kinetic Equations for State Variables<br>142                               |     |
|    |      | 8.1.4<br>Settling, Deposition and Resuspension of Particulate Matter<br>182         |     |
|    |      | 8.1.5<br>Method of Solution for Kinetics Equations<br>183                           |     |
|    | 8.2  | Rooted Aquatic Plants Formulation<br>184                                            |     |
|    |      | 8.2.1<br>State Variable Equations<br>184                                            |     |
|    | 8.3  | Sediment Diagenesis and Flux Formulation<br>202                                     |     |
|    |      | 8.3.1<br>Depositional Flux<br>205                                                   |     |
|    |      | 8.3.2<br>Diagenesis Flux<br>207                                                     |     |
|    |      | 8.3.3<br>Sediment Flux<br>207                                                       |     |
|    |      | 8.3.4<br>Silica<br>218                                                              |     |
|    |      | 8.3.5<br>Sediment Temperature<br>220                                                |     |
|    |      | 8.3.6<br>Method of Solution<br>220                                                  |     |
|    | 8.4  | Appendix<br>222                                                                     |     |
|    |      |                                                                                     |     |
| 9  |      | LAGRANGIAN PARTICLE TRACKING                                                        | 230 |
|    | 9.1  | Basic Equations<br>230                                                              |     |
|    | 9.2  | Oil Spill Model<br>233                                                              |     |
|    |      | 9.2.1<br>Wind Drag<br>233                                                           |     |
|    |      | 9.2.2<br>Loss Terms<br>233                                                          |     |
| 10 |      | MARINE HYDROKINETICS                                                                | 234 |
|    | 10.1 | Theory of Marine Hydrokinetics<br>234                                               |     |
|    | 10.2 | Implementation in EFDC+<br>235                                                      |     |
| 11 |      | SHELLFISH FARMING                                                                   | 239 |
|    | 11.1 | Governing Equation<br>239                                                           |     |
|    | 11.2 | Length - Weight Relation<br>240                                                     |     |
|    | 11.3 | Filtration Rate<br>240                                                              |     |
|    |      | 11.3.1<br>Maximum Filtration Rate<br>240                                            |     |
|    |      | 11.3.2<br>Temperature Effect<br>241                                                 |     |
|    |      | 11.3.3<br>Salinity Effect<br>241                                                    |     |
|    |      | 11.3.4<br>Suspended Solids Effect<br>242                                            |     |
|    |      | 11.3.5<br>Dissolved Oxygen (DO) Effect<br>242                                       |     |
|    |      |                                                                                     |     |

{6}------------------------------------------------

| 11.7 | Spawning    |              |  |                            |  |  |  |  |  |  |  |  |  |  |  |  |  |                          |
|------|-------------|--------------|--|----------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--------------------------|
| 11.6 |             |              |  |                            |  |  |  |  |  |  |  |  |  |  |  |  |  |                          |
| 11.5 | Respiration |              |  |                            |  |  |  |  |  |  |  |  |  |  |  |  |  |                          |
| 11.4 |             |              |  |                            |  |  |  |  |  |  |  |  |  |  |  |  |  |                          |
|      |             | Reproduction |  | Ingestion and Assimilation |  |  |  |  |  |  |  |  |  |  |  |  |  | 242<br>243<br>244<br>244 |

CONTENTS EFDC+ Theory

{7}------------------------------------------------

## List of Tables

| 2.1<br>2.2 | Parameters for Different Turbulent Models.<br><br>Values of Different Linear Wind Drag Relationships.<br>                                                                      | 15<br>21 |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| 5.1        | Values of parameters determined by fitting the sum of two exponentials to observations of<br>downward irradiance. Table adapted from<br>Paulson and Simpson<br>(1977).<br>     | 64       |
| 5.2        | List of Evaporation Calculation Methods<br>                                                                                                                                    | 71       |
| 7.1        | Volatilization Input Data<br>134                                                                                                                                               |          |
| 8.1<br>8.2 | Environmental Fluid Dynamics Code Plus (EFDC+)<br>Water Quality State Variables<br>137<br>Basal Metabolism Formulations and Parameter in<br>Integrated Compartment Model or CE |          |
|            | QUAL-ICM (ICM)<br>159                                                                                                                                                          |          |
| 8.3        | Generic and Florida Bay Seagrass Model Parameters for Thalassia and Halodule species                                                                                           | 185      |
| 8.4        | Generic and Florida Bay Seagrass Model Parameters for Epiphytes<br>186                                                                                                         |          |
| 8.5        | Maximum Growth Rate<br>186                                                                                                                                                     |          |
| 8.6        | List of Nutrient Limitation Parameters for the Florida Bay Seagrass Model<br>187                                                                                               |          |
| 8.7        | Epiphyte Light Attenuation Parameter for Florida Bay Seagrass Model<br>190                                                                                                     |          |
| 8.8        | Parameters for Temperature Effect on Growth for Equation<br>8.150<br>191                                                                                                       |          |
| 8.9        | Parameters for Plant Density Effect on Growth for Equation<br>8.152<br>192                                                                                                     |          |
| 8.10       | Parameters for Shoot Respiration in the Florida seagrass model<br>192                                                                                                          |          |
| 8.11       | Parameters for Shoot Mortality of non-respiration loss in the Florida seagrass model<br>193                                                                                    |          |
| 8.12       | Root to Shoot Transport Parameters in Equation<br>8.157<br>194                                                                                                                 |          |
| 8.13       | Parameters for Root Respiration in Equation<br>8.158<br>194                                                                                                                    |          |
| 8.14       | Parameters for Root Mortality in Equation<br>8.159<br>194                                                                                                                      |          |
| 8.15       | EFDC+<br>Sediment Diagenesis Model State Variables<br>203                                                                                                                      |          |
| 8.16       | Parameters Related to Algae in Water Column<br>222                                                                                                                             |          |
| 8.17       | Parameters Related to Zooplankton in Water Column<br>223                                                                                                                       |          |
| 8.18       | Parameters Related to Organic Carbon (OC) in Water Column<br>225                                                                                                               |          |
| 8.19       | Parameters Related to Phosphorus (P) in Water Column<br>226                                                                                                                    |          |
| 8.20       | Parameters Related to Nitrogen (N) in Water Column<br>227                                                                                                                      |          |
| 8.21       | Parameters Related to Silica (SiO2) in Water Column<br>228                                                                                                                     |          |
| 8.22       | Parameters Related to Carbonaceous Oxygen Demand (COD) and Dissolved Oxygen (DO)                                                                                               |          |
|            | in Water Column<br>228                                                                                                                                                         |          |
| 8.23       | Parameters Related to Total Active Metals (TAM) and Fecal Coliform Bacteria in Water                                                                                           |          |
|            | Column<br>229                                                                                                                                                                  |          |
| 8.24       | Assignment of Water Column Particulate Organic Matter (POM) to Sediment G Classes                                                                                              |          |
|            | used in (Cerco and Cole,<br>1994)<br>229                                                                                                                                       |          |
| 8.25       | Sediment Burial Rates (W) Used in (Cerco and Cole,<br>1994)<br>229                                                                                                             |          |

{8}------------------------------------------------

## List of Figures

| 1.1<br>1.2 | Overview of EFDC+ development history<br><br>Primary Modules of the<br>EFDC+<br>Model.<br>                 | 2<br>6 |
|------------|------------------------------------------------------------------------------------------------------------|--------|
| 2.1        | Conceptual Overview of the<br>EFDC+<br>Model.<br>                                                          | 9      |
| 2.2        | The Stretched Vertical Coordinate System.<br>                                                              | 10     |
| 2.3        | Conceptual Framework for Vegetation.<br>                                                                   | 18     |
| 2.4        | Conceptual Framework for Wind-Generated Waves.<br>                                                         | 24     |
| 2.5        | Diagrams for propeller wash-induced momentum (a) coupling with an EFDC+ model grid                         |        |
|            | cell and (b) splitting over vertical water layers.<br>                                                     | 32     |
| 2.6        | Free Surface Displacement Centered Horizontal Grid.<br>                                                    | 33     |
| 2.7        | U-centered grid in the horizontal (x, y) plane.<br>                                                        | 41     |
| 2.8        | U-centered Grid in the Vertical<br>(x,z)<br>Plane.<br>                                                     | 42     |
| 2.9        | An Illustration of<br>EFDC+<br>Layering Options for a Model with<br>K<br>=<br>10.<br>(a)<br>Standard Sigma |        |
|            | (SIG), (b)<br>Sigma Zed (SGZ)-Specified Bottom, and (c)<br>SGZ-Uniform Layering.<br>                       | 47     |
| 2.10       | Near field Jet Plume mixing.<br>                                                                           | 49     |
| 3.1        | S-centered Grid in the Vertical<br>(x,z)-Plane<br>                                                         | 54     |
| 3.2        | Sigma Coordinate and Variable Center (Ji,<br>2008).<br>                                                    | 55     |
| 5.1        | Conceptual Framework for Temperature.<br>                                                                  | 59     |
| 6.1        | Structure of the<br>Environmental Fluid Dynamics Code (EFDC)<br>Sediment Transport Model.                  | 73     |
| 6.2        | Structure of the SEDZLJ Sediment Transport Model.<br>                                                      | 73     |
| 6.3        | Conceptual Framework for<br>EFDC<br>Sediment Transport Module.<br>                                         | 77     |
| 6.4        | Critical Shield's shear velocity and settling velocity as a function of sediment grain size.<br>           | 80     |
| 6.5        | Schematic of the SEDFlume Apparatus.<br>                                                                   | 97     |
| 6.6        | SEDFlume Data for Conowingo Reservoir (DNR Maryland).<br>                                                  | 98     |
| 6.7        | Critical Shear Stresses for Erosion and Suspension of Quartz Particles.<br>101                             |        |
| 6.8        | Results from Flume Measurements of Suspended Load and Bedload (Guy et al.,<br>1966).<br>103                |        |
| 6.9        | Sample Probability Distributions for Cohesive and Non-Cohesive Particles.<br>105                           |        |
| 6.10       | Diagram of SEDflume Layering System.<br>108                                                                |        |
| 6.11       | Erosion Rates Versus Particle Size and Shear Stress for a Bulk Density of 1.9 g/cm2<br>, adapted           |        |
|            | from<br>Roberts et al.<br>(1998) by<br>James et al.<br>(2010).<br>109                                      |        |
| 7.1        | Conceptual Model of Chemical Fate and Transport in<br>EFDC+.<br>110                                        |        |
| 7.2        | Linkage Between Hydrodynamic, Sediment Transport, and Chemical Fate and Transport                          |        |
|            | Model.<br>111                                                                                              |        |
| 7.3        | Covar Method (1976).<br>131                                                                                |        |
| 8.1        | Structure of the<br>EFDC+<br>Water Quality Model.<br>136                                                   |        |

{9}------------------------------------------------

LIST OF FIGURES EFDC+ Theory

| 8.2 | Schematic Diagram of<br>EFDC+<br>Water Quality Model Structure.<br>138                                           |
|-----|------------------------------------------------------------------------------------------------------------------|
| 8.3 | Interaction of Zooplankton with Eutrophication components.<br>139                                                |
| 8.4 | KMV<br>=<br>0.25m/s<br>Velocity limitation function for (Option 1) the Monod equation where                      |
|     | and<br>KMV min<br>=<br>0.15m/s, and (Option 2) the 5-parameter logistic function where<br>a<br>=<br>1.0,         |
|     | b<br>=<br>12.0,<br>c<br>=<br>0.3,<br>d<br>=<br>0.35, and<br>e<br>=<br>3.0 (high velocities are limiting).<br>150 |
| 8.5 | a) Macrophytes grow in vertical columns from bottom upwards and its impact on flow                               |
|     | velocity. b) Plan view of macrophyte's impact on flow velocity<br>152                                            |
| 8.6 | Sediment Layers and Processes Included in Sediment Process Model<br>204                                          |
| 8.7 | Schematic Diagram for Sediment Process Model<br>205                                                              |
| 8.8 | Benthic stress (a) and its effect on particle mixing (b) as a function of overlying water                        |
|     | column<br>Dissolved Oxygen (DO)<br>concentration.<br>212                                                         |

{10}------------------------------------------------

## <span id="page-10-0"></span>List of Abbreviations

<span id="page-10-6"></span>*C* Carbon

<span id="page-10-22"></span>*CH*<sup>4</sup> Methane

<span id="page-10-20"></span>*CO*<sup>2</sup> Carbon dioxide

<span id="page-10-18"></span>*Fe* Iron

<span id="page-10-23"></span>*FeS* Iron monosulfide

<span id="page-10-19"></span>*Mn* Manganese *N* Nitrogen

<span id="page-10-9"></span><span id="page-10-7"></span>*NH*<sup>+</sup> <sup>4</sup> Ammonium

<span id="page-10-12"></span>*NO*<sup>−</sup> <sup>2</sup> Nitrite

<span id="page-10-10"></span>*NO*<sup>−</sup> <sup>3</sup> Nitrate *O* Oxygen

<span id="page-10-11"></span><span id="page-10-8"></span>*P* Phosphorus

<span id="page-10-13"></span>*PO*−<sup>3</sup> 4 Phosphate

<span id="page-10-2"></span>*R<sup>q</sup>* Richardson Number

<span id="page-10-3"></span>*R<sup>w</sup>* Wave Reynolds Number

<span id="page-10-17"></span><span id="page-10-16"></span>*SO*−<sup>2</sup> 4 Sulfate *S* − 2 Sulfide *SiO*<sup>2</sup> Silica

<span id="page-10-14"></span><span id="page-10-4"></span><span id="page-10-1"></span>2D two-dimensional 3D three-dimensional

<span id="page-10-21"></span>BOD Biological Oxygen Demand

<span id="page-10-24"></span>CFD Computational Fluid Dynamics

<span id="page-10-5"></span>chl *a* Chlorophyll *a*

<span id="page-10-15"></span>COD Chemical Oxygen Demand

{11}------------------------------------------------

List of Abbreviations EFDC+ Theory

<span id="page-11-27"></span>CSOD Carbonaceous Sediment Oxygen Demand

<span id="page-11-3"></span>DO Dissolved Oxygen

<span id="page-11-13"></span>DOC Dissolved Organic Carbon DON Dissolved Organic Nitrogen

<span id="page-11-20"></span><span id="page-11-18"></span>DOP Dissolved Organic Phosphorus

<span id="page-11-4"></span>DSI DSI, LLC

<span id="page-11-10"></span>EE EFDC+ Explorer

<span id="page-11-12"></span>EEMS EFDC+ Explorer Modeling System EFDC Environmental Fluid Dynamics Code

<span id="page-11-2"></span><span id="page-11-0"></span>EFDC+ Environmental Fluid Dynamics Code Plus

<span id="page-11-11"></span>EPA Environmental Protection Agency

<span id="page-11-26"></span>ferric oxide *Fe*2*O*3(*s*)

<span id="page-11-1"></span>ICM Integrated Compartment Model or CE-QUAL-ICM

<span id="page-11-22"></span>LHS Left Hand Side

<span id="page-11-19"></span><span id="page-11-16"></span>LPOC Labile Particulate Organic Carbon LPON Labile Particulate Organic Nitrogen LPOP Labile Particulate Organic Phosphorus

<span id="page-11-21"></span><span id="page-11-7"></span>LPT Lagrangian Particle Tracking

<span id="page-11-8"></span>MHK Marine and Hydro-Kinetic

<span id="page-11-14"></span>MPDATA Multidimensional Positive Definite Advection Transport Algorithm

<span id="page-11-6"></span>MPI Message Passing Interface

<span id="page-11-9"></span>NetCDF Network Common Data Form

<span id="page-11-28"></span>NSOD Nitrogenous Sediment Oxygen Demand

<span id="page-11-17"></span><span id="page-11-15"></span>OC Organic Carbon ON Organic Nitrogen

<span id="page-11-5"></span>OpenMP Open Multi-Processing

<span id="page-11-25"></span><span id="page-11-24"></span><span id="page-11-23"></span>PO4d Dissolved Phosphate as Phosphorus PO4p Sorbed Phosphate as Phosphorus PO4t Total Phosphate as Phosphorus

{12}------------------------------------------------

List of Abbreviations EFDC+ Theory

<span id="page-12-18"></span><span id="page-12-16"></span><span id="page-12-7"></span>POC Particulate Organic Carbon POM Particulate Organic Matter PON Particulate Organic Nitrogen POP Particulate Organic Phosphorus

<span id="page-12-17"></span><span id="page-12-15"></span>RHS Right Hand Side

<span id="page-12-4"></span>RPEM Rooted Plant and Epiphyte Model

<span id="page-12-9"></span>RPOC Refractory Particulate Organic Carbon RPON Refractory Particulate Organic Nitrogen

<span id="page-12-11"></span><span id="page-12-10"></span>RPOP Refractory Particulate Organic Phosphorus

<span id="page-12-3"></span>SEDZLJ SEDiment dynamics algorithms as developed by Ziegler, Lick, and Jones

<span id="page-12-1"></span>SGZ Sigma Zed

<span id="page-12-12"></span>SiA Dissolved Available Silica

<span id="page-12-0"></span>SIG Standard Sigma

<span id="page-12-13"></span>SiP Particulate Biogenic Silica

<span id="page-12-2"></span>SNL-EFDC Sandia National Laboratory version of EFDC

<span id="page-12-8"></span>SOD Sediment Oxygen Demand

<span id="page-12-14"></span>TAM Total Active Metals

<span id="page-12-19"></span>TMDL Total Maximum Daily Load

<span id="page-12-5"></span>TSS Total Inorganic Suspended Solids

<span id="page-12-6"></span>W2 CE-QUAL-W2

{13}------------------------------------------------

## <span id="page-13-0"></span>Chapter 1

## INTRODUCTION

Environmental Fluid Dynamics Code Plus [\(EFDC+\)](#page-11-0) is a surface water modeling system encompassing one-, two- and/or three-dimensional hydrodynamics and water column constituent transport. The hydrodynamics are internally coupled using an integrated, single source code implementation to multiple modules (including sediment erosion/deposition, propeller wash, chemical fate and transport, eutrophication kinetics, sediment diagenesis, particle tracking and oil spill). [EFDC+](#page-11-0) and its predecessor, [EFDC](#page-11-2) has been used worldwide in support of environmental assessment, management and regulatory requirements for hundreds of water bodies such as rivers, lakes, reservoirs, wetlands, estuaries, and coastal ocean regions.

## <span id="page-13-1"></span>1.1. Development History

[EFDC+](#page-11-0) is based on the public-domain, open-source version of [EFDC](#page-11-2) [\(Hamrick,](#page-261-3) [1992\)](#page-261-3) originally developed at the Virginia Institute of Marine Science (VIMS) and School of Marine Science of The College of William and Mary, by Dr. John M. Hamrick beginning in 1988. The historical evolution of [EFDC+](#page-11-0) has to a great extent been application driven by a diverse group of modelers in the academic, governmental, and private sectors, as highlighted in Figure [1.1.](#page-14-1)

Since 2000, [DSI, LLC \(DSI\)](#page-11-4) has provided ongoing enhancement and development to EFDC for various surface water, sediment transport, and water quality projects. This includes adding multiple new features based on the theory described in this document. DSI's improvements to the [EFDC](#page-11-2) code are so extensive that in 2016, the [DSI](#page-11-4) version of EFDC was renamed as [EFDC+.](#page-11-0)

{14}------------------------------------------------

<span id="page-14-1"></span>Fig. 1.1. Overview of EFDC+ development history

#### <span id="page-14-0"></span>1.2. EFDC+ Advancements

[EFDC+](#page-11-0) reflects the following key enhancements over [EFDC:](#page-11-2)

- [Open Multi-Processing \(OpenMP\)](#page-11-5) Multithreading: Integration of [OpenMP](#page-11-5) into [EFDC+](#page-11-0) provides vastly improved model run times. The Intel® [OpenMP](#page-11-5) Runtime Library binds [OpenMP](#page-11-5) threads to physical processing units. [EFDC+](#page-11-0) typically produces run times up to four times faster on a six-core processor than the conventional single-threaded [EFDC](#page-11-2) model.
- Dynamic Memory Allocation: Dynamic memory allocation eliminates the need to re-compile [EFDC](#page-11-2) for distinct applications. Previously, due to the limitations of Fortran 77, different maximum array sizes were required to specify computational grid domain and time series input data sets. Dynamic allocation also helps mitigate array indexing errors and provides better traceability for source code development and testing.
- Domain Decomposition and [Message Passing Interface \(MPI\):](#page-11-6) Domain decomposition in [EFDC+](#page-11-0) can significantly increase the model execution time. This is accomplished by splitting up the domain of a model into several smaller ones, referred to as subdomains [\(Fainchtein,](#page-260-0) [2014\)](#page-260-0). Each subdomain executes like a traditional [EFDC+](#page-11-0) run, except that each subdomain exchanges information with its neighboring subdomain at each time step [\(Gropp et al.,](#page-261-4) [2014\)](#page-261-4). This information exchange is accomplished by leveraging Intel's version of [MPI](#page-11-6) to communicate between domains.
- Sigma Zed [\(SGZ\)](#page-12-1) Layering: [EFDC+](#page-11-0) avoids the pressure gradient errors that occur in model simulations of steep changes in bed elevation by using the [SGZ](#page-12-1) layering option. Unlike the original [EFDC,](#page-11-2)

{15}------------------------------------------------

which uses a Sigma [\(SIG\)](#page-12-0) coordinate transformation in the vertical direction and the same number of layers for all cells in the domain, [SGZ](#page-12-1) in [EFDC+](#page-11-0) allows the number of vertical layers to vary over the model domain. This approach is computationally efficient and significantly improves the simulation of density stratification.

- Hydraulic Structures: [EFDC+](#page-11-0) implements equations governing hydraulic structures such as culverts, weirs, sluice gates, and orifices, which differs from the previous approach which only allowed rating curves for hydraulic structures. Additionally, the modeler can specify rules of operations that depend on the model hydrodynamics.
- Enhanced Heat Exchange: [EFDC+](#page-11-0) includes heat exchange options that use equilibrium temperatures for the water and atmospheric interface and spatially variable sediment bed temperatures. The water column concentrations in the eutrophication and sediment transport modules are now coupled with the heat module by including spatially and temporally varying light extinction.
- Ice Formation and Melt: [EFDC+](#page-11-0) includes a heat-coupled ice formation and melt approach to handle cold climates. Surface processes are controlled by the presence or absence of a dynamically computed ice cover.
- Multiple Dyes: [EFDC+](#page-11-0) can simulate an unlimited number of user-defined dye classes, including "Age of Water". Decay and/or growth and settling can be added to any dye class.
- [Lagrangian Particle Tracking \(LPT\):](#page-11-7) An [LPT](#page-11-7) module has been added to [EFDC+,](#page-11-0) which allows simulation of track releases/discharges and mixing studies. Particle settling, decay, and other processes are user configurable. [LPT](#page-11-7) modeling applications include oil spill and emergency response simulations, among many others.
- SEDZLJ Sediment Transport Implementation: [Sandia National Laboratory version of EFDC](#page-12-2) [\(SNL-EFDC\)](#page-12-2) [\(Thanh et al.,](#page-265-0) [2008\)](#page-265-0) contains the [SEDiment dynamics algorithms as developed by](#page-12-3) [Ziegler, Lick, and Jones \(SEDZLJ\)](#page-12-3) [\(Jones and Lick,](#page-261-5) [2000;](#page-261-5) [Ziegler and Lick,](#page-266-0) [1988,](#page-266-0) [1986\)](#page-266-1) for sediment transport computation. [DSI](#page-11-4) further enhanced this model in [EFDC+](#page-11-0) and implemented significant improvements for mass balance, hard bottom bypass, and computational efficiency. The SEDZLJ model is linked to the Chemical Fate and Transport module in [EFDC+.](#page-11-0)
- Propeller Wash Module: [EFDC+](#page-11-0) includes a propeller wash module, which uses a subgrid-based velocity/erosion field tracking to simulate the impacts of ship movement on hydrodynamics and sediment transport.
- Internal Wind Wave Generation: A wind-generated wave module has been added to [EFDC+](#page-11-0) to enable the computation of wind wave-generated bed shear stress on sediment resuspension, with or without wave-induced currents.
- External Wave Model Linkage: Linkage to SWAN [\(SWAN Team,](#page-264-0) [2019\)](#page-264-0) and other external wave models has been simplified and improved in [EFDC+.](#page-11-0)
- [Rooted Plant and Epiphyte Model \(RPEM\)](#page-12-4) Module: An [RPEM](#page-12-4) module was incorporated into a version of [EFDC](#page-11-2) to better simulate water quality interactions with submerged aquatic vegetation such as epiphytic algae and macrophytes [\(Hamrick,](#page-261-6) [2006\)](#page-261-6). This was also subsequently incorporated into [EFDC+.](#page-11-0)

{16}------------------------------------------------

• Shellfish Farming Module: A shellfish farming module was added to [EFDC+](#page-11-0) to simulate the kinetic processes of shellfish, including filtering, ingestion, assimilation, respiration, mortality, and spawning.

- [Marine and Hydro-Kinetic \(MHK\)](#page-11-8) Linkage: [EFDC+](#page-11-0) includes an [MHK](#page-11-8) module for simulating the potential effects of installing and operating turbines and wave energy converters in rivers, tidal channels, ocean currents, and other water bodies. This code is adapted from [SNL-EFDC](#page-12-2) [\(Thanh](#page-265-0) [et al.,](#page-265-0) [2008\)](#page-265-0).
- Run Continuation: If the model crashes or the user wishes to extend the period of simulation, the [EFDC+](#page-11-0) model can be configured as a continuation run, where the model outputs are seamlessly appended to the previous run.
- Spatially and Temporally Varying Fields: Pressure fields, bathymetry, and/or other data such as roughness and vegetation can be dynamically adjusted during the model run in [EFDC+.](#page-11-0) This allows for dredging scenarios and seasonal vegetation patterns. In addition, the boundary conditions can also be input as spatially and temporally varying fields. This helps connect [EFDC+](#page-11-0) with external sources or numerical models.
- [Network Common Data Form \(NetCDF\)](#page-11-9) Output: [EFDC+](#page-11-0) can output results in [NetCDF](#page-11-9) file formats. NetCDF is a community standard for sharing scientific data.
- High-Frequency Output: New output snapshot controls are available to target specific periods for high-frequency output within the standard output frequency.
- Code Streamlining: The code has been converted to Fortran 90 and streamlined for quicker execution times.
- Model Linkages: Users can customize the linkage of model results for use with the Windows-based [EFDC+ Explorer \(EE\)](#page-11-10) graphical pre- and post-processor.

#### <span id="page-16-0"></span>1.3. Enhancements to EFDC+ since EEMS10.3

Enhancement of EFDC+ has since the previous iteration of this theory document for EEMS10.3. Many of the changes do not involve changes to theory, but rather provide improved processes within modules and increased interactions between modules. Improvements have been made to the propeller wash module and the jet and plume module. Some of the significant additions include:

- The ICM kinetics have been rewritten to allow unlimited phytoplankton, periphyton, and macrophyte classes. Additionally, zooplankton has been added as an integrated part of algal dynamics.
- Macrophyte growth capability has been added between layers and for the base of the macrophytes to be in any layer. This allows for floating macrophytes to start at the surface and drape down into the water column.
- "Fast settling" of cohesive classes eroded by propwash have been added to the SEDZLJ sediment transport module. The fast settling classes reflect the process of mass erosion due to a more turbulent and energetic flow field in the propwash plume. These mass eroded sediments then behave differently in the water column than the original sediment classes, as larger chunks settle faster than the discrete particle erosion of more uniform flow patterns. This option was added to address different settling rates of material eroded by mass or bulk erosion of a cohesive bed (i.e., eroded chunks).

{17}------------------------------------------------

- The "fast settling" approach has also been fully integrated into the ChemFate module.
- ChemFate partitioning options have been supplemented. This new feature allows the user to control partitioning on a cell-by-cell basis to better represent spatially varying site conditions. There are now two new files, PARTITIONB.INP and PARTITIONW.INP to allow for spatial varying of toxic partition coefficients in the sediment bed and water column.
- A tropical cyclone module has been added, and the performance of the associated wind field boundary condition option has been improved.
- A user-defined wind drag option has been added.
- Two new open boundary condition types have been added. A free tangential and a zero tangential anti-reflection boundary condition were needed to improve the propagation of waves out of the model domain without reflecting off the open boundary.
- The use of harmonics for defining open boundary water levels for zero tangential and free tangential radiation boundary conditions have been improved to handle non-zero average tidal levels.
- Withdrawal layers have been limited to only active layers. This check was needed because the Sigma-Zed vertical layering approach can use different numbers of layers per cell.
- Horizontal eddy diffusivity and viscosity have been disabled for large aspect ratio cells on the open boundary.
- The NetCDF output has been updated to the latest format, UGRID. It also writes the Lagrangian particle tracking output, which is now a separate file.
- EFDC+ is now linked to the WASP8 water quality model. EFDC+ now writes out the \*.HYD file, allowing WASP to use the hydrodynamics to run the model.

## <span id="page-17-0"></span>1.4. EFDC+ Overview

[EFDC+](#page-11-0) is the most up-to-date, enhanced version of [EFDC,](#page-11-2) which is one of the most popular [three](#page-10-1)[dimensional \(3D\)](#page-10-1) hydrodynamic and water quality models available. The U.S. [Environmental Protection](#page-11-11) [Agency \(EPA\)](#page-11-11) describes the original [EFDC](#page-11-2) as "a state-of-the-art hydrodynamic model that can be used to simulate aquatic systems in one, two, and three dimensions. It has evolved over the past two decades to become one of the most widely used and technically defensible hydrodynamic models in the world." DSI created [EFDC+](#page-11-0) by taking the original version of [EFDC](#page-11-2) and vastly improving its speed, stability, and accuracy. Since 1998, [DSI](#page-11-4) has continually upgraded the model's hydrodynamics and stability while also decreasing run times. [EFDC+](#page-11-0) now far surpasses the features and performance of the legacy code.

[EFDC+](#page-11-0) contains multiple modules and features, which are highlighted in Figure [1.2](#page-18-0) and described in subsequent chapters.

{18}------------------------------------------------

<span id="page-18-0"></span>Fig. 1.2. Primary Modules of the [EFDC+](#page-11-0) Model.

{19}------------------------------------------------

#### <span id="page-19-0"></span>1.5. Conclusion

[EFDC+](#page-11-0) is a surface water modeling system developed by [DSI,](#page-11-4) and is built upon the original [EFDC](#page-11-2) software developed by [Hamrick](#page-261-3) [\(1992\)](#page-261-3). [EFDC+](#page-11-0) includes many new features and bug fixes over the original [EFDC](#page-11-2) code. This document describes the mathematical details of all modules available in [EFDC+.](#page-11-0)

[EFDC+](#page-11-0) executable is available as a part of the [EFDC+ Explorer Modeling System \(EEMS\)](#page-11-12) package available through DSI. For more details about [EEMS,](#page-11-12) please visit [https://www.eemodelingsystem.com/.](https://www.eemodelingsystem.com/) [EFDC+](#page-11-0) source code is open source and is available on our public repository [\(https://github.com/dsi-llc/EFDCPlus\)](https://github.com/dsi-llc/EFDCPlus). We encourage and seek inputs from the user community and partnership with the research community in improving [EFDC+.](#page-11-0)

{20}------------------------------------------------

## <span id="page-20-0"></span>Chapter 2

## HYDRODYNAMICS

#### <span id="page-20-1"></span>2.0.1 Overview

The [EFDC+](#page-11-0) hydrodynamics module simulates near-field plume, wind-generated, and externally linked wave models. In the hydrodynamics module, temperature and salinity may be optionally incorporated to address density effects. The hydrodynamics module is linked to other modules, such as dye/age of water, sediments, chemicals, water quality, [LPT](#page-11-7) and propeller wash, as illustrated in Figure [1.2.](#page-18-0) [EFDC+](#page-11-0) is a coupled model which solves hydrodynamics, transport, and kinetics in an integrated code, thus eliminating the need for external coupling between hydrodynamics and transport modules.

This section is primarily based on [Hamrick](#page-261-3) [\(1992\)](#page-261-3) and [Ji](#page-261-0) [\(2008\)](#page-261-0) with updates from [DSI](#page-11-4) and others. The basic governing equations for the [EFDC+](#page-11-0) hydrodynamics are presented and discussed. The primary sources used for this document are:

- 1. A Three-Dimensional Environmental Fluid Dynamics Computer Code: Theoretical and Computational Aspects [\(Hamrick,](#page-261-3) [1992\)](#page-261-3).
- 2. A User's Manual for the Environmental Fluid Dynamics Computer Code (EFDC), [\(Hamrick,](#page-261-7) [1996\)](#page-261-7).
- 3. A Three-dimensional Hydrodynamic-Eutrophication model (HEM3D): Description of Water Quality and Sediment Processes Submodels [\(Park et al.,](#page-263-2) [1995\)](#page-263-2).
- 4. Theoretical and Computational Aspects of Sediment and Contaminant Transport in the [EFDC](#page-11-2) Model [\(Tetra Tech,](#page-264-1) [2002a\)](#page-264-1).
- 5. Sandia National Laboratories Environmental Fluid Dynamics Code: Sediment Transport User Manual [\(Thanh et al.,](#page-265-0) [2008\)](#page-265-0).

#### <span id="page-20-2"></span>2.1. Governing Equations

The fundamental principles of the hydrodynamic model in [EFDC+](#page-11-0) are the laws of conservation for mass, momentum, and energy for the flows. With the basic assumption that ambient environmental flows are characterized by horizontal length scales which are orders of magnitude greater than their vertical length scales, the formulation of the governing equations begins with the vertically hydrostatic, boundary layer 

{21}------------------------------------------------

form of the turbulent equations of motion for an incompressible, variable density fluid. The governing equations of [EFDC+](#page-11-0) include Navier-Stokes for fluid flow, the advection-diffusion equations for salinity, temperature, dye, toxicants, eutrophication constituents and suspended sediment transport [\(Hamrick and](#page-261-8) [Wu,](#page-261-8) [1997;](#page-261-8) [Hamrick,](#page-261-3) [1992,](#page-261-3) [1996\)](#page-261-7). In the horizontal direction, the equations are presented in the curvilinear coordinate system and [SIG](#page-12-0) or [SGZ](#page-12-1) [\(Craig et al.,](#page-259-1) [2014\)](#page-259-1) transformation (at the bed and at the water surface) for the vertical direction. They are discretized with the finite difference method based on an explicit scheme. Figure [2.1](#page-21-1) shows the basic concepts of the [EFDC+](#page-11-0) model domain.

<span id="page-21-1"></span>Fig. 2.1. Conceptual Overview of the [EFDC+](#page-11-0) Model.

#### <span id="page-21-0"></span>2.1.1 Horizontal and Vertical Coordinate Systems

To accommodate realistic horizontal boundaries, it is convenient to formulate the equations such that the horizontal coordinates, *x* and *y*, are curvilinear and orthogonal.

To provide uniform resolution in the vertical direction, aligned with the gravitational vector and bounded by bottom topography and a free surface permitting long wave motion, a time variable mapping or stretching transformation is desirable. The mapping or stretching is given by

{22}------------------------------------------------

$$z = \frac{z^* + h}{\zeta + h} = \frac{z^* + h}{H} \tag{2.1}$$

where,

*z* is the sigma coordinate (dimensionless),

*z* ∗ is the vertical coordinate with respect to the vertical reference level (datum) (m),

*h* is the water depth below the vertical reference level (m),

ζ is the water surface elevation above the vertical reference level (m), and

*H* is the total depth of water columns (m), defined as or ζ + *h*.

<span id="page-22-1"></span>Figure [2.2](#page-22-1) provides a schematic of the vertical coordinate system in the physical space in the left panel and the sigma space in the right panel.

Fig. 2.2. The Stretched Vertical Coordinate System.

[EFDC+](#page-11-0) supports [SIG](#page-12-0) stretched and [SGZ](#page-12-1) grids for the vertical discretization of the water column. Details of the sigma transformation may be found in [Blumberg and Mellor](#page-258-1) [\(1987\)](#page-258-1); [Hamrick](#page-261-9) [\(1986\)](#page-261-9); [Vinokur](#page-265-1) [\(1974\)](#page-265-1). Details on the [SGZ](#page-12-1) vertical layering options are described in Section [2.6.2](#page-59-0)

#### <span id="page-22-0"></span>2.1.2 Basic Hydrodynamic Equations

Transforming the vertically hydrostatic boundary layer form of the turbulent equations of motion and utilizing the Boussinesq approximation for variable density results in the momentum and continuity equations and the transport equations for salinity and temperature shown in the following equations.

The momentum equation in the *x* direction:

{23}------------------------------------------------

$$\frac{\partial}{\partial t} (m_{x} m_{y} H u) + \frac{\partial}{\partial x} (m_{y} H u u) + \frac{\partial}{\partial y} (m_{x} H v u) + \frac{\partial}{\partial z} (m_{x} m_{y} w u) 
- m_{x} m_{y} f H v - \left( v \frac{\partial m_{y}}{\partial x} - u \frac{\partial m_{x}}{\partial y} \right) H v 
= - m_{y} H \frac{\partial}{\partial x} (g \zeta + p + P_{atm}) - m_{y} \left( \frac{\partial h}{\partial x} - z \frac{\partial H}{\partial x} \right) \frac{\partial p}{\partial z} + \frac{\partial}{\partial x} \left( \frac{m_{y}}{m_{x}} H A_{H} \frac{\partial u}{\partial x} \right) 
+ \frac{\partial}{\partial y} \left( \frac{m_{x}}{m_{y}} H A_{H} \frac{\partial u}{\partial y} \right) + \frac{\partial}{\partial z} \left( \frac{m_{x} m_{y}}{H} A_{v} \frac{\partial u}{\partial z} \right) - m_{x} m_{y} c_{p} D_{p} u \sqrt{u^{2} + v^{2}} + S_{u}$$
(2.2)

The momentum equation in the *y* direction:

$$\frac{\partial}{\partial t} (m_{x}m_{y}Hv) + \frac{\partial}{\partial x} (m_{y}Huv) 
+ \frac{\partial}{\partial y} (m_{x}Hvv) + \frac{\partial}{\partial z} (m_{x}m_{y}wv) + m_{x}m_{y}fHu + \left(v\frac{\partial m_{y}}{\partial x} - u\frac{\partial m_{x}}{\partial y}\right) Hu 
= -m_{x}H\frac{\partial}{\partial y} (g\zeta + p + P_{atm}) - m_{x} \left(\frac{\partial h}{\partial y} - z\frac{\partial H}{\partial y}\right) \frac{\partial p}{\partial z} + \frac{\partial}{\partial x} \left(\frac{m_{y}}{m_{x}}HA_{H}\frac{\partial v}{\partial x}\right) 
+ \frac{\partial}{\partial y} \left(\frac{m_{x}}{m_{y}}HA_{H}\frac{\partial v}{\partial y}\right) + \frac{\partial}{\partial z} \left(\frac{m_{x}m_{y}}{H}A_{v}\frac{\partial v}{\partial z}\right) - m_{x}m_{y}c_{p}D_{p}v\sqrt{u^{2} + v^{2}} + S_{v}$$
(2.3)

The momentum equation in the *z* direction:

<span id="page-23-3"></span><span id="page-23-2"></span><span id="page-23-1"></span><span id="page-23-0"></span>
$$\frac{\partial p}{\partial z} = -gH\frac{\rho - \rho_0}{\rho_0} = -gHb \tag{2.4}$$

The continuity equations (internal and external modes):

$$\frac{\partial}{\partial t} (m_x m_y \zeta) + \frac{\partial}{\partial x} (m_y H u) + \frac{\partial}{\partial y} (m_x H v) + \frac{\partial}{\partial z} (m_x m_y w) = S_h$$
 (2.5)

$$\frac{\partial}{\partial t} (m_x m_y \zeta) + \frac{\partial}{\partial x} (m_y H U) + \frac{\partial}{\partial y} (m_x H V) = S_h$$
(2.6)

where *U* and *V* are the depth-integrated horizontal velocities,

<span id="page-23-5"></span>
$$U = \int_0^1 u dz, \quad V = \int_0^1 v dz$$
 (2.7)

The equation of state for the density of water:

<span id="page-23-4"></span>
$$\rho = \rho \left( p, S, T, C \right) \tag{2.8}$$

The continuity equations for salinity *S* and temperature *T*:

$$\frac{\partial}{\partial t}(mHS) + \frac{\partial}{\partial x}(m_y H u S) + \frac{\partial}{\partial y}(m_x H v S) + \frac{\partial}{\partial z}(mwS) = \frac{\partial}{\partial z}(mH^{-1}A_b \frac{\partial}{\partial z}S) + Q_S$$
 (2.9)

$$\frac{\partial}{\partial t}(mHT) + \frac{\partial}{\partial x}(m_yHuT) + \frac{\partial}{\partial y}(m_xHvT) + \frac{\partial}{\partial z}(mwT) = \frac{\partial}{\partial z}(mH^{-1}A_b\frac{\partial}{\partial z}T) + Q_T$$
 (2.10)

and

{24}------------------------------------------------

*u*, *v* are the horizontal velocity components in the curvilinear coordinates (m/s),

*x*, *y* are the orthogonal curvilinear coordinates in the horizontal direction (m),

*z* is the sigma coordinate (dimensionless),

*t* is time (s),

*mx*, *m<sup>y</sup>* are the square roots of the diagonal components of the metric tensor (dimensionless),

*m* is the Jacobian of the metric tensor determinant (dimensionless), *m* = *mxmy*,

*p* is the physical pressure in excess of the reference density hydrostatic pressure (m<sup>2</sup> /s2 ),

*Patm* is the barotropic pressure normalized by the reference water density (m<sup>2</sup> /s2 ),

ρ*<sup>o</sup>* is the reference water density (kg/m<sup>3</sup> ),

*b* is the buoyancy,

*f* is the Coriolis parameter (1/s),

*A<sup>H</sup>* is the horizontal momentum and mass diffusivity (m<sup>2</sup> /s),

*A<sup>v</sup>* is the vertical turbulent eddy viscosity (m<sup>2</sup> /s),

*c<sup>p</sup>* is the vegetation resistance coefficient (dimensionless),

*D<sup>p</sup>* is the projected vegetation area normal to the flow per unit horizontal area (dimensionless),

*Su*, *S<sup>v</sup>* are the source/sink terms for the horizontal momentum in the *x* and *y* directions, respectively (m<sup>2</sup> /s2 ),

*S<sup>h</sup>* is the source/sink terms for the mass conservation equation (m<sup>3</sup> /s),

*S* is salinity (ppt),

*T* is temperature (◦C),

*C* is [Total Inorganic Suspended Solids \(TSS\)](#page-12-5) (g/m<sup>3</sup> ), and

*U*, *V* are the depth averaged velocity components in the *x* and *y* directions, respectively (m/s).

The vertical velocity, with physical units, in the stretched, dimensionless vertical coordinate *z* is *w*, and is related to the physical vertical velocity *w* <sup>∗</sup> by:

<span id="page-24-0"></span>
$$w = w^* - z \left( \frac{\partial \zeta}{\partial t} + \frac{u}{m_x} \frac{\partial \zeta}{\partial x} + \frac{v}{m_y} \frac{\partial \zeta}{\partial y} \right) + (1 - z) \left( \frac{u}{m_x} \frac{\partial h}{\partial x} + \frac{v}{m_y} \frac{\partial h}{\partial y} \right)$$
(2.11)

where,

*w* is the vertical velocity component in [SIG](#page-12-0) coordinate (m/s) and

*w* ∗ is the physical vertical velocity (m/s).

The pressure *p* is the physical pressure in excess of the reference density hydrostatic pressure, ρ*ogH*(1−*z*) divided by the reference density, ρ*o*. In the momentum equation [\(2.2\)](#page-23-0) and [\(2.3\)](#page-23-1), the momentum source/sink terms *S<sup>u</sup>* and *S<sup>v</sup>* are later modeled as subgrid scale horizontal diffusion. The density ρ is in general a function of temperature *T* and salinity *S* for hydrospheric flows and water vapor for atmospheric flows. Density can be a weak function of pressure but water is treated as an incompressible fluid in the continuity equation under the anelastic approximation [\(Clark and Hall,](#page-259-2) [1991;](#page-259-2) [Mellor,](#page-263-3) [1991\)](#page-263-3).

{25}------------------------------------------------

The buoyancy, *b* as defined in equation [\(2.4\)](#page-23-2) is the normalized deviation of density from the reference value. The continuity equation [\(2.5\)](#page-23-3) has been integrated with respect to *z* over the interval (0,1) to produce the depth integrated continuity equation [\(2.6\)](#page-23-4) using the vertical boundary conditions, *w* = 0, at *z* = (0,1), which follows from the kinematic conditions and equation [\(2.7\)](#page-23-5). It is noted that constraining the free surface displacement to be time independent and spatially constant, yields the equivalent of the rigid lid ocean circulation equations employed by [Semtner Jr](#page-264-2) [\(1974\)](#page-264-2) and equations similar to the terrain following equations used by [Clark](#page-259-3) [\(1977\)](#page-259-3) to model mesoscale atmospheric flow.

### <span id="page-25-0"></span>2.1.3 Equation of State

In case the water density is dependent on temperature and salinity, the UNESCO's equation of state [\(UN-](#page-265-2)[ESCO,](#page-265-2) [1981\)](#page-265-2) reads

$$\rho = 999.842594 + 6.793952 \times 10^{-2}T - 9.095290 \times 10^{-3}T^{2}$$

$$+1.001685 \times 10^{-4}T^{3} - 1.120083 \times 10^{-6}T^{4} + 6.536332 \times 10^{-9}T^{5}$$

$$+ \left( 0.824493 - 4.0899 \times 10^{-3}T + 7.6438 \times 10^{-5}T^{2} \right)$$

$$-8.2467 \times 10^{-7}T^{3} + 5.3875 \times 10^{-9}T^{4} \right) S$$

$$+ \left( -5.72466 \times 10^{-3} + 1.0227 \times 10^{-4}T - 1.6546 \times 10^{-6}T^{2} \right) S^{1.5} + 4.8314 \times 10^{-4}S^{2}$$

$$(2.12)$$

where,

ρ is the water density (kg/m<sup>3</sup> ),

*T* is the water temperature (◦C), and

*S* is the water salinity (ppt).

With the presence of sediment in the water column, the water density and the buoyancy are corrected using a correction factor. The correction factor, per [Tetra Tech](#page-264-3) [\(2007a\)](#page-264-3), for the water density is

$$C_{TSS} = 1 - \sum_{j}^{N} \rho_{s,j} C_j + \sum_{j}^{N} (s_j - 1) \rho_{s,j} C_j$$
 (2.13)

where,

*CT SS* is the correction factor that considers the influence of sediment on water density (dimensionless),

ρ*s*, *j* is the sediment density of the sediment class *j* (kg/m<sup>3</sup> ),

*Cj* is the concentration of the sediment class *j* (g/m<sup>3</sup> ),

*sj* is the specific gravity of the sediment class *j* (dimensionless), and

*N* is the number of sediment classes.

{26}------------------------------------------------

#### <span id="page-26-0"></span>2.1.4 Vertical Turbulent Closure

The system of eight equations from equations [\(2.2\)](#page-23-0) to [\(2.11\)](#page-24-0) provides a closed system for the variables *u*, *v*, *w*, *p*, ζ , ρ, and *C*, provided that the vertical turbulent viscosity and diffusivity, and the source and sink terms are specified. To provide the vertical turbulent viscosity and diffusivity, the second moment turbulence closure model developed by [Mellor and Yamada](#page-263-4) [\(1982\)](#page-263-4) and modified by [Galperin et al.](#page-260-1) [\(1988\)](#page-260-1) can be used. The model relates the vertical turbulent viscosity and diffusivity to the turbulent intensity (*q* 2 ), turbulent length scale (*l*), and [Richardson Number \(](#page-10-2)*Rq*) as shown in the following equations.

The vertical turbulent momentum diffusion coefficient is:

<span id="page-26-1"></span>
$$A_{\nu} = \phi_A A_0 q l, \tag{2.14}$$

where, φ*<sup>A</sup>* is the stability viscosity coefficient and can be defined as:

<span id="page-26-2"></span>
$$\phi_A = \frac{(1 + R_q/R_1)}{(1 + R_q/R_2)(1 + R_q/R_3)} \tag{2.15}$$

Additionally, the following definitions for variables in equations [\(2.14\)](#page-26-1) and [\(2.15\)](#page-26-2) are given as:

$$A_0 = A_1 \left( 1 - 3C_1 - \frac{6A_1}{B_1} \right) = \frac{1}{B_1^{1/3}}$$
 (2.16)

$$\frac{1}{R_1} = 3A_2 \frac{\left(B_2 - 3A_2\right)\left(1 - \frac{6A_1}{B_1}\right) - 3C_1\left(B_2 + 6A_1\right)}{1 - 3C_1 - \frac{6A_1}{B_1}} \tag{2.17}$$

$$\frac{1}{R_2} = 9A_1A_2 \tag{2.18}$$

$$\frac{1}{R_3} = 3A_2 \left[ 6A_1 + B_2 \left( 1 - C_3 \right) \right]. \tag{2.19}$$

The vertical mass diffusion coefficient is defined as:

$$A_b = \rho_K K_0 q l \tag{2.20}$$

where, φ*<sup>K</sup>* is the stability diffusivity coefficient given by

$$\phi_K = \frac{1}{(1 + R_q/R_3)} \tag{2.21}$$

and *K*<sup>0</sup> is the dimensionless coefficient:

$$K_0 = A_2 \left( 1 - \frac{6A_1}{B_1} \right) \tag{2.22}$$

The Richardson number can be calculated as,

$$R_q = \frac{gH}{q^2} \frac{l^2}{H^2} \frac{\partial b}{\partial z} \tag{2.23}$$

where,

{27}------------------------------------------------

*q* 2 is the turbulent intensity (m<sup>2</sup> /s2 ),

*l* is the turbulent length scale (m), and

*R<sup>q</sup>* is the Richardson number.

<span id="page-27-0"></span>[Mellor and Yamada](#page-263-4) [\(1982\)](#page-263-4) specify the constants *A*<sup>1</sup> = 0.92, *B*<sup>1</sup> = 16.6,*C*<sup>1</sup> = 0.08, *A*<sup>2</sup> = 0.74, and *B*<sup>2</sup> = 10.1. However, the values of *R*1, *R*2, *R*<sup>3</sup> calculated by [Galperin et al.](#page-260-1) [\(1988\)](#page-260-1) and [Kantha and Clayson](#page-261-10) [\(1994\)](#page-261-10) are different from [Mellor and Yamada](#page-263-4) [\(1982\)](#page-263-4) as in Table [2.1.](#page-27-0)

Table 2.1. Parameters for Different Turbulent Models.

| Formulation               | K0       | −1<br>R<br>1 | −1<br>R<br>2 | −1<br>R<br>3 |
|---------------------------|----------|--------------|--------------|--------------|
| Mellor and Yamada (1982)  | 0.493928 | 7.846436     | 34.676400    | 6.127200     |
| Galperin et al. (1988)    | 0.493928 | 7.760050     | 34.676440    | 6.127200     |
| Kantha and Clayson (1994) | 0.493928 | 8.679790     | 30.192000    | 6.127200     |
| Kantha (2003)             | 0.490025 | 14.509100    | 24.388300    | 3.236400     |

The stability functions φ*<sup>A</sup>* and φ*<sup>K</sup>* account for the reduced and enhanced vertical mixing or transport in stable and unstable vertically density stratified environments, respectively. The turbulence intensity and the turbulence length scale are determined by a pair of [Mellor and Yamada](#page-263-4) [\(1982\)](#page-263-4) equations:

$$\frac{\partial}{\partial t} \left( mHq^2 \right) + \frac{\partial}{\partial x} \left( Pq^2 \right) + \frac{\partial}{\partial y} \left( Qq^2 \right) + \frac{\partial}{\partial z} \left( mwq^2 \right) 
= \frac{\partial}{\partial z} \left( m\frac{A_q}{H} \frac{\partial q^2}{\partial z} \right) 2m\frac{A_v}{H} \left[ \left( \frac{\partial u}{\partial z} \right)^2 + \left( \frac{\partial v}{\partial z} \right)^2 \right] + 2mgA_b \frac{\partial b}{\partial z} - 2m\frac{Hq^3}{B_1 l} + S_b$$
(2.24)

$$\frac{\partial}{\partial t} \left( mHq^{2}l \right) + \frac{\partial}{\partial x} \left( Pq^{2}l \right) + \frac{\partial}{\partial y} \left( Qq^{2}l \right) + \frac{\partial}{\partial z} \left( mwq^{2}l \right) 
= \frac{\partial}{\partial z} \left[ m\frac{A_{ql}}{H} \frac{\partial}{\partial z} \left( q^{2}l \right) \right] + mlE_{1} \left\{ \frac{A_{v}}{H} \left[ \left( \frac{\partial u}{\partial z} \right)^{2} + \left( \frac{\partial v}{\partial z} \right)^{2} \right] + E_{3}gA_{b} \frac{\partial b}{\partial z} \right\} 
- mE_{2} \frac{Hq^{3}}{B_{1}} \left[ 1 + E_{4} \left( \frac{l}{\kappa Hz} \right)^{2} + E_{5} \left( \frac{l}{\kappa H(1-z)} \right)^{2} \right] + S_{l}$$
(2.25)

<span id="page-27-2"></span><span id="page-27-1"></span>
$$\frac{1}{L} = \frac{1}{H} \left( \frac{1}{z} + \frac{1}{1 - z} \right),\tag{2.26}$$

where,

*E*<sup>1</sup> = 1.8, *E*<sup>2</sup> = 1.0, *E*<sup>3</sup> = 1.8, *E*<sup>4</sup> = 1.33, and *E*<sup>5</sup> = 0.25 are empirical constants,

*S<sup>q</sup>* is the source-sink term for turbulent intensity equation,

*Sl* is the source-sink term for turbulent length scale equation, 

{28}------------------------------------------------

*A<sup>q</sup>* is the vertical turbulent diffusivity for turbulent intensity equation, and

*Aql* is the vertical turbulent diffusivity for turbulent length scale equation.

The vertical diffusivity for turbulence intensity, *A<sup>q</sup>* is set to 0.2*ql* following [Mellor and Yamada](#page-263-4) [\(1982\)](#page-263-4). For stable stratification, [Galperin et al.](#page-260-1) [\(1988\)](#page-260-1) suggested limiting the length scale such that the square root of *[R](#page-10-2)<sup>q</sup>* is less than 0.53.

#### <span id="page-28-0"></span>2.1.5 Horizontal Turbulence Closure

When horizontal turbulent viscosity, *A<sup>H</sup>* and diffusivity are included in the momentum and transport equations, they are determined independently using Smagorinsky's subgrid scale closure formulation [\(Smagorin](#page-264-4)[sky,](#page-264-4) [1963\)](#page-264-4):

$$A_{H} = C_{s} \Delta x \Delta y \sqrt{\left(\frac{\partial u}{\partial x}\right)^{2} + \left(\frac{\partial v}{\partial y}\right)^{2} + \frac{1}{2} \left(\frac{\partial u}{\partial y} + \frac{\partial v}{\partial x}\right)^{2}},$$
(2.27)

where *C<sup>s</sup>* is the horizontal mixing constant referred to as the Smagorinsky coefficient, ∆*x* and ∆*y* are the grid sizes in *x* and *y* directions, respectively. Values of *C<sup>s</sup>* range from 0.1 to 0.2 and has the effect of determining the strength of subgrid scale dissipation [\(Xiao and Cinnella,](#page-266-2) [2019\)](#page-266-2).

[Canuto and Cheng](#page-258-2) [\(1997\)](#page-258-2) recommended a constant value of 0.11. However [Canuto and Cheng](#page-258-2) [\(1997\)](#page-258-2) also advised against the view that this is a universal value. Instead,*C<sup>s</sup>* reflects a combination of physical processes that differ from flow to flow. That *C<sup>s</sup>* is actually a dynamical variable that adjusts itself to each flow has already been observed. [Meyers and Sagaut](#page-263-5) [\(2006\)](#page-263-5) derived the exact expression of *C<sup>s</sup>* which demonstrated *C<sup>s</sup>* depends on both the specific flow and on the grid size, indiciating that it should be treated as an uncertain quantity.

#### <span id="page-28-1"></span>2.2. Boundary Conditions and External Forcings

The vertical boundary conditions for the solution of the momentum equations [\(2.2\)](#page-23-0) and [\(2.3\)](#page-23-1) are based on the specification of the kinematic shear stresses at the free water surface and at the bed.

Vertical boundary conditions for the turbulent kinetic energy and length scale equations are:

$$q^2 = B_1^{2/3} \sqrt{t_{sx}^2 + t_{sy}^2}, \quad l = 0, \text{ at } z = 1$$
 (2.28)

<span id="page-28-3"></span>
$$q^2 = B_1^{2/3} \sqrt{t_{bx}^2 + t_{by}^2}, \quad l = 0, \text{ at } z = 0$$
 (2.29)

Equation [\(2.29\)](#page-28-3) can become inappropriate under several conditions associated with high near bottom sediment concentrations and/or high frequency surface wave activity.

#### <span id="page-28-2"></span>2.2.1 Bottom Friction

At the bed, the stress components are related to the near bed or bottom layer velocity components by the quadratic resistance formulation:

$$\frac{1}{\rho_w} \begin{bmatrix} \tau_{bx} \\ \tau_{by} \end{bmatrix} = C_b \sqrt{u_1^2 + v_1^2} \begin{bmatrix} u_1 \\ v_1 \end{bmatrix}$$
 (2.30)

{29}------------------------------------------------

where,

ρ*<sup>w</sup>* is the density of water,

τ*bx* and τ*by* are the bottom drag due to friction in x and y directions, respectively, and

*u*<sup>1</sup> and *v*<sup>1</sup> are the velocities of water for layer 1 in x and y directions, respectively.

where the subscript 1 denotes bottom layer values. Under the assumption that the near bottom velocity profile is logarithmic at any instant of time, the bottom stress coefficient is given by [Nezu](#page-263-6) [\(1993\)](#page-263-6).

$$C_b = \left[\frac{\kappa}{\ln\left(\Delta_1/2z_0\right) + (\Pi - 1)}\right]^2 \tag{2.31}$$

where,

κ is von Karman constant,

∆<sup>1</sup> is dimensionless thickness of the bottom layer,

*z<sup>o</sup>* = *z<sup>o</sup>* ∗ /*H* is dimensionless roughness height, and

Π is wake strength parameter. Π varies from 0 at low Reynolds numbers to 0.2 with fully turbulent flow. The Π is assumed to be 0.0.

#### <span id="page-29-0"></span>2.2.2 Vegetation

#### 2.2.2.1 Hydrodynamic Feedback

Drag exerted by plants reduces the mean flow within vegetated regions. Vegetation affects the mean velocity, as well as the turbulence intensity and its diffusion. The conceptual framework for vegetation in EFDC+ is shown in Figure [2.3.](#page-30-0)

To capture vegetation effects on flow dynamics, an additional drag term *D<sup>p</sup>* is included in the momentum equations [\(2.2\)](#page-23-0) and [\(2.3\)](#page-23-1) to represent physical obstructions to flow. The vegetation impacts on the turbulent intensity and the turbulent length scale are represented by adding the additional canopy related turbulence terms in the equations [\(2.24\)](#page-27-1) and [\(2.25\)](#page-27-2) as:

<span id="page-29-1"></span>
$$\partial_{t}(m_{x}m_{y}Hq^{2}) + \partial_{x}(m_{y}Huq^{2}) + \partial_{y}(m_{x}Hvq^{2}) + \partial_{z}(m_{x}m_{y}wq^{2})$$

$$= \partial_{z}(m_{x}m_{y}\frac{A_{q}}{H}\partial_{z}q^{2}) - 2m_{x}m_{y}\frac{Hq^{3}}{B_{1}l}$$

$$+ 2m_{x}m_{y}\left(\frac{A_{v}}{H}\left((\partial_{z}u)^{2} + (\partial_{z}v)^{2}\right) + gK_{v}\partial_{z}b + \partial_{p}c_{p}D_{p}\left(u^{2} + v^{2}\right)^{3/2}\right) + Q_{q}$$

$$(2.32)$$

<span id="page-29-2"></span>
$$\partial_{t}(m_{x}m_{y}Hq^{2}l) + \partial_{x}(m_{y}Huq^{2}l) + \partial_{y}(m_{x}Hvq^{2}l) + \partial_{z}(m_{x}m_{y}wq^{2}l) 
= \partial_{z}\left(m_{x}m_{y}\frac{A_{ql}}{H}\partial_{z}(q^{2}l)\right) - m_{x}m_{y}E_{2}\frac{Hlq^{3}}{lB_{1}}\left(1 + E_{4}\left(\frac{l}{\kappa Kz}\right)^{2} + E_{5}\left(\frac{l}{\kappa H(1-z)}\right)^{2}\right) 
+ m_{x}m_{y}l\left(E_{1}\frac{A_{v}}{H}\left((\partial_{z}u)^{2} + (\partial_{z}v)^{2}\right) + E_{3}gK_{v}\partial_{z}b + E_{1}\eta_{p}c_{p}D_{p}(u^{2} + v^{2})^{3/2}\right) + Q_{l}$$
(2.33)

{30}------------------------------------------------

<span id="page-30-0"></span>Fig. 2.3. Conceptual Framework for Vegetation.

In the equations [\(2.32\)](#page-29-1) and [\(2.33\)](#page-29-2), the second term on the last line represents net turbulent energy production by vegetation drag where *c<sup>p</sup>* is a production efficiency factor having a value less than one.

#### 2.2.2.2 Drag Coefficient Estimations

Specification of the drag coefficient is critical to describe the canopy behavior. Factors influencing the characterization of drag coefficient include flow conditions, canopy density and the shape of the canopy elements (Ghisalberti & Nepf, 2004). For submerged and suspended canopies, the finite cylinder has an effect on the drag coefficient. On the other hand, in depth-averaged models of emergent canopies, an increase of the drag coefficients with canopy density was reported by Wu et al. and O'Donncha et al.

An expression for the bulk drag coefficient as a function of dimensionless aquaculture canopy density can be obtained by fitting to the experimental data from (Plew, 2011) and (Scott and O'Donncha, 2019) as:

$$\bar{C}_D = 2.0 - 67ad \tag{2.34}$$

where *ad* is the dimensionless canopy density.

{31}------------------------------------------------

The depth-varying drag coefficients along normalized lengths of the canopy cylinders can be expressed as

$$C_D(\zeta) = \bar{C_D} \left( 1.2 + 0.8\zeta - 0.5\zeta^2 \right) \tag{2.35}$$

where  $\zeta$  is distance from the water surface, normalized by the emerged part of the canopy's length.

#### <span id="page-31-0"></span>2.2.3 Wind Forcings

The influence of wind on hydrodynamics are due to the wind shear stresses exerted on the water surface. At the free surface, the *x* and *y* components of the stress are specified by the wind stress:

$$\frac{1}{\rho_w} \begin{bmatrix} \tau_{sx} \\ \tau_{sy} \end{bmatrix} = C_D \frac{\rho_a}{\rho_w} W_s \begin{bmatrix} W_{sx} \\ W_{sy} \end{bmatrix}$$
 (2.36)

$$W_s = \sqrt{W_{sx}^2 + W_{sy}^2} (2.37)$$

where,

 $W_s$ ,  $W_{sx}$  and  $W_{sy}$  are the wind velocity and x- and y- components of the wind velocity (m/s) at 10 meters above the water surface, respectively,

 $\tau_{sx}$ , and  $\tau_{sy}$  are the surface drag due to wind in x and y directions, respectively,

 $C_D$  is the wind drag coefficient, and

 $\rho_a$  and  $\rho_w$  are air and water densities, respectively.

EFDC+ provides four options for calculating wind drag coefficient.

1. In case of magnitude sheltering and no directional sheltering, the original wind drag coefficient can be calculated as

$$C_{D} = \begin{cases} 3.83111 \times 10^{-5} W_{s}^{-3} - 0.000308715W_{s}^{-2} \\ +0.00116012W_{s}^{-1} + 0.000899602, & W_{s} < 5m/s \\ -5.37642 \times 10^{-6} W_{s}^{3} + 0.000112556W_{s}^{2} \\ -0.000721203W_{s} + 0.00259657, & 5m/s \le W_{s} < 7m/s \\ -3.99677 \times 10^{-7} W_{s}^{2} + 7.32937 \times 10^{-5} W_{s} \\ +0.000726716, & W_{s} \ge 7m/s \end{cases}$$

$$(2.38)$$

2. The second option is a modification of the original EFDC wind drag (Option 1) where the wind speed is calculated as relative to the water velocity.

$$W_{sx} = W_{sx} - u_s \tag{2.39}$$

$$W_{\rm sv} = W_{\rm sv} - v_{\rm s} \tag{2.40}$$

where,  $u_s$  and  $v_s$  are the surface water velocities in x and y directions, respectively.

{32}------------------------------------------------

3. The third option is from the European Centre for Medium-Range Weather Forecasts (ECMWF) which has determined a wind speed-dependent drag coefficient based on the wave age-dependent surface roughness computed with their coupled atmospheric wave model (Hersbach, 2011). The wind speed-dependent formulation is given by

$$C_D = \left[c_1 + c_2 \left(W_s\right)^{p_1}\right] / \left(W_s\right)^{p_2} \tag{2.41}$$

where,  $c_1 = 1.03 \times 10^{-3}$ ,  $c_2 = 0.04 \times 10^{-3}$ ,  $p_1 = 1.48$ , and  $p_2 = 0.21$ .

4. The fourth option is the COARE 3.6 approach based on the bulk momentum and heat flux algorithm described by Fairall et al. (1996), Fairall et al. (2003), and Edson et al. (2013). The approach implemented in EFDC+ is simplified by assuming neutral atmospheric conditions during the simulation. Edson et al. (2013) described the basic equations used under this assumption as follows.

Based on dimensional arguments, the exchange of momentum at the water surface is expected to scale as wind speed squared:

$$\tau = \rho_a C_D U_r^2 \tag{2.42}$$

where,  $\tau$  is the momentum flux or surface stress;  $\rho_a$  is the density of air;  $C_D$  is the transfer coefficient for momentum (i.e., the drag coefficient);  $U_r$  is the wind speed relative to water (i.e., the air-water velocity difference).

Under the assumption of neutral atmospheric conditions,  $C_D$  is computed as a function of the measurement height (z) and the surface roughness  $(z_0)$ :

$$C_D = \left[\frac{\kappa}{\ln(\frac{z}{z_0})}\right]^2 \tag{2.43}$$

The COARE algorithm parameterizes the surface roughness by separating it into two terms:

$$z_0 = z_0^{\text{smooth}} + z_0^{\text{rough}} = \gamma \frac{v}{u_*} + \alpha \frac{u_*^2}{\varrho}$$
 (2.44)

where  $z_0^{\rm smooth}$  accounts for "roughness" of the ocean when it is aerodynamically smooth and the surface stress is supported by viscous shear. The second term  $z_0^{\rm rough}$  accounts for the actual roughness element driven by the wind stress in the form of surface gravity waves (Fairall et al., 1996).  $\gamma$  is the roughness Reynolds number for smooth flow, which has been determined to be 0.11 from laboratory experiments;  $\nu$  is the kinematic viscosity;  $\alpha$  is the Charnock coefficient;  $u_*$  is the friction velocity.

5. There is a new option in EFDC+ version 10.4 that allows a user-defined wind drag relationship in the form of:

$$C_D = \begin{cases} C_1, & W_s \le W_1 \\ C_1 + \frac{C_2 - C_1}{W_2 - W_1} (W_s - W_1), & W_1 < W_s < W_2 \\ C_2, & W_s \ge W_2 \end{cases}$$

$$(2.45)$$

where,

{33}------------------------------------------------

2. HYDRODYNAMICS EFDC+ Theory

*W*<sup>1</sup> and *W*<sup>2</sup> are the lower and upper bounds wind velocities of the linear wind drag relationship, respectively, and

*C*<sup>1</sup> and *C*<sup>2</sup> the lower and upper bounds wind drag coefficients of the linear wind drag relationship, respectively.

<span id="page-33-1"></span>The values for some linear wind drag relationships can be found in Table [2.2.](#page-33-1)

Table 2.2. Values of Different Linear Wind Drag Relationships.

| Formulation               | W1(m/s) | W2(m/s) | C1(10−3<br>) | C2(10−3<br>) |
|---------------------------|---------|---------|--------------|--------------|
| Francis (1951)            | 1       | 25      | 1.3          | 32.5         |
| Sheppard (1958)           | 1       | 20      | 0.914        | 3.08         |
| Wilson (1960)             | 2.8     | 20      | 1.1          | 2.6          |
| Deacon and Webb (1962)    | 1       | 14      | 1.07         | 1.98         |
| Heaps (1965)              | 5       | 19.2    | 0.565        | 2.513        |
| Smith and Banke (1975)    | 6       | 21      | 1.06         | 2.185        |
| Garratt (1977)            | 4       | 21      | 1.018        | 2.157        |
| Large and Pond (1981)     | 10      | 26      | 1.14         | 2.18         |
| Wu (1982)                 | 1       | 80      | 0.865        | 6.0          |
| Anderson (1993)           | 4.5     | 21      | 0.81         | 1.98         |
| Yelland and Taylor (1996) | 6       | 26      | 1.02         | 2.42         |
| Yelland et al. (1998)     | 6       | 26      | 0.926        | 2.346        |

#### <span id="page-33-0"></span>2.2.4 Wave Action

The action of short waves on the field velocity of flow in a large water body could be an important aspect that may not be ignored, especially in estuaries and coastal areas. As is commonly known, both longshore currents and undertow are generated by waves. The asymmetry of wave velocity in its orbital plane is one of the causes of mass transport, such as sediment. Waves may be generated either by local wind or by distant storms with longer time periods. In this document, wind-induced wave theory is presented as applied in [EFDC+.](#page-11-0) In [EFDC+,](#page-11-0) there are two options to include wave effects; 1) by a Sverdrup, Munk and Bretschneider (SMB) wind-wave module inside [EFDC+,](#page-11-0) and 2) by an external Simulating WAves Nearshore (SWAN) wave model [\(SWAN Team,](#page-264-0) [2019\)](#page-264-0).

In the case of waves, apart from the forces from currents, it is also necessary to add the forces from waves for the whole water column, such as radiation stresses or stresses due to the roller in breaking waves [\(Mengguo](#page-263-7) [and Chongren,](#page-263-7) [2003\)](#page-263-7). However, the internal [EFDC+](#page-11-0) wave module only considers radiation stresses, which is the additional wave-induced momentum exerted on the flow field [\(Longuet-Higgins and Stewart,](#page-262-1) [1964\)](#page-262-1):

$$S_{xx} = n\cos^2\theta + n - \frac{1}{2}E\tag{2.46}$$

$$S_{xy} = S_{yx} = (n\cos\theta\sin\theta)E \tag{2.47}$$

$$S_{yy} = n\sin^2\theta + n - \frac{1}{2}E\tag{2.48}$$

{34}------------------------------------------------

where,

*Sxx*, *Sxy*, *Syx*, *Syy* are the components of wave radiation stresses,

*E* is the wave energy (*kg*/*s* 2 ),

$$E = \frac{1}{8}\rho g H_S^2 \tag{2.49}$$

where,

*Hs* is the significant wave height (m),

θ is the radian measure of the wave direction angle with respect to the *x* axis (counterclockwise), and

*k* is the wave number

$$k = \frac{2\pi}{L} \tag{2.50}$$

where

*L* is the wavelength (m),

and *n* is the ratio of group velocity to wave celerity

$$n = \frac{C_g}{C} = \frac{1}{2} \left[ 1 + \frac{2kh}{\sinh(2kh)} \right]$$
 (2.51)

where

*h* is the water depth (m)

In general, the wavelength *L* (m) can be computed by solving the non-linear equation for the dispersion relation shown in equation [\(2.52\)](#page-34-0).

<span id="page-34-0"></span>
$$L = \frac{gT^2}{2\pi} \tanh(kh) \tag{2.52}$$

This dispersion relation can be solved for the wavelength using approximations or iterative methods, for example, [EFDC+](#page-11-0) computes wavelength by using an approximate formula [\(Hunt,](#page-261-14) [1979\)](#page-261-14):

$$L \approx T \sqrt{\frac{1}{d}gh},\tag{2.53}$$

where,

$$d = \gamma + \frac{1}{(1 + 0.6522\gamma + 0.4622\gamma^2 + 0.0864\gamma^4 + 0.0675\gamma^5)},$$
(2.54)

and

$$\gamma = \omega^2 \frac{h}{g} \tag{2.55}$$

{35}------------------------------------------------

where ω is the wave angular frequency (1/s)

$$\omega = \frac{2\pi}{T}.\tag{2.56}$$

The regime of flow is determined through the [Wave Reynolds Number \(](#page-10-3)*Rw*), and the relative bed roughness *r* :

$$R_w = \frac{U_b A}{V}, \quad r = \frac{A}{k_s} \tag{2.57}$$

in which *A* is the semi-orbital excursion, *k<sup>s</sup>* is the Nikuradse equivalent sand grain roughness, and *U<sup>b</sup>* is the wave maximum orbital velocity near the bed.

<span id="page-35-1"></span>
$$A = \frac{H_s}{2\sinh\left(kh\right)} \tag{2.58}$$

$$U_b = A\omega = \frac{\omega H_s}{2\sinh{(kh)}} \tag{2.59}$$

The bottom friction, the bed forms (such as ripples) and the characteristics of bed materials are strongly interdependent in case of wave actions. The friction coefficient due to waves according to [Swart](#page-264-7) [\(1974\)](#page-264-7) is given in equation [\(2.60\)](#page-35-1).

$$f_w = \begin{cases} e^{(5.21r^{-0.19} - 6.0)} & r > 1.57\\ 0.3r & r = 1.57 \end{cases}$$
 (2.60)

#### <span id="page-35-0"></span>2.2.5 Local Wind-Generated Waves

The force applied by wind constitutes an important mechanism which drives the hydrodynamic processes as well as sediment transport in lakes, estuaries, and coastal areas. Wind effects do not only induce the flow current through the vertical boundary conditions at water surface, but also generate surface waves with wave height of several meters. Consequently, the calculation of the total bed shear stress should take the wave factor into account. The conceptual framework for wind-generated waves in EFDC+ is shown in Figure [2.4.](#page-36-0)

Waves with periods of 3 to 25 seconds are primarily caused by winds. Therefore, wind-generated waves play an important role in hydrodynamic modeling. The advantage of this wind-wave sub-model is that it can be easily incorporated into the source code of a hydrodynamic model instead of running a separate wave model. This means that the changes in hydrodynamic parameters are immediately updated in the wave calculations. Additionally, the calculation time is reduced compared to other wave models.

This section presents the details of the theoretical basis and tests of the wind wave module that is incorporated into [EFDC+.](#page-11-0) The mathematical formulae are empirical equations called the SMB (Sverdrup, Munk and Bretschneider) model [\(Ji,](#page-261-0) [2008\)](#page-261-0).

The basic assumptions of the SMB model for wind-generated waves are: a) the duration of wind blowing along one direction is long enough to attain the equilibrium condition, b) the wind speed and water depth are spatially uniform over the fetch. The main wave parameters can be determined including wave height, wave direction and wave period, c) the wave direction is the same as the wind direction, and d) the effects of refraction, diffraction and reflection are not considered. Wave height and period can be defined in the SMB

{36}------------------------------------------------

<span id="page-36-0"></span>Fig. 2.4. Conceptual Framework for Wind-Generated Waves.

model as:

$$H_s = 0.283\alpha \frac{W_s^2}{g} \tanh\left(\frac{0.0125}{\alpha} \left(\frac{gF}{W_s^2}\right)^{0.42}\right)$$
 (2.61)

$$T_p = 7.54\beta \frac{W_s}{g} \tanh\left(\frac{0.077}{\beta} \left(\frac{gF}{W_s^2}\right)^{0.25}\right)$$
 (2.62)

where

$$\alpha = \tanh\left\{0.53 \left(\frac{gH}{W_s^2}\right)^{0.75}\right\}, \text{ and}$$
 (2.63)

$$\beta = \tanh \left\{ 0.833 \left( \frac{gH}{W_s^2} \right)^{0.375} \right\}$$
 (2.64)

where,

*Hs* is the wave height (m),

*T<sup>p</sup>* is the wave period (s),

*H* is the water depth (m),

*Ws* is the wind velocity (m/s), and

*F* is the fetch length (m) from the land boundary to the cell in the upwind direction and is calculated for 16 directions.

{37}------------------------------------------------

## <span id="page-37-0"></span>2.2.6 Harmonic Forcings

The open boundary conditions in [EFDC+](#page-11-0) support a combination of forcings defined as a time series and harmonic forcings. This allows the user to model the situations in estuaries or coastal areas where the influences of tides and river flows or storm surges may occur.

The harmonic representation of a time series ζ (*t*) can be approximated as a combination of sine and cosine functions:

$$\zeta(t) = \zeta_0(t) + a_0 + \sum_{k=1}^{N} \left[ a_k \cos(\omega_k t) + b_k \sin(\omega_k t) \right]$$
 (2.65)

where,

*t* is the time (s),

ζ0(*t*) is the residual signal other than the periodic components (m),

*a*<sup>0</sup> is the mean value of the periodic components (m),

*N* is the number of the harmonic constituents,

*ak*, *b<sup>k</sup>* are the harmonic constant of the constituent *k* (m), and

ω*<sup>k</sup>* is the angular speed of constituent *k* (radians/s).

The angular speed of the constituent *k* can be calculated as

<span id="page-37-1"></span>
$$\omega_k = \frac{2\pi}{T_k} \tag{2.66}$$

where, *T<sup>k</sup>* is the period constituent *k* (s).

Equation [\(2.65\)](#page-37-1) can be also rewritten in another common form as

$$\zeta(t) = \zeta_0(t) + a_0 + \sum_{k=1}^{N} A_k \cos(\omega_k t - \phi_k)$$
 (2.67)

where, *A<sup>k</sup>* is the amplitude of the harmonic constituent *k* (m):

$$A_k = \sqrt{a_k^2 + b_k^2} (2.68)$$

and φ*<sup>k</sup>* is the phase lag the harmonic constituent *k* (radians):

$$f_k = \arctan\left(\frac{b_k}{a_k}\right) \tag{2.69}$$

{38}------------------------------------------------

## <span id="page-38-0"></span>2.2.7 Hydraulic Structures

Hydraulic structures can be modeled in [EFDC+](#page-11-0) by rating curves or hydraulic equations. A rating curve is a lookup table which presents a relationship between the flow rate through the structure and the water heads. Depending on the actual water heads of the structure at a certain time step, the flow rate is determined using the lookup table. [EFDC+](#page-11-0) allows a variety of rating curves in which the flow discharge can be determined from; a) upstream water depth, b) the head difference (between upstream and downstream), c) the head difference and flow accelerations, d) the upstream and downstream water surface elevations, e) upstream water depth for a low chord structure, and f) head difference for a low chord structure.

The last two types of rating curves use low chord structures such as bridges. With the low chord structures, when flows are below the deck, they may be bi-directional, i.e., water can flow from upstream toward downstream or vice-versa. However, once the bridge is overtopped, flows only go from upstream to downstream.

#### 2.2.7.1 Rating Curves

If the flow through a structure is uni-directional, i.e., the flow direction is from upstream to downstream of the structures only. The rating curve is a lookup table which composes of a single column for water head and a corresponding single column for flow rate.

If the flow through a structure is bi-directional, the rating curve is a two-dimensional lookup table where the flow rates can be determined based on both upstream and downstream water surface elevations.

Beside using lookup tables, [EFDC+](#page-11-0) can also simulate internally different types of hydraulic structures. This allows the user to model hydraulic structures rapidly and with ease in [EFDC+.](#page-11-0) The built-in modeling codes for hydraulic structures includes culverts, weirs, sluice gates, and orifices.

### 2.2.7.2 Culverts

Flow rate through a culvert or sluice gate is calculated in [EFDC+](#page-11-0) based on the water levels at both sides of the structure at its configuration. In a tidal region, the water levels on two sides of the structure are constantly changing, which can result in bi-directional flows. The characteristics of flow through a culvert are complicated and are determined by the inlet geometry, slope, shape, size, roughness, approach, and headwater and tailwater conditions. [Dill](#page-260-7) [\(2011\)](#page-260-7) described six different types of culvert flows based on the location of the control section within the culvert and the relative elevations of the headwater, tailwater, and culvert invert and crown elevations. The discharge through a culvert can be expressed as:

<span id="page-38-1"></span>
$$Q = AV = AC\sqrt{RS} = K\sqrt{S} \tag{2.70}$$

where *Q* is the flow discharge (*m* <sup>3</sup>/*s*), *A* is the cross-sectional flow area (*m* 2 ), *R* is the hydraulic radius (*m*), *S* is the culvert slope (fraction), *K* is the conveyance (*m* <sup>3</sup>/*s*), and *C* is the Chezy coefficient ( ´ *m* <sup>0</sup>.5/*s*) which can be calculated by using the Manning's formula

$$C = -\frac{1}{n}R^{\frac{1}{6}} \tag{2.71}$$

where, *n* is Manning's roughness coefficient.

Four distinct conditions arise depending on elevation of the tailwater and headwater compared to the height of the culvert. The handling of these conditions are described in case "a" through "d" below:

{39}------------------------------------------------

- a) If the tailwater is greater than the culvert height or the headwater is greater than 1.5 times the culvert height, the culvert outlet is submerged, and the culvert is assumed to flow full. The slope is estimated as the difference in headwater and tailwater elevation divided by the culvert length, L (m), the conveyance is determined for the full culvert, and discharge is calculated by equation (2.70).
- b) If both the inlet and outlet are not submerged, the critical depth  $(y_c)$  is computed, assuming free flow through the culvert inlet. In this case, it is assumed that the approach velocity is negligible so that total energy at the culvert inlet is equal to the headwater. Thus,

<span id="page-39-0"></span>
$$H_{HW} = y_c + \frac{V_c^2}{2g} \tag{2.72}$$

where,

 $H_{HW}$  is the headwater (m),

 $V_c$  is the critical velocity (m/s),

 $y_c$  is the critical depth (m), and

g is acceleration due to gravity.

In the case of critical flow through the culvert:

<span id="page-39-1"></span>
$$\frac{V_c^2}{2g} = \frac{D}{2} \tag{2.73}$$

where D is the hydraulic depth (m):

$$D = \frac{A}{T} \tag{2.74}$$

and T is the flow top width (m). Combining equations (2.72) and (2.73) yields an expression for the critical depth,

$$y_c = H_{HW} - \frac{D}{2} (2.75)$$

where  $H_{TW}$  is the tailwater (m).

Once the critical depth is determined, the critical velocity  $V_c$ , critical discharge  $Q_{cr}$ , and critical slope  $S_{cr}$  are also calculated. The critical discharge represents the maximum possible flow through the culvert for the given headwater as shown in equation (2.76)

<span id="page-39-2"></span>
$$Q_{cr} = V_c A \tag{2.76}$$

If the culvert slope is greater than the critical slope, the culvert can convey more flow than the inlet will allow. As such, the inlet controls the flow and the discharge is assumed to be equal to the critical discharge  $Q_{cr}$  calculated as equation (2.76).

c) If the culvert slope is less than the critical slope, the control section may be at the culvert outlet or downstream of the culvert. The critical depth is then compared to the tailwater, and if the tailwater is greater than the critical depth, the tailwater elevation is used to determine the flow area and hydraulic radius, and the flow through the culvert is calculated using the equation (2.70).

{40}------------------------------------------------

d) If the tailwater depth is less than the critical depth, but the slope is less than the critical slope, it is assumed that uniform flow will occur within the culvert. In this case potential energy is balanced by head loss due to friction in the culvert and conservation of energy between the control section and inlet can be expressed as;

<span id="page-40-0"></span>
$$H_{HW} = y_n + \frac{V^2}{2\varrho} {2.77}$$

where,  $y_n$  is the normal depth (m) in the culvert and V is the average velocity at the control section. It is also assumed that the approach velocity is negligible, and the slope is small such that the normal depth is approximately equal to the vertical depth.

Equation (2.70) can be re-written as an expression of the velocity head at the control section as;

<span id="page-40-1"></span>
$$V = -\frac{1}{n}R^{\frac{2}{3}}\sqrt{S} \tag{2.78}$$

Combining equations (2.77) and (2.78) yields an equation for the normal depth

<span id="page-40-2"></span>
$$y_n = H_{HW} - \frac{1}{2g} \frac{1}{n^2} R^{\frac{4}{3}} S \tag{2.79}$$

Because R is a function of depth, an adaptive procedure is employed to determine the normal depth. In culverts that experience bi-directional flow, the slope may be adverse or zero. In either case, the assumption of uniform flow is problematic because the water surface slope cannot be equal to the culvert slope. In this case, the water surface slope, as determined from the difference in headwater and tailwater elevations, is used in the equation (2.79).

#### **2.2.7.3** Weirs

A general formula for free flow through a weir can be expressed as

<span id="page-40-3"></span>
$$Q = C_d W \sqrt{2gH_{HW}^3} \tag{2.80}$$

where, W is the width of weir (m) and  $C_d$  is weir discharge coefficient. This coefficient depends on the type of weir (broad crested or sharp-/narrow-crested, ogee), shape of opening (rectangular, triangular, trapezoidal), and other weir parameters.

For submerged flow through a weir, an adjustment factor is applied to equation (2.80) to account for the submergence and is given in equation (2.81) (Villemonte, 1947)

<span id="page-40-4"></span>
$$Q = \left(1 - \frac{H_{TW}}{H_{HW}}\right)^{0.385} C_d W \sqrt{2gH_{HW}^3}$$
 (2.81)

#### 2.2.7.4 Sluice Gates

Flow through a sluice gate can be characterized by two basic parameters: the tranquility of the flow (i.e., subcritical or supercritical flow) and the water depth (i.e., gate is submerged or not). For super-critical weir flow the following equation is used

{41}------------------------------------------------

<span id="page-41-2"></span>
$$Q = C_1 W \sqrt{g \left(\frac{2}{3} H_{HW}\right)^3} \tag{2.82}$$

and for sub-critical weir flow

<span id="page-41-3"></span>
$$Q = C_2 W H_{TW} \sqrt{2g (H_{HW} - H_{TW})}$$
 (2.83)

where,

*C*<sup>1</sup> is the supercritical discharge coefficient,

*C*<sup>2</sup> is the subcritical discharge coefficient,

*HHW* is the headwater (m),

*HTW* is the tailwater (m),

*W* is the width of the gate (m), and

*g* is acceleration due to gravity.

When the water surface is determined to be below the top of the gate, the gate is modeled as a broad crested weir and equation [\(2.80\)](#page-40-3) is used. When the gate is submerged, the appropriate equation for either free sluice flow (supercritical) or submerged orifice flow (subcritical) is applied. To determine the flow through the sluice gate at a given model time step, the headwater is compared to the tailwater.

For free sluice flow the equation [\(2.84\)](#page-41-0) is used:

<span id="page-41-0"></span>
$$Q = C_3 A \sqrt{2gH_{HW}} \tag{2.84}$$

Similarly, for submerged orifice flow equation [\(2.85\)](#page-41-1) is used.

<span id="page-41-1"></span>
$$Q = C_4 A \sqrt{2g \left( H_{HW} - H_{TW} \right)} \tag{2.85}$$

where,

*C*<sup>3</sup> is the discharge coefficient for free sluice flow,

*C*<sup>4</sup> is the discharge coefficient for submerged orifice flow, and

*A* is the gate opening (*m* 2 ).

If the ratio of tailwater to headwater is less than 0.64, equation [\(2.82\)](#page-41-2) for supercritical flow is applied. If the ratio of tailwater to headwater is greater than 0.68, equation [\(2.83\)](#page-41-3) for subcritical flow is applied. This is either a free sluice for supercritical flow, or a submerged orifice for subcritical flow. In cases when the tailwater to headwater ratio is between 0.64 and 0.68 both discharges are computed and a weighted average of the two is used.

{42}------------------------------------------------

#### 2.2.7.5 Orifices

If the headwater is lower than the opening of an orifice, the flow through the orifice is treated as weir flow, and the equation [\(2.80\)](#page-40-3) is used. If the tailwater is higher than the opening of an orifice, then equation [\(2.85\)](#page-41-1) submerged flow through the orifice is applied. If the headwater is higher than the opening of an orifice but the tailwater is lower than the opening of an orifice, the free jet flow through the orifice is calculated as

$$Q = C_2 A \sqrt{2g \left( H_{HW} + 0.5B \right)} \tag{2.86}$$

where, *B* is the height of the orifice opening (m), and *HHW* is calculated based on the center line of the orifice.

### 2.2.7.6 Masks

In EFDC+, "masks" are implemented as barriers across cell flow faces in order to fully or partially block flow between cells in the model domain. At *U* or *V* face of a cell with mask, a "Draft Depth" and a "Bottom Sill Height" are defined as the thickness of a floating or fixed object at the water surface, and the thickness of a structure at the bed, respectively. If the space between "Draft" and "Bottom Sill" is equal to 0, the cell face is fully blocked, otherwise it is partially blocked.

The blocking mask is useful to simulate structural obstacles such as breakwaters and causeways locally aligning with the model grid, but have widths much less than the cell size or grid spacing in one direction.

### <span id="page-42-0"></span>2.2.8 Propeller Wash

The [EFDC+](#page-11-0) propeller wash module simulates sediment resuspension and transport processes due to ship traffic, with a fully coupled representation of hydrodynamics, sediment transport, and propeller wash effects. Using ship traffic data, this module computes each ship's propeller wash effects (e.g., flow velocity, shear stress, sediment erosion rate) based on an independent sub-grid, representing a propeller wash jet area behind the ship. The momentum flux induced by the propeller rotation is also calculated for the ship locations during the simulation. The propeller wash results are then linked to model grid cells for every time step of the hydrodynamics and sediment transport computation in the model simulation. The details for the theoretical basis and algorithmic structure of the [EFDC+](#page-11-0) propeller wash module are described in [DSI](#page-260-8) [\(2021\)](#page-260-8).

Propeller wash may significantly impact the hydrodynamics and transport processes of constituents in the water column, especially in areas of substantial ship traffic. The [EFDC+](#page-11-0) propeller wash module has the option to add the momentum associated with the propeller efflux velocity to a [3D](#page-10-1) hydrodynamic flow field as a source term. If this option is activated, the [EFDC+](#page-11-0) hydrodynamic model includes the propeller wash momentum effects when it computes the [3D](#page-10-1) hydrodynamic flow field for the next time step. The resulting flow velocities then impact the movement of the suspended sediments and other constituents in the water layers of the [EFDC+](#page-11-0) model grid.

Figure [2.5\(](#page-44-1)a) shows a [two-dimensional \(2D\)](#page-10-4) conceptual diagram for the velocity vector components of a ship passing through an [EFDC+](#page-11-0) model grid cell. Based on the angle between the ship's heading and the [EFDC+](#page-11-0) model grid rotation, the [EFDC+](#page-11-0) propeller wash module vectorially splits the propeller efflux velocity *V*<sup>0</sup> into the computational grid space (in *i* and *j* directions) as:

$$V_i = V_0 \times \cos\left(\theta_3 - \theta_1\right) \tag{2.87}$$

{43}------------------------------------------------

$$V_j = V_0 \times \sin(\theta_3 - \theta_1) \tag{2.88}$$

$$\theta_3 = \theta_2 - \frac{\pi}{2} \tag{2.89}$$

where,

*V*<sup>0</sup> is the propeller efflux velocity from the propeller plane (m/s)

*Vi* is the grid-oriented efflux velocity component in the *i* direction (m/s)

*Vj* is the grid-oriented efflux velocity component in the *j* direction (m/s)

θ<sup>1</sup> is the EFDC+ model grid cell rotation (radian)

θ<sup>2</sup> is the ship heading in compass orientation (radian)

θ<sup>3</sup> is the propeller wash efflux angle (radian)

Given the velocity components *V<sup>i</sup>* and *V<sup>j</sup>* , the [EFDC+](#page-11-0) propeller wash module computes the specific momentum flux due to propeller wash for each direction as follows:

$$M_{pi} = |V_i \times A_P| \times V_i \times f_p \tag{2.90}$$

$$M_{pj} = |V_j \times A_P| \times V_j \times f_p \tag{2.91}$$

where,

*MPi* is the specific momentum flux due to propeller wash in the *i* direction (m<sup>4</sup> /s2 )

*MP j* is the specific momentum flux due to propeller wash in the *j* direction (m<sup>4</sup> /s2 )

*A<sup>P</sup>* is the area of propeller wash face in the efflux zone (m<sup>2</sup> )

*f<sup>p</sup>* is the momentum effect factor (dimensionless)

The [EFDC+](#page-11-0) propeller wash module then incorporates the resultant momentum flux *MPi* and *MP j* into the momentum equations of [EFDC+](#page-11-0) hydrodynamic model computations as a source term. The [EFDC+](#page-11-0) propeller wash module also applies a factor *f<sup>p</sup>* to adjust the propeller wash-induced momentum flux to account for losses and turbulence that are not directly simulated. This factor is a user-defined input parameter of the [EFDC+](#page-11-0) propeller wash module, which can range between 0.3 and 0.7 according to observations from [Kee](#page-262-2) [et al.](#page-262-2) [\(2006\)](#page-262-2) and [Hamill and Kee](#page-261-15) [\(2016\)](#page-261-15) that the actual cross-sectional area of the efflux velocity plane can be smaller than the propeller face area *Ap*.

Vertically, the [EFDC+](#page-11-0) propeller wash module distributes the propeller wash-induced momentum effects proportionately across the [EFDC+](#page-11-0) model grid water layers that the propeller intersects. The vertical splitting process for the momentum change rates *MPi* and *MP j* is implemented with relative to the ship draft, propeller diameter, water depth, and the number of the model grid water layers where the propeller is located. Figure [2.5\(](#page-44-1)b) shows an example of vertical fractions (%) for the propeller wash-induced momentum change rates over the [EFDC+](#page-11-0) model grid water layers.

{44}------------------------------------------------

<span id="page-44-1"></span>2. HYDRODYNAMICS EFDC+ Theory

Fig. 2.5. Diagrams for propeller wash-induced momentum (a) coupling with an EFDC+ model grid cell and (b) splitting over vertical water layers.

#### <span id="page-44-0"></span>2.3. Numerical Solution for the Equations of Motion

The equations of motion, shown previously in equations [\(2.2\)](#page-23-0) and [\(2.3\)](#page-23-1) are solved in a region subdivided into six faced cells. The projection of the vertical cell boundaries to a horizontal plane forms a curvilinear, orthogonal grid in the orthogonal coordinate system (*x*, *y*). In a vertical(*x*,*z*) or(*y*,*z*) plane, the cells bounded by the same constant *z* surfaces are referred to as cell layers. The equations are solved using a combination of finite volume and finite difference techniques, with the variable locations shown in Figure [2.6.](#page-45-0)

The staggered grid location of variables is often referred to as the Arakawa C grid [\(Arakawa and Lamb,](#page-258-4) [1977\)](#page-258-4) or the MAC grid [\(Peyret and Taylor,](#page-263-8) [1983\)](#page-263-8). To proceed, it is convenient to modify equations [\(2.2\)](#page-23-0) and [\(2.3\)](#page-23-1) by eliminating the vertical pressure gradients using equation [\(2.4\)](#page-23-2). After some manipulation, the horizontal momentum equations are given in the equations [\(2.92\)](#page-44-2) and [\(2.93\)](#page-45-1).

<span id="page-44-2"></span>
$$\frac{\partial}{\partial t} (m_x m_y H u) + \frac{\partial}{\partial x} (m_y H u u) + \frac{\partial}{\partial y} (m_x H v u) + \frac{\partial}{\partial z} (m_x m_y w u) 
- \left( v \frac{\partial m_y}{\partial x} - u \frac{\partial m_x}{\partial y} \right) H v - m_x m_y f H v 
= - m_y H \frac{\partial}{\partial x} - m_y H g \frac{\partial}{\partial x} + m_y H g b \frac{\partial}{\partial x} - m_y H g b z \frac{\partial}{\partial x} + \frac{\partial}{\partial z} \left( \frac{m_x m_y A_v}{H} \frac{\partial}{\partial z} \right) + S_u$$
(2.92)

{45}------------------------------------------------

<span id="page-45-0"></span>Fig. 2.6. Free Surface Displacement Centered Horizontal Grid.

$$\frac{\partial}{\partial t} (m_x m_y H v) + \frac{\partial}{\partial x} (m_y H u v) + \frac{\partial}{\partial y} (m_x H v v) + \frac{\partial}{\partial z} (m_x m_y w v) 
+ \left( v \frac{\partial m_y}{\partial x} - u \frac{\partial m_x}{\partial y} \right) H u + m_x m_y f H u 
= -m_x H \frac{\partial p}{\partial y} - m_x H g \frac{\partial \zeta}{\partial y} + m_x H g b \frac{\partial h}{\partial y} - m_x H g b z \frac{\partial H}{\partial y} + \frac{\partial}{\partial z} \left( \frac{m_x m_y A_v}{H} \frac{\partial v}{\partial z} \right) + S_v$$
(2.93)

First, the vertical discretization of equations [\(2.92\)](#page-44-2) and [\(2.93\)](#page-45-1) is performed. The equations are integrated with respect to *z* over a cell layer assuming that vertically defined variables (at the cell or layer centers) are constant. Additionally, these variables must be defined vertically at the cell layer interfaces or boundaries. Using the notation for mass fluxes,

<span id="page-45-3"></span><span id="page-45-2"></span><span id="page-45-1"></span>
$$P_k = m_y H u_k, Q_k = m_x H v_k \tag{2.94}$$

equations [\(2.92\)](#page-44-2) and [\(2.93\)](#page-45-1) are redefined as;

$$\frac{\partial}{\partial t} (m_{x} P_{k} \Delta_{k}) + \frac{\partial}{\partial x} (P_{k} u_{k} \Delta_{k}) + \frac{\partial}{\partial y} (Q_{k} u_{k} \Delta_{k}) + m \left[ (wu)_{k} - (wu)_{k-1} \right] 
- \left( v_{k} \frac{\partial m_{y}}{\partial x} - u_{k} \frac{\partial m_{x}}{\partial y} \right) H v_{k} \Delta_{k} - m_{y} f Q_{k} \Delta_{k} 
= -\frac{1}{2} m_{y} H \Delta_{k} \frac{\partial}{\partial x} (p_{k} + p_{k-1}) - m_{y} H \Delta_{k} g \frac{\partial \zeta}{\partial x} + m_{y} H \Delta_{k} g b_{k} \frac{\partial h}{\partial x} 
- 0.5 m_{y} H \Delta_{k} g b_{k} (z_{k} + z_{k-1}) \frac{\partial H}{\partial x} + m \left[ (\tau_{xz})_{k} - (\tau_{xz})_{k-1} \right] + (S_{u} \Delta)_{k}$$
(2.95)

{46}------------------------------------------------

$$\frac{\partial}{\partial t} (m_{y}Q_{k}\Delta_{k}) + \frac{\partial}{\partial x} (P_{k}v_{k}\Delta_{k}) + \frac{\partial}{\partial y} (Q_{k}v_{k}\Delta_{k}) 
+ m \left[ (wv)_{k} - (wv)_{k-1} \right] + \left( v_{k} \frac{\partial m_{y}}{\partial x} - u_{k} \frac{\partial m_{x}}{\partial y} \right) H u_{k}\Delta_{k} + m_{x}f P_{k}\Delta_{k} 
= -\frac{1}{2} m_{x} H \Delta_{k} \frac{\partial}{\partial y} (p_{k} + p_{k-1}) - m_{x} H \Delta_{k} g \frac{\partial \zeta}{\partial y} + m_{x} H \Delta_{k} g b_{k} \frac{\partial h}{\partial y} 
- 0.5 m_{x} H \Delta_{k} g b_{k} (z_{k} + z_{k-1}) \frac{\partial H}{\partial y} + m \left[ (t_{yz})_{k} - m(t_{yz})_{k-1} \right] + (S_{v}\Delta)_{k}$$
(2.96)

where, ∆*<sup>k</sup>* is the vertical cell or layer thickness, and the turbulent shear stresses at the cell layer interfaces are defined by:

<span id="page-46-3"></span><span id="page-46-2"></span>
$$(\tau_{xz})_k = \frac{2}{H} (A_v)_k \frac{u_{k+1} - u_k}{\Delta_{k+1} + \Delta_k}$$
(2.97)

<span id="page-46-4"></span>
$$(t_{yz})_k = \frac{2}{H} (A_v)_k \frac{v_{k+1} - v_k}{\Delta_{k+1} + \Delta_k}$$
 (2.98)

If there are *K* cells in the *z* direction, the hydrostatic equation can be integrated from a cell layer interface to the surface to give:

<span id="page-46-5"></span><span id="page-46-0"></span>
$$p_k = gH\left(\sum_{j=k}^K b_j \Delta_j - b_k \Delta_k\right) + p_s \tag{2.99}$$

where, *p<sup>s</sup>* is the physical pressure at the free surface or under the rigid lid divided by the reference density. The continuity equation [\(2.5\)](#page-23-3) is also integrated with respect to *z* over a cell or layer to give:

<span id="page-46-1"></span>
$$\frac{\partial}{\partial t} (m\zeta \Delta_k) + \frac{\partial}{\partial x} (P_k \Delta_k) + \frac{\partial}{\partial y} (Q_k \Delta_k) + m(w_k + w_{k-1}) = S_h$$
(2.100)

The numerical solution of the vertically discrete momentum equations [\(2.92\)](#page-44-2) and [\(2.93\)](#page-45-1) proceeds by splitting the external depth-integrated mode (associated with external long surface gravity waves) from the internal mode (associated with vertical current structure).

The external mode equations are obtained by summing equations [\(2.92\)](#page-44-2) and [\(2.93\)](#page-45-1) over *K* cells or layers in the vertical utilizing equation [\(2.99\)](#page-46-0), and are given by:

$$\frac{\partial}{\partial t} (m_x \hat{P}) + \sum_{k=1}^K \left[ \frac{\partial}{\partial x} (P_k u_k \Delta_k) + \frac{\partial}{\partial y} (Q_k u_k \Delta_k) - \left( v_k \frac{\partial m_y}{\partial x} - u_k \frac{\partial m_x}{\partial y} \right) H v_k \Delta_k - m_y f Q_k \Delta_k \right] 
= -m_y H g \frac{\partial \zeta}{\partial x} - m_y H \frac{\partial p_s}{\partial x} + m_y H g \hat{b} \frac{\partial h}{\partial x} - m_y H g \left[ \sum_{k=1}^K \left( \beta_k \Delta_k + \frac{1}{2} (z_k + z_{k-1}) b_k \Delta_k \right) \right] \frac{\partial H}{\partial x} 
- m_y g H^2 \frac{\partial}{\partial x} \left( \sum_{k=1}^K \beta_k \Delta_k \right) + m \left[ (\tau_{xz})_K - (\tau_{xz})_0 \right] + \hat{S}_u$$
(2.101)

{47}------------------------------------------------

$$\frac{\partial}{\partial t} \left( m_x \hat{Q} \right) + \sum_{k=1}^K \left[ \frac{\partial}{\partial x} \left( P_k v_k \Delta_k \right) + \frac{\partial}{\partial y} \left( Q_k v_k \Delta_k \right) - \left( v_k \frac{\partial m_y}{\partial x} - u_k \frac{\partial m_x}{\partial y} \right) H u_k \Delta_k - m_x f P_k \Delta_k \right] \\
= - m_x H g \frac{\partial \zeta}{\partial y} - m_x H \frac{\partial p_s}{\partial y} + m_x H g \hat{b} \frac{\partial h}{\partial y} - m_x H g \left[ \sum_{k=1}^K \left( \beta_k \Delta_k + \frac{1}{2} \left( z_k + z_{k-1} \right) b_k \Delta_k \right) \right] \frac{\partial H}{\partial y} \\
- m_x g H^2 \frac{\partial}{\partial y} \left( \sum_{k=1}^K \beta_k \Delta_k \right) + m \left[ \left( \tau_{yz} \right)_K - \left( \tau_{yz} \right)_0 \right] + \hat{S}_u \tag{2.102}$$

<span id="page-47-3"></span><span id="page-47-2"></span>
$$\frac{\partial}{\partial t}(m\zeta) + \frac{\partial}{\partial x}\bar{P} + \frac{\partial}{\partial y}\bar{Q} = S_h \tag{2.103}$$

where the over bar indicates an average over the depth as reiterated in equation [\(2.104\)](#page-47-0). Additionally, equation [\(2.105\)](#page-47-1) is introduced to simplify equations [\(2.101\)](#page-46-1) and [\(2.102\)](#page-47-2).

<span id="page-47-0"></span>
$$\hat{P} = m_y H \hat{u}, \hat{Q} = m_x H \hat{v} \tag{2.104}$$

<span id="page-47-1"></span>
$$\beta_k = \sum_{j=k}^K b_j \Delta_j - \frac{1}{2} b_k \Delta_k \tag{2.105}$$

The depth integrated continuity equation, equation [\(2.103\)](#page-47-3), follows from equation [\(2.6\)](#page-23-4) and provides the continuity constraint for the external mode. Consistent with the form of equation [\(2.103\)](#page-47-3) the external mode variables are chosen to be the free surface displacement, ζ and the volumetric transports, *P* = *myHu* and *Q* = *mxHv*. Details of the solution of the external mode equations [\(2.101\)](#page-46-1) to [\(2.103\)](#page-47-3) are presented in Section [2.4.](#page-49-0)

Several formulations are possible for the internal mode equations. Equations [\(2.92\)](#page-44-2) and [\(2.93\)](#page-45-1) have *K* degrees of freedom for each of the horizontal velocity components. However, the summation of these equations over *K* cells or layers in the vertical to form the external mode equations [\(2.101\)](#page-46-1) and [\(2.102\)](#page-47-2) effectively removes a degree of freedom since the constraints

$$\sum_{k=1}^{K} u_k \Delta_k = \hat{u}, \text{ and}$$
 (2.106)

<span id="page-47-5"></span><span id="page-47-4"></span>
$$\sum_{k=1}^{K} \nu_k \Delta_k = \hat{\nu} \tag{2.107}$$

must be satisfied. One approach to the internal mode is to solve equations [\(2.92\)](#page-44-2) and [\(2.93\)](#page-45-1) using the free surface slopes, or the surface pressure gradients in the rigid lid case, from the external solution and distribute the error such that equations [\(2.106\)](#page-47-4) and [\(2.107\)](#page-47-5) are satisfied. A second approach is to form equations for the deviations of the velocity components from their vertical means by subtracting the external equations [\(2.101\)](#page-46-1) and [\(2.102\)](#page-47-2) from the layer integrated equations [\(2.92\)](#page-44-2) and [\(2.93\)](#page-45-1). However, it will still be necessary to satisfy the constraints [\(2.106\)](#page-47-4) and [\(2.107\)](#page-47-5). The approach proposed herein is to reduce the systems of 

{48}------------------------------------------------

*K* layer averaged equations [\(2.95\)](#page-45-2) and [\(2.96\)](#page-46-2) to systems of *K* −1 equations and use equations [\(2.106\)](#page-47-4) and [\(2.107\)](#page-47-5) to provide the *K* th equation consistent with the actual degrees of freedom.

The internal mode equations are formed by first dividing equations [\(2.95\)](#page-45-2) and [\(2.96\)](#page-46-2) by the cell layer thickness (∆*k*). Next, the equations for cell layer *k* is subtracted from the equations for cell layer *k* + 1. The resulting equation from these two operations is divided by the average thickness (∆*k*+1,*k*) of the two cell layers resulting in:

<span id="page-48-0"></span>
$$\frac{\partial}{\partial t} \left( m_x \frac{P_{k+1} - P_k}{\Delta_{k+1,k}} \right) + \frac{\partial}{\partial x} \left( \frac{P_{k+1}u_{k+1} - P_ku_k}{\Delta_{k+1,k}} \right) + \frac{\partial}{\partial y} \left( \frac{Q_{k+1}u_{k+1} - Q_ku_k}{\Delta_{k+1,k}} \right) \\
+ \frac{m}{\Delta_{k+1,k}} \left[ \frac{(wu)_{k+1} - (wu)_k}{\Delta_{k+1}} - \frac{(wu)_k - (wu)_{k-1}}{\Delta_k} \right] - m_y f \frac{Q_{k+1} - Q_k}{\Delta_{k+1,k}} \\
- \frac{1}{\Delta_{k+1,k}} \left[ \left( v_{k+1} \frac{\partial m_y}{\partial x} - u_{k+1} \frac{\partial m_x}{\partial y} \right) H v_{k+1} - \left( v_k \frac{\partial m_y}{\partial x} - u_k \frac{\partial m_x}{\partial y} \right) H v_k \right]$$

$$= m_y H \frac{b_{k+1} - b_k}{\Delta_{k+1,k}} g \left( \frac{\partial h}{\partial x} - z_k \frac{\partial H}{\partial x} \right) + \frac{1}{2} \frac{m_y H^2}{\Delta_{k+1,k}} g \left( \Delta_{k+1} \frac{\partial b_{k+1}}{\partial x} + \Delta_k \frac{\partial b_k}{\partial x} \right) \\
+ \frac{m}{\Delta_{k+1,k}} \left[ \frac{(\tau_{xz})_{k+1} - (\tau_{xz})_k}{\Delta_{k+1}} - \frac{(\tau_{xz})_k - (\tau_{xz})_{k-1}}{\Delta_k} \right] + \frac{(S_u)_{k+1} - (S_u)_k}{\Delta_{k+1,k}} \right) \\
+ \frac{m}{\Delta_{k+1,k}} \left[ \frac{(wv)_{k+1} - (wv)_k}{\Delta_{k+1,k}} - \frac{(wv)_k - (wv)_{k-1}}{\Delta_k} \right] + m_x f \frac{P_{k+1} - Q_k v_k}{\Delta_{k+1,k}} \right) \\
+ \frac{1}{\Delta_{k+1,k}} \left[ \left( v_{k+1} \frac{\partial m_y}{\partial x} - u_{k+1} \frac{\partial m_x}{\partial y} \right) H u_{k+1} - \left( v_k \frac{\partial m_y}{\partial x} - u_k \frac{\partial m_x}{\partial y} \right) H u_k \right]$$

$$= m_x H \frac{b_{k+1} - b_k}{\Delta_{k+1,k}} g \left( \frac{\partial h}{\partial y} - z_k \frac{\partial H}{\partial y} \right) + \frac{1}{2} \frac{m_x H^2}{\Delta_{k+1,k}} g \left( \Delta_{k+1} \frac{\partial b_{k+1}}{\partial y} + \Delta_k \frac{\partial b_k}{\partial y} \right) \\
+ \frac{m}{\Delta_{k+1,k}} \left[ \frac{(\tau_{yz})_{k+1} - (\tau_{yz})_k}{\Delta_{k+1}} - \frac{(\tau_{yz})_k - (\tau_{yz})_{k-1}}{\Delta_k} \right] + \frac{(S_v)_{k+1} - (S_v)_k}{\Delta_{k+1,k}} \right]$$

<span id="page-48-1"></span>
$$\Delta_{k+1,k} = \frac{1}{2} \left( \Delta_{k+1} + \Delta_k \right) \tag{2.110}$$

Inspection of equations [\(2.108\)](#page-48-0) and [\(2.109\)](#page-48-1) reveals that they could have also been obtained by differentiating the horizontal momentum equations [\(2.92\)](#page-44-2) and [\(2.93\)](#page-45-1) with respect to *z* and introducing a finite difference discretion in *z*. Using equations [\(2.97\)](#page-46-3) and [\(2.98\)](#page-46-4) to relate the shear stresses to the velocity differences across the interior interfaces suggests that the equations [\(2.108\)](#page-48-0) and [\(2.109\)](#page-48-1) be interpreted as a system of *K* − 1 equations for either the *K* − 1 interfacial velocity differences or the *K* − 1 interior interfacial shear stresses. Details of the solution of the internal mode equations [\(2.108\)](#page-48-0) and [\(2.109\)](#page-48-1) is presented in Section [2.5.](#page-54-0)

The solution of the vertical velocity, *w*, employs the continuity equations. Dividing equation [\(2.100\)](#page-46-5) by ∆*k*, and subtracting equation [\(2.102\)](#page-47-2) yields

<span id="page-48-2"></span>
$$w_k = w_{k-1} - \frac{\Delta_k}{m} \left[ \frac{\partial}{\partial x} \left( P_k - \hat{P} \right) + \frac{\partial}{\partial y} \left( Q_k - \hat{Q} \right) \right]. \tag{2.111}$$

{49}------------------------------------------------

Since *w<sup>o</sup>* = 0, the solution proceeds from the first cell layer to the surface. Provided the constraints (equations [\(2.106\)](#page-47-4) and [\(2.107\)](#page-47-5)) are satisfied, the surface velocity at *k* = *K* will be zero and satisfy the boundary condition.

#### <span id="page-49-0"></span>2.4. Computational Aspects of the Three Time Level External Mode Solution

The formulation of a computational algorithm for the numerical solution of the external mode equations [\(2.101\)](#page-46-1) to [\(2.103\)](#page-47-3) begins by introducing modified variables and reorganizing the equations to give:

$$\frac{\partial \hat{P}}{\partial t} = -\frac{m_{y}}{m_{x}} H g \frac{\partial \zeta}{\partial x} - \frac{m_{y}}{m_{x}} H \frac{\partial p_{s}}{\partial x} + \frac{m_{y}}{m_{x}} H g \left( \hat{b} \frac{\partial h}{\partial x} - \hat{B} \frac{\partial H}{\partial x} - H \frac{\partial \hat{\beta}}{\partial x} \right) 
- \frac{1}{m_{x}} \sum_{k=1}^{K} \Delta_{k} \left( \frac{\partial}{\partial x} (P_{k} u_{k}) + \frac{\partial}{\partial y} (Q_{k} u_{k}) \right) + \frac{1}{m_{x}} \sum_{k=1}^{K} \Delta_{k} \left[ \left( v_{k} \frac{\partial m_{y}}{\partial x} - u_{k} \frac{\partial m_{x}}{\partial y} \right) H v_{k} + m_{y} f Q_{k} \right] 
+ \frac{1}{m_{x}} \sum_{k=1}^{K} \left[ \frac{\partial}{\partial x} \left( \frac{m_{y}}{m_{x}} H A_{Hk} \Delta_{k} \frac{\partial u_{k}}{\partial x} \right) + \frac{\partial}{\partial y} \left( \frac{m_{x}}{m_{y}} H A_{Hk} \Delta_{k} \frac{\partial u_{k}}{\partial y} \right) \right] 
+ m_{y} (\tau_{xz})_{K} - m_{y} (\tau_{xz})_{0} + \frac{1}{m_{x}} \hat{S}_{u}$$
(2.112)

$$\frac{\partial \hat{Q}}{\partial t} = -\frac{m_x}{m_y} H g \frac{\partial \zeta}{\partial y} - \frac{m_x}{m_y} H \frac{\partial p_s}{\partial y} + \frac{m_x}{m_y} H g \left( \hat{b} \frac{\partial h}{\partial y} - \hat{B} \frac{\partial H}{\partial y} - H \frac{\partial \hat{\beta}}{\partial y} \right) 
- \frac{1}{m_y} \sum_{k=1}^K k \left( \frac{\partial}{\partial x} (P_k v_k) + \frac{\partial}{\partial y} (Q_k v_k) \right) + \frac{1}{m_y} \sum_{k=1}^K \Delta_k \left[ \left( v_k \frac{\partial m_y}{\partial x} - u_k \frac{\partial m_x}{\partial y} \right) H u_k + m_x f P_k \right] 
+ \frac{1}{m_y} \sum_{k=1}^K \left[ \frac{\partial}{\partial x} \left( \frac{m_y}{m_x} H A_{Hk} \Delta_k \frac{\partial v_k}{\partial x} \right) + \frac{\partial}{\partial y} \left( \frac{m_x}{m_y} H A_{Hk} \Delta_k \frac{\partial v_k}{\partial y} \right) \right] 
+ m_x (\tau_{yz})_K - m_x (\tau_{yz})_0 + \frac{1}{m_y} \hat{S}_v$$
(2.113)

<span id="page-49-2"></span><span id="page-49-1"></span>
$$\frac{\partial \zeta}{\partial t} + \frac{1}{m} \left( \frac{\partial \hat{P}}{\partial x} + \frac{\partial \hat{Q}}{\partial y} \right) = S_h \tag{2.114}$$

where,

<span id="page-49-3"></span>
$$\hat{\beta} = \sum_{k=1}^{K} \beta_k \Delta_k, \text{ and}$$
 (2.115)

$$\hat{\beta} = \sum_{k=1}^{K} \left[ \beta_k \Delta_k + \frac{1}{2} (z_k + z_{k-1}) b_k \Delta_k \right].$$
 (2.116)

Equations [\(2.112\)](#page-49-1) and [\(2.113\)](#page-49-2) now equate the time rate of change of the external or depth integrated volumetric transports to the pressure gradients associated with the free surface slope, atmospheric pressure and 

{50}------------------------------------------------

buoyancy, the advective accelerations, the Coriolis and curvature accelerations, the free surface and bottom tangential stresses, and the general source, sink terms. The staggered location of variables on the computational grid (Figure 2.6) allows most horizontal spatial derivatives in equations (2.112) to (2.114) to be represented by second order accurate central differences and results in conservation of volume, mass, momentum and energy in the limit of exact integration of the equations in time (Haltiner and Williams, 1980; Simons et al., 1973). When a variable is not located at a point required for implementation of central difference operators, averaging in either or both spatial directions is appropriate. The use of the spatial averaging scheme of Arakawa and Lamb (1977) to represent the Coriolis and curvature accelerations also guarantees energy conservation.

Following the introduction of discrete finite difference and averaging representations in space, equations (2.112) to (2.114), for a horizontal grid of L cells, may be viewed as a system of 3L ordinary differential equations in time for the volumetric transport and the free surface displacement. The numerous techniques available to solve these equations generally fall within the categories of explicit and semi-implicit. The most frequently used explicit scheme is the three-time level leapfrog scheme where the time derivatives are approximated between the time levels n+1 and n-1, and the remaining terms are evaluated at time level n. Although computationally simple to implement, the maximum time step is restricted by the Courant-Fredrick-Levy condition based on the gravity wave phase speed. An alternate approach allowing larger time steps is the semi-implicit three-time level scheme (Madala and Piacseki, 1977), which when implemented for equations (2.112) to (2.114) is

<span id="page-50-0"></span>
$$\hat{P}^{n+1} = \hat{P}^{n-1} - \Delta t \left(\frac{m_{y}}{m_{x}}H\right)^{u} g d_{x}^{u} \left(\zeta^{n+1} + \zeta^{n-1}\right) - 2\Delta t \left(\frac{m_{y}}{m_{x}}H\right)^{u} d_{x}^{u} p_{s}$$

$$+ 2\Delta t \left(\frac{m_{y}}{m_{x}}H\right)^{u} g \left(\hat{b}^{u} d_{x}^{u} h - \hat{B}^{u} d_{x}^{u} H - H^{u} d_{x}^{u} \hat{\beta}\right)$$

$$- 2\Delta t \left(\frac{1}{m_{x}}\right)^{u} \sum_{k=1}^{K} \Delta_{k} \left[d_{x}^{u} (P_{k} u_{k}) + d_{y}^{u} (Q_{k} u_{k})\right]$$

$$+ 2\Delta t \left(\frac{1}{m_{x}}\right)^{u} \sum_{k=1}^{K} \Delta_{k} \left[\left(v_{k} \frac{\partial m_{y}}{\partial x} - u_{k} \frac{\partial m_{x}}{\partial y}\right) H v_{k} + m_{y} f Q_{k}\right]^{u}$$

$$+ 2\Delta t m_{y}^{u} \left[\left(t_{xz}^{n-1}\right)_{K} - \left(t_{xz}^{n-1}\right)_{0}\right]^{u}$$

$$+ 2\Delta t \left(\frac{1}{m_{x}}\right)^{u} \sum_{k=1}^{K} \Delta_{k} \left[\frac{\partial}{\partial x} \left(m_{y} H t_{xx}^{n-1}\right) + \frac{\partial}{\partial y} \left(m_{x} H t_{xy}^{n-1}\right)\right]^{u}$$

$$+ \frac{\partial}{\partial y} \left(m_{x} H t_{xy}^{n-1}\right) - \frac{\partial}{\partial x} \left(m_{y} H t_{yy}^{n-1}\right)\right]_{k}^{u}$$

$$(2.117)$$

{51}------------------------------------------------

<span id="page-51-4"></span>
$$\hat{Q}^{n+1} = \hat{Q}^{n-1} - \Delta t \left(\frac{m_x}{m_y}H\right)^{\nu} g \delta_y^{u} \left(\zeta^{n+1} + \zeta^{n-1}\right) - 2\Delta t \left(\frac{m_x}{m_y}H\right)^{\nu} \delta_y^{u} p_s 
+ 2\Delta t \left(\frac{m_x}{m_y}H\right)^{\nu} g \left(\hat{b}^{\nu} d_y^{\nu} h - \hat{B}^{\nu} \delta_y^{\nu} H - H^{\nu} \delta_y^{\nu} \hat{\beta}\right) 
- 2\Delta t \left(\frac{1}{m_y}\right)^{u} \sum_{k=1}^{K} \Delta_k \left[d_x^{\nu} (P_k \nu_k) + d_y^{\nu} (Q_k \nu_k)\right] 
- 2\Delta t \left(\frac{1}{m_y}\right)^{\nu} \sum_{k=1}^{K} \Delta_k \left[\left(\nu_k \frac{\partial m_y}{\partial x} - u_k \frac{\partial m_x}{\partial y}\right) H u_k + m_x f P_k\right]^{\nu} 
+ 2\Delta t m_x^{\nu} \left[\left(\tau_{yz}^{n-1}\right)_K - \left(\tau_{yz}^{n-1}\right)_0\right]^{\nu} 
+ 2\Delta t \left(\frac{1}{m_y}\right)^{\nu} \sum_{k=1}^{K} \Delta_k \left[\frac{\partial}{\partial x} \left(m_y H t_{yx}^{n-1}\right) + \frac{\partial}{\partial y} \left(m_x H t_{yy}^{n-1}\right) \right]^{\nu} 
\frac{\partial}{\partial y} \left(m_x H t_{xx}^{n-1}\right) - \frac{\partial}{\partial x} \left(m_y H t_{yx}^{n-1}\right)\right]_k^{\nu}$$
(2.118)

$$\zeta^{n+1} - \zeta^{n-1} + \Delta t \left(\frac{1}{m}\right)^{\zeta} \left[\delta_{x}^{\zeta} \left(\hat{P}^{n+1} + \hat{P}^{n-1}\right) + \delta_{y}^{\zeta} \left(\hat{Q}^{n+1} + \hat{Q}^{n-1}\right)\right] = S_{h} \Delta t \tag{2.119}$$

where,  $\Delta t$  indicates the time step. All terms in equations (2.117) to (2.119) are understood to be evaluated at the center time level n except those evaluated at the forward and backward time levels, n+1 and n-1, which are denoted by superscripts. The u, v, and  $\zeta$  superscripts indicate that a variable is evaluated, or that a spatial derivative is centered, at the corresponding spatial point.

The subscript of the spatial central difference operator  $\delta$  indicates direction. The grid cells are presumed to be bounded in the horizontal by lines of constant integer values of the dimensionless orthogonal coordinates x and y, resulting in the central spatial differences having the forms given in equations (2.120) and (2.121).

<span id="page-51-1"></span><span id="page-51-0"></span>
$$\delta_{x}\left(\phi_{i,j,k}\right) = \frac{1}{\Lambda x} \left(\phi_{i+\frac{1}{2},j,k} - \phi_{i-\frac{1}{2},j,k}\right) \tag{2.120}$$

<span id="page-51-5"></span><span id="page-51-3"></span><span id="page-51-2"></span>
$$\delta_{y}\left(\phi_{i,j,k}\right) = \frac{1}{\Delta y} \left(\phi_{i,j+\frac{1}{2},k} - \phi_{i,j-\frac{1}{2},k}\right) \tag{2.121}$$

Application of these finite difference operators to the advective accelerations is illustrated by,

$$\delta_{x}^{u}\left(P_{i,j,k}u_{i,j,k}\right) = \frac{1}{\Delta x}\left(P_{i+\frac{1}{2},j,k}u_{i+\frac{1}{2},j,k} - P_{i-\frac{1}{2},j,k}u_{i-\frac{1}{2},j,k}\right),\tag{2.122}$$

where the constant y dependence of the variables is implied. Since the u type variables are located at integer values of x, averaging is necessary to obtain values at half intervals. Averaging both the transport and the velocity yields,

$$\delta_x^u \left( P_{i,j,k} u_{i,j,k} \right) = \frac{1}{\Delta x} \left( \frac{P_{i+1,j,k} + P_{i,j,k}}{2} \frac{u_{i+1,j,k} + u_{i,j,k}}{2} - \frac{P_{i,j,k} + P_{i-1,j,k}}{2} \frac{u_{i,j,k} + u_{i-1,j,k}}{2} \right), \tag{2.123}$$

{52}------------------------------------------------

2. HYDRODYNAMICS EFDC+ Theory

which is consistent with a central difference approximation of the non-conservative form of this portion of the advective acceleration. Averaging the transport and allowing the velocity to be advected from the upwind direction gives,

<span id="page-52-0"></span>
$$\delta_{x}^{u}\left(P_{i,j,k}u_{i,j,k}\right) = \frac{1}{\Delta x} \left[ \max\left(\frac{P_{i+1,j,k} + P_{i,j,k}}{2}, 0\right) u_{i,j,k}^{n-1} - \max\left(\frac{P_{i,j,k} + P_{i-1,j,k}}{2}, 0\right) u_{i-1,j,k}^{n-1} \right] + \frac{1}{\Delta x} \left[ \min\left(\frac{P_{i+1,j,k} + P_{i,j,k}}{2}, 0\right) u_{i+1,j,k}^{n-1} - \min\left(\frac{P_{i,j,k} + P_{i-1,j,k}}{2}, 0\right) u_{i,j,k}^{n-1} \right]$$
(2.124)

which is consistent with an upwind or backward difference approximation of the non-conservative form of this portion of the advective acceleration. In equation (2.124), the transport is still at time level n, while the velocity is at time level n-1, for both stability and accuracy (Smolarkiewicz and Clark, 1986). The preference for the use of equation (2.123) or equation (2.124) generally depends upon the physical situation being simulated. The central difference form introduces no numerical diffusion, but may produce solution fields which exhibit cell to cell spatial oscillations. These oscillations can be eliminated by the addition of horizontal diffusion terms to the momentum equations. Specification of the horizontal diffusivity allows the degree of spatial smoothing to be controlled. The upwind difference form introduces numerical diffusion and does not produce spatial oscillations in the solution field. The Coriolis and curvature terms in equations (2.117) and (2.118) are discretized using an energy conserving spatial averaging and differencing (Arakawa and Lamb, 1977; Haltiner and Williams, 1980). For example, the Coriolis and curvature term in equation (2.117) is given by:

$$\left[ m_{y} f Q_{k} + \left( v_{k} \frac{\partial m_{y}}{\partial x} - u_{k} \frac{\partial m_{x}}{\partial y} \right) H v_{k} \right]^{u} = \frac{1}{2} \left[ (RH)_{i+\frac{1}{2},j}^{\zeta} v_{i+\frac{1}{2},j,k}^{\zeta} + (RH)_{i-\frac{1}{2},j}^{\zeta} v_{i-\frac{1}{2},j,k}^{\zeta} \right]$$
(2.125)

$$R_{i+\frac{1}{2},j}^{\zeta} = (mf)_{i+\frac{1}{2},j} + \frac{(m_y)_{i+1,j} - (m_y)_{i,j}}{\Delta x} v_{i+\frac{1}{2},j,k}^{\zeta} - \frac{(m_x)_{i+\frac{1}{2},j+\frac{1}{2}} - (m_x)_{i+\frac{1}{2},j-\frac{1}{2}}}{\Delta y} u_{i+\frac{1}{2},j,k}^{\zeta}$$
(2.126)

<span id="page-52-2"></span>
$$v_{i+\frac{1}{2},j,k}^{\zeta} = \frac{1}{2} \left( v_{i+\frac{1}{2},j+\frac{1}{2},k} + v_{i+\frac{1}{2},j-\frac{1}{2},k} \right)$$
 (2.127)

<span id="page-52-3"></span>
$$u_{i+\frac{1}{2},j,k}^{\zeta} = \frac{1}{2} \left( u_{i+1,j,k} + u_{i,j,k} \right)$$
 (2.128)

where the variables locations are shown in Figure 2.7.

Since the bottom tangential stresses in equations (2.117) and (2.118) must be supplied from the internal mode solution which follows the external solution, it is lagged at the backward time level. The general source, sink term has been replaced by horizontal diffusion terms having the form proposed by Mellor and Blumberg (1985). The horizontal stress tensors are shown in equations (2.129) to (2.131).

<span id="page-52-1"></span>
$$(\tau_{xx})_k = 2A_H \frac{1}{m_x} \frac{\partial u_k}{\partial x} \tag{2.129}$$

$$(\tau_{xy})_k = (t_{yx})_k = 2A_H \left(\frac{1}{m_x} \frac{\partial v_k}{\partial x} + \frac{1}{m_y} \frac{\partial u_k}{\partial y}\right)$$
 (2.130)

{53}------------------------------------------------

<span id="page-53-0"></span>2. HYDRODYNAMICS EFDC+ Theory

Fig. 2.7. U-centered grid in the horizontal (x, y) plane.

<span id="page-53-2"></span><span id="page-53-1"></span>
$$(t_{yy})_k = 2A_H \frac{1}{m_y} \frac{\partial v_k}{\partial y}.$$
 (2.131)

The horizontal diffusion coefficient, *A<sup>H</sup>* is often specified as a minimum constant value necessary to smooth cell to cell spatial oscillations in the solution field when the central difference form of the advective acceleration, equation [\(2.123\)](#page-51-3) is used. When the horizontal turbulent diffusion is used to represent subgrid scale mixing, *A<sup>H</sup>* may be determined as suggested by [\(Smagorinsky,](#page-264-4) [1963\)](#page-264-4).

The solution scheme for equations [\(2.117\)](#page-50-0) to [\(2.119\)](#page-51-0) requires first, the evaluation of all terms in the three equations at time levels *n* and *n*−1. On boundaries where the transports are specified, the specified values at time level *n*+1 are inserted into equation [\(2.119\)](#page-51-0). Equations [\(2.117\)](#page-50-0) and [\(2.118\)](#page-51-4) are then used to eliminate the unknown transports at time level *n*+1, from equation [\(2.119\)](#page-51-0). The result is a discrete Helmholtz type elliptic equation for the free surface displacement at time level *n*+1, having the general form

$$\zeta^{n+1} - g\Delta t^2 \left(\frac{1}{m}\right)^{\zeta} \left[\delta_x^{\zeta} \left(H\frac{m_y}{m_x}\right)^u \delta_x^u \zeta^{n+1} + \delta_x^{\zeta} \left(H\frac{m_x}{m_y}\right)^v \delta_y^v \zeta^{n+1}\right] - \phi = 0$$
 (2.132)

with the term φ containing all previously evaluated terms and transport boundary conditions. For cells where the free surface displacement is specified, equation [\(2.132\)](#page-53-2) is replaced by an equation which enforces the specified boundary condition at time level *n*+1. For the rigid lid case where the free surface displacement is constant in time and space, equation [\(2.132\)](#page-53-2) is modified to give an equation for the unknown surface pressure, *p<sup>s</sup>* by eliminating the first term, replacing *g*ζ in the discrete elliptic operator by *p<sup>s</sup>* , and appropriately modifying the last term. In the computer code, the system of equations corresponding to equation 

{54}------------------------------------------------

[\(2.132\)](#page-53-2) is solved by a reduced system conjugate gradient scheme with a multicolor or red-black ordering of the cells [\(Hageman and Young,](#page-261-17) [1981\)](#page-261-17). The conjugate gradient iterations continue until the sum of the squared residuals is less than a specified value. The free surface displacements or surface pressures are then substituted into equations [\(2.117\)](#page-50-0)-[\(2.118\)](#page-51-4) to determine the transports at time level *n*+1. Since the solution of equation [\(2.132\)](#page-53-2) is approximate, equation [\(2.119\)](#page-51-0) may not be identically satisfied upon substitution of the time level *n*+1 transports and free surface displacement. To ensure that the equation [\(2.119\)](#page-51-0) is identically satisfied in the case of a dynamic free surface, it is solved for a revised value of the time level *n* + 1, free surface displacement after introduction of the time level *n*+1 transports. For the rigid lid case, an external divergence error is calculated and compensated for by adding appropriate volumetric source or sink terms to equation [\(2.119\)](#page-51-0) during the next time step.

#### <span id="page-54-0"></span>2.5. Computational Aspects of the Three-Time Level Internal Mode Solution

<span id="page-54-1"></span>The internal mode equations [\(2.108\)](#page-48-0) and [\(2.109\)](#page-48-1) are solved using a fractional step scheme [\(Peyret and](#page-263-8) [Taylor,](#page-263-8) [1983\)](#page-263-8) with the first step being explicit and the second step being implicit. Figure [2.8](#page-54-1) illustrates the location variables in the *x*, *z* plane for the *x* component of the internal mode equations.

Fig. 2.8. U-centered Grid in the Vertical (*x*,*z*) Plane.

{55}------------------------------------------------

The computational equations for the three-time level explicit step are;

<span id="page-55-2"></span>
$$(P_{k+1} - P_{k})^{**} = (P_{k+1} - P_{k})^{n-1}$$

$$-2\Delta t \left(\frac{1}{m_{x}}\right)^{u} \left[\delta_{x}^{u}(P_{k+1}u_{k+1} - P_{k}u_{k}) + \delta_{y}^{u}(Q_{k+1}u_{k+1} - Q_{k}u_{k})\right]$$

$$-2\Delta t \left(\frac{1}{m_{x}}\right)^{u} \left[\frac{(Wu)_{k+1} - (Wu)_{k}}{\Delta_{k+1}} - \frac{(Wu)_{k} - (Wu)_{k-1}}{\Delta_{k}}\right]^{u}$$

$$+2\Delta t \left(\frac{1}{m_{x}}\right)^{u} \left[m_{y}fQ_{k+1} - m_{y}fQ_{k}\right]^{u}$$

$$+2\Delta t \left(\frac{1}{m_{x}}\right)^{u} \left[\left(v_{k+1}\frac{\partial m_{y}}{\partial x} - u_{k+1}\frac{\partial m_{x}}{\partial y}\right)Hv_{k+1} - \left(v_{k}\frac{\partial m_{y}}{\partial x} - u_{k}\frac{\partial m_{x}}{\partial y}\right)Hv_{k}\right]^{u}$$

$$+2\Delta t \left(\frac{m_{y}}{m_{x}}H\right)^{u} g\left[\left(b_{k+1} - b_{k}\right)^{u}\delta_{x}^{u}(h - z_{k}H) + \frac{1}{2}H^{u}\delta_{x}^{u}(b_{k+1}\Delta_{k+1} + b_{k}\Delta_{k})\right]$$

$$+2\Delta t \left(\frac{1}{m_{x}}\right)^{u} \left[\left(S_{u}\right)_{k+1} - \left(S_{u}\right)_{k}\right]^{u}$$

$$(Q_{k+1} - Q_{k})^{**} = (Q_{k+1} - Q_{k})^{n-1}$$

$$-2\Delta t \left(\frac{1}{m_{y}}\right)^{v} \left[\delta_{y}^{v} (P_{k+1}v_{k+1} - P_{k}v_{k}) + \delta_{y}^{v} (Q_{k+1}v_{k+1} - Q_{k}v_{k})\right]$$

$$-2\Delta t \left(\frac{1}{m_{y}}\right)^{v} \left[\frac{(Wv)_{k+1} - (Wv)_{k}}{\Delta_{k+1}} - \frac{(Wv)_{k} - (Wv)_{k-1}}{\Delta_{k}}\right]^{v}$$

$$-2\Delta t \left(\frac{1}{m_{y}}\right)^{v} \left[m_{x}fP_{k+1} - m_{x}fP_{k}\right]^{v}$$

$$-2\Delta t \left(\frac{1}{m_{y}}\right)^{v} \left[\left(v_{k+1}\frac{\partial m_{y}}{\partial x} - u_{k+1}\frac{\partial m_{x}}{\partial y}\right) H u_{k+1} - \left(v_{k}\frac{\partial m_{y}}{\partial x} - u_{k}\frac{\partial m_{x}}{\partial y}\right) H u_{k}\right]^{v}$$

$$+2\Delta t \left(\frac{m_{x}}{m_{y}}H\right)^{v} g \left[(b_{k+1} - b_{k})^{v}\delta_{y}^{v} (h - z_{k}H) + \frac{1}{2}H^{v}\delta_{y}^{v} (\Delta_{k+1}b_{k+1} + \Delta_{k}b_{k})\right]$$

$$+2\Delta t \left(\frac{1}{m_{y}}\right)^{v} \left[(S_{v})_{k+1} - (S_{v})_{k}\right]^{v}$$

<span id="page-55-4"></span><span id="page-55-3"></span><span id="page-55-1"></span><span id="page-55-0"></span>
$$W = m_x m_y w = m w, (2.135)$$

where the superscript ∗∗ denotes the provisional solution, and all the terms that don't have a specified time level are at the centered time level *n*. The horizontal volume transport, *P* and *Q* are defined by the equation [\(2.94\)](#page-45-3), and *W* is the vertical volume transport. The horizontal difference operations on the horizontal advection terms are identical to those presented in Section [2.3,](#page-44-0) equations [\(2.122\)](#page-51-5) to [\(2.124\)](#page-52-0). The vertical momentum flux terms may be represented in forms consistent with central or upwind differencing as shown in equations [\(2.136\)](#page-55-0) and [\(2.137\)](#page-55-1).

$$(Wu)_{i,j,k}^{u} = \frac{W_{i-\frac{1}{2},j,k} + W_{i+\frac{1}{2},j,k}}{2} \frac{u_{i,j,k} + u_{i,j,k+1}}{2}$$
(2.136)

$$(Wu)_{i,j,k}^{u} = \max\left(\frac{W_{i-\frac{1}{2},j,k} + W_{i+\frac{1}{2},j,k}}{2},0\right)u_{i,j,k}^{n-1} + \min\left(\frac{W_{i-\frac{1}{2},j,k} + W_{i+\frac{1}{2},j,k}}{2},0\right)u_{i,j,k+1}^{n-1}$$
(2.137)

{56}------------------------------------------------

2. HYDRODYNAMICS EFDC+ Theory

where the advected velocity is in the upwind form, equation [\(2.137\)](#page-55-1) is evaluated at time level *n*−1 for stability. The horizontal difference operations on the buoyancy and mean and total depths are central difference operators defined by equations [\(2.120\)](#page-51-1) and [\(2.121\)](#page-51-2). The inclusion of horizontal diffusion in the source, sink terms in equations [\(2.133\)](#page-55-2) and [\(2.134\)](#page-55-3) would follow from its inclusion in equations [\(2.117\)](#page-50-0) and [\(2.118\)](#page-51-4). The Coriolis and curvature terms are averaged and differenced by the energy conserving scheme presented in the Section [2.3,](#page-44-0) equations [\(2.125\)](#page-52-2) to [\(2.128\)](#page-52-3). The stability of the explicit fractional step (Equations [\(2.133\)](#page-55-2) and [\(2.134\)](#page-55-3)) is governed by the stability of the discretization of the horizontal and vertical advective accelerations, which will be discussed in Section [2.5,](#page-54-0) and the discretization of the Coriolis and curvature terms. The results of the Fourier stability analysis of the external mode scheme, with respect to the Coriolis acceleration, can be shown to apply to the internal mode scheme as well.

The computational equations for the second step of the three-time level scheme are:

$$\frac{(P_{k+1} - P_k)^{n+1}}{m_y^u \Delta_{k+1,k}} = \frac{(P_{k+1} - P_k)^{**}}{m_y^u \Delta_{k+1,k}} + 2\Delta t \left[ \frac{(\tau_{xz})_{k+1} - (\tau_{xz})_k}{\Delta_{k+1} \Delta_{k+1,k}} - \frac{(\tau_{xz})_k - (\tau_{xz})_{k-1}}{\Delta_k \Delta_{k+1,k}} \right]^{n+1}$$
(2.138)

$$\frac{\left(Q_{k+1} - Q_k\right)^{n+1}}{m_x^{\nu} \Delta_{k+1,k}} = \frac{\left(Q_{k+1} - Q_k\right)^{**}}{m_x^{\nu} \Delta_{k+1,k}} + 2\Delta t \left[ \frac{\left(t_{yz}\right)_{k+1} - \left(t_{yz}\right)_k}{\Delta_{k+1} \Delta_{k+1,k}} - \frac{\left(t_{yz}\right)_k - \left(t_{yz}\right)_{k-1}}{\Delta_k \Delta_{k+1,k}} \right]^{n+1}$$
(2.139)

Using equations [\(2.97\)](#page-46-3) and [\(2.98\)](#page-46-4), the turbulent shear stresses are related to the horizontal transports by:

<span id="page-56-3"></span><span id="page-56-2"></span><span id="page-56-0"></span>
$$(\tau_{xz})_k^{n+1} = \left(\frac{A_v^u}{H^u}\right)_k^n \left(\frac{1}{m_y^u H^u} \frac{P_{k+1} - P_k}{\Delta_{k+1,k}}\right)^{n+1}$$
(2.140)

<span id="page-56-4"></span><span id="page-56-1"></span>
$$(t_{yz})_k^{n+1} = \left(\frac{A_v^v}{H^v}\right)_k^n \left(\frac{1}{m_x^v H^v} \frac{Q_{k+1} - Q_k}{\Delta_{k+1,k}}\right)^{n+1}$$
(2.141)

Equations [\(2.140\)](#page-56-0) and [\(2.141\)](#page-56-1) could be used to eliminate the turbulent shear stresses from equations [\(2.138\)](#page-56-2) and [\(2.139\)](#page-56-3) to give a pair of *K*−1 systems of equations for the transport differences between layers, however, the resulting equations are poorly conditioned. Instead, equations [\(2.140\)](#page-56-0) and [\(2.141\)](#page-56-1) are used to eliminate the horizontal transport differences at time level *n*+1 from equations [\(2.138\)](#page-56-2) and [\(2.139\)](#page-56-3) to give a pair of *K* −1 equations for the turbulent shear stresses.

$$-\frac{1}{\Delta_{k}\Delta_{k+1,k}}(\tau_{xz})_{k-1}^{n+1} + \left[\frac{1}{\Delta_{k}\Delta_{k+1,k}} + \frac{(H^{u})^{n+1}}{2\Delta t} \left(\frac{H^{u}}{A_{v}^{u}}\right)_{k}^{n} + \frac{1}{\Delta_{k+1}\Delta_{k+1,k}}\right] (\tau_{xz})_{k}^{n+1} - \frac{1}{\Delta_{k+1}\Delta_{k+1,k}} (\tau_{xz})_{k+1}^{n+1} = \frac{1}{2\Delta t m_{y}^{u}} \frac{(P_{k+1} - P_{k})^{**}}{\Delta_{k+1,k}}$$

$$(2.142)$$

<span id="page-56-5"></span>
$$-\frac{1}{\Delta_{k}\Delta_{k+1,k}}(t_{yz})_{k-1}^{n+1} + \left[\frac{1}{\Delta_{k}\Delta_{k+1,k}} + \frac{(H^{v})^{n+1}}{2\Delta t} \left(\frac{H^{v}}{A_{v}^{v}}\right)_{k}^{n} + \frac{1}{\Delta_{k+1}\Delta_{k+1,k}}\right] (t_{yz})_{k}^{n+1} - \frac{1}{\Delta_{k+1}\Delta_{k+1,k}} (t_{yz})_{k+1}^{n+1} = \frac{1}{2\Delta t m_{x}^{v}} \frac{(Q_{k+1} - Q_{k})^{**}}{\Delta_{k+1,k}}$$

$$(2.143)$$

{57}------------------------------------------------

2. HYDRODYNAMICS EFDC+ Theory

These equations are diagonally dominant and well conditioned, and can be solved independently at each of the horizontal velocity locations. Since equations (2.142) and (2.143) represent fully implicit, backward difference in time, schemes for one dimensional parabolic diffusion equations, the solutions are unconditionally stable (Fletcher, 1988). Given the solutions of the equations (2.142) and (2.143), the shear stresses, the K-1 transport differences,  $P_{k+1}-P_k$ , and  $Q_{k+1}-Q_k$ , are determined from equations (2.140) and (2.141) and combined with the continuity constraints, equations (2.106) and (2.107), to form a pair of K equations for the horizontal transports in each cell layer. To illustrate, the horizontal transports in the surface cell layer are determined analytically and given as

$$P_k = \hat{P} + \sum_{k=1}^{K-1} \left( \sum_{j=1}^k \Delta_j \right) (P_{k+1} - P_k). \tag{2.144}$$

A similar expression can be derived for  $Q_K$ . Working down from the surface using the K-1 transport differences allows the remaining transports to be determined. It is noted for later use that the bottom cell layer transports can be expressed in terms of the depth integrated transports and the transport differences using:

<span id="page-57-1"></span>
$$P_1 = \hat{P} - \sum_{k=1}^{K-1} \left( 1 - \sum_{j=1}^k \Delta_j \right) (P_{k+1} - P_k), \tag{2.145}$$

and an identical equation for  $Q_1$ .

The solution of equations (2.142) and (2.143) requires specification of bottom and surface stresses at k = 0 and k = K, respectively. On the free surface, (k = K) the surface wind stress components are specified. On the bottom fluid-solid boundary, (k = 0) the bottom stress must be specified. The simplest approach to specifying the bottom stress components utilizes the velocity component in the bottom cell layer and the quadratic friction relations shown in equations (2.146) and (2.146).

$$(\tau_{xz})_0^{n+1} = C_b \left( \sqrt{(u_1)^2 + (v_1^u)^2} \right)^n \left( \frac{P_1}{m_y^u H^u} \right)^{n+1}$$
 (2.146)

$$(t_{yz})_0^{n+1} = C_b \left( \sqrt{(u_1^{\nu})^2 + (\nu_1)^2} \right)^n \left( \frac{Q_1}{m_x^{\nu} H^{\nu}} \right)^{n+1}$$
(2.147)

Assuming a logarithmic velocity profile between the solid bottom and the middle of the bottom cell layer gives the bottom stress coefficient:

<span id="page-57-2"></span><span id="page-57-0"></span>
$$C_b = \frac{\kappa^2}{\left[\ln\left(\frac{\Delta_1 H}{2z_0^*}\right)\right]^2} \tag{2.148}$$

where  $z_o^*$  is the dimensional bottom roughness height. Inserting equation (2.145) and a corresponding equation for  $Q_1$  into equations (2.146) and (2.147), respectively allows the bottom stresses at time level n + 1

{58}------------------------------------------------

to be expressed in terms of the depth integrated transport components, known from the external mode solution, and the unknown transport differences at time level n + 1. However, the transport differences at time level n + 1 are related to the shear stress components by equations (2.140) and (2.141), allowing the bottom stresses to be expressed in terms of the depth integrated transports and the internal shear stresses by:

$$(\tau_{xz})_0^{n+1} = C_b \left( \sqrt{(u_1)^2 + (v_1^u)^2} \right)^n \left[ \left( \frac{\hat{P}}{m_y^u H^u} \right)^{n+1} - \sum_{k=1}^{K-1} \left( 1 - \sum_{j=1}^k \Delta_j \right) \frac{\Delta_{k+1,k} (\tau_{xz})_k^{n+1}}{\left( \frac{A_y^u}{H^u} \right)_k^n} \right], \tag{2.149}$$

and a similar expression for the y component. Inserting equation (2.149) and the corresponding y component equation for the bottom stress components into the k = 1 pair of equations (2.142) and (2.143) results in a nearly tri-diagonal system with a fully populated first row. The systems of equations are still efficiently solved using a tri-diagonal equation solver and the Sherman-Morrison formula (Press et al., 1986).

The internal mode solution is completed by the determination of the vertical velocity using:

<span id="page-58-3"></span><span id="page-58-2"></span>
$$w_k = w_{k-1} - \frac{\Delta_k}{m^{\zeta}} \left[ \delta_x^{\zeta} \left( P_k - \hat{P} \right) + \delta_y^{\zeta} \left( Q_k - \hat{Q} \right) \right]$$
 (2.150)

which follows from the equation (2.111). The solution of equation (2.150), where all variables are at time level n+1, proceeds from k=1 since  $w_o=0$ . A two time level correction step is also periodically inserted into the internal mode time integration on the same time step as the external mode correction. The computational equations follow directly from the three time level equations using the details of the external mode presented in Section 2.4..

#### <span id="page-58-0"></span>2.6. Vertical Layering Options

This section summarizes the vertical coordinate options in EFDC+. It supplements the theoretical and computational description of the basic EFDC+ hydrodynamic and transport model components. The EFDC+ model was originally formulated with a SIG stretched vertical coordinate. Later, more efficient vertical layering options, namely SGZ options have been implemented to reduce the error due to the horizontal pressure gradients and to reduce the number of computational cells.

#### <span id="page-58-1"></span>2.6.1 Standard Sigma (SIG) Approach

The SIG approach is a topographically conformal vertical coordinate system which is widely used in threedimensional hydrodynamic models. In this vertical coordinate system, the number of vertical levels in the water column is the same everywhere in the domain irrespective of the depth of the water column (Figure 2.9(a)). This can resolve the water column equally well and equally efficiently in both shallow and deep regions of a computational domain simultaneously and it is suitable for a water body with complicated geometry and large changes in bottom elevation. The transformation of the governing equations using sigma-coordinate in the vertical is described in the Section 2.1.

In the SIG coordinate formulation, the number of vertical layers is the same at all horizontal locations in the model grid. Although this formulation is widely accepted, conceptually attractive and adequate for a large range of applications, there are numerous application classes where a traditional z or physical vertical

{59}------------------------------------------------

<span id="page-59-1"></span>Fig. 2.9. An Illustration of [EFDC+](#page-11-0) Layering Options for a Model with *K* = 10. (a) [SIG,](#page-12-0) (b) [SGZ-](#page-12-1)Specified Bottom, and (c) [SGZ-](#page-12-1)Uniform Layering.

grid is desirable, such as deep reservoirs with rapid and large lateral bathymetric changes. There are also applications where the ability to use a combination of [SIG](#page-12-0) and physical *z* vertical layering in different regions of the horizontal domain would be desirable. An example would be a deep navigation channel in an otherwise shallow estuary. The [SIG](#page-12-0) stretched vertical grid formulation may also be subject to internal pressure gradient errors [\(Mellor et al.,](#page-263-11) [1994\)](#page-263-11) providing another motivation for having alternative options to the sigma formulation.

#### <span id="page-59-0"></span>2.6.2 Sigma-Zed Approach (SGZ)

The [SIG](#page-12-0) grid used for the transformation of the vertical coordinate introduces a well-known error in the horizontal gradient terms including the concentration, velocity, and pressure [\(Mellor et al.,](#page-263-11) [1994\)](#page-263-11). In general, this error is significant only in the regions with steeply varying bathymetry. In order to overcome this weakness, two new vertical layering approaches that are computationally efficient have been developed and applied in [EFDC+](#page-11-0) model [\(Craig et al.,](#page-259-1) [2014\)](#page-259-1). The vertical layering scheme has been modified to allow the number of layers to vary over the model domain based on the water depth. Consequently, each cell can have a different number of layers. The *z* coordinate system varies for each cell face, matching the number of active layers to the adjacent cells (face matching of layering is a fundamental difference with the GVC approach). Such a transformation is referred to as the [SGZ](#page-12-1) coordinate. The differences in the two optional [SGZ](#page-12-1) approaches relate to the [SIG](#page-12-0) layer thickness computed for each cell. Figure [2.9](#page-59-1) shows a schematic demonstrating the layering options. Panel (a) represents a [SIG](#page-12-0) stretch grid with 10 layers. Panels (b) represents the specified bottom approach which allows a user specified number of layers in each horizontal cell. Figure [2.9\(](#page-59-1)c) represent [SGZ](#page-12-1) options with uniform layering where the bottom of each vertical layer are aligned in the horizontal direction. It should be noted that, in [SGZ](#page-12-1) coordinate the number of vertical layers can be very large, but the computational time is shorter in comparison with a similarly configured [SIG](#page-12-0) coordinate model.

A new vertical layering option following the Sigma-Zed (SGZ Specified Thickness from Top ) approach has recently been added to EEMS 12.1. When using this approach, the user can configure the model layers not as relative splits but as actual layer thicknesses in meters. The layers are built starting from the top, and the 

{60}------------------------------------------------

2. HYDRODYNAMICS EFDC+ Theory

bottom of each layer is aligned in the horizontal direction. Similar to a Z grid, this option gives the user the flexibility to specify the layer thickness and the maximum depth of the model domain to generate an appropriate vertical layering scheme.

For [SGZ](#page-12-1) transformation, the equations are still the same as the [SIG](#page-12-0) transformation, however, the number of layers at each cell differs based on a factor determined based on the ratio between bed elevation and the minimum elevation. In addition, the thickness of layers at each cell must satisfy

$$\sum_{k=n}^{KC} \Delta z_k = 1, \tag{2.151}$$

in which *KC* is the maximum number of layers, *n* the index of bottom layer and ∆*z<sup>k</sup>* the thickness of layer *k*.

For the original [SIG](#page-12-0) the index of the bed layer always is equal to *n* = 1 while in the [SGZ](#page-12-1) this value can vary in the range 1 ≤ *n* ≤ *K* depending on the number of layers due to the rescaling. This requirement improves the accuracy of the horizontal gradient calculation for the variable *Ci*, *<sup>j</sup>*,*<sup>k</sup>* of the cell *L*(*i*, *j*) at layer *k* :

$$pd[C_{i,j,k}]x = \frac{C_{i,j,k} - C_{i-1,j,k}}{\Delta x}.$$
(2.152)

When sediment transport is simulated and bed morphology is considered, the determination of the new indices of bottom layers should be implemented at every time step. This is because currently the ratios between water depths and the maximum are changing due to erosion or deposition compared to the previous time step. Therefore, an update of layering for the whole domain is important and necessary for [SGZ.](#page-12-1) However, the re-layering is only an optional approach.

The other necessary modification for [SGZ](#page-12-1) coordinate system is the treatment on wet/dry in 3-D calculation of the horizontal gradient when the number of layers at cell *L*(*i* − 1, *j*) is less than that at cell *L*(*i*, *j*). It should be noted that this problem does not appear for [SIG](#page-12-0) coordinates, because the number of layers is the same for every cell. This means that the [SIG](#page-12-0) model requires more calculation time than the model with [SGZ](#page-12-1) approach.

#### <span id="page-60-0"></span>2.7. Near-Field Discharge Dilution and Mixing Zone Analysis

The calculation procedure of the jet/plume submodel is mainly based on [Lee and Cheung](#page-262-4) [\(1990\)](#page-262-4). The trajectory of a group of plume particles is traced in time using a Lagrangian formulation. The plume puff gains mass as ambient fluid is entrained and mixed within it, but once entrained, the new mass becomes an indistinguishable part of the plume puff. In the simplest version, the plume is assumed to be essentially a cylindrical segment whose radius grows as mass is entrained. The initial plume mass is identified as the mass issuing from a diffuser with radius *b*<sup>0</sup> :

$$M_0 = \rho_0 \pi b_0^2 h_0, \tag{2.153}$$

where, *M*<sup>0</sup> is the initial mass, ρ<sup>0</sup> is the initial density, *b*<sup>0</sup> is the diffuser radius, *h*<sup>0</sup> is the length of the plume mass and is chosen to be comparable to *b*0. For example, *h*<sup>0</sup> = *r* and *b*<sup>0</sup> = *r*, where *r* is the radius of the diffuser. The initial length of the plume can be estimated from the initial plume velocity *V*<sup>0</sup> and time ∆*t*:

{61}------------------------------------------------

<span id="page-61-2"></span>
$$h_0 = V_0 \Delta t \tag{2.154}$$

The increment in the plume mass at the time step *n th* is evaluated as the sum of the plume mass increment due to the shear-induced entrainment and the forced entrainment.

$$\Delta M_n = \Delta M_s + \Delta M_f \tag{2.155}$$

In equation [\(2.155\)](#page-61-2) ∆*M<sup>s</sup>* is the increase in mass due to shear entrainment, and ∆*M<sup>f</sup>* is the increase in mass due to forced entrainment. A schematic of a rising plume discharged into a water body is shown in Figure [2.10.](#page-61-1)

<span id="page-61-1"></span>Fig. 2.10. Near field Jet Plume mixing.

#### <span id="page-61-0"></span>2.7.1 Shear-Induced Entrainment

The increase in mass of the plume element is due to turbulent entrainment of the ambient flow. Close to the discharge point, or in a very weak current, shear-induced entrainment dominates. In general, however, the forced entrainment of the cross flow dominates, except very close to the source. In the model, assuming the total entrainment is a function of the horizontal currents and a shearing action of the plume relative to the currents, the increase in mass due to shear entrainment, ∆*M<sup>s</sup>* , is written as

$$\Delta M_s = \rho_a 2\pi b_n h_n E \left| V_n - u_a \cos \phi_n \cos \theta_n \right| \Delta t. \tag{2.156}$$

Where the jet axis makes an angle of φ*<sup>n</sup>* with the horizontal plane, and θ*<sup>n</sup>* is the angle between the *x*-axis and the projection of the jet axis on the horizontal plane. ρ*<sup>a</sup>* is the ambient density and *u<sup>a</sup>* is the ambient current. 

{62}------------------------------------------------

The subscript n denotes the value of plume element at n<sup>th</sup> step of calculation, the subscript a denotes the local ambient value, E is the entrainment coefficient which is dependent on the local densimetric Froude number  $F_1$  and jet orientation

$$E = \sqrt{2} \frac{0.057 - 0.554 \frac{\sin \theta_n}{F_1^2}}{1 + 5 \frac{u_a \cos \phi_n \cos \theta_n}{|V_n - u_a \cos \phi_n \cos \theta_n|}},$$
(2.157)

where,  $F_1$  is the local densimetric Froude number, and is given by

<span id="page-62-2"></span>
$$F_1 = \alpha \frac{|V_n - u_a \cos \phi_n \cos \theta_n|}{\sqrt{g \frac{\Delta \rho_n}{\rho_a} b_n}},$$
(2.158)

and  $\alpha$  is a proportionality constant.

#### <span id="page-62-0"></span>2.7.2 Forced Entrainment

Experimental observations by Chu and Goldberg (1984) and Stuart Churchill (1975) have shown that the transfer of horizontal momentum is complete beyond a few jet diameters. We assume that all the ambient flow on the downdrift side of the plume is entrained into the plume element. This forced entrainment of the ambient flow into an arbitrarily inclined plume element can be formulated as

$$\Delta M_f = \rho_a u_a \left[ 2b\Delta s \sqrt{1 - \cos^2 \phi \cos^2 \theta} + \pi b\Delta b \cos \phi \cos \theta + \frac{1}{2}\pi b^2 \Delta (\cos \phi \cos \theta) \right]$$
 (2.159)

In the equation 2.159, the first term represents the forced entrainment due to the projected plume area normal to the cross flow; the second term is a correction due to the growth of plume radius; and the third term is a correction due to the curvature of the trajectory.  $\Delta s$  is the arc length of the centerline axis of the plume element subtending an angle  $\Delta \phi$  at the center of curvature.

An initial estimate of  $\Delta M_f$  can be obtained as

$$\Delta M_f = \rho_a u_a h_n b_n \left[ 2\sqrt{\left(\sin^2 \phi + \sin^2 \theta - \sin^2 \phi \sin^2 \theta\right)_n} + \pi \left(\frac{\Delta b}{\Delta s} \cos \phi \cos \theta\right)_n + \frac{\pi b_n}{2} \frac{\left(\cos \phi \cos \theta\right)_n - (\cos \phi \cos \theta)_{n-1}}{\Delta s_n} \right] \Delta t$$
(2.160)

#### <span id="page-62-1"></span>2.7.3 Model Implementation

At the  $n^{\text{th}}$  step, consider a plume element located at  $(x_n, y_n, z_n)$  with the velocity  $(u_n, v_n, w_n)$  and its magnitude  $V_n$ . The jet axis makes an angle of  $\phi_n$  with the horizontal plane, and  $\theta_n$  is the angle between the x-axis and the projection of the jet axis on the horizontal plane. The half-width or radius of the plume element

{63}------------------------------------------------

2. HYDRODYNAMICS EFDC+ Theory

is *bn*; *h<sup>n</sup>* is the thickness, defined as proportional to the magnitude of the local jet velocity, *h<sup>n</sup>* = *Vn*∆*t*. The mass of the plume element is then given by

$$M_n = \rho_n \pi b_n^2 h_n \tag{2.161}$$

Given the increase in mass due to turbulent entrainment, ∆*M<sup>n</sup>* the plume element characteristics at the next step are obtained by applying conservation of mass, horizontal and vertical momentum, energy, and tracer mass to the discrete element. For completeness, the self-explanatory equations of the generalized Lagrangian model, essentially similar to its original two-dimensional counterpart [\(Winiarski and Frick,](#page-265-6) [1976\)](#page-265-6) are summarized as follows:

Mass conservation:

$$M_{n+1} = M_n + \Delta M_n \tag{2.162}$$

$$M_{n+1} = \rho_{n+1} \pi b_{n+1}^2 h_{n+1} \tag{2.163}$$

The concentration of the tracer, salinity, temperature and water density:

$$C_{n+1} = \frac{M_n C_n + \Delta M_n C_a}{M_{n+1}} \tag{2.164}$$

$$S_{n+1} = \frac{M_n S_n + \Delta M_n S_a}{M_{n+1}} \tag{2.165}$$

$$T_{n+1} = \frac{M_n T_n + \Delta M_n T_a}{M_{n+1}} \tag{2.166}$$

$$\rho_{n+1} = \rho \left( S_{n+1}, T_{n+1} \right) \tag{2.167}$$

The horizontal momentum:

$$u_{n+1} = \frac{M_n u_n + \Delta M_n u_a}{M_{n+1}} \tag{2.168}$$

$$v_{n+1} = \frac{M_n v_n}{M_{n+1}} \tag{2.169}$$

The vertical momentum

$$w_{n+1} = \frac{M_n w_n + \Delta M_{n+1} \left(\frac{\Delta \rho}{\rho}\right)_{n+1} g \Delta t}{M_{n+1}}$$
(2.170)

{64}------------------------------------------------

$$(Mw)_{n+1} = (Mw)_n + (\Delta \rho V)_{n+1} g \Delta t$$
 (2.171)

where,

$$V_{n+1} = \sqrt{u_{n+1}^2 + v_{n+1}^2 + w_{n+1}^2},$$
 and (2.172)

$$U_{n+1} = \sqrt{u_{n+1}^2 + v_{n+1}^2} (2.173)$$

The new thickness and radius of the plume element:

$$h_{n+1} = \frac{V_{n+1}}{V_n} h_n (2.174)$$

$$b_{n+1} = \sqrt{\frac{M_{n+1}}{\pi \rho_{n+1} h_{n+1}}} \tag{2.175}$$

The jet orientation:

$$\phi_{n+1} = \arctan\left(\frac{w_{n+1}}{U_{n+1}}\right) \tag{2.176}$$

$$\theta_{n+1} = \arctan\left(\frac{v_{n+1}}{u_{n+1}}\right) \tag{2.177}$$

The new location of the plume element:

$$x_{n+1} = x_n + u_{n+1} \Delta t (2.178)$$

$$y_{n+1} = y_n + v_{n+1}\Delta t (2.179)$$

$$z_{n+1} = z_n + w_{n+1} \Delta t \tag{2.180}$$

The distance along the trajectory:

$$\Delta s_{n+1} = V_{n+1} \Delta t \tag{2.181}$$

The time step ∆*t* can be fixed or variable; its is chosen via a "prediction-correction" procedure to attain a prescribed fractional change in mass (typically of the order of 1%) at each step.

#### <span id="page-64-0"></span>2.8. Conclusion

In this chapter, the theoretical aspect of basic for the EFDC+ hydrodynamics are presented, including the governing equations, vertical layering options, near-field discharge, and external forcing options, such as wave models. The following chapters describe how the density effects for temperature and salinity may be incorporated into the hydrodynamic module, as well as linkage to constituent transport modules.

{65}------------------------------------------------

## <span id="page-65-0"></span>Chapter 3

## CONSERVATIVE CONSTITUENTS TRANSPORT

### <span id="page-65-1"></span>3.1. Introduction

This section summarizes the theoretical and computational aspects of the transport formulations for passive scalar transport used in [EFDC+.](#page-11-0) Theoretical and computational aspects for the [EFDC](#page-11-2) generic transport model components are presented in [Hamrick](#page-261-3) [\(1992\)](#page-261-3).

#### <span id="page-65-2"></span>3.2. Basic Equation of Advection-Diffusion Transport

The generic transport equation for a dissolved or suspended material is shown in equation [\(3.1\)](#page-65-3):

<span id="page-65-3"></span>
$$\frac{\partial}{\partial t} (m_x m_y HC) + \frac{\partial}{\partial x} (m_y HuC) + \frac{\partial}{\partial y} (m_x HvC) + \frac{\partial}{\partial z} (m_x m_y wC) - \frac{\partial}{\partial z} (m_x m_y w_{sc}C) \\
= \frac{\partial}{\partial x} \left( \frac{m_y}{m_x} HA_H \frac{dC}{dx} \right) + \frac{\partial}{\partial y} \left( \frac{m_x}{m_y} HA_H \frac{dC}{dy} \right) + \frac{\partial}{\partial z} \left( \frac{m_x m_y}{H} A_b \frac{dC}{dz} \right) + S_C \quad (3.1)$$

where,

*x*, *y* are the orthogonal curvilinear coordinates in the horizontal direction (m),

*z* is the sigma coordinate (dimensionless),

*t* is time (s),

*mx*, *m<sup>y</sup>* are the square roots of the diagonal components of the metric tensor (dimensionless),

*m* is the Jacobian of the metric tensor determinant (dimensionless), *m* = *mxmy*,

*C* is the concentration or intensity of transport constituent (g/m<sup>3</sup> for concentration of dissolved/suspended material, ◦C for temperature, ppt for salinity),

*H* is the total water depth (m),

*u*, *v* are the horizontal velocity components in the curvilinear coordinates (m/s),

{66}------------------------------------------------

- *w* is the vertical velocity component (m/s),
- *A<sup>H</sup>* is the horizontal turbulent eddy diffusivity (m<sup>2</sup> /s),
- *A<sup>b</sup>* is the vertical turbulent eddy diffusivity (m<sup>2</sup> /s),
- *wsc* is a positive settling velocity when *C* represents a suspended material, and
- *S<sup>c</sup>* is the source/sink term for the constituent that includes subgrid scale horizontal diffusion and thermal sources and sinks.

## <span id="page-66-0"></span>3.3. Numerical Solution for Transport Equations

<span id="page-66-1"></span>In this section, solutions techniques for the transport equations for salinity, temperature, turbulence intensity, and turbulence length scale are presented. Stability and accuracy aspects of the advection schemes common to the transport equations and the external and internal horizontal momentum equations are also discussed. The salinity transport equation [\(3.2\)](#page-66-2) is used as a generic example and the location of variables is shown in Figure [3.1.](#page-66-1)

<span id="page-66-2"></span>Fig. 3.1. S-centered Grid in the Vertical (*x*,*z*)-Plane

The salinity transport equation [\(3.2\)](#page-66-2) is integrated over a cell layer to give:

$$\frac{\partial}{\partial t} (mHC_k) + \frac{\partial}{\partial x} (P_k C_k) + \frac{\partial}{\partial y} (Q_k C_k) + \frac{(WC)_k - (WC)_{k-1}}{d_k} - \frac{m}{d_k} \left[ \left( \frac{A_b}{H} \frac{dC}{dz} \right)_k - \left( \frac{A_b}{H} \frac{dC}{dz} \right)_{k-1} \right] - (S_C)_k = 0 \quad (3.2)$$

where, *Pk*, *Qk*, and *W<sup>k</sup>* are defined by equations [\(2.94\)](#page-45-3) and [\(2.135\)](#page-55-4). The source, sink, advection, and vertical diffusion portions of equation [\(3.2\)](#page-66-2) are treated in separate fractional steps, as was done for the internal mode momentum equations in Section [2.4.](#page-49-0)

{67}------------------------------------------------

<span id="page-67-0"></span>**Fig. 3.2.** Sigma Coordinate and Variable Center (Ji, 2008).

The three time level fractional step sequence is given by:

<span id="page-67-4"></span><span id="page-67-3"></span><span id="page-67-2"></span><span id="page-67-1"></span>
$$C_k^* = C_k^{n-1} + \frac{2dt}{mH^{n-1}} (S_C)_k^{n-1}$$
(3.3)

$$(mH)^{n+1}C_k^{**} = (mH)^{n-1}C_k^* - 2dt \left[ d_x^d (P_k C_k) + d_y^d (Q_k C_k) + \frac{(WC)_k - (WC)_{k-1}}{d_k} \right]$$
 (3.4)

$$(HC_k)^{n+1} - 2dt \left\{ \left[ \left( \frac{A_b}{H} \right)_k^n \frac{(C_{k+1} - C_k)^{n+1}}{d_k d_{k+1,k}} \right] - \left[ \left( \frac{A_b}{H} \right)_{k-1}^n \frac{(C_k - C_{k-1})^{n+1}}{d_k d_{k,k-1}} \right] \right\} = H^{n+1} C_k^{**}$$
 (3.5)

The source, sink step (see equation (3.3)) is explicit and involves no changes in cell volumes. When the source, sink term represents horizontal turbulent diffusion, it is evaluated at time level n-1, for stability (Fletcher, 1988). The advection step, equation (3.4), is explicit and involves changes in cell volumes. The vertical diffusion step, equation (3.5), which involves no changes in cell volumes, is fully implicit and unconditionally stable (Fletcher, 1988).

Rearranging equation (3.5), the vertical diffusion step, gives:

$$-\frac{2dt}{d_{k}d_{k,k-1}} \left(\frac{A_{b}}{H}\right)_{k-1}^{n} C_{k-1}^{n+1} + \left[\frac{2dt}{d_{k}d_{k,k-1}} \left(\frac{A_{b}}{H}\right)_{k-1}^{n} + H^{n+1} + \frac{2dt}{d_{k}d_{k+1,k}} \left(\frac{A_{b}}{H}\right)_{k}^{n}\right] C_{k}^{n+1} - \frac{2dt}{d_{k}d_{k+1,k}} \left(\frac{A_{b}}{H}\right)_{k}^{n} C_{k+1}^{n+1} = H^{n+1} C_{k}^{**}$$
(3.6)

For salinity, temperature, and suspended sediment concentration, the generic variable C is defined vertically at cell layer centers, and the diffusivity is defined at cell layer interfaces. Equation (3.6) then represents

{68}------------------------------------------------

a system of K equations and the boundary conditions are generally of the specified flux type. Specified surface and bottom flux boundary conditions are most conveniently incorporated in the surface and bottom cell layer source and sink terms allowing  $A_b$  at the bottom boundary (k = 0) and the surface boundary (k = k + 1) to be set to zero making equation (3.6) tri-diagonal. For turbulence intensity and turbulence length scale, equations (2.24) and (2.25), the generic variable C is defined vertically at cell layer interfaces and the diffusivity is defined at cell layer centers. Equation (3.6) then represents a system of K - 1 equations for the variables at internal interfaces with the variable values at the free surface and bottom being provided as boundary conditions. For the turbulence intensity and length scale, the boundary conditions are:

$$q_0^2 = B_1^{2/3} \sqrt{t_{bx}^2 + t_{by}^2}, l_0 = 0, \text{ at } z = 0$$
 (3.7)

<span id="page-68-0"></span>
$$q_K^2 = B_1^{2/3} \sqrt{t_{sx}^2 + t_{sy}^2}, l_K = 0, \text{ at } z = 1$$
 (3.8)

where,  $\tau_b$  and  $\tau_s$  are the bottom and surface stress vectors, respectively. Insertion of these boundary conditions results in equation (3.6) representing tri-diagonal systems of K-1 equations for the turbulence intensity and length scale.

Without loss of generality, the notation used in analyzing the three time level advection step, equation (3.4), is simplified by replacing the double and single asterisk intermediate time level indicators by n+1 and n-1, respectively to give:

$$(mHC_k)^{n+1} = (mHC_k)^{n-1} - 2\frac{dt}{dx} \left[ (PC)_{i+\frac{1}{2},j,k} - (PC)_{i-\frac{1}{2},j,k} \right] - 2\frac{dt}{dy} \left[ (QC)_{i,j+\frac{1}{2},k} - (QC)_{i,j-\frac{1}{2},k} \right] - 2\frac{dt}{dk} \left[ (WC)_k - (WC)_{k-1} \right]$$
(3.9)

where the horizontal central difference operators have been expanded about the cell volume centroid (x,y), according to equations (2.120) and (2.121). The cell face fluxes can be represented consistent with centered in time and space differencing as was illustrated by equations (2.122), (2.123) and (2.136) or forward in time and backward or upwind in space as was illustrated by equations (2.124) and (2.137) for the x momentum fluxes. For the centered in time and space form, equation (3.9) becomes:

$$(mHC_{k})^{n+1} = (mHC_{k})^{n-1} - \frac{dt}{dx} \left[ \tilde{P}_{i+\frac{1}{2},j,k} \left( C_{i+1,j,k} + C_{i,j,k} \right) - \tilde{P}_{i-\frac{1}{2},j,k} \left( C_{i,j,k} + C_{i-1,j,k} \right) \right] - \frac{dt}{dy} \left[ \tilde{Q}_{i,j+\frac{1}{2},k} \left( C_{i,j+1,k} + C_{i,j,k} \right) - \tilde{Q}_{i,j-\frac{1}{2},k} \left( C_{i,j,k} + C_{i,j-1,k} \right) \right] - \frac{dt}{dk} \left[ \tilde{W}_{i,j,k} \left( C_{i,j,k+1} + C_{i,j,k} \right) - \tilde{W}_{i,j,k-1} \left( C_{i,j,k} + C_{i,j,k-1} \right) \right]$$
(3.10)

The transports in equation (3.10) are evaluated at the centered time level when used in the external and internal momentum equations, and are averaged to the centered time level using

<span id="page-68-1"></span>
$$\tilde{P}_k = \frac{1}{2} \left( P_k^{n+1} + P_k^{n-1} \right) \tag{3.11}$$

when used in the transport equations for scalar variables.

{69}------------------------------------------------

## <span id="page-69-0"></span>Chapter 4

## DYE MODULE

The dye constituent in [EFDC+](#page-11-0) represents a dissolved substance in the water column that does not impact the hydrodynamics (i.e. no impact on thermal physical properties such as density and viscosity) or any other water column process (e.g. light extinction). This constituent can be used as a tracer, with or without decay, or it can also be used to compute the age of water in days.

The dye is transported in the water column as determined by the equation [\(4.1\)](#page-69-2).

$$\frac{\partial}{\partial t} (m_x m_y HC) + \frac{\partial}{\partial x} (m_y HuC) + \frac{\partial}{\partial y} (m_x HvC) + \frac{\partial}{\partial z} (m_x m_y wC) - \frac{\partial}{\partial z} (m_x m_y w_{sc}C) 
= \frac{\partial}{\partial x} \left( \frac{m_y}{m_x} HA_H \frac{dC}{dx} \right) + \frac{\partial}{\partial y} \left( \frac{m_x}{m_y} HA_H \frac{dC}{dy} \right) + \frac{\partial}{\partial z} \left( \frac{m_x m_y}{H} A_b \frac{dC}{dz} \right) + \frac{dC}{dt} + S_C \quad (4.1)$$

#### <span id="page-69-1"></span>4.1. Decay

The dye constituent can be configured to decay with a zeroth or first order approach, as shown in the equations [\(4.2\)](#page-69-3) and [\(4.3\)](#page-69-4), respectively.

<span id="page-69-3"></span><span id="page-69-2"></span>
$$\frac{dC}{dt} = -K \tag{4.2}$$

<span id="page-69-4"></span>
$$\frac{dC}{dt} = -KC \tag{4.3}$$

In equations [4.2](#page-69-3) and [4.3,](#page-69-4) *C* is the dye concentration in *g*/*m* 3 , *K* is the first order decay rate in 1/*s* and *t* is time is seconds.

Additionally, dye decay rate can be a function of water temperature using the equation [\(4.4\)](#page-69-5).

<span id="page-69-5"></span>
$$\frac{dC}{dt} = -K\theta^{(T-T_{ref})}C\tag{4.4}$$

{70}------------------------------------------------

4. DYE MODULE EFDC+ Theory

## <span id="page-70-0"></span>4.2. Age of Water

As mentioned, the dye constituent may be used to calculate the age of water (in days). With this option, a zero-order kinetic rate approach is used:

$$\frac{dC}{dt} = -K \tag{4.5}$$

where *C* is "age" in days, *t* is time in days and *K* is in units of 1/day. By averaging cell ages over all or parts of the model domain, residence times can be computed. If the model is run sufficiently long enough to achieve a dynamic steady state, the hydraulic residence time can be computed.

{71}------------------------------------------------

## <span id="page-71-0"></span>Chapter 5

## TEMPERATURE AND HEAT TRANSFER

<span id="page-71-1"></span>This chapter presents an overview of heat transfer implemented in [EFDC+,](#page-11-0) including the energy equation and heat transfer options. Additional details are given regarding the processes for water column temperature, surface and bed heat exchange, and ice formation and melt. The sources of heat in the system include surface heat exchange, short wave radiation absorption, bottom heat exchange, and any inflow or outflow (e.g. boundary condition). The conceptual framework for temperature is shown in Figure [5.1.](#page-71-1)

Fig. 5.1. Conceptual Framework for Temperature.

The basic equation for heat transfer in curvilinear and sigma coordinates is the generic transport equation [3.1.](#page-65-3) To solve the equation for heat transport; hydrodynamic transport, turbulent mixing, and horizontal diffusion are provided by the hydrodynamic module.

{72}------------------------------------------------

## <span id="page-72-0"></span>5.1. Surface Heat Exchange

At the water surface (*z* = 1), the boundary condition for the heat exchange can be calculated as

$$-\frac{\rho c_p A_b}{H} \frac{\partial T}{\partial z} = H_L + H_E + H_C \tag{5.1}$$

where,

ρ is the water density (*kg*/*m* 3 ),

*c<sup>p</sup>* is the specific heat of water (*J*/*kg*/ ◦*C*)),

*A<sup>b</sup>* is the vertical eddy diffusivity (*m* <sup>2</sup>/*s*),

*H* is the water depth (*m*),

*H<sup>L</sup>* is the surface heat exchange flux due to long wave back radiation (*W*/*m* 2 ),

*H<sup>E</sup>* is the surface heat exchange flux due to latent heat (*W*/*m* 2 ), and

*H<sup>C</sup>* is the surface heat exchange flux due to sensible heat (*W*/*m* 2 ).

The surface heat exchange is calculated using three methods:

- 1. Full Heat Balance
- 2. COARE 3.6 bulk algorithm
- 3. Equilibrium Temperature

## <span id="page-72-1"></span>5.1.1 Full Heat Balance

In the full heat balance method, the heat exchange flux due to long wave back radiation, latent heat, and sensible heat are calculated based on the approach proposed by [Rosati and Miyakoda](#page-264-11) [\(1988\)](#page-264-11) and [Hamrick](#page-261-3) [\(1992\)](#page-261-3).

$$H_L = \varepsilon \sigma (T_s + 273.15)^4 (0.39 - 0.05\sqrt{e_a}) (1 + B_c C) + 4\varepsilon \sigma (T_s + 273.15)^3 (T_s - T_a)$$
 (5.2)

$$H_E = c_e \rho_a L_E W_s (e_s - e_a) \frac{0.622}{P_a}$$
 (5.3)

$$H_C = c_h \rho_a c_{pa} W_s \left( T_s - T_a \right) \tag{5.4}$$

where,

- ε is the emissivity of the waterbody (ε = 0.97),
- σ is the Stefan–Boltzmann constant (σ = 5.67×10−<sup>8</sup> W/m2/K 4 ),
- *C* is the cloud fraction (*C* = 0 : cloudless, *C* = 1 : full cloud coverage),
- *B<sup>c</sup>* is an empirical constant (*B<sup>c</sup>* = 0.8),

{73}------------------------------------------------

*Ts* is the water surface temperature (◦*C*),

*T<sup>a</sup>* is the air temperature (◦*C*),

*ce*, *c<sup>h</sup>* are the turbulent exchange coefficients,

ρ*<sup>a</sup>* is the atmospheric density (ρ*<sup>a</sup>* = 1.2 *kg*/*m* 3 ),

*cpa* is the specific heat of air (*cpa* = 1005 *J*/*kg*/*K*),

*L<sup>E</sup>* is the latent heat of evaporation (*L<sup>E</sup>* = 2.501×10<sup>6</sup> *J*/*kg*),

*Ws* is the wind speed (*m*/*s*),

*es* is the saturation vapor pressure at surface water temperature (*mb*),

*e<sup>a</sup>* is the actual vapor pressure (*mb*), and

*P<sup>a</sup>* is the atmospheric pressure (*mb*).

The full heat balance method in the EFDC+ (non-legacy option) is fully linked with the ice module that incorporates ice growth and melt processes.

## <span id="page-73-0"></span>5.1.2 COARE 3.6 Bulk Algorithm

From [EFDC+](#page-11-0) 12.1, the Coupled Ocean–Atmosphere Response Experiment (COARE) module version 3.6 has been implemented in the EFDC+ code as a new option for the calculation of water surface heat exchange. The algorithm of COARE, developed by C. Fairall, E. F. Bradley, and D. Rogers (see [Fairall et al.](#page-260-2) [\(1996\)](#page-260-2), [Fairall et al.](#page-260-3) [\(2003\)](#page-260-3)), follows the standard Monin-Obukhov similarity theory (MOST) for near-surface meteorological measurements and is designed to give estimates of the turbulent fluxes of sensible and latent heat and the stress from inputs of bulk variables.

Bulk algorithms are based upon MOST representations of the fluxes in terms of mean quantities:

$$\overline{w'x'} = c_x^{1/2} c_d^{1/2} S\Delta X = C_x S\Delta X \tag{5.5}$$

Where *x* can be wind components, the potential temperature, the water vapor specific humidity, etc. Here *c<sup>x</sup>* is the bulk transfer coefficient for the variable *x* and *C<sup>x</sup>* is the total transfer coefficient. Here ∆*X* is the air-sea difference in the mean value of *x*, and *S* is the mean wind speed. As a result, sensible heat *HC*, and latent heat *H<sup>E</sup>* are defined by the normal Reynolds averages,

$$H_C = \rho_a c_{pa} \overline{w'T'} = \rho_a c_{pa} C_h S(T_s - \theta)$$
(5.6)

$$H_E = \rho_a L_e \overline{w'q'} = \rho_a L_e C_e S(q_s - q)$$
(5.7)

Where*C<sup>h</sup>* and*C<sup>e</sup>* are the transfer coefficients for sensible heat, and latent heat, respectively; θ is the potential temperature, *q* is the water vapor mixing ratio, and *u<sup>i</sup>* is one of the horizontal wind components. *S* is the average value of the wind speed; *T<sup>s</sup>* is the water surface temperature; *usi* is the surface current; and *q<sup>s</sup>* is the interfacial value of the water vapor mixing ratio.

The water surface is characterized by the velocity roughness, specified as Charnock's expression plus a smooth flow limit,

$$z_0 = \frac{\alpha u_*^2}{g} + \frac{0.11v}{u_*} \tag{5.8}$$

Where *u*<sup>∗</sup> is the friction velocity, and is water kinetic viscosity.

{74}------------------------------------------------

## <span id="page-74-0"></span>5.1.3 Equilibrium Temperature

A computed equilibrium temperature can be used for the surface heat exchange in [EFDC+.](#page-11-0) The approach used here is based on the equilibrium temperature computation approach in the [CE-QUAL-W2 \(W2\)](#page-12-6) [\(Wells](#page-265-7) [and Cole,](#page-265-7) [2000\)](#page-265-7). Equilibrium temperature module is fully linked with ice module that incorporates ice growth and ice melt processes.

Because some of the terms in the term-by-term heat balance equation are surface temperature dependent and others are measurable or computable input variables, the most direct route to simplify computation is to define an equilibrium temperature, *T<sup>e</sup>* as the temperature at which the net rate of surface heat exchange is zero.

Linearization of the term-by-term heat balance along with the definition of equilibrium temperature allows for expression of the net rate of surface heat exchange, *H<sup>n</sup>* as:

$$H_n = -K_{aw} \left( T_s - T_e \right) \tag{5.9}$$

where,

*H<sup>n</sup>* is the rate of surface heat exchange (*W*/*m* 2 ),

*Kaw* is the coefficient of surface heat exchange (*W*/*m* 2/ ◦*C*),

*Ts* is the water surface temperature (◦*C*), and

*T<sup>e</sup>* is the equilibrium temperature (◦*C*).

Seven separate heat exchange processes are summarized in the coefficient of surface heat exchange and equilibrium temperature. In [EFDC+,](#page-11-0) *T<sup>e</sup>* and *Kaw* are computed from heat flux equation where *H<sup>n</sup>* = 0 or approximate technique [\(Brady et al.,](#page-258-5) [1969\)](#page-258-5).

$$T_e = \frac{I_{sw}}{23 + f(W)(\beta + 0.255)} + T_d \tag{5.10}$$

where,

*T<sup>e</sup>* is the equilibrium temperature in ◦F,

*Isw* is the solar radiation at the water surface (*Btu*/ *ft*2/*day*),

β = 0.255−0.0085*T* <sup>∗</sup> +0.000204*T* ∗2,

*T* <sup>∗</sup> = 0.5(*T<sup>s</sup>* +*Td*),

*Ts* is the water surface temperature in ◦F,

*T<sup>d</sup>* is the dew point temperature in ◦F,

*W*<sup>2</sup> is the wind speed at 2*m* in *mph*, and

*K* is computed from the slope of the net flux vs temperature or using the approximate formula in units of *Btu*/ *ft*2/*day*/ ◦*F*.

$$K = 23 + (\beta_w + 0.225) \, 17W_2 \tag{5.11}$$

{75}------------------------------------------------

where,

$$\beta_w = 0.255 - 0.0085T_w - 0.000204T_w^2 \tag{5.12}$$

It must be noted that the equations for heat flux in this method are English units. EFDC+ internally converts the SI units to English units and then converts them back to SI units after the calculation.

#### <span id="page-75-0"></span>5.2. Short Wave Radiation

Short wave solar radiation is an important contributor to the heat balance in water. As the short wave radiation passes from the surface (liquid or ice), the The light extinction coefficient (also referred to as the light attenuation coefficient) is the measure for the reduction (absorption) of light intensity within a water column. The solar radiation at the surface  $I_{sw}$  is a function of location, time of the year, time of day, meteorological conditions, and shading due to terrain and vegetation. The incident solar radiation  $I_0$  is a function of location, time of the year, time of day, and meteorological conditions. The light intensity at the water surface  $I_{sw}$ , is given by:

$$I_{sw} = I_0 S_f \min \left\{ \exp \left[ -K_{eme} (H_{rns} - H) \right], 1 \right\} \min \left\{ \exp \left[ -K_{eice} H_{ice} \right], 1 \right\}$$
 (5.13)

where,

 $I_0$  is the measured solar radiation at the Earth's surface  $(W/m^2)$ ,

 $S_f$  is the tree canopy and/or terrain shading factor (dimensionless),

 $H_{ice}$  is the ice thickness (m),

 $K_{e,ice}$  is the light extinction coefficient for ice cover (1/m),

 $K_{e,me}$  is the light extinction coefficient for emergent shoots (1/m),

 $H_{rps}$  is the rooted plant shoot height (m), and

H is the water column depth (m).

#### <span id="page-75-1"></span>5.2.1 One-band Light Attenuation Model

Solar radiation that penetrates the surface of water is absorbed by water. The absorption heats the water column and radiation penetration depends on the light extinction coefficient,  $\zeta$ . In the water columns, the depth distribution of short-wave radiation is exponential and can be expressed as Beer's Law:

$$I(z) = I_{\text{sw}} \exp\left(-\zeta z\right) \tag{5.14}$$

where,

I(z) is the solar radiation at depth z below the surface  $(W/m^2)$ ,

 $I_{sw}$  is the solar radiation at the water surface  $(W/m^2)$ ,

z is the depth below water surface (m), and

 $\zeta$  is the light extinction coefficient (1/m).

{76}------------------------------------------------

## <span id="page-76-0"></span>5.2.2 Two-band Light Attenuation Model

In this method, the extinction coefficient is constant spatially and temporally, and this method is available for the legacy version of [EFDC.](#page-11-2) The depth distribution of the solar radiation heating is an exponential function using two attenuation coefficients, and is expressed as:

<span id="page-76-3"></span>
$$I(z) = I_{sw} [R \exp(z\zeta_f) + (1 - R) \exp(z\zeta_s)]$$
(5.15)

where,

*I*(*z*) is the solar radiation at water depth *z* (*W*/*m* 2 ),

*Isw* is the solar radiation at water surface (*W*/*m* 2 ),

ζ*f* is the fast attenuation coefficients (1/*m*),

ζ*s* is the slow attenuation coefficients (1/*m*), and

*R* is the fraction of solar radiation fast attenuation, and varies between 0 and 1.

In equation [\(5.15\)](#page-76-3), the first exponential term characterizes the rapid attenuation in the upper 5 meters due to absorption of the red end of the spectrum; the second exponential represents the attenuation of the blue-green light below 10 meters. The selection of *R*, ζ*<sup>f</sup>* , and ζ*<sup>s</sup>* as constant values depends largely on the characteristic optical properties of the water body being simulated. Several authors have derived these parameters based on observed conditions (Table [5.1\)](#page-76-2).

<span id="page-76-2"></span>Table 5.1. Values of parameters determined by fitting the sum of two exponentials to observations of downward irradiance. Table adapted from [Paulson and Simpson](#page-263-0) [\(1977\)](#page-263-0).

| Author                     | Water               | R    | ζf    | ζs    |
|----------------------------|---------------------|------|-------|-------|
|                            | Type                |      | (1/m) | (1/m) |
| Paulson and Simpson (1977) | Run 1               | 0.74 | 0.588 | 0.063 |
|                            | Composite           | 0.62 | 0.667 | 0.050 |
| Kraus and Businger (1994)  | Very Clear Water    | 0.4  | 0.200 | 0.025 |
| Jerlov (1968)              | Type I              | 0.58 | 2.857 | 0.043 |
|                            | Type I (upper 50 m) | 0.68 | 0.833 | 0.036 |
|                            | Type IA             | 0.62 | 1.667 | 0.050 |
|                            | Type IB             | 0.67 | 1.000 | 0.059 |
|                            | Type II             | 0.77 | 0.667 | 0.071 |
|                            | Type III            | 0.78 | 0.714 | 0.127 |

#### <span id="page-76-1"></span>5.2.3 Water Quality Linked Light Attenuation

This method is used for light attenuation for the Full Heat Exchange and Equilibrium Temperature option. In the Equilibrium Temperature heat exchange option, a constant fraction of the solar radiation is always absorbed in the top layer, regardless of how thick it is or what the extinction coefficient is. This is described by the Beer's law with the additional term β :

{77}------------------------------------------------

$$I(z) = (1 - \beta) I_{sw} \exp(-K_e z)$$
 (5.16)

where,

*I*(*z*) is the short wave radiation at depth *z* (*W*/*m* 2 ),

β is the fraction absorbed at the water surface (dimensionless),

*K<sup>e</sup>* is the extinction coefficient (1/*m*), and

*Isw* is the short wave radiation reaching the water surface (*W*/*m* 2 ).

### 5.2.3.1 Light Extinction Factors

The standard [EFDC+](#page-11-0) term by term full heat balance surface heat exchange processes are the same as the full heat balance (legacy) option. The major difference between these two options is that the standard [EFDC+](#page-11-0) full heat balance uses variable light extinction factors. A general formulation of the total light extinction including rooted aquatic plants in the model is given by:

<span id="page-77-0"></span>
$$K_{ess} = K_{e,b} + K_{e,TSS}TSS + K_{e,POC}POC + K_{e,DOC}DOC + K_{e,Chl}\sum Chl + K_{e,MAC}MAC$$
 (5.17)

where,

*Kess* is the total light extinction coefficient (1/*m*),

*Ke*,*T SS* is the light extinction coefficient for [TSS](#page-12-5) (1/*m* per *g*/*m* 3 ),

*Ke*,*<sup>b</sup>* is the background light extinction (1/*m*),

*T SS* is the [TSS](#page-12-5) concentration (*g*/*m* 3 ) provided from the sediment transport module,

*POC* is the total [Particulate Organic Carbon \(POC\)](#page-12-7) concentration (labile and refractory) (*g*/*m* 3 ) provided from the water quality module,

*Ke*,*POC* is the light extinction factor as a function of [POC](#page-12-7) concentrations (1/*m* per *g*/*m* 3 ),

*DOC* is the [Dissolved Organic Carbon \(DOC\)](#page-11-13) concentration (Labile and Refractory) (*g*/*m* 3 ) provided from the water quality module,

*Ke*,*DOC* is the light extinction factor as a function of [DOC](#page-11-13) concentrations (1/*m* per *g*/*m* 3 ),

*Ke*,*Chl* is the light extinction coefficient for floating algae [Chlorophyll](#page-10-5) *a* (chl *a*) (1/*m* per *mg Chl* per *m* 2 ),

*Chl* is the [chl](#page-10-5) *a* concentration of the floating algae group *m*,

*B<sup>m</sup>* is the concentration of algae group *m* (*g C* per *ml*),

*CChl<sup>m</sup>* is the carbon-to-chlorophyll ratio in algal group *m* (*g C* per *mg Chl*),

*Ke*,*MAC* is the light extinction coefficient for fixed biota or rooted plant shoots (1/*m* per *gm C* per *m* 2 ), and

*MAC* is the concentration of fixed biota or plant shoots (*g C* per *m* 2 ). 

{78}------------------------------------------------

If only hydrodynamics and temperature are simulated in the [EFDC+](#page-11-0) model, then the background light extinction coefficient is used. If hydrodynamics, temperature, and [TSS](#page-12-5) are simulated, then the total light extinction coefficient is a function of the background extinction coefficient and light extinction coefficient due to [TSS.](#page-12-5) If a full water quality model is simulated with [TSS](#page-12-5) then the total light extinction coefficient is the function of background extinction, [TSS,](#page-12-5) [POC,](#page-12-7) [DOC](#page-11-13) and [chl](#page-10-5) *a*.

Full heat balance with variable light extinction option is fully coupled with ice sub-model and accounts for the ice melt and ice growth. Finally, the surface heat exchange coefficients for latent and sensible heat exchange can be spatially variable.

#### <span id="page-78-0"></span>5.3. Bed Heat Exchange

Sediment bed and water interface heat exchange is typically small compared to water and air interface heat exchange, therefore it is frequently neglected. However, including sediment bed heat exchange can improve the simulation of temperature in deep lakes and reservoirs. The heat exchange between the sediment bed and the bottom layer of the water column can be described as

$$H_b = -(K_{b,v}U + K_{b,c})(T_w - T_b)$$
(5.18)

$$U = \sqrt{u_1^2 + v_1^2} \tag{5.19}$$

where,

*H<sup>b</sup>* is the sediment bed-water heat exchange (*W*/*m* 2 ),

*Kb*,*<sup>v</sup>* is the convective heat exchange coefficient (*W* −*s*/*m* <sup>3</sup> −◦*C*),

*Kb*,*<sup>c</sup>* is the conductive heat exchange coefficient (*W*/*m* <sup>2</sup> −◦*C*),

*u*<sup>1</sup> is the *u* component water velocity in layer 1 (*m*/*s*),

*v*<sup>1</sup> is the *v* component water velocity in layer 1 (*m*/*s*),

*T<sup>w</sup>* is the water temperature in layer 1 (◦*C*), and

*T<sup>b</sup>* is the sediment bed temperature (◦*C*)

In [EFDC+](#page-11-0) code implementation, both sides are divided by water density and specific heat of water, and therefore the units of *Kb*,*<sup>c</sup>* is in *m*/*s* and *Kb*,*<sup>v</sup>* is dimensionless. Typical applications have used a value of 0.3 *W*/*m* <sup>2</sup>−◦C for *Kb*,*<sup>c</sup>* that is approximately two orders of magnitude smaller than the surface heat exchange coefficient. *Kb*,*<sup>c</sup>* is often not used (i.e. equal to zero) but can be in the range of 0 to 10. Average yearly air temperature is a good initial estimate of *Tb*.

Optionally, the bed temperature (*Tb*) can change with time due to the heat exchange.

$$\frac{\delta\left(D_{b}T_{b}\right)}{\delta t} = -\left(K_{b,v}U + K_{b,c}\right)\left(T_{b} - T_{w}\right) \tag{5.20}$$

where, *D<sup>B</sup>* is the sediment bed-thermal thickness (m). Selection of the thermal thickness is subject to initial approximation and subsequent calibration. The larger the thermal thickness is, the slower the bed temperature will change.

{79}------------------------------------------------

### <span id="page-79-0"></span>5.4. Ice Formation and Melt

The ice module implemented in [EFDC+](#page-11-0) is based on the [W2](#page-12-6) [\(Wells and Cole,](#page-265-7) [2000\)](#page-265-7) ice module. In this module, ice formation and melt is simulated by [EFDC+](#page-11-0) using a coupled heat approach. However, ice dynamics (i.e. movement of ice block/chunks) have not yet been implemented.

### <span id="page-79-1"></span>5.4.1 Heat Balance

The heat balance for the water-to-ice air system is given by:

$$\rho_i L_f \frac{dh}{dt} = h_{ai} (T_i - T_e) - h_{wi} (T_w - T_m)$$
(5.21)

where,

ρ*i* is the density of ice (*kg*/*m* 3 ),

*Lf* is the latent heat of fusion of ice (*J*/*kg*),

*dh*/*dt* is the change in ice thickness (*h*) with time (*t*) (*m*/*s*),

*hai* is the coefficient of ice-to-air heat exchange (*W*/*m* 2/ ◦*C*),

*hwi* is the coefficient of water-to-ice heat exchange through the melt layer (*W*/*m* 2/ ◦*C*),

*Ti* is the ice temperature (◦*C*),

*T<sup>e</sup>* is the equilibrium temperature of ice to air heat exchange (◦*C*),

*T<sup>w</sup>* is the water temperature below ice (◦*C*), and

*T<sup>m</sup>* is the melt temperature (◦*C*).

Formation of ice requires lowering the surface water temperature to the freezing point by normal surface heat exchange processes. With further heat removal, ice begins to form on the water surface. This is indicated by a negative water surface temperature. The negative water surface temperature is then converted to equivalent ice thickness and equivalent heat is added to the heat source and sink term for water. The thickness of ice formation is calculated as

$$\theta_0 = -\frac{T_{wn}\rho_w c_{pw}h}{\rho_i L_f} \tag{5.22}$$

where,

θ<sup>0</sup> is the thickness of initial ice formation during a time step (*m*),

*Twn* is the local temporary negative water temperature (◦*C*),

*h* is the layer thickness (*m*),

ρ*<sup>w</sup>* is the density of water (*kg*/*m* 3 ), *cpw* is the specific heat of water (*J*/*kg*/ ◦*C*),

ρ*i* is the density of ice (*kg*/*m* 3 ), and

*Lf* is the latent heat of fusion (*J*/*kg*).

{80}------------------------------------------------

#### <span id="page-80-0"></span>**5.4.2** Ice Surface Temperature

The ice surface temperature is given by the equations:

$$T_{s}^{n} = \frac{\theta^{n-1}}{K_{i}} \left[ H_{sn}^{n} + H_{an}^{n} - H_{br} \left( T_{s}^{n} \right) - H_{c} \left( T_{s}^{n} \right) \right]$$
 (5.23)

$$H_{sn} + H_{an} - H_{br} - H_e - H_c + q_i = \rho_i L_f \frac{d\theta_{ai}}{dt}$$
, for  $T_s = 0^{\circ} C$  (5.24)

$$q_i = K_i \frac{T_f - T_s(t)}{\theta(t)} \tag{5.25}$$

where,

 $K_i$  is the thermal conductivity of ice  $(W/m/^{\circ}C)$ ,

 $T_f$  is the freezing point temperature (°C),

*n* is the time level,

 $q_i$  is the heat flux through ice  $(W/m^2)$ ,

 $H_n$  is the net rate of heat exchange across the water surface  $(W/m^2)$ ,

 $H_s$  is the incident short wave solar radiation  $(W/m^2)$ ,

 $H_a$  is the incident long wave radiation  $(W/m^2)$ ,

 $H_{sr}$  is the reflected short wave solar radiation  $(W/m^2)$ ,

 $H_{ar}$  is the reflected long wave radiation  $(W/m^2)$ ,

 $H_{br}$  is the back radiation from the water surface  $(W/m^2)$ ,

 $H_e$  is the evaporative heat loss  $(W/m^2)$ , and

 $H_c$  is the heat conduction  $(W/m^2)$ .

## <span id="page-80-1"></span>**5.4.3** Freezing Temperature

The freezing temperature relationship is described as below:

$$T_f = \begin{cases} -0.0545 \, TDS \,, & TDS < 35 \, \text{ppt} \\ -0.3146 - 0.0417 \, TDS - 0.000166 \, TDS^2 \,, & TDS > 35 \, \text{ppt} \end{cases}$$
(5.26)

where,

 $T_f$  is the freezing point temperature (°C), and

TDS is the total dissolved solids (ppt).

{81}------------------------------------------------

#### <span id="page-81-0"></span>5.4.4 Ice Melt at Air/Water Interface

The ice melt at the air/water interface is described by the equation below:

$$\rho_i c_{pi} \frac{T_s(t)}{2} \theta(t) = \rho_i L_f \Delta \theta_{ai}$$
 (5.27)

where,

 $c_{pi}$  is the specific heat of ice  $(J/kg/^{\circ}C)$ , and

 $\theta_{ai}$  is the ice melt at the air-ice interface (1/m).

#### <span id="page-81-1"></span>5.4.5 Ice Growth/Melt at Bottom of Ice

The ice growth/melt at the bottom of the ice is described by the equation below:

$$q_i - q_{iw} = \rho_i L_f \frac{d\theta_{iw}}{dt} \tag{5.28}$$

where,

 $q_i$  is the heat flux through the ice  $(W/m^2)$ ,

 $q_{iw}$  is the heat flux at the ice/water interface  $(W/m^2)$ , and

 $\theta_{iw}$  is the ice growth/melt at the ice-water interface.

$$\Delta \theta_{iw}^{n} = \frac{1}{\rho_{i} L_{f}} \left[ K_{i} \frac{T_{f} - T_{s}^{n}}{\theta^{n-1}} - h_{wi} \left( T_{w}^{n} - T_{f} \right) \right]$$
 (5.29)

#### <span id="page-81-2"></span>5.4.6 Solar Radiation at Bottom of Ice

Solar radiation at the bottom of the ice is given by the equation below:

$$H_{DS} = H_S(1 - \alpha_i)(1 - \beta_i) \exp\left[-\gamma_i \theta(t)\right]$$
(5.30)

where,

 $H_{ps}$  is the solar radiation at the ice-water interface  $(W/m^2)$ ,

 $H_s$  is the incident solar radiation  $(W/m^2)$ ,

 $\alpha_i$  is the ice albedo,

 $\beta_i$  is the fraction of the incoming solar radiation absorbed in the ice surface, and

 $\gamma_i$  is the ice extinction coefficient (1/m).

{82}------------------------------------------------

## <span id="page-82-0"></span>5.5. Water Volume Evaporative Losses

Although the Heat flux due to evaporation is included for the Full Heat and the Equilibrium Temperature [\(W2\)](#page-12-6) option, it does not calculate the volume of water lost from the waterbody due to the evaporation process. User may choose to not calculate evaporative losses or use the input evaporation data to calculate these losses.

User may select other options including [EFDC](#page-11-2) original approach where the latent heat estimated using the full heat balance is used to calculate evaporation and consequently water volume loss due to evaporation. [EFDC+,](#page-11-0) however allows the user to have a different turbulent exchange coefficient for evaporation. The water depth change due to evaporation can be calculated as

$$\Delta z = E\Delta t = \frac{H_E}{\rho L_E} \Delta t \tag{5.31}$$

where,

*H<sup>E</sup>* is the latent heat flux due to evaporation (*W*/*m* 2 ),

ρ is the water density (*kg*/*m*3),

*L<sup>E</sup>* is the latent heat of water (*J*/*kg*),

*E* is the evaporation rate (*m*/*s*),

∆*t* is the time interval (*s*) and

∆*z* is the water depth change over the period ∆*t*

For evaporation, the latent heat flux may also be estimated using the empirical formula proposed by [Edinger](#page-260-10) [et al.](#page-260-10) [\(1974\)](#page-260-10), as

$$H_E = f(W)(e_s - e_a) \tag{5.32}$$

where,

*f*(*W*) is the wind speed function,

*es* is the saturated vapor pressure at water surface temperature (mbar), and

*e<sup>a</sup>* is the actual vapor pressure in the overlying air.

The wind speed function has the general form,

$$f(W) = a + bW + cW^2 (5.33)$$

where,

a, b, c are the wind coefficients (Table [5.2\)](#page-83-0), and

*W* is the windspeed in m/s.

The value of the coefficients is a function of the method selected for evaporative loss (Table [5.2\)](#page-83-0).

{83}------------------------------------------------

Table 5.2. List of Evaporation Calculation Methods

<span id="page-83-0"></span>

| IEAVAP | Evaporation Approach       | General Usage          | a     | b     | c     |
|--------|----------------------------|------------------------|-------|-------|-------|
| 0      | Do Not Include Evaporation |                        |       |       |       |
| 1      | Use Evaporation from ASER  | Measured or Externally |       |       |       |
|        |                            | Estimated              |       |       |       |
| 2      | EFDC Original              |                        |       |       |       |
| 3      | Ward (1980)                | Cooling Lake           | 0.0   | 3.534 | 0.0   |
| 4      | Harbeck Jr (1964)          | Cooling Lake           | 0.0   | 3.818 | 0.0   |
| 5      | Brady et al. (1969)        | Cooling Pond           | 6.442 | 0.0   | 0.322 |
| 6      | Anderson et al. (1954)     | Large Lake             | 0.0   | 2.403 | 0.0   |
| 7      | Webster and Sherman (1995) | Lakes                  | 2.717 | 2.743 | 0.0   |
| 8      | Fulford and Sturm (1984)   | Rivers                 | 8.359 | 2.090 | 0.0   |
| 9      | Gulliver and Stefan (1984) | Streams                | 7.732 | 1.672 | 0.0   |
| 10     | Edinger et al. (1974)      | Lakes/Rivers           | 6.9   | 0.0   | 0.345 |

{84}------------------------------------------------

## <span id="page-84-0"></span>Chapter 6

## SEDIMENT TRANSPORT

#### <span id="page-84-1"></span>6.1. Introduction

[EFDC+](#page-11-0) supports two separate options for sediment transport computation:

- 1. [EFDC](#page-11-2) Sediment Transport module based on Hamrick's work [\(Tetra Tech,](#page-265-10) [2007b\)](#page-265-10).
- 2. [SEDZLJ](#page-12-3) Sediment Transport module that came from [SNL-EFDC](#page-12-2) [\(Jones and Lick,](#page-261-5) [2000;](#page-261-5) [Thanh et al.,](#page-265-0) [2008;](#page-265-0) [Ziegler and Lick,](#page-266-0) [1988,](#page-266-0) [1986\)](#page-266-1).

Both approaches compute the suspended sediment transport in the water column in the same way. Still, they present distinct differences in (1) how they treat cohesive sediment and non-cohesive sediment and (2) how they compute sediment mass exchange between the water column and sediment bed. The [EFDC](#page-11-2) Sediment Transport module applies separate computation processes for cohesive and non-cohesive sediments (see Figure [6.1\)](#page-85-0); this method simulates the erosion process using a user-defined constant erosion rate parameter of each sediment class. The [SEDZLJ](#page-12-3) Sediment Transport module uses a unified treatment for multiple sediment classes regardless of cohesiveness (see Figure [6.2\)](#page-85-1); this approach can apply spatially-varied erosion properties by using site-specific erosion rate data acquired from the SEDFlume apparatus. Both sediment transport modules are dynamically linked to the hydrodynamics module. Therefore, [EFDC+](#page-11-0) can implement direct geomorphic feedback between flow field and sediment bed changes in a simulation. This chapter presents the theoretical basis for the sediment transport computation in [EFDC+.](#page-11-0)

#### <span id="page-84-2"></span>6.2. Suspended Sediment Transport

#### <span id="page-84-3"></span>6.2.1 Governing Equations for Suspended Sediment Transport

The transport equation for the suspended sediments in the water column follows the generic transport equation [\(3.1\)](#page-65-3) for a dissolved or suspended material. For the [EFDC+](#page-11-0) implementation, the physical horizontal diffusion terms in equation [\(3.1\)](#page-65-3) are omitted due to the small inherent numerical diffusion encountered. This yields the following form of the suspended sediment transport equation:

{85}------------------------------------------------

<span id="page-85-0"></span>Fig. 6.1. Structure of the [EFDC](#page-11-2) Sediment Transport Model.

<span id="page-85-1"></span>Fig. 6.2. Structure of the SEDZLJ Sediment Transport Model.

{86}------------------------------------------------

<span id="page-86-1"></span>
$$\frac{\partial}{\partial t} (m_x m_y H C_j) + \frac{\partial}{\partial x} (m_y H u C_j) + \frac{\partial}{\partial y} (m_x H v C_j) + \frac{\partial}{\partial z} (m_x m_y w C_j) - \frac{\partial}{\partial z} (m_x m_y w_{s,j} C_j)$$

$$= \frac{\partial}{\partial z} \left( \frac{m_x m_y}{H} A_b \frac{\partial}{\partial z} C_j \right) + S_{s,j}^E + S_{s,j}^I \quad (6.1)$$

where

*x*, *y* are the orthogonal curvilinear coordinates in the horizontal direction (m),

*z* is the sigma coordinate (dimensionless),

*t* is time (s),

*mx*, *m<sup>y</sup>* are the square roots of the diagonal components of the metric tensor (dimensionless),

*Cj* is the concentration of sediment class *j* in the water column (g/m<sup>3</sup> ),

*H* is the total water column depth (m),

*u*, *v* are the horizontal velocity components in the curvilinear coordinates (m/s),

*w* is the vertical velocity component (m/s),

*ws*, *<sup>j</sup>* is a settling velocity of suspended sediment class *j* (m/s),

*A<sup>b</sup>* is the vertical turbulent eddy diffusivity (m<sup>2</sup> /s),

*S E s*, *j* is the external source-sink term of sediment class *j* (g/m<sup>2</sup> /s), and

*S I s*, *j* is the internal source-sink term of sediment class *j* (g/m<sup>2</sup> /s).

The source-sink term has been split into two terms: the external term would include point and non-point source loads, and the internal term could include reactive decay of organic sediments or mass exchange between sediment classes if floc formation and destruction are simulated.

The boundary conditions in the vertical direction for equation [\(6.1\)](#page-86-1) are:

<span id="page-86-2"></span>
$$-\frac{A_b}{H}\frac{\partial}{\partial z}C_j - w_{s,j}C_j = J_{o,j} \quad \text{at} \quad z = 0$$
(6.2)

$$-\frac{A_b}{H}\frac{\partial}{\partial z}C_j - w_{s,j}C_j = 0 \quad \text{at} \quad z = 1$$
(6.3)

where *Jo*, *<sup>j</sup>* is the net exchange flux of sediment class *j* (g/m<sup>2</sup> /s) between the water column-sediment bed, defined as positive into the water column.

## <span id="page-86-0"></span>6.2.2 Numerical Solution

The general procedure follows that for the salinity transport equation, which uses a high order upwind difference discretization scheme for the advective terms, described in [Hamrick](#page-261-3) [\(1992\)](#page-261-3). The numerical solution of equation [\(6.1\)](#page-86-1) utilizes a fractional step procedure.

{87}------------------------------------------------

The first step advances the concentration due to advection and external sources and sinks having corresponding volume fluxes by:

$$H^{n+1}C^* = H^nC^n + \frac{\Delta t}{m_x m_y} \left(S_s^E\right)^{n+\frac{1}{2}} - \frac{\Delta t}{m_x m_y} \left[\frac{\partial}{\partial x} \left(m_y (Hu)^{n+\frac{1}{2}} C^n\right) + \frac{\partial}{\partial y} \left(m_x (Hv)^{n+\frac{1}{2}} C^n\right) + \frac{\partial}{\partial z} \left(m_x m_y w^{n+\frac{1}{2}} C^n\right)\right]$$
(6.4)

where the superscripts n and n+1 denote the old and new time levels, and the superscript \* denotes the intermediate fractional step results. Note that the sediment class subscript j has been dropped to simplify the equation. The source and sink term portion, associated with volumetric sources and sinks, is included in the advective step for consistency with the continuity constraint. This source-sink term, as well as the advective field  $(u, v, w_i)$ , is defined as an intermediate in time between the old and new time levels consistent with the temporal discretization of the continuity equation. The advection step uses the anti-diffusive Multidimensional Positive Definite Advection Transport Algorithm (MPDATA) scheme (Smolarkiewicz and Clark, 1986) with optional flux corrected transport (Smolarkiewicz and Grabowski, 1990).

The second fractional step, or settling step, is given by:

$$C^{**} = C^* + \frac{\Delta t}{H^{n+1}} \frac{\partial}{\partial z} (w_s C^{**})$$
(6.5)

, which is solved by a fully implicit upwind difference scheme as below:

$$C_{KC}^{**} = C_{KC}^{*} + \frac{\Delta t}{\Delta_z H^{n+1}} (w_s C^{**})_{KC}$$
(6.6)

$$C_k^{**} = C_k^* + \frac{\Delta t}{\Delta_1 H^{n+1}} (w_s C^{**})_{k+1} - \frac{\Delta t}{\Delta_k H^{n+1}} (w_s C^{**})_k \text{ for } 2 \le k \le KC - 1$$
 (6.7)

$$C_1^{**} = C_1^* + \frac{\Delta t}{\Delta H^{n+1}} (w_s C^{**})_2$$
(6.8)

where

k is the water column layer index,

KC is the maximum number of water column layers,

 $C_{KC}$  is the top layer concentration (g/m<sup>3</sup>),

 $C_k$  is the concentration in each layer k (g/m<sup>3</sup>), and

 $C_1$  is the bottom layer concentration (g/m<sup>3</sup>).

For the second fractional step, the solution starts at the top layer (k = KC) and marches down to the bottom layer (k = 1). The implicit solution includes an optional anti-diffusion correction across internal water column layer interfaces.

{88}------------------------------------------------

The third fractional step accounts for water column-sediment bed exchange by resuspension and deposition as follows:

<span id="page-88-0"></span>
$$C_1^{***} = C_1^{**} + \frac{\Delta t}{\Delta_z H^{n+1}} L_o J_o^{***}$$
(6.9)

where  $L_o$  is a flux limiter (dimensionless) such that only the current top layer of the sediment bed can be completely resuspended in a single time step.

For resuspension and deposition of suspended non-cohesive sediment, the bed flux is given by:

$$J_0^{***} = w_s (C_{eq} - C_1^{***}) (6.10)$$

where  $C_{eq}$  is the equilibrium concentration (g/m<sup>3</sup>) with respect to hydrodynamic and sediment physical parameters.

For cohesive sediment resuspension, the bed flux is specified as a function of the bed shear stress and bed geomechanical properties. For cohesive sediment deposition, the bed flux is typically given by:

$$J_0^{***} = -P_d w_s C_1^{***} (6.11)$$

where  $P_d$  is a probability of deposition. The representation of the water column-sediment bed exchange by a distinct fractional step is equivalent to a splitting of the bottom boundary condition equation (6.2) such that the bed flux is imposed at the intermediate step between settling and vertical diffusion.

The remaining step is an implicit vertical turbulent diffusion step corresponding to:

$$C^{n+1} = C^{***} + \Delta t \frac{\partial}{\partial z} \left[ \left( \frac{A_b}{H^2} \right)^{n+1} \frac{\partial}{\partial z} C^{n+1} \right]$$
 (6.12)

with zero diffusive fluxes at the bed and water surface.

{89}------------------------------------------------

#### <span id="page-89-0"></span>6.3. EFDC Sediment Transport Module

The implementation of [EFDC](#page-11-2) Sediment Transport module applies separate computation processes for noncohesive and cohesive sediments. The conceptual framework of the sediment transport processes is illustrated in Figure [6.3.](#page-89-2)

<span id="page-89-2"></span>Fig. 6.3. Conceptual Framework for [EFDC](#page-11-2) Sediment Transport Module.

## <span id="page-89-1"></span>6.3.1 Non-Cohesive Sediment

#### 6.3.1.1 Settling Velocity

Non-cohesive inorganic sediments settle as discrete particles under low sediment concentration conditions, with hindered settling and multi-phase interactions becoming important in regions of high sediment concentrations near the bed. At low sediment concentrations, the settling velocity for the non-cohesive sediment class *j* corresponds to the settling velocity of a discrete particle as:

$$w_{sj} = w_{soj} \tag{6.13}$$

{90}------------------------------------------------

where, *wso j* is the discrete particle settling velocity (m/s) that depends on the sediment particle density ρ*<sup>s</sup>* , effective grain diameter, and fluid kinematic viscosity ν. A piece-wise relation for *wso j* by [van Rijn](#page-265-11) [\(1984\)](#page-265-11) is as follows:

<span id="page-90-0"></span>
$$w_{soj} = \sqrt{g'd_j} \begin{cases} \frac{R_{dj}}{18}, & d \le 100 \,\mu\text{m} \\ \frac{10}{R_{dj}} \left( \sqrt{1 + 0.01R_{dj}^2} - 1 \right), & 100\mu m < d_j \le 1000 \,\mu\text{m} \\ 1.1, & d_j > 1000\mu\text{m} \end{cases}$$
(6.14)

where *g* ′ is the reduced gravitational acceleration presented as:

$$g' = g\left(\frac{\rho_{sj}}{\rho_w} - 1\right) \tag{6.15}$$

and *Rd j* is the sediment grain densimetric Reynolds number calculated as:

$$R_{dj} = \frac{d_j \sqrt{g'd_j}}{V} \tag{6.16}$$

At higher concentrations and hindering settling conditions, the settling velocity is less than the discrete velocity and can be expressed in the form:

$$w_{sj} = \left(1 - \sum_{i}^{I} \frac{C_i}{\rho_{si}}\right)^n w_{soj} \tag{6.17}$$

where ρ*<sup>s</sup>* is the sediment particle density with values of *n* ranging from 2 to 4 [\(van Rijn,](#page-265-11) [1984\)](#page-265-11). The expression [\(6.14\)](#page-90-0) is approximated to within 5 percent by:

$$w_{sj} = \left(1 - n\sum_{i}^{I} \frac{C_i}{\rho_{si}}\right) w_{soj} \tag{6.18}$$

for total sediment concentrations up to 200,000 mg/l. For total sediment concentrations less than 25,000 mg/l, neglecting the hindered settling correction results in less than a 5% error in the settling velocity, which is well within the range of uncertainty in parameters used to estimate the discrete particle settling velocity.

### 6.3.1.2 Critical Thresholds of Transport and Erosion

In the [EFDC](#page-11-2) Sediment Transport module, the preceding set of rules is used to determine the mode of transport of multiple-size classes of non-cohesive sediment. Non-cohesive sediment is transported as bedload and suspended load. The initiation of both transport modes begins with erosion or resuspension of sediments from the bed when the bed stress τ*<sup>b</sup>* exceeds a critical stress referred to as the Shield's stress τ*cs*. The Shield's stress τ*cs* depends upon the density and diameter of the sediment particles and the kinematic viscosity of the fluid and can be expressed in empirical dimensionless relationships of the form:

<span id="page-90-1"></span>
$$\theta_{csj} = \frac{\tau_{csj}}{g'd_j} = \frac{u_{*csj}^2}{g'd_j} = f(R_{dj})$$
(6.19)

{91}------------------------------------------------

Useful numerical expressions of the relationship of equation [\(6.19\)](#page-90-1), provided by [van Rijn](#page-265-11) [\(1984\)](#page-265-11) are:

<span id="page-91-1"></span>
$$\theta_{csj} = \begin{cases} 0.24 \left( R_{dj}^{2/3} \right)^{-1} & \text{for } R_{dj}^{2/3} < 4 \\ 0.14 \left( R_{dj}^{2/3} \right)^{-0.64} & \text{for } 4 \le R_{dj}^{2/3} < 10 \end{cases}$$

$$\theta_{csj} = \begin{cases} 0.04 \left( R_{dj}^{2/3} \right)^{-0.1} & \text{for } 10 \le R_{dj}^{2/3} < 20 \\ 0.013 \left( R_{dj}^{2/3} \right)^{0.29} & \text{for } 20 \le R_{dj}^{2/3} < 150 \\ 0.055 & \text{for } 150 \le R_{dj}^{2/3} \end{cases}$$

$$(6.20)$$

Several approaches have been used to distinguish whether a particular sediment size class is transported as bedload or suspended load under specific local flow conditions characterized by bed shear velocity *u*∗:

$$u_* = \sqrt{\tau_b} \tag{6.21}$$

The approach proposed by [van Rijn](#page-265-11) [\(1984\)](#page-265-11) is used in the [EFDC](#page-11-2) Sediment Transport module and is as follows. When the bed shear velocity is less than the critical shear velocity *u*∗*cs j* for sediment class *j*:

<span id="page-91-0"></span>
$$u_{*csj} = \sqrt{\tau_{csj}} = \sqrt{g'd_j\theta_{csj}}$$
 (6.22)

no erosion or resuspension takes place, and there is no bedload transport. Sediment in suspension in the water column under this condition will deposit to the sediment bed.

When the bed shear velocity exceeds the critical shear velocity but remains less than the settling velocity:

<span id="page-91-2"></span>
$$u_{*csj} < u_* < w_{soj} \tag{6.23}$$

sediment will be eroded from the bed and transported as bedload. Sediment in suspension in the water column under this condition will deposit to the bed. When the bed shear velocity exceeds both the critical shear velocity and the settling velocity, bedload transport ceases, and the eroded or resuspended sediments will be transported as a suspended load. These various transport modes are further illustrated by reference to Figure [6.4,](#page-92-0) which shows dimensional forms of the settling velocity relationship equation [\(6.14\)](#page-90-0), and the critical Shield's shear velocity equation [\(6.22\)](#page-91-0) determined using equation [\(6.20\)](#page-91-1) for sediment with a specific gravity of 2.65.

For grain diameters less than 1.3×10−<sup>4</sup> m (130 µm), the settling velocity is less than the critical shear velocity. So, when the bed shear velocity exceeds the critical shear velocity, the sediments will be resuspended from the bed and transported entirely as a suspended load. For grain diameters greater than 1.3×10−<sup>4</sup> m, eroded sediment can be transported by bedload in the region corresponding to equation [\(6.23\)](#page-91-2) and then as a suspended load when the bed shear velocity exceeds the settling velocity.

{92}------------------------------------------------

<span id="page-92-0"></span>Fig. 6.4. Critical Shield's shear velocity and settling velocity as a function of sediment grain size.

#### 6.3.1.3 Bedload

Bedload transport is determined using a general bedload transport rate formula:

$$\frac{q_B}{\rho_s d\sqrt{g'd}} = \Phi(\theta, \theta_{cs}) \tag{6.24}$$

where *q<sup>B</sup>* is the bedload transport rate (mass per unit time per unit width) in the direction of the near bottom horizontal flow velocity vector. The function Φ depends on the Shield's parameter θ:

<span id="page-92-1"></span>
$$\theta = \frac{\tau_b}{g'd_j} = \frac{u_*^2}{g'd_j} \tag{6.25}$$

and the critical Shield's parameter θ*cs* defined by the equations [\(6.19\)](#page-90-1) and [\(6.20\)](#page-91-1).

{93}------------------------------------------------

In [EFDC+,](#page-11-0) bedload transport formulations have the general form, which conforms to equation [\(6.25\)](#page-92-1):

$$\Phi(\theta, \theta_{cs}) = \phi \left(\theta - \theta_{cs}\right)^{\alpha} \left(\sqrt{\theta} - \gamma \sqrt{\theta_{cs}}\right)^{\beta}$$
(6.26)

The bedload transport parameter φ is specified as a function of the critical Shield's parameter θ*cs* and/or grain densimetric Reynolds number *R<sup>d</sup>* following [van Rijn](#page-265-11) [\(1984\)](#page-265-11) formulation:

$$\phi = \frac{0.053}{R_d^{1/5} \theta_{cs}^{2.1}} \tag{6.27}$$

The bedload constants α, β, and γ are treated as user-defined parameters, which can be specified following the literature listed below.

[van Rijn](#page-265-11) [\(1984\)](#page-265-11) formulation:

$$\Phi = \phi \left(\theta - \theta_{cs}\right)^{2.1} \tag{6.28}$$

[Engelund and Hansen](#page-260-12) [\(1967\)](#page-260-12) formulation:

$$\Phi = \phi \left(\theta\right)^{2.1} \left(\sqrt{\theta}\right)^{\beta} \tag{6.29}$$

[Meyer-Peter and Muller](#page-263-12) ¨ [\(1948\)](#page-263-12) formulation:

$$\Phi = \phi \left(\theta - \theta_{cs}\right)^{1.5} \tag{6.30}$$

[Bagnold](#page-258-7) [\(1956\)](#page-258-7) formulation:

$$\Phi = \phi \left(\theta - \theta_{cs}\right) \left(\sqrt{\theta}\right) \tag{6.31}$$

[Wu et al.](#page-266-5) [\(2000\)](#page-266-5) formulation:

$$\Phi = \phi \left(\theta - \theta_{cs}\right)^{2.2} \tag{6.32}$$

Additionally, there are also other bedload formulations that were developed for riverine prediction [\(Ack](#page-258-8)[ers and White,](#page-258-8) [1973;](#page-258-8) [Laursen,](#page-262-6) [1958;](#page-262-6) [Yang,](#page-266-6) [1973;](#page-266-6) [Yang and Molinas,](#page-266-7) [1982\)](#page-266-7); however, they do not readily conform to equation [\(6.25\)](#page-92-1) so those approaches are not incorporated in the [EFDC+](#page-11-0) model.

The procedure for coupling bedload transport with the sediment bed in the [EFDC+](#page-11-0) model is as follows. First, the magnitude of the bedload mass flux per unit width is calculated according to equation [\(6.25\)](#page-92-1) at horizontal model cell centers, denoted by the subscript *C*. The cell center flux is then transformed into cell center vector components using:

<span id="page-93-0"></span>
$$q_{bcx} = \frac{u}{\sqrt{u^2 + v^2}} q_{bc}$$

$$q_{bcy} = \frac{v}{\sqrt{u^2 + v^2}} q_{bc}$$
(6.33)

{94}------------------------------------------------

where *u* and *v* are the cell center horizontal velocities near the bed. Cell face mass fluxes are determined by downwind projection of the cell center fluxes

$$q_{bfx} = (q_{bcx})_{upwind}$$

$$q_{bfy} = (q_{bcy})_{upwind}$$
(6.34)

<span id="page-94-1"></span>where the subscript *upwind* denotes the cell center upwind of the *x* normal and *y* normal cell faces. The net removal or accumulation rate of sediment material from the deposited bed underlying a water cell is then given by:

<span id="page-94-0"></span>
$$m_x m_y J_b = (m_y q_{bfx})_e - (m_y q_{bfx})_w + (m_x q_{bfy})_n - (m_x q_{bfy})_s$$
 (6.35)

where,

*J<sup>b</sup>* is the net removal rate (*gm*/*m* <sup>2</sup> −*sec*) from the bed,

*m<sup>x</sup>* and *m<sup>y</sup>* are *x* and *y* dimensions of the cell, and

*e*,*w*,*n*,*s* represent the compass direction subscripts, which define the four cell faces.

The implementation of equations [\(6.33\)](#page-93-0) through [\(6.35\)](#page-94-0) in the [EFDC+](#page-11-0) includes logic to limit the out fluxes equation [\(6.34\)](#page-94-1) over a time step, such that the time-integrated mass flux from the bed does not exceed bed sediment available for erosion or resuspension.

#### 6.3.1.4 Suspended Load

Under conditions when the bed shear velocity exceeds the settling velocity and critical Shield's shear velocity, non-cohesive sediment will be resuspended and transported as a suspended load in the water column. When the bed shear velocity falls below both the settling velocity and the critical Shield's shear velocity, suspended sediments in the water column will deposit into the bed.

A consistent formulation of these processes is developed using the concept of a near-bed equilibrium sediment concentration. Under steady, uniform flow and sediment loading conditions, an equilibrium distribution of sediment in the water column tends to be established, with the resuspension and deposition fluxes canceling each other. Using a number of simplifying assumptions, the equilibrium sediment concentration distribution in the water column can be expressed analytically in terms of the near bed reference or equilibrium concentration, the settling velocity, and the vertical turbulent diffusivity. For unsteady or spatially varying flow conditions, the water column sediment concentration distribution varies in space and time in response to sediment load variations, changes in hydrodynamic transport, and associated nonzero fluxes across the water column-sediment bed interface. An increase or decrease in the bed stress and the intensity of vertical turbulent mixing will result in net erosion or deposition, respectively, at a particular location or time.

To illustrate how an appropriate suspended non-cohesive sediment bed flux boundary condition can be established, consider the approximation to the sediment transport equation [\(6.1\)](#page-86-1) for nearly uniform horizontal conditions:

<span id="page-94-2"></span>
$$\frac{\partial}{\partial t}(HC) = \frac{\partial}{\partial z} \left( \frac{A_b}{H} \frac{\partial C}{\partial z} + w_z C \right) \tag{6.36}$$

{95}------------------------------------------------

Integrating equation [\(6.36\)](#page-94-2) over the depth of the bottom hydrodynamic model layer gives:

<span id="page-95-0"></span>
$$\frac{\partial}{\partial t} \left( \Delta H \bar{C} \right) = J_0 - J_\Delta \tag{6.37}$$

where the overbar denotes the mean over the dimensionless layer thickness ∆. Subtracting equation [\(6.37\)](#page-95-0) from equation [\(6.36\)](#page-94-2) gives:

<span id="page-95-1"></span>
$$\frac{\partial}{\partial t} (HC') = \frac{\partial}{\partial z} \left( \frac{A_b}{H} \frac{\partial C}{\partial z} + w_z C \right) - \left( \frac{J_0 - J_\Delta}{\Delta} \right)$$
 (6.38)

By assuming that the rate of change of the deviation of the sediment concentration from the mean is small,

$$\frac{\partial}{\partial t} \left( HC' \right) << \frac{\partial}{\partial t} \left( H\bar{C} \right) \tag{6.39}$$

equation [\(6.38\)](#page-95-1) can be approximated by:

<span id="page-95-2"></span>
$$\frac{\partial}{\partial z} \left( \frac{A_b}{H} \frac{\partial C}{\partial z} + w_z C \right) = \left( \frac{J_0 - J_\Delta}{\Delta} \right) \tag{6.40}$$

Integrating equation [\(6.40\)](#page-95-2) once gives:

<span id="page-95-3"></span>
$$\frac{A_b}{H} \frac{\partial C}{\partial z} + w_z C = (J_0 - J_\Delta) \frac{z}{\Delta} - J_0 \tag{6.41}$$

Very near the bed, equation [\(6.41\)](#page-95-3) can be approximated by:

<span id="page-95-5"></span>
$$\frac{A_b}{H}\frac{\partial C}{\partial z} + w_z C = -J_0 \tag{6.42}$$

Neglecting stratification effects and using the results of Section [5.1.1,](#page-72-1) the near-bed diffusivity is approximately:

<span id="page-95-4"></span>
$$\frac{A_b}{H} = K_o q \frac{l}{H} \cong u_* \kappa z \tag{6.43}$$

Integrating equation [\(6.43\)](#page-95-4) into [\(6.42\)](#page-95-5) gives:

<span id="page-95-6"></span>
$$\frac{\partial C}{\partial z} + \frac{R}{z}C = -\frac{R}{z}\frac{J_o}{w_s} \tag{6.44}$$

where *R* is the Rouse parameter calculated as:

$$R = \frac{w_s}{u_* \kappa} \tag{6.45}$$

The solution of equation [\(6.44\)](#page-95-6) is:

{96}------------------------------------------------

<span id="page-96-1"></span>
$$C = -\frac{J_o}{w_s} + \frac{C_0}{z^R} \tag{6.46}$$

The constant of integration is evaluated by setting the near-bed sediment concentration to an equilibrium value, defined just above the bed under no net flux condition as:

<span id="page-96-0"></span>
$$C = C_{eq}$$
 at  $z = z_{eq}$  and  $J_o = 0$  (6.47)

Using equation (6.47), equation (6.46) becomes

<span id="page-96-2"></span>
$$C = \left(\frac{z_{eq}}{z}\right)^R C_{eq} - \frac{J_o}{w_s} \tag{6.48}$$

For non-equilibrium conditions, the net flux is given by evaluating equation (6.48) at the equilibrium level

<span id="page-96-3"></span>
$$J_o = w_s (C_{eq} - C_{ne}) (6.49)$$

where  $C_{ne}$  is the actual concentration at the reference equilibrium level. Equation (6.49) clearly indicates that when the near bed sediment concentration is less than the equilibrium value, a net flux from the bed into the water column occurs. Likewise, when the concentration exceeds equilibrium, a net flux to the bed occurs. When  $C_{ne}$  is greater than  $C_e$ , equation (6.49) can be rewritten as:

<span id="page-96-4"></span>
$$J_o = -w_s C_{ne} \left( 1 - \frac{C_{eq}}{C_{ne}} \right) \tag{6.50}$$

and the term inside the parenthesis in the equation (6.50) can be considered as the deposition factor, which does not exceed unity.

For the relationship equation (6.49) to be useful in a three-dimensional numerical model, the bed flux must be expressed in terms of the model layer mean concentration as:

<span id="page-96-6"></span><span id="page-96-5"></span>
$$J_o = w_s \left( \bar{C}_{eq} - \bar{C} \right) \tag{6.51}$$

where

$$\bar{C}_{eq} = \frac{\ln\left(\Delta z_{eq}^{-1}\right)}{\left(\Delta z_{eq}^{-1} - 1\right)} C_{eq} , \quad R = 1$$

$$\bar{C}_{eq} = \frac{\left(\Delta z_{eq}^{-1}\right)^{1-R} - 1}{\left(1 - R\right)\left(\Delta z_{eq}^{-1} - 1\right)} C_{eq} , \quad R \neq 1$$
(6.52)

, which defines an equivalent layer's mean equilibrium concentration in terms of the near-bed equilibrium concentration. The corresponding quantities in the numerical solution for bottom boundary condition equation (6.9) are:

{97}------------------------------------------------

<span id="page-97-5"></span><span id="page-97-0"></span>
$$w_r C_r = w_s \bar{C}_{eq}$$

$$P_d w_s = w_s$$
(6.53)

If the dimensionless equilibrium elevation,  $z_{eq}$  exceeds the dimensionless layer thickness, equation (6.33) can be modified to:

$$\bar{C}_{eq} = \frac{\ln\left(M\Delta z_{eq}^{-1}\right)}{\left(M\Delta z_{eq}^{-1} - 1\right)} C_{eq} , \quad R = 1$$

$$\bar{C}_{eq} = \frac{\left(M\Delta z_{eq}^{-1}\right)^{1-R} - 1}{\left(1 - R\right)\left(M\Delta z_{eq}^{-1} - 1\right)} C_{eq} , \quad R \neq 1$$
(6.54)

where the over bars in equations (6.51) and (6.53) implying a concentration average of the first M layers above the bed.

For two-dimensional depth-averaged model application, a number of additional considerations are necessary. For depth average modeling, the equivalent of equation (6.41) is:

<span id="page-97-2"></span>
$$\frac{A_b}{H}\frac{\partial C}{\partial z} + w_s C = -J_o(1-z) \tag{6.55}$$

Neglecting stratification effects and using the results of the sediment boundary layers, the diffusivity is:

<span id="page-97-1"></span>
$$\frac{A_b}{H} = K_o q \frac{1}{H} \cong u_* \kappa z (1 - z)^{\lambda} \tag{6.56}$$

Integrating equation (6.56) into equation (6.55) gives:

<span id="page-97-3"></span>
$$\frac{\partial C}{\partial z} + \frac{R}{z(1-z)^{\lambda}}C = -\frac{R(1-z)^{1-\lambda}}{z}\frac{J_o}{w_s}$$
(6.57)

A closed form solution of equation (6.57) is possible for  $\lambda$  equal to zero. Although the resulting diffusivity is not as reasonable as the choice of  $\lambda$  equal to one, the resulting vertical distribution of sediment is much more sensitive to the near-bed diffusivity distribution than the distribution in the upper portions of the water column. For  $\lambda$  equal to zero, the solution of equation (6.57) is:

$$C = -\left(1 - \frac{Rz}{(1+R)}\right) \frac{J_o}{w_s} + \frac{C_0}{z^R}$$
 (6.58)

Evaluating the constant of integration using equation (6.56) gives:

<span id="page-97-4"></span>
$$C = \left(\frac{z_{eq}}{z}\right)^{R} C_{eq} - \left(1 - \frac{Rz}{(1+R)}\right) \frac{J_{o}}{w_{s}}$$

$$(6.59)$$

For non-equilibrium conditions, the net flux is given by evaluating equation (6.59) at the equilibrium level:

{98}------------------------------------------------

<span id="page-98-0"></span>
$$J_o = w_s \left(\frac{1+R}{1+R(1-z_{eq})}\right) (C_{eq} - C_{ne})$$
(6.60)

where  $C_{ne}$  is the actual concentration at the reference equilibrium level. Since  $z_{eq}$  is on the order of the sediment grain diameter divided by the depth of the water column, equation (6.60) is essentially equivalent to equation (6.49). To obtain an expression for the bed flux in terms of the depth average sediment concentration, equation (6.59) is integrated over the depth to give

$$J_o = w_s \left( \frac{2(1+R)}{2+R(1-z_{eq})} \right) \left( \bar{C}_{eq} - \bar{C} \right)$$
 (6.61)

where

<span id="page-98-1"></span>
$$\bar{C}_{eq} = \frac{\ln(z_{eq}^{-1})}{(z_{eq}^{-1} - 1)} C_{eq}, \quad R = 1$$

$$\bar{C}_{eq} = \frac{(z_{eq}^{R-1} - 1)}{(1 - R)(z_{eq}^{-1} - 1)} C_{eq}, \quad R \neq 1$$
(6.62)

The corresponding quantities in the numerical solution bottom boundary condition equation (6.9) are

$$w_{r}s_{r} = w_{s} \left(\frac{2(1+R)}{2+R(1-z_{eq})}\right) \bar{C}_{eq}$$

$$P_{d}w_{s} = \left(\frac{2(1+R)}{2+R(1-z_{eq})}\right) w_{s}$$
(6.63)

When multiple sediment size classes are simulated, the equilibrium concentrations given by equations (6.52), (6.54), and (6.62) are adjusted by multiplying by their respective sediment volume fractions in the surface layer of the bed.

The specification of the water column-bed flux of non-cohesive sediment has been reduced to the specification of the near-bed equilibrium concentration and its corresponding reference distance above the bed. Garcia and Parker (1991) evaluated seven relationships, derived by combinations of analysis and experiment correlation, for determining the near bed equilibrium concentration as well as proposing a new relationship. All of the relationships essentially specify the equilibrium concentration in terms of hydrodynamic and sediment physical parameters

$$C_{eq} = C_{eq}(d, \rho_s, \rho_w, w_s, u_*, v)$$
 (6.64)

including the sediment particle diameter, the sediment and water densities, the sediment settling velocity, the bed shear velocity, and the kinematic molecular viscosity of water. Garcia and Parker concluded that the representations of Smith and McLean (1977) and van Rijn (1984), as well as their own proposed representation, perform acceptably when tested against experimental and field observations.

Smith and McLean (1977) formula for the equilibrium concentration, which requires the critical Shields stress to be specified for each sediment size class, as:

{99}------------------------------------------------

$$C_{eq} = \rho_s \frac{0.65 \gamma_o T}{1 + \gamma_o T} \tag{6.65}$$

where γ*<sup>o</sup>* is a constant equal to 2.4×10−<sup>3</sup> and *T* is given by

$$T = \frac{\tau_b - \tau_{cs}}{\tau_{cs}} = \frac{u_*^2 - u_{*cs}^2}{u_{*cs}^2}$$
 (6.66)

where

τ*<sup>b</sup>* is the bed stress, and

τ*cs* is the critical Shields stress.

[van Rijn](#page-265-11) [\(1984\)](#page-265-11) formula is

$$C_{eq} = 0.015 \rho_s \frac{d}{z_{eq}^*} T^{3/2} R_d^{-1/5}$$
(6.67)

where

*z* ∗ *eq* = *Hzeq* is the dimensional reference height, and

*R<sup>d</sup>* is a sediment grain Reynolds number.

When van Rijn's formula is selected for use in [EFDC+,](#page-11-0) the critical Shields stress is internally calculated using relationships from [van Rijn](#page-265-11) [\(1984\)](#page-265-11), which suggests setting the dimensional reference height to threegrain diameters. In the [EFDC+](#page-11-0) model, the user specifies the reference height as a multiple of the largest non-cohesive sediment size class diameter.

[Garcia and Parker](#page-260-13) [\(1991\)](#page-260-13) general formula for multiple sediment size classes is

$$C_{jeq} = \rho_s \frac{A \left(\lambda Z_j\right)^5}{\left(1 + 3.33A \left(\lambda Z\right)^5\right)}$$
(6.68)

$$Z_j = \frac{u_*}{w_{sj}} R_{dj}^{3/5} F_H \tag{6.69}$$

$$F_H = \left(\frac{d_j}{d_{50}}\right)^{1/5} \tag{6.70}$$

$$\lambda = 1 + \frac{\sigma_{\phi}}{\sigma_{\phi o}} \left( \lambda_o - 1 \right) \tag{6.71}$$

where

*A* is a constant equal to 1.3×10−<sup>7</sup> ,

*d*<sup>50</sup> is the median grain diameter based on all sediment classes,

{100}------------------------------------------------

λ is a straining factor,

*F<sup>H</sup>* is a hiding factor, and

σ<sup>ø</sup> is the standard deviation of the sedimentological phi scale of sediment size distribution.

[Garcia and Parker](#page-260-13) [\(1991\)](#page-260-13) formulation is unique in that it can account for armoring effects when multiple sediment classes are simulated. For the simulation of a single non-cohesive size class, the straining factor and the hiding factor are set to one. [EFDC+](#page-11-0) has the option to simulate armoring with Garcia and Parker's formulation. For armoring simulation, the current surface layer of the sediment bed is restricted to a thickness equal to the dimensional reference height.

#### <span id="page-100-0"></span>6.3.2 Cohesive Sediments

### 6.3.2.1 Settling Velocity

The settling of cohesive inorganic sediments and organic particulate materials is an extremely complex process. Inherent in the process of gravitational settling is the process of flocculation, where individual cohesive sediment particles and particulate organic particles aggregate to form larger groupings (or flocs) having settling characteristics significantly different from those of the component particles [\(Burban et al.,](#page-258-9) [1989,](#page-258-9) [1990;](#page-258-10) [Gibbs,](#page-261-21) [1985;](#page-261-21) [Mehta et al.,](#page-263-13) [1989\)](#page-263-13). Floc formation is dependent upon the type and concentration of the suspended materials, the ionic characteristics of the environment, and the fluid shear and turbulence intensity of the flow environment. Progress has been made in first principles mathematical modeling of floc formation or aggregation and disaggregation by intense flow shear [\(Lick and Lick,](#page-262-7) [1988;](#page-262-7) [Tsai et al.,](#page-265-12) [1987\)](#page-265-12). However, the computational cost of such approaches precludes direct simulation of flocculation in operational cohesive sediment transport models.

An alternative approach, which has been applied with reasonable success, is the parameterization of the settling velocity of flocs in terms of cohesive and organic material fundamental particle size *d*, concentration *C*, and flow characteristics such as vertical shear of the horizontal velocity *du*/*dz*, shear stress *Avdu*/*sz*, or turbulence intensity in the water column or near the sediment bed *q*. This implementation has allowed semi-empirical expressions with the functional form:

$$w_{se} = w_{se} \left( d, C, \frac{du}{dz}, q \right) \tag{6.72}$$

to be developed to represent the effective settling velocity. In [EFDC+,](#page-11-0) the settling velocity of each cohesive sediment class is determined by either a user-defined constant or one of the approaches described below.

#### 6.3.2.1.1 Option 1

[Hwang and Mehta](#page-261-22) [\(1989\)](#page-261-22) proposed the following:

<span id="page-100-1"></span>
$$w_s = \frac{aC''}{(C^2 + b^2)^m} \tag{6.73}$$

based on observations of settling at six sites in Lake Okeechobee. This equation has a general parabolic shape with the settling velocity decreasing with decreasing concentration at low concentrations and decreasing with increasing concentration at high concentrations. Least squares analysis for the parameters *a*, *m*, *n*,

{101}------------------------------------------------

in equation [\(6.73\)](#page-100-1) was shown to agree well with observational data. Equation [\(6.73\)](#page-100-1) does not have a dependence on flow characteristics but is based on data from an energetic field condition having both currents and high-frequency surface waves.

#### 6.3.2.1.2 Option 2

The formulation given by [Shrestha and Orlob](#page-264-14) [\(1996\)](#page-264-14) and as subsequently modified by [Mehta et al.](#page-263-13) [\(1989\)](#page-263-13) has the form:

$$cw_s = C^{\alpha} \exp\left(-4.21 + 0.147G\right) \tag{6.74}$$

$$\alpha = 1.11075 + 0.0386G \tag{6.75}$$

where

$$G = \sqrt{\left(\frac{\partial u}{\partial z}\right)^2 + \left(\frac{\partial v}{\partial z}\right)^2} \tag{6.76}$$

is the magnitude of the vertical shear of the horizontal velocity. It is noted that all of these formulations are based on specific dimensional units for input parameters and predicted settling velocities and that appropriate unit conversions are made internally in the implementation in the [EFDC+](#page-11-0) model.

## 6.3.2.1.3 Option 3

[Ziegler and Nisbet](#page-266-8) [\(1994,](#page-266-8) [1995\)](#page-266-9) proposed a formulation to express the effective settling as a function of the floc diameter *d<sup>f</sup>*

<span id="page-101-0"></span>
$$w_s = ad_f^b (6.77)$$

with the floc diameter given by:

$$d_f = \sqrt{\frac{\alpha_f}{C\sqrt{\tau_{xz}^2 + \tau_{yz}^2}}} \tag{6.78}$$

where

*C* is the sediment concentration,

α*j* is an experimentally determined constant, and

τ*xz* and τ*yz* are the *x* and *y* components of the turbulent shear stress at a given position in the water column.

Other quantities in equation [\(6.77\)](#page-101-0) have been experimentally determined to fit the relationships:

$$a = B_1 \left( C \sqrt{\tau_{xz}^2 + \tau_{yz}^2} \right)^{-0.85} \tag{6.79}$$

{102}------------------------------------------------

$$b = -0.8 - 0.5 \log \left( C \sqrt{\tau_{xz}^2 + \tau_{yz}^2} - B_2 \right)$$
 (6.80)

where  $B_1$  and  $B_2$  are experimental constants.

#### 6.3.2.1.4 Option 4

The generalized approach to computing settling velocities based on shear stress is as follows:

$$w_s = \begin{cases} 1.510 \times 10^{-5} (C')^{0.45}, & C' < 40\\ 8 \times 10^{-5}, & 40 \le C' \le 400\\ 0.893 \times 10^{-6} (C')^{0.75}, & C' > 400 \end{cases}$$
(6.81)

$$C' = \tau C \tag{6.82}$$

where  $\tau$  is shear stress  $(cm^2/s^2)$ , and C is total cohesive concentration  $(g/m^3)$ .

#### 6.3.2.2 Deposition

Water column-sediment bed exchange of cohesive sediments and organic solids is controlled by the nearbed flow environment and the geomechanics of the deposited bed. Net deposition to the bed occurs as the flow-induced bed surface stress decreases. The most widely used expression for the depositional flux is:

$$J_o^d = \begin{cases} -w_s C_d \left(\frac{\tau_{cd} - \tau_b}{\tau_{cd}}\right) = -w_s P_d C_d, & \tau_b < \tau_{cd} \\ 0, & \tau_b \ge \tau_{cd} \end{cases}$$

$$(6.83)$$

where

- $\tau_b$  is the stress exerted by the flow on the bed,
- $\tau_{cd}$  is a critical stress for deposition which depends on sediment material and floc physiochemical properties (Mehta et al., 1989), and
- $C_d$  is the near-bed depositing sediment concentration.

The probability of deposition  $P_d$  is based on the linear term,  $(\tau_{cd} - \tau_b)/\tau_{cd}$ . The critical deposition stress is generally determined from laboratory or *in situ* field observations and values ranging from 0.06 to 1.1 N/m<sup>2</sup> have been reported in the literature. Given this wide range of reported values, in the absence of site-specific data, the depositional stress is generally treated as a calibration parameter. The depositional critical stress is an input parameter for each cohesive sediment class in EFDC+.

{103}------------------------------------------------

#### **6.3.2.3** Erosion

Cohesive bed erosion occurs in two distinct modes, mass erosion, and surface erosion. Mass erosion occurs rapidly when the bed stress exerted by the flow exceeds the depth-varying shear strength  $\tau_s$  of the bed at a depth  $H_{me}$  below the bed surface. Surface erosion occurs gradually when the flow-exerted bed stress is less than the bed shear strength near the surface but greater than critical erosion stress  $\tau_{ce}$ , which is dependent on the shear strength and density of the bed. A typical scenario under conditions of accelerating flow and increasing bed stress would involve first the occurrence of gradual surface erosion, followed by a rapid interval of mass erosion, followed by another interval of surface erosion. Alternately, if the bed is well consolidated with a sufficiently high shear strength profile, only gradual surface erosion would occur.

Surface erosion is generally represented by relationships of the form:

<span id="page-103-0"></span>
$$J_o^r = w_r C_r = \frac{dm_e}{dt} \left( \frac{\tau_b - \tau_{ce}}{\tau_{ce}} \right)^{\alpha} , \quad \tau_b \ge \tau_{ce}$$
 (6.84)

or

<span id="page-103-1"></span>
$$J_o^r = w_r C_r = \frac{dm_e}{dt} \exp\left(-\beta \left(\frac{\tau_b - \tau_{ce}}{\tau_{ce}}\right)^{\gamma}\right) , \quad \tau_b \ge \tau_{ce}$$
 (6.85)

where,

 $\frac{dm_e}{dt}$  is the surface erosion rate per unit surface area of the bed,

 $\tau_{ce}$  is the critical stress for surface erosion or resuspension.

The critical erosion rate and stress and the parameters  $\alpha$ ,  $\beta$ , and  $\gamma$  are generally determined from laboratory or *in situ* field experimental observations. Equation (6.84) is more appropriate for consolidated beds, while (6.85) is appropriate for soft partially consolidated beds. The base erosion rate and the critical stress for erosion depend upon the type of sediment, the bed water content, total salt content, ionic species in the water, pH, and temperature (Mehta et al., 1989) and can be measured in laboratory and sea bed flumes.

Surface erosion rates ranging from 0.005 to  $0.1 gs^{-1}m^{-2}$  have been reported in the literature, and it is generally accepted that the surface erosion rate decreases with increasing bulk density. The critical erosion stress is related to but generally less than the shear strength of the bed, which in turn depends upon the sediment type and the state of consolidation of the bed. Experimentally determined relationships between the critical surface erosion stress and the dry density of the bed of the form

$$\tau_{ce} = c\rho_s^d \tag{6.86}$$

have been presented (Mehta et al., 1989).

EFDC+ allows a user-defined constant critical stress for surface erosion or the use of a computed  $\tau_{ce}$  based on one of the following options.

#### 6.3.2.3.1 Option 1

Hwang and Mehta (1989) proposed the relationship

{104}------------------------------------------------

$$\tau_{ce} = \begin{cases} a(\rho_b - \rho_l)^b + c, \ \rho_b > 1.065\\ 0, \ \rho_b \le 1.065 \end{cases}$$
(6.87)

between the critical surface erosion stress and the bed bulk density with *a* = 0.883, *b* = 0.2, *c* = 0.05, and ρ*<sup>l</sup>* = 1.065 for the stress in *N*/*m* 2 and the bulk density in *g*/*cm*<sup>3</sup> .

#### 6.3.2.3.2 Options 2 and 3

[Sanford and Maa](#page-264-15) [\(2001\)](#page-264-15) proposed the relationship

$$\tau_{ce} = \tau_{ci} \frac{(1 + \varepsilon_r)}{(1 + \varepsilon_b)} \tag{6.88}$$

where

τ*ci* is the critical shear stress normalized by water density (*m* <sup>2</sup>/*s* 2 ),

ε*r* is the reference void ratio (dimensionless), and

ε*<sup>b</sup>* is the void ratio of the sediment bed (dimensionless).

The void ratio, ε is defined as the ratio of the volume of voids, φ to the total volume of the sediment (dimensionless).

$$\varepsilon = \frac{\phi}{1 - \phi} \tag{6.89}$$

For Option 2, ε*<sup>b</sup>* is specified using the void ratio of the top sediment bed layer. Option 3 computes ε*<sup>b</sup>* for the void ratio of the top sediment bed layer with cohesive sediment fraction.

### 6.3.2.3.3 Option 4

This option is governed by the relationship:

$$\tau_{ce} = \tau_{ci} \tag{6.90}$$

where τ*ci* is the critical shear stress normalized by water density (*m* <sup>2</sup>/*s* 2 ).

### <span id="page-104-0"></span>6.3.3 Consolidation of Mixed Cohesive and Non-Cohesive Sediment Beds

This section presents a methodology for representing the consolidation of sediment beds containing both cohesive and non-cohesive sediments. The methodology allows for both cohesive and non-cohesive sediment in any bed layer and is based on the following assumptions. First, it is assumed that during the consolidation step, a fraction of the bed pore water volume per unit horizontal area is associated with each sediment type or

<span id="page-104-1"></span>
$$\left(\frac{\varepsilon H_{bed}}{1+\varepsilon}\right) = (\psi_{wc} + \psi_{wn})H_{bed} \tag{6.91}$$

where,

{105}------------------------------------------------

ε is the porosity of the sediment bed (dimensionless),

*Hbed* is the bed thickness (*m*),

ψ is the volume fraction of water with the subscripts, and

*wc* and *wn* denote cohesive and non-cohesive sediment, respectively.

Likewise, the volume of sediment per unit horizontal area can be fractionally partitioned between cohesive and non-cohesive,

<span id="page-105-0"></span>
$$\left(\frac{H_{bed}}{1+\varepsilon}\right) = (\psi_{sc} + \psi_{sn})H_{bed} \tag{6.92}$$

where,

*sc* and *sn* denote the cohesive and non-cohesive sediment for volume fractions, respectively.

Following the Lagrangian formulation of the previous section, the total volume of sediment and the fractional sediment volume in a bed layer remain constant during a consolidation step.

$$\frac{\partial}{\partial} \left( H_{bed} \psi_{sc} \right) = \frac{\partial}{\partial} \left( H_{bed} \psi_{sn} \right) = 0 \tag{6.93}$$

Fractional void ratios can also be defined

<span id="page-105-2"></span>
$$\varepsilon_c = \frac{\psi_{wc}}{\psi_{sc}} \tag{6.94}$$

<span id="page-105-3"></span>
$$\varepsilon_n = \frac{\psi_{wn}}{\psi_{sn}} \tag{6.95}$$

and using equations [\(6.91\)](#page-104-1) and [\(6.92\)](#page-105-0), the void ratio of the mixture is

<span id="page-105-1"></span>
$$\varepsilon = \frac{\psi_{sc}\varepsilon_c + \psi_{sn}\varepsilon_n}{\psi_{sc} + \psi_{sn}} \tag{6.96}$$

which is the sediment volume-weighted average of the void ratios of the two sediment types.

The second assumption is that during the consolidation time step, the fraction of water associated with noncohesive sediment remains constant, as does the fractional void ratio. This is equivalent to assuming that the portion of the bed layer associated with non-cohesive sediment is incompressible and that the pore water associated with the non-cohesive sediment is specified by ε*n*.

Consistent with the preceding assumptions, the thickness of the bed layer can be divided into cohesive and non-cohesive fractions *Hbed*,*<sup>c</sup>* and *Hbed*,*n*, respectively.

$$H_{bed,c} = (\psi_{wc} + \psi_{sc})H_{bed} = (1 + \varepsilon_c)\psi_{sc}H_{bed}$$

$$H_{bed,n} = (\psi_{wn} + \psi_{sn})H_{bed} = (1 + \varepsilon_n)\psi_{sn}H_{bed}$$
(6.97)

The hydraulic conductivity of the layer can be expressed by

{106}------------------------------------------------

<span id="page-106-0"></span>
$$K = \frac{(H_{bed,c} + H_{bed,n})}{\left(\frac{H_{bed,c}}{K_c} + \frac{H_{bed,n}}{K_n}\right)}$$
(6.98)

which is equivalent to an infinite number of alternating infinitesimal cohesive and non-cohesive sublayers of proportional thickness comprising the mixed bed layer. Equation (6.98) can be written as

$$\frac{K}{(1+\varepsilon)} = \frac{1}{\left(f_{sc}\frac{(1+\varepsilon_c)}{K_c} + f_{sn}\frac{(1+\varepsilon_n)}{K_n}\right)}$$
(6.99)

where,

$$f_{sc} = \frac{\psi_{sc}}{(\psi_{sc} + \psi_{sn})}, \text{ and}$$

$$f_{sn} = \frac{\psi_{sn}}{(\psi_{sc} + \psi_{sn})}$$
(6.100)

are the time-invariant total cohesive and non-cohesive sediment fractions in the bed layer. Likewise, equation (6.96) can be written as

<span id="page-106-1"></span>
$$\varepsilon = f_{sc}\varepsilon_c + f_{sn}\varepsilon_n \tag{6.101}$$

The final assumption for the mixed material consolidation formulation is that changes in effective stress are due entirely to changes in the cohesive void ratio. Under this assumption, the specific discharge can be written as

$$q = -\left(\frac{K}{1+\varepsilon}\right)_{k+\frac{1}{2}} \frac{2\lambda_{k+\frac{1}{2}}}{(\Delta_{k+1} + \Delta_k)} \left[ (f_{sc}\varepsilon_c)_{k+1} - (f_{sc}\varepsilon_c)_k \right] + \left(\frac{K}{1+\varepsilon}\right)_{k+\frac{1}{2}} \left(\frac{\bar{\rho}_s}{\rho_w} - 1\right)_{k+\frac{1}{2}}$$
(6.102)

and

$$\lambda_{k+\frac{1}{2}} = -\frac{1}{g\rho_w} \left( \frac{\sigma_{e,k+1} - \sigma_{e,k}}{(f_{sc}\varepsilon_c)_{k+1} - (f_{sc}\varepsilon_c)_k} \right) \tag{6.103}$$

When the depositional void ratio is specified for the surface layer specific discharge becomes

$$q_{w:kt+} = -\left(\frac{2\lambda_{kt+}}{\Delta_{kt}}\right) \left(\frac{K}{1+\varepsilon}\right)_{kt+} \left[\left(\varepsilon_{c}\right)_{dep} - \left(\varepsilon_{c}\right)_{k}\right] + \left(\frac{\bar{\rho}_{s}}{\rho_{w}} - 1\right)_{kt+} \left(\frac{K}{1+\varepsilon}\right)_{kt+}$$
(6.104)

When the zero excess pore pressure boundary condition at the bed surface is used

$$q_{w:kt+} = \left(\frac{K}{1+\varepsilon}\right)_{Kt} \frac{2}{\Delta_{Kt}} \left(\lambda^* f_{sc} \varepsilon_c^{n+1}\right)_{Kt} + \left(\frac{K}{1+\varepsilon}\right)_{Kt} \left(\frac{\bar{\rho}_s}{\rho_w} - 1\right)_{Kt} - \left(\frac{K}{1+\varepsilon}\right)_{Kt} \frac{2}{\Delta_{Kt}} \left(\frac{\sigma_e^n}{g\rho_w} + \lambda^* f_{sc} \varepsilon^*\right)_{Kt}$$
(6.105)

{107}------------------------------------------------

The equation for updating the void ratio is modified using equation (6.101) to give

$$(f_{sc}\varepsilon_c)_k^{**} = (f_{sc}\varepsilon_c)_k^* + \frac{\Delta t}{2} \left(\frac{1+\varepsilon}{H_{bed}}\right)_k^{**} (q_{w:k}-q_{w:k})$$

$$(6.106)$$

Thus the mixed bed layer consolidation formulation essentially solves the space and time evolution of  $f_{sc}\varepsilon_c$  with the continuum constitutive relationship for  $\lambda$  given by

$$\lambda = -\frac{1}{f_{sc}} \frac{\partial}{\partial \varepsilon} \left( \frac{\sigma}{g \rho_w} \right) \tag{6.107}$$

The formulation has the desirable characteristic of reducing to the well-established cohesive formulation in the absence of non-cohesive material. The solution for  $f_{sc}\varepsilon_c$  proceeds by introducing equations (6.92) and (6.94) or (6.95) into (6.96) and solving the resulting tri-diagonal system of equations. The new specific discharges are then directly calculated using equations (6.92) and (6.94) or (6.95) and used to update the layer thickness

$$H_{bed,k}^{n+1} = H_{bed,k}^* + \Delta t \left( q_{w:k-} - q_{w:k+} \right)$$
(6.108)

The ratio  $H_{bed}/(1+\varepsilon)$  can then be updated

$$\left(\frac{H_{bed}}{1+\varepsilon}\right)_{k}^{n+1} = \left(\frac{H_{bed}}{1+\varepsilon}\right)_{k}^{*}$$
(6.109)

Followed by the solution of equation (6.101) for the cohesive void ratio

$$\varepsilon_c = \frac{\varepsilon - f_{sn}\varepsilon_n}{f_{sc}} \tag{6.110}$$

#### <span id="page-107-0"></span>**6.4. SEDZLJ Sediment Transport Module**

The mathematical framework for the unified treatment of erosion, deposition, and bedload transport is referred to as the SEDZLJ model (Jones and Lick, 2000; Ziegler and Lick, 1988, 1986), which incorporates physical and erosion properties of sediment beds measured from an erosion rate measurement apparatus referred to as SEDFlume (Jones and Lick, 2001). EFDC+ incorporates the SEDZLJ module for sediment transport computation with significant enhancements for mass balance, hard bottom bypass, and computational efficiency. This section of the EFDC+ theory document provides the summary of the SEDZLJ's theory (James et al., 2010; Jones and Lick, 2001; Thanh et al., 2008).

#### <span id="page-107-1"></span>6.4.1 Background

Most models are calibrated using hindcasting techniques which can have limitations when extending the simulation to future conditions. The most typically available sediment transport indicator measured in aquatic systems is the suspended sediment concentration. Unfortunately, many different combinations of erosion and deposition rates can be used to reach the same suspended sediment concentration. This can be illustrated as follows.

{108}------------------------------------------------

In the steady state, an equilibrium exists between erosion and deposition. The deposition is generally described as *D* = *PwsC* where *P* is a probability of deposition, *w<sup>s</sup>* is the settling speed of the sediment particles, and *C* is the sediment concentration in the water. Equilibrium then gives

$$E - Pw_s C = 0 (6.111)$$

This can be solved by the sediment concentration, which is

$$C = \frac{E}{Pw_s} \tag{6.112}$$

From this equation, it is seen that any suspended sediment concentration can be matched with an infinite number of erosion rates and deposition parameters by adjusting both accordingly. For example, the observed value of *C* can be obtained by high values of *E* and high values of *Pw<sup>s</sup>* or by low values of *E* and low values of *Pw<sup>s</sup>* . In other words, measurements of suspended sediment concentrations are not sufficient to determine erosion and/or deposition. Historically, erosion was constrained by theoretical relationships between shear stress and grain sizes, however, there is still a range of parameters that would produce the same suspended concentrations. In order to predict erosion and deposition accurately, these quantities should be determined as functions of sediment characteristics and hydrodynamic variables by means of experiments or theory based on experiments.

The [SEDZLJ](#page-12-3) approach [\(Jones and Lick,](#page-261-5) [2000;](#page-261-5) [Ziegler and Lick,](#page-266-0) [1988,](#page-266-0) [1986\)](#page-266-1) incorporates the erosion rates directly measured from the sediment core samples using SEDFlume apparatus [\(Jones and Lick,](#page-261-23) [2001\)](#page-261-23). The SEDFlume consists of a straight flume with an open bottom through which a rectangular cross-section core tube containing sediment can be inserted. The main components of the flume are the core tube and sediment, the test section, the inlet section for uniform, fully developed, turbulent flow, the flow exit section, the water storage tank, and the pump (which forces water through the system). A schematic of the SEDFlume is shown in Figure [6.5.](#page-109-1) Data produced from these tests produce erosion rates, critical shear stress, and bulk density by depth in a core.

{109}------------------------------------------------

<span id="page-109-1"></span>Fig. 6.5. Schematic of the SEDFlume Apparatus.

### <span id="page-109-0"></span>6.4.2 Bed Shear Stress

In [EFDC,](#page-11-2) the [SEDZLJ](#page-12-3) module computes the bed shear stress τ*<sup>b</sup>* (dynes/cm<sup>2</sup> ) as:

$$\tau_b = \rho_w c_f V^2 \tag{6.113}$$

where ρ*<sup>w</sup>* is the density of water (g/cm<sup>3</sup> ) and *V* is the flow velocity magnitude (cm/s). The bottom shear stress friction factor *c<sup>f</sup>* (dimensionless) is calculated using a log-layer distribution of velocity as:

$$c_f = \begin{cases} \frac{\kappa^2}{\left(\ln\frac{11H}{2z_b}\right)^2} & \text{for } H \ge H_{min} \\ 0.0 & \text{for } H < H_{min} \end{cases}$$

$$(6.114)$$

where

κ is von Karman's constant (κ=0.42),

*z<sup>b</sup>* is bottom skin friction based on the *d*<sup>50</sup> at the sediment surface (m), and

*Hmin* is the minimum depth to allow shear computations (m).

The bottom skin friction is assumed to be equal to the average particle diameter of the surface of the sediment bed at any given location. Therefore, the bottom shear stress friction factor *c<sup>f</sup>* increases as the particle size at the sediment bed surface increases or as the depth of water decreases.

{110}------------------------------------------------

### <span id="page-110-0"></span>6.4.3 Erosion Rate

Results of a typical application of SEDFlume are shown in Figure [6.6,](#page-110-1) where erosion rates *E* in units of cm/s are plotted as a function of bed depth (cm) with shear stress τ (N/m<sup>2</sup> ). Erosion rates are generally highest at the surface and decrease with depth; they also increase with shear stress. In general, information of this type for sediments throughout the system is necessary for accurate predictions of sediment transport [\(Jones](#page-261-5) [and Lick,](#page-261-5) [2000\)](#page-261-5). The availability of this type of data is assumed and is used in [SEDZLJ.](#page-12-3)

<span id="page-110-1"></span>Fig. 6.6. SEDFlume Data for Conowingo Reservoir (DNR Maryland).

Information on erosion rates is generally reported in units of cm/s. In order to convert this to a mass flux in units of g/cm<sup>2</sup> /s, which is needed in the modeling, the mass of solids within a sediment volume is needed. This quantity, for a sediment consisting of solids and water only (i.e., no gas), can be determined in terms of the bulk density of the sediments ρ as follows:

$$\rho = \rho_s x_s + \rho_w x_w = \rho_s x_s + \rho_w (1 - x_s)$$
(6.115)

{111}------------------------------------------------

where

ρ*s* is the density of solids (g/cm<sup>3</sup> ),

*xs* is the volume fraction of the solids,

ρ*<sup>w</sup>* is the density of water (g/cm<sup>3</sup> ), and

*x<sup>w</sup>* is the volume fraction of water.

Since *x<sup>w</sup>* = 1 − *x<sup>s</sup>* , the mass of solids per unit volume is *xs*ρ*<sup>s</sup>* , which can be determined from the above equation as:

$$x_s \rho_s = \frac{\rho_s (\rho - \rho_w)}{\rho_s - \rho_w} = \frac{2.6}{1.6} (\rho - 1)$$
 (6.116)

where it is assumed that ρ*<sup>s</sup>* = 2.6g/cm<sup>3</sup> and ρ*<sup>w</sup>* = 1.0 g/cm<sup>3</sup> . Once the bulk density of the sediments is known, the erosion rate in units of g/cm<sup>2</sup> /s can be determined by multiplying the erosion rate in units of cm/s by *xs*ρ*<sup>s</sup>* .

As indicated above, erosion rates change as a function of bed depth. This variation is incorporated into the sediment bed model through a discrete layering system where the erosion rate is defined at each layer interface, and the particle size distribution and bulk density are defined as constant throughout the layer. Any number and thickness of layers required to approximate the variation of sediment properties with depth can be introduced as necessitated by field data.

The [SEDZLJ](#page-12-3) sediment transport model can incorporate erosion rate data collected in the field that are typically spatially discrete and at specific depths but can also be interpolated where no direct data are available. The total erosion rate is interpolated across sediment layer thicknesses and shear stresses. Linear interpolation is used to calculate an erosion rate at a specified shear stress τ as:

<span id="page-111-0"></span>
$$E\left(\tau\right) = \left(\frac{\tau_{i+1} - \tau}{\tau_{i+1} - \tau_i}\right) E_i + \left(\frac{\tau - \tau_i}{\tau_{i+1} - \tau_i}\right) E_{i+1} \tag{6.117}$$

where subscript *i* denotes data for a shear stress less than τ and *i*+1 denotes measured data for a shear stress greater than τ, with τi<τ<τi+1.

Because *E* often changes rapidly with depth, the logarithmic interpolation between data points best represents erosion rates as a function of depth:

<span id="page-111-1"></span>
$$\ln[E(T)] = \left(\frac{T_0 - T}{T_0}\right) \ln(E^j) + \frac{T}{T_0} \ln\left(E^{j+1}\right)$$
(6.118)

where *T* is the actual sediment bed layer thickness, *T*<sup>0</sup> is the initial bed layer thickness, and the superscripts *j* and *j* + 1 denote data for the interface at the top and the bottom of the specific layer where the erosion rate is required, respectively. Equations [\(6.117\)](#page-111-0) and [\(6.118\)](#page-111-1) are combined so that the erosion rates may be calculated as a function of shear stress and depth.

{112}------------------------------------------------

### 6.4.3.1 Critical Shear Stress for Erosion

In addition to erosion rates, another parameter of significance in modeling is the critical stress for erosion, τ*ce*. Consider the flow of water over a sediment bed. As the rate of flow is increased starting from rest, there is a range of velocities (or shear stresses) at which the movement of the easiest-to-move particles (generally the smallest) is first noticeable to an observer. These eroded particles then travel a relatively short distance until they come to rest in a new location. This initial motion tends to occur only at a few isolated spots. As the flow velocity and shear stress increase further, more particles participate in this process of erosion, transport, and deposition, and the movement of the particles becomes more sustained.

Because of this gradual increase in sediment erosion as the shear stress increases, it is difficult to precisely define a critical velocity or critical shear stress at which sediment erosion is first initiated. More quantitatively and with less ambiguity, critical shear stress for erosion can be defined as the shear stress at which a small but accurately measurable rate of erosion occurs. [Roberts et al.](#page-263-1) [\(1998\)](#page-263-1) defined this rate as 10−<sup>6</sup> m/s represented by approximately 1 mm of erosion in 15 minutes, though different rates have been used to define τ*ce*.

Critical shear stresses for erosion as a function of particle diameter *d* are shown in Figure [6.7.](#page-113-0) For *d* ¿ 200 µm, the sediments behave in a non-cohesive manner, i.e., they consolidate rapidly, and they erode particle by particle. For *d* ¡ 200 µm, cohesive effects between particles become significant. The sediments consolidate relatively slowly with time, and the critical stresses depend not only on particle diameter but also on the bulk density of the sediments. For these cohesive sediments, τ*ce* increases as *d* decreases and as bulk density increases.

For non-cohesive sediment beds, the curve of [Shields](#page-264-16) [\(1936\)](#page-264-16), or any approximation thereof [van Rijn](#page-265-11) [\(1984\)](#page-265-11) could be used to define the critical shear stress for erosion. [Soulsby et al.](#page-264-17) [\(1997\)](#page-264-17) approximated the critical shear for erosion as:

$$\tau_{ce} = \rho g d\theta = \rho g d \left\{ \frac{0.3}{1 + 1.2d_*} + 0.055 \left[ 1 - \exp(-0.02d_*) \right] \right\}$$
 (6.119)

<span id="page-112-0"></span>
$$d_* = d \left[ (\rho_{sd}/\rho_w - 1) g/v^2 \right]^{1/3}$$
 (6.120)

where

*g* is the acceleration due to gravity,

*d* is the sediment particle diameter,

*d*<sup>∗</sup> is the non-dimensional particle diameter,

*v* is the kinematic fluid viscosity, and

θ is the critical Shields parameter, represented by the algebraic fit shown in the parenthesis in equation [\(6.119\)](#page-112-0)

{113}------------------------------------------------

<span id="page-113-0"></span>Fig. 6.7. Critical Shear Stresses for Erosion and Suspension of Quartz Particles.

#### 6.4.3.2 Erosion into Suspended Load versus Bedload

As bottom sediments are eroded, a fraction of the sediments are suspended into the overlying water and are transported as suspended loads; the rest of the eroded sediments move by rolling and/or sliding in a thin layer near the bed in what is called bedload. The fraction in each of the transport modes depends on the particle size and shear stress.

For fine-grained particles (which are generally cohesive), erosion occurs both as individual particles and in the form of chunks or small aggregates of particles. The individual particles move as a suspended load. The aggregates tend to move downstream near the bed but generally seem to disintegrate into small particles in the high-stress boundary layer near the bed as they move downstream. These disaggregated particles then move as suspended loads. For this reason, it is assumed that fine-grained sediments less than 200 µm are completely transported as suspended load.

Coarser, non-cohesive particles (defined here as those particles with diameters greater than about 200 µm) can be transported both as suspended load and bedload, with the fraction in each dependent on particle diameter and shear stress. For particles of a particular size, the shear stress at which the suspended load (or sediment suspension) is initiated is defined as τ*cs* (N/m<sup>2</sup> ). This shear stress τ*cs*, can be defined from the [van](#page-265-11) [Rijn](#page-265-11) [\(1984\)](#page-265-11) formulations as:

$$\tau_{cs} = \begin{cases} \frac{1}{\rho_w} \left(\frac{4w_s}{d_*}\right)^2, & \text{for } d \le 400 \ \mu m\\ \frac{1}{\rho_w} (0.4w_s)^2, & \text{for } d > 400 \ \mu m \end{cases}$$
(6.121)

where

{114}------------------------------------------------

- $d_*$  is the non-dimensional particle diameter calculated from  $d_* = d \left[ \frac{(\rho_s \rho)}{\rho} \frac{g}{v^2} \right]^{1/3}$  where d is the particle diameter (cm), and
- $w_s$  is the particle settling speed (cm/s)

For  $\tau^b > \tau_{cs}$ , sediments are transported both as bedload and suspended load with the fraction in suspended load f increasing with  $\tau^b$  from f = 0 until f reaches 1. For  $\tau^b$  greater than this, sediments are transported completely as suspended load.

In EFDC+, the settling speed of each sediment class is determined as a user-specified input parameter, which can be specified based on Cheng (1997) and van Rijn (1984). Cheng's formula for settling speed is

<span id="page-114-0"></span>
$$w_s = \frac{v}{d} \left( \sqrt{25 + 1.2d_*^2} - 5 \right)^{1.5} \tag{6.122}$$

where v is the kinematic fluid viscosity (cm<sup>2</sup>/s).

Since Cheng's formula is based on the observations of the settling of real sediment particles, it produces settling speeds lower than Stoke's law. This is because real sediments are often irregular in shape and have a greater hydrodynamic resistance to settling than perfect spheres as in Stoke's law.

van Rijn (1984) computes the settling velocity as

$$w_{s} = \begin{cases} \frac{1}{18} \left[ \frac{(s-1)gD_{s}^{2}}{v} \right], & D_{s} < 100 \,\mu\text{m} \\ 10 \frac{v}{D_{s}} \left\{ \left[ 1 + \frac{0.01(s-1)gD_{s}^{3}}{v^{2}} \right]^{0.5} - 1 \right\}, & 100 \,\mu\text{m} \le D_{s} < 1000 \,\mu\text{m} \\ 1.1 \left[ (s-1) gD_{s} \right]^{0.5}, & D_{s} \ge 1000 \,\mu\text{m} \end{cases}$$
(6.123)

where

- $D_s$  is the representative particle size (m),
- s is the specific density,
- g is the acceleration due to gravity  $(m/s^2)$ , and
- v is the kinematic viscosity coefficient and  $w_s$  is in m/s.

Guy et al. (1966) performed detailed flume measurements of suspended load and bedload transport for sediments ranging in median diameter  $d_{50}$ , from 190  $\mu$ m to 930  $\mu$ m. They found that, as the ratio of shear velocity (defined as  $u_* = \sqrt{\tau^b/\rho_w}$ ) to settling velocity increases, the proportion of suspended load to total load transport,  $q_s/q_t$  increases. An approximation of their data can be made with the following function:

$$\frac{q_{s}}{q_{t}} = \begin{cases}
0, & \tau^{b} < \tau_{cs} \\
\frac{\ln(u_{*}/w_{s}) - \ln(\sqrt{\tau_{cs}/\rho_{w}}/w_{s})}{\ln(4) - \ln(\sqrt{\tau_{cs}/\rho_{w}}/w_{s})}, & \tau^{b} > \tau_{cs} \text{ and } \frac{u_{*}}{w_{s}} < 4 \\
1, & \frac{u_{*}}{w_{s}} > 4
\end{cases}$$
(6.124)

{115}------------------------------------------------

This approximation is used in the [EFDC+](#page-11-0) implementation. The original data is shown with the result given by the above equation in Figure [6.8.](#page-115-0)

<span id="page-115-0"></span>Fig. 6.8. Results from Flume Measurements of Suspended Load and Bedload [\(Guy et al.,](#page-261-1) [1966\)](#page-261-1).

Although sediments in nature have a continuous size distribution, physical quantities in numerical models are inherently discrete; hence, sediment particle sizes are discretized. The discretization of particle size classes *j* is done by measuring the different sediment sizes in a site-specific sediment core and grouping them into appropriate size classes. The sediment bed in the model is described as the product of the particle size class and the corresponding mass fraction. By multiplying the total erosion flux of a particular size class *j* by *qs*/*q<sup>t</sup>* , the erosion flux of that class into suspended load *Es*, *<sup>j</sup>* can be calculated. The corresponding erosion flux into bedload *Eb*, *<sup>j</sup>* is also calculated by multiplying the total erosion flux of the size class by the factor (1−*qs*/*qt*). Thus, the erosion flux for any size class *j* is

$$E_{s,j} = \begin{cases} 0, & \tau^b < \tau_{ce} \\ \frac{q_s}{q_t} f_j E, & r\tau^b \ge \tau_{ce} \end{cases}$$
 (6.125)

$$E_{b,j} = \begin{cases} 0, & \tau^b < \tau_{\text{ce}} \\ \left(1 - \frac{q_s}{q_t}\right) f_j E, & \tau^b \ge \tau_{\text{ce}} \end{cases}$$
 (6.126)

where *f<sup>j</sup>* is the mass fraction of the *j th* sediment size class.

{116}------------------------------------------------

### <span id="page-116-0"></span>6.4.4 Suspended Load

For suspended sediments, the three-dimensional, time-dependent transport equation in the water over the bed is shown in equation [\(6.1\)](#page-86-1). The net sediment flux into suspension *Q<sup>s</sup>* is calculated as the total erosion flux into suspended load *Es*, *<sup>j</sup>* minus the deposition flux from suspended load *Ds*, *<sup>j</sup>* for each sediment size class *j*:

$$Q_{s,j} = E_{s,j} - D_{s,j} (6.127)$$

where

$$Q_s = \sum_j Q_{s,j} \tag{6.128}$$

In a quiescent fluid where no shear stress is present, the deposition flux for suspended sediments can be described as the product of the settling speed of the sediment and the concentration of the sediment in the overlying water. However, in flowing water, the deposition is affected by the fluid turbulence, quantified as shear stress. In this case, a probability of deposition for each size class *j*, *P<sup>k</sup>* can be included in the formulation to account for the effects of the shear stress to yield:

$$D_{sj} = P_j w_{sj} C_{sj} \tag{6.129}$$

This probability would be unity in the case of quiescent flow and decrease as the flow, turbulence, and shear stress increase. The probability for suspended load deposition seems to differ for cohesive and non-cohesive particle sizes. For cohesive particles (size classes with effective diameters less than 200 µm), [Krone](#page-262-8) [\(1962\)](#page-262-8) found that the probability of deposition varied approximately as:

$$P_{j} = \begin{cases} 0 & \text{for } \tau^{b} \tau_{cs,j} \\ \left(1 - \frac{\tau^{b}}{\tau_{cs,j}}\right) & \text{for } \tau^{b} > \tau_{cs,j} \end{cases}$$
 (6.130)

For larger non-cohesive particles (size classes with an effective diameter greater than 200 µm), [Gessler](#page-260-14) [\(1967\)](#page-260-14) showed that the probability of deposition could be described with a Gaussian distribution or error function given by:

$$P_{j}(Y) = \operatorname{erf}\left(\frac{Y}{2}\right) = \frac{2}{\sqrt{\pi}} \int_{0}^{Y/2} \exp\left(-\xi^{2}\right) d\xi$$
 (6.131)

where

$$Y = \frac{1}{\sigma} \left( \frac{\tau_{cs,j}}{\tau^b} - 1 \right) \tag{6.132}$$

where τ*cs*, *<sup>j</sup>* is the critical shear stress for suspension for size class *j* and σ is the standard deviation for shear stress variation, which [Gessler](#page-260-14) [\(1967\)](#page-260-14) determined to be about 0.57.

An approximation to this function for *Y* > 0 with an error of less than 0.001 % is found to be [\(Abramowitz,](#page-258-11) [1964;](#page-258-11) [Dwight,](#page-260-15) [1947\)](#page-260-15):

{117}------------------------------------------------

$$P_j = 1 - F(Y)(0.4632X - 0.1202X^2 + 0.9373X^3)$$
(6.133)

where

$$F(Y) = \frac{1}{(2\pi)^{1/2}} e^{-\frac{1}{2}Y^2}$$
 (6.134)

$$X = \frac{1}{(1 + 0.33267Y)} \tag{6.135}$$

When *Y* < 0

$$P_{j} = 1 - P(|Y|) \tag{6.136}$$

<span id="page-117-1"></span>Figure [6.9](#page-117-1) shows sample probability distributions using the formulations for cohesive and non-cohesive particles.

Fig. 6.9. Sample Probability Distributions for Cohesive and Non-Cohesive Particles.

#### <span id="page-117-0"></span>6.4.5 Bedload

For the description of bedload transport, the [van Rijn](#page-265-11) [\(1984\)](#page-265-11) approach is used. To calculate the concentration of particles moving in bedload, a mass balance equation can be written as:

$$\frac{\partial (mC_b)}{\partial t} = \frac{\partial (mq_{bx})}{\partial x} + \frac{\partial (mq_{by})}{\partial y} + Q_b \tag{6.137}$$

where

{118}------------------------------------------------

*C<sup>b</sup>* is the bedload concentration (g/cm<sup>2</sup> ),

*q<sup>b</sup>* is the horizontal bedload flux in the *x* or *y* directions (g/s/cm),

*m* is the cell area (cm<sup>2</sup> ), and

*Q<sup>b</sup>* is the net vertical flux of sediments between the sediment bed and bedload (g/s).

This equation is solved using a central difference approximation for the fluxes in the *x* and *y* directions. The horizontal bedload flux in general is calculated as

$$q_b = u_b C_b \tag{6.138}$$

where *u<sup>b</sup>* is the bedload velocity (cm/s) in the direction of interest. The bedload velocity and thickness can be calculated from [van Rijn](#page-265-11) [\(1984\)](#page-265-11) using formulations as follows:

$$u_b = 1.5T^{0.6}[(\rho_s - 1)gd]^{0.5}$$
(6.139)

$$h_b = 3dd_*^{0.6} T^{0.9} (6.140)$$

The transport parameter *T* is calculated as:

$$T = \frac{\tau^b - \tau_{ce}}{\tau_{ce}} \tag{6.141}$$

The flux of sediments between the bottom sediments and bedload *Q<sup>b</sup>* is calculated as the erosion of sediments into bedload *E<sup>b</sup>* minus the deposition of sediments from bedload *D<sup>b</sup>* and is

$$Q_b = E_b - D_b \tag{6.142}$$

where *D<sup>b</sup>* is given by:

$$D_b = Pw_s C_b \tag{6.143}$$

In steady state equilibrium, the concentration of sediments in bedload, *C<sup>e</sup>* is due to a dynamic equilibrium between erosion and deposition:

$$E_b = Pw_s C_e \tag{6.144}$$

From this, the probability of deposition can be written as:

<span id="page-118-0"></span>
$$P = \frac{E_b}{w_s C_e} \tag{6.145}$$

The erosion rate can be determined from SEDFlume, while the settling speed can be calculated from equation [\(6.123\)](#page-114-0). The equilibrium concentration *C<sup>e</sup>* has been investigated by several authors; the formulation by [van Rijn](#page-265-11) [\(1984\)](#page-265-11) will be used here and is calculated as:

{119}------------------------------------------------

$$C_e = 0.117 \frac{\rho_s T}{d_*} \tag{6.146}$$

Once *Eb*, *w<sup>s</sup>* , and *C<sup>e</sup>* are known as a function of particle diameter and shear stress, *P* can be calculated from equation [\(6.145\)](#page-118-0). It is then assumed that this probability is also valid for the non-steady case so that the deposition rate can be calculated in this case.

The equilibrium concentration *C<sup>e</sup>* is based on experiments with uniform sediments. In general, the sediment bed must be represented by more than one size class. In this case, the erosion rate for each size class is given by *fjEb*, and the probability of deposition for the size class *j* is then given by:

<span id="page-119-1"></span>
$$P_{j} = \frac{f_{j}E_{b}}{w_{sj}f_{j}C_{ej}} = \frac{E_{b}}{w_{sj}C_{ej}}$$
(6.147)

In equation [\(6.147\)](#page-119-1), it is implicitly assumed that there is a dynamic equilibrium between erosion and deposition for each size class *j*.

#### <span id="page-119-0"></span>6.4.6 Bed Armoring

A decrease in sediment erosion rates with time, or bed armoring, can occur due to (1) the consolidation of cohesive sediments with depth and time, (2) the deposition of coarser sediments on the sediment bed during a flow event, and (3) the erosion of finer sediments from the surface sediment, leaving coarser sediments behind, again during a flow event. The consolidation of sediments and subsequent change in erosion rates with depth can be determined by SEDFlume in-situ measurements. The consolidation of sediment and increase of erosion rates with time can be determined approximately from consolidation studies, again by means of SEDFlume.

Here we are concerned about bed armoring due to processes (2) and (3). In order to describe these processes, it is assumed in the present model that a thin mixing layer, or active layer, is formed at the surface of the bed. The existence and properties of this have been discussed by previous researchers [\(Parker et al.,](#page-263-14) [2000;](#page-263-14) [van Niekerk et al.,](#page-265-13) [1992\)](#page-265-13). The presence of this active layer permits the interaction of depositing and eroding sediments to occur in a discrete layer without allowing deposited sediments to affect the undisturbed sediments below. The authors in [van Niekerk et al.](#page-265-13) [\(1992\)](#page-265-13) have suggested that the thickness *T<sup>a</sup>* can be approximated by:

$$T_a = 2d_{50} \frac{\tau^b}{\tau_{ce}} \tag{6.148}$$

This formulation takes into account the deeper penetration of turbulence into the bed with increasing shear stress. In the present calculations, *d*<sup>50</sup> is approximated by the average diameter in the interest of computational efficiency.

{120}------------------------------------------------

<span id="page-120-0"></span>Fig. 6.10. Diagram of SEDflume Layering System.

Since the active layer is kept at a constant thickness (*Ta*), three possible states of the active layer must be considered. The first state is a net erosion of the active layer, where there may be deposition occurring, but the net flux is erosional. If the thickness of the active layer after this net erosion is *T* then a thickness of material equal to *Ta*−*T* is added to the active layer so that a thickness of *T<sup>a</sup>* can be maintained. This material is added from the layer below in size class proportions equivalent to that in the layer below. The second possible state of the active layer is a net depositional state where the thickness of the active layer exceeds *Ta*. In this case, the excess material *T* −*T<sup>a</sup>* is put into a newly deposited material layer just below the active layer but above the parent bed. This material is added to the deposited layer in size class proportions equal to the active layer. The third state of the active layer is where *T* is equal in thickness to *Ta*. In this case, no action is taken. Figure [6.10](#page-120-0) shows a diagram of the layering system.

The erosion rates for this active layer are dependent on its average particle size. Figure [6.11](#page-121-0) shows the erosion rate vs. particle diameter for quartz sediment. It is seen that as the particle diameter increases beyond 200 µm, the erosion rate decreases. This demonstrates how bed coarsening affects erosion rates. A dataset of this type can be constructed utilizing laboratory and field cores to determine erosion rates as a function of particle size for any particular site. The erosion rate for an active or deposited layer can then be calculated from the average particle size of the layer with an interpolation similar to equation [\(6.117\)](#page-111-0) with particle size in place of thickness.

{121}------------------------------------------------

<span id="page-121-0"></span>Fig. 6.11. Erosion Rates Versus Particle Size and Shear Stress for a Bulk Density of 1.9 g/cm<sup>2</sup> , adapted from [Roberts et al.](#page-263-1) [\(1998\)](#page-263-1) by [James et al.](#page-261-2) [\(2010\)](#page-261-2).

{122}------------------------------------------------

## <span id="page-122-0"></span>Chapter 7

## CHEMICAL FATE AND TRANSPORT

This chapter presents processes associated with the fate and transport of organic and metallic compounds and their mathematical modeling in water and sediments. It starts with the basic equations and their numerical aspects, then follows by characteristics of organic chemicals and metals, and the sorption and desorption processes. Figure [7.1](#page-122-1) provides an outline of the conceptual model for the chemical fate and transport in [EFDC+.](#page-11-0)

<span id="page-122-1"></span>Fig. 7.1. Conceptual Model of Chemical Fate and Transport in [EFDC+.](#page-11-0)

{123}------------------------------------------------

#### <span id="page-123-0"></span>7.1. Development Overview

When the "original" sediment transport capability was added, chemical fate and transport was also added (Tetra Tech, 2002b). This module allows for optional chemical partitioning onto water columns and sediment bed solids. Prior to 2015, even though multiple partitioning options were available, only one approach could be used for all the chemicals included in a simulation. DSI updated the chemical partitioning module to allow each chemical constituent to use its own unique partitioning approach. Figure 7.2 provides a schematic of the basic approach.

<span id="page-123-2"></span>Fig. 7.2. Linkage Between Hydrodynamic, Sediment Transport, and Chemical Fate and Transport Model.

#### <span id="page-123-1"></span>7.2. Basic Equations

The transport of a sorptive chemical in the water column is governed by transport equations for the chemical dissolved in the water phase, sorbed to material effectively dissolved in the water phase, and sorbed to the suspended sediment particles. Note that the equations below have been generalized for water column processes with general source terms neglected for simplicity.

For the portion of the chemical dissolved in the water phase, the transport can be described as

<span id="page-123-3"></span>
$$\frac{\partial}{\partial t} (mHC_{w}) + \frac{\partial}{\partial x} (m_{y}HuC_{w}) + \frac{\partial}{\partial y} (m_{x}HvC_{w}) + \frac{\partial}{\partial z} (mwC_{w}) = 
\frac{\partial}{\partial z} \left( m\frac{A_{b}}{H} \frac{\partial}{\partial z} C_{w} \right) + mH \left( \sum_{i} \left( K_{dS}^{i} S^{i} \chi_{S}^{i} \right) + \sum_{j} \left( K_{dD}^{j} D^{j} \chi_{D}^{j} \right) \right) 
- mH \sum_{i} \left( K_{aS}^{i} S^{i} \right) \left( \psi_{w} \frac{C_{w}}{\phi} \right) \left( \widehat{\chi}_{S}^{i} - \chi_{S}^{i} \right) 
- mH \sum_{j} \left( K_{aD}^{j} D^{j} \right) \left( \psi_{w} \frac{C_{w}}{\phi} \right) \left( \widehat{\chi}_{D}^{j} - \chi_{D}^{j} \right) - mH\gamma C_{w} \quad (7.1)$$

{124}------------------------------------------------

The transport equation for the portion of material sorbed to a dissolved constituent D is,

$$\frac{\partial}{\partial t} \left( mHD^{j} \chi_{D}^{j} \right) + \frac{\partial}{\partial x} \left( m_{y} H u D^{j} \chi_{D}^{j} \right) 
+ \frac{\partial}{\partial y} \left( m_{x} H v D^{j} \chi_{D}^{j} \right) + \frac{\partial}{\partial z} \left( m w D^{j} \chi_{D}^{j} \right) 
= \frac{\partial}{\partial z} \left( m \frac{A_{b}}{H} \frac{\partial}{\partial z} \left( D^{j} \chi_{D}^{j} \right) \right) + mH \left( K_{sD}^{j} D^{j} \right) \left( \psi_{w} \frac{C_{w}}{\phi} \right) \left( \widehat{\chi}_{D}^{j} - \chi_{D}^{j} \right) 
- mH \left( K_{dD}^{j} + \gamma \right) \left( D^{j} \chi_{D}^{j} \right) \quad (7.2)$$

The transport equation for the portion of material sorbed to a suspended constituent S is,

<span id="page-124-1"></span><span id="page-124-0"></span>
$$\frac{\partial}{\partial t} \left( mHS^{i} \chi_{S}^{i} \right) + \frac{\partial}{\partial x} \left( m_{y} HuS^{i} \chi_{S}^{i} \right) 
+ \frac{\partial}{\partial y} \left( m_{x} HvS^{i} \chi_{S}^{i} \right) + \frac{\partial}{\partial z} \left( mwS^{i} \chi_{S}^{i} \right) 
= \frac{\partial}{\partial z} \left( m\frac{A_{b}}{H} \frac{\partial}{\partial z} \left( S^{i} \chi_{S}^{i} \right) \right) + mH \left( K_{aS}^{i} S^{i} \right) \left( \psi_{w} \frac{C_{w}}{\phi} \right) \left( \widehat{\chi}_{S}^{i} - \chi_{S}^{i} \right) 
- mH \left( K_{aS}^{i} + \gamma \right) \left( S^{i} \chi_{S}^{i} \right) \quad (7.3)$$

{125}------------------------------------------------

where,

 $C_w$  is the mass of a dissolved chemical per unit total volume  $(mg/m^3)$ ,

 $S^i$  is the mass of sediment class  $i(g/m^3)$ ,

 $D^{j}$  is the mass of the dissolved substance class j (i.e. DOC)  $(g/m^{3})$ ,

 $\chi_S^i$  is the mass of contaminant sorbed to sediment class i per mass of sediment (mg/g),

 $\chi_D^j$  is the mass of contaminant sorbed to dissolved material j per unit mass of dissolved material (i.e. sorbed to DOC) (mg/g),

 $\widehat{\chi}$  is the saturation sorbed mass per carrier mass, with subscripts denoting sediment *S* or dissolved material *D* and superscripts denoting the class of sediment *i* or class of dissolved material j (mg/g),

 $\phi$  is the porosity (dimensionless),

 $\psi_w$  is the fraction of the water dissolved contaminant available for sorption (dimensionless),

 $K_{aS}$  is the sorption rate of sediment (/s),

 $K_{aD}$  is the sorption rate of dissolved material (/s),

 $K_{dS}$  is the desorption rate of sediment (/s),

 $K_{dD}$  is the desorption rate of dissolved material (/s),

 $\gamma$  is the net loss rate due to biodegradation, volatilization, and/or decay.

#### <span id="page-125-0"></span>7.3. Chemical Partitioning

The sorption kinetics are based on the Langmuir isotherm (Chapra et al., 1997). Introducing sorbed concentrations defining sorbed mass per unit total volume

<span id="page-125-3"></span>
$$C_D^j = D^j \chi_D^j \tag{7.4}$$

<span id="page-125-4"></span>
$$C_S^i = S^i \chi_S^i \tag{7.5}$$

The EFDC+ sorbed contaminant transport formulation currently employs equilibrium partitioning with the sorption and desorption terms

<span id="page-125-1"></span>
$$\left(K_{sD}^{j}D^{j}\right)\left(\psi_{w}\frac{C_{w}}{\phi}\right)\left(\widehat{\chi}_{D}^{j}-\chi_{D}^{j}\right)=K_{dD}^{j}C_{D}^{j}\tag{7.6}$$

<span id="page-125-2"></span>
$$\left(K_{aS}^{i}S^{i}\right)\left(\psi_{w}\frac{C_{w}}{\phi}\right)\left(\widehat{\chi}_{S}^{i}-\chi_{S}^{i}\right)=K_{dS}^{i}C_{S}^{i}\tag{7.7}$$

Solving equations (7.6) and (7.7) for the sorbed to water phase concentration ratios gives

{126}------------------------------------------------

<span id="page-126-0"></span>
$$\frac{C_D^j}{C_W} = \frac{f_D^j}{f_W} = P_D^j \frac{D^j}{\phi}$$

$$P_D^j = P_{Do}^j \left( 1 + P_{Do}^j \left( \frac{C_W}{\widehat{\chi}_D^j \phi} \right) \right)^{-1}$$

$$P_{Do}^j = \frac{\psi_w K_{aD}^j \widehat{\chi}_D^j}{K_{dD}^j}$$
(7.8)

<span id="page-126-1"></span>
$$\frac{C_S^i}{C_W} = \frac{f_S^i}{f_W} = P_S^i \frac{S^i}{\phi}$$

$$P_S^i = P_{So}^i \left( 1 + P_{So}^i \left( \frac{C_W}{\widehat{\chi}_S^i \phi} \right) \right)^{-1}$$

$$P_{So}^i = \frac{\psi_w K_{aS}^i \widehat{\chi}_S^i}{K_{dS}^i}$$
(7.9)

where, P denotes the partition coefficient, and  $P_o$  is its linear equilibrium value. For linear equilibrium partitioning, P is set to  $P_o$ , which in effect approximates

$$\left(1 + P_{So}^{i}\left(\frac{C_{w}}{\widehat{\chi}_{S}^{i}\phi}\right)\right)^{-1}$$

terms in equations (7.8) and (7.9) as unity. Requiring the mass fractions to sum to unity

$$f_w + \sum_i f_S^i + \sum_j f_D^j = 1 \tag{7.10}$$

gives

<span id="page-126-2"></span>
$$f_{w} = \frac{C_{w}}{C} = \frac{\phi}{\phi + \sum_{i} P_{S}^{i} S^{i} + \sum_{j} P_{D}^{j} D^{j}}$$

$$f_{D}^{j} = \frac{C_{D}^{j}}{C} = \frac{P_{D}^{j} D^{j}}{\phi + \sum_{i} P_{S}^{i} S^{i} + \sum_{j} P_{D}^{j} D^{j}}$$

$$f_{S}^{i} = \frac{C_{S}^{i}}{C} = \frac{P_{S}^{i} S^{i}}{\phi + \sum_{i} P_{D}^{i} S^{i} + \sum_{j} P_{D}^{j} D^{j}}$$
(7.11)

The dissolved concentrations can be alternately expressed by mass per unit volume of the water phase

$$C_{w:w} = \frac{C_w}{\phi}$$

$$C_{D:w}^j = \frac{C_D^j}{\phi}$$

$$D_{:w}^J = \frac{D^j}{\phi}$$
(7.12)

with equation (7.11) becoming

{127}------------------------------------------------

<span id="page-127-4"></span>
$$\frac{C_{w;w}}{C} = \frac{1}{\phi + \sum_{i} P_{S}^{i} S^{i} + \sum_{j} P_{D}^{j} \phi D_{:w}^{j}}$$

$$\frac{C_{D;w}^{j}}{C} = \frac{P_{D}^{j} D_{:w}^{j}}{\phi + \sum_{i} P_{S}^{i} S^{i} + \sum_{j} P_{D}^{j} \phi D_{:w}^{j}}$$

$$\frac{C_{S}^{i}}{C} = \frac{P_{S}^{i} S^{i}}{\phi + \sum_{i} P_{S}^{i} S^{i} + \sum_{j} P_{D}^{j} \phi D_{:w}^{j}}$$
(7.13)

which is a generalization of the Chapra et al. (1997) formulation for adsorption to DOC and POC.

#### <span id="page-127-0"></span>7.4. Water Column Chemical Transport and Boundary Conditions

The partitioning relationships shown in equation (7.4) and equation (7.5) allows equations (7.1), (7.2), and (7.3) to be expanded into the transport equation for each contaminant fractions

$$\frac{\partial}{\partial t} (mHC_w) + \frac{\partial}{\partial x} (m_y H u C_w) + \frac{\partial}{\partial y} (m_x H v C_w) + \frac{\partial}{\partial z} (m_x m_y w C_w)$$

$$= \frac{\partial}{\partial z} \left( m_x m_y \frac{A_b}{H} \frac{\partial}{\partial z} (C_w) \right) + mH \left( \sum_i \left( K_{dS}^j C_S^i \right) + \sum_j \left( K_{dD}^j C_D^i \right) \right)$$

$$- mH \left( \sum_i \left( K_{dS}^i S^i \right) (\psi_w \frac{C_w}{\emptyset}) (\widehat{\chi}_S^i - \chi_S^i) \right)$$

$$+ \sum_j \left( K_{dD}^j D^j \right) (\psi_w \frac{C_w}{\emptyset}) (\widehat{\chi}_D^j - \chi_D^j) + \gamma C_w \right) (7.14)$$

<span id="page-127-2"></span><span id="page-127-1"></span>
$$\frac{\partial}{\partial t} \left( mHC_D^j \right) + \frac{\partial}{\partial x} \left( m_y H u C_D^j \right) + \frac{\partial}{\partial y} \left( m_x H v C_D^j \right) + \frac{\partial}{\partial z} \left( m_w C_D^j \right) 
= \frac{\partial}{\partial z} \left[ m \frac{A_b}{H} \frac{\partial}{\partial z} (C_D^j) \right] + mH \left( K_{sD}^j D^j \right) \left( \psi_w \frac{C_w}{\phi} \right) \left( \widehat{\chi}_D^j - \chi_D^j \right) 
- mH \left( K_{dD}^j + \gamma \right) C_D^j \quad (7.15)$$

<span id="page-127-3"></span>
$$\frac{\partial}{\partial t} \left( mHC_S^i \right) + \frac{\partial}{\partial x} \left( m_y HuC_S^i \right) + \frac{\partial}{\partial y} \left( m_x HvC_S^i \right) + \frac{\partial}{\partial z} \left( mwC_S^i \right) + \frac{\partial}{\partial z} \left( mw_S^i C_S^i \right) 
= \frac{\partial}{\partial z} \left( m\frac{A_b}{H} \frac{\partial}{\partial z} C_S^i \right) + mH \left( K_{aS}^i S^i \right) \left( \psi_w \frac{C_w}{\phi} \right) \left( \widehat{\chi}_S^i - \chi_S^i \right) 
- mH \left( K_{dS}^i + \gamma \right) C_S^i \quad (7.16)$$

Where, equation (7.14) is for the dissolved fraction, equation (7.15) is for the fraction sorbed to the dissolved material and equation (7.16) is for the fraction sorbed to the sediments.

{128}------------------------------------------------

Adding equations (7.14), (7.15), and (7.16), using the equilibrium partitioning relationship equations (7.6) and (7.7) gives

<span id="page-128-1"></span>
$$\frac{\partial}{\partial t}(mHC) + \frac{1}{m}\frac{\partial}{\partial x}(m_yHuC) + \frac{1}{m}\frac{\partial}{\partial y}(m_xvC) 
+ \frac{\partial}{\partial z}(m_xm_ywC) - \frac{\partial}{\partial z}\left(m\sum_i w_S^i f_S^i C\right) 
= \frac{\partial}{\partial z}\left(m\frac{A_b}{\partial z}\frac{\partial C}{\partial z}\right) - mH\gamma C \quad (7.17)$$

the equation for the total concentration C. The boundary condition at the water column-sediment bed interface, z = 0 is

$$-\frac{A_{b}}{H}\frac{\partial C}{\partial z} - \sum_{i} w_{S}^{i} f_{S}^{i} C$$

$$= \sum_{i} \left( \left( \max \left( J_{SBS}^{i} \chi_{S}^{i}, 0 \right) + \varepsilon \max \left( \frac{J_{SBS}^{i}}{\rho_{S}^{i}}, 0 \right) \right) \left( \frac{C_{w} + \sum_{j} C_{D}^{j}}{\phi} \right) \right)_{SB}$$

$$+ \sum_{i} \left( \left( \min \left( J_{SBS}^{i} \chi_{S}^{i}, 0 \right) + \varepsilon_{dep} \min \left( \frac{J_{SBS}^{i}}{\rho_{S}^{i}}, 0 \right) \right) \left( \frac{C_{w} + \sum_{j} C_{D}^{j}}{\phi_{dep}} \right) \right)_{WC}$$

$$+ \sum_{i} \left( \left( \varepsilon \max \left( \frac{J_{SBB}^{i}}{\rho_{S}^{i}}, 0 \right) \right) \left( \frac{C_{w} + \sum_{j} C_{D}^{j}}{\phi} \right) \right)_{SB}$$

$$+ \sum_{i} \left( \left( \varepsilon_{dep} \min \left( \frac{J_{SBB}^{i}}{\rho_{S}^{i}}, 0 \right) \right) \left( \frac{C_{w} + \sum_{j} C_{D}^{j}}{\phi_{dep}} \right) \right)_{WC}$$

$$+ \left( \max \left( q_{w}, 0 \right) \left( \frac{C_{w} + \sum_{j} C_{D}^{j}}{\phi} \right) \right)_{SB} + \left( \min \left( q_{w}, 0 \right) \left( \frac{C_{w} + \sum_{j} C_{D}^{j}}{\phi_{dep}} \right) \right)_{WC}$$

$$- q_{dif} \left( \left( \frac{C_{w} + \sum_{j} C_{D}^{j}}{\phi_{dep}} \right)_{WC} - \left( \frac{C_{w} + \sum_{j} C_{D}^{j}}{\phi} \right)_{SB} \right)$$
 (7.18)

where,

<span id="page-128-0"></span> $J_{SBS}$  and  $J_{SBB}$  are the suspended load and bedload sediment fluxes between the sediment bed and the water column, defined as positive from the bed,

 $\rho_s$  is the sediment density in  $g/m^3$ ,

 $q_w$  is the water specific discharge due to bed consolidation and groundwater interaction, defined as positive from the bed in  $m^3/s$ , and

 $q_{dif}$  is a diffusion velocity incorporating the effects of molecular diffusion, hydrodynamic dispersion, and biological induced mixing in m/s.

The subscript SB denotes conditions in the top layer of the sediment bed, while the subscript WC denotes condition in the water column immediately above the bed, with the exception that the specific discharge and

{129}------------------------------------------------

diffusion velocity are defined at the water column-bed interface. The subscript *dep* is used to denote the void ratio and porosity of newly deposited sediment. Equation (7.13) indicates that the contaminant flux between the bed and water column includes a flux of suspended sediment sorbed material; fluxes of water dissolved and sorbed to water dissolved material due to the specific discharge of water associated with consolidation and ground water interaction and water entrainment and expulsion associated with both suspended and bedload sediment deposition and resuspension; and a flux of water dissolved and sorbed to water dissolved material due to diffusion like processes. Transport of bedload sediment sorbed material is represented by direct transport between horizontally adjacent top bed layers and is included in the contaminant mass conservation equations for the sediment bed. The boundary condition at the water free surface is

$$-\frac{A_b}{H}\frac{\partial C}{\partial z} - \sum_i w_S^i f_S^i C = 0 : z = 1$$

$$(7.19)$$

Using the relationship between the porosity and void ratio

$$\phi = \frac{\varepsilon}{1 + \varepsilon} \tag{7.20}$$

and equation (7.5) allows equation (7.18) to be written as

$$-\frac{A_{b}}{H}\frac{\partial C}{\partial z} - \sum_{i} w_{S}^{i} f_{S}^{i} C$$

$$= \sum_{i} \left( \left( \max \left( J_{SBS}^{i} \frac{C_{S}^{i}}{S^{i}}, 0 \right) + (1 + \varepsilon) \max \left( \frac{J_{SB}^{i}}{\rho_{S}^{i}}, 0 \right) \right) \left( C_{w} + \sum_{j} C_{D}^{j} \right) \right)_{SB}$$

$$+ \sum_{i} \left( \left( \min \left( J_{SBS}^{i} \frac{C_{S}^{i}}{S^{i}}, 0 \right) + (1 + \varepsilon_{dep}) \min \left( \frac{J_{SBS}^{i}}{\rho_{S}^{i}}, 0 \right) \right) \left( C_{w} + \sum_{j} C_{D}^{j} \right) \right)_{WC}$$

$$+ \sum_{i} \left( \left( (1 + \varepsilon) \max \left( \frac{J_{SBB}^{i}}{\rho_{S}^{i}}, 0 \right) \right) \left( C_{w} + \sum_{j} C_{D}^{j} \right) \right)_{SB}$$

$$+ \sum_{i} \left( \left( (1 + \varepsilon_{dep}) \min \left( \frac{J_{SBB}^{i}}{\rho_{S}^{i}}, 0 \right) \right) \left( C_{w} + \sum_{j} C_{D}^{j} \right) \right)_{WC}$$

$$+ \left( \left( \max (q_{w}, 0) + q_{dif} \right) \frac{1}{\phi} \left( C_{w} + \sum_{j} C_{D}^{j} \right) \right)_{SB}$$

$$+ \left( \left( \min (q_{w}, 0) - q_{dif} \right) \frac{1}{\phi} \left( C_{w} + \sum_{j} C_{D}^{j} \right) \right)_{WC}$$

$$(7.21)$$

The sediment concentration can be expressed in terms of the sediment density and void ratio by

<span id="page-129-1"></span><span id="page-129-0"></span>
$$S^{i} = \frac{F^{i} \rho_{s}^{i}}{1 + \varepsilon} \tag{7.22}$$

where,  $F^{i}$  is the fraction of the total sediment volume occupied by each sediment class.

<span id="page-129-2"></span>
$$F^{i} = \left(\sum_{i} \left(\frac{S^{i}}{\rho_{s}^{i}}\right)\right)^{-1} \left(\frac{S^{i}}{\rho_{s}^{i}}\right) \tag{7.23}$$

{130}------------------------------------------------

Introducing equations (7.11) and (7.22) into equation (7.21) gives the final form of the bottom boundary

$$-\frac{A_{b}}{H}\frac{\partial C}{\partial z} - \sum_{i} w_{S}^{i} f_{S}^{i} C$$

$$= \sum_{i} \left( \max \left( \frac{J_{SBS}^{i} f_{S}^{i}}{S^{i}}, 0 \right) C + \max \left( \frac{F^{i} J_{SBS}^{i}}{S^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) C \right)_{SB}$$

$$+ \sum_{i} \left( \min \left( \frac{J_{SBS}^{i} f_{S}^{i}}{S^{i}}, 0 \right) C + \min \left( \frac{F_{dep}^{i} J_{SBS}^{i}}{S_{dep}^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) C \right)_{WC}$$

$$+ \sum_{i} \left( \left( (1 + \varepsilon) \max \left( \frac{J_{SBB}^{i}}{\rho_{S}^{i}}, 0 \right) \right) \left( C_{w} + \sum_{j} C_{D}^{j} \right) \right)_{SB}$$

$$+ \sum_{i} \left( \left( (1 + \varepsilon_{dep}) \min \left( \frac{J_{SBB}^{i}}{\rho_{S}^{i}}, 0 \right) \right) \left( C_{w} + \sum_{j} C_{D}^{j} \right) \right)_{WC}$$

$$+ \left( \left( \max (q_{w}, 0) + q_{dif} \right) \frac{1}{\phi} \left( f_{w} + \sum_{j} f_{D}^{j} \right) C \right)_{SB}$$

$$+ \left( \left( \min (q_{w}, 0) - q_{dif} \right) \frac{1}{\phi} \left( f_{w} + \sum_{j} f_{D}^{j} \right) C \right)_{WC}$$

$$(7.24)$$

Note that the form of the bed flux associated with bedload transport remains unmodified since the sediment concentration in the water column cannot be readily defined for sediment being transported as bedload.

#### <span id="page-130-0"></span>7.4.1 Numerical Solution to the Water Column Chemical Transport Equations

The transport equation (7.17) for the total contaminant concentration in the water column is solved using a fractional step procedure:

- 1. advection;
- 2. settling, deposition, and resuspension;
- 3. pore water advection and diffusion; and
- 4. reactions.

The fractional phase distribution of the contaminant is recalculated between each steps above using equation (7.11).

#### **7.4.1.1** Advection

The advection step is

<span id="page-130-1"></span>
$$(HC)^{n+1/4} - (HC)^n + \frac{\Delta t}{m} \frac{\partial}{\partial x} (m_y H u C) + \frac{\Delta t}{m} \frac{\partial}{\partial y} (m_x H v C) + \Delta t \frac{\partial (w C)}{\partial z} = 0$$
 (7.25)

{131}------------------------------------------------

with the vertical boundary conditions

$$wC = 0 : z = 0, 1 (7.26)$$

The fractional time level in equation (7.25) and subsequent equations is used to denote an intermediate result in the fractional step procedure. The spatially discrete form of equation (7.25) is solved using one of the standard high order, flux limited, advective transport solvers in EFDC+.

#### 7.4.1.2 Settling, Deposition, and Resuspension

The settling, deposition, and resuspension step is

<span id="page-131-0"></span>
$$(H)^{n+1/2} - (HC)^{n+1/4} = \Delta t \frac{\partial}{\partial z} \left( \sum_{i} w_S^i f_S^i C \right)$$
(7.27)

with the boundary conditions

$$-\sum_{i} w_{S}^{i} f_{S}^{i} C = \sum_{i} \left( \max \left( \frac{J_{SBS}^{i} f_{S}^{i}}{S^{i}}, 0 \right) C + \max \left( \frac{F^{i} J_{SBS}^{i}}{S^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) C \right)_{SB}$$

$$+ \sum_{i} \left( \min \left( \frac{J_{SBS}^{i} f_{S}^{i}}{S^{i}}, 0 \right) C + \min \left( \frac{F_{dep}^{i} J_{SBS}^{i}}{S_{dep}^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) C \right)_{WC}$$

$$+ \sum_{i} \left( \left( (1 + \varepsilon) \max \left( \frac{J_{SBB}^{i}}{\rho_{S}^{i}}, 0 \right) \right) \left( C_{w} + \sum_{j} C_{D}^{j} \right) \right)_{SB}$$

$$= \sum_{i} \left( \left( (1 + \varepsilon_{dep}) \min \left( \frac{J_{SBB}^{i}}{\rho_{S}^{i}}, 0 \right) \right) \left( C_{w} + \sum_{j} C_{D}^{j} \right) \right)_{WC} : z = 0 \quad (7.28)$$

<span id="page-131-1"></span>
$$w_S^i f_S^i C = 0 : z = 1 (7.29)$$

Integrating equation (7.27) over a water column layer and using upwind differencing for the settling gives,

$$\Delta_{k}(HC)_{k}^{n+\frac{1}{2}} - \Delta_{k}(HC)_{k}^{n+\frac{1}{4}} = \Delta t \sum_{i} \left( \frac{\left( w_{S}^{i} S^{i} \right)_{k+}}{H} \left( \frac{f_{S}^{i}}{S^{i}} \right)_{k+1} \right)^{n+\frac{1}{2}} (HC)_{k+1}^{n+\frac{1}{2}}$$

$$-\Delta t \sum_{i} \left( \frac{\left( w_{S}^{i} S^{i} \right)_{k-}}{H} \left( \frac{f_{S}^{i}}{S^{i}} \right)_{k} \right)^{n+\frac{1}{2}} (HC)_{k}^{n+\frac{1}{2}}$$
 (7.30)

for a layer not adjacent to the bed (i.e., k > 1), and,

{132}------------------------------------------------

$$\Delta_{1}(HC)_{1}^{n+\frac{1}{2}} - \Delta_{1}(HC)_{1}^{n+\frac{1}{4}}$$

$$= \Delta t \sum_{i} \left( \left( w_{S}^{i} S^{i} \right)_{1+} \left( \frac{f_{S}^{i}}{S^{i}} \right)_{2} \right)^{n+\frac{1}{2}} C_{2}^{n+\frac{1}{2}}$$

$$+ \Delta t \sum_{i} \left( \max \left( \frac{J_{SBS}^{i} f_{S}^{i}}{S^{i}}, 0 \right) + \max \left( \frac{J_{SBS}^{i} F^{i}}{S^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) \right)_{sb}^{n+\frac{1}{2}} C_{sb}^{n+\frac{1}{2}}$$

$$+ \Delta t \sum_{i} \left( \min \left( \frac{J_{SBS}^{i} f_{S}^{i}}{S^{i}}, 0 \right) + \min \left( \frac{J_{SBS}^{i} F^{i}}{S^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) \right)_{1}^{n+\frac{1}{2}} C_{1}^{n+\frac{1}{2}}$$

$$+ \Delta t \sum_{i} \left( (1 + \varepsilon) \max \left( \frac{J_{SBB}^{i}}{\rho_{S}^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) \right)_{sb}^{n+\frac{1}{2}} C_{sb}^{n+\frac{1}{2}}$$

$$+ \Delta t \sum_{i} \left( (1 + \varepsilon) \min \left( \frac{J_{SBB}^{i}}{\rho_{S}^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) \right)_{1}^{n+\frac{1}{2}} C_{1}^{n+\frac{1}{2}}$$

$$+ \Delta t \sum_{i} \left( (1 + \varepsilon) \min \left( \frac{J_{SBB}^{i}}{\rho_{S}^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) \right)_{1}^{n+\frac{1}{2}} C_{1}^{n+\frac{1}{2}}$$

$$(7.31)$$

for the first layer adjacent to the bed (i.e, k = 1). Note that equation (7.31) is also the appropriate form for single layer or depth average application. Since the sediment settling flux is zero at the top of the free surface adjacent layer, equation (7.27) is integrated downward from the top layer to the bottom layer. The bottom layer equation (7.31) is solved simultaneously with a corresponding equation for the top layer of the sediment bed. The settling fluxes,  $w_S S$  and water column-sediment bed fluxes,  $J_{SB(S/B)}$  in equations (7.30) and (7.31) are known from the preceding solution for sediment settling, deposition and resuspension. Terms containing the sediment sorbed fraction divided by the sediment concentration in equations (7.30) and (7.31)

<span id="page-132-0"></span>
$$\frac{f_S^i}{S^i} = \frac{P_S^i}{\phi + \sum_i P_S^i S^i + \sum_j P_D^j D^j}$$
 (7.32)

#### 7.4.1.3 Porewater Advection and Diffusion

The diffusion step is given by

$$(HC)^{n+\frac{3}{4}} - (HC)^{n+\frac{1}{2}} = \Delta t \frac{\partial}{\partial z} \left( \frac{A_b}{H} \frac{\partial}{\partial z} C \right)$$
 (7.33)

with boundary conditions

$$-\frac{A_{b}}{H}\frac{\partial C}{\partial z} = \left(\left(\max\left(q_{w},0\right) + q_{dif}\right)\frac{1}{\phi}\left(f_{w} + \sum_{j} f_{D}^{j}\right)C\right)_{SB} + \left(\left(\min\left(q_{w},0\right) - q_{dif}\right)\frac{1}{\phi_{dep}}\left(f_{w} + \sum_{j} f_{D}^{j}\right)C\right)_{WC} : z = 0 \quad (7.34)$$

{133}------------------------------------------------

<span id="page-133-1"></span>
$$-\frac{A_b}{H}\frac{\partial C}{\partial z} = 0 : z = 1 \tag{7.35}$$

For the first layer adjacent to the bed

$$(HC)_{1}^{n+3/4} - (HC)_{1}^{n+1/2} = \frac{\Delta t}{\Delta_{1}} \left( \frac{A_{b}}{H} \frac{\partial C}{\partial z} \right)_{1+}^{n+\frac{3}{4}} + \frac{\Delta t}{\Delta_{1}} \left( \max \left( q_{w}, 0 \right) + q_{dif} \right) \left( \left( f_{w} + \sum_{j} f_{D}^{j} \right) \frac{1}{\phi} \right)_{SB}^{n+\frac{1}{2}} C_{SB}^{n+\frac{3}{4}} + \frac{\Delta t}{\Delta_{1}} \left( \min \left( q_{w}, 0 \right) - q_{dif} \right) \left( \left( f_{w} + \sum_{j} f_{D}^{j} \right) \frac{1}{\phi_{dep}} \right)_{1}^{n+\frac{1}{2}} C_{1}^{n+\frac{1}{2}}$$
 (7.36)

It is noted that the bed concentrations are advanced to the n + 3/4 intermediate time level before the advance of the water column concentrations. While for layers not adjacent to the bed,

$$(HC)_{k}^{n+\frac{3}{4}} - (HC)_{k}^{n+\frac{1}{2}} = \frac{\Delta t}{\Delta_{1}} \left( \frac{A_{b}}{H} \frac{\partial C}{\partial z} \right)_{k+}^{n+\frac{3}{4}} - \frac{\Delta t}{\Delta_{1}} \left( \frac{A_{b}}{H} \frac{\partial C}{\partial z} \right)_{k-}^{n+\frac{3}{4}}$$
(7.37)

#### **7.4.1.4 Reactions**

The solution is completed by

$$(HC)_{k}^{n+1} - (H)_{k}^{n+3/4} = -\Delta t \gamma (HC)_{k}^{n+1}$$
(7.38)

an implicit reaction step.

#### <span id="page-133-0"></span>7.5. Sediment Bed Chemical Processes

Chemical transport in the sediment bed is represented using the discrete layer formulation developed for bed geomechanical processes. The conservation of mass for the total chemical concentration in a layer of the sediment bed is given by

{134}------------------------------------------------

$$\begin{split} \frac{\partial}{\partial t}(BC)_{k} &= -\gamma (BC)_{k} \\ &- \delta\left(k,kt\right) \sum_{i} \left( \max\left(\frac{J_{SBS}^{i} f_{S}^{i}}{BS^{i}},0\right) + \max\left(\frac{J_{SBS}^{i} F^{i}}{BS^{i}},0\right) \left(f_{w} + \sum_{j} f_{D}^{j}\right) \right)_{kl} (BC)_{kl} \\ &- \delta\left(k,kt\right) \sum_{i} \left( \min\left(\frac{J_{SBS}^{i} f_{S}^{i}}{S^{i}},0\right) C + \min\left(\frac{J_{SBS}^{i} F_{dep}^{i}}{S_{dep}^{i}},0\right) \left(f_{w} + \sum_{j} f_{D}^{j}\right) C \right)_{WC} \\ &- \delta\left(k,kt\right) \sum_{i} \left( \min(J_{SBB}^{i} \chi_{SBL}^{i},0) - \delta\left(k,kt\right) \sum_{i} \left( (1+\varepsilon) \max\left(\frac{J_{SBS}^{i} F_{dep}^{i}}{Bp_{S}^{i}},0\right) \left(f_{w} + \sum_{j} f_{D}^{j}\right) C \right)_{kl} (BC)_{kl} \\ &- \delta\left(k,kt\right) \sum_{i} \left( (1+\varepsilon_{dep}) \min\left(\frac{J_{SBB}^{i}}{p_{S}^{i}},0\right) \left(f_{w} + \sum_{j} f_{D}^{j}\right) C \right)_{WC} \\ &- \left( \left( \max\left(q_{w},0\right) + q_{dif}\right)_{k+} - \left(\min\left(q_{w},0\right) - q_{dif}\right)_{k-} \right) \left(\frac{1}{\phi B} \left(f_{w} + \sum_{j} f_{D}^{j}\right) C \right)_{WC} \\ &- \delta\left(k,kt\right) \left(\min\left(q_{w},0\right) - q_{dif}\right)_{k+} \left(\frac{1}{\phi} \left(f_{w} + \sum_{j} f_{D}^{j}\right) C \right)_{WC} \\ &- \left(1 - \delta\left(k,kt\right)\right) \left(\min\left(q_{w},0\right) - q_{dif}\right)_{k+} \left(\frac{1}{\phi B} \left(f_{w} + \sum_{j} f_{D}^{j}\right) \right)_{k+1} (BC)_{k+1} \\ &+ \left(\max\left(q_{w},0\right) + q_{dif}\right)_{k-} \left(\frac{1}{\phi B} \left(f_{w} + \sum_{j} f_{D}^{j}\right) \right)_{k-1} (BC)_{k-1} \end{aligned}$$

where,

<span id="page-134-0"></span>
$$\delta(k,kt) = \begin{cases} 1 : k = kt \\ 0 : k \neq kt \end{cases}$$
 (7.40)

is used to distinguish processes specific to the top, water column adjacent layer of the bed, kt. Advective fluxes associated with pore water advection in equation (7.39) are represented in upwind form. In the sediment bed, the actual computational variables for sediment, contaminant, and dissolved material are their concentrations times the thickness of the bed layer. Consistent with this formulation, the fractional phase components in the bed are defined by

<span id="page-134-1"></span>
$$(f_w)_k = \left(\frac{BC_w}{BC}\right)_k = \left(\frac{B\phi}{B\phi + \sum_i P_S^i BS^i + \sum_j P_D^j BD^j}\right)_k$$

$$\left(f_D^j\right)_k = \left(\frac{BC_D^j}{BC}\right)_k = \left(\frac{P_D^j BD^j}{B\phi + \sum_i P_S^i BS^i + \sum_j P_D^j BD^j}\right)_k$$

$$(f_S^i)_k = \left(\frac{BC_S^i}{BC}\right)_k = \left(\frac{P_S^i BS^i}{B\phi + \sum_i P_S^i BS^i + \sum_j P_D^j BD^j}\right)_k$$

$$(7.41)$$

{135}------------------------------------------------

## <span id="page-135-0"></span>7.5.1 Bedload Transport

The contaminant fluxes associated bedload sediment transport are determined as follows.

<span id="page-135-2"></span>
$$mJ_{SBB}^{i} = \frac{\partial}{\partial x} \left( m_{y} Q_{SBLx}^{i} \right) + \frac{\partial}{\partial x} \left( m_{x} Q_{SBLy}^{i} \right)$$
 (7.42)

Equation [\(7.42\)](#page-135-2) is used to evaluate the flux associated with pore water entrainment and expulsion in equations [\(7.25\)](#page-130-1) and [\(7.39\)](#page-134-0). The transport equation for material sorbed to the bedload is

<span id="page-135-3"></span>
$$\frac{\partial}{\partial x} \left( m_y Q_{SBLx}^i \chi_{SBL}^i \right) + \frac{\partial}{\partial x} \left( m_x Q_{SBLy}^i \chi_{SBL}^i \right) = m J_{SBB}^i \chi_{SBL}^i$$
 (7.43)

Since the contaminant mass per sediment mass in the transport divergence corresponds to conditions in the top layer of the sediment bed, equation [\(7.43\)](#page-135-3) can be written as

$$\frac{\partial}{\partial x} \left( m_y Q_{SBLx}^i \frac{f_S^i}{S^i} C \right) + \frac{\partial}{\partial x} \left( m_x Q_{SBLy}^i \frac{f_S^i}{S^i} C \right) = m J_{SBB}^i \chi_{SBL}^i$$
 (7.44)

and solved using an upwind approximation

$$mJ_{SB}^{i}\chi_{SBL}^{i} = \max\left(m_{y}Q_{SBLx}^{i}\right)_{E} \left(\frac{f_{S}^{i}}{S^{i}}C\right)_{C} + \min\left(m_{y}Q_{SBLx}^{i}\right)_{E} \left(\frac{f_{S}^{i}}{S^{i}}C\right)_{E}$$

$$- \max\left(m_{y}Q_{SBLx}^{i}\right)_{W} \left(\frac{f_{S}^{i}}{S^{i}}C\right)_{W} - \min\left(m_{y}Q_{SBLx}^{i}\right)_{W} \left(\frac{f_{S}^{i}}{S^{i}}C\right)_{C}$$

$$+ \max\left(m_{x}Q_{SBLy}^{i}\right)_{N} \left(\frac{f_{S}^{i}}{S^{i}}\right)_{C} + \min\left(m_{x}Q_{SBy}^{i}\right)_{N} \left(\frac{f_{S}^{i}}{S^{i}}C\right)_{N}$$

$$- \max\left(m_{x}Q_{SBLy}^{i}\right)_{S} \left(\frac{f_{S}^{i}}{S^{i}}C\right)_{S} - \min\left(m_{x}Q_{SBLy}^{i}\right)_{S} \left(\frac{f_{S}^{i}}{S^{i}}C\right)_{C}$$

$$(7.45)$$

to evaluate the transport of bedload sorbed material between horizontally adjacent top layers of the sediment bed.

#### <span id="page-135-1"></span>7.5.2 Numerical Solution to the Bed Chemical Process Equations

Equation [\(7.39\)](#page-134-0) is solved using a fractional step procedure consistent with that used for the water column transport. Equation [\(7.41\)](#page-134-1) is used to update the fractional distribution in the bed between the settling, deposition, and resuspension step and the pore water advection and diffusion step.

#### 7.5.2.1 Settling, Deposition, and Resuspension

The settling, deposition, and resuspension step applies only to the top layer of the bed and is

{136}------------------------------------------------

$$(BC)_{kt}^{n+\frac{1}{2}} - (BC)_{kt}^{n}$$

$$= -\Delta t \sum_{i} \left( \max \left( \frac{J_{SBS}^{i} f_{S}^{i}}{BS^{i}}, 0 \right) + \max \left( \frac{J_{SBS}^{i} F^{i}}{BS^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) \right)_{kt}^{n+\frac{1}{2}} (BC)_{kt}^{n+\frac{1}{2}}$$

$$-\Delta t \sum_{i} \left( \min \left( \frac{J_{SBS}^{i} f_{S}^{i}}{S^{i}}, 0 \right) C + \min \left( \frac{J_{SBS}^{i} F_{dep}^{i}}{S_{dep}^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) C \right)_{WC}^{n+\frac{1}{2}}$$

$$-\Delta t \sum_{i} \left( J_{SBB}^{i} \chi_{SBL}^{i}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) \right)_{kt}^{n+\frac{1}{2}} (BC)_{kt}^{n+\frac{1}{2}}$$

$$-\Delta t \sum_{i} \left( (1 + \varepsilon_{dep}) \min \left( \frac{J_{SBB}^{i}}{\rho_{S}^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) C \right)_{WC}^{n+\frac{1}{2}}$$

$$(7.46)$$

This equation is solved simultaneously with equation (7.31) for the bottom layer of the water column. The solution is represented by

<span id="page-136-0"></span>
$$\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
\begin{cases}
(BC)_{kt}^{n+\frac{1}{2}} \\
(HC)_{1}^{n+\frac{1}{2}}
\end{cases}
\begin{cases}
(BC)_{kt}^{n} - \Delta t \sum_{i} \left(J_{S}^{i} \chi_{SBL}^{i}\right)^{n+\frac{1}{2}} \\\ni=ib \\
\Delta_{1}C_{1}^{n+\frac{1}{4}} + \Delta t \sum_{i} \left(\left(w_{S}^{i} S^{i}\right)_{1+} \left(\frac{f_{S}^{i}}{S^{i}}\right)_{2}\right)^{n+\frac{1}{2}} C_{2}^{n+\frac{1}{2}}
\end{cases}$$
(7.47)

where the coefficients are given by

$$a_{11} = 1 + \Delta t \sum_{i} \left( \max \left( \frac{J_{SBS}^{i} f_{S}^{i}}{BS^{i}}, 0 \right) + \max \left( \frac{J_{SBS}^{i} F^{i}}{BS^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) \right)_{kt}^{n+\frac{1}{2}} + \Delta t \sum_{i} \left( (1 + \varepsilon) \max \left( \frac{J_{SBB}^{i}}{B\rho_{S}^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) \right)_{kt}^{n+\frac{1}{2}}$$
(7.48)

$$a_{12} = \frac{\Delta t}{H} \sum_{i} \left( \min \left( \frac{J_{SBS}^{i} f_{S}^{i}}{S^{i}}, 0 \right) + \min \left( \frac{J_{SBS}^{i} F_{dep}^{i}}{S_{dep}^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) \right)_{1}^{n + \frac{1}{2}} + \frac{\Delta t}{H} \sum_{i} \left( \left( 1 + \varepsilon_{dep} \right) \min \left( \frac{J_{SBB}^{i}}{\rho_{S}^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) \right)_{1}^{n + \frac{1}{2}}$$
(7.49)

{137}------------------------------------------------

$$a_{21} = -\Delta t \sum_{i} \left( \max \left( \frac{J_{SBS}^{i} f_{S}^{i}}{BS^{i}}, 0 \right) + \max \left( \frac{J_{SBS}^{i} F^{i}}{BS^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) \right)_{kt}^{n + \frac{1}{2}}$$

$$-\Delta t \sum_{i} \left( (1 + \varepsilon) \max \left( \frac{J_{SBB}^{i}}{B\rho_{S}^{i}}, 0 \right) \left( f_{w} + \sum_{j} f_{D}^{j} \right) \right)_{kt}^{n + \frac{1}{2}}$$

$$(7.50)$$

$$a_{22} = \Delta_1 - \frac{\Delta t}{H} \sum_{i} \left( \min \left( \frac{J_{SBS}^i f_S^i}{S^i}, 0 \right) + \min \left( \frac{J_{SBS}^i F^i}{S^i}, 0 \right) \left( f_w + \sum_{j} f_D^j \right) \right)_1^{n + \frac{1}{2}} - \frac{\Delta t}{H} \sum_{i} \left( (1 + \varepsilon) \min \left( \frac{J_{SBB}^i}{\rho_S^i}, 0 \right) \left( f_w + \sum_{j} f_D^j \right) \right)_1^{n + \frac{1}{2}}$$
(7.51)

Adding the two equations in (7.46) gives

<span id="page-137-0"></span>
$$(BC)_{kt}^{n+\frac{1}{2}} + \Delta_{1}(HC)_{1}^{n+\frac{1}{2}} =$$

$$(BC)_{kt}^{n} + \Delta_{1}(HC)_{1}^{n+\frac{1}{4}} + \Delta t \sum_{i} \left( \left( w_{S}^{i} S^{i} \right)_{1} + \left( \frac{f_{S}^{i}}{S^{i}} \right)_{2} \right)^{n+\frac{1}{2}} C_{2}^{n+\frac{1}{2}}$$

$$-\Delta t \sum_{i} \left( J_{S}^{i} \chi_{SBL}^{i} \right)^{n+\frac{1}{2}}$$
 (7.52)

This equation verifies the consistency of the water column-sediment bed exchange since the source and sinks on the right side include only settling into the top of the water column layer, and transfer of bedload sediment sorbed contaminant between horizontal sediment bed cells.

#### 7.5.2.2 Porewater Advection and Diffusion

The pore water advection and diffusion step for the top, water column adjacent, layer is

$$(BC)_{kt}^{n+3/4} = (BC)_{kt}^{n+1/2}$$

$$-\Delta t \left( \max(q_w, 0) + q_{dif} \right)_{kt} + \left( \frac{1}{\phi B} \left( f_w + \sum_j f_D^j \right) \right)_{kt}^{n+1/2} (BC)_{kt}^{n+3/4}$$

$$+ \Delta t \left( \min(q_w, 0) - q_{dif} \right)_{kt} - \left( \frac{1}{\phi B} \left( f_w + \sum_j f_D^j \right) \right)_{kt}^{n+1/2} (BC)_{kt}^{n+3/4}$$

$$-\Delta t \left( \min(q_w, 0) - q_{dif} \right)_{kt} + \left( \frac{1}{\phi H} \left( f_w + \sum_j f_D^j \right) \right)_{1}^{n+1/2} (HC)_{1}^{n+1/2}$$

$$+ \Delta t \left( \max(q_w, 0) + q_{dif} \right)_{kt} - \left( \frac{1}{\phi B} \left( f_w + \sum_j f_D^j \right) \right)_{kt-1}^{n+1/2} (BC)_{kt-1}^{n+1/2}$$

$$(7.53)$$

{138}------------------------------------------------

which is an implicit form. Writing equation [\(7.36\)](#page-133-1) in the form

$$\Delta_{1}(HC)_{1}^{n+3/4} = \Delta_{1}(HC)_{1}^{n+1/2} + \Delta t \left(\frac{A_{b}}{H} \frac{\partial C}{\partial z}\right)_{1+}^{n+3/4}$$

$$+ \Delta t \left(\max(q_{w}, 0) + q_{dif}\right)_{kt+} \left(\frac{1}{\phi B} \left(f_{w} + \sum_{j} f_{D}^{j}\right)\right)_{SB}^{n+1/2} (BC)_{kt}^{n+3/4}$$

$$+ \Delta t \left(\min(q_{w}, 0) - q_{dif}\right)_{kt+} \left(\frac{1}{\phi H} \left(f_{w} + \sum_{j} f_{D}^{j}\right)\right)_{1}^{n+1/2} (HC)_{1}^{n+1/2}$$
 (7.54)

and combining with equation [\(7.52\)](#page-137-0) gives

<span id="page-138-0"></span>
$$(BC)_{kt}^{n+3/4} + \Delta_{1} (HC)_{1}^{n+3/4}$$

$$= (BC)_{kt}^{n+1/2} + \Delta_{1} (HC)_{1}^{n+1/2} + \Delta_{t} \left(\frac{A_{b}}{H} \partial_{z} C\right)_{1+}^{n+3/4}$$

$$+ \Delta_{t} \left(\min(q_{w}, 0) - q_{dif}\right)_{kt-} \left(\frac{1}{\phi B} \left(f_{w} + \sum_{j} f_{D}^{j}\right)\right)_{kt}^{n+1/2} (BC)_{kt}^{n+3/4}$$

$$+ \Delta_{t} \left(\max(q_{w}, 0) + q_{dif}\right)_{kt-} \left(\frac{1}{\phi B} \left(f_{w} + \sum_{j} f_{D}^{j}\right)\right)_{kt-1}^{n+1/2} (BC)_{kt-1}^{n+3/4}$$

$$(7.55)$$

This equation verifies the consistency of the representation of pore water advection and diffusion across water column-sediment bed interface since the source and sink terms on the right side of equation [\(7.55\)](#page-138-0) represent fluxes at the top to the water column cell and the bottom of the bed cell.

The pore water diffusion and advection step for the remaining bed layers is given by

$$(BC)_{k}^{n+3/4} = (BC)_{k}^{n+1/2}$$

$$-\Delta t \left(\min(q_{w}, 0) - q_{dif}\right)_{k+} \left(\frac{1}{\phi B} \left(f_{w} + \sum_{j} f_{D}^{j}\right)\right)_{k+1}^{n+1/2} (BC)_{k+1}^{n+3/4}$$

$$-\Delta t \left(\max(q_{w}, 0) + q_{dif}\right)_{k+} \left(\frac{1}{\phi B} \left(f_{w} + \sum_{j} f_{D}^{j}\right)\right)_{k}^{n+1/2} (BC)_{k}^{n+3/4}$$

$$+\Delta t \left(\min(q_{w}, 0) - q_{dif}\right)_{k-} \left(\frac{1}{\phi B} \left(f_{w} + \sum_{j} f_{D}^{j}\right)\right)_{k}^{n+1/2} (BC)_{k}^{n+3/4}$$

$$+\Delta t \left(\max(q_{w}, 0) + q_{dif}\right)_{k-} \left(\frac{1}{\phi B} \left(f_{w} + \sum_{j} f_{D}^{j}\right)\right)_{k-1}^{n+1/2} (BC)_{k-1}^{n+3/4} (7.56)$$

For the bottom-most layer (*k* = 1) layer-bottom boundary (denoted by *k*−), the specific discharge and diffusion velocity must be specified along with the total contaminant concentration, *C*0. The corresponding 

{139}------------------------------------------------

thickness of the unresolved layer *k* = 0, is set to unity without loss of generality. The system of equations represented by equations [\(7.52\)](#page-137-0) and [\(7.55\)](#page-138-0) is implicit and is solved using a tri-diagonal linear equation solver. It is noted that the *n*+3/4 time level layer thickness is actually the *n*+1 time level thickness determined by the solution of equation [\(7.23\)](#page-129-2). The specific discharges in equations [\(7.52\)](#page-137-0) and [\(7.55\)](#page-138-0) are given by equation [\(7.41\)](#page-134-1) and represent those appearing in equation [\(7.23\)](#page-129-2) and guarantee mass conservation for the pore water advection.

### 7.5.2.3 Reactions

The bed transport solution is completed by

$$(BC)_k^{n+1} - (BC)_k^{n+3/4} = -\Delta t \gamma (BC)_k^{n+1}$$
(7.57)

an implicit reaction step.

#### <span id="page-139-0"></span>7.6. Chemical Loss Terms

#### <span id="page-139-1"></span>7.6.1 Bulk Degradation

Bulk degradation can be included in the water column and/or the sediment bed for any chemical constituent. The bulk degradation in the water column follows a first order decay rate

$$\frac{dC_k}{dt} = -KC_k \tag{7.58}$$

where,

C is the chemical concentration in *mg*/*m* 3 in layer *k*,

K is the first order decay rate in 1/*s*, and

t is the time in seconds.

For bulk degradation there is no temperature effects on the degradation rate.

In the sediment bed, bulk degradation can be applied for sediment thickness up to a maximum sediment depth

$$\frac{dC_{b,k}}{dt} = -KC_{b,k}, \quad \text{for} \quad \sum_{k}^{kt} H_{bed,k} \le D_{max}$$
 (7.59)

where,

*Cb*,*<sup>k</sup>* is the sediment bed chemical contaminant concentration in layer *k* (*mg*/*g*),

*K* is the bulk decay rate (1/*s*),

*Hbed*,*<sup>k</sup>* is the sediment bed layer thickness (*m*), and

*Dmax* is the maximum depth to use bulk degradation (*m*).

{140}------------------------------------------------

## <span id="page-140-0"></span>7.6.2 Biodegradation

Bacterial degradation, sometimes referred to as microbial transformation, biodegradation or biolysis, is the breakdown of a compound by the enzyme systems in bacteria. Although these transformations can detoxify and mineralize chemicals and defuse potential chemicals, they can also activate potential chemicals.

Biodegradation in [EFDC+](#page-11-0) follows the bulk degradation approach shown previously

$$\frac{dC_k}{dt} = -K_{w,bio}C_k \tag{7.60}$$

and

$$\frac{dC_{b,k}}{dt} = -K_{b,bio}C_{b,k}, \quad \text{for} \quad \sum_{k}^{kt} H_{bed,k} \le D_{bio}$$
 (7.61)

where,

*C<sup>k</sup>* is the chemical concentration in the water column in layer *k* (*mg*/*m* 3 ),

*Cb*,*<sup>k</sup>* is the sediment bed chemical contaminant concentration in layer k (mg/g),

*Kw*,*bio* is the water column biodegradation rate (1/*s*),

*Kb*,*bio* is the sediment bed biodegradation rate (1/*s*),

*Hbed*,*<sup>k</sup>* is the sediment bed layer thickness (*m*), and

*Dbio* is the maximum depth to apply biodegradation (*m*).

And where the degradation coefficient is temperature dependent, it can be calculated as

$$K_{bio} = K_{bio,ref} Q_{10}^{(T-20)/10} (7.62)$$

where,

*Kbio*,*re f* is respective reference biodegradation rate at 20 ◦*C* (1/*s*),

*Q*<sup>10</sup> is the temperature correction factor for biodegradation, and

*T* is the current temperature (◦*C*).

The temperature correction factors represent the increase in the biodegradation rate constants resulting from a 10 ◦C temperature increase. Values in the range of 1.5 to 2.0 are common.

## <span id="page-140-1"></span>7.6.3 Volatilization

Volatilization is the movement of chemical across the air-water interface as the dissolved neutral concentration attempts to equilibrate with the gas phase concentration. Equilibrium occurs when the partial pressure exerted by the chemical in solution equals the partial pressure of the chemical in the overlying atmosphere. The rate of exchange is proportional to the gradient between the dissolved concentration and the concentration in the overlying atmosphere and the conductivity across the interface of the two fluids. The conductivity 

{141}------------------------------------------------

is influenced by both chemical properties (molecular weight, Henry's Law constant) and environmental conditions at the air-water interface (turbulence-controlled by wind speed, current velocity, and water depth).

In EFDC+, volatilization of a dissolved chemical constituent is computed by

$$\left. \frac{\partial C}{\partial t} \right|_{volat} = \frac{K_v}{H_{KC}} \left( f_d C - \frac{C_a}{\frac{H_L}{RT_v}} \right) \tag{7.63}$$

where,

C is the water column concentration in layer KC  $(mg/m^3)$ ,

KC is the top layer number (dimensionless),

 $K_v$  is the transfer rate (m/dav),

 $H_{kc}$  is the water column thickness of the layer KC(m),

 $f_d$  is the fraction of the total chemical that is dissolved,

 $C_a$  is the atmospheric concentration  $(mg/m^3)$ ,

R is the universal gas constant  $8.206 \times 10^{-5} atm - m^3/mole - K$ ,

 $T_K$  is the water temperature in Kelvin ( ${}^{\circ}K$ ), and

 $H_L$  is the Henry's law coefficient for the air-water partitioning of the chemical  $(atm - m^3/mole)$ .

Equilibrium occurs when the dissolved concentration equals the partial pressure divided by the Henry's Law Constant.

The dissolved concentration of a chemical in a surface water column segment can volatilize at a rate determined by the two-layer resistance model Whitman et al. (1923). The two-resistance method assumes that two "stagnant films" are bounded on either side by well mixed compartments. Concentration differences serve as the driving force for the water layer diffusion. Pressure differences drive the diffusion for the air layer. From mass balance considerations, it is obvious that the same mass must pass through both films, thus the two resistances combine in series, so that the conductivity is the reciprocal of the total resistance:

<span id="page-141-0"></span>
$$K_{\nu} = (R_L + R_G)^{-1} = \left[ K_L^{-1} + \left( K_G \frac{H_L}{RT_K} \right)^{-1} \right]^{-1}$$
 (7.64)

where,

 $R_L$  is the liquid phase resistance (s/m),

 $K_L$  is the liquid phase transfer coefficient (s/day),

 $R_G$  is the gas phase resistance (s/m), and

 $K_G$  is the gas phase transfer coefficient (m/s).

There is yet another resistance involved, the transport resistance between the two interfaces, but it is assumed to be negligible. This may not be true in very turbulent conditions, and in the presence of surface-active contaminants. Although this two-resistance method, the Whitman model, is rather simplified in its assumption of uniform layers, it has been shown to be as accurate as more complex models.

{142}------------------------------------------------

The value of *Kv*, the conductivity, depends on the intensity of turbulence in a water body and in the overlying atmosphere. [Leinonen and Mackay](#page-262-9) [\(1975\)](#page-262-9) have discussed conditions under which the value of *K<sup>v</sup>* is primarily determined by the intensity of turbulence in the water. As the Henry's Law coefficient increases, the conductivity tends to be increasingly influenced by the intensity of turbulence in water. As the Henry's Law coefficient decreases, the value of the conductivity tends to be increasingly influenced by the intensity of atmospheric turbulence.

The computed volatilization rate from equation [\(7.64\)](#page-141-0) is for a temperature of 20◦*C*. It is adjusted for water temperature using the equation:

$$K_{\nu,T} = K_{\nu} \Theta^{T-20} \tag{7.65}$$

where,

Θ is the temperature correction factor, and

*T* is the water temperature (◦ *C*).

The liquid and gas film transfer coefficients computed under this option vary with the type of waterbody. The type of waterbody is specified as one of the volatilization constants and can either be a flowing stream, river or estuary or a stagnant pond or lake. The primary difference is that in a flowing waterbody the turbulence is primarily a function of the stream velocity, while for stagnant waterbodies wind shear may dominate. The formulations used to compute the transfer coefficients vary with the waterbody type as shown below.

[EFDC+](#page-11-0) automatically determines which flow regime to apply based on the following criteria

$$\begin{bmatrix}
H > H_{max}, Lake conditions \\
H \le H_{max}, River conditions
\end{bmatrix}$$
(7.66)

or

$$\begin{bmatrix} U \leq U_{max}, Lake \ conditions \\ U > U_{max}, \ River \ conditions \end{bmatrix}$$
 (7.67)

where,

*H* is total depth (*m*),

*Hmax* is maximum depth allowed for river conditions (*m*),

*U* is the depth averaged velocity magnitude (*m*/*s*), and

*Umax* is the maximum lake velocity magnitude (*m*/*s*).

#### 7.6.3.1 Flowing Stream, River or Estuary

For a flowing system, the transfer coefficients are controlled by flow induced turbulence. For flowing conditions, the liquid film transfer coefficient (*KL*) is computed using the Covar method Fig. [7.3](#page-143-0) [\(Covar,](#page-259-7) [1976\)](#page-259-7) in which the equation used varies with the velocity and depth of the cell.

{143}------------------------------------------------

<span id="page-143-0"></span>Fig. 7.3. Covar Method (1976).

For cells with depths less than 0.61 *m*, the Owens formula is used to calculate the volatilization rate [\(7.68\)](#page-143-1).

<span id="page-143-1"></span>
$$K_L = \frac{5.35}{86400} \frac{U^{0.67}}{H^{1.85}} H \tag{7.68}$$

where,

*U* is the depth averaged water velocity magnitude (*m*/*s*), and

*H* is cell depth (*m*).

For segments with a cell depth greater than 0.61 *m* and cell depth (*m*) greater than 3.45*U* 2.5 the O'Connor-Dobbins formula is used:

$$K_L = \frac{(D_w U)^{0.5}}{H^{1.5}} H \tag{7.69}$$

where, *D<sup>w</sup>* is the diffusivity of the chemical in water (*m* <sup>2</sup>/*s*), computed from

{144}------------------------------------------------

<span id="page-144-0"></span>
$$D_w = \frac{22 \cdot 10^{-9}}{M_w^{0.6667}} \tag{7.70}$$

In all other cases, the Churchill formula is used to calculate volatilization rate:

$$K_L = \frac{5.049}{86400} \frac{U^{0.969}}{H^{1.673}} H \tag{7.71}$$

The gas transfer coefficient  $(K_G)$  is assumed constant at  $100 \, m/day$  for flowing systems.

#### **7.6.3.2** Lake or Pond

For more quiescent conditions, the transfer coefficients are controlled by wind induced turbulence. For these systems, the liquid film transfer coefficient ( $K_L$ ) is computed using either the O'Connor equations or Mackay and Yeun (1983).

#### **Option 1 O'Connor Approach**

$$K_L = u_* \left(\frac{\rho_a}{\rho_w}\right)^{0.5} \frac{\kappa^{0.33}}{\lambda_2} S_{cw}^{-0.67}$$
 (7.72)

$$K_G = u_* \frac{\kappa^{0.33}}{\lambda_2} S_{ca}^{-0.67} \tag{7.73}$$

where,  $u_*$  is the shear velocity (m/s) computed from

$$u_* = C_d^{0.5} W_{10} (7.74)$$

where,

 $C_d$  is the drag coefficient (0.0011),

 $W_{10}$  is wind velocity at 10 m above the water surface (m/s),

 $\rho_a$  is density of air, internally calculated from air temperature  $(kg/m^3)$ ,

 $\rho_w$  is density of water, internally calculated from water temperature  $(kg/m^3)$ ,

 $\kappa$  is von Karman's constant,

 $\lambda_2$  is dimensionless viscous sublayer thickness, and

 $S_{ca}$  and  $S_{cw}$  are air and water Schmidt Numbers, computed from

$$S_{ca} = \frac{\mu_a}{\partial_a D_a} \tag{7.75}$$

$$S_{cw} = \frac{\mu_w}{\partial_w D_w} \tag{7.76}$$

where,

{145}------------------------------------------------

 $D_a$  is diffusivity of chemical in air  $(m^2/s)$ ,

 $D_w$  is diffusivity of chemical in water  $(m^2/s)$ ,

 $\mu_a$  is viscosity of air, internally calculated from air temperature (kg/m - sec), and

 $\mu_w$  is viscosity of water, internally calculated from water temperature (kg/m - sec).

The diffusivity of the chemical in water is computed using equation (7.70) while the diffusivity of the chemical in air  $(D_a, m^2/sec)$  is computed from

$$D_a = \frac{1.9 \cdot 10^{-4}}{M_w^{2/3}} \tag{7.77}$$

Thus  $K_G$  is proportional to wind and inversely proportional to molecular weight to the 4/9 power.

#### **Option 2 Mackay and Yeun Approach**

Under this option, the liquid and gas film transfer coefficients are computed using formulations described by Mackay and Yeun (1983). The Mackay equations are:

$$K_L = \begin{cases} 10^{-6} + 0.00341 u_* S_{cw}^{-0.5}, \ u_* > 0.3 \text{m/s} \\ 10^{-6} + 0.01441 u_*^{2.2} S_{cw}^{-0.5}, \ u_* < 0.3 \text{m/s} \end{cases}$$
(7.78)

$$K_G = 10^{-3} + 0.0462u_* S_{ca}^{-0.67} (7.79)$$

#### **Volatilization Input Data**

Although there are many calculations involved in determining volatilization, most are performed internally using a small set of data. Volatilization data specifications are summarized in Table 7.1 Not all of the constants are required. Volatilization is only active for the surface layer.

{146}------------------------------------------------

Table 7.1. Volatilization Input Data

<span id="page-146-0"></span>

| Description                                                      | Notation | Range       | Units           |
|------------------------------------------------------------------|----------|-------------|-----------------|
| Measured or calibrated conductance                               | Kv       | 0.6 — 25    | m/day           |
| Henry's Law Constant                                             | H        | 10−7 — 10−1 | 3/mole<br>atm−m |
| Concentration of chemical in<br>atmosphere                       | Ca       | 0 — 1000    | µg/L            |
| Molecular weight                                                 | Mw       | 10 — 103    | g/mole          |
| Reaeration coefficient (conductance<br>of oxygen)                | Ka       | 0.6 — 25    | m/day           |
| Experimentally measured ratio of<br>volatilization to reaeration | kvo      | 0 — 1       |                 |
| Current velocity                                                 | ux       | 0.2         | m/s             |
| Water depth                                                      | D        | 0.1 — 10    | m               |
| Water temperature                                                | T        | 4 — 30      | ◦C              |
| Wind speed 10m above surface                                     | W10      | 0 — 20      | m/s             |

{147}------------------------------------------------

## <span id="page-147-0"></span>Chapter 8

## EUTROPHICATION

In [EFDC+,](#page-11-0) the eutrophication module refers to modeling aquatic plants, algae, zooplankton, and the biochemical transformation of nutrients during this process. Collectively, these biological organisms are referred to as "Biota" in the [EFDC+](#page-11-0) interface, although it does not include higher trophic level organisms that consume the zooplankton. This chapter summarizes the basic theory of these processes as they are modeled in [EFDC+.](#page-11-0) The kinetic processes included in the [EFDC+](#page-11-0) eutrophication module are derived from the [ICM](#page-11-1) water quality model [\(Cerco and Cole,](#page-259-8) [1995\)](#page-259-8) as described in [Park et al.](#page-263-2) [\(1995\)](#page-263-2), and the formulation provided by [Cerco et al.](#page-259-9) [\(2004\)](#page-259-9). A sediment diagenesis process was also implemented in [EFDC+,](#page-11-0) primarily based on the Chesapeake Bay Sediment Flux Model developed by [DiToro and Fitzpatrick](#page-260-16) [\(1993\)](#page-260-16). The coupling of the sediment diagenesis module with the water quality module enhances the model to simulate long-term changes in water quality conditions in response to changes in nutrient loading by sediment fluxes released from the bed.

Prior to [EFDC+1](#page-11-0)0.3, the eutrophication module could only simulate three groups of phytoplankton (freefloating), and one group of macroalgae (attached). The predation of phytoplankton by higher trophic level organisms such as zooplankton was modeled using a constant rate or a rate proportional to algal biomass. From [EFDC+1](#page-11-0)0.3, the eutrophication module was enhanced to model unlimited groups of aquatic plants and algae, and zooplankton groups.[1](#page-147-1) Users can differentiate between the "Biota" groups by names and parameters assigned to these groups. The model simulates spatial and temporal distributions of water quality parameters, including dissolved oxygen, floating or attached algae (unlimited species), zooplankton (unlimited species), various components of carbon, nitrogen, phosphorus, and silica cycles, and fecal coliform bacteria. Figure [8.1](#page-148-0) illustrates the structure of the water quality model implemented in [EFDC+](#page-11-0) with the set of state variables listed in Table [8.1.](#page-149-0) The coupling between the water quality components is illustrated in Figure [8.2.](#page-150-2)

All the biota classes in [EFDC+](#page-11-0) are represented in [Carbon \(](#page-10-6)*C*) units. [Organic Carbon \(OC\),](#page-11-15) [Nitrogen \(](#page-10-7)*N*), and [Phosphorus \(](#page-10-8)*P*) are represented by up to three reactive sub-classes, refractory particulate, labile particulate, and labile dissolved. The use of sub-classes allows a more realistic distribution of organic material by reactive classes when data is available to estimate distribution factors. The following sections discuss the role of each variable and summarize their kinetic interaction processes. Sediment diagenesis processes including the exchange of nutrient fluxes at the sediment-water interface and [Sediment Oxygen Demand](#page-12-8)

<span id="page-147-1"></span><sup>1</sup>[Professor Dongil Seo from Chungnam National University, South Korea, has made significant contributions to the](#page-12-8) [development of the kinetic equations for phytoplankton and zooplankton modeling in](#page-12-8) [EFDC+.](#page-11-0) Journal articles pub[lished by Professor Seo's research group, based on their research using EFDC, include Kim et al. \(2021a\), Kim et al.](#page-12-8) [\(2021b](#page-262-12)), [Shiferaw et al.](#page-12-8) [\(2022\)](#page-264-19), [Kim et al.](#page-262-13) [\(2022\)](#page-262-13), and [Kim and Seo](#page-262-14) [\(2024\)](#page-262-14).

{148}------------------------------------------------

<span id="page-148-0"></span>[\(SOD\)](#page-12-8) are presented as a full sediment diagenesis model. A rooted plant and epiphytes sub-module is also described that can be used to model submerged macrophytes with shoots, roots, and epiphytes. The description of the [EFDC+](#page-11-0) eutrophication module in this section closely follows [Park et al.](#page-263-2) [\(1995\)](#page-263-2).

Fig. 8.1. Structure of the [EFDC+](#page-11-0) Water Quality Model.

{149}------------------------------------------------

Table 8.1. [EFDC+](#page-11-0) Water Quality State Variables

<span id="page-149-0"></span>

| #  | Water quality state variable              | Acronyms | Units       | Group                 |
|----|-------------------------------------------|----------|-------------|-----------------------|
| 1  | Refractory particulate organic carbon     | RPOC     | mg/l        | Organic carbon        |
| 2  | Labile particulate organic carbon         | LPOC     | mg/l        |                       |
| 3  | Dissolved Organic Carbon                  | DOC      | mg/l        |                       |
| 4  | Refractory particulate organic phosphorus | RPOP     | mg/l        | Phosphorus            |
| 5  | Labile particulate organic phosphorus     | LPOP     | mg/l        |                       |
| 6  | Dissolved organic phosphorus              | DOP      | mg/l        |                       |
| 7  | Total phosphate                           | PO4t     | mg/l        |                       |
| 8  | Refractory particulate organic nitrogen   | RPON     | mg/l        | Nitrogen              |
| 9  | Labile particulate organic nitrogen       | LPON     | mg/l        |                       |
| 10 | Dissolved Organic Nitrogen                | DON      | mg/l        |                       |
| 11 | Ammonium                                  | NH4      | mg/l        |                       |
| 12 | Nitrate and Nitrite                       | NO3, NO2 | mg/l        |                       |
| 13 | Particulate biogenic silica               | SiP      | mg/l        | Silica                |
| 14 | Dissolved available silica                | SiA      | mg/l        |                       |
| 15 | Chemical Oxygen Demand                    | COD      | mg/l        | Others                |
| 16 | Dissolved Oxygen                          | DO       | mg/l        |                       |
| 17 | Total Active Metals                       | TAM      | 3<br>mole/m |                       |
| 18 | Fecal coliform bacteria                   | FCB      | MPN/100ml   |                       |
| 19 | Carbon dioxide                            | CO2      | mg/l C      |                       |
| 20 | Aquatic Plants                            | Ba       | mg/l C      | Algae and Macrophytes |
|    |                                           |          |             | (Unlimited groups)    |
| 21 | Aquatic Animals                           | Zz       | mg/l C      | Zooplankton           |
|    |                                           |          |             | (Unlimited groups)    |

{150}------------------------------------------------

<span id="page-150-2"></span>Fig. 8.2. Schematic Diagram of [EFDC+](#page-11-0) Water Quality Model Structure.

### <span id="page-150-0"></span>8.1. Water Column Eutrophication Formulation

## <span id="page-150-1"></span>8.1.1 Model State Variables

#### 8.1.1.1 Algae and Macrophyte

Algae and macrophyte are a central part of the numerical eutrophication models. From the modeling point of view, algae are often grouped based on the distinctive characteristics and the significant role the characteristics play in the ecosystem. The legacy [EFDC](#page-11-2) eutrophication module included three free-floating groups (cyanobacteria, diatoms, and greens) and a stationary or non-transported group (macroalgae).

Cyanobacteria, commonly called blue-green algae, are characterized by their abundance (as picoplankton) in saline water and by their bloom-forming characteristics in fresh water. Cyanobacteria are unique in that some species fix atmospheric nitrogen, although nitrogen fixers are not believed to be predominant in many river systems. Diatoms are distinguished by their requirement of silica as a nutrient to form cell walls. Diatoms are large algae, characterized by high settling velocities. Settling of spring diatom blooms to the sediments may be a significant source of carbon for [SOD.](#page-12-8) Algae that do not fall into the preceding two groups are lumped into green algae. Green algae settle at a rate intermediate between cyanobacteria and diatoms, and are subject to greater grazing pressure than cyanobacteria.

{151}------------------------------------------------

Macrophyte group, defined as stationary or non-transported algae variables, can be included in the model to simulate macroalgae/periphyton groups. The stationary algae variables have the same kinetic formulation as the original algae groups, with the exception that they are not transported. The stationary algae groups can also be used to represent various types of bottom substrate attached or floating periphyton.

From [EFDC+1](#page-11-0)0.3 onwards, unlimited groups of algae and macrophyte could be modeled and are differentiated based on the label and parameters. Appendix [8.4](#page-234-0) provides additional information regarding model configuration for eutrophication simulation.

### 8.1.1.2 Zooplankton

Zooplankton consist of animal life that are adrift in a waterbody. They include the larval forms of large adult organisms (e.g., crabs, fish) and small animals that never get larger than several millimeters. Zooplankton form an important link in the food web. They consume algae by filtering the surrounding water and then clearing off the algae. They also consume bacteria, detritus, and sometimes other zooplankton, and are also predated by small fish. Zooplankton grazing can be a key loss mechanism for algae, depending on the time of the year, zooplankton population, and zooplankton grazing rate. From [EFDC+1](#page-11-0)0.3 onwards, an unlimited number of zooplankton groups can be included in the simulation through specification of their kinetics parameters. Kinetic equations of zooplankton and its interaction with the water quality components are derived from [\(Cerco et al.,](#page-259-10) [2004;](#page-259-10) [Seo,](#page-264-20) [2019\)](#page-264-20). Figure [8.3](#page-151-0) illustrates the interaction between zooplankton and other state variables.

<span id="page-151-0"></span>Fig. 8.3. Interaction of Zooplankton with Eutrophication components.

#### 8.1.1.3 Organic Carbon (OC)

The three [OC](#page-11-15) state variables considered in [EFDC+](#page-11-0) are; [\(DOC\)](#page-11-13), [Labile Particulate Organic Carbon \(LPOC\),](#page-11-16) and [Refractory Particulate Organic Carbon \(RPOC\).](#page-12-9) Labile and refractory distinctions are based upon the 

{152}------------------------------------------------

time scale of decomposition. Labile OC decomposes rapidly on a time scale of days to weeks, whereas refractory OC requires more time, and may take multiple years.

#### **8.1.1.4** Nitrogen (N)

N is first divided into organic and mineral fractions. Organic Nitrogen (ON) state variables are Dissolved Organic Nitrogen (DON), Labile Particulate Organic Nitrogen (LPON), and Refractory Particulate Organic Nitrogen (RPON). The mineral N forms are Ammonium  $(NH_4^+)$  and Nitrate  $(NO_3^-)$ . Both mineral forms are utilized to satisfy algal nutrient requirements, although  $NH_4^+$  is thermodynamically preferred.  $NH_4^+$  is oxidized by nitrifying bacteria into  $NO_3^-$ . This oxidation can be a significant sink of Oxygen (O) in the water column and sediments. An intermediate in the complete oxidation of  $NH_4^+$ , Nitrite  $(NO_2^-)$  also exists.  $NO_2^-$  concentrations are usually much less than  $NO_3^-$ , and for modeling purposes,  $NO_2^-$  is combined with  $NO_3^-$ . Hence, the  $NO_3^-$  state variable actually represents the sum of  $NO_3^-$  and  $NO_2^-$ .

#### **8.1.1.5 Phosphorus (P)**

Organic P is also considered in three states; Dissolved Organic Phosphorus (DOP), Labile Particulate Organic Phosphorus (LPOP), and Refractory Particulate Organic Phosphorus (RPOP). Only a single mineral form, Phosphate  $(PO_4^{-3})$ , is considered.  $PO_4^{-3}$  exists in several states within the model ecosystem; dissolved, sorbed to inorganic solids, and incorporated in the algal cells. Equilibrium partition coefficients are used to distribute the  $PO_4^{-3}$  among the three states.

#### **8.1.1.6** Silica (*SiO*<sub>2</sub>)

Silica ( $SiO_2$ ) is divided into two state variables; Dissolved Available Silica (SiA) and Particulate Biogenic Silica (SiP). SiA is primarily dissolved and can be utilized by diatoms. SiP cannot be utilized. In the model, SiP is produced through diatom mortality. SiP undergoes dissolution to SiA or else settles to the bottom sediments.

#### **8.1.1.7** Chemical Oxygen Demand (COD)

In EFDC+, Chemical Oxygen Demand (COD) is the concentration of reduced substances that are oxidizable by inorganic means. The primary component of COD is Sulfide  $(S_2^-)$  released from sediments. Oxidation of  $S_2^-$  to Sulfate  $(SO_4^{-2})$  may remove substantial quantities of DO from the water column.

#### 8.1.1.8 Dissolved Oxygen (DO)

DO is required for the existence of higher life forms, and is a central component of the water quality model. DO availability determines the distribution of organisms and the flows of energy and nutrients in an ecosystem.

{153}------------------------------------------------

#### **8.1.1.9** Total Active Metal (TAM)

Both  $PO_4^{-3}$  and SiA adsorb to inorganic solids, primarily Iron (Fe) and Manganese (Mn). Sorption and subsequent settling is one pathway for removal of  $PO_4^{-3}$  and SiA from the water column. However, limited data does not allow a complete treatment of Fe and Mn chemistry. Rather, a single-state variable Total Active Metals (TAM), is defined as the total concentration of metals that are active in  $PO_4^{-3}$  and SiA. TAM is partitioned between particulate and dissolved phases by an oxygen-dependent partition coefficient. Inorganic suspended solids can be used, in lieu of TAM, as a sorption site for  $PO_4^{-3}$  and SiA. TSS concentration is provided by the sediment transport component of the EFDC+ modeling system.

#### <span id="page-153-0"></span>**8.1.2** Conservation of Mass Equation

The conservation of mass accounts for the material entering/leaving a water body, transport of the material within the water body, and physical, chemical, biological transformation of material. Hence, the governing mass-balance equation for each of the water quality state variables with a concentration C can be expressed as:

$$\frac{\partial}{\partial t} (m_x m_y HC) + \frac{\partial}{\partial x} (m_y HuC) + \frac{\partial}{\partial y} (m_x HvC) + \frac{\partial}{\partial z} (m_x m_y wC) = 
\frac{\partial}{\partial x} \left( \frac{m_y HA_x}{m_x} \frac{\partial C}{\partial x} \right) + \frac{\partial}{\partial y} \left( \frac{m_x HA_y}{m_y} \frac{\partial C}{\partial y} \right) + \frac{\partial}{\partial z} \left( m_x m_y \frac{A_z}{H} \frac{\partial C}{\partial z} \right) + m_x m_y HS_C \quad (8.1)$$

The last three terms on the Left Hand Side (LHS) of equation 8.1 account for the advective transport, and the first three terms on the Right Hand Side (RHS) account for the diffusive transport. These six terms for physical transport are analogous to, and thus the numerical method of solution is the same as, those in the mass-balance equation for salinity in the hydrodynamic model (Hamrick, 1992). The last term  $S_C$  in the equation 8.1 is the internal and external sources and sinks per unit volume, represents the kinetic processes and external loads for each of the state variables.

EFDC+ solves equation 8.1 using a fractional step procedure which decouples the kinetic terms from the physical transport terms. The equation for physical transport is written as:

$$\frac{\partial}{\partial t_{p}} (m_{x}m_{y}HC) + \frac{\partial}{\partial x} (m_{y}HuC) + \frac{\partial}{\partial y} (m_{x}HvC) + \frac{\partial}{\partial z} (m_{x}m_{y}wC) = 
\frac{\partial}{\partial x} \left( \frac{m_{y}HA_{x}}{m_{x}} \frac{\partial C}{\partial x} \right) + \frac{\partial}{\partial y} \left( \frac{m_{x}HA_{y}}{m_{y}} \frac{\partial C}{\partial y} \right) + \frac{\partial}{\partial z} \left( m_{x}m_{y} \frac{A_{z}}{H} \frac{\partial C}{\partial z} \right) + m_{x}m_{y}HS_{CP} \quad (8.2)$$

The equation for kinetic processes and external loading, called kinetic equation, is:

<span id="page-153-3"></span><span id="page-153-2"></span><span id="page-153-1"></span>
$$\frac{\partial C}{\partial t_k} = S_{CK} \tag{8.3}$$

with

<span id="page-153-4"></span>
$$\frac{\partial}{\partial t} (m_x m_y HC) = \frac{\partial}{\partial t_p} (m_x m_y HC) + (m_x m_y H) \frac{\partial C}{\partial t_k}$$
(8.4)

{154}------------------------------------------------

In the equations above, the subscript *k* refers to the kinetic processes while the subscript *p* refers to the physical transport of a water quality component.

The source sink term *S<sup>C</sup>* in equation [8.2,](#page-153-2) has been split into physical sources and sinks which are associated in volumetric inflows and outflows, and kinetic sources and sinks in equations [8.3](#page-153-3) and [8.4,](#page-153-4) respectively. Since variations in the water column depth are coupled with the divergence of the volume transport field, the kinetic step is made at a constant water column depth corresponding to the depth field at the end for the physical transport step. This allows the depth and scale factors to be eliminated from the kinetic step in equation [8.3](#page-153-3) which can be further split into reactive and internal sources and sinks as:

<span id="page-154-1"></span>
$$\frac{\partial C}{\partial t_k} = K \cdot C + R \tag{8.5}$$

where,

*K* is the kinetic rate (*time*−<sup>1</sup> ), and

*R* represents internal source/sink term (*mass volume*−<sup>1</sup> *time*−<sup>1</sup> ).

Equation [8.5](#page-154-1) is obtained by linearizing some terms in the kinetic equations, mostly Monod type expressions. Hence, *K* and *R* are known values in equation [8.5.](#page-154-1) Equation [8.2](#page-153-2) is identical to, and thus its numerical method of solution is the same as, the mass-balance equation for salinity [\(Hamrick,](#page-261-3) [1992\)](#page-261-3). The solution scheme for both the physical transport [\(Hamrick,](#page-261-3) [1992\)](#page-261-3) and the kinetic equations is second-order accurate.

## <span id="page-154-0"></span>8.1.3 Kinetic Equations for State Variables

The remainder of this chapter details the kinetics portion of the mass-conservation equation for each state variable. Parameters are defined where they first appear. All parameters are listed, in alphabetical order, in Appendix (section [8.4\)](#page-234-0). For consistency with reported rate coefficients, kinetics are detailed using a temporal dimension of days. Within the [EFDC+](#page-11-0) code, kinetic sources and sinks are converted to a dimension of seconds before they are used in the mass-conservation equations.

#### 8.1.3.1 Algae

[EFDC+](#page-11-0) simulates unlimited general autotroph groups that can be parameterized to represent any specific species or a group of species. Each group can be paramterized and labeled accordingly. For a general group, the kinetics in the model are governed by:

- 1. Growth (production)
- 2. Basal metabolism
- 3. Predation by zooplankton
- 4. Mortality
- 5. Settling
- 6. External loads

{155}------------------------------------------------

Since these processes are largely the same for all algal groups, the kinetics equation for a general algae x can be written as:

<span id="page-155-1"></span>
$$\frac{\partial B_{x}}{\partial t} = (P_{x} - BM_{x} - D_{x})B_{x} - PR_{x} + \frac{\partial}{\partial Z}(WS_{x}B_{x}) + \frac{WB_{x}}{V}$$
(8.6)

where,

*B*<sup>x</sup> is the algal biomass of algal group x (*g C*/*m* 3 ),

*t* is the time (*days*),

*P*<sup>x</sup> is the production rate of algal group x (1/*day*),

*BM*<sup>x</sup> is the basal metabolism rate of algal group x (1/*day*),

*D*<sup>x</sup> is the mortality rate of algal group x (1/*day*),

*PR*<sup>x</sup> is the predation rate of algal group x by zooplankton,

*WS*<sup>x</sup> is the positive settling velocity of algal group x (*m*/*day*),

*WB*<sup>x</sup> is the external loading of algal group x (*g C*/*day*), and

*V* is the model cell volume (*m* 3 ).

### 8.1.3.1.1 Production (Algal Growth)

Algal growth depends on nutrient availability, ambient light, and temperature. The effects of these processes are considered to be multiplicative:

<span id="page-155-0"></span>
$$P_{x} = PM_{x}f_{1}(N)f_{2}(I)f_{3}(T)f_{4}(S)$$
(8.7)

where,

*PM<sup>x</sup>* is the maximum growth rate under optimal conditions for algal group *x* (1/*day*),

*f*1(*N*) is the effect of suboptimal nutrient concentration (0 ≤ *f*<sup>1</sup> ≤ 1),

*f* <sup>2</sup>(*I*) is the effect of suboptimal light intensity (0 ≤ *f*<sup>2</sup> ≤ 1),

*f* <sup>3</sup>(*T*) is the effect of suboptimal temperature (0 ≤ *f*<sup>3</sup> ≤ 1), and

*f*4(*S*) is the effect of salinity on the growth (0 ≤ *f*<sup>4</sup> ≤ 1),

For the freshwater organisms, the increased mortality is included in the model by the salinity toxicity term in the growth equation.

#### 8.1.3.1.1.1 Effect of Nutrients on Algal Growth

Using Liebig's "law of the minimum" [\(Odum,](#page-263-15) [1971\)](#page-263-15) algal growth is determined by the nutrient in least supply, the nutrient limitation for growth of an algal group is expressed as:

<span id="page-155-2"></span>
$$f_1(N) = min\left(\frac{NH4 + NO3}{KHN_x + NH4 + NO3}, \frac{PO4}{KHP_x + PO4}, \frac{SAd}{KHS + SAd}\right)$$
(8.8)

where,

{156}------------------------------------------------

*NH*4 is the *[NH](#page-10-9)*<sup>+</sup> 4 concentration as N (*g N*/*m* 3 ),

*NO*3 is the *[NO](#page-10-10)*<sup>−</sup> 3 concentration as N (*g N*/*m* 3 ),

*KHN<sup>x</sup>* is the half-saturation constant for *[N](#page-10-7)* uptake for algal group *x* (*g N*/*m* 3 ),

*PO*4 is the dissolved phosphate concentration as *[P](#page-10-8)* (*g P*/*m* 3 ),

*KHP<sup>x</sup>* is the half-saturation constant for *[P](#page-10-8)* uptake for algal group *x* (*g P*/*m* 3 ),

*SAd* is the concentration of dissolved available *[SiO](#page-10-14)*<sup>2</sup> (*g Si*/*m* 3 ), and

*KHS* is the half-saturation constant for *[SiO](#page-10-14)*<sup>2</sup> uptake for diatoms (*g Si*/*m* 3 ).

Some cyanobacteria (e.g., *Anabaena*) can fix *[N](#page-10-7)* from atmosphere and thus are not limited by *[N](#page-10-7)*. In that case, *[N](#page-10-7)* terms can be ignored for cyanobacteria. *[SiO](#page-10-14)*<sup>2</sup> is a limitation for diatoms only, and can be ignored for other groups.

### 8.1.3.1.1.2 Effect of Light on Algal Growth

The effect of light on algal growth is calculated using daily and vertically integrated form of Steele's equation [\(Cerco and Cole,](#page-259-8) [1995\)](#page-259-8) as shown below:

<span id="page-156-0"></span>
$$f_2(I) = \frac{\exp(1) FD}{K_{ess} (ZB - ZT)} \left( \exp(-\alpha_b) - \exp(-\alpha_T) \right)$$
(8.9)

<span id="page-156-1"></span>
$$\alpha_B = \left(\frac{I_0}{FD \cdot I_{sx}}\right) \exp\left(-K_{ess} ZB\right) \tag{8.10}$$

$$\alpha_T = \left(\frac{I_0}{FD \cdot I_{sx}}\right) \exp\left(-K_{ess} ZT\right) \tag{8.11}$$

where,

*FD* is the fractional day length (0 ≤ *FD* ≤ 1),

*Kess* is the total light extinction coefficient (1/*m*),

*ZT* is the distance from water surface to layer top (*m*),

*ZB* is the distance from water surface to layer bottom (*m*),

*I*<sup>0</sup> is the daily total light intensity at water surface (*langleys*/*day*), and

*Isx* is the optimal light intensity for algal group *x* (*langleys*/*day*).

The total light extinction *Kess* in the water column is calculated using equation [5.17.](#page-77-0) Optimal light intensity *Isx* for photosynthesis depends on algal taxonomy, duration of exposure, temperature, nutritional status, and previous acclimation. Variations in *Isx* are largely due to adaptations by algae intended to maximize production in a variable environment. [Steele](#page-264-21) [\(1962\)](#page-264-21) noted the result of adaptations is that the optimal intensity is a consistent fraction (approximately 50 %) of daily intensity. [Kremer and Nixon](#page-262-15) [\(1978\)](#page-262-15) reported an analogous finding that maximum algal growth occurs at a constant depth (approximately 1 *m*) in the water column. Their approach is adopted so that optimal intensity is expressed as:

{157}------------------------------------------------

<span id="page-157-0"></span>
$$I_{sx} = \max \left( I_{0avg} \cdot \exp \left( -K_{ess} D_{optx} \right), I_{sxmin} \right)$$
(8.12)

where,

*Doptx* is the depth of maximum algal growth for algal group *x* (*m*),

*I*0*avg* is the adjusted surface light intensity (*W*/*m* 2 ), and

*Isxmin* is the minimum optimum light intensity (*W*/*m* 2 ).

A minimum *Isxmin*, in equation [8.12](#page-157-0) is specified so that algae do not thrive at extremely low light levels. The time required for algae to adapt to changes in light intensity is recognized by estimating *I*0*avg* based on a time-weighted average of daily light intensity:

<span id="page-157-2"></span><span id="page-157-1"></span>
$$I_{0avg} = CI_aI_0 + CI_bI_1 + CI_cI_2 (8.13)$$

where,

*I*<sup>1</sup> is the daily light intensity 1 day preceding model day (*langleys*/*day*),

*I*<sup>2</sup> is the daily light intensity 2 days preceding model day (*langleys*/*day*), and

*CIa*, *CIb*, *CI<sup>c</sup>* are the weighting factors for *I*0,*I*<sup>1</sup> and *I*2, respectively: *CI<sup>a</sup>* +*CI<sup>b</sup>* +*CI<sup>c</sup>* = 1.

## 8.1.3.1.1.3 Effect of Temperature on Algal Growth

A Gaussian probability curve is used to represent temperature dependency of algal growth:

$$f_3(T) = \begin{cases} \exp(-KTG1_x \cdot (T - TM1_x)^2), & T \le TM1_x \\ 1, & TM1_x < T < TM2_x \\ \exp(-KTG2_x \cdot (T - TM2_x)^2), & T \ge TM2_x \end{cases}$$
(8.14)

where,

*T* is the temperature (◦*C*) provided from the hydrodynamic model,

*T M*1*<sup>x</sup>* is the minimum optimal temperature for algal growth for algal group *x* ( ◦*C*),

*T M*2*<sup>x</sup>* is the maximum optimal temperature for algal growth for algal group *x* ( ◦*C*),

*KT G*1*<sup>x</sup>* is the effect of temperature below *T M*1*<sup>x</sup>* on growth for algal group *x* (1/◦*C* 2 ), and

*KT G*2*<sup>x</sup>* is the effect of temperature above *T M*2*<sup>x</sup>* on growth for algal group *x* (1/◦*C* 2 ).

The formulation of equation [8.14](#page-157-1) represents a modification to the [ICM](#page-11-1) formulation to allow for temperature range specification of optimum growth.

{158}------------------------------------------------

## 8.1.3.1.1.4 Effect of Salinity

For models that are simulating algal groups affected by salinity (e.g. cyanobacteria), the growth limitation due to salinity can be calculated as:

<span id="page-158-0"></span>
$$f_4(S) = \frac{STOXS^2}{STOXS^2 + S^2}$$
 (8.15)

where,

*STOXS* is the salinity at which the algal group growth is halved (*ppt*), and

*S* is the salinity in water column (*ppt*) provided from the hydrodynamic model.

## 8.1.3.1.2 Basal Metabolism

Algal biomass in the model decreases through basal metabolism (respiration and excretion), predation and death. In basal metabolism, algal matter (*[C](#page-10-6)*, *[N](#page-10-7)*, *[P](#page-10-8)*, and *[SiO](#page-10-14)*2) is returned to organic and inorganic pools in the environment, mainly to dissolved organic and inorganic matter. Respiration, which may be viewed as a reversal of photosynthesis, consumes [DO.](#page-11-3) Basal metabolism is considered to be an exponentially increasing function of temperature:

<span id="page-158-1"></span>
$$BM_{x} = BMR_{x} \exp\left(KTB_{x}\left[T - TR_{x}\right]\right) \tag{8.16}$$

where,

*T R<sup>x</sup>* is the reference temperature for basal metabolism for algal group *x* ( ◦*C*).

*BMR<sup>x</sup>* is the basal metabolism rate at *T R<sup>x</sup>* for algal group *x* (1/*day*), and

*KT B<sup>x</sup>* is the effect of temperature on metabolism for algal group *x* (1/◦*C*).

#### 8.1.3.1.3 Algal Predation

In cases, where there is limited data available regarding zooplankton, a constant predation rate can be specified for each algal group, which implicitly assumes zooplankton biomass is a constant fraction of algal biomass. Alternately, the predation rate can be taken as proportional to the algae biomass. Using a temperature effect similar to that for metabolism, the predation rate is given as:

<span id="page-158-2"></span>
$$PR_{x} = PRR_{x} \left(\frac{B_{x}}{B_{xP}}\right)^{\alpha_{P}} \exp\left(KTP_{x}\left[T - TP_{x}\right]\right)$$
(8.17)

where,

*T P<sup>x</sup>* is the reference temperature rate for predation for algal group *x*,

*BxP* is the reference algae concentration for predation (*g C*/*m* 3 ),

*PRR<sup>x</sup>* is the reference predation rate at *BxP* and *T P<sup>x</sup>* for algal group *x* (1/*day*),

α*<sup>P</sup>* is the exponential dependence factor, and

*KT P<sup>x</sup>* is the effect of temperature on predation for algal group *x* (1/◦*C*).

{159}------------------------------------------------

When the model simulates zooplankton, the predation of algae group x is estimated based on the utilization of zooplankton as:

$$PR_{x} = \frac{PA_{z}}{KHC_{z} + PA_{z}} \cdot RMAX_{z} \cdot Z_{z} \cdot \frac{UB_{xz} \cdot B_{x}}{PA_{z}} \cdot f(T)$$
(8.18)

where,

*Zz* is the concentration of zooplankton group *z* (gCm−<sup>3</sup> ),

*PA<sup>z</sup>* is the prey available to zooplankton group *z* (gCm−<sup>3</sup> ),

*KHC<sup>z</sup>* is the prey density at which grazing is halved (gCm−<sup>3</sup> ),

*RMAX<sup>z</sup>* is the maximum ration of zooplankton group *z* (g prey C g−<sup>1</sup> zooplankton C day−<sup>1</sup> ),

*UBxz* is the utilization of algal group *x* by zooplankton group *z*,

*f*(*T*) is the effect of temperature on grazing

The difference between predation and basal metabolism lies in the distribution of the end products of the two processes. In predation, algal matter (*[C](#page-10-6)*, *[N](#page-10-7)*, *[P](#page-10-8)*, and *[SiO](#page-10-14)*2) is returned to the organic and inorganic pools in the environment, mainly to particulate organic matter, compared to metabolism where the algal matter is returned to dissolved organic and inorganic matter. This distribution can be specified by the modeler.

It is also noted that predation in the [EFDC+](#page-11-0) water quality model follows the original formulation in the [ICM](#page-11-1) model [\(Cerco and Cole,](#page-259-8) [1995\)](#page-259-8) which uses a predation rate constant with total predation loss being proportional to algae concentration. Subsequent [ICM](#page-11-1) documentation [Cerco et al.](#page-259-11) [\(2000\)](#page-259-11), appear to define predation independent of algae concentration.

#### 8.1.3.1.4 Algal Vertical Migration

The vertical migration of algae includes the settling process which removes algae from the water column and deposits it onto the bottom of the waterbody. The settling algae can be a significant source of nutrients to the sediment bed and can play an important role in the sediment diagenesis process. The settled algal biomass undergoes bacterial and biochemical reactions in the bed, and then releases nutrients back to the water column.

Additionally, some cyanobacteria can move vertically in the water column, independent of water velocity. According to [Kromkamp and Mur](#page-262-16) [\(1984\)](#page-262-16), the daily pattern of cyanobacteria vertical migration can be explained by increased cell density due to carbohydrate accumulation by photosynthesis in the light and decreased cell density due to utilization of carbohydrates in the dark. The vertical migration of those cyanobacteria species is thought to facilitate these species' alternating access to the surface layers of a waterbody, where light is abundant, and photosynthesis can occur, and lower, more nutrient-rich layers. This can result in the creation of surface accumulations known as harmful algae blooms (HABs), which lead to reducing sunlight penetration in the water and subsequent oxygen depletion, harming fish, and other aquatic organisms. From [EFDC+](#page-11-0) 12, different models for the vertical movement of algae that have been added to the Water Quality module.

#### 8.1.3.1.4.1 Predefined velocity model

The vertical migration of cyanobacteria can be simulated using a predefined velocity function based on their typical movement patterns. The first model approach, based on [Overman and Wells](#page-263-16) [\(2022\)](#page-263-16), simply assumes 

{160}------------------------------------------------

that the cyanobacteria migrate vertically on a daily cycle with a velocity depends on time as:

<span id="page-160-0"></span>
$$v_s(t) = A \frac{2\pi}{86400} \cos\left(\frac{2\pi}{86400}t + \varphi\right) \tag{8.19}$$

Where, *v<sup>s</sup>* (*ms*−<sup>1</sup> ) is the algae settling velocity, *A*(*m*) is the migration amplitude and the period is assumed to be one day (86400 s), ϕ (*rad*) is the phase shift which depends on the initial location of the colony. The second model approach is slightly more complex by assuming the velocity function is dependent both on time and on space. Modifying Equation [8.19](#page-160-0) to include the variation in space of the amplitude as in [Belov](#page-258-12) [and Giles](#page-258-12) [\(1997\)](#page-258-12) gives:

$$v_s(t) = \begin{cases} A \frac{2\pi}{86400} \cos\left(\frac{2\pi}{86400}t + \varphi\right) e^{-\alpha(H-z)}, & I_s > 0\\ A \frac{2\pi}{86400} \cos\left(\frac{2\pi}{86400}t + \varphi\right), & I_s \le 0 \end{cases}$$
(8.20)

Where, α is the light attenuation coefficient and *I<sup>s</sup>* (*Wm*−<sup>2</sup> ) is solar irradiance at the water surface, *H* (*m*) is the water depth, *z*(*m*) is the depth coordinate. The addition of the exponential term is only applied when there is sunlight present. During the dark periods, the equation reduced to the Equation [8.19.](#page-160-0)

#### 8.1.3.1.4.2 Dynamic Velocity model

The predefined velocity models can predict cyanobacteria movement based on their observed tendency of migration on a daily cycle; however, they do not reflect the response of cyanobacteria to variations in solar irradiance. To capture this behavior, a dynamic velocity model was implemented based on [Visser et al.](#page-265-15) [\(1997\)](#page-265-15). In this model, the settling velocity is calculated dynamically by Stokes's law based on the timevarying density of the cyanobacteria cell. Equations of relationship between density changes and photon irradiance were established and applied based on laboratory experiment data.

During periods when photon irradiance is higher than a compensation value *Ic*, the rate of density change is estimated using Equation [8.21:](#page-160-1)

<span id="page-160-1"></span>
$$\frac{d\rho}{dx} = \left(\frac{N_0}{60}\right) I e^{-I/I_0} + c, \quad I \ge I_c \tag{8.21}$$

where *N<sup>o</sup>* is a regression coefficient, *I*(*Wm*−<sup>2</sup> ) is the photon irradiance at depth of colony, *c* is the rate of density change when *I* = 0, and *I<sup>o</sup>* (*Wm*−<sup>2</sup> ) is the light intensity corresponding to the maximum density.

During periods of darkness when the photon irradiance is lower than the compensation value *Ic*, the density decreases at a rate calculated as:

<span id="page-160-2"></span>
$$\frac{d\rho}{dx} = f_1 \rho_i + f_2 \quad I < I_c \tag{8.22}$$

where, ρ*i*(*kgm*−<sup>3</sup> ) is the cell density at the end of the preceding light period, and *f*<sup>1</sup> and *f*<sup>2</sup> are regression coefficients. The numerical solutions of Equations [8.21](#page-160-1) and [8.22](#page-160-2) are given as:

$$\rho_i^{n+1} = \left(c_1 I e^{-I/I_0} + c_2\right) \Delta t + \rho_i^n \quad I \ge I_c$$
(8.23)

$$\rho_i^{n+1} = (f_1(\rho_i^n + \rho_*) + f_2) \Delta t + \rho_i^n \quad I < I_c$$
(8.24)

where, ρ ( *i n* + 1) is the cyanobacteria density of cell *i* at time *n* + 1, ρ<sup>∗</sup> is a correction factor to reflect the difference between the buoyant density modeled here and the non-buoyant density.

{161}------------------------------------------------

Once the new density is updated, it will be introduced into a modified Stokes's law to calculate the settling velocity *vs*(*t*):

$$v_s(t) = 2gr^2 \frac{(\rho_i - \rho_w)R}{9\phi n}$$
 (8.25)

Where *g*(*ms*−<sup>2</sup> ) is the gravity acceleration, *r*(*m*) is the cell radius for Stokes, *R* is the ratio of cell volume to colony volume, φ is the drag coefficient of a cell for Stokes, *n*(*kgm*−<sup>1</sup> *s* −1 ) is the water viscosity, and ρ*<sup>i</sup>* and ρ*<sup>w</sup>* (*kgm*−<sup>3</sup> ) are the densities of the cyanobacteria and water, respectively.

## <span id="page-161-0"></span>8.1.3.2 Algae (immobile)

[EFDC+](#page-11-0) simulates unlimited groups of algae and macrophytes and the specification of a class as mobile or immobile determines if the class is attached to the channel bottom or substrate. Macrophytes and periphyton are common immobile classes. The major difference between modeling techniques for attached and freefloating classes are as follows: (1) attached algal classes are expressed in terms of areal densities rather than volumetric concentrations, (2) the availability of nutrients to the attached classes can be influenced by stream velocity, and (3) these classes are not subject to hydrodynamic transport.

#### 8.1.3.2.1 Production of Algae (immobile)

A good description of periphyton kinetics as it relates to water quality modeling can be found in [Warwick](#page-265-16) [et al.](#page-265-16) [\(1997\)](#page-265-16) and has been used to develop the current section of this document.

A mass balance approach is used to model attached algae growth with *[C](#page-10-6)* serving as the measure of standing crop size or biomass. For each model grid cell, the equation for growth is slightly different than the one for free-floating algae (equation [8.7\)](#page-155-0):

$$P_{m} = PM_{m} \cdot min(f_{1}(N), f_{4}(V)) \cdot f_{2}(I) \cdot f_{3}(T) \cdot f_{5}(D)$$
(8.26)

where,

*PM<sup>m</sup>* is the maximum growth rate under optimal conditions for macroalgae,

*f*1(*N*) is the effect of suboptimal nutrient concentration (0 ≤ *f* <sup>1</sup> ≤ 1),

*f*2(*I*) is the effect of suboptimal light intensity (0 ≤ *f* <sup>2</sup> ≤ 1),

*f*3(*T*) is the effect of suboptimal temperature (0 ≤ *f*<sup>3</sup> ≤ 1),

*f*4(*V*) is the velocity limitation factor (0 ≤ *f*<sup>4</sup> ≤ 1), and

*f* <sup>5</sup>(*D*) is the density dependent growth rate reduction factor (0 ≤ *f*<sup>5</sup> ≤ 1).

Above a certain level, stream velocity has a stimulating effect on periphyton metabolism by mixing the overlying waters with nutrient poor waters that develop around cells [\(Whitford and Schumacher,](#page-265-17) [1964\)](#page-265-17). On the other hand, excess velocities can cause scour and loss of biomass.

The effects of suboptimal velocity upon growth rate are represented in the model by a velocity limitation function. Two options are available in the model for specifying the velocity limitation: (1) a Michaelis-Menton (or Monod) equation [8.27,](#page-162-1) and (2) a five-parameter logistic function equation [8.28.](#page-162-2) The Monod equation limits attached algae growth due to low velocities, whereas the five-parameter logistic function can be configured to limit growth due to either low or high velocities (see Figure [8.4\)](#page-162-0).

{162}------------------------------------------------

Velocity limitation option 1, the Michaelis-Menton equation is written as follows:

<span id="page-162-1"></span>
$$f_4(V) = \frac{U}{KMV + U} \tag{8.27}$$

where,

U is the stream velocity (m/s), and

*KMV* is the half-saturation velocity (m/s).

Velocity limitation option 2, the five-parameter logistic function is as follows:

<span id="page-162-2"></span>
$$f_4(V) = d + \frac{a - d}{\left[1 + \left(\frac{U}{c}\right)^b\right]^e}$$
(8.28)

where,

U is the stream velocity (m/s),

a is the asymptote at minimum x,

b is the slope after asymptote a,

c is the x-translation,

d is the asymptote at maximum x, and

<span id="page-162-0"></span>e is the slope before asymptote d.

**Fig. 8.4.** Velocity limitation function for (Option 1) the Monod equation where KMV = 0.25m/s and KMVmin = 0.15m/s, and (Option 2) the 5-parameter logistic function where a = 1.0, b = 12.0, c = 0.3, d = 0.35, and e = 3.0 (high velocities are limiting).

{163}------------------------------------------------

The half-saturation velocity in equation [8.27](#page-162-1) is the velocity at which half the maximum growth rate occurs. This effect is analogous to the nutrient limitation because at low stream velocity, the exchange of nutrients between the algal matrix and the overlying water [\(Runke,](#page-264-22) [1985\)](#page-264-22) is lower, and it increases with the increase in stream velocity. However, this formula can be too limiting at low velocities or still water. Therefore, the function is applied only at velocities above a minimum threshold level (*KMV min*). When velocities are at or below this lower level, the limitation function is applied at the minimum level. Above this velocity, the current produces a steeper diffusion gradient around the macrophytes and periphyton [\(Whitford and](#page-265-17) [Schumacher,](#page-265-17) [1964\)](#page-265-17). A minimum formulation is used to combine the limiting factors for *[N](#page-10-7)*, *[P](#page-10-8)*, velocity and the most severely limiting factor alone limits macrophytes and periphyton growth. Note that the equation [8.28](#page-162-2) can be configured so that low velocities are limiting by setting parameter *d* greater than parameter *a*, and vice versa to limit growth due to high velocities. In waters that are rich in nutrients, low velocities will not limit growth. However, high velocities may cause scouring and detachment of the macroalgae resulting in a reduction in biomass. The five-parameter logistic function can be configured to approximate this reduction by limiting growth at high velocities.

Macrophytes and periphyton growth can also be limited by the availability of suitable substrate [\(Ross and](#page-264-23) [Ultsch,](#page-264-23) [1980\)](#page-264-23). Macroalgae communities reach maximum rates of primary productivity at low levels of biomass [\(McIntire,](#page-263-17) [1973;](#page-263-17) [Pfeifer and McDiffett,](#page-263-18) [1975\)](#page-263-18). The relationship between standing crop and production employs the Michaelis-Menton kinetic equation as shown below:

<span id="page-163-0"></span>
$$f_5(D) = \frac{KBP}{KBP + MAC_m} \tag{8.29}$$

where,

*KBP* is the half-saturation biomass level (*g C*/*m* 2 ), and

*MAC<sup>m</sup>* is the macroalgae biomass level (*g C*/*m* 2 ).

The half-saturation biomass level, *KBP*, is the biomass at which half the maximum growth rate occurs. [Caupp et al.](#page-259-12) [\(1991\)](#page-259-12) used a *KBP* value of 5.0*g C*/*m* 2 (assuming 50% of ash free dry mass is *[C](#page-10-6)*) for a region of the Truckee River system in California. The function in equation [8.29](#page-163-0) allows maximum rates of primary productivity at low levels of biomass with decreasing rates of primary productivity as the community matrix expands.

#### 8.1.3.2.2 Growth and death between the cell layers

From [EFDC+](#page-11-0) 11, the kinetic of immobile or attached algae is handled to grow upwards from the bed layer through model layers. This feature provides an extension from the modeling of submerged macrophyte, which is originally attached and exists only at the bottom layer, to suspended canopy such as suspended aquaculture farms.

{164}------------------------------------------------

<span id="page-164-0"></span>Fig. 8.5. a) Macrophytes grow in vertical columns from bottom upwards and its impact on flow velocity. b) Plan view of macrophyte's impact on flow velocity

Figure [8.5a](#page-164-0) illustrates the macrophyte growing upwards from the bottom through model layers. A layered threshold value of biomass concentration is specified for the simulated macrophyte group. Growth upward is accomplished by moving the biomass of a layer to the layer above if the macrophyte concentration in the layer is greater than a threshold value and the concentration in the upper layer is less than the same threshold value. The canopy's height *HM* is calculated as:

$$HM = min\left(\frac{\sum_{K=1}^{KC} BM}{BM_{Lim}}, HM_{Max}\right)$$
(8.30)

where *HMMax* is the maximum value of the canopy's height and *BMLim* is the threshold biomass concentration.

Additionally, macrophyte shading is modeled by making light attenuation a function of macrophyte concentration.

#### 8.1.3.2.3 Macrophyte hydrodynamics impacts

Figure [8.5b](#page-164-0) illustrates the impact of macrophyte on the flow velocity. Similar to the vegetation drag described in Section [2.2.2,](#page-29-0) the resistance of flow through macrophyte is dependent on the flow velocity, macrophyte distribution and its hydrodynamic properties associated with stems and leaves. To model the additional flow resistance of macrophyte, drag of individual stems and leaves is summed to determine the total drag force in a model cell. Here, the drag force on a rigid obstacle has been introduced as a sink term in the momentum equations [\(2.2\)](#page-23-0) and [\(2.3\)](#page-23-1), and can be calculated as:

$$F_D = \rho \frac{U^2}{2} C_D \lambda \tag{8.31}$$

where *U* is the velocity averaged, *C<sup>D</sup>* is the experimental drag coefficient which corresponds to the shape and diameter of the macrophyte, λ is the stem density.

{165}------------------------------------------------

## 8.1.3.3 Zooplankton

Zooplankton are assumed to be non-mobile and are transported only by advection and dispersion. Sources and sinks of zooplankton included in the model are;

- 1. Grazing
- 2. Basal metabolism
- 3. Mortality
- 4. Predation
- 5. External loads

Each zooplankton group is represented by an identical production equation. The kinetic equation describing this process is:

$$\frac{\partial Z_z}{\partial t} = (G_z - BM_z - D_z - PR_z)Z_z + \frac{WZ_z}{V}$$
(8.32)

where,

*Z*<sup>z</sup> is the zooplankton biomass of zooplankton group z (gCm−<sup>3</sup> ),

*t* is the time (day),

*G*<sup>z</sup> is the grazing rate of zooplankton group z (day−<sup>1</sup> ),

*BM*<sup>z</sup> is the basal metabolism rate of zooplankton group z (day−<sup>1</sup> ),

*D*<sup>z</sup> is the mortality rate of zooplankton group z (day−<sup>1</sup> ),

*PR*<sup>z</sup> is the predation rate of zooplankton group z (day−<sup>1</sup> ),

*WZ*<sup>z</sup> is the external loads of zooplankton group z (gCday−<sup>1</sup> ), and

*V* is the model cell volume (m<sup>3</sup> ).

## 8.1.3.3.1 Zooplankton growth

The growth rate of zooplankton is assumed to be a function of food and temperature. Food for zooplankton includes phytoplankton and detritus as [POCs](#page-12-7). Assimilation efficiency of zooplankton is applied under the assumption that all prey grazed is assimilated.

$$G_z = \frac{PA_z}{KHC_z + PA_z}.RMAX_z.f(T)$$
(8.33)

where,

*PA<sup>z</sup>* is the prey available to zooplankton group *z* (gCm−<sup>3</sup> ),

*KHC<sup>z</sup>* is the prey density at which grazing is halved (gCm−<sup>3</sup> ),

*RMAX<sup>z</sup>* is the maximum ration of zooplankton group *z* (g prey C g−<sup>1</sup> zooplankton C day−<sup>1</sup> ), and

*f*(*T*) is the effect of temperature on grazing.

{166}------------------------------------------------

#### 1. Available prey

Zooplankton are generally assumed to graze on phytoplankton and [POC.](#page-12-7) To compute the available prey from phytoplankton for each zooplankton group, a threshold concentration *CT<sup>z</sup>* is defined below which prey is not grazed. The portion of phytoplankton group *x* as a food source for zooplankton group *z* then can be determined as:

$$BA_{xz} = Max(B_{xz} - CT_z, 0)$$

$$(8.34)$$

where,

*BAxz* is the portion of phytoplankton group *x* available to zooplankton group *z* (gCm−<sup>3</sup> ),

*CT<sup>z</sup>* is the threshold concentration of zooplankton group *z* (gCm−<sup>3</sup> )

When the model simulates several zooplankton groups such as microzooplankton and mesozooplankton, the microzooplankton becomes an important prey for the mesozooplankton. For these cases, [EFDC+](#page-11-0) allows the user to classify all the zooplankton groups into two general groups; predator and prey. A general formulation of total available prey including the food source from [POC](#page-12-7) for a zooplankton predator group is expressed as:

<span id="page-166-0"></span>
$$PA_{z} = UL_{z}.LPOCA_{z} + UR_{z}.RPOCA_{z} + \sum UB_{xz}.BA_{xz} + UZ_{z}.ZA$$
(8.35)

*PA<sup>z</sup>* is the available prey to zooplankton predator group *z* (gCm−<sup>3</sup> ),

*UL<sup>z</sup>* is the utilization of *LPOC* by zooplankton predator group *z*,

*UR<sup>z</sup>* is the utilization of *RPOC* by zooplankton predator group *z*,

*UBxz* is the utilization of phytoplankton group *x* by zooplankton predator group *z*,

*LPOCA<sup>z</sup>* is the LPOC available to the zooplankton predator group *z* (gCm−<sup>3</sup> ),

*RPOCA<sup>z</sup>* is the RPOC available to the zooplankton predator group *z* (gCm−<sup>3</sup> ),

*BAxz* is the phytoplankton group *x* available to the zooplankton predator group *z* (gCm−<sup>3</sup> ),

*ZA* is the total zooplankton prey biomass (gCm−<sup>3</sup> ), and

*UZ<sup>z</sup>* is the utilization of total zooplankton prey by zooplankton predator group *z*.

The total available prey for a zooplankton prey group can be obtained by simply removing the zooplankton prey biomass term in [8.35.](#page-166-0)

$$PA_{z} = UL_{z}.LPOCA_{z} + UR_{z}.RPOCA_{z} + \sum UB_{xz}.BA_{xz}$$
(8.36)

#### 2. Temperature effect

The effect of temperature on grazing is described as:

$$f(T) = \begin{cases} \exp(-KT_{g1} \cdot (T - T_{opt1})^2), & T \le T_{opt1} \\ 1, & T_{opt1} < T < T_{opt2} \\ \exp(-KT_{g2} \cdot (T - T_{opt2})^2), & T \ge T_{opt2} \end{cases}$$
(8.37)

where,

*KTg*<sup>1</sup> is the effect of temperature below optimal on grazing (◦C −2 ),

*KTg*<sup>2</sup> is the effect of temperature above optimal on grazing (◦C −2 ), and

*Topt* is the optimal temperature for grazing (◦C).

{167}------------------------------------------------

## 8.1.3.3.2 Basal metabolism

Basal metabolism of zooplankton is represented as an exponentially increasing function of temperature:

$$BM_z = BMR_z \cdot \exp(KTB_z \cdot (T - T_{rz})) \tag{8.38}$$

where,

*Trz* is the reference temperature for metabolism of zooplankton group *z* ( ◦C),

*BMR<sup>z</sup>* is the metabolism rate of zooplankton group *z* at temperature *Trz* (day−<sup>1</sup> ), and

*KT B<sup>z</sup>* is the effect of temperature on metabolism of zooplankton group *z* ( ◦C −1 )

### 8.1.3.3.3 Mortality

Zooplankton are subject to death at low [DO](#page-11-3) concentration. The death term is zero at a threshold [DO](#page-11-3) and increases as [DO](#page-11-3) decreases. The death rate is calculated as:

$$D_z = DZERO_z(1 - \frac{DO_{ref}}{DOCRIT_z})$$
(8.39)

where,

*Dz* is the death rate of zooplankton group *z* (day−<sup>1</sup> ),

*DZERO<sup>z</sup>* is the death rate of zooplankton group *z* at zero [DO](#page-11-3) concentration (day−<sup>1</sup> ),

*DOCRIT<sup>z</sup>* is the [DO](#page-11-3) threshold below which zooplankton death occurs (gDOm−<sup>3</sup> ), and

*DOre f* is the [DO](#page-11-3) concentration when *DO* < *DOCRIT*, otherwise zero (gDOm−<sup>3</sup> )

### 8.1.3.3.4 Predation on Zooplankton

Zooplankton can be eaten by higher level predators that are not represented in the model (e.g., jellyfish, finfish). Zooplankton predation is calculated using an exponential function of temperature as:

$$PR_z = PRR_z \cdot \exp(KTP_z \cdot (T - T_{rz}))$$
(8.40)

where,

*Trz* is the reference temperature for predation of zooplankton group *z* ( ◦C),

*PRR<sup>z</sup>* is the predation rate of zooplankton group *z* at temperature *Trz* (day−<sup>1</sup> ), and

*KT P<sup>z</sup>* is the effect of temperature on predation of zooplankton group *z* ( ◦C −1 )

#### 8.1.3.4 Organic Carbon (OC)

[EFDC+](#page-11-0) models three state variables for [OC:](#page-11-15) refractory particulate, labile particulate, and dissolved.

{168}------------------------------------------------

## 8.1.3.4.1 Particulate Organic Carbon (POC)

For [LPOC](#page-11-16) and [RPOC,](#page-12-9) sources and sinks included in the model are (Figure [8.2\)](#page-150-2);

- 1. Algal death and predation,
- 2. Zooplankton death and predation,
- 3. Uptake by zooplankton growth,
- 4. Dissolution to [DOC,](#page-11-13)
- 5. Settling, and
- 6. External loads.

The governing equations for [LPOC](#page-11-16) and [RPOC](#page-12-9) are:

<span id="page-168-0"></span>
$$\frac{\partial RPOC}{\partial t} = \sum_{algae} FCRP_x \cdot D_x \cdot B_x + \sum_{zoopl} \left( FCRDZ_z \cdot D_z + FCRPZ_z \cdot PR_z - \frac{UR_z \cdot RPOC}{PA_z} \cdot R_z \right) \cdot Z_z - K_{RPOC} \cdot RPOC + \frac{\partial}{\partial Z} \left( WS_{RP} \cdot RPOC \right) + \frac{WRPOC}{V}$$

$$(8.41)$$

<span id="page-168-1"></span>
$$\frac{\partial LPOC}{\partial t} = \sum_{algae} FCLP_x \cdot D_x \cdot B_x + \sum_{zoopl} \left( FCLDZ_z \cdot D_z + FCLPZ_z \cdot PR_z - \frac{UL_z \cdot LPOC}{PA_z} \cdot R_z \right) \cdot Z_z - \frac{UL_z \cdot LPOC}{PA_z} \cdot R_z$$

$$-K_{LPOC} \cdot LPOC + \frac{\partial}{\partial Z} \left( WS_{LP} \cdot LPOC \right) + \frac{WLPOC}{V}$$

$$(8.42)$$

where,

*RPOC* is the concentration of [RPOC](#page-12-9) (*g C*/*m* 3 ),

*LPOC* is the concentration of [LPOC](#page-11-16) (*g C*/*m* 3 ),

*D<sup>x</sup>* is the death (predated) rate of algae group *z* (day−<sup>1</sup> ),

*FCRP<sup>x</sup>* is the fraction of dead (or predated) *[C](#page-10-6)* produced as [RPOC](#page-12-9) by algal group x,

*FCLP<sup>x</sup>* is the fraction of dead (or predated) *[C](#page-10-6)* produced as [LPOC](#page-11-16) by algal group x,

*FCRDZ<sup>z</sup>* is the fraction of dead *[C](#page-10-6)* produced as [RPOC](#page-12-9) by zooplankton group z,

*FCLDZ<sup>z</sup>* is the fraction of dead *[C](#page-10-6)* produced as [LPOC](#page-11-16) by zooplankton group z,

*FCRPZ<sup>z</sup>* is the fraction of predated *[C](#page-10-6)* produced as [RPOC](#page-12-9) by zooplankton group z,

*FCLPZ<sup>z</sup>* is the fraction of predated *[C](#page-10-6)* produced as [LPOC](#page-11-16) by zooplankton group z

*UR<sup>z</sup>* is the utilization of *RPOC* by zooplankton group *z*,

*UL<sup>z</sup>* is the utilization of *LPOC* by zooplankton group *z*,

*KRPOC* is the dissolution rate of [RPOC](#page-12-9) (1/*day*),

*KLPOC* is the dissolution rate of [LPOC](#page-11-16) (1/*day*),

*WSRP* is the settling velocity of [RPOC](#page-12-9) (*m*/*day*),

{169}------------------------------------------------

 $WS_{LP}$  is the settling velocity of LPOC (m/day),

WRPOC is the external loads of RPOC (g C/day), and

WLPOC is the external loads of LPOC (g C/day.)

The rate of total C uptake by zooplankton group z is the product of the maximum ration  $R_z$  and its biomass. The ration  $R_z$  (g prey C  $g^{-1}$  zooplankton C day<sup>-1</sup>) can be calculated as:

$$R_z = \frac{PA_z}{KHC_z + PA_z}.RMAX_z.f(T)$$
(8.43)

where,

 $PA_z$  is the prey available to zooplankton group z (g C m<sup>-3</sup>),

 $KHC_z$  is the prey density at which grazing is halved (g C m<sup>-3</sup>),

 $RMAX_z$  is the maximum ration of zooplankton group z (g prey C / g zooplankton C/day)

f(T) is the effect of temperature on grazing

#### 8.1.3.4.2 Dissolved Organic Carbon (DOC)

Sources and sinks for DOC included in EFDC+ are (Figure 8.2);

- 1. Algal excretion (exudation) and death and predation,
- 2. Zooplankton predation and death,
- 3. Dissolution from LPOC and RPOC,
- 4. Heterotrophic respiration of DOC (decomposition),
- 5. Denitrification, and
- 6. External loads.

The rate of change in DOC can be calculated as:

<span id="page-169-0"></span>
$$\frac{\partial DOC}{\partial t} = \sum_{algae} \left[ FCD_x + (1 - FCD_x) \left( \frac{KHR_x}{KHR_x + DO} \right) \right] \cdot BM_x \cdot B_x + \sum_{algae} FCDP_x \cdot D_x \cdot B_x \\
+ \sum_{zoopl} \left( FCDDZ \cdot D_z + FCDPZ \cdot PR_z \right) \cdot Z_z + K_{RPOC} \cdot RPOC \\
+ K_{LPOC} \cdot LPOC - K_{HR} \cdot DOC - Denit \cdot DOC + \frac{WDOC}{V}$$
(8.44)

where,

DOC is the concentration of DOC ( $g C/m^3$ ),

 $FCD_x$  is the fraction of basal metabolism exuded as DOC at infinite DO concentration for algal group x,

 $KHR_x$  is the half-saturation constant of DO for DOC excretion by group x (g  $O_2/m^3$ ),

*DO* is the DO concentration ( $g O_2/m^3$ ),

{170}------------------------------------------------

*FCDP<sup>x</sup>* is the fraction of dead (or predated) *[C](#page-10-6)* produced as [DOC](#page-11-13) by algae group x,

*FCDDZ<sup>z</sup>* is the fraction of dead *[C](#page-10-6)* produced as [DOC](#page-11-13) by zooplankton group z,

*FCDPZ<sup>z</sup>* is the fraction of predated *[C](#page-10-6)* produced as [DOC](#page-11-13) by zooplankton group z,

*KHR* is the heterotrophic respiration rate of [DOC](#page-11-13) (1/*day*),

*Denit* is the denitrification rate (1/*day*), and

*WDOC* is the external loads of [DOC](#page-11-13) (*g C*/*day*).

The remainder of this section explains each term in equations [8.41](#page-168-0)[-8.44.](#page-169-0)

#### 8.1.3.4.3 Effect of Algae on Organic Carbon [\(OC\)](#page-11-15)

#### 8.1.3.4.3.1 Basal Metabolism

Basal metabolism, consisting of respiration and excretion, returns algal matter (*[C](#page-10-6)*, *[N](#page-10-7)*, *[P](#page-10-8)*, and *[SiO](#page-10-14)*2) back to the environment. Loss of algal biomass through basal metabolism is calculated as:

<span id="page-170-0"></span>
$$\frac{\partial B_x}{\partial t} = -BM_x B_x \tag{8.45}$$

The equation [8.45](#page-170-0) indicates that the total loss of algal biomass due to basal metabolism is independent of ambient [DO](#page-11-3) concentration. In [EFDC+,](#page-11-0) it is assumed that the distribution of total loss between respiration and excretion is constant as long as there is sufficient [DO](#page-11-3) for algae to respire. Under that condition, the losses by respiration and excretion may be written as:

<span id="page-170-1"></span>
$$(1 - FCD_x)BM_xB_x$$
: respiration (8.46)

<span id="page-170-4"></span>
$$FCD_xBM_xB_x$$
: excretion (8.47)

where, *FCD<sup>x</sup>* is a constant of value between 0 and 1.

Although the total loss of algal biomass due to basal metabolism is *[O](#page-10-11)* independent (equation [8.45\)](#page-170-0), the distribution of total loss between respiration and excretion is *[O](#page-10-11)*-dependent, as algae cannot respire in absence of *[O](#page-10-11)*. When *[O](#page-10-11)* level is high, respiration is a large fraction of the total. As [DO](#page-11-3) becomes scarce, excretion becomes dominant. Thus, equation [8.46](#page-170-1) represents the loss by respiration only at high *[O](#page-10-11)* levels. In general, equation [8.46](#page-170-1) can be decomposed into two fractions as a function of [DO](#page-11-3) availability:

<span id="page-170-2"></span>
$$(1 - FCD_x) \left(\frac{DO}{KHR_x + DO}\right) BM_x B_x$$
: respiration (8.48)

<span id="page-170-3"></span>
$$(1 - FCD_x) \left(\frac{KHR_x}{KHR_x + DO}\right) BM_x B_x : \text{ excretion}$$
 (8.49)

where, *KHR<sup>x</sup>* is the metabolic [DO](#page-11-3) coefficient (*g*/*m* <sup>3</sup> *O*2).

Equation [8.48](#page-170-2) represents the loss of algal biomass by respiration, and equation [8.49](#page-170-3) represents additional excretion due to insufficient [DO](#page-11-3) concentration. The parameter *KHRx*, which is defined as the half-saturation

{171}------------------------------------------------

constant of [DO](#page-11-3) for algal [DOC](#page-11-13) excretion in equation [8.44,](#page-169-0) can also be defined as the half-saturation constant of [DO](#page-11-3) for algal respiration in equation [8.49.](#page-170-3)

Combining equations [8.47](#page-170-4) and [8.49](#page-170-3) the total loss due to excretion can be calculated as

<span id="page-171-1"></span>
$$\left[FCD_x + (1 - FCD_x)\left(\frac{KHR_x}{KHR_x + DO}\right)\right]BM_xB_x \tag{8.50}$$

Equations [8.48](#page-170-2) and [8.50](#page-171-1) combine to give the total loss of algal biomass due to basal metabolism. The definition of the fraction *FCD<sup>x</sup>* in equation becomes apparent in equation [8.50,](#page-171-1) i.e., fraction of basal metabolism exuded as [DOC](#page-11-13) at infinite [DO](#page-11-3) concentration. At zero oxygen level, the total loss due to basal metabolism is by excretion regardless of *FCDx*.

The end *[C](#page-10-6)* product of respiration is primarily [Carbon dioxide \(](#page-10-20)*CO*2), an inorganic form not considered in the present model, while the end *[C](#page-10-6)* product of excretion is primarily [DOC.](#page-11-13) Therefore, equation [8.50,](#page-171-1) that appears in equation [8.44,](#page-169-0) represents the contribution of excretion to [DOC,](#page-11-13) and there is no source term for [POC](#page-12-7) from algal basal metabolism in equations [8.41](#page-168-0) and [8.42.](#page-168-1)

Although this general formulation is incorporated for consistency with the original CE-QUAL-IMC formulation [\(Cerco and Cole,](#page-259-8) [1995\)](#page-259-8), most of the subsequent applications of [ICM](#page-11-1) have simplified the basal metabolism in the published *DOC* and *DO* equations or specified input parameters which effectively set *KHR<sup>x</sup>* and *FCD<sup>x</sup>* to zero (see Table [8.2\)](#page-171-0), which results in simplifying the *DOC* equation to:

$$\frac{\partial DOC}{\partial t} = \sum_{algae} FCDP_x PR_x B_x + K_{RPOC} RPOC + K_{LPOC} LPOC - K_{HR} DOC - Denit DOC + \frac{WDOC}{V}$$
(8.51)

Table 8.2. Basal Metabolism Formulations and Parameter in [ICM](#page-11-1)

<span id="page-171-0"></span>

| Study                                                      | FCDx<br>and KHRx<br>in DOC Equa<br>tion                           | FCDx and KHRx<br>in from DO<br>Equation              |
|------------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------|
| Cerco<br>and<br>Cole<br>(1995)<br>(Chesa<br>peake Bay)     | General                                                           | General                                              |
| Bunch et al. (2000) (San Juan Bay,<br>PR)                  | General (used FCD = 0, KHRx =<br>0.5)                             | General (used FCD = 0, KHRx =<br>0.5)                |
| Cerco et al. (2000) (Florida Bay)                          | No BMx<br>source in equation, implies<br>FCDx<br>= 0, KHRx<br>= 0 | FCDx<br>=<br>0,<br>Consistent<br>with<br>KHRx<br>= 0 |
| Cerco et al. (2002) (Chesapeake<br>Bay, Trib. Refinements) | No BMx source in equation, im<br>plies FCDx<br>= 0, KHRx<br>= 0   | FCDx<br>=<br>0,<br>Consistent<br>with<br>KHRx<br>= 0 |
| Cerco et al. (2004) (Lake Washing<br>ton)                  | Equation implies KHRx<br>= 0 (used<br>FCDx<br>= 0)                | Consistent with KHRx<br>= 0 (used<br>FCDx<br>= 0)    |
| Tillman et al. (2004) (St.<br>Johns<br>River)              | No BMx<br>source in equation, implies<br>FCDx<br>= 0, KHRx<br>= 0 | =<br>0,<br>Consistent<br>with<br>FCDx<br>KHRx<br>= 0 |

{172}------------------------------------------------

### 8.1.3.4.3.2 Predation

Algae produce [OC](#page-11-15) through the effects of predation. Zooplankton takes up and redistributes algal *[C](#page-10-6)* through grazing, assimilation, respiration, and excretion. In case that zooplankton are not included in the model, routing of algal *[C](#page-10-6)* through zooplankton predation is simulated by empirical distribution coefficients in equations [8.41](#page-168-0) to [8.44;](#page-169-0) *FCRPx*, *FCLP<sup>x</sup>* and *FCDPx*. The sum of these three predation fractions for each algal class should be unity.

#### 8.1.3.4.4 Heterotrophic Respiration and Dissolution

The [RPOC](#page-12-9) and [LPOC](#page-11-16) equations [8.41](#page-168-0) and [8.44](#page-169-0) contain decay terms that represent dissolution of particulate material into dissolved material. These terms appear in equation [8.44](#page-169-0) as sources. The third sink term in the [DOC](#page-11-13) equation [8.44](#page-169-0) represents heterotrophic respiration of [DOC.](#page-11-13) The oxic heterotrophic respiration is a function of [DO;](#page-11-3) the lower the [DO,](#page-11-3) the smaller the respiration term becomes. Heterotrophic respiration rate, therefore, is expressed using a Monod function of [DO;](#page-11-3)

<span id="page-172-2"></span>
$$K_{HR} = \left(\frac{DO}{KHOR_{DO} + DO}\right) K_{DOC} \tag{8.52}$$

where,

*KHORDO* is the oxic respiration half-saturation constant for [DO](#page-11-3) (*g O*2/*m* 3 ), and

*KDOC* is the heterotrophic respiration rate of [DOC](#page-11-13) at infinite [DO](#page-11-3) concentration (1/*day*).

Dissolution and heterotrophic respiration rates depend on the availability of carbonaceous substrate and on heterotrophic activity. Algae produce labile *[C](#page-10-6)* that fuels heterotrophic activity; dissolution and heterotrophic respiration do not require the presence of algae though, and may be fueled entirely by external *[C](#page-10-6)* inputs. In the model, algal biomass, as a surrogate for heterotrophic activity, is incorporated into formulations of dissolution and heterotrophic respiration rates. Formulations of these rates require specification of algaldependent and algal-independent rates:

<span id="page-172-0"></span>
$$K_{RPOC} = \left(K_{RC} + K_{RCalg} \sum_{algae} B_x\right) \exp\left(KT_{HDR} \left(T - TR_{HDR}\right)\right)$$
(8.53)

<span id="page-172-3"></span>
$$K_{LPOC} = \left(K_{LC} + K_{LCalg} \sum_{algae} B_x\right) \exp\left(KT_{HDR} \left(T - TR_{HDR}\right)\right)$$
(8.54)

<span id="page-172-1"></span>
$$K_{DOC} = \left(K_{DC} + K_{DCalg} \sum_{algae} B_x\right) \exp\left(KT_{MIN} \left(T - TR_{MIN}\right)\right)$$
(8.55)

where,

*KRC* is the minimum dissolution rate of [RPOC](#page-12-9) (1/*day*),

*KLC* is the minimum dissolution rate of [LPOC](#page-11-16) (1/*day*),

*KDC* is the minimum respiration rate of [DOC](#page-11-13) (1/*day*),

{173}------------------------------------------------

 $K_{RCalg}$ ,  $K_{LCalg}$  are the constants that relate dissolution of RPOC and LPOC, respectively, to algal biomass  $(1/day; per g C/m^3)$ ,

 $K_{DCalg}$  is the constant that relates respiration to algal biomass  $(1/day \ per \ g \ C/m^3)$ ,

 $KT_{HDR}$  is the effect of temperature on the hydrolysis of Particulate Organic Matter (POM) (1/°C),

 $TR_{HDR}$  is the reference temperature for hydrolysis of POM ( ${}^{\circ}C$ ),

 $KT_{MIN}$  is the effect of temperature on mineralization of dissolved organic matter (1/°C), and

 $TR_{MIN}$  is the reference temperature for mineralization of dissolved organic matter (°C).

Equations 8.53 to 8.55 have exponential functions that relate rates to temperature.

In EFDC+, the term "hydrolysis" is defined as the process by which POM is converted to dissolved organic form, and thus includes both dissolution of particulate C and hydrolysis of particulate P and N. Therefore, the parameters  $KT_{HDR}$  and  $TR_{HDR}$ , are also used for the temperature effects on hydrolysis of particulate P (equations 8.66 and 8.67) and N (equations 8.76 and 8.77). The term "mineralization" is defined as the process by which dissolved organic matter is converted to dissolved inorganic form, and thus includes both heterotrophic respiration of DOC and mineralization of DOP and DON. Therefore, the parameters,  $KT_{MIN}$  and  $TR_{MIN}$ , are also used for the temperature effects on mineralization of dissolved P 8.68 and N 8.78.

#### <span id="page-173-1"></span>8.1.3.4.5 Effect of Denitrification on Dissolved Organic Carbon (DOC)

As O is depleted from natural systems, organic matter is oxidized by the reduction of alternate electron acceptors. Thermodynamically, the first alternate acceptor reduced in the absence of O is  $NO_3^-$ . According to Stumm et al. (1970), the reduction of  $NO_3^-$  by a large number of heterotrophic anaerobes is referred to as denitrification, and the stoichiometry of this reaction is:

<span id="page-173-2"></span>
$$4NO_3^- + 4H^+ + 5CH_2O \rightarrow 2N_2 + 7H_2O + 5CO_2$$
 (8.56)

The second last term in the equation 8.44 accounts for the effect of denitrification on DOC. The kinetics of denitrification in the model are first-order:

<span id="page-173-0"></span>
$$Denit = \left(\frac{KHOR_{DO}}{KHOR_{DO} + DO}\right) \left(\frac{NO3}{KHDN_N + NO3}\right) AANOX \cdot K_{DOC}$$
(8.57)

where,

 $KHOR_{DO}$  is the denitrification half-saturation constant for DO ( $g O/m^3$ ),

 $KHDN_N$  is the denitrification half-saturation constant for  $NO_3^-$  ( $gN/m^3$ ), and

AANOX is the ratio of denitrification rate to oxic DOC respiration rate.

In equation 8.57, the DOC respiration rate  $K_{DOC}$ , is modified so that significant decomposition via denitrification occurs only when  $NO_3^-$  is freely available and DO is depleted. The ratio AANOX, makes the anoxic respiration slower than oxic respiration. Note that  $K_{DOC}$ , defined in equation 8.55, includes the temperature effect on denitrification.

{174}------------------------------------------------

## 8.1.3.5 Phosphorus (P)

[EFDC+](#page-11-0) has four state variables for *[P](#page-10-8)*; three organic forms [\(RPOP,](#page-12-11) [LPOP,](#page-11-21) and [DOP\)](#page-11-20), and one inorganic form [\(Total Phosphate as Phosphorus \(PO4t\)\)](#page-11-23). [PO4t](#page-11-23) represents the sum of [Dissolved Phosphate as Phosphorus](#page-11-24) [\(PO4d\)](#page-11-24) and [Sorbed Phosphate as Phosphorus \(PO4p\)](#page-11-25) in the water phase, but exclude *[PO](#page-10-13)*−<sup>3</sup> 4 in algae cells.

### 8.1.3.5.1 Particulate Organic Phosphorus (POP)

For [RPOP](#page-12-11) and [LPOP,](#page-11-21) sources and sinks included in [EFDC+](#page-11-0) are (Figure [8.2\)](#page-150-2);

- 1. Algal basal metabolism, death and predation,
- 2. Zooplankton death and predation,
- 3. Uptake by zooolankton growth,
- 4. Dissolution to [DOP,](#page-11-20)
- 5. Settling, and
- 6. External loads.

The kinetic equations for [RPOP](#page-12-11) and [LPOP](#page-11-21) are;

<span id="page-174-0"></span>
$$\frac{\partial RPOP}{\partial t} = \sum_{algae} (FPR_x \cdot BM_x + FPRP_x \cdot D_x) \cdot APC \cdot B_x + \sum_{zoopl} FPRDZ_z \cdot D_z \cdot Z_z \cdot APC_z 
+ \sum_{zoopl} (FPRPZ_z \cdot PR_z - \frac{UR_z \cdot RPOP}{PA_z} \cdot R_z) \cdot Z_z \cdot APC_z 
- K_{RPOP} \cdot RPOP + \frac{\partial}{\partial Z} (WS_{RP} \cdot RPOP) + \frac{WRPOP}{V}$$
(8.58)

$$\frac{\partial LPOP}{\partial t} = \sum_{algae} (FPL_x \cdot BM_x + FPLP_x \cdot D_x) \cdot APC \cdot B_x + \sum_{zoopl} FPLDZ_z \cdot D_z \cdot Z_z \cdot APC_z 
+ \sum_{zoopl} (FPLPZ_z \cdot PR_z - \frac{UL_z \cdot LPOP}{PA_z} \cdot R_z) \cdot Z_z \cdot APC_z 
- K_{LPOP} \cdot LPOP + \frac{\partial}{\partial Z} (WS_{LP} \cdot LPOP) + \frac{WLPOP}{V}$$
(8.59)

<span id="page-174-1"></span>where,

*RPOP* is the concentration of [RPOP](#page-12-11) (*g P*/*m* 3 ),

*LPOP* is the concentration of [LPOP](#page-11-21) (*g P*/*m* 3 ),

*FPR<sup>x</sup>* is the fraction of metabolized *[P](#page-10-8)* by algal group *x* produced as [RPOP,](#page-12-11)

*FPL<sup>x</sup>* is the fraction of metabolized *[P](#page-10-8)* by algal group *x* produced as [LPOP,](#page-11-21)

*FPRP<sup>x</sup>* is the fraction of death (or predated) *[P](#page-10-8)* produced as [RPOP](#page-12-11) by algae group x,

*FPLP<sup>x</sup>* is the fraction of death (or predated) *[P](#page-10-8)* produced as [LPOP](#page-11-21) by algae group x,

{175}------------------------------------------------

*FPRDZ<sup>z</sup>* is the fraction of death *[P](#page-10-8)* produced as [RPOP](#page-12-11) by zooplankton group z,

*FPLDZ<sup>z</sup>* is the fraction of death *[P](#page-10-8)* produced as [LPOP](#page-11-21) by zooplankton group z,

*FPRPZ<sup>z</sup>* is the fraction of predated *[P](#page-10-8)* produced as [RPOP](#page-12-11) by zooplankton group z,

*FPLPZ<sup>z</sup>* is the fraction of predated *[P](#page-10-8)* produced as [LPOP](#page-11-21) by zooplankton group z,

*APC* is the mean algal *[P](#page-10-8)*-to-*[C](#page-10-6)* ratio for all algal groups (*g P per g C*),

*APC<sup>z</sup>* is the *[P](#page-10-8)*-to-*[C](#page-10-6)* ratio for zooplankton (*g P per g C*),

*KRPOP* is the hydrolysis rate of [RPOP](#page-12-11) (1/*day*),

*KLPOP* is the hydrolysis rate of [LPOP](#page-11-21) (1/*day*),

*WRPOP* is the external loads of [RPOP](#page-12-11) (*g P*/*day*), and

*WLPOP* is the external loads of [LPOP](#page-11-21) (*g P*/*day*).

## 8.1.3.5.2 Dissolved Organic Phosphorus [\(DOP\)](#page-11-20)

Sources and sinks for [DOP](#page-11-20) included in the model are (Figure [8.2\)](#page-150-2);

- 1. Algal basal metabolism, death and predation,
- 2. Zooplankton basal metabolism, death and predation,
- 3. Dissolution from [RPOP](#page-12-11) and [LPOP,](#page-11-21)
- 4. Mineralization to *[PO](#page-10-13)*−<sup>3</sup> 4 , and
- 5. External loads.

<span id="page-175-0"></span>The kinetic equation describing these processes is:

$$\frac{\partial DOP}{\partial t} = \sum_{algae} (FPD_x BM_x + FPDP_x D_x) APC B_x + \sum_{zoopl} FPDBZ_z \cdot BM_z \cdot Z_z \cdot APC_z 
+ \sum_{zoopl} (FPDDZ \cdot D_z + FPDPZ \cdot PR_z) \cdot Z_z \cdot APC_z 
+ K_{RPOP} \cdot RPOP + K_{LPOP} \cdot LPOP - K_{DOP} \cdot DOP + \frac{WDOP}{V}$$
(8.60)

where

*DOP* is the concentration of [DOP](#page-11-20) (*g P*/*m* 3 ),

*FPD<sup>x</sup>* is the fraction of metabolized *[P](#page-10-8)* produced as [DOP](#page-11-20) by algal group x,

*FPDP<sup>x</sup>* is the fraction of death (or predated) *[P](#page-10-8)* produced as [DOP](#page-11-20) by algal group x,

*FPDBZ<sup>z</sup>* is the fraction of metabolized *[P](#page-10-8)* produced as [DOP](#page-11-20) by zooplankton group z,

*FPDDZ<sup>z</sup>* is the fraction of death *[P](#page-10-8)* produced as [DOP](#page-11-20) by zooplankton group z,

*FPDPZ<sup>z</sup>* is the fraction of predated *[P](#page-10-8)* produced as [DOP](#page-11-20) by zooplankton group z,

*KDOP* is the mineralization rate of [DOP](#page-11-20) (1/*day*), and

*WDOP* is the external loads of [DOP](#page-11-20) (*g P*/*day*).

{176}------------------------------------------------

## 8.1.3.5.3 Total Water Phase Phosphate

For [PO4t](#page-11-23) that includes both [PO4d](#page-11-24) and [PO4p](#page-11-25) in the water phase, sources and sinks included in the model are;

- 1. Algal basal metabolism, predation, and uptake,
- 2. Zooplankton basal metabolism, death and predation,
- 3. Mineralization from [DOP,](#page-11-20)
- 4. Settling of *[PO](#page-10-13)*−<sup>3</sup> 4 ,
- 5. Sediment-water exchange of [PO4d](#page-11-24) for the bottom layer only, and
- 6. External loads.

<span id="page-176-0"></span>The kinetic equation describing these processes is:

$$\frac{\partial}{\partial t} (PO4p + PO4d) = \sum_{algae} (FPI_x BM_x + FPIP_x D_x - P_x) APC \cdot B_x + K_{DOP} \cdot DOP 
+ \sum_{zoopl} (FPIBZ_z \cdot BM_z + FPIDZ_z \cdot D_z + FPIPZ_z \cdot PR_z) Z_z \cdot APC_z 
+ \frac{\partial}{\partial Z} (WS_{TSS} \cdot PO4p) + \frac{BFPO4d}{\Delta Z} + \frac{WPO4p}{V} + \frac{WPO4d}{V}$$
(8.61)

where,

[PO4t](#page-11-23) is [PO4d](#page-11-24) + *[PO](#page-10-13)*−<sup>3</sup> 4 ] (*g P*/*m* 3 ),

*PO*4*d* is the dissolved phosphate as *[P](#page-10-8)* (*g P*/*m* 3 ),

*PO*4*p* is the sorbed phosphate as *[P](#page-10-8)* (*g P*/*m* 3 ),

*FPI<sup>x</sup>* is the fraction of metabolized *[P](#page-10-8)* by algal group *x* produced as inorganic *[P](#page-10-8)*,

*FPIP<sup>x</sup>* is the fraction of death (or predated) *[P](#page-10-8)* produced as inorganic *[P](#page-10-8)* by algal group x,

*FPIBZ<sup>z</sup>* is the fraction of metabolized *[P](#page-10-8)* produced as *[PO](#page-10-13)*−<sup>3</sup> 4 by zooplankton group z,

*FPIDZ<sup>z</sup>* is the fraction of *[P](#page-10-8)* produced as *[PO](#page-10-13)*−<sup>3</sup> 4 by zooplankton group z as a result of death,

*FPIPZ<sup>z</sup>* is the fraction of *[P](#page-10-8)* produced as *[PO](#page-10-13)*−<sup>3</sup> 4 by zooplankton group z as a result of predation,

*WST SS* is the settling velocity of suspended solid (*m*/*day*), provided by the hydrodynamic model,

*BFPO*4*d* is the sediment-water exchange flux of *[PO](#page-10-13)*−<sup>3</sup> 4 (*g P*/*m* <sup>2</sup>/*day*), applied to the bottom layer only, and

*WPO*4*t* is the external loads of [PO4t](#page-11-23) (*g P*/*day*).

In equation [8.61,](#page-176-0) if the [TAM](#page-12-14) is chosen as a measure of sorption site, the settling velocity of [TSS](#page-12-5) *WST SS*, is replaced by that of particulate metal *WS<sup>s</sup>* . The remainder of this section explains each term in equations [8.58](#page-174-0) to [8.61.](#page-176-0) Alternate forms of the [PO4t](#page-11-23) equation are discussed in next paragraph.

{177}------------------------------------------------

#### **8.1.3.5.4** Total Phosphate (PO4t)

Suspended and bottom sediment particles (clay, silt, and metal hydroxides) sorb and desorb  $PO_4^{-3}$  in river and estuarine waters. This sorption-desorption process buffers  $PO_4^{-3}$  concentration in the water column and enhances the transport of  $PO_4^{-3}$  away from its external sources (Carritt and Goodgal, 1954; Froelich, 1988). To ease the computational complication due to the sorption-desorption of  $PO_4^{-3}$ , PO4d and PO4p are treated and transported as a single state variable. Therefore, the model  $PO_4^{-3}$  state variable PO4t, is defined as the sum of PO4d and PO4p (equation 8.61), and the concentrations for each fraction are determined by equilibrium partitioning of their sum.

In ICM, sorption of  $PO_4^{-3}$  to particulate species of metals including Fe and Mn was considered based on a phenomenon observed in the monitoring data from the mainstem of the Chesapeake Bay, where the PO4p rapidly depleted from anoxic bottom waters during the autumn reaeration event (Cerco and Cole, 1994). Their hypothesis was that the reaeration of bottom waters caused dissolved Fe and Mn to precipitate, and  $PO_4^{-3}$  sorbed to newly formed metal particles and rapidly settled to the bottom. One state variable TAM was defined as the sum of all metals that acts as sorption sites, and the TAM was partitioned into particulate and dissolved fractions via an equilibrium partitioning coefficient. Then  $PO_4^{-3}$  was assumed to sorb to only the particulate fraction of the TAM.

In the treatment of  $PO_4^{-3}$  sorption in ICM, the particulate fraction of metal hydroxides was emphasized as a sorption site in bottom waters under anoxic conditions. Phosphorus is a highly particle-reactive element, and  $PO_4^{-3}$  in solution reacts quickly with a wide variety of surfaces, being taken up by and released from particles Froelich (1988). EFDC+ has two options, SED or TSS and TAM, as a measure of a sorption site for  $PO_4^{-3}$ , and dissolved and sorbed fractions are determined by equilibrium partitioning of their sum as a function of SED or TAM concentration:

<span id="page-177-0"></span>
$$PO4p = \left(\frac{K_{PO4p}SORPS}{1 + K_{PO4p}SORPS}\right) (PO4p + PO4d)$$

$$PO4d = \left(\frac{1}{1 + K_{PO4p}SORPS}\right) (PO4p + PO4d)$$

$$SORPS = SED \text{ or } TAM_{P}$$
(8.62)

where,

 $K_{PO4p}$  is the empirical coefficient relating  $PO_4^{-3}$  sorption to SED  $(per\ g/m^3)$  or particulate TAM  $(per\ mol/m^3)$  concentration,

SED is the total cohesive sediment concentration (mg/l), and

TAMp is the particulate TAM  $(mol/m^3)$ .

The definition of the partition coefficient alternately follows from equation 8.62 as:

$$K_{PO4_p} = \frac{PO4_p}{PO4_d} \frac{1}{SED} \tag{8.63}$$

$$K_{PO4_p} = \frac{PO4_p}{PO4_d} \, \frac{1}{TAM_p} \tag{8.64}$$

where the meaning of  $K_{PO4p}$  becomes apparent, i.e., the ratio of PO4p to PO4d per unit concentration of SED or particulate TAM (i.e., per unit sorption site available).

{178}------------------------------------------------

#### 8.1.3.5.5 Algal Phosphorus-to-Carbon Ratio (APC)

Algal biomass is quantified in units of C per volume of water. In order to express the effects of algal biomass on P and N, the ratios of P-to-C and N-to-C in algal biomass must be specified. Although global mean values of these ratios are well known (Redfield, 1963), algal composition varies especially as a function of nutrient availability. As P and N become scarce, algae adjust their composition so that smaller quantities of these vital nutrients are required to produce carbonaceous biomass (Di Toro, 1980). Examining the field data from the surface of upper Chesapeake Bay, Cerco and Cole (1993) showed that the variation of N-to-C stoichiometry was small and thus used a constant algal N-to-C ratio  $ANC_x$ . Large variations, however, were observed for algal P-to-C ratio indicating the adaptation of algae to ambient P concentration (Cerco and Cole, 1993); algal P content is high when ambient P is abundant and is low when ambient P is scarce. Thus, a variable algal P-to-C ratio APC, is used in model formulation. A mean ratio for all algal groups APC, is described by an empirical approximation to the trend observed in field data (Cerco and Cole, 1994):

<span id="page-178-1"></span>
$$APC = (CP1_{prm} + CP2_{prm} \exp(-CP3_{prm}PO4d))^{-1}$$
(8.65)

where

 $CP1_{prm}$  is the minimum C-to-P ratio (g C per g P),

 $CP2_{prm}$  is the difference between minimum and maximum C-to-P ratio (g C per g P), and

 $CP3_{prm}$  is the effect of dissolved phosphate concentration on C-to-P ratio (per  $gP/m^3$ ).

#### 8.1.3.5.6 Effect of Algae on Phosphorus

The terms within summation in equations 8.58 to 8.61 account for the effects of algae on P. Both basal metabolism (respiration and excretion) and predation are considered, and thus formulated, to contribute to organic and inorganic P. That is, the total loss by basal metabolism  $(BM_x \cdot APC \cdot B_x)$  is distributed using distribution coefficients  $(FPR_x, FPL_x, FPD_x, \text{ and } FPI_x)$ . When the model does not include zooplankton, the total loss by predation  $(PR_x \cdot APC \cdot B_x)$ , is also distributed using distribution coefficients  $(FPRP_x, FPLP_x, FPDP_x, \text{ and } FPIP_x)$ . The sum of four distribution coefficients for basal metabolism should be unity, and as is the sum for predation. Algae take up dissolved  $PO_4^{-3}$  for growth, and algae uptake of  $PO_4^{-3}$  is represented by  $(\sum P_x \cdot APC \cdot B_x)$  in equation 8.61.

#### 8.1.3.5.7 Mineralization and Hydrolysis

The third term on the RHS of equations 8.58 and 8.59 represents hydrolysis of Particulate Organic Phosphorus (POP) and the last term in equation 8.60 represents mineralization of DOP. Mineralization of organic P is mediated by the release of nucleotidase and phosphatase enzymes by bacteria Chróst and Overbeck (1987) and algae Boni et al. (1989). Since the algae themselves release the enzymes, and bacterial abundance is related to algal biomass, the rate of organic P mineralization is related to algal biomass in model formulation. This mechanism is included in the model formulation where the algae stimulate the production of an enzyme that mineralizes organic P to  $PO_4^{-3}$  when  $PO_4^{-3}$  is scarce (Boni et al., 1989; Chróst and Overbeck, 1987). The formulations for hydrolysis and mineralization rates, including these processes, are:

<span id="page-178-0"></span>
$$K_{RPOP} = \left(K_{RP} + \left(\frac{KHP}{KHP + PO4d}\right)K_{RPalg}\sum_{algae}B_{x}\right)\exp\left(KT_{HDR}\left(T - TR_{HDR}\right)\right)$$
(8.66)

{179}------------------------------------------------

<span id="page-179-0"></span>
$$K_{LPOP} = \left(K_{LP} + \left(\frac{KHP}{KHP + PO4d}\right)K_{LPalg}\sum_{alage}B_x\right)\exp\left(KT_{HDR}(T - TR_{HDR})\right)$$
(8.67)

<span id="page-179-1"></span>
$$K_{DOP} = \left(K_{DP} + \left(\frac{KHP}{KHP + PO4d}\right)K_{DPalg}\sum_{algae}B_x\right)\exp\left(KT_{MIN}\left(T - TR_{MIN}\right)\right)$$
(8.68)

where,

 $K_{RP}$  is the minimum hydrolysis rate of RPOP (1/day),

 $K_{LP}$  is the minimum hydrolysis rate of LPOP (1/day),

 $K_{DP}$  is the minimum mineralization rate of DOP (1/day),

 $K_{RPalg}$  and  $K_{LPalg}$  are the constants that relate hydrolysis of RPOP and LPOP, respectively, to algal biomass  $(1/day \ per \ g \ C/m^3)$ ,

 $K_{DPalg}$  is the constant that relates mineralization to algal biomass  $(1/day\ per\ g\ C/m^3)$ , and

KHP is the mean half-saturation constant for algal phosphorus uptake  $(g P/m^3)$ .

$$KHP = \frac{\sum_{algae} KHP_x}{number\ algae} \tag{8.69}$$

When  $PO_4^{-3}$  is abundant relative to KHP, the rates are close to the minimum values with little influence from algal biomass. When  $PO_4^{-3}$  becomes scarce relative to KHP, the rates increase with the magnitude of increase depending on algal biomass. Equations 8.66 to 8.68 have exponential functions that relate rates to temperature.

#### **8.1.3.6** Nitrogen (N)

EFDC+ has five state variables for N; three organic forms (RPON, LPON, and DON) and two inorganic forms ( $NH_4^+$  and  $NO_3^-$ ). The  $NO_3^-$  state variable in the model represents the sum of  $NO_3^-$  and  $NO_2^-$ .

#### 8.1.3.6.1 Particulate Organic Nitrogen (PON)

For RPON and LPON, sources and sinks included in the model are (Figure 8.2);

- 1. Algal basal metabolism, death and predation,
- 2. Zooplankton death and predation,
- 3. Dissolution to DON,
- 4. Settling, and
- 5. External loads.

{180}------------------------------------------------

The kinetic equations for [RPON](#page-12-10) and [LPON](#page-11-19) are:

<span id="page-180-0"></span>
$$\frac{\partial RPON}{\partial t} = \sum_{algae} (FNR_x \cdot BM_x + FNRP_x \cdot D_x) \cdot ANC_x \cdot B_x + \sum_{zoopl} FNRDZ_z \cdot D_z \cdot Z_z \cdot ANC_z 
+ \sum_{zoopl} (FNRPZ_z \cdot PR_z - \frac{UR_z \cdot RPON}{PA_z} \cdot R_z) \cdot Z_z \cdot ANC_z 
- K_{RPON}RPON + \frac{\partial}{\partial Z} (WS_{RP} \cdot RPON) + \frac{WRPON}{V}$$
(8.70)

<span id="page-180-1"></span>
$$\frac{\partial LPON}{\partial t} = \sum_{algae} (FNL_x \cdot BM_x + FNLP_x \cdot D_x) \cdot ANC_x \cdot B_x + \sum_{zoopl} FNLDZ_z \cdot D_z \cdot Z_z \cdot ANC_z 
+ \sum_{zoopl} (FNLPZ_z \cdot PR_z - \frac{UL_z \cdot LPON}{PA_z} \cdot R_z) \cdot Z_z \cdot ANC_z 
-K_{LPON}LPON + \frac{\partial}{\partial Z} (WS_{LP} \cdot LPON) + \frac{WLPON}{V}$$
(8.71)

where,

*RPON* is the concentration of [RPON](#page-12-10) (*g N*/*m* 3 ),

*LPON* is the concentration of [LPON](#page-11-19) (*g N*/*m* 3 ),

*FNR<sup>x</sup>* is the fraction of metabolized *[N](#page-10-7)* by algal group x as [RPON,](#page-12-10)

*FNL<sup>x</sup>* is the fraction of metabolized *[N](#page-10-7)* by algal group x as [LPON,](#page-11-19)

*FNRP<sup>x</sup>* is the fraction of death (or predated) *[N](#page-10-7)* produced as [RPON](#page-12-10) by algal group x,

*FNLP<sup>x</sup>* is the fraction of death (or predated) *[N](#page-10-7)* produced as [LPON](#page-11-19) by algal group x,

*FNRDZ<sup>x</sup>* is the fraction of death *[N](#page-10-7)* produced as [RPON](#page-12-10) by zooplankton group z,

*FNLDZ<sup>x</sup>* is the fraction of death *[N](#page-10-7)* produced as [LPON](#page-11-19) by zooplankton group z,

*FNRPZ<sup>x</sup>* is the fraction of predated *[N](#page-10-7)* produced as [RPON](#page-12-10) by zooplankton group z,

*FNLPZ<sup>x</sup>* is the fraction of predated *[N](#page-10-7)* produced as [LPON](#page-11-19) by zooplankton group z,

*ANC<sup>x</sup>* is the *[N](#page-10-7)*-to-*[C](#page-10-6)* ratio in algal group *x* (*g*; *N*; *per g C*),

*ANC<sup>z</sup>* is the *[N](#page-10-7)*-to-*[C](#page-10-6)* ratio in zooplankton group *z* (*g*; *N*; *per g C*),

*KRPON* is the hydrolysis rate of [RPON](#page-12-10) (1/*day*),

*KLPON* is the hydrolysis rate of [LPON](#page-11-19) (1/*day*),

*WRPON* is the external loads of [RPON](#page-12-10) (*g N*/*day*), and

*WLPON* is the external loads of [LPON](#page-11-19) (*g N*/*day*).

## 8.1.3.6.2 Dissolved Organic Nitrogen (DON)

Sources and sinks for [DON](#page-11-18) included in the model are (Figure [8.2\)](#page-150-2);

- 1. Algal basal metabolism, death and predation,
- 2. Zooplankton basal metabolism, death and predation,

{181}------------------------------------------------

- 3. Dissolution from [RPON](#page-12-10) and [LPON,](#page-11-19)
- 4. Mineralization to *[NH](#page-10-9)*<sup>+</sup> 4 , and
- 5. External loads.

<span id="page-181-1"></span>The kinetic equation describing these processes is:

$$\frac{\partial DON}{\partial t} = \sum_{algae} (FND_x BM_x + FNDP_x D_x) ANC_x B_x + \sum_{zoopl} FNDBZ_z \cdot BM_z \cdot Z_z \cdot ANC_z 
+ \sum_{zoopl} (FNDDZ \cdot D_z + FNDPZ \cdot PR_z) \cdot Z_z \cdot ANC_z 
+ K_{RPON} \cdot RPON + K_{LPON} \cdot LPON - K_{DON} \cdot DON + \frac{WDON}{V}$$
(8.72)

where,

*DON* is the concentration of [DON](#page-11-18) (*g N*/*m* 3 ),

*FND<sup>x</sup>* is the fraction of metabolized *[N](#page-10-7)* by algal group x produced as [DON,](#page-11-18)

*FNDP<sup>x</sup>* is the fraction of death (or predated) *[N](#page-10-7)* produced as [DON](#page-11-18) by algal group x,

*FNDBZ<sup>z</sup>* is the fraction of metabolized *[N](#page-10-7)* produced as [DON](#page-11-18) by zooplankton group z,

*FNDDZ<sup>z</sup>* is the fraction of death *[N](#page-10-7)* produced as [DON](#page-11-18) by zooplankton group z,

*FNDPZ<sup>z</sup>* is the fraction of predated *[N](#page-10-7)* produced as [DON](#page-11-18) by zooplankton group z,

*KDON* is the mineralization rate of [DON](#page-11-18) (1/*day*),

*WDON* is the external loads of [DON](#page-11-18) (*g N*/*day*).

#### 8.1.3.6.3 Ammonium (*NH*<sup>+</sup> 4 )

Sources and sinks for *[NH](#page-10-9)*<sup>+</sup> 4 included in the model are (Figure [8.2\)](#page-150-2):

- 1. Algal basal metabolism, death, predation, and uptake,
- 2. Zooplankton basal metabolism, death and predation,
- 3. Mineralization from [DON,](#page-11-18)
- 4. Nitrification to *[NO](#page-10-10)*<sup>−</sup> 3 ,
- 5. Sediment-water exchange for the bottom layer only, and
- 6. External loads.

<span id="page-181-0"></span>The kinetic equation describing these processes is:

$$\frac{\partial NH4}{\partial t} = \sum_{algae} (FNI_x BM_x + FNIP_x D_x - PN_x P_x) ANC_x \cdot B_x + K_{DON} \cdot DON 
+ \sum_{zoopl} (FNIBZ_z \cdot BM_z + FNIDZ_z \cdot D_z + FNIPZ_z \cdot PR_z) Z_z \cdot ANC_z 
-KNit NH4 + \frac{BFNH4}{\Delta Z} + \frac{WNH4}{V}$$
(8.73)

where,

{182}------------------------------------------------

*FNI<sup>x</sup>* is the fraction of metabolized *[N](#page-10-7)* by algal group *x* produced as inorganic *[N](#page-10-7)*,

*FNIP<sup>x</sup>* is the fraction of predated *[N](#page-10-7)* produced as inorganic *[N](#page-10-7)*,

*PN<sup>x</sup>* is the preference for *[NH](#page-10-9)*<sup>+</sup> 4 uptake by algal group *x* (0 ≤ *PN<sup>x</sup>* ≤ 1),

*FNIBZ<sup>z</sup>* is the fraction of metabolized *[N](#page-10-7)* produced as *[NH](#page-10-9)*<sup>+</sup> 4 by zooplankton group z,

*FNIDZ<sup>z</sup>* is the fraction of death *[N](#page-10-7)* produced as *[NH](#page-10-9)*<sup>+</sup> 4 by zooplankton group z,

*FNIPZ<sup>z</sup>* is the fraction of predated *[N](#page-10-7)* produced as *[NH](#page-10-9)*<sup>+</sup> 4 by zooplankton group z,

*Knit* is the nitrification rate (1/*day*) given in equation [8.80,](#page-184-0)

*BFNH*4 is the sediment-water exchange flux of *[NH](#page-10-9)*<sup>+</sup> 4 (*g N*/*m* <sup>2</sup>/*day*), applied to the bottom layer only

*WNH*4 is the external loads of *[NH](#page-10-9)*<sup>+</sup> 4 (*g N*/*day*)

#### 8.1.3.6.4 Nitrate (*NO*<sup>−</sup> 3 )

Sources and sinks for *[NO](#page-10-10)*<sup>−</sup> 3 included in the model are:

- 1. Algal uptake,
- 2. Nitrification from *[NH](#page-10-9)*<sup>+</sup> 4 ,
- 3. Denitrification to *[N](#page-10-7)* gas,
- 4. Sediment-water exchange for the bottom layer only, and
- 5. External loads.

The kinetic equation describing these processes is:

$$\frac{\partial NO3}{\partial t} = -\sum_{algae} (1 - PN_X) P_X ANC_X B_X + KNit NH4 -$$

$$ANDC Denit DOC + \frac{BFNO3}{\Delta Z} + \frac{WNO3}{V}$$
 (8.74)

where,

<span id="page-182-0"></span>*ANDC* is the mass of *[NO](#page-10-10)*<sup>−</sup> 3 reduced per mass of [DOC](#page-11-13) oxidized (0.933 *g N per g C*),

*BFNO*3 is the sediment-water exchange flux of *[NO](#page-10-10)*<sup>−</sup> 3 (*g N*/*m* <sup>2</sup>/*day*), applied to the bottom layer only, and

*WNO*3 is the external loads of *[NO](#page-10-10)*<sup>−</sup> 3 (*g N*/*day*).

The remainder of this section explains each term in equations [8.70-](#page-180-0)[8.74.](#page-182-0) It is noted that the form of the nitrification sink in [8.73](#page-181-0) and the subsequent source in the *[NO](#page-10-10)*<sup>−</sup> 3 equation [8.74](#page-182-0) differ from that in [ICM.](#page-11-1)

{183}------------------------------------------------

#### 8.1.3.6.5 Effect of Algae on Nitrogen

The terms within summation in equations 8.70 to 8.74 account for the effects of algae on N. As in P, both basal metabolism (respiration and excretion) and predation are considered, and thus formulated to contribute to ON and  $NH_4^+$ . That is, algal N released by both basal metabolism and predation are represented by distribution coefficients ( $FNR_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,  $FNL_x$ ,

Algae takes up  $NH_4^+$  and  $NO_3^-$  for growth, and  $NH_4^+$  is preferred from thermodynamic considerations. The preference of algae for  $NH_4^+$  is expressed as:

$$PN_x = NH4 \frac{NO3}{(KHN_x + NH4)(KHN_x + NO3)} + NH4 \frac{KHN_x}{(NH4 + NO3)(KHN_x + NO3)}$$
 (8.75)

This equation forces the preference for  $NH_4^+$  to be unity when  $NO_3^-$  is absent, and to be zero when  $NH_4^+$  is absent.

#### 8.1.3.6.6 Mineralization and Hydrolysis

The terms  $K_{RPON}$  and  $K_{LPON}$  on the RHS of equations 8.70 and 8.71 represent hydrolysis of the two states of Particulate Organic Nitrogen (PON) and the term of  $K_{DON}$  in equation 8.72 represents mineralization of DON. The hydrolysis and mineralization rates can be specified by the following formulations:

<span id="page-183-0"></span>
$$K_{RPON} = \left(K_{RN} + \left(\frac{KHN}{KHN + NH4 + NO3}\right)K_{RNalg}\sum_{algae}B_x\right) \exp\left(KT_{HDR}\left(T - TR_{HDR}\right)\right)$$
(8.76)

<span id="page-183-1"></span>
$$K_{LPON} = \left(K_{LN} + \left(\frac{KHN}{KHN + NH4 + NO3}\right)K_{LNalg}\sum_{algae}B_x\right) \exp\left(KT_{HDR}\left(T - TR_{HDR}\right)\right)$$
(8.77)

<span id="page-183-2"></span>
$$K_{DON} = \left(K_{DN} + \left(\frac{KHN}{KHN + NH4 + NO3}\right)K_{DNalg}\sum_{algae}B_x\right)\exp\left(KT_{MIN}\left(T - TR_{MIN}\right)\right)$$
(8.78)

where,

 $K_{RN}$  is the minimum hydrolysis rate of RPON (1/day),

 $K_{IN}$  is the minimum hydrolysis rate of LPON (1/day),

 $K_{DN}$  is the minimum mineralization rate of DON (1/day),

 $K_{RNalg}$  and  $K_{LNalg}$  are the constants that relate hydrolysis of RPON and LPON, respectively, to algal biomass  $(1/day \ per \ g \ C/m^3)$ ,

 $K_{DNalg}$  is the constant that relates mineralization to algal biomass  $(1/day \ per \ g \ C/m^3)$ , and

KHN is the mean half-saturation constant for algal N uptake  $(gN/m^3)$ .

{184}------------------------------------------------

<span id="page-184-1"></span>
$$KHN = \frac{\sum_{algae} KHN_x}{number\ of\ algae}$$
 (8.79)

Equations 8.76 to 8.78 include exponential functions that relate rates to temperature.

#### 8.1.3.6.7 Nitrification

Nitrification is a process mediated by autotrophic nitrifying bacteria that obtain energy through the oxidation of  $NH_4^+$  to  $NO_2^-$  and of  $NO_2^-$  to  $NO_3^-$ . According to Bowie et al. (1985), the stoichiometry of complete reaction is:

<span id="page-184-0"></span>
$$NH_4^+ + 2O_2 \to NO_3^- + H_2O + 2H^+$$
 (8.80)

The term of KNit in equations 8.73 and 8.74 represents the effect of nitrification on  $NH_4^+$  and  $NO_3^-$ . The kinetics of the complete nitrification process are formulated as a function of available  $NH_4^+$ , DO and temperature:

<span id="page-184-2"></span>
$$KNit \cdot NH4 = fNit \left(T\right) \left(\frac{DO}{KHNit_{DO} + DO}\right) \left(\frac{NH4}{KHNit_N + NH4}\right) Nit_m$$
 (8.81)

and

<span id="page-184-3"></span>
$$fNit(T) = \begin{cases} \exp\left(-KNit1(T - TNit)^2\right), T \le TNit \\ \exp\left(-KNit2(TNit - T)^2\right), T > TNit \end{cases}$$
(8.82)

where,

KHNit<sub>DO</sub> is the nitrification half-saturation constant for DO ( $g O_2/m^3$ ),

 $KHNit_N$  is the nitrification half-saturation constant for  $NH_4^+$  ( $gN/m^3$ ),

 $Nit_m$  is the maximum nitrification rate at TNit  $(gN/m^3/day)$ ,

*TNit* is the optimum temperature for nitrification ( ${}^{\circ}C$ ),

*KNit*1 is the effect of temperature below *TNit* on nitrification rate  $(1/^{\circ}C^{2})$ , and

*KNit2* is the effect of temperature above *TNit* on nitrification rate  $(1/^{\circ}C^{2})$ .

This follows the ICM model formulation for nitrification. The Monod function of DO in equation 8.79 indicates the inhibition of nitrification at low O level. The Monod function of  $NH_4^+$  indicates that when  $NH_4^+$  is abundant, the nitrification rate is limited by the availability of nitrifying bacteria.

In EFDC+, a reference value of KNit is input into the model instead of  $Nit_m$  by writing equation 8.81 as:

$$KNit = fNit(T) \left(\frac{DO}{KHNit_{DO} + DO}\right) \left(\frac{KHNit_{N}}{KHNit_{N} + NH4}\right) KNit_{m}$$
(8.83)

where,

{185}------------------------------------------------

$$KNit_m = \frac{Nit_m}{KHNit_N} \tag{8.84}$$

 $KNit_m$  is interpreted as the linear kinetic rate corresponding to  $KHNit_N$  equal to unity, since NH4 in this case must less than unity, and DO effects eliminated by setting  $KHNit_{DO}$  to zero. In certain applications, particularly those having long-term Biological Oxygen Demand (BOD) and nitrogen series test results,  $KNit_m$  can be observed.

#### 8.1.3.6.8 Denitrification

The effect of denitrification on DOC was described in Section 8.1.3.4.5. Denitrification removes  $NO_3^-$  from the system in stoichiometric proportion to C removal as determined by equation 8.56. The sink term in 8.74 represents this removal of  $NO_3^-$ .

#### 8.1.3.7 Silica

EFDC+ models two different forms of silica; SiP and SiA. Although the description below uses diatoms as the biota that uses  $SiO_2$ , EFDC+ allows modeler to include any number of biota groups and select the species that need  $SiO_2$  for growth.

#### **8.1.3.7.1** Particulate Biogenic Silica (SiP)

Sources and sinks for SiP included in the model are (Figure 8.2);

- 1. diatom basal metabolism, death and predation,
- 2. zooplankton death, and predation,
- 3. dissolution to available silica,
- 4. settling, and
- 5. external loads.

<span id="page-185-0"></span>The kinetic equation describing these processes is:

$$\frac{\partial SiP}{\partial t} = (FSP_d \cdot BM_d + FSPP_d \cdot D_d)ASC_d B_d + \sum_{zoopl} FSPDZ_z \cdot D_z \cdot Z \cdot ASC_z \frac{UB_d B_d}{PA_z} + \sum_{zoopl} FSPPZ_z \cdot PR_z \cdot Z_z \cdot ASC_z \frac{UB_d B_d}{PA_z} - K_{SUA} \cdot SiP + \frac{\partial}{\partial Z} (WS_d \cdot SiP) + \frac{WSiP}{V}$$
(8.85)

where,

SiP is the concentration of particulate biogenic silica ( $g Si/m^3$ ),

 $FSP_d$  is the fraction of metabolized  $SiO_2$  by diatoms produced as SiP,

 $FSPP_d$  is the fraction of death (or predated) diatom  $SiO_2$  produced as SiP,

 $FSPDZ_z$  is the fraction of predated  $SiO_2$  produced as SiP by zooplankton group z,

{186}------------------------------------------------

*FSPPZ<sup>z</sup>* is the fraction of death *[SiO](#page-10-14)*<sup>2</sup> produced as [SiP](#page-12-13) by zooplankton group z,

*ASC<sup>d</sup>* is the *[SiO](#page-10-14)*2-to-*[C](#page-10-6)* ratio of diatoms (*g Si per g C*),

*KSUA* is the dissolution rate of [SiP](#page-12-13) (1/*day*), and

*WSiP* is the external loads of [SiP](#page-12-13) (*g Si*/*day*).

### 8.1.3.7.2 Available Silica (SiA)

Sources and sinks for [SiA](#page-12-12) included in the model are;

- 1. diatom basal metabolism, death, predation, and uptake,
- 2. zooplankton basal metabolism, death and predation,
- 3. settling of sorbed (particulate) available *[SiO](#page-10-14)*2,
- 4. dissolution from [SiP,](#page-12-13)
- 5. sediment-water exchange of dissolved *[SiO](#page-10-14)*<sup>2</sup> for the bottom layer only, and
- 6. external loads.

<span id="page-186-0"></span>The kinetic equation describing these processes is:

$$\frac{\partial SiA}{\partial t} = (FSI_d BM_d + FSIP_d D_d - P_d)ASC_d B_d + K_{SUA} \cdot SiP 
+ \sum_{zoopl} (BM_z + FSADZ_z \cdot D_z + FSAPZ_z \cdot PR_z)Z_z \cdot ASC_z \cdot \frac{UB_d B_d}{PA_z} 
+ \frac{\partial}{\partial Z} (WS_{TSS}SiAp) + \frac{BFSiAd}{\Delta Z} + \frac{WSiA}{V}$$
(8.86)

where,

*SiAd* is the dissolved [SiA](#page-12-12) (*g Si*/*m* 3 ),

*SiAp* is the particulate (sorbed) [SiA](#page-12-12) (*g Si*/*m* 3 ),

*SiA* = *SiAd* +*SiAp* is the concentration of [SiA](#page-12-12) (*g Si*/*m* 3 ),

*FSI<sup>d</sup>* is the fraction of metabolized *[SiO](#page-10-14)*<sup>2</sup> by diatoms produced as [SiA,](#page-12-12)

*FSIP<sup>d</sup>* is the fraction of death (or predated) diatom *[SiO](#page-10-14)*<sup>2</sup> produced as [SiA,](#page-12-12)

*FSADZ<sup>z</sup>* is the fraction of death *[SiO](#page-10-14)*<sup>2</sup> produced as [SiA](#page-12-12) by zooplankton group z,

*FSAPZ<sup>z</sup>* is the fraction of predated *[SiO](#page-10-14)*<sup>2</sup> produced as [SiA](#page-12-12) by zooplankton group z,

*BFSAd* is the sediment-water exchange flux of [SiA](#page-12-12) (*g Si*/*m* <sup>2</sup>/*day*), applied to bottom layer only, and

*WSiA* is the external loads of [SiA](#page-12-12) (*g Si*/*day*).

In equation [8.86,](#page-186-0) if [TAM](#page-12-14) is chosen as a measure of sorption site, the settling velocity of total suspended solid *WST SS*, is replaced by that of particulate metal *WS<sup>s</sup>* .

{187}------------------------------------------------

## 8.1.3.7.3 Available Silica System

Analysis of Chesapeake Bay monitoring data indicates that silica shows similar behavior as *[PO](#page-10-13)*−<sup>3</sup> 4 in the adsorption-desorption process [\(Cerco and Cole,](#page-259-15) [1993\)](#page-259-15). As in *[PO](#page-10-13)*−<sup>3</sup> 4 , therefore, [SiA](#page-12-12) is defined to include both dissolved and sorbed fractions. Treatment of [SiA](#page-12-12) is the same as [PO4t,](#page-11-23) and the same method to partition [PO4d](#page-11-24) and *[PO](#page-10-13)*−<sup>3</sup> 4 is used to partition dissolved and sorbed [SiA.](#page-12-12)

$$SiAp = \left(\frac{K_{SiAp} SORPS}{1 + K_{SiAp} SORPS}\right) SiA \tag{8.87}$$

$$SiAd = \left(\frac{1}{1 + K_{SiAp} SORPS}\right) SiA \tag{8.88}$$

<span id="page-187-0"></span>
$$SORPS = SED \text{ or } TAM_p$$
 (8.89)

$$SiA = SiAp + SiAd (8.90)$$

where, *KSiAp* is the empirical coefficient relating [SiA](#page-12-12) sorption to SED (*per g*/*m* 3 ) or particulate [TAM](#page-12-14) (*per mol*/*m* 3 ) concentration.

#### 8.1.3.7.4 Effect of Diatoms on Silica

In equations [8.85](#page-185-0) and [8.87,](#page-187-0) those terms expressed as a function of diatom biomass (*Bd*) account for the effects of diatoms on silica. As in *[P](#page-10-8)* and *[N](#page-10-7)*, both basal metabolism (respiration and excretion) and predation are considered, and thus formulated, to contribute to [SiP](#page-12-13) and [SiA.](#page-12-12) That is, diatom silica released by both basal metabolism and predation are represented by distribution coefficients (*FSPd*, *FSId*, *FSPP*, and *FSIP*). The sum of two distribution coefficients for basal metabolism should be unity and so is that for predation. Diatoms require silica as well as *[P](#page-10-8)* and *[N](#page-10-7)*, and diatom uptake of [SiA](#page-12-12) is represented by (−*P<sup>d</sup> ASC<sup>d</sup> Bd*) in equation [8.86.](#page-186-0)

## 8.1.3.7.5 Dissolution

The term (−*KSUASiP*) in equation [8.85](#page-185-0) and its corresponding term in equation [8.86](#page-186-0) represent dissolution of [SiP](#page-12-13) to [SiA.](#page-12-12) The dissolution rate is expressed as an exponential function of temperature

<span id="page-187-1"></span>
$$K_{SUA} = K_{PSi} \exp\left(KT_{SUA} \left(T - TR_{SUA}\right)\right) \tag{8.91}$$

where,

*KSiP* is the dissolution rate of [SiP](#page-12-13) at *T RSUA* (1/*day*),

*KTSUA* is the effect of temperature on dissolution of [SiP](#page-12-13) (1/ ◦*C*), and

*T RSUA* is the reference temperature for dissolution of [SiP](#page-12-13) ( ◦*C*).

#### 8.1.3.8 Chemical Oxygen Demand (COD)

In [EFDC+,](#page-11-0) [COD](#page-10-15) is the concentration of reduced substances that are oxidizable through inorganic means. The source of [COD](#page-10-15) in saline water is *[S](#page-10-16)* − 2 released from sediments. A cycle occurs in which *[SO](#page-10-17)*−<sup>2</sup> 4 is reduced

{188}------------------------------------------------

to  $S_2^-$  in the sediments and reoxidized to  $SO_4^{-2}$  in the water column. In fresh water, Methane  $(CH_4)$  is released to the water column by the sediment process model. Both  $S_2^-$  and  $CH_4$  are quantified in units of O demand and are treated with the same kinetic formulation. The kinetic equation, including external loads, if any, is:

<span id="page-188-0"></span>
$$\frac{\partial COD}{\partial t} = -\left(\frac{DO}{KH_{COD} + DO}\right)K_{COD}COD + \frac{BFCOD}{\Delta Z} + \frac{WCOD}{V}$$
(8.92)

where,

COD is the concentration of COD (g  $O_2$  – equivalents/ $m^2$ /day),

 $KH_{COD}$  is the half-saturation constant of DO required for oxidation of COD ( $g O_2/m^3$ ),

 $K_{COD}$  is the oxidation rate of COD (1/day),

BFCO is the sediment flux of COD ( $g O_2 - equivalents/m^2/day$ ), applied to bottom layer only, and

WCOD is the external loads of COD ( $g O_2 - equivalents/day$ ).

An exponential function is used to describe the temperature effect on the oxidation rate of COD;

<span id="page-188-1"></span>
$$K_{COD} = K_{CD} \exp\left(KT_{COD}\left(T - TR_{COD}\right)\right) \tag{8.93}$$

where,

 $K_{CD}$  is the oxidation rate of COD at  $TR_{COD}$  (1/day),

 $KT_{COD}$  is the effect of temperature on oxidation of COD (1/°C), and

 $TR_{COD}$  is the reference temperature for oxidation of COD (°*C*).

#### 8.1.3.9 Dissolved Oxygen (DO)

Sources and sinks of DO in the water column included in the model are (Figure 8.2);

- 1. algal photosynthesis and respiration,
- 2. zooplankton basal metabolism,
- 3. nitrification,
- 4. heterotrophic respiration of DOC,
- 5. oxidation of COD,
- 6. surface reaeration for the surface layer only,
- 7. SOD for the bottom layer only, and
- 8. external loads.

{189}------------------------------------------------

<span id="page-189-0"></span>The kinetic equation describing these processes is:

$$\frac{\partial DO}{\partial t} = \sum_{algae} \left( (1 + 0.3(1 - PN_x)) P_x - (1 - FCD_x) \frac{DO}{KHR_x + DO} \cdot BM_x \right) AOCR B_x$$

$$-AONT Nit NH4 - AOCR K_{HR}DOC - \frac{DO}{KH_{COD} + DO} \cdot K_{COD}COD$$

$$- \sum_{zoopl} BM_z \cdot Z_z \cdot AOCR + K_R (DO_S - DO) + \frac{SOD}{\Delta Z} + \frac{WDO}{V}$$
(8.94)

where,

AONT is the mass of DO consumed per unit mass of  $NH_4^+$  as N nitrified (4.33 g  $O_2$  per g N),

AOCR is the DO-to-C ratio in respiration (2.67 g  $O_2$  per g C),

 $K_R$  is the reaeration coefficient (1/day): the reaeration term is applied to the surface layer only,

 $DO_s$  is the saturated concentration of DO  $(g O_2/m^3)$ ,

SOD is the SOD ( $g O_2/m^2/day$ ), applied to the bottom layer only; positive is to the water column,

WDO is the external loads of DO  $(g O_2/day)$ , and

 $PN_x$  is the preference for  $NH_4^+$  uptake by algae group x (0 <  $PN_x$  < 1).

The remainder of this section explains the effects of algae, nitrification, and surface reaeration.

#### 8.1.3.9.1 Dissolved Oxygen Saturation

The saturated concentration of DO can be determined based on temperature, salinity and elevation using an empirical formula in the form:

$$DO_{S} = f(T) \cdot f(S) \cdot f(z) \tag{8.95}$$

Where f(T) and f(S) indicate the dependencies of the saturated DO on temperature and salinity, which decreases as temperature and salinity increase, and f(z) is the influence of oxygen partial pressure on the saturated DO.

At sea-level, the saturated DO can be computed using several empirical formulae such as Genet et al. (1974), Garcia and Gordon (1992) and Chapra (1997).

The dependency of saturated DO on temperature according to Genet et al. (1974) is:

$$f(T) = 5.4258 \times 10^{-3} T^2 - 0.38217 \times T + 14.5532 \tag{8.96}$$

Garcia and Gordon (1992) proposed formulae based on a fit to precise data selected from the literature as:

$$\ln f(T) = 1.41575T_s^5 + 1.01567T_s^4 + 4.93845T_s^3 + 4.11890T_s^2 + 3.20684T_s + 5.80818$$
 (8.97)

$$\ln f(S) = -10^{-3} S \times \left[ 1.32412 \times 10^{-4} S^2 + (5.54491 T_s^3 + 7.93334 T_s^2 + 7.25958 T_s + 7.01211) \right]$$
(8.98)

{190}------------------------------------------------

where  $T_s$  is the scaled temperature

$$T_s = \log\left(\frac{298.15 - T}{273.15 + T}\right) \tag{8.99}$$

The saturated concentration of DO is from  $\mu mol/L$  to mg/L using a factor of  $32.0 \times 10^{-3}$ .

The fractional reductions of DO saturation due to temperature and salinity at sea-level according to Chapra (1997) are:

$$\ln f(T) = -\frac{8.621949 \times 10^{11}}{T_a^4} + \frac{1.2438 \times 10^{10}}{T_a^3} - \frac{6.642308 \times 10^7}{T_a^2} + \frac{1.575701 \times 10^5}{T_a} - 139.34411 \quad (8.100)$$

$$\ln f(S) = -S \times \left( -\frac{2140.7}{T_a^2} + \frac{10.754}{T_a} + 1.7674 \times 10^{-2} \right)$$
 (8.101)

where  $T_a$  is the absolute temperature (°K),  $T_a = T + 273.15$ .

The effect of atmospheric pressure on DO saturation at an elevation is based on the standard atmosphere as described by the cubic polynomial according to Chapra et al. (2021):

$$f(z) = 1 - 0.11988 \cdot z + 6.10834 \times 10^{-3} \cdot z^2 - 1.60747 \times 10^{-4} \cdot z^3$$
(8.102)

Zison (1978) used a linear elevation adjustment factor of

$$f(z) = 1 - 0.1148 \cdot z \tag{8.103}$$

In these formulae, z is the elevation in km.

#### 8.1.3.9.2 Effect of Algae on Dissolved Oxygen (DO)

The first line on the RHS of equation 8.94 accounts for the effects of algae on DO. Algae produces *O* through photosynthesis and consumes *O* through respiration. The quantity produced depends on the form of *N* utilized for growth. Equations describing production of DO are (Morel, 1983);

$$106CO_2 + 16NH_4^+ + H_2PO_4^- + 106H_2O \rightarrow protoplasm + 106O_2 + 15H^+$$
 (8.104)

$$106CO_2 + 16NO_3^- + H_2PO_4^- + 122H_2O \rightarrow protoplasm + 138O_2$$
 (8.105)

When  $NH_4^+$  is the N source, one mole of O is produced per mole of  $CO_2$  fixed. When  $NO_3^-$  is the N source, 1.3 moles of O are produced per mole of  $CO_2$  fixed. The quantity  $(1.3-0.3PN_x)$ , in the first term of equation 8.94 is the photosynthesis ratio and represents the molar quantity of O produced per mole of  $CO_2$  fixed. It approaches unity as the algal preference for  $NH_4^+$  approaches unity.

{191}------------------------------------------------

The last term in the first line of equation 8.94 accounts for the O consumption due to algal respiration. A simple representation of respiration process is:

$$CH_2O + O_2 \to CO_2 + H_2O$$
 (8.106)

from which,  $AOCR = 2.67 g O_2 per g C$ .

#### 8.1.3.9.3 Effect of Nitrification on Dissolved Oxygen (DO)

The stoichiometry of nitrification reaction equation 8.80, indicates that two moles of O are required to nitrify one mole of  $NH_4^+$  into  $NO_3^-$ . However, cell synthesis by nitrifying bacteria is accomplished by the fixation of  $CO_2$  so that less than two moles of oxygen are consumed per mole  $NH_4^+$  utilized (Wezenak and Gannon, 1968), i.e.  $AONT = 4.33 \, g \, O_2 \, per \, g \, N$ .

### 8.1.3.9.4 Effect of Surface Reaeration on Dissolved Oxygen (DO)

The reaeration rate of DO at the air-water interface is proportional to the O gradient across the interface  $(DO_s - DO)$ , assuming that the air is saturated with O. The term  $K_r$  on the RHS of equation 8.94 is reaeration rate which represents the reaeration process mathematically. The reaeration rate in natural waters depends on (1) water flow speed and wind speed, (2) water temperature and salinity, and (3) water depth. When wind effects are excluded, the empirical formula for the reaeration rate coefficient are based on velocity and depth:

$$K_r(20\,^{\circ}C) = A.\frac{V^B}{H^C}$$
 (8.107)

where,

 $K_r(20^{\circ}C)$  is the reaeration rate at  $20^{\circ}C$  (1/day)

V is water velocity (m/s)

H is water depth or thickness of the top layer (m)

A,B,C are empirical parameters

The effects of water temperature on the reaeration rate are expressed as:

$$K_r = K_r(20^{\circ}C)1.024^{T-20} \tag{8.108}$$

Where,

 $K_r$  is reaeration rate at  $T \circ C$ 

T is water temperature ( ${}^{\circ}C$ )

The reaeration coefficient includes the effect of turbulence generated by bottom friction (O'Connor and Dobbins, 1958) and that by surface wind stress (Banks and Herrera, 1977):

<span id="page-191-0"></span>
$$K_r = \frac{1}{\Delta z} \left( K_{ro} \sqrt{\frac{ueq}{heq}} + W_{rea} \right) \left( KT_r \right)^{T-20}$$
(8.109)

where,

{192}------------------------------------------------

Kro = 3.933 is the proportionality constant in SI units,

 $ueq = \sum (ukVk)/3(Vk)$  is the weighted velocity over cross-section (m/s),

 $heq = \sum (Vk)/B$  is the weighted depth over cross-section (m),

B is the width at the free surface (m), and

*KTr* is the constant for temperature adjustment of DO reaeration rate.

and the wind-induced reaeration Wrea (m/day) is expressed as:

$$W_{reg} = 0.728\sqrt{U_w} - 0.317U_w + 0.0372U_w^2$$
(8.110)

in which Uw is the wind speed (m/s) at the height of 10 m above surface.

The EFDC+ code provides several options for the calculation of the reaeration coefficient rate. These options varies from a constant value to complex formulas which include the effects of temperature, water and wind speed, water depth in the reaeration process.

#### 8.1.3.9.5 Simplified Equation for Dissolved Oxygen

The simplified *DO* equation for  $KHR_x$  and  $FCD_x$  equal to zero is:

$$\frac{\partial DO}{\partial t} = \sum_{algae} ((1.3 - 0.3PN_x) P_x - BM_x) AOCR B_x - AONT Nit NH4$$

$$-AOCR K_{HR} DOC - \sum_{zoopl} BM_z \cdot Z_z \cdot AOCR - \left(\frac{DO}{KH_{COD} + DO}\right) K_{COD}COD +$$

$$K_R (DO_S - DO) + \frac{SOD}{\Delta Z} + \frac{WDO}{V} \quad (8.111)$$

which is consistent with equation 8.94.

#### **8.1.3.10** Total Active Metals (TAM)

EFDC+ requires simulation of TAM for adsorption of  $PO_4^{-3}$ , and  $SiO_2$  if that option is chosen. The TAM state variable is the sum of Fe and Mn concentrations, both particulate and dissolved. The origin of TAM is benthic sediments in EFDC+. Since sediment release of metal is not explicit in the sediment model (see Chapter 6), release is specified in the kinetic portion of the water column model. The only other term included is settling of the particulate fraction. Then the kinetic equation for TAM, including external loads, if any, may be written as:

<span id="page-192-0"></span>
$$\frac{\partial TAM}{\partial t} = \left(\frac{KHbmf}{KHbmf + DO}\right) \left(\exp\left(Ktam\left(T - Ttam\right)\right)\right) \frac{BFTAM}{\Delta z} + \frac{\partial}{\partial Z} \left(WS_sTAMp\right) + \frac{WTAM}{V} \quad (8.112)$$

where,

{193}------------------------------------------------

*TAM* = *TAMd* +*TAMp* is the [TAM](#page-12-14) concentration (*mol*/*m* 3 ),

*TAMd* is the dissolved [TAM](#page-12-14) (*mol*/*m* 3 ),

*TAMp* is the particulate [TAM](#page-12-14) (*mol*/*m* 3 ),

*KHbm f* is the [DO](#page-11-3) concentration at which [TAM](#page-12-14) release is half the anoxic release rate (*g O*2/*m* 3 ),

*BFTAM* is the anoxic release rate of [TAM](#page-12-14) (*mol*/*m* <sup>2</sup>/*day*), applied to the bottom layer only,

*Ktam* is the effect of temperature on sediment release of [TAM](#page-12-14) (1/ ◦*C*),

*Ttam* is the reference temperature for sediment release of [TAM](#page-12-14) ( ◦*C*),

*WS<sup>s</sup>* is the settling velocity of particulate metal (*m*/*day*), and

*WTAM* is the external loads of [TAM](#page-12-14) (*mol*/*day*).

In estuaries, *[Fe](#page-10-18)* and *[Mn](#page-10-19)* exist in particulate and dissolved forms depending on [DO](#page-11-3) concentration. In oxygenated water, most of the *[Fe](#page-10-18)* and *[Mn](#page-10-19)* exist as particulate while under anoxic conditions, large fractions are dissolved. The partitioning between particulate and dissolved phases is expressed using a concept that [TAM](#page-12-14) concentration must achieve a minimum level, which is a function of [DO,](#page-11-3) before precipitation occurs:

<span id="page-193-0"></span>
$$TAMd = \min\left(TAM_{dmx}exp\left(-K_{dotam}\ DO\right),\ TAM\right) \tag{8.113}$$

$$TAMp = TAM - TAMd (8.114)$$

where,

*TAMdmx* is the solubility of [TAM](#page-12-14) under anoxic conditions (*mol*/*m* 3 ), and

*Kdotam* is the constant that relates [TAM](#page-12-14) solubility to [DO](#page-11-3) (*per g O*2/*m* 3 ).

#### 8.1.3.11 Fecal Coliform Bacteria

Fecal coliform bacteria are indicative of organisms from the intestinal tract of humans and other animals and can be used as an indicator bacteria as a measure of public health [\(Thomann and Mueller,](#page-265-20) [1987\)](#page-265-20). [EFDC+](#page-11-0) includes fecal coliform variable in the eutrophication module for convenience in developing [Total Maximum](#page-12-19) [Daily Load \(TMDL\)](#page-12-19) applications and is completely decoupled from the rest of the water quality model. In [EFDC+,](#page-11-0) fecal coliform bacteria have no interaction with other state variables, and have only one sink term, die-off. The kinetic equation, including external loads, may be written as:

<span id="page-193-1"></span>
$$\frac{\partial FCB}{\partial t} = KFCB \left( TFCB^{T-20} \right) FCB + \frac{WFCB}{V}$$
 (8.115)

where,

*FCB* is the bacteria concentration (*MPN per* 100*ml*),

*KFCB* is the first order die-off rate at 20 ◦*C* (1/*day*),

*T FCB* is the effect of temperature on decay of bacteria (1/ ◦*C*), and

*WFCB* is the external loads of fecal coliform bacteria (*MPN per* 100*ml m*3/*day*).

{194}------------------------------------------------

## <span id="page-194-0"></span>8.1.4 Settling, Deposition and Resuspension of Particulate Matter

The kinetic equations for particulate matter, including particulate organic matter, *[PO](#page-10-13)*−<sup>3</sup> 4 , the two *[SiO](#page-10-14)*<sup>2</sup> state variables, and [TAM](#page-12-14) contain settling term. A representative generic equation is

<span id="page-194-1"></span>
$$\frac{\partial PM}{\partial t} = \frac{\partial}{\partial z} (WS_{PM}PM) + PM_{SS}$$
(8.116)

where, *PMSS* represents the additional terms in the equation. Integration of equation [8.116](#page-194-1) over the bottom layer gives

<span id="page-194-2"></span>
$$\frac{\partial PM_1}{\partial t} = \frac{WS_{PM}}{\Delta Z_1} PM_2 - \frac{WS_{PM}}{\Delta Z_1} PM_1 + PM_{SS1}$$
(8.117)

The original [ICM](#page-11-1) and [EFDC](#page-11-2) water quality models were formulated with settling velocities representing long-term average net settling. In the subsequent application of [ICM](#page-11-1) to Florida Bay [\(Cerco et al.,](#page-259-11) [2000\)](#page-259-11), the resuspension or erosion of particulate material from the sediment bed was added and has also been added to the [EFDC+](#page-11-0) water quality model.

[EFDC+](#page-11-0) allows the use of the net settling formulation [8.117](#page-194-2) and a formulation allowing resuspension with equation [8.117](#page-194-2) modified

<span id="page-194-3"></span>
$$\frac{\partial PM_1}{\partial t} = \frac{WS_{POM}}{\Delta Z_1} PM_2 - \frac{P_{depPM}WS_{PM}}{\Delta Z_1} PM_1 + \frac{E_{PM}}{\Delta Z_1} + PM_{SS1}$$
(8.118)

to include a probability of deposition factor and an erosion term *EPM* with units of mass per unit time-unit area. For [EFDC+](#page-11-0) applications with the erosion of particulate material in the water quality module, sediment transport must be active in the hydrodynamic model. The erosion term is then defined by

$$E_{PM} = \left(\frac{PM_{bed}}{SED_{bed}}\right) \max\left(J_{ERO}, 0\right)$$
(8.119)

where,

*PMbed* is the particulate material concentration in bed (*g PM*/*m* <sup>2</sup> or *g PM*/*m* 3 ),

*SEDbed* is the concentration of finest sediment class in bed (*g PM*/*m* <sup>2</sup> or *g PM*/*m* 3 ),

*PdepPM* is the probability of deposition of the specific particulate matter variable (0 ≤ *PdepPM* ≤ 1), and

*JERO* is the mass rate of erosion or resuspension of the finest sediment class (*g SED*/*day*/*m* 2 ).

Usage of the ratio of the water quality model particulate state variable concentration to the finest sediment size class concentration rather than the total solids concentration is based on the reality that the finest sediment class (generally less than 63µ*m*) includes both inorganic and organic material and field observations of settling, deposition and resuspension, when available for model calibration, account for this. If simultaneous deposition and erosion are not permitted, the probability of deposition is defined as zero when the sediment erosion flux is greater than zero.

In conclusion, it is noted that in the [ICM](#page-11-1) documentation which includes particulate matter resuspension [\(Cerco et al.,](#page-259-11) [2000\)](#page-259-11), resuspension is explicitly included in various state variable equations, while in this document it is included implicitly as described in the current section.

{195}------------------------------------------------

#### <span id="page-195-0"></span>8.1.5 Method of Solution for Kinetics Equations

The kinetic equations for the state variables, excluding fecal coliform, in the EFDC+ water column water quality model can be expressed in a system of  $n \times n$  (where n = total number of state variables) partial differential equations in each model cell, after linearizing some terms, mostly Monod type expressions:

<span id="page-195-1"></span>
$$\frac{\partial C}{\partial t} = KC + \frac{\partial}{\partial z}(WC) + R \tag{8.120}$$

where,

C is the vector of concentration of water quality state variables in  $[ML^{-3}]$ ,

K is a matrix kinetic rate in  $[T^{-1}]$ ,

W is a vector of settling velocity in  $[LT^{-1}]$ , and

R is a vector of source/sink term in  $[ML^{-3}T^{-1}]$ .

The ordering of variables follows that in Table 8.1 which results in K being lower triangular. Integrating 8.120 over layer k, gives

<span id="page-195-3"></span><span id="page-195-2"></span>
$$\frac{C_k}{\partial t} = K \mathbf{1}_k C_k + \delta_k K \mathbf{2}_k C_{k+1} + R_k$$

$$K \mathbf{1}_k = K_k - \frac{1}{\Delta_k} W$$

$$K \mathbf{2}_k = \frac{1}{\Delta_k} W$$
(8.121)

which indicates that the settling of particulate matter from the overlying cell acts as an input for a given cell. For the layer of cells adjacent to the bed, the erosion term in 8.118 is included in the vector  $\mathbf{R}$ . The matrices and vectors in 8.120 and 8.121 are defined in Appendix A of Park et al. (1995). The layer index k increases upward with KC vertical layers; k = 1 is the bottom layer and k = KC is the surface layer. Then  $\delta_k = 0$  for k = KC; otherwise,  $\delta_k = 1$ . The matrix  $\mathbf{K}2$  is a diagonal matrix, and the non-zero elements account for the settling of particulate matter from the overlying cell.

Equation 8.121 is solved using a generalized trapezoidal scheme over a time step of  $\theta$ , which may be expressed as:

$$C_{k}^{n+1} - C_{k}^{n} = \lambda \theta \left( K 1_{k}^{n} C_{k}^{n+1} + \delta_{k} K 2_{k}^{n} C_{k+1}^{n+1} + R_{k}^{n+1} \right) + (1 - \lambda) \theta \left( K 1_{k}^{n} C_{k}^{n} + \delta_{k} K 2_{k}^{n} C_{k+1}^{n} + R_{k}^{n} \right)$$
(8.122)

or

$$(\mathbf{I} - \lambda \theta \mathbf{K} \mathbf{1}_{k}^{n}) \mathbf{C}_{k}^{n+1} = (\mathbf{I} + (1 - \lambda) \theta \mathbf{K} \mathbf{1}_{k}^{n}) \mathbf{C}_{k}^{n} + \theta \delta_{k} \mathbf{K} \mathbf{2}_{k}^{n} (\lambda \mathbf{C}_{k+1}^{n+1} + (1 - \lambda) \mathbf{C}_{k+1}^{n}) + \theta (\lambda \mathbf{R}_{k}^{n+1} + (1 - \lambda) \mathbf{R}_{k}^{n})$$
(8.123)

where,

{196}------------------------------------------------

 $\lambda$  is an implicitness factor  $(0 \le \lambda \le 1)$ ,

 $\theta = 2 \cdot m \cdot \Delta t$  is the time step for the kinetic equations and

is the identity matrix; the superscripts n and n+1 designate the variables before and after being adjusted for the relevant kinetic processes. Since equation 8.121 is solved from the surface layer downward, the term with  $C_{k+1}^{n+1}$  is known for the  $k^{th}$  layer and thus placed on the RHS. In equation 8.122, inversion of a matrix can be avoided when the 20 state variables are solved in the order given in Table 8.1.

#### <span id="page-196-0"></span>8.2. Rooted Aquatic Plants Formulation

Rooted macrophyte beds are commonly observed along the banks of many rivers. The accuracy of a water quality model may be improved by simulating submerged aquatic vegetation (epiphytic algae and rooted macrophytes) if a waterbody has documented rooted macrophyte occurrences. EFDC+'s generic Rooted Aquatic Plant and Epiphyte Algae Sub-Model (RPEM) uses kinetic mass balance equations for rooted plant shoots, roots and epiphyte algae growing on the shoots. The user may enable or disable a variety of combinations for RPEM, including enabling simulation of rooted plants or epiphytes; enabling epiphytes growing on rooted plants; enabling the RPEM – Water Column Nutrient Interaction; and enabling RPEM – Sediment Diagenesis Interaction.

The focus of this section will be on the RPEM variables and their processes. The state variables in the submodel are rooted plant shoots, roots, epiphyte algae biomass and rooted plant shoot detritus biomass. The kinetic mass balance of these variables depends mainly on production, respiration and non-respiration loss rates. These rates in turn are mainly controlled by nutrients, C, O, light field, and temperature. Parameters for RPEM sub-model are highlighted by comparing with the Florida Bay seagrass model in which Thalassia and Halodule are selected as dominant species (Madden et al., 2018).

#### <span id="page-196-1"></span>**8.2.1** State Variable Equations

The kinetic mass balance equations for rooted plant shoots, roots and epiphyte algae growing on the shoots are

$$\frac{\partial (RPS)}{\partial t} = ((1 - F_{PRPR}) \cdot P_{RPS} - R_{RPS} - L_{RPS}) RPS + JRP_{RS}$$
(8.124)

$$\frac{\partial (RPR)}{\partial t} = F_{PRPR} \cdot P_{RPS} \cdot RPS - (R_{RPR} + L_{RPR}) RPR + JRP_{RS}$$
(8.125)

$$\frac{\partial (RPE)}{\partial t} = (P_{RPE} - R_{RPE} - L_{RPE})RPE \tag{8.126}$$

where,

t is the time (day),

 $RPS(T_a, H_a)$  is the Rooted Plant Shoot Biomass  $(g C/m^2)$ ,

 $F_{PRPR}(\chi_{Ta}, \chi_{Ha})$  is the fraction of production directly transferred to roots (0 < FPGR < 1),

{197}------------------------------------------------

*PRPS* (*gTa*, *gHa*) is the production rate for plant shoots (1/*day*),

*RRPS* (*r<sup>T</sup> a*, *rHa*) is the respiration rate for plant shoots (1/*day*),

*LRPS* (*mTa*, *mHa*) is the non-respiration loss rate for plant shoots (1/*day*),

*JRPRS* (χ*T bTb*, χ*HbHb*) is the *[C](#page-10-6)* transport positive from roots to shoots (*g C*/*m* <sup>2</sup>/*day*) ,

*RPR* (*Tb*, *Hb*) is the Rooted Plant Root Biomass (*g C*/*m* 2 ),

*RRPR* (*rT b*, *rHb*) is the respiration rate for plant roots (1/*day*),

*LRPR* (*mT b*, *mHb*) is the non-respiration loss rate for plant roots (1/*day*) ,

*RPE* (*E*) is the Rooted Plant Epiphyte Biomass (*g C*/*m* 2 ),

*PRPE* (*gE*) is the production rate for epiphytes (1/*day*),

*RPRE*(*rEE*) is the respiration rate for epiphytes (1/*day*), and

*LRPE* (*rTa* +*mE*) is the non-respiration loss rate for epiphytes (1/*day*).

Equivalent notation used in the Florida Bay seagrass model appears in parentheses (), in which *T* is associated with Thalassia and *H* is associated with Halodule. For comparison, Table [8.3](#page-197-0) and Table [8.4](#page-198-0) show generic and Florida Bay seagrass model parameters.

<span id="page-197-0"></span>Table 8.3. Generic and Florida Bay Seagrass Model Parameters for Thalassia and Halodule species

| Parameter                 | Dimension      | Generic                                   | Thalassia                                | Halodule                                 |
|---------------------------|----------------|-------------------------------------------|------------------------------------------|------------------------------------------|
| FPRPR<br>(χTa, χHa)       | none           | constant                                  | 0.4                                      | 0.34                                     |
| PRPS<br>(gTa, gHa)        | 1/day          | Function of N,<br>P, Light, Temp,<br>Salt | Function of N, P,<br>Light, Temp, Salt   | Function of N, P,<br>Light, Temp, Salt   |
| RRPS<br>(rTa, rHa)        | 1/day          | Function of<br>Temp                       | 0.01 (base)<br>Temperature<br>Function   | 0.029 (base)<br>Temperature<br>Function  |
| LRPS<br>(mTa, mHa)        | 1/day          | Function of<br>Temp                       | 0.001 (base)<br>Temperature<br>Function  | 0.004 (base)<br>Temperature<br>Function  |
| RRPR<br>(rT b, rHb)       | 1/day          | Function of<br>Temp                       | 0.0025 (base)<br>Temperature<br>Function | 0.011(base)<br>Temperature<br>Function   |
| LRPR<br>(mT b, mHb)       | 1/day          | Function of<br>Temp                       | 0.0001 (base)<br>Temperature<br>Function | 0.0004 (base)<br>Temperature<br>Function |
| JRPRS<br>(χT bT b, χHbHb) | 2/day<br>g C/m | KRPRS<br>·RPR                             | χT bT b<br>(χT b<br>= 0.0005)            | χHbHb<br>= 1×10−5<br>(χHb<br>)           |

{198}------------------------------------------------

<span id="page-198-0"></span>

| Parameter                | Dimension | Generic                                             | Epiphytes                                           |
|--------------------------|-----------|-----------------------------------------------------|-----------------------------------------------------|
| $P_{RPE}(g_E)$           | none      | Function of <i>N</i> , <i>P</i> , Light, Temp, Salt | Function of <i>N</i> , <i>P</i> , Light, Temp, Salt |
| $R_{RPE}(r_E E)$         | 1/day     | Function of Temp                                    | $r_E E  r_E = 0.01 m^2 / g - day$                   |
| $L_{RPE}(m_{Ta}+m_{E}E)$ | 1/day     | constant                                            | $m_{Ta} + m_E E$ $r_E = 0.05m^2/g - day$            |

**Table 8.4.** Generic and Florida Bay Seagrass Model Parameters for Epiphytes

An additional state variable is also added to account for shoot detritus at the bottom of the water column:

$$\frac{\partial (RPD)}{\partial t} = F_{PRSD} \cdot P_{RPS} \cdot RPS - L_{RPD}RPS \tag{8.127}$$

where,

*RPD* is the Rooted Plant Shoot Detritus Biomass ( $g C/m^2$ ),

 $F_{RPSD}$  is the fraction of shoot loss to detritus (0 <  $F_{RPSD}$  < 1), and

 $L_{RPD}$  is the decay rate of detritus (1/day).

It is noted that the Florida Bay seagrass model does not include this variable.

#### **8.2.1.1** Production Rate for Plant Shoots

The production or growth rate for plant shoots is given by:

$$P_{RPS} = PM_{RPS} \cdot f_{1W}(N) \cdot f_{1B}(N) \cdot f_{2}(I) \cdot f_{3}(T) \cdot f_{4}(S) \cdot f_{5}(RPS)$$
(8.128)

where,

 $PM_{RPS}(V_T, V_H)$  is the maximum growth rate under optimal conditions for plant shoots (1/day),

 $f_1(N)$  is the effect of suboptimal nutrient concentration  $(0 \le f_1 \le 1)$ ,

 $f_2(I)$  is the effect of suboptimal light intensity  $(0 \le f_2 \le 1)$ ,

 $f_3(T)$  is the effect of suboptimal temperature  $(0 \le f_3 \le 1)$ ,

 $f_4(S)$  is the effect of salinity on fresh water plant shoot growth  $(0 \le f_4 \le 1)$ , and

 $f_5(RPS)$  is the carrying capacity effect on shoot growth  $(0 \le f_5 \le 1)$ .

The subscripts "W" and "B" indicate the water column and the bed, respectively.

<span id="page-198-1"></span>Maximum growth rates for the Florida Bay seagrass model are shown in Table 8.5.

**Table 8.5.** Maximum Growth Rate

| Parameter            | Units | Generic  | Thalassia | Halodule |
|----------------------|-------|----------|-----------|----------|
| $PM_{RPS}(V_T, V_H)$ | 1/day | constant | 0.208     | 0.29     |

{199}------------------------------------------------

## 8.2.1.1.1 Effect of Nutrients on Production

Nutrient limitation is specified in terms of both water column and bed nutrient levels by:

$$f_{1W}(N) = \min\left(\frac{(NH4 + NO3)_W}{KHN_{RPS} + (NH4 + NO3)_W}, \frac{PO4d_W}{KHP_{RPS} + PO4d_W}\right)$$

$$f_{1B}(N) = \min\left(\frac{(NH4 + NO3)_B}{KHN_{RPS} + (NH4 + NO3)_B}, \frac{PO4d_B}{KHP_{RPS} + PO4d_B}\right)$$
(8.129)

where,

*NH*4 is the *[NH](#page-10-9)*<sup>+</sup> 4 concentration as *[N](#page-10-7)* (*g N*/*m* 3 ),

*NO*3 is the *[NO](#page-10-10)*<sup>−</sup> 3 + *[NO](#page-10-12)*<sup>−</sup> 2 concentration as *[N](#page-10-7)* (*g N*/*m* 3 ),

*KHNRPS* is the half-saturation constant for *[N](#page-10-7)* uptake from water column (*g N*/*m* 3 ),

*KHNRPR* (*KT N*,*KHN*) is the half-saturation constant for *[N](#page-10-7)* uptake from bed (*g N*/*m* 3 ),

*PO*4*d* is the dissolved phosphate phosphorus concentration (*g P*/*m* 3 ),

*KHPRPS* is the half-saturation constant for phosphorus uptake from water column (*g P*/*m* 3 ), and

*KHPRPR* (*KT P*,*KHP*) is the half-saturation constant for phosphorus uptake from bed (*g P*/*m* 3 ).

<span id="page-199-0"></span>Parameter values from the Florida Bay Seagrass Model are provided in Table [8.6.](#page-199-0)

Table 8.6. List of Nutrient Limitation Parameters for the Florida Bay Seagrass Model

| Parameter | Units      | Generic  | Thalassia | Halodule |
|-----------|------------|----------|-----------|----------|
| KHNRPS    | 3<br>g N/m | constant | 0.0       | 0.0      |
| KHNRPR    | 3<br>g N/m | constant | 0.00056   | 0.00056  |
| KHPRPS    | 3<br>g P/m | constant | 0.0       | 0.0      |
| KHPRPR    | 3<br>g P/m | constant | 0.0031    | 0.0031   |
|           |            |          |           |          |

#### 8.2.1.1.2 The Light Field

The light field in the water column is governed by

<span id="page-199-1"></span>
$$\frac{\partial I}{\partial Z_*} = -K_{ess} \cdot I \tag{8.130}$$

where,

*I* is the light intensity (*Langley*/*day*),

*Kess* is the light extinction coefficient (1/*m*), and

*Z*<sup>∗</sup> is the depth below the water surface (*m*).

{200}------------------------------------------------

With the light extinction coefficient being a function of the depth below the water surface. Integration of [8.130](#page-199-1) gives

<span id="page-200-2"></span>
$$I = I_{ws} \exp\left(-\int_0^{Z_*} K_{ess} \cdot dZ_*\right)$$
(8.131)

The light intensity at the water surface *Iws*, is given by

$$I_{ws} = I_o \min\left(exp\left(-K_{eme} \cdot (H_{RPS} - H)\right), 1\right) \tag{8.132}$$

where,

*I<sup>o</sup>* is the light intensity at the top of the emergent shoot canopy for emergent shoots or the light intensity at the water surface for submerged shoots (*W*/*m* 2 ),

*Keme* is the light extinction coefficient for emergent shoots (1/*m*),

*HRPS* is the shoot height (*m*), and

*H* is the water column depth (*m*).

For submerged shoots, it is assumed that the light extinction coefficient in the water column above the shoot canopy is given by

<span id="page-200-0"></span>
$$K_{essac} = Ke_b + Ke_{TSS} \cdot TSS + Ke_{VSS} \cdot VSS + Ke_{Chl} \sum_{m=1}^{M} \left(\frac{B_m}{CChl_m}\right)$$
(8.133)

And the light extinction coefficient in the water column within the canopy is given by

<span id="page-200-1"></span>
$$K_{essic} = Ke_b + Ke_{TSS} \cdot TSS + Ke_{VSS} \cdot VSS + Ke_{Chl} \sum_{m=1}^{M} \left(\frac{B_m}{CChl_m}\right) + Ke_{RPS} \cdot RPS$$
(8.134)

where,

*Ke<sup>b</sup>* is the background light extinction (1/*m*),

*KeT SS* is the light extinction coefficient for inorganic suspended solid (1/*m per g*/*m* 3 ),

*T SS* is the total inorganic suspended solid concentration (*g*/*m* 3 ) provided from the hydrodynamic model,

*KeV SS* is the light extinction coefficient for volatile suspended solid (1/*m per g*/*m* 3 ),

*V SS* is the volatile suspended solid concentration (*g*/*m* 3 ) provided from the water quality model,

*CChlRPE* is the *[C](#page-10-6)*-to-chlorophyll ratio for epiphytes (*g C per mg Chl*),

*KeChl* is the light extinction coefficient for algae chlorophyll (1/*m per mg Chl*/*m* 3 ),

*B<sup>m</sup>* is the concentration of algae group *m* (*g C per ml*),

*CChl<sup>m</sup>* is the *[C](#page-10-6)*-to-chlorophyll ratio in algal group *m* (*g C per mg Chl*),

*KeRPS* is the light extinction coefficient for rooted plant shoots (1/*m per gm C*/*m* 2 ), and

*RPS* is the concentration of plant shoots (*g C per m*<sup>2</sup> ). 

{201}------------------------------------------------

The forms of equations [8.133](#page-200-0) and [8.134](#page-200-1) readily allow for the inclusion of algae biomass into the volatile suspended solids or vice-versa. The form of equation [8.134](#page-200-1) assumes that the shoots are primarily self shading and that epiphyte effect are manifest on the shoot surface.

The solutions of equation [8.131](#page-200-2) above and in the canopy are

<span id="page-201-0"></span>
$$I = I_{ws} \exp\left(-K_{essac} \cdot Z_*\right) \quad ; \quad 0 \le Z_* \le H - H_{RPS} \tag{8.135}$$

$$I = I_{ct} \cdot \exp\left(-K_{essic} \cdot (Z_* - H + H_{RPS})\right) \quad ; \quad H - H_{RPS} \le Z_* \le H$$

$$I_{ct} = I_{ws} \cdot \exp\left(-K_{essac} \cdot (H - H_{RPS})\right)$$
(8.136)

Since rooted plants are represented as *[C](#page-10-6)* mass per unit area, the average light intensity over the shoot canopy is an appropriate light measure. For emergent shoots, the average of equation [8.135](#page-201-0) over the water column depth, noting that *H* = *HRPS*, is

<span id="page-201-1"></span>
$$I_{icwa} = \frac{I_{ws}}{K_{essic} \cdot H} \left( 1 - \exp\left( -K_{essac} \cdot H \right) \right)$$
 (8.137)

For submerged shoots, the average over the canopy is

<span id="page-201-2"></span>
$$I_{icwa} = \frac{I_{ws}}{K_{essic} \cdot H_{RPS}} \exp\left(-K_{essac} \cdot (H - H_{RPS})\right) \cdot \left(1 - \exp\left(-K_{essic} \cdot H_{RPS}\right)\right)$$
(8.138)

where *Iicwa* in both equation [8.137](#page-201-1) and equation [8.138](#page-201-2) is the average in canopy water column light intensity.

When epiphytes grow on the shoot surface, the light intensity at the shoot surface is further reduced according to

<span id="page-201-4"></span>
$$I_{RPS} = I_{icw} \exp\left(-Ke_{RPE} \cdot RPE\right) \tag{8.139}$$

where,

*IRPS* is the light intensity on the plant shoots (*W*/*m* 2 ),

*Iicw* is the average water column light intensity in the shoot canopy (*W*/*m* 2 ), and

*KeRPE* is the light extinction coefficient for epiphyte (*m* <sup>2</sup> *per gm C*).

For the Florida Bay seagrass model, the epiphyte light extinction coefficient is given by

<span id="page-201-3"></span>
$$Ke_{RPE} = 0.11 \frac{\delta_{RPE}}{\sum_{Nspecies} \left(\frac{2 \cdot RPS \cdot \delta_{RPS}}{W_{RPS}}\right)}$$
(8.140)

where,

δ *RPE* is the epiphyte dry mass to *[C](#page-10-6)* mass ratio,

δ *RPS* is the rooted plant shoot dry mass to *[C](#page-10-6)* mass ratio, and

*WRPS* is the rooted plant shoot mass per unit shoot area.

{202}------------------------------------------------

Values of these parameters for the Florida Bay model are listed in the Table [8.7.](#page-202-0) It is noted that the expression in equation [8.140](#page-201-3) is not dimensionally homogeneous with the numerical coefficient 0.11 having implied units of (*cm*<sup>2</sup> *lea f sur f ace area* )/( *mg dry weight*). Equation [8.140](#page-201-3) can be made dimensionally consistent by use of the alternative form

$$Ke_{RPE} \cdot RPE = \frac{RPE}{\sum_{Nspecies} (KRPSE \cdot RPS)}$$
 (8.141)

<span id="page-202-0"></span>Where the dimensionless parameter *KRPSE* is also defined in Table [8.7](#page-202-0)

Table 8.7. Epiphyte Light Attenuation Parameter for Florida Bay Seagrass Model

| Parameter | Units                          | Thalassia | Halodule |
|-----------|--------------------------------|-----------|----------|
| δRPE      | Dry mass/ Carbon mass          | 9         | 9        |
| δRPS      | Dry mass/ Carbon mass          | 2.94      | 2.4      |
| WRPS      | Mg dry mass/ C-m2<br>leaf area | 1.7       | 2        |
| KRPSE     | Dimensionless                  | 3.49      | 2.42     |

Using equations [8.139](#page-201-4) and [8.135,](#page-201-0) the light intensity on the shoot surface can be expressed as

$$I_{RPS} = I_{ws} \cdot \exp\left(-K_{essac} \cdot (H - H_{RPS}) - Ke_{RPE} \cdot RPE\right) \cdot \exp\left(-K_{essic} \cdot (Z_* - H + H_{RPS})\right)$$
(8.142)

While equations [8.139](#page-201-4) and [8.138](#page-201-2) give the canopy average light intensity on the shoot surface

<span id="page-202-1"></span>
$$I_{RPSA} = \frac{I_{ws}}{K_{essic} \cdot H_{RPS}} \exp\left(-K_{essac} \cdot (H - H_{RPS}) - Ke_{RPE} \cdot RPE\right) \cdot \left(1 - \exp\left(-K_{essic} \cdot H_{RPS}\right)\right)$$
(8.143)

#### 8.2.1.1.3 Effects of Light on Growth

In the [EFDC+](#page-11-0) generic rooted plant model, the effect of light on rooted plant growth is estimated based on Steele's equation [\(Steele,](#page-264-21) [1962\)](#page-264-21)

$$f_2(I) = \frac{I}{I_{RSPopt}} \exp\left(1 - \frac{I}{I_{RSPopt}}\right)$$
(8.144)

which can be applied in terms of the average light intensity reaching the shoots to give

$$f_2(I) = \frac{I_{RPSA}}{I_{RSPopt}} \exp\left(1 - \frac{I_{RPSA}}{I_{RSPopt}}\right)$$
(8.145)

or due to its unique mathematical form directly averaged over the shoot canopy. The average is given by

$$f_{2avg}(I) = \frac{F_2}{H_{RPS}} \int_{H-H_{RPS}}^{H} \exp\left(\begin{array}{c} 1 - K_{essic} \cdot (Z_* - H + H_{RPS}) \\ -F_2 \cdot exp\left( -K_{essic} \cdot (Z_* - H + H_{RPS}) \right) \end{array}\right) dZ_*$$
 (8.146)

With the results being

{203}------------------------------------------------

$$f_{2avg}(I) = \frac{\exp(1)}{K_{essic} \cdot H_{RPS}} \left[ \exp\left(-F_2 \cdot exp\left(-K_{essic} \cdot H_{RPS}\right)\right) - \exp\left(F_2\right) \right]$$
(8.147)

$$F_2 = \frac{I_{ws}}{I_{RSPopt}} \cdot \exp\left(-K_{essac} \cdot (H - H_{RPS}) - Ke_{RPE} \cdot RPE\right)$$
(8.148)

## 8.2.1.1.4 Effect of Temperature on Shoot Growth

The effect of temperature on shoot growth is given by a Gaussian function

$$f_{3}(T) = \begin{cases} \exp\left(-KTP1_{RPS}[T - TP1_{RPS}]^{2}\right) & \text{if } T \leq TP1_{RPS} \\ 1 & \text{if } TP1_{RPS} < T < TP2_{RPS} \\ \exp\left(-KTP2_{RPS}[T - TP2_{RPS}]^{2}\right) & \text{if } T \geq TP1_{RPS} \end{cases}$$
(8.149)

where,

*T* is the temperature (◦*C*) provided from the hydrodynamic model,

*T P*1*RPS* < *T* < *T P*2*RPS* is the optimal temperature range for shoot production (◦*C*),

*KT P*1*RPS* is the effect of temperature below *T P*1*RPS* on shoot production (1/◦*C* 2 ), and

*KT P*2*RPS* is the effect of temperature above *T P*2*RPS* on shoot production (1/◦*C* 2 ).

or an exponential function.

<span id="page-203-1"></span>
$$f_3(T) = \exp(KTP_{RPS}[T - TPREF_{RPS}])$$
(8.150)

where,

*T PREFRPS* is the reference temperature for shoot production (◦*C*), and *KT PRPS* is the effect of temperature on shoot production (1/ ◦*C*).

<span id="page-203-0"></span>The parameters for the Florida Bay seagrass model given in Table [8.8.](#page-203-0)

Table 8.8. Parameters for Temperature Effect on Growth for Equation [8.150](#page-203-1)

| Parameter | Units | Thalassia | Halodule |
|-----------|-------|-----------|----------|
| T PREFRPS | ◦C    | 28        | 31       |
| KT PRPS   | 1/◦C  | 0.07      | 0.07     |

#### 8.2.1.1.5 Effect of Salinity

The effect of salinity on fresh water plant shoot growth is given by

$$f_4(S) = \frac{STOXS^2}{STOXS^2 + S^2}$$
 (8.151)

where,

{204}------------------------------------------------

*STOXS* is the salinity at which growth is halved (*ppt*), and

*S* is the salinity in water column (*ppt*) provided from the hydrodynamic model

#### 8.2.1.1.6 Effect of Rooted Plant Density

The effect of rooted plant density on growth is given by

<span id="page-204-1"></span>
$$f_5(RPS) = 1 - \left(\sum_{species} \frac{RPS}{RPS_{sat}}\right)^2$$
(8.152)

where *RPSsat* is the density saturation parameter (*g C*/*m* 2 ).

<span id="page-204-0"></span>The summation indicates when multiple species are simulated, the total density of all species affects each individual species

Table 8.9. Parameters for Plant Density Effect on Growth for Equation [8.152](#page-204-1)

| Parameter | Units            | Thalassia | Halodule |
|-----------|------------------|-----------|----------|
| RPSsat    | 2<br>(g C/m<br>) | 400       | 667      |

## 8.2.1.2 Respiration Rate for Plant Shoots

The respiration rate for plant shoots is assumed to be temperature dependent

$$R_{RPS} = RREF_{RPS} \cdot \exp\left(KTR_{RPS}\left[T - TRREF_{RPS}\right]\right) \tag{8.153}$$

where,

*RREFRPS* is the reference respiration rate for shoots (1/*day*),

*T* is the temperature (◦*C*) provided from the hydrodynamic model,

*T RREFRPS* is the reference temperature for shoot respiration (◦*C*), and

<span id="page-204-2"></span>*KT RRPS* is the effect of temperature on shoot respiration (1/◦*C* 2 ).

Table 8.10. Parameters for Shoot Respiration in the Florida seagrass model

| Parameter | Units         | Thalassia | Halodule |
|-----------|---------------|-----------|----------|
| RREFRPS   | 1/day         | 0.01      | 0.029    |
| KT RRPS   | dimensionless | 0.07      | 0.07     |
| T RREFRPS | ◦C            | 28        | 31       |

{205}------------------------------------------------

## 8.2.1.3 Non-Respiration Loss Rate for Plant Shoots

The non-respiration loss rate for shoots is assumed to be temperature dependent.

$$L_{RPS} = LREF_{RPS} \cdot \exp\left(KTL_{RPS}\left[T - TLREF_{RPS}\right]\right) \tag{8.154}$$

where,

*LREFRPS* is the reference loss rate for shoots (1/*day*),

*T* is the temperature (◦*C*) provided from the hydrodynamic model,

*T LREFRPS* is the reference temperature for shoot loss (◦*C*), and

*KT LRPS* is the effect of temperature on shoot loss (1/◦*C* 2 ).

<span id="page-205-0"></span>Table 8.11. Parameters for Shoot Mortality of non-respiration loss in the Florida seagrass model

| Parameter | Units         | Thalassia | Halodule |
|-----------|---------------|-----------|----------|
| LREFRPS   | 1/day         | 0.001     | 0.004    |
| KLRRPS    | dimensionless | 0.07      | 0.07     |
| T LREFRPS | ◦C            | 28        | 28       |

### 8.2.1.4 Carbon Transport from Roots to Shoots

The *[C](#page-10-6)* transport from roots to shoots is defined as positive to the shoots. Two formulations can be utilized; the first is based on observed shoot to root biomass ratios

$$JRP_{RS} = KRPO_{RS} \cdot (RPR - RORS \cdot RPS)$$
(8.155)

$$RORS = \frac{RPR_{obs}}{RPS_{obs}} \tag{8.156}$$

where,

*KRPORS* is the root to shoot transfer rate to follow observed ratio (1/*day*), and

*RORS* is the observed ratio of root *[C](#page-10-6)* to shoot *[C](#page-10-6)* (dimensionless).

and the second formulation transfers root *[C](#page-10-6)* to shoot *[C](#page-10-6)* under unfavorable light conditions for the shoots

<span id="page-205-1"></span>
$$JRP_{RS} = KRP_{RS} \left( \frac{I_{SS}}{I_{SS} + I_{SSS}} \right) RPR$$
(8.157)

where,

*KRPRS* (χ*T b*,χ*Hb*) is the root to shoot transfer rate (1/*day*),

*ISS* is the solar ratio at shoot surface (*W*/*m* 2 ),

{206}------------------------------------------------

<span id="page-206-0"></span>*ISSS* is the half-saturation solar ratio at shoot surface (*W*/*m* 2 ).

Table 8.12. Root to Shoot Transport Parameters in Equation [8.157](#page-205-1)

| Parameter | Dimension     | Generic  | Thalassia | Halodule |
|-----------|---------------|----------|-----------|----------|
| KRPORS    | 1/day         | constant | 5E-4      | 1E-5     |
| RORS      | dimensionless | constant | 0.0       | 0.0      |
| KRPRS     | 1/day         | constant | 5E-4      | 1E-5     |
| ISSS      | 2<br>W/m      | constant | 0.0       | 0.0      |

#### 8.2.1.5 Respiration Rate for Plant Roots

The respiration rate for plant roots is assumed to be temperature dependent

<span id="page-206-2"></span>
$$R_{RPR} = RREF_{RPR} \cdot \exp\left(KTR_{RPR}\left[T - TRREF_{RPR}\right]\right) \tag{8.158}$$

where,

*RREFRPR* is the reference respiration rate for roots (1/*day*),

*T* is the temperature (◦*C*) provided from the hydrodynamic model,

*T RREFRPR* is the reference temperature for root respiration (◦*C*), and

<span id="page-206-1"></span>*KT RRPR* is the effect of temperature on shoot respiration (1/◦C 2 ).

Table 8.13. Parameters for Root Respiration in Equation [8.158](#page-206-2)

| Parameter | Units         | Thalassia | Halodule |
|-----------|---------------|-----------|----------|
| RREFRPR   | 1/day         | 0.0025    | 0.011    |
| KT RRPR   | dimensionless | 0.07      | 0.07     |
| T RREFRPR | ◦C            | 28        | 31       |

#### 8.2.1.6 Non-Respiration Loss Rate for Plant Roots

<span id="page-206-3"></span>The non-respiration loss rate for shoots is assumed to be temperature dependent.

<span id="page-206-4"></span>
$$L_{RPR} = LREF_{RPR} \cdot \exp\left(KTL_{RPR}\left[T - TLREF_{RPR}\right]\right) \tag{8.159}$$

Table 8.14. Parameters for Root Mortality in Equation [8.159](#page-206-4)

| Parameter | Units         | Thalassia | Halodule |
|-----------|---------------|-----------|----------|
| LREFRPR   | 1/day         | 1E-4      | 4E-4     |
| KLRRPR    | dimensionless | 0.07      | 0.07     |
| T LREFRPR | ◦C            | 28        | 28       |

{207}------------------------------------------------

## 8.2.1.7 Production Rate for Epiphytes

The production or growth rate for epiphytes on plant shoots is given by

$$P_{RPE} = PM_{RPE} \cdot f_W(N) \cdot f_2(I) \cdot f_3(T) \cdot f_4(RPE, RPS)$$
(8.160)

where ,

*PMRPE* is the maximum growth rate under optimal conditions for plant shoots (1/*day*),

*f* <sup>1</sup>(*N*) is the effect of suboptimal nutrient concentration (0≤*f* <sup>1</sup>≤1),

*f* <sup>2</sup>(*I*) is the effect of suboptimal light intensity (0≤*f* <sup>2</sup>≤1),

*f* <sup>3</sup>(*T*) is the effect of suboptimal temperature (0≤*f* <sup>3</sup>≤1), and

*f* <sup>4</sup>(*RPE*,*RPS*) is the effect of epiphyte and host rooted density (0 ≤ *f*<sup>4</sup> ≤ 1).

#### 8.2.1.7.1 Effect of Nutrients on Epiphyte Growth

Nutrient limitation for epiphytes is given by

$$f_1(N) = \min\left(\frac{NH4 + NO3}{KHN_{RPE} + NH4 + NO3}, \frac{PO4d}{KHP_{RPE} + PO4d}\right)$$
 (8.161)

where,

*NH*4 is the *[NH](#page-10-9)*<sup>+</sup> 4 concentration as *[N](#page-10-7)* (*g N*/*m* 3 ),

*NO*3 is the *[NO](#page-10-10)*<sup>−</sup> 3 + *[NO](#page-10-12)*<sup>−</sup> 2 concentration as *[N](#page-10-7)* (*g N*/*m* 3 ),

*KHNRPE* is the half-saturation constant for *[N](#page-10-7)* uptake for epiphytes (*g N*/*m* 3 ),

*PO*4*d* is the dissolved *[PO](#page-10-13)*−<sup>3</sup> 4 concentration as *[P](#page-10-8)* (*g P*/*m* 3 ), and

*KHPRPE* is the half-saturation constant for *[P](#page-10-8)* uptake for epiphytes (*g P*/*m* 3 ).

#### 8.2.1.7.2 Effect of Light on Epiphyte Growth

Light limitation for epiphyte growth is based on a Monod type equation (e.g., [Bunch et al.,](#page-258-13) [2000\)](#page-258-13):

<span id="page-207-0"></span>
$$f_2(I) = \left(\frac{I_{RPE}}{I_{RPE} + KHI_{RPE}}\right) \tag{8.162}$$

where,

*KHIRPE* is the half-saturation constant for epiphyte light limitation (*W*/*m* 2 ).

The average light intensity over the shoot canopy

$$I_{RPEA} = \frac{I_{ws}}{K_{essic} \cdot H_{RPS}} \exp\left(-K_{essac} \cdot (H - H_{RPS})\right) \cdot \left(1 - \exp\left(-K_{essic} \cdot H_{RPS}\right)\right)$$
(8.163)

{208}------------------------------------------------

which follows from equation [8.143](#page-202-1) with *KeRPE* = 0. Equation [8.162](#page-207-0) can be averaged over the shoot canopy to give

$$f_{2avg}(I) = \frac{1}{K_{essic} \cdot H_{RSP}} \ln \left( \frac{KHI_{RPE} + I_{ct}exp\left( -K_{essic} \cdot (H - H_{RSP}) \right)}{KHI_{RPE} + I_{ct}exp\left( -K_{essic} \cdot H \right)} \right)$$
(8.164)

$$I_{ct} = I_{ws} \cdot \exp\left(-K_{essic} \cdot (H - H_{RSP})\right) \tag{8.165}$$

## 8.2.1.7.3 Effect of Temperature on Epiphyte Growth

The effect of temperature on epiphyte growth is given by

$$f_3(T) = \begin{cases} \exp(-KTP1_{RPE}[T - TP1_{RPE}]^2), & T \le TP1_{RPE} \\ 1, & TP1_{RPE} < T < TP2_{RPE} \\ \exp(-KTP2_{RPE}[T - TP2_{RPE}]^2), & T \ge TP1_{RPE} \end{cases}$$
(8.166)

where,

*T* is the temperature (◦*C*) provided from the hydrodynamic model,

*T P*1*RPE* < *T* < *T P*2*RPE* is the optimal temperature range for epiphyte production (◦*C*),

*KT P*1*RPE* is the effect of temperature below *T P*1*RPE* on epiphyte production (1/◦*C* 2 ), and

*KT P*2*RPE* is the effect of temperature above *T P*2*RPE* on epiphyte production (1/◦*C* 2 )

#### 8.2.1.7.4 Effect of Epiphyte and Rooted Plant Density on Epiphyte Growth

The effect of rooted plant density on growth is given by

$$f_4(RPE, RPS) = 1 - \left(\frac{RPE \cdot \delta_{RPE}}{W_{RPE} \sum_{Nspecies} \left(\frac{2 \cdot RPS \cdot \delta_{RPS}}{W_{RPS}}\right)}\right)^2$$
(8.167)

where

δ*RPE* is the Epiphyte dry mass to *[C](#page-10-6)* mass ratio

*WRPE* is the maximum epiphyte mass per unit shoot area

#### 8.2.1.8 Respiration Rate for Epiphytes

The respiration rate for epiphytes is assumed to be temperature dependent:

$$R_{RPE} = RREF_{RPE} \cdot \exp\left(KTR_{RPE} \left[T - TRREF_{RPE}\right]^2\right)$$
(8.168)

where,

{209}------------------------------------------------

*RREFRPE* is the reference respiration rate for epiphytes (1/*day*),

*T* is the temperature (◦*C*) provided from the hydrodynamic model,

*T RREFRPE* is the reference temperature for epiphytes respiration (◦*C*), and

*KT RRPE* is the effect of temperature on epiphytes respiration (1/◦*C* 2 ).

### 8.2.1.9 Coupling with Organic Carbon (OC)

The interaction between rooted plants and epiphytes and water column (W) and bed [OC](#page-11-15) species is given by:

$$\frac{\partial RPOC_W}{\partial t} = \frac{1}{H} \left( FCR_{RPS} \cdot R_{RPS} + (1 - F_{RPSD}) \cdot FCRL_{RPS} \cdot L_{RPS} \right) RPS 
+ \frac{1}{H} \left( FCR_{RPE} \cdot R_{RPE} + FCRL_{RPE} \cdot L_{RPE} \right) RPE + \frac{1}{H} FCRL_{RPD} \cdot L_{RPD} \cdot RPD \quad (8.169)$$

$$\frac{\partial RPOC_B}{\partial t} = \frac{1}{B} \left( FCR_{RPR} \cdot R_{RPR} + FCRL_{RPR} \cdot L_{RPR} \right) RPR \tag{8.170}$$

$$\frac{\partial LPOC_W}{\partial t} = \frac{1}{H} \left( FCL_{RPS} \cdot R_{RPS} + (1 - F_{RPSD}) \cdot FCLL_{RPS} \cdot L_{RPS} \right) RPS 
+ \frac{1}{H} \left( FCL_{RPE} \cdot R_{RPE} + FCLL_{RPE} \cdot L_{RPE} \right) RPE + \frac{1}{H} FCLL_{RPD} \cdot L_{RPD} \cdot RPD \quad (8.171)$$

$$\frac{\partial LPOC_B}{\partial t} = \frac{1}{B} \left( FCL_{RPR} \cdot R_{RPR} + FCLL_{RPR} \cdot L_{RPR} \right) RPR \tag{8.172}$$

$$\frac{\partial DOC_W}{\partial t} = \frac{1}{H} \left( FCD_{RPS} \cdot R_{RPS} + (1 - F_{RPSD}) \cdot FCDL_{RPS} \cdot L_{RPS} \right) RPS 
+ \frac{1}{H} \left( FCD_{RPE} \cdot R_{RPE} + FCDL_{RPE} \cdot L_{RPE} \right) RPE + \frac{1}{H} FCDL_{RPD} \cdot L_{RPD} \cdot RPD \quad (8.173)$$

$$\frac{\partial DOC_B}{\partial t} = \frac{1}{B} \left( FCD_{RPR} \cdot R_{RPR} + FCDL_{RPR} \cdot L_{RPR} \right) RPR \tag{8.174}$$

where,

*RPOC* is the concentration of [RPOC](#page-12-9) (*g C*/*m* 3 ),

*LPOC* is the concentration of [LPOC](#page-11-16) (*g C*/*m* 3 ),

*DOC* is the concentration of [DOC](#page-11-13) (*g C*/*m* 3 ),

*FCR* is the fraction of respired *[C](#page-10-6)* produced as [RPOC,](#page-12-9)

*FCL* is the fraction of respired *[C](#page-10-6)* produced as [LPOC,](#page-11-16)

{210}------------------------------------------------

*FCD* is the fraction of respired *[C](#page-10-6)* produced as [DOC,](#page-11-13)

*FCRL* is the fraction of non-respired *[C](#page-10-6)* produced as [RPOC,](#page-12-9)

*FCLL* is the fraction of non-respired *[C](#page-10-6)* produced as [LPOC,](#page-11-16)

*FCDL* is the fraction of non-respired *[C](#page-10-6)* produced as [DOC,](#page-11-13)

*H* is the depth of water column, and

*B* is the depth of bed.

### 8.2.1.10 Coupling with Dissolved Oxygen (DO)

The interaction between rooted plants and epiphytes and [DO](#page-11-3) is given by

$$\frac{\partial DO_W}{\partial t} = \frac{1}{H} \left( P_{RPS} \cdot RPSOC \cdot RPS + P_{RPE} \cdot RPEOC \cdot RPE \right) \tag{8.175}$$

where,

*DO* is the concentration of [DO](#page-11-3) (*g O*2/*m* 3 ),

*RPSOC* is the *[O](#page-10-11)* to *[C](#page-10-6)* ratio for plant shoots (*g O*<sup>2</sup> *per g C*), and

*RPEOC* is the *[O](#page-10-11)* to *[C](#page-10-6)* ratio for epiphytes (*g O*<sup>2</sup> *per g C*).

### 8.2.1.11 Coupling with Phosphorous (P)

The interaction between rooted plants and epiphytes and water column and bed *[P](#page-10-8)* is given by

$$\frac{\partial RPOP_{W}}{\partial t} = \frac{1}{H} \left( FPR_{RPS} \cdot R_{RPS} + (1 - F_{RPSD}) \cdot FPRL_{RPS} \cdot L_{RPS} \right) \cdot RPSPC \cdot RPS 
+ \frac{1}{H} \left( FPR_{RPE} \cdot R_{RPE} + FPRL_{RPE} \cdot L_{RPE} \right) \cdot RPEPC \cdot RPE 
+ \frac{1}{H} FPRL_{RPD} \cdot L_{RPD} \cdot RPSPC \cdot RPD \quad (8.176)$$

$$\frac{\partial RPOP_B}{\partial t} = \frac{1}{B} \left( FPR_{RPR} \cdot R_{RPR} + FPRL_{RPR} \cdot L_{RPR} \right) RPRPC \cdot RPR \tag{8.177}$$

$$\frac{\partial LPOP_{W}}{\partial t} = \frac{1}{H} \left( FPL_{RPS} \cdot R_{RPS} + (1 - F_{RPSD}) \cdot FPLL_{RPS} \cdot L_{RPS} \right) \cdot RPSPC \cdot RPS 
+ \frac{1}{H} \left( FPL_{RPE} \cdot R_{RPE} + FPLL_{RPE} \cdot L_{RPE} \right) \cdot RPEPC \cdot RPE 
+ \frac{1}{H} FPLL_{RPD} \cdot L_{RPD} \cdot RPSPC \cdot RPD \quad (8.178)$$

$$\frac{\partial LPOP_B}{\partial t} = \frac{1}{B} \left( FPL_{RPR} \cdot R_{RPR} + FPLL_{RPR} \cdot L_{RPR} \right) RPRPC \cdot RPR \tag{8.179}$$

{211}------------------------------------------------

$$\frac{\partial DOP_{W}}{\partial t} = \frac{1}{H} \left( FPD_{RPS} \cdot R_{RPS} + (1 - F_{RPSD}) \cdot FPDL_{RPS} \cdot L_{RPS} \right) \cdot RPSPC \cdot RPS 
+ \frac{1}{H} \left( FPD_{RPE} \cdot R_{RPE} + FPDL_{RPE} \cdot L_{RPE} \right) \cdot RPEPC \cdot RPE 
+ \frac{1}{H} FCDL_{RPD} \cdot L_{RPD} \cdot RPSPC \cdot RPD \quad (8.180)$$

$$\frac{\partial DOP_B}{\partial t} = \frac{1}{B} \left( FPD_{RPR} \cdot R_{RPR} + FPDL_{RPR} \cdot L_{RPR} \right) RPRPC \cdot RPR \tag{8.181}$$

$$\begin{split} \frac{\partial PO4t_{W}}{\partial t} &= \frac{1}{H} \left( FPI_{RPS} \cdot R_{RPS} + (1 - F_{RPSD}) \cdot FPIL_{RPS} \cdot L_{RPS} \right) \cdot RPSPC \cdot RPS \\ &\quad + \frac{1}{H} \left( FPI_{RPE} \cdot R_{RPE} + FPIL_{RPE} \cdot L_{RPE} \right) \cdot RPEPC \cdot RPE \\ &\quad + \frac{1}{H} FCIL_{RPD} \cdot L_{RPD} \cdot RPSPC \cdot RPD - \frac{1}{H} F_{RPSPW} \cdot R_{RPS} \cdot RPSPC \cdot RPS \\ &\quad - \frac{1}{H} P_{RPE} \cdot RPEPC \cdot RPE \quad (8.182) \end{split}$$

$$\frac{\partial PO4t_B}{\partial t} = \frac{1}{B} \left( FPI_{RPR} \cdot R_{RPR} + FPIL_{RPR} \cdot L_{RPR} \right) RPRPC \cdot RPR - \frac{1}{H} \left( 1 - F_{RPSPW} \right) P_{RPS} \cdot RPRPC \cdot RPS \quad (8.183)$$

$$F_{RPSPW} = \frac{KHP_{RPR}P04d_w}{KHP_{RPR}PO4d_w + KHP_{RPS}P04d_b}$$
(8.184)

where,

*RPOP* is the concentration of [RPOP](#page-12-11) (*g P*/*m* 3 ),

*LPOP* is the concentration of [LPOP](#page-11-21) (*g P*/*m* 3 ),

*DOP* is the concentration of [DOP](#page-11-20) (*g P*/*m* 3 ),

*PO*4*t* = *PO*4*d* +*PO*4*p* is the [PO4t](#page-11-23) (*g P*/*m* 3 ),

*PO*4*d* is the concentration of dissolved *[PO](#page-10-13)*−<sup>3</sup> 4 (*g P*/*m* 3 ),

*PO*4*p* is the concentration of sorbed *[PO](#page-10-13)*−<sup>3</sup> 4 (*g P*/*m* 3 ),

*FPR* is the fraction of respired *[P](#page-10-8)* produced as [RPOP,](#page-12-11)

*FPL* is the fraction of respired *[P](#page-10-8)* produced as [LPOP,](#page-11-21)

*FPD* is the fraction of respired *[P](#page-10-8)* produced as [DOP,](#page-11-20)

*FPI* is the fraction of respired *[P](#page-10-8)* produced as [PO4t,](#page-11-23)

*FPRL* is the fraction of non-respired *[P](#page-10-8)* produced as [RPOP,](#page-12-11)

{212}------------------------------------------------

*FPLL* is the fraction of non-respired *[P](#page-10-8)* produced as [LPOP,](#page-11-21)

*FPDL* is the fraction of non-respired *[P](#page-10-8)* produced as [DOP,](#page-11-20)

*FPIL* is the fraction of non-respired *[P](#page-10-8)* produced as [PO4t,](#page-11-23)

*RPSPC* is the plant shoot *[P](#page-10-8)* to *[C](#page-10-6)* ratio (*g P per g C*),

*RPRPC* is the plant root *[P](#page-10-8)* to *[C](#page-10-6)* ratio (*g P per g C*),

*RPEPC* is the epiphyte *[P](#page-10-8)* to *[C](#page-10-6)* ratio (*g P per g C*),

*FRPSPW* is the fraction of *PO*4*d* uptake from water column,

*KHPRPS* is the half-saturation constant for *[P](#page-10-8)* uptake from water column (*g P*/*m* 3 ), and

*KHPRPR* is the half-saturation constant for *[P](#page-10-8)* uptake from bed (*g P*/*m* 3 ).

## 8.2.1.12 Coupling with Nitrogen (N)

The interaction between rooted plants and epiphytes and water column and bed *[N](#page-10-7)* is given by

$$\frac{\partial RPON_{W}}{\partial t} = \frac{1}{H} \left( FNR_{RPS} \cdot R_{RPS} + (1 - F_{RPSD}) \cdot FNRL_{RPS} \cdot L_{RPS} \right) \cdot RPSNC \cdot RPS 
+ \frac{1}{H} \left( FNR_{RPE} \cdot R_{RPE} + FNRL_{RPE} \cdot L_{RPE} \right) \cdot RPENC \cdot RPE 
+ \frac{1}{H} FNRL_{RPD} \cdot L_{RPD} \cdot RPSNC \cdot RPD \quad (8.185)$$

$$\frac{\partial RPON_B}{\partial t} = \frac{1}{B} \left( FNR_{RPR} \cdot R_{RPR} + FNRL_{RPR} \cdot L_{RPR} \right) RPRNC \cdot RPR \tag{8.186}$$

$$\frac{\partial LPON_W}{\partial t} = \frac{1}{H} \left( FNL_{RPS} \cdot R_{RPS} + (1 - F_{RPSD}) \cdot FNLL_{RPS} \cdot L_{RPS} \right) \cdot RPSNC \cdot RPS 
+ \frac{1}{H} \left( FNL_{RPE} \cdot R_{RPE} + FNLL_{RPE} \cdot L_{RPE} \right) \cdot RPENC \cdot RPE 
+ \frac{1}{H} FNLL_{RPD} \cdot L_{RPD} \cdot RPSNC \cdot RPD \quad (8.187)$$

$$\frac{\partial LPON_B}{\partial t} = \frac{1}{B} \left( FNL_{RPR} \cdot R_{RPR} + FNLL_{RPR} \cdot L_{RPR} \right) RPRNC \cdot RPR \tag{8.188}$$

$$\frac{\partial DON_{W}}{\partial t} = \frac{1}{H} \left( FND_{RPS} \cdot R_{RPS} + (1 - F_{RPSD}) \cdot FNDL_{RPS} \cdot L_{RPS} \right) \cdot RPSNC \cdot RPS 
+ \frac{1}{H} \left( FND_{RPE} \cdot R_{RPE} + FNDL_{RPE} \cdot L_{RPE} \right) \cdot RPENC \cdot RPE 
+ \frac{1}{H} FNDL_{RPD} \cdot L_{RPD} \cdot RPSNC \cdot RPD \quad (8.189)$$

{213}------------------------------------------------

$$\frac{\partial DON_B}{\partial t} = \frac{1}{B} \left( FND_{RPR} \cdot R_{RPR} + FNDL_{RPR} \cdot L_{RPR} \right) RPRNC \cdot RPR \tag{8.190}$$

$$\frac{\partial NH4_{W}}{\partial t} = \frac{1}{H} \left( FNI_{RPS} \cdot R_{RPS} + (1 - F_{RPSD}) \cdot FNIL_{RPS} \cdot L_{RPS} \right) \cdot RPSNC \cdot RPS$$

$$+ \frac{1}{H} \left( FNI_{RPE} \cdot R_{RPE} + FNIL_{RPE} \cdot L_{RPE} \right) \cdot RPENC \cdot RPE$$

$$+ \frac{1}{H} FNIL_{RPD} \cdot L_{RPD} \cdot RPSNC \cdot RPD$$

$$- \frac{1}{H} PN_{RPS} \cdot F_{RPSNW} \cdot R_{RPS} \cdot RPSNC \cdot RPS$$

$$- \frac{1}{H} PN_{RPE} \cdot P_{RPE} \cdot RPENC \cdot RPE \quad (8.191)$$

$$\frac{\partial NH4_{B}}{\partial t} = \frac{1}{B} \left( FNI_{RPR} \cdot R_{RPR} + FNIL_{RPR} \cdot L_{RPR} \right) RPRNC \cdot RPR$$
$$-\frac{1}{H} PN_{RPE} \left( 1 - F_{RPSPW} \right) P_{RPS} \cdot RPSNC \cdot RPS \quad (8.192)$$

$$\frac{\partial NO3_W}{\partial t} = -\frac{1}{H} (1 - PN_{RPS}) F_{RPSNW} \cdot P_{RPS} \cdot RPSNC \cdot RPS$$

$$-\frac{1}{H} (1 - PN_{RPE}) P_{RPE} \cdot RPENC \cdot RPE \quad (8.193)$$

$$\frac{\partial NO3_B}{\partial t} = -\frac{1}{H} (1 - PN_{RPS}) (1 - F_{RPSNW}) P_{RPS} \cdot RPSNC \cdot RPS$$
(8.194)

$$PN_{RPS} = \frac{NH4 \cdot NO3}{(KHNP_{RPS} + NH4)(KHNP_{RPS} + NO3)} + \frac{NH4 \cdot KHNP_{RPS}}{(NH4 + NO3)(KHNP_{RPS} + NO3)}$$
(8.195)

$$PN_{RPE} = \frac{NH4 \cdot NO3}{(KHNP_{RPE} + NH4)(KHNP_{RPE} + NO3)} + \frac{NH4 \cdot KHNP_{RPE}}{(NH4 + NO3)(KHNP_{RPE} + NO3)}$$
(8.196)

$$F_{RPSNW} = \frac{KHN_{RPR}(NH4 + NO3)_{w}}{KHN_{RPR}(NH4 + NO3)_{w} + KHN_{RPS}(NH4 + NO3)_{b}}$$
(8.197)

where,

RPON is the concentration of RPON  $(g N/m^3)$ ,

LPON is the concentration of LPON ( $g N/m^3$ ),

DON is the concentration of DON  $(g N/m^3)$ ,

NH4 is the concentration of  $NH_4^+$  as N (g  $N/m^3$ ),

{214}------------------------------------------------

*NO*3 is the concentration of *[NO](#page-10-10)*<sup>−</sup> 3 + *[NO](#page-10-12)*<sup>−</sup> 2 as *[N](#page-10-7)* (*g N*/*m* 3 ),

*FNR* is the fraction of respired *[N](#page-10-7)* produced as [RPON,](#page-12-10)

*FNL* is the fraction of respired *[N](#page-10-7)* produced as [LPON,](#page-11-19)

*FND* is the fraction of respired *[N](#page-10-7)* produced as [DON,](#page-11-18)

*FNI* is the fraction of respired *[N](#page-10-7)* produced as *[NH](#page-10-9)*<sup>+</sup> 4 ,

*FNRL* is the fraction of non-respired *[N](#page-10-7)* produced as [RPON,](#page-12-10)

*FNLL* is the fraction of non-respired *[N](#page-10-7)* produced as [LPON,](#page-11-19)

*FNDL* is the fraction of non-respired *[N](#page-10-7)* produced as [DON,](#page-11-18)

*FNIL* is the fraction of non-respired *[N](#page-10-7)* produced as *[NH](#page-10-9)*<sup>+</sup> 4 ,

*RPSNC* is the plant shoot *[N](#page-10-7)* to *[C](#page-10-6)* ratio (*g*; *N*; *per g C*),

*RPRNC* is the plant root *[N](#page-10-7)* to *[C](#page-10-6)* ratio (*g*; *N*; *per g C*),

*FRPSNW* is the plant shoot fraction of *NH*4 and *NOX* uptake from water column,

*PNRPS* is the *[NH](#page-10-9)*<sup>+</sup> 4 preference fraction for plant shoots,

*KHNPRPS* is the saturation coefficient for *[N](#page-10-7)* preference for plant shoots (*g*; *N*; *per g C*),

*PNRPE* is the *[NH](#page-10-9)*<sup>+</sup> 4 preference fraction for epiphytes,

*KHNPRPE* is the saturation coefficient for *[N](#page-10-7)* preference for epiphytes (*g*; *N*; *per g C*),

*KHNRPS* is the half-saturation constant for *[N](#page-10-7)* uptake from water column (*g N*/*m* 3 ), and

*KHNRPR* is the half-saturation constant for *[N](#page-10-7)* uptake from bed (*g N*/*m* 3 ).

#### <span id="page-214-0"></span>8.3. Sediment Diagenesis and Flux Formulation

[EFDC+](#page-11-0) water quality model provides three options for defining the sediment-water interface fluxes for nutrients and [DO.](#page-11-3) The options are; (1) externally forced spatially and temporally constant fluxes, (2) externally forced spatially and temporally variable fluxes, and (3) internally coupled fluxes simulated with the sediment diagenesis model. The water quality state variables that are controlled by diffusive exchange across the sediment-water interface include *[PO](#page-10-13)*−<sup>3</sup> 4 , *[NH](#page-10-9)*<sup>+</sup> 4 , *[NO](#page-10-10)*<sup>−</sup> 3 , *[SiO](#page-10-14)*2, [COD](#page-10-15) and [DO.](#page-11-3) The first two options require that the sediment fluxes be assigned as spatial/temporal forcing functions based on either observed sitespecific data from field surveys or best estimates based on the literature and sediment bed characteristics. The first two options, although acceptable for model calibration against historical data sets, do not provide the cause-effect predictive capability that is needed to evaluate future water quality conditions that might result from implementation of pollutant load reductions from watershed runoff. The third option, activation of the sediment diagenesis model developed by [Di Toro et al.](#page-260-20) [\(2001\)](#page-260-20) does provide the cause-effect predictive capability to evaluate how water quality conditions might change with implementation of alternative load reduction or management scenarios.

Living and non-living particulate [OC](#page-11-15) deposition, simulated in the [EFDC+](#page-11-0) water quality model, is internally coupled with the [EFDC+](#page-11-0) sediment diagenesis model. The sediment diagenesis model, based on the sediment flux model of [Di Toro et al.](#page-260-20) [\(2001\)](#page-260-20), describes the decomposition of [POM](#page-12-16) in the sediment bed, the consumption of [DO](#page-11-3) at the sediment-water interface [\(SOD\)](#page-12-8) and the exchange of dissolved constituents (*[NH](#page-10-9)*<sup>+</sup> 4 , *[NO](#page-10-10)*<sup>−</sup> 3 , *[PO](#page-10-13)*−<sup>3</sup> 4 , *[SiO](#page-10-14)*2, [COD\)](#page-10-15) across the sediment-water interface. State variables of the [EFDC+](#page-11-0) sediment flux model are sediment bed temperature, sediment bed [POC,](#page-12-7) [PON,](#page-12-18) [POP,](#page-12-17) porewater concentrations

{215}------------------------------------------------

<span id="page-215-0"></span>of  $PO_4^{-3}$ ,  $NH_4^+$ ,  $NO_3^-$ ,  $SiO_2$  and  $S_2^-/CH_4$ . The sediment diagenesis model computes sediment-water fluxes of COD, SOD,  $PO_4^{-3}$ ,  $NH_4^+$ ,  $NO_3^-$ , and  $SiO_2$ . The state variables modeled for a typical lake sediment flux model are listed and described in Table 8.15. An overview of the source and sink terms is presented with a description of each state variable group in this section. The details of the state variable equations, kinetic terms and numerical solution methods for the sediment diagenesis model are presented in Di Toro et al. (2001); Ji (2008); Park et al. (1995).

**Table 8.15.** EFDC+ Sediment Diagenesis Model State Variables

| #  | Name                       | Bed Layer | Units         |
|----|----------------------------|-----------|---------------|
| 1  | POC-G1                     | Layer-2   | $g/m^3$       |
| 2  | POC-G2                     | Layer-2   | $g/m^3$       |
| 3  | POC-G3                     | Layer-2   | $g/m^3$       |
| 4  | PON-G1                     | Layer-2   | $g/m^3$       |
| 5  | PON-G2                     | Layer-2   | $g/m^3$       |
| 6  | PON-G3                     | Layer-2   | $g/m^3$       |
| 7  | POP-G1                     | Layer-2   | $g/m^3$       |
| 8  | POP-G2                     | Layer-2   | $g/m^3$       |
| 9  | POP-G3                     | Layer-2   | $g/m^3$       |
| 10 | SiP                        | Layer-2   | $g/m^3$       |
| 11 | $S_2^-/CH_4$               | Layer-1   | $g/m^3$       |
| 12 | $S_2^-/CH_4$               | Layer-2   | $g/m^3$       |
| 13 | $NH_4^+$                   | Layer-1   | $g/m^3$       |
| 14 | $NH_4^+$                   | Layer-2   | $g/m^3$       |
| 15 | $NO_3^-$                   | Layer-1   | $g/m^3$       |
| 16 | $NO_3^-$                   | Layer-2   | $g/m^3$       |
| 17 | $PO_4^{-3}$                | Layer-1   | $g/m^3$       |
| 18 | $PO_4^{-3}$                | Layer-2   | $g/m^3$       |
| 19 | Available-SiO <sub>2</sub> | Layer-1   | $g/m^3$       |
| 20 | Available- $SiO_2$         | Layer-2   | $g/m^3$       |
| 21 | $NH_4^+$ -Flux             |           | $g/m^2 - day$ |
| 22 | $NO_3^-$ -Flux             |           | $g/m^2 - day$ |
| 23 | $PO_4^{-3}$ -Flux          |           | $g/m^2 - day$ |
| 24 | SiO <sub>2</sub> Flux      |           | $g/m^2 - day$ |
| 25 | SOD                        |           | $g/m^2 - day$ |
| 26 | COD Flux                   |           | $g/m^2 - day$ |
| 27 | Sediment Temperature       |           | $^{\circ}C$   |

A sediment process model developed by DiToro and Fitzpatrick (1993) hereinafter referred to as D&F was coupled with ICM for the Chesapeake Bay water quality modeling (Cerco and Cole, 1994). The sediment process model was slightly modified and incorporated into the EFDC+ water quality model to simulate the processes in the sediment and at the sediment-water interface. The description of the EFDC+ sediment process model in this section is from Park et al. (1995).

The  $NO_3^-$  state variables (15, 16 and 22 in Table 8.15), represent the sum of  $NO_3^-$  and  $NO_2^-$  in the model.

{216}------------------------------------------------

The difference in decay rates of [POM](#page-12-16) is accounted for by assigning a fraction of [POM](#page-12-16) to various decay classes [\(Westrich and Berner,](#page-265-21) [1984\)](#page-265-21). [POM](#page-12-16) in the sediments is divided into three *G* classes, or fractions, representing three scales of reactivity. The *G*<sup>1</sup> (labile) fraction has a half life of 20 days, and the *G*<sup>2</sup> (refractory) fraction has a half life of one year. The *G*<sup>3</sup> (inert) fraction is non-reactive, i.e., it undergoes no significant decay before burial into deep, inactive sediments. The varying reactivity of the *G* classes controls the time scale over which changes in depositional flux is reflected in changes in diagenesis flux. If the *G*<sup>1</sup> class would dominate the [POM](#page-12-16) input into the sediments, then there would be no significant time lag introduced by [POM](#page-12-16) diagenesis and any changes in depositional flux would be readily reflected in diagenesis flux.

In the sediment model, benthic sediments are represented as two layers (Figure [8.6\)](#page-216-0). Details of the processes shown in Figure [8.6](#page-216-0) will be discussed in the next sections. The upper layer (Layer 1) is in contact with the water column and may be oxic or anoxic depending on [DO](#page-11-3) concentration in the overlying water. The lower layer (Layer 2) is permanently anoxic. The upper layer depth, which is determined by the penetration of oxygen into the sediments, is at its maximum only a small fraction of the total depth. Because *H*<sup>1</sup> (∼ 0.1*cm*) << *H*2,

<span id="page-216-1"></span>
$$H = H_1 + H_2 \approx H_2 \tag{8.198}$$

where,

*H* is the total depth (approximately 10*cm*),

*H*<sup>1</sup> is the upper layer depth, and

<span id="page-216-0"></span>*H*<sup>2</sup> is the lower layer depth.

Fig. 8.6. Sediment Layers and Processes Included in Sediment Process Model

{217}------------------------------------------------

The model incorporates three basic processes (Figure [8.7\)](#page-217-1); (1) depositional flux of [POM,](#page-12-16) (2) the diagenesis of [POM,](#page-12-16) and (3) the resulting sediment flux. The sediment model is driven by the net settling of [POC,](#page-12-7) [PON,](#page-12-18) [POP](#page-12-17) and PSi from the overlying water to the sediments (depositional flux). Because of the negligible thickness of the upper layer (equation [8.198\)](#page-216-1), deposition proceeds from the water column directly to the lower layer. Within the lower layer, the model simulates the diagenesis (mineralization or decay) of deposited [POM,](#page-12-16) which produces *[O](#page-10-11)* demand and inorganic nutrients (diagenesis flux). The third basic process is the flux of substances produced by diagenesis (sediment flux). *[O](#page-10-11)* demand, as *[S](#page-10-16)* − 2 (in saltwater) or *[CH](#page-10-22)*<sup>4</sup> (in freshwater), takes three paths out of the sediments; (1) oxidation at the sediment-water interface as [SOD,](#page-12-8) (2) export to the water column as [COD,](#page-10-15) or (3) burial to deep, inactive sediments. Inorganic nutrients produced by diagenesis take two paths out of the sediments; (1) release to the water column or (2) burial to deep, inactive sediments (Figure [8.7\)](#page-217-1).

<span id="page-217-1"></span>Fig. 8.7. Schematic Diagram for Sediment Process Model

This section describes the three basic processes with reactions and sources/sinks for each state variable. The method of the solution includes finite difference equations, solution scheme, boundary, and initial conditions. Complete model documentation can be found in [DiToro and Fitzpatrick](#page-260-16) [\(1993\)](#page-260-16).

#### <span id="page-217-0"></span>8.3.1 Depositional Flux

Deposition is one process that couples the water column model with the sediment model. Consequently, deposition is represented in both the water column and sediment models. In the water column model, the governing mass-balance equations for the following state variables contain settling terms, which represent the depositional fluxes:

- 1. algal groups (equation [8.6\)](#page-155-1)
- 2. [RPOC](#page-12-9) and [LPOC](#page-11-16) (equations [8.41](#page-168-0) and [8.42\)](#page-168-1)
- 3. [RPOP](#page-12-11) and [LPOP](#page-11-21) (equations [8.58](#page-174-0) and [8.59](#page-174-1) and [PO4t](#page-11-23) (equation [8.61\)](#page-176-0)
- 4. [RPON](#page-12-10) and [LPON](#page-11-19) (equations [8.70](#page-180-0) and [8.71\)](#page-180-1)
- 5. [SiP](#page-12-13) (equation [8.85\)](#page-185-0) and [SiA](#page-12-12) (equation [8.86\)](#page-186-0)

The sediment model receives these depositional fluxes of [POC,](#page-12-7) [PON,](#page-12-18) [POP](#page-12-17) and [SiP.](#page-12-13) Because of the negligible thickness of the upper layer (equation [8.198\)](#page-216-1), deposition is considered to proceed from the water column

{218}------------------------------------------------

directly to the lower layer. Since the sediment model has three G classes of POM depending on the time scales of reactivity (Section 8.3.1), the POM fluxes from the water column should be mapped into three G classes based on their reactivity. Then, the depositional fluxes for the  $i^{th}$  G class (i = 1, 2 or 3) may be expressed as:

<span id="page-218-0"></span>
$$J_{POC,i} = FCLP_i \cdot WS_{LP} \cdot LPOC^N + FCRP_i \cdot WS_{RP} \cdot RPOC^N + \sum_{algae} FCB_{x,i} \cdot WS_x \cdot B_x^N$$
(8.199)

$$J_{PON,i} = FNLP_i \cdot WS_{LP} \cdot LPON^N + FNRP_i \cdot WS_{RP} \cdot RPON^N + \sum_{algae} FNB_{x,i} \cdot ANC_x \cdot WS_x \cdot B_x^N \quad (8.200)$$

$$J_{POP,i} = FPLP_i \cdot WS_{LP} \cdot LPOP^N + FPRP_i \cdot WS_{RP} \cdot RPOP^N + \sum_{algae} FPB_{x,i} \cdot APC \cdot WS_x \cdot B_x^N + \gamma_i \cdot WS_{TSS} \cdot PO4_p^N$$
(8.201)

<span id="page-218-2"></span><span id="page-218-1"></span>
$$J_{PSi} = WS_d \cdot PSi^N + ASC_d \cdot WS_d \cdot B_d^N + WS_{TSS} \cdot SA_p^N$$
(8.202)

where,

 $J_{POM,i}$  is the depositional flux of POM (M=C, N or P) routed into the  $i^{th}$  G class  $(g/m^2/day)$ ,

 $J_{PSi}$  is the depositional flux of SiP ( $g Si/m^2/day$ ),

 $FCLP_i, FNLP_i$  and  $FPLP_i$  are the fraction of water column LPOC, LPON, and LPOP respectively, routed into the  $i^{th}$  G class in sediment,

 $FCRP_i$ ,  $FNRP_i$  and  $FPRP_i$  are the fraction of water column RPOC, RPON and RPOP respectively, routed into the  $i^{th}$  G class in sediment,

 $FCB_{x,i}$ ,  $FNB_{x,i}$  and  $FPB_{x,i}$  are the fraction of POC, PON and POP, respectively, in the algal group x routed into the  $i^{th}$  G class in sediment, and

$$\gamma_i = 1$$
 for  $i = 1$ ,  $\gamma_i = 0$  for  $i = 2$  or 3.

In the source code, the sediment process model is solved after the water column water quality model. The calculated fluxes using the water column conditions at  $t = t_n$  are used for the computation of the water quality variables at  $t = t_n + \theta$ , where  $\theta = 2 \cdot m \cdot \Delta t$  is the time step for the kinetic equations. The superscript N in equation 8.199 to 8.202 indicates the variables after being updated for the kinetic processes.

The settling of sorbed  $PO_4^{-3}$  is considered to contribute to the labile G1 pool in equation 8.201, and settling of sorbed  $SiO_2$  contributes to  $J_{PSi}$  in equation 8.202 to avoid creation of additional depositional fluxes for inorganic particulates. The sum of distribution coefficients should be unity:

$$\begin{split} \sum_{i} FCLP_{i} &= \sum_{i} FNLP_{i} = \sum_{i} FPLP_{i} = \sum_{i} FCRP_{i} = \\ &\sum_{i} FNRP_{i} = \sum_{i} FPRP_{i} = \sum_{i} FCB_{x,i} = \sum_{i} FNB_{x,i} = \sum_{i} FPB_{x,i} = 1. \end{split}$$

{219}------------------------------------------------

The settling velocities, *WSLP*, *WSRP*, *WSx*, and *WST SS*, as defined in the [EFDC+](#page-11-0) water column model (Section [8.1.3.2\)](#page-161-0), are net settling velocities. If [TAM](#page-12-14) is selected as a measure of sorption site, *WST SS* is replaced by *WS<sup>s</sup>* in Equations [8.201](#page-218-2) and [8.202.](#page-218-1)

### <span id="page-219-0"></span>8.3.2 Diagenesis Flux

Another coupling point of the sediment model to the water column model is the sediment flux. The computation of sediment flux requires that the magnitude of the diagenesis flux be known. The diagenesis flux is explicitly computed using mass-balance equations for deposited [POC,](#page-12-7) [PON,](#page-12-18) and [POP.](#page-12-17) Dissolved *[SiO](#page-10-14)*<sup>2</sup> is produced in the sediments as a result of the dissolution of [SiP.](#page-12-13) Since the dissolution process is different from the bacterial-mediated diagenesis process, it is presented separately. In the mass-balance equations, the depositional fluxes of [POM](#page-12-16) are the source terms and the decay of [POM](#page-12-16) in the sediments produces the diagenesis fluxes. The integration of the mass-balance equations for [POM](#page-12-16) provides the diagenesis fluxes that are the inputs for the mass-balance equations for *[NH](#page-10-9)*<sup>+</sup> 4 , *[NO](#page-10-10)*<sup>−</sup> 3 , *[PO](#page-10-13)*−<sup>3</sup> 4 and *[S](#page-10-16)* − 2 /*[CH](#page-10-22)*<sup>4</sup> in the sediments.

As the upper layer thickness is negligible (equation [8.198\)](#page-216-1) the depositional flux is considered to proceed directly to the lower layer (equations [8.199,](#page-218-0) to [8.202\)](#page-218-1), and diagenesis is considered to occur only in the lower layer. The mass-balance equations are similar for [POC,](#page-12-7) [PON,](#page-12-18) and [POP,](#page-12-17) and for different *G* classes. The mass-balance equation in the anoxic lower layer for the *i th G* class (*i* = 1, 2 *or* 3) may be expressed as:

<span id="page-219-3"></span>
$$H_2 \frac{\partial G_{POM,i}}{\partial t} = -K_{POM,i} \cdot \theta_{POM,i}^{T-20} \cdot G_{POM,i} \cdot H_2 - W \cdot G_{POM,i} + J_{POM,i}$$
(8.203)

where,

*GPOM*,*<sup>i</sup>* is the concentration of *POM*(*M* = *C*, *N or P*) in the *i th G* class in Layer 2 (*g*/*m* 3 )

*KPMO*,*<sup>i</sup>* is the decay rate of the *i th G* class [POM](#page-12-16) at 20◦*C* in Layer 2 (1/*day*)

θ*POM*,*i* is the constant for temperature adjustment for *KPOM*,*<sup>i</sup>*

*T* is the sediment temperature (◦*C*)

*W* is the burial rate (*m*/*day*)

Since the *G*<sup>3</sup> class is inert *KPOM*,<sup>3</sup> = 0.

Once the mass-balance equations for *GPOM*,<sup>1</sup> and *GPOM*,<sup>2</sup> are solved, the diagenesis fluxes are computed from the rate of mineralization of the two reactive G classes:

<span id="page-219-2"></span>
$$J_{M} = \sum_{i=1}^{2} K_{POM,i} \cdot \theta_{POM,i}^{T-20} \cdot G_{POM,i} \cdot H_{2}$$
(8.204)

*J<sup>M</sup>* is the diagenesis flux (*g*/*m* <sup>2</sup>/*day*) of *M* = *C*, *N* or *P*

#### <span id="page-219-1"></span>8.3.3 Sediment Flux

#### 8.3.3.1 Basic Equations

The mineralization of [POM](#page-12-16) produces soluble intermediates, which are quantified as diagenesis fluxes in the previous section. The intermediates react in the oxic and anoxic layers, and portions are returned to the 

{220}------------------------------------------------

overlying water as sediment fluxes. Computation of sediment fluxes requires mass-balance equations for  $NH_4^+$ ,  $NO_3^-$ ,  $PO_4^{-3}$ ,  $S_2^-/CH_4$  and available  $SiO_2$ . This section describes the flux portion for  $NH_4^+$ ,  $NO_3^-$ ,  $PO_4^{-3}$  and  $S_2^-/CH_4$  of the model.

In the upper layer, the processes included in the flux portion are:

- 1. exchange of dissolved fraction between Layer 1 and the overlying water,
- 2. exchange of dissolved fraction between Layer 1 and 2 via diffusive transport,
- 3. exchange of particulate fraction between Layer 1 and 2 via particle mixing,
- 4. loss by burial to the lower layer (Layer 2),
- 5. removal (sink) by reaction, and
- 6. internal sources.

Since the upper layer is quite thin ( $H_1 \sim 0.1$  cm, equation 8.198) and the surface mass transfer coefficient (s) is on the order of 0.1 m/day, the residence time of dissolved nutrient in the upper layer is:  $H/s \sim 10^{-2}$  days. Hence, a steady-state approximation is made in the upper layer. Then the mass-balance equation for  $NH_4^+$ ,  $NO_3^-$ ,  $PO_4^{-3}$  or  $S_2^-/CH_4$  in the upper layer is:

$$H_{1} \frac{\partial Ct_{1}}{\partial t} = 0 = s \left( f d_{0} \cdot Ct_{0} - f d_{1} \cdot Ct_{1} \right) + KL \left( f d_{2} \cdot Ct_{2} - f d_{1} \cdot Ct_{1} \right) + \omega \left( f p_{2} \cdot Ct_{2} - f p_{1} \cdot Ct_{1} \right) - W \cdot Ct_{1} - \frac{K_{1}^{2}}{s} Ct_{1} + J_{1} \quad (8.205)$$

where,

<span id="page-220-0"></span> $Ct_1$  and  $Ct_2$  are the total concentrations in Layer 1 and 2, respectively  $(g/m^3)$ ,

 $Ct_0$  is the total concentrations in the overlying water  $(g/m^3)$ ,

s is the surface mass transfer coefficient (m/day),

KL is the diffusion velocity for dissolved fraction between Layer 1 and 2 (m/day),

 $\omega$  is the particle mixing velocity between Layer 1 and 2 (m/day),

 $fd_0$  is the dissolved fraction of total substance in the overlying water  $(0 \le fd_0 \le 1)$ ,

 $fd_1$  is the dissolved fraction of total substance in Layer 1 ( $0 \le fd_1 \le 1$ ),

 $fp_1$  is the particulate fraction of total substance in Layer 1 (= 1 -  $fd_1$ ),

 $fd_2$  is the dissolved fraction of total substance in Layer 2 ( $0 \le fd_2 \le 1$ ),

 $fp_2$  is the particulate fraction of total substance in Layer 2 (= 1 -  $fd_2$ ),

 $K_1$  is the reaction velocity in Layer 1 (m/day), and

 $J_1$  is the sum of all internal sources in Layer 1  $(g/m^2/day)$ .

The first term on the RHS of equation 8.205 represents the exchange across sediment-water interface. Then the sediment flux from Layer 1 to the overlying water, which couples the sediment model to the water column model, may be expressed as:

{221}------------------------------------------------

<span id="page-221-0"></span>
$$J_{aq} = s(fd_1 \cdot Ct_1 - fd_0 \cdot Ct_0)$$
(8.206)

where, *Jaq* is the sediment flux of *[NH](#page-10-9)*<sup>+</sup> 4 , *[NO](#page-10-10)*<sup>−</sup> 3 , *[PO](#page-10-13)*−<sup>3</sup> 4 or *[S](#page-10-16)* − 2 /*[CH](#page-10-22)*<sup>4</sup> to the overlying water (*g*/*m* <sup>2</sup>/*day*).

The convention used in equation [8.206](#page-221-0) is that the positive flux is from the sediment to the overlying water. In the lower layer, the processes included in the flux portion are (Figure [8.6\)](#page-216-0):

- 1. exchange of dissolved fraction between Layer 1 and 2 via diffusive transport,
- 2. exchange of particulate fraction between Layer 1 and 2 via particle mixing,
- 3. deposition from Layer 1 and burial to the deep inactive sediments,
- 4. removal (sink) by reaction, and
- 5. internal sources including diagenetic source.

The mass-balance equation for *[NH](#page-10-9)*<sup>+</sup> 4 , *[NO](#page-10-10)*<sup>−</sup> 3 , *[PO](#page-10-13)*−<sup>3</sup> 4 or *[S](#page-10-16)* − 2 /*[CH](#page-10-22)*<sup>4</sup> in the lower layer is

$$H_{2} \frac{\partial Ct_{2}}{\partial t} = -KL(fd_{2} \cdot Ct_{2} - fd_{1} \cdot Ct_{1}) - \omega(fp_{2} \cdot Ct_{2} - fp_{1} \cdot Ct_{1}) + W(Ct_{1} - Ct_{2}) - K_{2} \cdot Ct_{2} + J_{2}$$
 (8.207)

where,

*K*<sup>2</sup> is the reaction velocity in Layer 2 (*m*/*day*), and

*J*<sup>2</sup> is the sum of all internal sources including diagenesis in Layer 2 (*g*/*m* <sup>2</sup>/*day*).

The substances produced by mineralization of [POM](#page-12-16) in sediments may be present in both dissolved and particulate phases. This distribution directly affects the magnitude of the substance that is returned to the overlying water. In equations [8.205](#page-220-0) to [8.207,](#page-221-1) the distribution of a substance between the dissolved and particulate phases in a sediment is parameterized using a linear partitioning coefficient.

The dissolved and particulate fractions are computed from the partitioning equations:

<span id="page-221-3"></span><span id="page-221-1"></span>
$$fd_1 = \frac{1}{1 + m_1 \cdot \pi_1} \qquad fp_1 = 1 - fd_1 \tag{8.208}$$

<span id="page-221-2"></span>
$$fd_2 = \frac{1}{1 + m_2 \cdot \pi_2} \qquad fp_2 = 1 - fd_2 \tag{8.209}$$

where,

*m*<sup>1</sup> and *m*<sup>2</sup> are the solid concentrations in Layer 1 and 2, respectively (*kg*/*l*), and

π<sup>1</sup> and π<sup>2</sup> are the partition coefficient in Layer 1 and 2, respectively (*per kg*/*l*).

The partition coefficient is the ratio of particulate to dissolved fraction per unit solid concentration (i.e. per unit sorption site available).

All terms, except the last two terms, in equations [8.205](#page-220-0) and [8.207](#page-221-1) are common to all state variables and are described in Section 5.3.1. The last two terms represent the reaction and source/sink terms, respectively.

{222}------------------------------------------------

## 8.3.3.2 Common Parameters for Sediment Flux

Parameters that are needed for the sediment fluxes are *s*, ω, *KL*, *W*,*H*2, *m*1, *m*2, π1,

π2, κ1, κ2, *J*1, and *J*<sup>2</sup> in equations [8.205](#page-220-0) to [8.209.](#page-221-2) Of these, κ1, κ2, *J*<sup>1</sup> and *J*<sup>2</sup> are variable-specific. Among the other common parameters, *W*, *H*2, *m*<sup>1</sup> and *m*2, are specified as input. The modeling of the remaining three parameters, *s*, ω, *KL*, are described in this section.

#### 8.3.3.2.1 Surface Mass Transfer Coefficient

The surface mass transfer coefficient, *s* can be estimated from the ratio of [SOD](#page-12-8) and overlying water *[O](#page-10-11)* concentration [\(Di Toro et al.,](#page-260-21) [1990\)](#page-260-21):

<span id="page-222-0"></span>
$$s = \frac{D_1}{H_1} = \frac{SOD}{DO_0} \tag{8.210}$$

where, *D* is the diffusion coefficient in Layer 1 (*m* <sup>2</sup>/*day*).

It is possible to estimate other model parameters, once *s* has been calculated.

### 8.3.3.2.2 Particulate Phase Mixing Coefficient

The particle mixing velocity ω between Layer 1 and 2 is parameterized as:

$$\omega = \frac{D_p \cdot \theta_{D_p}^{T-20}}{H_2} \frac{G_{POC,1}}{G_{POC,R}} \frac{DO_0}{KM_{D_p} + DO_0}$$
(8.211)

where,

*D<sup>p</sup>* is the apparent diffusion coefficient for particle mixing (*m* <sup>2</sup>/*day*),

θ*Dp* is the constant for temperature adjustment for *Dp*,

*GPOC*,*<sup>R</sup>* is the reference concentration for *GPOC*,<sup>1</sup> (*g C*/*m* 3 ), and

*KMDp* is the particle mixing half-saturation constant for oxygen (*g O*2/*m* 3 ).

The enhanced mixing of sediment particles by macrobenthos (bioturbation) is quantified by estimating *Dp*. The particle mixing appears to be proportional to the benthic biomass [\(Matisoff,](#page-262-18) [1982\)](#page-262-18), which is correlated to the*[C](#page-10-6)* input to the sediment [\(Robbins et al.,](#page-263-22) [1989\)](#page-263-22). This is parameterized by assuming that benthic biomass is proportional to the available labile*[C](#page-10-6)*. *GPOC*,1, and *GPOC*,*<sup>R</sup>* is the reference concentration at which the particle mixing velocity is at its nominal value. The Monod-type *[O](#page-10-11)* dependency accounts for the *[O](#page-10-11)* dependency of benthic biomass.

It has been observed that a hysteresis exists in the relationship between the bottom water *[O](#page-10-11)* and benthic biomass. Benthic biomass increases as the summer progresses. However, the occurrence of anoxia/hypoxia reduces the biomass drastically and also imposes stress on benthic activities. After full overturn, the bottom water *[O](#page-10-11)* increases but the population does not recover immediately. Hence, the particle mixing velocity, which is proportional to the benthic biomass, does not increase in response to the increased bottom water *[O](#page-10-11)*. Recovery of benthic biomass following hypoxic events depends on many factors including severity and longevity of hypoxia, constituent species, and salinity [\(Diaz et al.,](#page-260-22) [1995\)](#page-260-22).

{223}------------------------------------------------

This phenomenon of reduced benthic activities and hysteresis is parameterized based on the idea of stress that low *[O](#page-10-11)* imposes on the benthic population. It is analogous to the modeling of the toxic effect of chemicals on organisms [\(Mancini,](#page-262-19) [1983\)](#page-262-19). A first order differential equation is employed, in which the benthic stress 1) accumulates only when overlying *[O](#page-10-11)* is below *KMDp* and 2) is dissipated at a first order rate (Figure [8.8a](#page-224-0)):

<span id="page-223-0"></span>
$$\frac{\partial ST}{\partial t} = \begin{cases} -K_{ST} \cdot ST + \left(1 - \frac{DO_0}{KM_{Dp}}\right), & \text{if } DO_0 < KM_{Dp} \\ -K_{ST} \cdot ST, & \text{if } DO_0 > KM_{Dp} \end{cases}$$
(8.212)

where,

*ST* is the accumulated benthic stress (*day*), and

*KST* is the first order decay rate for *ST* (1/*day*).

The behavior of this formulation can be understood by evaluating the steady-state stresses at two extreme conditions of overlying water oxygen, *DO*<sup>0</sup> as:

$$DO_0 = 0, K_{ST} \cdot ST = 1$$
  $f(ST) = (1 - K_{ST} \cdot ST) = 0$ 

$$DO_0 \ge KM_{Dp}, K_{ST} \cdot ST = 0$$
  $f(ST) = (1 - K_{ST} \cdot ST) = 1$ 

The dimensionless expression, *f*(*ST*) = 1−*KST* ·*ST*, appears to be the proper variable to quantify the effect of benthic stress on benthic biomass and thus particle mixing (Figure [8.8b](#page-224-0)).

The final formulation for the particle mixing velocity including the benthic stress is:

$$\omega = \frac{D_p \cdot \theta_{Dp}^{T-20}}{H_2} \frac{G_{POC,1}}{G_{POC,R}} \frac{DO_0}{KM_{Dp} + DO_0} f(ST) + \frac{D_{p_{min}}}{H_2}$$
(8.213)

where *Dpmin* is the minimum diffusion coefficient for particle mixing (*m* <sup>2</sup>/*day*).

The reduction in particle mixing due to the benthic stress, *f*(*ST*) is estimated by employing the following procedure. The stress, *ST* is normally calculated using equation [8.212.](#page-223-0) Once *DO*<sup>0</sup> drops below a critical concentration *DOST*,*c*, for *NChypoxia* consecutive days or more, the calculated stress is not allowed to decrease until *tMBS* days of *DO*<sup>0</sup> > *DOST*,*c*. That is, only when hypoxic days are longer than critical hypoxia days (*NChypoxia*), the maximum stress, or minimum (1−*KST* · *ST*), is retained for a specified period (*tMBS* days) after *DO*<sup>0</sup> recovery (Figure [8.8\)](#page-224-0). No hysteresis occurs if *DO*<sup>0</sup> does not drop below *DOST*,*<sup>c</sup>* or if hypoxia lasts less than *NChypoxia* days. When applying maximum stress for *tMBS* days, the subsequent hypoxic days are not included in *tMBS*. This parameterization of hysteresis essentially assumes seasonal hypoxia, i.e., one or two major hypoxic events during summer, and might be unsuitable for systems with multiple hypoxic events throughout the year.

{224}------------------------------------------------

<span id="page-224-0"></span>Fig. 8.8. Benthic stress (a) and its effect on particle mixing (b) as a function of overlying water column [DO](#page-11-3) concentration.

Three parameters relating to hysteresis *DOST*,*c*, *NChypoxia*, and *tMBS* are functions of many factors including severity and longevity of hypoxia, constituent species and salinity, and thus have site-specific variabilities [\(Diaz et al.,](#page-260-22) [1995\)](#page-260-22). The critical overlying [DO](#page-11-3) concentration *DOST*,*c*, also depends on the distance from the bottom of the location of *DO*0. The critical hypoxia days *NChypoxia*, depends on tolerance of benthic organisms to hypoxia and thus on benthic community structure [\(Diaz et al.,](#page-260-22) [1995\)](#page-260-22). The time lag for the recovery of benthic biomass following hypoxic events, *tMBS* tends to be longer for higher salinity. The above three parameters are considered to be spatially constant input parameters.

#### 8.3.3.2.3 Dissolved Phase Mixing Coefficient

Dissolved phase mixing between Layer 1 and 2 is via passive molecular diffusion, which is enhanced by the mixing activities of the benthic organisms (bio-irrigation). This is modeled by increasing the diffusion coefficient relative to the molecular diffusion coefficient:

{225}------------------------------------------------

<span id="page-225-0"></span>
$$KL = \frac{D_d \cdot \theta_{Dd}^{T-20}}{H_2} + R_{BI,BT} \cdot \omega \tag{8.214}$$

where,

 $D_d$  is the diffusion coefficient in pore water  $(m^2/day)$ ,

 $\theta_{Dd}$  is the constant for temperature adjustment for  $D_d$ , and

 $R_{BI,BT}$  is the ratio of bio-irrigation to bioturbation.

The last term in equation 8.214 accounts for the enhanced mixing by organism activities.

#### 8.3.3.3 Ammonia Nitrogen

Diagenesis is assumed not to occur in the upper layer because of its shallow depth, and  $NH_4^+$  is produced by diagenesis in the lower layer:

$$J_{1.NH4} = 0 J_{2.NH4} = J_N (8.215)$$

where  $J_N$  is from equation 8.204.

 $NH_4^+$  is nitrified to  $NO_3^-$  in the presence of O. A Monod-type expression is used for the  $NH_4^+$  and O dependency of the nitrification rate. Then, the oxic layer reaction velocity in equation 8.205 for  $NH_4^+$  may be expressed as:

$$K_{1,NH4}^2 = \frac{DO_0}{2 \cdot KM_{NH4,O2} + DO_0} \frac{KM_{NH4}}{KM_{NH4} + NH4_1} K_{NH4}^2 \cdot \theta_{NH4}^{T-20}$$
(8.216)

and then the nitrification flux becomes:

<span id="page-225-1"></span>
$$J_{Nit} = \frac{K_{1,NH4}^2}{s} \cdot NH4_1 \tag{8.217}$$

where,

 $KM_{NH4,O2}$  is the nitrification half-saturation constant for DO ( $g O_2/m^3$ ),

 $NH4_1$  is the total  $NH_4^+$  concentration as N in Layer 1 ( $gN/m^3$ ),

 $KM_{NH4}$  is the nitrification half-saturation constant for  $NH_4^+$  (g  $N/m^3$ ),

 $K_{NH4}$  is the optimal reaction velocity for nitrification at  $20^{\circ}C$  (m/day),

 $\theta_{NH4}$  is the constant for temperature adjustment for  $K_{NH4}$ , and

 $J_{Nit}$  is the nitrification flux  $(g N/m^2/day)$ .

Nitrification does not occur in the anoxic lower layer:

$$K_{2,NH4} = 0 (8.218)$$

{226}------------------------------------------------

Once equations 8.205 and 8.207 are solved for  $NH4_1$  and  $NH4_2$ , the sediment flux of  $NH_4^+$  to the overlying water  $J_{aq,NH4}$ , can be calculated using equation 8.206. Note that it is not  $NH4_1$  and  $NH4_2$  that determine the magnitude of  $J_{aq,NH4}$  (DiToro and Fitzpatrick (1993, Section X-B-2)), but the magnitude is determined by (1) the diagenesis flux, (2) the fraction that is nitrified, and (3) the surface mass transfer coefficient (s) that mixes the remaining portion.

#### 8.3.3.4 Nitrate Nitrogen

Nitrification flux is the only source of  $NO_3^-$  in the upper layer, given by Equation 8.217, and there is no diagenetic source for  $NO_3^-$  in both layers:

$$J_{1,NO3} = J_{Nit} J_{2,NO3} = 0$$
 (8.219)

 $NO_3^-$  is present in sediments as a dissolved substance, i.e.,  $\pi_{1,NO3} = \pi_{2,NO3} = 0$ , making  $fd_{1,NO3} = fd_{2,NO3} = 1$  (Equations 8.208 and 8.209): it also makes R meaningless, hence R = 0.  $NO_3^-$  is removed by denitrification in both oxic and anoxic layers with the C required for denitrification supplied by C diagenesis. The reaction velocities in equations 8.205 and 8.207 for  $NO_3^-$  may be expressed as:

$$K_{1,NO3}^2 = K_{NO3,1}^2 \cdot \theta_{NO3}^{T-20}$$
 (8.220)

$$K_{2,NO3} = K_{NO3,2}^2 \cdot \theta_{NO3}^{T-20} \tag{8.221}$$

and the denitrification flux out of sediments as a N gas becomes:

<span id="page-226-0"></span>
$$J_{N2(g)} = \frac{K_{1,NO3}^2}{s} NO3_1 + K_{2,NO3} \cdot NO3_2$$
 (8.222)

where,

 $K_{NO3,1}$  is the reaction velocity for denitrification in Layer 1 at  $20^{\circ}C$  (m/day),

 $K_{NO3,2}$  is the reaction velocity for denitrification in Layer 2 at  $20^{\circ}C$  (m/day),

 $\theta_{NO3}$  is the constant for temperature adjustment for  $K_{NO3,1}$  and  $K_{NO3,2}$ ,

 $J_{N2(g)}$  is the denitrification flux  $(g N/m^2/day)$ ,

 $NO3_1$  is the total  $NO_3^-$  concentration as N in Layer 1 ( $gN/m^3$ ), and

 $NO3_2$  is the total  $NO_3^-$  concentration as N in Layer 2 ( $gN/m^3$ ).

Once equations 8.205 and 8.207 are solved for  $NO3_1$  and  $NO3_2$ , the sediment flux of  $NO_3^-$  to the overlying water  $J_{aq,NO3}$ , can be calculated using equation 8.206. The steady-state solution for  $NO_3^-$  showed that the  $NO_3^-$  flux is a linear function of  $NO3_0$  (DiToro and Fitzpatrick, 1993, equation III-15); the intercept quantifies the amount of  $NH_4^+$  in the sediment that is nitrified but not denitrified (thus releases as  $J_{aq,NO3}$ ), and the slope quantifies the extent to which overlying water  $NO_3^-$  is denitrified in the sediment. It also revealed that if the internal production of  $NO_3^-$  is small relative to the flux of  $NO_3^-$  from the overlying water,

{227}------------------------------------------------

the normalized  $NO_3^-$  flux to the sediment  $-J_{aq,NO3}/NO3_0$ , is linear in s for small s and constant for large s (DiToro and Fitzpatrick, 1993, Section III-C). For small s ( $\sim 0.01 m/day$ ), H is large (equation 8.210) so that oxic layer denitrification predominates and  $J_{aq,NO3}$  is essentially zero independent of  $NO3_0$  (DiToro and Fitzpatrick, 1993, Figure III-4).

#### 8.3.3.5 Phosphate Phosphorus

Phosphate is produced by the diagenetic breakdown of POP in the lower layer:

$$J_{1,PO4} = 0 J_{2,PO4} = J_P$$
 (8.223)

where  $J_P$  is the diagenesis flux of phosphorus obtained from equation 8.204. A portion of the liberated  $PO_4^{-3}$  remains in the dissolved form and a portion becomes particulate  $PO_4^{-3}$ , either via precipitation of  $PO_4^{-3}$  containing minerals (Troup, 1974) (e.g. vivianite,  $Fe_3(PO_4)_2(s)$ ), or by partitioning to  $PO_4^{-3}$  sorption sites (Barrow, 1983; Giordani and Astorri, 1986; Lijklema, 1980). The extent of particulate formation is determined by the magnitude of the partition coefficients  $\pi_{1,PO4}$  and  $\pi_{2,PO4}$  in equations 8.208 and 8.209.  $PO_4^{-3}$  flux is strongly affected by  $PO_0$ , the overlying water DO concentration. As  $PO_0$  approaches zero, the  $PO_4^{-3}$  flux from the sediments increases. This mechanism is incorporated by making  $PO_0$  larger, under oxic conditions, than  $PO_0$  in the model, when  $PO_0$  exceeds a critical concentration  $PO_0$  crit,  $PO_0$ , sorption in the upper layer is enhanced by an amount  $PO_0$  exceeds a critical concentration  $PO_0$  crit,  $PO_0$ , sorption in the upper layer is enhanced by an amount  $PO_0$  exceeds a critical concentration  $PO_0$  crit,  $PO_0$  sorption in the upper layer is enhanced by an amount  $PO_0$  exceeds a critical concentration  $PO_0$  critical concentration  $PO_0$  critical concentration is the upper layer is enhanced by an amount  $PO_0$  exceeds a critical concentration is  $PO_0$  critical concentration in the upper layer is enhanced by an amount  $PO_0$  exceeds a critical concentration is  $PO_0$  and  $PO_0$  exceeds a critical concentration is  $PO_0$  exceeds a critical concentration is  $PO_0$  exceeds a critical concentration is  $PO_0$  exceeds a critical concentration is  $PO_0$  exceeds a critical concentration is  $PO_0$  exceeds a critical concentration is  $PO_0$  exceeds a critical concentration is  $PO_0$  exceeds a critical concentration is  $PO_0$  exceeds a critical concentration is  $PO_0$  exceeds a critical concentration is  $PO_0$  exceeds a critical concentration is  $PO_0$  exceeds a critical concentration is  $PO_0$  exceeds a critical co

$$\pi_{1,PO4} = \pi_{2,PO4} \cdot (\Delta \pi_{PO4,1}) \qquad DO_0 > (DO_0)_{crit,PO4}$$
(8.224)

When DO falls below  $(DO_0)_{crit,PO4}$ , then:

$$\pi_{1,PO4} = \pi_{2,PO4} \cdot (\Delta \pi_{PO4,1})^{\frac{DO_0}{(DO_0)_{crit,PO4}}} \qquad DO_0 \le (DO_0)_{crit,PO4}$$
(8.225)

which smoothly reduces  $\pi_{1,PO4}$  to  $\pi_{2,PO4}$  as  $DO_0$  goes to zero.

There is no removal reaction for  $PO_4^{-3}$  in both layers:

$$\kappa_{1,PO4} = \kappa_{2,PO4} = 0 \tag{8.226}$$

Once equations 8.205 and 8.207 are solved for  $PO4_1$  and  $PO4_2$ , the sediment flux of  $PO_4^{-3}$  to the overlying water  $J_{aq,PO4}$ , can be calculated using equation 8.206.

#### 8.3.3.6 Sulfide/Methane and Oxygen Demand

#### 8.3.3.6.1 Sulfide

No diagenetic production of  $S_2^-$  occurs in the upper layer. In the lower layer,  $S_2^-$  is produced by carbon diagenesis (equation 8.204) and is decremented by the OC consumed due to denitrification (equation 8.222). Then:

{228}------------------------------------------------

<span id="page-228-0"></span>
$$J_{1,H2S} = 0$$

$$J_{2,H2S} = a_{O2,C} \cdot J_C - a_{O2,NO3} \cdot J_{N2(g)}$$
(8.227)

where,

 $a_{O2,C}$  is the stoichiometric coefficient for carbon diagenesis consumed by  $S_2^-$  oxidation (2.6667g  $O_2$  – equivalents per g C), and

 $a_{O2,NO3}$  is the stoichiometric coefficient for carbon diagenesis consumed by denitrification (2.8571g  $O_2$  – equivalents per g N).

A portion of the dissolved  $S_2^-$  that is produced in the anoxic layer reacts with the Fe to form particulate Iron monosulfide (FeS) (Morse et al., 1987). The particulate fraction is mixed into the oxic layer where it can be oxidized to  $Fe_2O_3(s)$  (ferric oxide). The remaining dissolved fraction also diffuses into the oxic layer where it is oxidized to  $SO_4^{-2}$ . Partitioning between dissolved and particulate  $S_2^-$  in the model represents the formation of FeS(s), which is parameterized using partition coefficients  $\pi_{1,H2S}$  and  $\pi_{2,H2S}$ , in equations 8.208 and 8.209.

EFDC+ has three pathways for  $S_2^-$ , the reduced end product of C diagenesis: (1)  $S_2^-$  oxidation, (2) aqueous  $S_2^-$  flux, and (3) burial. The distribution of  $S_2^-$  among the three pathways is controlled by the partitioning coefficients and the oxidation reaction velocities (Section V-E in DiToro and Fitzpatrick (1993)). Both dissolved and particulate  $S_2^-$  are oxidized in the oxic layer, consuming O in the process. In the oxic upper layer, the oxidation rate that is linear in O concentration is used (Boudreau, 1991; Cline and Richards, 1969; Millero, 1986). In the anoxic lower layer, no oxidation can occur. Then, the reaction velocities in equations 8.205 and 8.207 may be expressed as:

$$K_{1,H2S}^{2} = \left(K_{H2S,d1}^{2} \cdot f d_{1,H2S} + K_{H2S,p1}^{2} \cdot f p_{1,H2S}\right) \theta_{H2S}^{T-20} \frac{DO_{0}}{2 \cdot K M_{H2S,O2}}$$
(8.228)

$$K_{2.H2S}^2 = 0 (8.229)$$

where,

 $K_{H2S,d1}$  is the reaction velocity for dissolved  $S_2^-$  oxidation in Layer 1 at  $20^{\circ}C$  (m/day),

 $K_{H2S,p1}$  is the reaction velocity for particulate  $S_2^-$  oxidation in Layer 1 at  $20^{\circ}C$  (m/day),

 $\theta_{H2S}$  is the constant for temperature adjustment for  $K_{H2S,d1}$  and  $K_{H2S,p1}$ , and

 $KM_{H2S,O2}$  is the constant to normalize the  $S_2^-$  oxidation rate for  $O(g O_2/m^3)$ .

The constant  $KM_{H2S,O2}$ , which is included for convenience only, is used to scale the O concentration in the overlying water. At  $DO_0 = KM_{H2S,O2}$ , the reaction velocity for  $S_2^-$  oxidation rate is at its nominal value.

The oxidation reactions in the oxic upper layer cause O flux to the sediment, which exerts SOD. By convention, SOD is positive:  $SOD = -J_{aq,O2}$ . The SOD in the model consists of two components, Carbonaceous Sediment Oxygen Demand (CSOD) due to  $S_2^-$  oxidation and Nitrogenous Sediment Oxygen Demand (NSOD) due to nitrification:

{229}------------------------------------------------

<span id="page-229-0"></span>
$$SOD = CSOD + NSOD = \frac{K_{1,H2S}^2}{s} H2S_1 + a_{O2,NH4} \cdot J_{Nit}$$
 (8.230)

where,

 $H2S_1$  is the total  $S_2^-$  concentration in Layer 1 ( $g O_2 - equivalents/m^2/day$ ), and  $a_{O2.NH4}$  is the stoichiometric coefficient for O consumed by nitrification (4.33  $g O_2$  per g N).

Equation 8.230 is nonlinear for SOD because the RHS contains  $s = SOD/DO_0$  so that SOD appears on both sides of the equation: note that  $J_{Nit}$  (equation 8.217) is also a function of s. A simple back substitution method is used to solve this equation.

If the overlying water DO is low, then the  $S_2^-$  that is not completely oxidized in the upper layer can diffuse into the overlying water. This aqueous  $S_2^-$  flux out of the sediments, which contributes to the COD in the water column model, is modeled using

<span id="page-229-1"></span>
$$J_{aa,H2S} = s(fd_{1,H2S} \cdot H2S_1 - COD)$$
(8.231)

The  $S_2^-$  released from the sediment reacts very quickly in the water column when O is available, but can accumulate in the water column under anoxic conditions. The COD, quantified as O equivalents, is entirely supplied by benthic release in the water column model (equation 8.92). Since  $S_2^-$  also is quantified as O equivalents, COD is used as a measure of  $S_2^-$  in the water column in equation 8.231.

#### 8.3.3.6.2 Methane

When  $SO_4^{-2}$  is used up,  $CH_4$  can be produced by carbon diagenesis and  $CH_4$  oxidation consumes O (Di Toro et al., 1990). Owing to the abundant  $SO_4^{-2}$  in the saltwater, only the aforementioned  $S_2^-$  production and oxidation are considered to occur in the saltwater. Since the  $SO_4^{-2}$  concentration in the freshwater is generally insignificant,  $CH_4$  production is considered to replace  $S_2^-$  production in the freshwater. In the freshwater,  $CH_4$  is produced by carbon diagenesis in the lower layer and is decremented by the OC consumed due to denitrification. No diagenetic production of  $CH_4$  occurs in the upper layer (equation 8.227):

<span id="page-229-3"></span>
$$J_{1,CH4} = 0$$

$$J_{2,CH4} = a_{O2,C} \cdot J_C - a_{O2,NO3} \cdot J_{N2(g)}$$
(8.232)

The dissolved  $CH_4$  produced takes two pathways; (1) oxidation in the oxic upper layer causing CSOD, or (2) escape from the sediment as aqueous flux or as gas flux:

<span id="page-229-2"></span>
$$J_{2.CH4} = CSOD + J_{aa.CH4} + J_{CH4(g)}$$
(8.233)

where,

 $J_{aq,CH4}$  is the aqueous  $CH_4$  flux  $(g O_2 - equivalents/m^2/day)$ , and  $J_{CH4(g)}$  is the gaseous  $CH_4$  flux  $(g O_2 - equivalents/m^2/day)$ .

{230}------------------------------------------------

A portion of dissolved  $CH_4$  that is produced in the anoxic layer diffuses into the oxic layer where it is oxidized. This  $CH_4$  oxidation causes CSOD in the freshwater sediment (Di Toro et al., 1990):

<span id="page-230-2"></span>
$$CSOD = CSOD_{max} \cdot \left(1 - \operatorname{sech}\left[\frac{K_{CH4} \cdot \theta_{CH4}^{T-20}}{s}\right]\right)$$
(8.234)

$$CSOD_{max} = minimum \left\{ \sqrt{2 \cdot KL \cdot CH4_{sat} \cdot J_{2,CH4}}, J_{2,CH4} \right\}$$
(8.235)

<span id="page-230-1"></span>
$$CH4_{sat} = 100\left(1 + \frac{h + H_2}{10}\right)1.024^{20-T} \tag{8.236}$$

where,

 $CSOD_{max}$  is the maximum CSOD occurring when all the dissolved  $CH_4$  transported to the oxic layer is oxidized,

 $K_{CH4}$  is the reaction velocity for dissolved  $CH_4$  oxidation in Layer 1 at 20°C (m/day),

 $\theta_{H2S}$  is the constant for temperature adjustment for  $K_{CH4}$  , and

 $CH4_{sat}$  is the saturation concentration of  $CH_4$  in the pore water ( $g\ O_2 - equivalents/m^3$ ).

The term,  $(h+H_2)/10$  where h and  $H_2$  are in meters, in equation 8.236 is the depth from the water surface that corrects for the in situ pressure. Equation 8.236 is accurate to within 3% of the reported  $CH_4$  solubility between 5 and 20°C (Yamamoto et al., 1976).

If the overlying water O is low, the  $CH_4$  that is not completely oxidized can escape the sediment into the overlying water either as aqueous flux or as gas flux. The aqueous  $CH_4$  flux, which contributes to the COD in the water column model, is modeled using (Di Toro et al., 1990):

<span id="page-230-3"></span>
$$J_{aq,CH4} = CSOD_{max} \cdot \operatorname{sech}\left[\frac{K_{CH4} \cdot \theta_{CH4}^{T-20}}{s}\right] = CSOD_{max} - CSOD$$
(8.237)

 $CH_4$  is only slightly soluble in water. If its solubility  $CH_{3at}$  given by equation 8.236 is exceeded in the pore water, it forms a gas phase that escapes as bubbles. The loss of  $CH_4$  as bubbles, i.e. the gaseous  $CH_4$  flux, is modeled using equation 8.233 with  $J_{2,CH_4}$  from equation 8.232, CSOD from equation 8.234 and  $J_{aq,CH_4}$  from equation 8.237 (Di Toro et al., 1990).

#### <span id="page-230-0"></span>**8.3.4** Silica

The production of  $NH_4^+$ ,  $NO_3^-$  and  $PO_4^{-3}$  in sediments is the result of the mineralization of POM by bacteria. The production of dissolved  $SiO_2$  in sediments is the result of the dissolution of SiP or opaline  $SiO_2$ , which is thought to be independent of bacterial processes. The depositional flux of SiP from the overlying water to the sediments is modeled using equation 8.202. With this source, the mass-balance equation for SiP may be written as:

<span id="page-230-4"></span>
$$H_2 \frac{\partial PSi}{\partial t} = -S_{Si} \cdot H_2 - W \cdot PSi + J_{PSi} + J_{DSi}$$
(8.238)

{231}------------------------------------------------

where,

*Psi* is the concentration of SiP in the sediment  $(g Si/m^3)$ ,

 $S_{Si}$  is the dissolution rate of PSi in Layer 2 (g Si/m<sup>3</sup>/day),

 $J_{Psi}$  is the depositional flux of PSi ( $gSi/m^3/day$ ) given by the equation 8.202, and

 $J_{DSi}$  is the detrital flux of PSi ( $g Si/m^3/day$ ) to account for PSi settling to the sediment that is not associated with the algal flux of biogenic silica.

The processes included in equation 8.238 are dissolution (i.e., production of dissolved silica), burial, and depositional and detrital fluxes from the overlying water. Equation 8.238 can be viewed as the analog of the diagenesis equations for POM (equation 8.203). The dissolution rate is formulated using a reversible reaction that is first order in  $SiO_2$  solubility deficit and follows a Monod-type relationship in SiP:

<span id="page-231-0"></span>
$$S_{Si} = K_{Si} \cdot \theta_{Si}^{T-20} \frac{PSi}{PSi + KH_{PSi}} (Si_{sat} - fd_{2,Si} \cdot Si_2)$$
(8.239)

where,

 $K_{Si}$  is the first order dissolution rate for SiP at  $20^{\circ}C$  in Layer 2 (1/day),

 $\theta_{Si}$  is the constant for temperature adjustment for  $K_{Si}$ ,

 $KM_{PSi}$  is the  $SiO_2$  dissolution half-saturation constant for PSi (g  $Si/m^3$ ), and

 $Si_{sat}$  is the saturation concentration of  $SiO_2$  in the pore water  $(g Si/m^3)$ .

The mass-balance equations for mineralized  $SiO_2$  can be formulated using the general forms, equations 8.205 and 8.207. There is no source/sink term and no reaction in the upper layer:

$$J_{1,Si} = \kappa_{1,Si} = 0 \tag{8.240}$$

In the lower layer,  $SiO_2$  is produced by the dissolution of SiP, which is modeled using equation 8.239. The two terms in equation 8.239 correspond to the source term and reaction term in equation 8.207:

$$J_{2,Si} = K_{Si} \cdot \theta_{Si}^{T-20} \frac{PSi}{PSi + KM_{PSi}} Si_{sat} \cdot H_2$$

$$(8.241)$$

$$\kappa_{2,Si} = K_{Si} \cdot \theta_{Si}^{T-20} \frac{PSi}{PSi + KM_{PSi}} f_{d2,Si} \cdot H_2$$
(8.242)

A portion of  $SiO_2$  dissolved from particulate  $SiO_2$  sorbs to solids and a portion remains in the dissolved form. Partitioning using the partition coefficients  $\pi_{1,Si}$  and  $\pi_{2,Si}$ , in Equations 8.208 and 8.209 controls the extent to which dissolved  $SiO_2$  sorbs to solids. Since  $SiO_2$  shows similar behavior as  $PO_4^{-3}$  in the adsorption-desorption process, the same partitioning method as applied to  $PO_4^{-3}$  is used for  $SiO_2$ . That is, when  $DO_0$  exceeds a critical concentration  $(DO_0)_{crit,Si}$ , sorption in the upper layer is enhanced by an amount  $\Delta \pi_{Si,1}$ :

$$\pi_{1,Si} = \pi_{2,Si} \cdot (\Delta \pi_{Si,1}) \qquad DO_0 > (DO_0)_{crit,Si}$$
(8.243)

When O falls below  $(DO_0)_{crit,Si}$ , then:

{232}------------------------------------------------

$$\pi_{1,Si} = \pi_{2,Si} \cdot (\Delta \pi_{Si,1})^{\frac{DO_0}{(DO_0)_{crit,Si}}} \qquad DO_0 \le (DO_0)_{crit,Si}$$
(8.244)

which smoothly reduces  $\pi_{1,Si}$  to  $\pi_{2,Si}$  as  $DO_0$  goes to zero.

Once equations 8.205 and 8.207 are solved for  $Si_1$  and  $Si_2$ , the sediment flux of  $SiO_2$  to the overlying water  $J_{aa,Si}$ , can be calculated using equation 8.206.

#### <span id="page-232-0"></span>**8.3.5** Sediment Temperature

All rate coefficients in the aforementioned mass-balance equations are expressed as a function of sediment temperature, *T*. The sediment temperature is modeled based on the diffusion of heat between the water column and sediment:

<span id="page-232-2"></span>
$$\frac{\partial T}{\partial t} = \frac{D_T}{H^2} (T_W - T) \tag{8.245}$$

where,

 $D_T$  is the heat diffusion coefficient between the water column and sediment  $(m^2/s)$ , and

 $T_W$  is the temperature in the overlying water column (°C) calculated by equation 8.121.

The model application in (Di Toro and Fitzpatrick, 1993) and (Cerco and Cole, 1994) used  $D_T = 1.8 \times 10^{-7}$   $m^2/s$ .

#### <span id="page-232-1"></span>8.3.6 Method of Solution

#### 8.3.6.1 Finite-Difference Equations and Solution Scheme

An implicit integration scheme is used to solve the governing mass-balance equations for ammonium, nitrate, phosphate or sulfide/methane in the upper and lower layer. The finite difference form of equation 8.205 may be expressed as:

$$0 = s \left( f d_0 \cdot C t_o' - f d_1 \cdot C t_1' \right) + KL \left( f d_2 \cdot C t_2' - f d_1 \cdot C t_1' \right)$$

$$+ \omega \left( f p_2 \cdot C t_2' - f p_1 \cdot C t_1' \right) - W \cdot C t_1' - \frac{K_1^2}{s} C t_1' + J_1' \quad (8.246)$$

where the primed variables designate the values evaluated at t+ and the unprimed variables are those at t, where  $\theta$  is defined in equation 8.121.

The finite difference form of equation 8.207 may be expressed as:

$$0 = -KL\left(fd_{2} \cdot Ct_{2}^{'} - fd_{1} \cdot Ct_{1}^{'}\right) - \omega\left(fp_{2} \cdot Ct_{2}^{'} - fp_{1} \cdot Ct_{1}^{'}\right) + W\left(Ct_{1}^{'} - Ct_{2}^{'}\right) - \left(K_{2} + \frac{H_{2}}{\theta}\right)Ct_{2}^{'} + \left(J_{2}^{'} + \frac{H_{2}}{\theta}Ct_{2}\right)$$
(8.247)

{233}------------------------------------------------

The two terms  $-(H_2/\theta)Ct_2'$  and  $(H_2/\theta)Ct_2$ , are from the derivative term  $H_2(\partial Ct_2/\partial t)$  in equation 8.207. Each of these terms simply add to the Layer 2 removal rate and the forcing function, respectively. Setting these two terms equal to zero results in the steady-state model. The two unknowns  $Ct_1'$  and  $Ct_2'$ , can be calculated at every time step using:

$$\begin{bmatrix} s \cdot f d_1 + a_1 + \frac{K_1^2}{s} & -a_2 \\ -a_1 & a_2 + W + K_2 + \frac{H_2}{\theta} \end{bmatrix} \begin{bmatrix} Ct_1' \\ Ct_2' \end{bmatrix} = \begin{bmatrix} J_1' + s \cdot f d_0 \cdot Ct_0' \\ J_2' + \frac{H_2}{\theta} Ct_2 \end{bmatrix}$$
(8.248)

<span id="page-233-0"></span>
$$a_1 = KL \cdot f d_1 + \omega \cdot f p_1 + W$$

$$a_2 = KL \cdot f d_2 + \omega \cdot f p_2$$
(8.249)

The solution of equation 8.248 requires an iterative method since the surface mass transfer coefficient, s is a function of the SOD (equation 8.210), which is also a function of s (equation 8.230). A simple back substitution method is used:

- 1. Start with an initial estimate of SOD, for example,  $SOD = a_{O2,C}J_C$  or the previous time step SOD.
- 2. Solve equation 8.248 for  $NH_4^+$ ,  $NO_3^-$ , and  $S_2^-/CH_4$ .
- 3. Compute the SOD using equation 8.230.
- 4. Refine the estimate of SOD: a root finding method (Brent's method in Press et al. (1986)) is used to make the new estimate.
- 5. Go to (2) if no convergence.
- 6. Solve equation 8.248 for  $PO_4^{-3}$  and  $SiO_2$ .

For the sake of symmetry, the equations for diagenesis, SiP and sediment temperature are also solved in implicit form. The finite difference form of the diagenesis equation (equation 8.203) may be expressed as:

$$G_{POM,i}^{'} = \left(G_{POM,i} + \frac{\theta}{H_2}J_{POM,i}\right) \left(1 + \theta \cdot K_{POM,i} \cdot \theta_{POM,i}^{T-20} + \frac{\theta}{H_2}W\right)^{-1}$$
(8.250)

The finite difference form of the SiP equation (equation 8.238) may be expressed as:

$$PSi' = \left(PSi + \frac{\theta}{H_2}(J_{PSi} + J_{DSi})\right) \left(1 + \theta \cdot K_{Si} \cdot \theta_{Si}^{T-20} \frac{Si_{sat} - f_{d2,Si} \cdot Si_2}{PSi + KM_{PSi}} + \frac{\theta}{H_2}W\right)^{-1}$$
(8.251)

using equation 8.233 for the dissolution term, in which *PSi* in the Monod-type term has been kept at time level *t* to simplify the solution. The finite difference form of the sediment temperature, shown in equation 8.245, may be expressed as:

$$T' = \left(T + \frac{\theta}{H^2} D_T \cdot T_W\right) \left(1 + \frac{\theta}{H^2} D_T\right)^{-1}$$
 (8.252)

{234}------------------------------------------------

## 8.3.6.2 Boundary and Initial Conditions

The above finite difference equations constitute an initial boundary-value problem. The boundary conditions are the depositional fluxes (*JPOM*,*<sup>i</sup>* and *JPSi*) and the overlying water conditions (*Ct*<sup>0</sup> and *T<sup>W</sup>* ) as a function of time, which are provided from the water column water quality model. The initial conditions are the concentrations at *t* = 0, *GPOM*,*i*(0), *PSi*(0), *Ct*1(0), *Ct*2(0) and *T*(0), to start the computations. Strictly speaking, these initial conditions should reflect the past history of the overlying water conditions and depositional fluxes, which is often impractical because of lack of field data for these earlier years.

#### <span id="page-234-0"></span>8.4. Appendix

The appendix includes values of some parameters based on literature review and professional experiences. Parameters of three legacy algae groups cyanobacteria (C), diatoms (D), and green algae (G) are presented in Table [8.16.](#page-234-1) These values may be used as a starting point for the model calibration process.

Table 8.16. Parameters Related to Algae in Water Column

<span id="page-234-1"></span>

| Parameter                                  | Valuea                                      | Equation Numberb |
|--------------------------------------------|---------------------------------------------|------------------|
| ∗PMc<br>(1/day)                            | 2.5 (upper Potomac only)                    | 8.7              |
| ∗PMd<br>(1/day)                            | 2.25                                        | 8.7              |
| ∗PMg<br>(1/day)                            | 2.5                                         | 8.7              |
| 3<br>KHNx<br>(g N/m<br>)                   | 0.01 (all groups)                           | 8.8              |
| 3<br>KHPx<br>(g P/m<br>)                   | 0.001 (all groups)                          | 8.8              |
| 3<br>KHS (g Si/m<br>)                      | 0.05                                        | 8.8              |
| FD                                         | Temporally-varying input                    | 8.9              |
| Isx<br>(langleys/day)                      | Temporally-varying input                    | 8.10             |
| ∗Keb<br>(1/m)                              | spatially-varying input                     | 8.134            |
| (1/m per m3<br>KeISS<br>)                  | NAc                                         | 8.134            |
| 3<br>KeChl<br>(1/m per mg Chl/m<br>)       | 0.017                                       | 8.134            |
| CChlx<br>(g C per mg Chl)                  | 0.06 (all groups)                           | 8.134            |
| (Dopt)x<br>(m)                             | 1.0 (all groups)                            | 8.12             |
| (Is)min<br>(langleys/day)                  | 40.0                                        | 8.12             |
| CIa, CIb<br>and CIc                        | 0.7, 0.2 & 0.1                              | 8.13             |
| oC)<br>T Mc, T Md<br>and T Mg<br>(         | 27.5, 20.0 & 25.0                           | 8.14             |
| oC<br>−2<br>KT G1c<br>and KT G2c<br>(<br>) | 0.005 & 0.004                               | 8.14             |
| −2<br>oC<br>KT G1d<br>and KT G2d<br>(<br>) | 0.004 & 0.006                               | 8.14             |
| oC<br>−2<br>KT G1g<br>and KT G2g<br>(<br>) | 0.008 & 0.01                                | 8.14             |
| STOX (ppt)                                 | 1.0                                         | 8.15             |
| ∗BMRc<br>(1/day)                           | 0.04                                        | 8.16             |
| ∗BMRd<br>(1/day)                           | 0.01 (0.03 during JanMay in saltwater only) | 8.16             |
| ∗BMRg<br>(1/day)                           | 0.01                                        | 8.16             |
| oC)<br>T Rx, (                             | 20.0 (all groups)                           | 8.16             |
| oC<br>−1<br>KT Bx<br>(<br>)                | 0.069 (all groups)                          | 8.16             |
|                                            | Continued on next page                      |                  |

222

{235}------------------------------------------------

Table 8.16 – continued from previous page

| Parameter        | Valuea                                         | Equation Numberb |
|------------------|------------------------------------------------|------------------|
| ∗PRRc<br>(1/day) | 0.01                                           | 8.17             |
| ∗PRRd<br>(1/day) | 0.215 (0.065 during Jan-May in saltwater only) | 8.17             |
| ∗PRRg<br>(1/day) | 0.215                                          | 8.17             |
| ∗WSc<br>(m/day)  | 0.0                                            | 8.6              |
| ∗WSd<br>(m/day)  | 0.35 (Jan-May), 0.1 (Jun-Dec)                  | 8.6              |
| ∗WSg<br>(m/day)  | 0.1                                            | 8.6              |

<sup>a</sup> The evaluation of these values is detailed in Chapter IX of [\(Cerco and Cole,](#page-259-0) [1994\)](#page-259-0).

Table 8.17. Parameters Related to Zooplankton in Water Column

<span id="page-235-0"></span>

| (gN g−1C)<br>0.2<br>8.7<br>(gP g−1C)<br>0.02<br>8.8<br>(1/day)<br>0.254<br>8.8<br>(mgC/l)<br>0.01<br>8.8<br>(mgDO/l)<br>2<br>8.9<br>0 ≤ FCRDZz<br>≤ 1<br>8.10<br>0 ≤ FCRPZz<br>≤ 1<br>8.10<br>0 ≤ FCLDZz<br>≤ 1<br>8.10<br>0 ≤ FCLPZz<br>≤ 1<br>8.10<br>0 ≤ FCDDZz<br>≤ 1<br>8.10<br>FCDPZz<br>0 ≤ FCDPZz<br>≤ 1<br>8.10<br>0 ≤ FPRDZz<br>≤ 1<br>FPRDZz<br>8.10<br>FPRPZz<br>0 ≤ FPRPZz<br>≤ 1<br>8.10<br>0 ≤ FPLDZz<br>≤ 1<br>8.10<br>0 ≤ FPLPZz<br>≤ 1<br>FPLPZz<br>8.10<br>FPDBZz<br>0 ≤ FPDBZz<br>≤ 1<br>8.10<br>0 ≤ FPDDZz<br>≤ 1<br>FPDPZz<br>8.10<br>FPDPZz<br>0 ≤ FPDPZz<br>≤ 1<br>8.10<br>FPIBZz<br>0 ≤ FPIBZz<br>≤ 1<br>8.10<br>0 ≤ FPIDZz<br>≤ 1<br>FPIPZz<br>8.10<br>FPIPZz<br>0 ≤ FPIPZz<br>≤ 1<br>8.10<br>0 ≤ FNRDZz<br>≤ 1<br>FNRDZz<br>8.10<br>FNRPZz<br>0 ≤ FNRPZz<br>≤ 1<br>8.10<br>FNLDZz<br>0 ≤ FNLDZz<br>≤ 1<br>8.10<br>0 ≤ FNLPZz<br>≤ 1<br>8.10<br>Continued on next page | Parameter | Valuea | Equation Numberb |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------|------------------|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | ANCz      |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | APCz      |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | BMRz      |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | CTz       |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | DOCRITz   |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | FCRDZz    |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | FCRPZz    |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | FCLDZz    |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | FCLPZz    |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | FCDDZz    |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | FPLDZz    |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | FNLPZz    |        |                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           |        |                  |

<sup>b</sup> The equation number where the corresponding parameter is first shown and defined.

<sup>c</sup> Not available in [\(Cerco and Cole,](#page-259-0) [1994\)](#page-259-0) since their formulations do not include these parameters.

<sup>\*</sup> The parameters are declared as an array in the source code.

{236}------------------------------------------------

Table 8.17 – continued from previous page

| FNDBZz                                 | 0 ≤ FNDBZz<br>≤ 1 | 8.10 |     |
|----------------------------------------|-------------------|------|-----|
| FNDPZz                                 | 0 ≤ FNDDZz<br>≤ 1 | 8.10 |     |
| FNDPZz                                 | 0 ≤ FNDPZz<br>≤ 1 | 8.10 |     |
| FNIBZz                                 | 0 ≤ FNIBZz<br>≤ 1 | 8.10 |     |
| FNIDZz                                 | 0 ≤ FNIDZz<br>≤ 1 | 8.10 |     |
| FNIPZz                                 | 0 ≤ FNIPZz<br>≤ 1 | 8.10 |     |
| FSPDZz                                 | 0 ≤ FSPDZz<br>≤ 1 | 8.10 |     |
| FSPPZz                                 | 0 ≤ FSPPZz<br>≤ 1 | 8.10 |     |
| FSADZz                                 | 0 ≤ FSADZz<br>≤ 1 | 8.10 |     |
| FSAPZz                                 | 0 ≤ FSAPZz<br>≤ 1 | 8.10 |     |
| KHCz<br>, (mgC/l)                      | 0.05              | 8.16 |     |
| oC<br>−1<br>KT Bz<br>(<br>)            | 0.069             | 8.16 |     |
| oC<br>−2<br>KTg1<br>(<br>)             | 0.0035            | 8.16 |     |
| −2<br>oC<br>KTg2<br>(<br>)             | 0.025             | 8.16 |     |
| (1/day)<br>DZEROz                      | 4.0               | 8.17 |     |
| (g preyCg−1<br>zooplCd−1<br>RMAXz<br>) | 2.25              |      | 8.6 |
| oC)<br>Topt1<br>(                      | 25                |      | 8.6 |
| oC)<br>Topt2<br>(                      | 25                |      | 8.6 |
| oC)<br>T Rz<br>(                       | 20                |      | 8.6 |
| oC)<br>UBzs<br>(                       | 0 ≤ UBzs<br>≤ 1   |      | 8.6 |
| oC)<br>ULz<br>(                        | 0 ≤ ULz<br>≤ 1    |      | 8.6 |
| oC)<br>URz<br>(                        | 0 ≤ URz<br>≤ 1    |      | 8.6 |
|                                        |                   |      |     |

<sup>a</sup> The evaluation of these values is detailed in Chapter VIII of (Cerco and Cole, 2004).

<sup>b</sup> The equation number where the corresponding parameter is first shown and defined.

{237}------------------------------------------------

Table 8.18. Parameters Related to Organic Carbon (*OC*) in Water Column

<span id="page-237-0"></span>

| Parameter                            | Valuea            | Equation Numberb |
|--------------------------------------|-------------------|------------------|
| FCRPx                                | 0.35 (all groups) | 8.41             |
| FCLPx                                | 0.55 (all groups) | 8.42             |
| FCDPx                                | 0.10 (all groups) | 8.44             |
| FCDx                                 | 0.0 (all groups)  | 8.44             |
| ∗WSRP<br>(m/day)                     | 1.0               | 8.41             |
| ∗WSLP<br>(m/day)                     | 1.0               | 8.42             |
| 3<br>KHRx<br>(g O2/m<br>)            | 0.5 (all groups)  | 8.44             |
| 3<br>(g O2/m<br>KHORDO<br>)          | 0.5               | 8.52             |
| KRC<br>(1/day)                       | 0.005             | 8.53             |
| KLC<br>(1/day)                       | 0.075             | 8.54             |
| KDC<br>(1/day)                       | 0.01              | 8.55             |
| 3<br>KRCalg<br>(1/day per g C/m<br>) | 0.0               | 8.53             |
| 3<br>(1/day per g C/m<br>KLCalg<br>) | 0.0               | 8.54             |
| 3<br>KDCalg<br>(1/day per g C/m<br>) | 0.0               | 8.55             |
| OC)<br>T RHDR<br>(                   | 20.0              | 8.53             |
| OC)<br>T RMIN<br>(                   | 20.0              | 8.55             |
| −1<br>OC<br>KTHDR<br>(<br>)          | 0.069             | 8.53             |
| OC<br>−1<br>KTMIN<br>(<br>)          | 0.069             | 8.55             |
| 3<br>KHDNN<br>(g N/m<br>)            | 0.1               | 8.57             |
| AANOX                                | 0.5               | 8.57             |

<sup>a</sup> The evaluation of these values is detailed in Chapter IX of [\(Cerco and Cole,](#page-259-0) [1994\)](#page-259-0).

<sup>b</sup> The equation number where the corresponding parameter is first shown and defined.

<sup>\*</sup> The parameters are declared as an array in the source code.

{238}------------------------------------------------

Table 8.19. Parameters Related to Phosphorus (*P*) in Water Column

<span id="page-238-0"></span>

| Parameter                             | Valuea           | Equation Numberb |
|---------------------------------------|------------------|------------------|
| FPLPx                                 | 0.2 (all groups) | 8.59             |
| FPDPx                                 | 0.5 (all groups) | 8.60             |
| FPIPx                                 | 0.2 (all groups) | 8.61             |
| FPRx                                  | 0.0 (all groups) | 8.58             |
| FPLx                                  | 0.0 (all groups) | 8.59             |
| FPDx                                  | 1.0 (all groups) | 8.60             |
| FPIx                                  | 0.0 (all groups) | 8.61             |
| ∗WSs<br>(m/day)                       | 1.0              | 8.61             |
| 3<br>(per g/m<br>KPO4p<br>) for TSS   | NA               | 8.62             |
| 3<br>KPO4p<br>(per mol/m<br>) for TAM | 6.0              | 8.62             |
| CPprm1<br>(g C per g P)               | 42.0             | 8.65             |
| CPprm2<br>(g C per g P)               | 85.0             | 8.65             |
| 3<br>CPprm3<br>(per g P/m<br>)        | 200.0            | 8.65             |
| (1/day)<br>KRP                        | 0.005            | 8.66             |
| KLP<br>(1/day)                        | 0.075            | 8.67             |
| KDP<br>(1/day)                        | 0.1              | 8.68             |
| 3<br>KRPalg<br>(1/day per g C/m<br>)  | 0.0              | 8.66             |
| 3<br>KLPalg<br>(1/day per g C/m<br>)  | 0.0              | 8.67             |
| 3<br>(1/day per g C/m<br>KDPalg<br>)  | 0.2              | 8.68             |

<sup>a</sup> The evaluation of these values are detailed in Chapter IX of [\(Cerco and Cole,](#page-259-0) [1994\)](#page-259-0).

<sup>b</sup> The equation number where the corresponding parameter is first shown and defined.

<sup>c</sup> Not available in [\(Cerco and Cole,](#page-259-0) [1994\)](#page-259-0) since their formulations do not include these parameters.

<sup>:</sup> *FPI<sup>x</sup>* is estimated from *FPR<sup>x</sup>* +*FPL<sup>x</sup>* +*FPD<sup>x</sup>* +*FPI<sup>x</sup>* = 1.

<sup>\*</sup> The parameters declared as an array in the source code.

{239}------------------------------------------------

Table 8.20. Parameters Related to Nitrogen (*N*) in Water Column

<span id="page-239-0"></span>

| Parameter                            | Valuea             | Equation Numberb |
|--------------------------------------|--------------------|------------------|
| FNLPx                                | 0.55 (all groups)  | 8.71             |
| FNDPx                                | 0.1 (all groups)   | 8.72             |
| FNIPx                                | 0.0 (all groups)   | 8.73             |
| FNRx                                 | 0.0 (all groups)   | 8.70             |
| FNLx                                 | 0.0 (all groups)   | 8.71             |
| FNDx                                 | 1.0 (all groups)   | 8.72             |
| FNIx                                 | 0.0 (all groups)   | 8.73             |
| ANCx<br>(g; N; per g C)              | 0.167 (all groups) | 8.70             |
| ANDC (g; N; per g C)                 | 0.933              | 8.74             |
| KRN<br>(1/day)                       | 0.005              | 8.76             |
| KLN<br>(1/day)                       | 0.075              | 8.77             |
| KDN<br>(1/day)                       | 0.015              | 8.78             |
| 3<br>(1/day per g C/m<br>KRNalg<br>) | 0.0                | 8.76             |
| 3<br>KLNalg<br>(1/day per g C/m<br>) | 0.0                | 8.77             |
| 3<br>KDNalg<br>(1/day per g C/m<br>) | 0.2                | 8.78             |
| 3/day)<br>Nitm<br>(g N/m             | 0.07               | 8.81             |
| 3<br>KHNitDO<br>(g N/m<br>)          | 1.0                | 8.81             |
| 3<br>(g O2/m<br>KHNitN<br>)          | 1.0                | 8.81             |
| oC)<br>T Nit (                       | 27.0               | 8.82             |
| oC<br>−2<br>KNit (<br>)              | 0.0045             | 8.82             |
| oC<br>−2<br>KNit (<br>)              | 0.0045             | 8.82             |

<sup>a</sup> The evaluation of these values are detailed in Chapter IX of [\(Cerco and Cole,](#page-259-0) [1994\)](#page-259-0).

<sup>b</sup> The equation number where the corresponding parameter is first shown and defined.

{240}------------------------------------------------

<span id="page-240-0"></span>Parameter Value<sup>a</sup> Equation Number<sup>b</sup> *FSPP<sup>d</sup>* 1.0 [8.85](#page-185-0) *FSIP<sup>d</sup>* 0.0 [8.86](#page-186-0) *FSP<sup>d</sup>* 1.0 [8.85](#page-185-0) *FSI<sup>d</sup>* 0.0 [8.86](#page-186-0) *ASC<sup>d</sup>* (*g Si per g C*) 0.5 [8.85](#page-185-0) 3

) for TSS NA [8.87](#page-187-0)

) for TAM 6.0 [8.87](#page-187-0)

Table 8.21. Parameters Related to Silica (*SiO*2) in Water Column

*KSU* (1/*day*) 0.03 [8.91](#page-187-1)

*<sup>o</sup>*C) 20.0 [8.91](#page-187-1)

) 0.092 [8.91](#page-187-1)

*KSAp* (*per g*/*m*

*T RSUA* (

*KTSUA* (

*KSAp* (*per mol*/*m*

*o*C −1 3

<span id="page-240-1"></span>Table 8.22. Parameters Related to Carbonaceous Oxygen Demand (*COD*) and Dissolved Oxygen (*DO*) in Water Column

| Parameter                   | Valuea              | Equation Numberb |
|-----------------------------|---------------------|------------------|
| 3<br>KHCOD<br>(g O2/m<br>)  | 1.5                 | 8.92             |
| KCD<br>(1/day)              | 20.0                | 8.93             |
| oC)<br>T RCOD<br>(          | 20.0                | 8.93             |
| oC<br>−1<br>KTCOD<br>(<br>) | 0.041               | 8.93             |
| AOCR (g O2<br>per g C)      | 2.67                | 8.94             |
| AONT (g O2<br>per g N)      | 4.33                | 8.93             |
| KR<br>(in MKS unit)         | 3.933               | 8.94             |
| KTr                         | 1.024 (1.005-1.030) | 8.109            |

<sup>a</sup> The evaluation of these values are detailed in Chapter IX of [Cerco and Cole](#page-259-0) [\(1994\)](#page-259-0).

<sup>a</sup> The evaluation of these values are detailed in Chapter IX of [\(Cerco and Cole,](#page-259-0) [1994\)](#page-259-0).

<sup>b</sup> The equation number where the corresponding parameter is first shown and defined.

<sup>c</sup> Not available in [\(Cerco and Cole,](#page-259-0) [1994\)](#page-259-0) since their formulations do not include these parameters.

<sup>:</sup> *FSPP<sup>d</sup>* and *FSIP<sup>d</sup>* are estimated from *FSPP<sup>d</sup>* +*FSIP<sup>d</sup>* = 1.

<sup>:</sup> *FSP<sup>d</sup>* and *FSI<sup>d</sup>* are estimated from *FSP<sup>d</sup>* +*FSI<sup>d</sup>* = 1.

<sup>b</sup> The equation number where the corresponding parameter is first shown and defined.

<sup>c</sup> Not available in [\(Cerco and Cole,](#page-259-0) [1994\)](#page-259-0) since their formulations do not include these parameters.

<sup>:</sup> Kro is from O'Connor & Dobbins [O'Connor and Dobbins](#page-263-21) [\(1958\)](#page-263-21).

<sup>:</sup> KTr is from Thomann & Mueller [Thomann and Mueller](#page-265-20) [\(1987\)](#page-265-20).

{241}------------------------------------------------

<span id="page-241-0"></span>Table 8.23. Parameters Related to Total Active Metals (TAM) and Fecal Coliform Bacteria in Water Column

| Parameter                | Valuea               | Equation Numberb |
|--------------------------|----------------------|------------------|
| 3<br>KHbm f (g O2/m<br>) | 0.5                  | 8.112            |
| 2/day)<br>BFTAM (mol/m   | 0.01                 | 8.112            |
| oC)<br>Ttam (            | 20.0                 | 8.112            |
| oC<br>−1<br>Ktam (<br>)  | 0.2                  | 8.112            |
| 3<br>TAMdmx (mol/m<br>)  | 0.015                | 8.113            |
| Kdotam (per g O2/m3<br>) | 1.0                  | 8.113            |
| KFCB (1/day)             | 0.0 - 6.1 (seawater) | 8.115            |
| oC<br>−1<br>T FCB (<br>) | 1.07                 | 8.115            |

<sup>a</sup> The evaluation of these values is detailed in Chapter IX of [Cerco and Cole](#page-259-0) [\(1994\)](#page-259-0).

<span id="page-241-1"></span>Table 8.24. Assignment of Water Column Particulate Organic Matter (POM) to Sediment G Classes used in [\(Cerco and Cole,](#page-259-0) [1994\)](#page-259-0)

| WCM Variable                        | Carbon & Phosphorus |       | Nitrogen |      |      |      |
|-------------------------------------|---------------------|-------|----------|------|------|------|
|                                     | G1                  | G2    | G3       | G1   | G2   | G3   |
| A. "stand alone" model              | 0.65                | 0.20  | 0.15     | 0.65 | 0.25 | 0.10 |
| B. coupled model Labile Particulate | 1.0                 | 0.0   | 0.0      | 1.0  | 0.0  | 0.0  |
| Refractory Particulatea             |                     |       |          |      |      |      |
| : Bay and Tributary Zones 1         | 0.0                 | 0.11  | 0.89     | 0.0  | 0.26 | 0.74 |
| : Bay Zones 2 and 10                | 0.0                 | 0.43  | 0.57     | 0.0  | 0.54 | 0.46 |
| : All Other Zones                   | 0.0                 | 0.73  | 0.27     | 0.0  | 0.82 | 0.18 |
| Algae                               | 0.65                | 0.255 | 0.095    | 0.65 | 0.28 | 0.07 |

<span id="page-241-2"></span><sup>a</sup> See [\(Cerco and Cole,](#page-259-0) [1994,](#page-259-0) Figure 10-6) for the Zones definition.

Table 8.25. Sediment Burial Rates (W) Used in [\(Cerco and Cole,](#page-259-0) [1994\)](#page-259-0)

| Bay Zonesa | Rate (cm/yr) | Tributary Zonesa | Rate (cm/yr) |
|------------|--------------|------------------|--------------|
| 1, 2, 10   | 0.50         | 1                | 0.50         |
| 3, 6, 9    | 0.25         | 2, 3             | 0.25         |
| 7, 8       | 0.37         |                  |              |

<sup>a</sup> See [\(Cerco and Cole,](#page-259-0) [1994,](#page-259-0) Figure 10-6) for the definition of Zones.

<sup>b</sup> The equation number where the corresponding parameter is first shown and defined.

<sup>c</sup> Not available in [Cerco and Cole](#page-259-0) [\(1994\)](#page-259-0) since their formulations do not include these parameters.

<sup>:</sup> *KFCB* and *T FCB* are from [Thomann and Mueller](#page-265-20) [\(1987\)](#page-265-20).

{242}------------------------------------------------

## <span id="page-242-0"></span>Chapter 9

## LAGRANGIAN PARTICLE TRACKING

The Lagrangian Particle Tracking [\(LPT\)](#page-11-7) module in [EFDC+](#page-11-0) is developed as an effective tool for solving numerous problems in fluid dynamics related to the simulation and prediction of the trajectory of objects traveling in rivers, lakes, and marine systems. DSI has calibrated [EFDC+](#page-11-0) with [LPT](#page-11-7) module using a simple analytical calculation for quasi-steady state and uniform flow in an open channel. In addition, several tests with different hydrodynamic regimes and geometries have been performed. The soundness of this module was also demonstrated in a variety of applications [\(DSI,](#page-260-23) [2009\)](#page-260-23). Through the simulations, it was found that not only the velocity field but also the randomness and diffusion due to turbulence also considerably impact the dispersion of the cluster and behavior of drifter trajectories.

Study of the trajectories of movement of solid particles in a fluid environment appeared very early in mechanics and was considered as a movement in a Lagrangian approach. The advantage of this method is that it is possible to track the process of movement for each specific particle in more detail and more accurately in comparison with the method of determining average concentration for grid cells. However, the solution was too difficult to implement in practice when the number of particles was very large because of computation costs. With the reduction in computing costs it is now easier to implement the solutions to these problems. The movement of solid particles is decided by a field of fluid velocity, therefore it is necessary to couple it to a fluid flow model.

#### <span id="page-242-1"></span>9.1. Basic Equations

The governing equations used in [EFDC+](#page-11-0) are Navier-Stokes for fluid flow, the advection-diffusion equations for salinity, temperature, dye, toxic substances and suspended sediment transport [\(Hamrick and Wu,](#page-261-8) [1997;](#page-261-8) [Hamrick,](#page-261-3) [1992,](#page-261-3) [1996\)](#page-261-7). The equations are presented in curvilinear coordinate system for 2DH and [SIG](#page-12-0) coordinates for the vertical direction. They are discretized with the finite difference method with explicit scheme. It should be noted that the hypothesis of hydrostatic pressure is used in [EFDC+.](#page-11-0) However, the effect of non-hydrostatic pressure is not important when the vertical velocity of flow is not very large in comparison with the horizontal components as mentioned in [Huu Chung and Eppel](#page-261-25) [\(2008\)](#page-261-25).

The advection-diffusion equation for mass transport in a three dimensional curvilinear orthogonal coordinate system is:

<span id="page-242-2"></span>
$$\frac{\partial C}{\partial t} + \frac{\partial (uC)}{\partial x} + \frac{\partial (vC)}{\partial y} + \frac{\partial (wC)}{\partial z} = \frac{\partial}{\partial x} \left( A_H \frac{\partial C}{\partial x} \right) + \frac{\partial}{\partial y} \left( A_H \frac{\partial C}{\partial y} \right) + \frac{\partial}{\partial z} \left( A_b \frac{\partial C}{\partial z} \right)$$
(9.1)

where,

*t* is time,

(*x*, *y*,*z*) are Lagrangian coordinates of a particle,

{243}------------------------------------------------

*C* is concentration,

(*u*, *v*,*w*) are velocity components of fluid flow, and

*A<sup>H</sup>* and *A<sup>b</sup>* are the horizontal and vertical diffusion coefficients, respectively.

The differential equations for the Lagrangian movement of particles is consistent with the equation [\(9.1\)](#page-242-2) and are as follows:

<span id="page-243-0"></span>
$$dx = \left(u + \frac{\partial A_H}{\partial x}\right)dt + (2p - 1)\sqrt{2A_H dt}$$
(9.2)

$$dy = \left(v + \frac{\partial A_H}{\partial y}\right) dt + (2p - 1)\sqrt{2A_H dt}$$
(9.3)

<span id="page-243-1"></span>
$$dz = \left(w + \frac{\partial A_b}{\partial z}\right)dt + (2p - 1)\sqrt{2A_b dt}$$
(9.4)

In which *dt* is the time step and *p* is a random number from a uniformly distributed random variable generator with a mean value of 0.5. When transformed using 2*p* − 1, the random component has a mean of zero and a range from -1 to 1. The transformed random value allows the diffusion term to move particles +/− about the advected position. Equations [\(9.2\)](#page-243-0) to [\(9.4\)](#page-243-1) follow the 3D random walk approach used by [Dunsbergen and Stelling](#page-260-24) [\(1993\)](#page-260-24).

In order to determine the Lagrangian trajectory of the particle, the equations [\(9.2\)](#page-243-0) to [\(9.4\)](#page-243-1) were incorporated into [EFDC+](#page-11-0) model. The numerical solution was separately divided into the advective transport and random components as described above. This approach allows the user to enable (i.e. turn on random walk) or disable (advective transport only) the random components for either the horizontal and/or the vertical directions.

Three options are available for the solution of the differential equations [\(9.2\)](#page-243-0) to [\(9.4\)](#page-243-1). They are explicit Euler, predictorcorrector Euler, and forth order Runge-Kutta. Their discretization for the equations are as follows:

Explicit Euler method: This method is very simple with the approximation of *O*(∆*t*)

$$x_{n+1} = x_n + u(t_n, x_n, y_n, z_n) \Delta t$$
(9.5)

<span id="page-243-2"></span>
$$y_{n+1} = y_n + v(t_n, x_n, y_n, z_n) \Delta t$$
 (9.6)

$$z_{n+1} = z_n + w(t_n, x_n, y_n, z_n) \Delta t$$
(9.7)

Predictor-corrector Euler method: This method has the advantage of explicit and implicit features with the approximation of *O*(∆*t* 2 )

$$x_{n+1} = x_n + \frac{1}{2} \left[ u(t_n, x_n, y_n, z_n) + u(t_{n+1}, x_{n+1}^p, y_{n+1}^p, z_{n+1}^p) \right] \Delta t$$
(9.8)

$$y_{n+1} = y_n + \frac{1}{2} \left[ v(t_n, x_n, y_n, z_n) + v(t_{n+1}, x_{n+1}^p, y_{n+1}^p, z_{n+1}^p) \right] \Delta t$$
(9.9)

$$z_{n+1} = z_n + \frac{1}{2} \left[ w(t_n, x_n, y_n, z_n) + w(t_{n+1}, x_{n+1}^p, y_{n+1}^p, z_{n+1}^p) \right] \Delta t$$
(9.10)

where , *x p n*+1 , *y p n*+1 ,*z p n*+1 are calculated by equations [\(9.4\)](#page-243-1) to [\(9.6\)](#page-243-2)

Runge-Kutta 4 method: This method has the approximation of *O*(∆*t* 4 ) and has been shown in testing that it is the best option of the three solution techniques provided

{244}------------------------------------------------

$$x_{n+1} = x_n + \frac{1}{6} \left( \Delta x_1 + 2\Delta x_2 + 2\Delta x_3 + \Delta x_4 \right)$$
 (9.11)

$$y_{n+1} = y_n + \frac{1}{6} \left( \Delta y_1 + 2\Delta y_2 + 2\Delta y_3 + \Delta y_4 \right)$$
 (9.12)

$$z_{n+1} = z_n + \frac{1}{6} \left( \Delta z_1 + 2\Delta z_2 + 2\Delta z_3 + \Delta z_4 \right)$$
 (9.13)

in which

$$\Delta x_1 = u(t_n, x_n, y_n, z_n) \Delta t \tag{9.14}$$

$$\Delta y_1 = v(t_n, x_n, y_n, z_n) \Delta t \tag{9.15}$$

$$\Delta z_1 = w(t_n, x_n, y_n, z_n) \Delta t \tag{9.16}$$

$$\Delta x_2 = u \left( t_n + \frac{1}{2} \Delta t, x_n + \frac{1}{2} \Delta x_1, y_n + \frac{1}{2} \Delta y_1, z_n + \frac{1}{2} \Delta z_1 \right) \Delta t \tag{9.17}$$

$$\Delta y_2 = v \left( t_n + \frac{1}{2} \Delta t, x_n + \frac{1}{2} \Delta x_1, y_n + \frac{1}{2} \Delta y_1, z_n + \frac{1}{2} \Delta z_1 \right) \Delta t \tag{9.18}$$

$$\Delta z_2 = w \left( t_n + \frac{1}{2} \Delta t, x_n + \frac{1}{2} \Delta x_1, y_n + \frac{1}{2} \Delta y_1, z_n + \frac{1}{2} \Delta z_1 \right) \Delta t$$
 (9.19)

$$\Delta x_3 = u \left( t_n + \frac{1}{2} \Delta t, x_n + \frac{1}{2} \Delta x_2, y_n + \frac{1}{2} \Delta y_2, z_n + \frac{1}{2} \Delta z_2 \right) \Delta t \tag{9.20}$$

$$\Delta y_3 = v \left( t_n + \frac{1}{2} \Delta t, x_n + \frac{1}{2} \Delta x_2, y_n + \frac{1}{2} \Delta y_2, z_n + \frac{1}{2} \Delta z_2 \right) \Delta t \tag{9.21}$$

$$\Delta z_3 = w \left( t_n + \frac{1}{2} \Delta t, x_n + \frac{1}{2} \Delta x_2, y_n + \frac{1}{2} \Delta y_2, z_n + \frac{1}{2} \Delta z_2 \right) \Delta t$$
 (9.22)

$$\Delta x_4 = u \left( t_n + \Delta t, x_n + \Delta x_3, y_n + \Delta y_3, z_n + \Delta z_3 \right) \Delta t \tag{9.23}$$

$$\Delta y_4 = v \left( t_n + \Delta t, x_n + \Delta x_3, y_n + \Delta y_3, z_n + \Delta z_3 \right) \Delta t \tag{9.24}$$

$$\Delta z_4 = w \left( t_n + \Delta t, x_n + \Delta x_3, y_n + \Delta y_3, z_n + \Delta z_3 \right) \Delta t \tag{9.25}$$

{245}------------------------------------------------

## <span id="page-245-0"></span>9.2. Oil Spill Model

[EFDC+](#page-11-0) allows for the simulation of oil spills using the same net transport approach used for the drifters. Each oil spill "particle" (referred to here as a "packet") is assigned a mass based on the total mass spilled or discharged and the number of packets defined for that event. Packets can be released all at once or over a specified time interval. The oil packets will be maintained near the water surface (5 mm below) if settling or rising rates are set to zero. Additional processes unique to the oil spill module include direct wind drag (in addition to wind drag induced surface currents), evaporation and biodegradation.

#### <span id="page-245-1"></span>9.2.1 Wind Drag

If the oil spill is located at the surface, wind drag can be added to the advective transport component of the oil spill following [\(Kim et al.,](#page-262-21) [2014\)](#page-262-21).

$$V_{oil} = V_{current} + (CD \times V_{wind}) \tag{9.26}$$

where *Voil* and *Vcurrent* are the velocities of the oil spill and tidal current respectively, *Vwind* is the wind speed at a height of 10 m, and *CD* is the wind drag coefficient . In [EFDC+,](#page-11-0) this basic equation is implemented with two options.

Option 1

$$CD = A \times V_{wind_{mag}} + B \tag{9.27}$$

Option 2

$$CD_X = A \times V_{wind_X} + B \tag{9.28}$$

$$CD_Y = A \times V_{wind_y} + B \tag{9.29}$$

Finally, the actual displacement due to wind drag is calculated using:

$$dx = CD_X \times V_{wind_x} \times \Delta t \tag{9.30}$$

$$dy = CD_Y \times V_{wind_y} \times \Delta t \tag{9.31}$$

Where coefficient *A* has units of s/m, coefficient *B* is dimensionless, *CD* is dimensionless and the velocity terms are all in m/s. If *A* is zero then a constant drag coefficient is used, similar to [Kim et al.](#page-262-21) [\(2014\)](#page-262-21). The range of values for *CD* can vary from 0.0 to 0.1, with a typical value of 0.02 to 0.03.

#### <span id="page-245-2"></span>9.2.2 Loss Terms

The mass of the oil spill can be impacted by a number of processes, two of which are currently in [EFDC+,](#page-11-0) evaporation and biodegradation. If the mass in a packet is less than 1e-9 kg, [EFDC+](#page-11-0) will deactivate that packet for future processing.

For simulation of the oil evaporation process, the theory of surface evaporation presented in the paper by [Stiver and](#page-264-25) [Mackay](#page-264-25) [\(1984\)](#page-264-25) is used. If water temperature is being simulated, then the oil packet temperature is assumed to be the same as the surrounding water. If temperature is not simulated, then the specified temperature is used as a constant value for the evaporation process.

Biodegradation of an oil packet uses a simple first order decay approach based on [Stewart et al.](#page-264-26) [\(1993\)](#page-264-26). As an example, a biodegradation rate of 0.011 *day*−<sup>1</sup> is approximately equal to the half-life of two months. If water temperature is being simulated, then the spill temperature specified by the user is the biodegradation rate reference temperature for the optimal biodegradation. If water temperature is not being simulated, the user input degradation rate is applied as a constant.

To ignore evaporation, set the vapor pressure to zero. To ignore biodegradation, set the degradation rate to zero.

{246}------------------------------------------------

## <span id="page-246-0"></span>Chapter 10

## MARINE HYDROKINETICS

Marine hydrokinetic [\(MHK\)](#page-11-8) devices extract energy from ocean currents and tides, thereby altering water velocities and currents in the project sites. These hydrodynamic changes can potentially affect the ecosystem, both near the [MHK](#page-11-8) installation and in surrounding (i.e., far field) regions. In both marine and freshwater environments, devices will remove energy (momentum) from the system, potentially altering water quality and sediment dynamics. In estuaries, tidal ranges and residence times could change (either increasing or decreasing depending on system flow properties and where the effects are being measured). Effects will be proportional to the number and size of structures installed, with large [MHK](#page-11-8) projects having the greatest potential effects and requiring the most in-depth analyses. The theory and implementation of [MHK](#page-11-8) in SNL-EFDC+ is presented by [James et al.](#page-261-2) [\(2010\)](#page-261-2).

## <span id="page-246-1"></span>10.1. Theory of Marine Hydrokinetics

[MHK](#page-11-8) devices remove momentum from a system, but also alter the turbulent kinetic energy *K*, and turbulent kinetic energy dissipation rate ε. These effects are captured with appropriate sink terms. *S<sup>Q</sup>* (*m* <sup>4</sup>/*s* 2 ) is the volumetric momentum extraction rate by the [MHK](#page-11-8) device due to energy removal, as well as due to form and viscous drag from the [MHK](#page-11-8) structure. *S<sup>K</sup>* (*m* <sup>5</sup>/*s* 3 ) represents the volumetric change in net turbulent kinetic energy in the appropriate model cell due to the [MHK](#page-11-8) device (support), with *S*<sup>ε</sup> (*m* <sup>5</sup>/*s* 3 ) as its analogous term for the volumetric kinetic energy dissipation rate equation [\(Poggi et al.,](#page-263-25) [2004\)](#page-263-25). These quantities are advected and dispersed downstream of the [MHK](#page-11-8) device according to the standard conservation equations used in [EFDC+.](#page-11-0) The standard calculation for *S<sup>Q</sup>* neglects viscous drag relative to energy removal and form drag by the [MHK](#page-11-8) device, thereby resulting in

<span id="page-246-2"></span>
$$S_Q = -\frac{1}{2}C_T A_M U^2 (10.1)$$

where,

*C<sup>T</sup>* is the [MHK](#page-11-8) thrust coefficient (drag coefficient, *CD*, for the support) (dimensionless),

*A<sup>M</sup>* is the [MHK-](#page-11-8)device flow-facing area (support flow-facing area) (m<sup>2</sup> ), and

*U* is the local flow speed in a cell p (*u* <sup>2</sup> +*v* <sup>2</sup>) (m/s).

Here, [MHK-](#page-11-8)device power *P<sup>M</sup>* (*kgm*2/*s* 3 ) is defined as

$$P_M = \frac{1}{2} C_T A_M \rho U^3 \tag{10.2}$$

where, ρ (*kg*/*m* 3 ) is the water density. 

{247}------------------------------------------------

The term  $S_K$  arises because MHK devices break up the mean flow motion and generate wake turbulence ( $\approx \frac{1}{2}C_TA_MU^3$ ). However, such wakes dissipate fairly rapidly, speculatively within about 30 MHK device lengths (turbine diameters). Preliminary MHK Computational Fluid Dynamics (CFD) models showed overly persistent wakes, perhaps in part because this term was not taken into account. The canonical (or physics-based) form for  $S_K$  reflecting the effects of a momentum sink (or partial flow obstruction) is (Sanz, 2003):

$$S_K = \frac{1}{2} C_T A_M \left( \beta_p U^3 - \beta_d U K \right) \tag{10.3}$$

where,

K is the wake-generated turbulent kinetic energy  $(m^2/s^2)$ ,

 $\beta_p$  ( $\approx$  1.0) is the fraction of mean flow kinetic energy converted to K by drag (i.e., a source term in the K budget) (dimensionless), and

 $\beta_d$  ( $\approx 1.0 - 5.0$ ) is the fraction of K dissipated by conversion to kinetic energy (i.e., a sink term in the K budget) (dimensionless).

The most obvious weakness of the  $K - \varepsilon$  approaches is its least understood term  $S_{\varepsilon}$  (Wilson et al., 1998). Over the last decade or so, various models have been proposed for  $S_{\varepsilon}$  (Green, 1992; Katul et al., 2004; Liu et al., 1996), but the simplest is used in this model:

<span id="page-247-1"></span>
$$S_e = C_{e4} \frac{e}{K} S_K \tag{10.4}$$

where  $C_{\varepsilon 4}$  is a closure constant (Katul et al., 2004).

The formulation for equation (10.4) is based on standard dimensional analysis common to all  $K - \varepsilon$  approaches. Upon adding equations (10.1) to (10.4) to the momentum and  $K - \varepsilon$  equations, it is possible to solve for momentum K, and  $\varepsilon$  if appropriate upper and lower boundary conditions are specified. For this implementation,  $C_{\varepsilon 4} = 0.9$ ,  $\beta_p = 1.0$  and  $\beta_d = 5.1$ . In SNL-EFDC+, momentum is defined as the product of flow depth H, and velocity u and v; conservation of kinetic energy is solved in terms of  $\frac{1}{2}HQ^2$ , where q is the turbulent intensity, and conservation of turbulent energy dissipation rate takes the form  $HQ^2l$ , where l is the turbulence length scale.

#### <span id="page-247-0"></span>10.2. Implementation in EFDC+

The simplified kinetic energy equation for an MHK device in a model  $\sigma$  layer is

$$\frac{\partial}{\partial t} \left( m_x m_y \rho H \Delta_k \frac{u^2 + v^2}{2} \right) = -\frac{1}{2} \rho C_T A_M \left( u^2 + v^2 \right)^{\frac{3}{2}} = -P_M$$
 (10.5)

$$A_M = W_M H \Delta_k \tag{10.6}$$

where,

 $m_x$ ,  $m_y$  are the (horizontal) x and y dimensions of a model cell (m),

 $\Delta_k$  is the fraction of total water depth assigned to the  $k^{th}$   $\sigma$  layer,

 $A_M$  is the frontal flow area of the device  $(m^2)$ ,

 $W_M$  is the device or support width (m), and

 $H\Delta_k$  is the layer thickness (m).

{248}------------------------------------------------

The corresponding components of the momentum equations, simplified to exclude advective and diffusive terms are [\(Galperin and Orszag,](#page-260-25) [1993\)](#page-260-25),

$$\frac{\partial}{\partial t} \left( m_x m_y H \Delta_k u \right) = -g m_y H \Delta_k \frac{\partial \zeta}{\partial x} - \frac{1}{2} C_T A_M \left( u^2 + v^2 \right)^{\frac{1}{2}} u \tag{10.7}$$

$$\frac{\partial}{\partial t} \left( m_x m_y H \Delta_k v \right) = -g m_x H \Delta_k \frac{\partial \zeta}{\partial y} - \frac{1}{2} C_T A_M \left( u^2 + v^2 \right)^{\frac{1}{2}} v \tag{10.8}$$

where,

*g* is acceleration due to gravity (*m*/*s* 2 ), and

ζ is the free-surface potential (*m*), or the difference between the hydrostatic water level and the flow depth (this is how water elevation or pressure head drives flow).

Solutions of the *x*- and *y*-momentum equations in [EFDC+](#page-11-0) use the form,

$$\frac{\partial}{\partial t}(Hu) = -g\frac{H}{m_x}\frac{\partial \zeta}{\partial x} - \frac{1}{2m_x m_y \Delta_k} C_T A_M (u^2 + v^2)^{\frac{1}{2}} u$$
(10.9)

$$\frac{\partial}{\partial t}(Hv) = -g\frac{H}{m_y}\frac{\partial \zeta}{\partial y} - \frac{1}{2m_x m_y \Delta_k} C_T A_M (u^2 + v^2)^{\frac{1}{2}}v$$
(10.10)

which can be written in terms of [MHK](#page-11-8) device power (and equivalently for support-structure momentum removal) as

$$\frac{\partial}{\partial t}(Hu) = -g\frac{H}{m_x}\frac{\partial \zeta}{\partial x} - \frac{1}{m_x m_y \Delta_k} \frac{P_M}{\rho (u^2 + v^2)} u \tag{10.11}$$

$$\frac{\partial}{\partial t}(Hv) = -g\frac{H}{m_y}\frac{\partial \zeta}{\partial y} - \frac{1}{m_x m_y \Delta_k} \frac{P_M}{\rho (u^2 + v^2)}v$$
(10.12)

The solution procedure begins by introducing the σ layer notation based on ∆k:

$$\frac{\partial}{\partial t} \left( \Delta_k H u_k \right) = -g \Delta_k \frac{H}{m_x} \frac{\partial \zeta}{\partial x} - \left[ \frac{1}{m_x m_y \Delta_k} \frac{P_M}{\rho \left( u^2 + v^2 \right)} \right]_k \Delta_k u_k \tag{10.13}$$

$$\frac{\partial}{\partial t} \left( \Delta_k H \nu_k \right) = -g \Delta_k \frac{H}{m_y} \frac{\partial \zeta}{\partial y} - \left[ \frac{1}{m_x m_y \Delta_k} \frac{P_M}{\rho \left( u^2 + v^2 \right)} \right]_k \Delta_k \nu_k \tag{10.14}$$

The momentum conservation equations are

$$\frac{\partial}{\partial t} \left( \Delta_k H u_k \right) = -g \Delta_k \frac{H}{m_x} \frac{\partial \zeta}{\partial x} - \Delta_k \left( Q_k - \hat{Q} \right) u_k - \Delta_k \hat{Q} u_k \tag{10.15}$$

$$\frac{\partial}{\partial t} \left( \Delta_k H v_k \right) = -g \Delta_k \frac{H}{m_y} \frac{\partial \zeta}{\partial y} - \Delta_k \left( Q_k - \hat{Q} \right) v_k - \delta_k \hat{Q} v_k \tag{10.16}$$

where volumetric fluxes *Q* are

$$Q_k = \left[ \frac{1}{m_x m_y \Delta_k} \frac{P_M}{\rho \left( u^2 + v^2 \right)} \right]_k \tag{10.17}$$

{249}------------------------------------------------

$$\hat{Q} = \sum_{k=1}^{KC} \Delta_k Q_k \tag{10.18}$$

From this point, the solution procedure is illustrated using only the *u* equation, which is summed over all *KC* layers to give

$$\frac{\partial}{\partial t} (H\hat{u}) = -g \frac{H}{m_x} \frac{\partial \zeta}{\partial x} - \sum_{k=1}^{KC} \Delta_k (Q_k - \hat{Q}) u_k - \hat{Q}\hat{u}$$
(10.19)

$$\hat{u} = \sum_{k=1}^{KC} \Delta_k u_k \tag{10.20}$$

which is the simplified external mode equation. This equation is solved with the continuity equation for the depthaveraged velocity components, ˆ*u* and *v* <sup>−</sup>, and the water surface elevation *H*, using the time-differenced form

$$\left(1 + \frac{\hat{Q}}{H}\Delta t\right) (H\hat{u})^{n+1} + \frac{\Delta t}{2} g \frac{H}{m_x} \frac{\partial \zeta^{n+1}}{\partial x} = (H\hat{u})^n - \frac{\Delta t}{2} g \frac{H}{m_x} \frac{\partial \zeta^n}{\partial x} - \Delta t \sum_{k=1}^{KC} \left[\Delta_k \left(Q_k - \hat{Q}\right) u_k\right]^n \quad (10.21)$$

where ∆*t* is the time step.

The internal-mode equation solution is based on considering the difference between equations for two adjacent layers

$$\frac{\partial}{\partial t} \left( H u_{k+1} \right) = -g \frac{H}{m_x} \frac{\partial \zeta}{\partial x} - \left( Q_{k+1} - \hat{Q} \right) u_{k+1} - \hat{Q} u_{k+1} \tag{10.22}$$

$$\frac{\partial}{\partial t} (H u_k) = -g \frac{H}{m_x} \frac{\partial \zeta}{\partial x} - (Q_k - \hat{Q}) u_k - \hat{Q} u_k$$
(10.23)

which has the remainder as

$$\frac{\partial}{\partial t} (H u_{k+1} - H u_k) + \frac{\hat{Q}}{H} (H u_{k+1} - H u_k) = -(Q_{k+1} - \hat{Q}) u_{k+1} + (Q_k - \hat{Q}) u_k$$
 (10.24)

Time differencing yields

$$\left(1 + \Delta t \frac{\hat{Q}}{H}\right) (Hu_{k+1} - Hu_k)^{n+1} =$$

$$(Hu_{k+1} - Hu_k)^n - \Delta t \left[ (Q_{k+1} - \hat{Q}) u_{k+1} - (Q_k - \hat{Q}) u_k \right]^n \quad (10.25)$$

The system of *KC* − 1 layer-interface equations can be solved for the velocity differences across the layer and used with the definition of the depth-averaged velocity to determine the actual layer velocities.

The [MHK](#page-11-8) device effect in the turbulent kinetic energy (turbulent intensity) equation is given by

$$\frac{\partial}{\partial t} \left( H \frac{q^2}{2} \right) = \beta_p \left( \frac{1}{2} \frac{1}{m_x m_y \Delta_k} C_T A_M \right) \left( u^2 + v^2 \right)^{\frac{1}{2}} \left( u^2 + v^2 \right) - \beta_d \left( \frac{1}{2} \frac{1}{m_x m_y \Delta_k} C_T A_M \right) \left( u^2 + v^2 \right)^{\frac{1}{2}} \frac{q^2}{2} - \frac{H}{B_1 l} q^3 \quad (10.26)$$

{250}------------------------------------------------

where, *B*<sup>1</sup> = 16.6 (dimensionless) is a turbulence closure coefficient from [Mellor and Yamada](#page-263-4) [\(1982\)](#page-263-4).

The dissipation effect of the device is combined with the standard flow dissipation term to give

$$\frac{\partial}{\partial t} \left( H \frac{q^2}{2} \right) + \left[ \beta_d \left( \frac{1}{2} \frac{C_T A_M}{m_x m_y \Delta_k} \right) \frac{\left( u^2 + v^2 \right)^{\frac{1}{2}}}{H} + \frac{q}{B_1 l} \right] H q^2 =$$

$$\beta_p \left( \frac{1}{2} \frac{C_T A_M}{m_x m_y \Delta_k} \right) \left( u^2 + v^2 \right)^{\frac{1}{2}} \left( u^2 + v^2 \right) \quad (10.27)$$

where the total dissipation has been moved to the left side of the equation to emphasize that it must be treated implicitly in the numerical solution procedure given by

$$\left\{1 + \Delta t \left[\beta_d \left(\frac{C_T A_M}{m_x m_y \Delta_k}\right) \frac{\left(u^2 + v^2\right)^{\frac{1}{2}}}{H} + \frac{2q}{B_1 l}\right]\right\} (Hq^2)^{n+1} = (Hq^2)^n + \Delta t \beta_p \left(\frac{C_T A_M}{m_x m_y \Delta_k}\right) (u^2 + v^2)^{\frac{1}{2}} (u^2 + v^2) \quad (10.28)$$

The turbulent length scale equation (turbulent kinetic energy dissipation rate) is

$$\frac{\partial}{\partial t} (Hq^{2}l) + \left[ C_{e4} \beta_{d} \left( \frac{1}{2} \frac{C_{T} A_{M}}{m_{x} m_{y} \Delta_{k}} \right) \frac{\left(u^{2} + v^{2}\right)^{\frac{1}{2}}}{H} + \frac{q}{B_{1}l} \right] Hq^{2}l = C_{e4} \beta_{p} \left( \frac{1}{2} \frac{C_{T} A_{M}}{m_{x} m_{y} \Delta_{k}} \right) \left(u^{2} + v^{2}\right)^{\frac{1}{2}} \left(u^{2} + v^{2}\right) l \quad (10.29)$$

which is solved similar to the turbulent kinetic energy equation using

$$\left\{1 + \Delta t \left[C_{e4}\beta_d \left(\frac{1}{2} \frac{C_T A_M}{m_x m_y \Delta_k}\right) \frac{\left(u^2 + v^2\right)^{\frac{1}{2}}}{H} + \frac{q}{B_1 l}\right]\right\} \left(Hq^2 l\right)^{n+1} = 
\left(Hq^2 l\right)^n + \Delta t C_{e4}\beta_p \left(\frac{1}{2} \frac{C_T A_M}{m_x m_y \Delta_k}\right) \left(u^2 + v^2\right)^{\frac{1}{2}} \left(u^2 + v^2\right) l \quad (10.30)$$

For completeness, vegetative resistance effects on *K* −ε were also included in the SNL[-EFDC+](#page-11-0) coding.

{251}------------------------------------------------

## <span id="page-251-0"></span>Chapter 11

## SHELLFISH FARMING

This section summarizes the basic theory of the shellfish module implemented in the [EFDC+](#page-11-0) code. [DSI](#page-11-4) appreciates ongoing collaboration with the Marine Environment Research Division of Korea's National Institute of Fisheries Science for developing this module. Shellfish filter feeders interact with multiple components of the eutrophication model. These organisms remove [POM](#page-12-16) from the water column for ingestion and assimilation and deposit a portion of it in the bottom sediments as feces. [\(Cerco and Noel,](#page-259-21) [2005\)](#page-259-21). In [EFDC+,](#page-11-0) the kinetic processes of the shellfish include filtering, ingestion, assimilation, respiration, mortality, and spawning. A shellfish individual is quantified as the [OC](#page-11-15) incorporated in soft tissue which is computed as a function of food availability, respiration, and mortality. The environmental effects on shellfish life processes are considered by its interactions with the water quality model.

## <span id="page-251-1"></span>11.1. Governing Equation

For each shellfish individual, the change of its weight with time is the result of changes in net production. Therefore, a fundamental growth equation for filter feeder biomass can be written as:

$$\frac{dW_d}{dt} = NP \tag{11.1}$$

where,

*t* is the time (s),

*W<sup>d</sup>* is the dry meat weight (g C), and

*NP* is the net production (g C).

According to [White et al.](#page-265-24) [\(1988\)](#page-265-24) and [Kobayashi et al.](#page-262-23) [\(1997\)](#page-262-23), the net production is the sum of somatic and reproductive tissue production, which is assumed to be the difference between assimilation and respiration:

$$NP = P_g + P_r = A - R \tag{11.2}$$

where,

*P<sup>g</sup>* is the somatic production (g C),

*Pr* is the reproductive tissue production (g C), and

*A* is the assimilation (g C) and *R* is the respiration (g C).

{252}------------------------------------------------

#### <span id="page-252-0"></span>11.2. Length - Weight Relation

The relationship between shell length and live weight is routinely used as an index of oyster growth. It is well known with an equation of the form:

$$L = A \cdot W_d^{\ B} \tag{11.3}$$

where,

*L* is the shell length (cm), and

*A*,*B* are constants parameters.

By fitting this equation to the experimental measurements, [Kobayashi et al.](#page-262-23) [\(1997\)](#page-262-23) gave *A* = 77.9 and *B* = 0.291 for the Japanese oyster, *Crassostrea gigas*.

## <span id="page-252-1"></span>11.3. Filtration Rate

Shellfish filtration rate is quantified as water volume cleared of particles per individual per unit time. It is the major determinant of growth that in turn affects changes in shellfish biomass. In [EFDC+,](#page-11-0) filtration rate is represented as a maximum or optimal rate that is modified by ambient temperature, suspended solids, salinity, and dissolved oxygen:

$$FR = FR_W \cdot f_1(T) \cdot f_2(S) \cdot f_3(TSS) \cdot f_4(DO)$$
(11.4)

where,

*FR* is the filtration rate (l filtered per individual h−<sup>1</sup> ),

*FR<sup>W</sup>* is the maximum filtration rate (l filtered per individual h−<sup>1</sup> ),

*f*1(*T*) is the effect of temperature on filtration rate (0 < *f*1(*T*) ≤ 1),

*f*2(*S*) is the effect of salinity on filtration rate (0 < *f*2(*S*) ≤ 1),

*f*3(*T SS*) is the effect of suspended solids on filtration rate (0 < *f*3(*T SS*) ≤ 1), and

*f*4(*DO*) is the effect of dissolved oxygen on filtration rate (0 < *f*4(*DO*) ≤ 1).

#### <span id="page-252-2"></span>11.3.1 Maximum Filtration Rate

The maximum filtration rate is commonly estimated from the dry meat weight *Wd*. [Coughlan and Ansell](#page-259-22) [\(1964\)](#page-259-22) provides the following relationship for siphonate bivalves:

$$FR_W = 2.59 \cdot W_d^{0.73} \tag{11.5}$$

Another formulation was used by [Cloern](#page-259-23) [\(1982\)](#page-259-23) for studying of bivalves in South San Francisco Bay:

$$FR_W = 7.0 \cdot W_d^{0.67} \tag{11.6}$$

For the Japanese oyster, *Crassostrea gigas*, [Kobayashi et al.](#page-262-23) [\(1997\)](#page-262-23) proposed the following formula for the maximum filtration rate:

$$FR_W = \begin{cases} 2.51 \cdot W_d^{0.279}, & W_d \ge 2g\\ 0.117 \cdot W_d^3 - 1.05 \cdot W_d^2 + 3.09 \cdot W_d + 0.133, & W_d < 2g \end{cases}$$
(11.7)

{253}------------------------------------------------

Cerco and Noel (2007) used a constant factor for the maximum filtration rate while studying the native oysters, *Crassostrea virginica* in Chesapeake Bay:

$$FR_W = 0.55 \cdot \frac{1000}{24} \cdot W_d = 22.917 \cdot W_d \tag{11.8}$$

On the other hand, Officer et al. (1982) determined the maximum filtration rate from the total weight W:

$$FR_W = 0.76 \cdot W^{0.60} \tag{11.9}$$

The temperature effect on the maximum filtration rate can be also included as (Doering and Oviatt, 1986):

$$FR_W = \frac{60}{1000} \frac{L^{0.96} T^{0.95}}{2.95} \tag{11.10}$$

#### <span id="page-253-0"></span>11.3.2 Temperature Effect

From Kobayashi et al. (1997), the effect of temperature on filtration rate is modeled as:

$$f_1(T) = \begin{cases} \frac{T^{0.5}}{4.47}, & T \ge 7 \,^{\circ} \text{C} \\ 0.59, & T < 7 \,^{\circ} \text{C} \end{cases}$$
 (11.11)

Cerco and Noel (2007) considered the temperature effect as an exponentially increasing function of temperature :

$$f_1(T) = \exp(-K_{tg} \cdot (T - T_{opt})^2)$$
(11.12)

where,

T is the temperature ( $^{\circ}$ C),

 $T_{opt}$  is the temperature for optimal filtration ( ${}^{\circ}$ C), and

 $K_{tg}$  is the coefficient for the effect of temperature on filtration.

#### <span id="page-253-1"></span>11.3.3 Salinity Effect

According to Loosanoff (1958), the filtration rate decreases below 7.5 ppt and ceases at 3.5 ppt. A linear relationship was also introduced for the salinity effect between these threshold values:

$$f_2(S) = \begin{cases} 1, & S \ge 7.5 \text{ ppt} \\ \frac{S-3.5}{7.5-3.5}, & 3.5 < S < 7.5 \text{ ppt} \\ 0, & S \le 3.5 \text{ ppt} \end{cases}$$
(11.13)

where *S* is the ambient salinity (ppt).

A similar mathematical formulation for the salinity effect was reported by Quayle (1988) and Mann et al. (1991) but different threshold salinity values:

$$f_2(S) = \begin{cases} 1, & S \ge 20 \text{ ppt} \\ \frac{S-10}{20-10}, & 10 < S < 20 \text{ ppt} \\ 0, & S \le 10 \text{ ppt} \end{cases}$$
 (11.14)

{254}------------------------------------------------

In [Cerco and Noel](#page-259-21) [\(2005\)](#page-259-21), the authors proposed a tanh functional from for the effect of salinity on filtration rate:

$$f_2(T) = 0.5 \cdot (1 + \tanh(S - S_{KH})) \tag{11.15}$$

with *SKH* is the the salinity at which the filtration rate is halved (ppt).

[Fulford et al.](#page-260-27) [\(2007\)](#page-260-27) adjusted the salinity effect as a linear function salinity based on data measurement for oyster *Crassostrea virginica* in Chesapeake Bay, USA:

$$f_2(T) = 0.0926 \cdot S - 0.139 \tag{11.16}$$

[Buzzelli et al.](#page-258-20) [\(2015\)](#page-258-20) included the effect of salinity on filtration rate simulation of oyster in south Florida estuaries as:

$$f_2(T) = -0.0017 \cdot S^2 + 0.0084 \cdot S - 0.1002$$
(11.17)

#### <span id="page-254-0"></span>11.3.4 Suspended Solids Effect

The effect of high suspended solids concentrations on oyster filtration rate has been long recognized through experiments by [Loosanoff and Tommers](#page-262-26) [\(1948\)](#page-262-26). From the given data, [Hofmann et al.](#page-261-28) [\(1992\)](#page-261-28) deduced a formulation as follows:

$$f_3(TSS) = 1 - 0.001 \cdot \frac{\log_{10}(TSS) + 3.38}{0.418}$$
(11.18)

[Cerco and Noel](#page-259-21) [\(2005\)](#page-259-21) applied a piecewise function, obtained though visual fit to the data from [Jordan](#page-261-29) [\(1987\)](#page-261-29) and supplement with the results from [Loosanoff and Tommers](#page-262-26) [\(1948\)](#page-262-26):

$$f_3(TSS) = \begin{cases} 0.1, & TSS < 5 \,\text{mg/l} \\ 1.0, & 5 < TSS < 25 \,\text{mg/l} \\ 0.2, & 25 < TSS < 100 \,\text{mg/l} \\ 0.0, & TSS \ge 100 \,\text{mg/l} \end{cases}$$
(11.19)

[Fulford et al.](#page-260-27) [\(2007\)](#page-260-27) modeled the effect of suspended solid as a power function derived from the data measured by the EPA Chesapeake Bay Monitoring Program:

$$f_3(TSS) = 10.364 \cdot \ln(TSS)^{-2.0477}, \quad TSS > 25 \,\text{mg/l}$$
 (11.20)

#### <span id="page-254-1"></span>11.3.5 Dissolved Oxygen (DO) Effect

The model formulation incorporates [DO](#page-11-3) effects on filtration rate which are expressed as proposed in [Cerco and Noel](#page-259-21) [\(2005\)](#page-259-21):

$$f_4(DO) = \frac{1}{1 + \exp(1.1 \times \frac{DO_{hx} - DO}{DO_{hx} - DO_{qx}})}$$
(11.21)

where [DO](#page-11-3) is the dissolved oxygen concentration (mg/l); *DOhx* and *DOqx* are the [DO](#page-11-3) concentrations (mg/l) at which the filtration rates are 50% and 25% of maximum, respectively.

#### <span id="page-254-2"></span>11.4. Ingestion and Assimilation

Shellfish ingestion capacity is given by multiplying the filtration rate by the food concentration:

$$I = \frac{24}{1000} \times f \times FR \tag{11.22}$$

{255}------------------------------------------------

where, *I* is the ingestion (g dry weight per individual day−<sup>1</sup> ) and *f* is the food concentration (measured food value) (mg dry weight l−<sup>1</sup> ).

Shellfish assimilation is obtained from ingestion using an assimilation efficiency. It is noted that the fraction of ingested carbon assimilated by shellfish depends on the carbon source.

$$A = \alpha \times I \tag{11.23}$$

in which *A* is the assimilation rate (g dry weight per individual day−<sup>1</sup> ) and α is the assimilation efficiency.

Shellfish assimilation can be converted into energy via:

$$E_A = C_E \times A \tag{11.24}$$

where *E<sup>A</sup>* is the assimilation energy (calories per individual day−<sup>1</sup> ) and *C<sup>E</sup>* is the caloric conversion factor (5210 calories per g dry weight).

### <span id="page-255-0"></span>11.5. Respiration

Shellfish respiration is commonly represented as a function of temperature and the dry meat weight:

$$R = B_M \cdot W_d \tag{11.25}$$

where *B<sup>M</sup>* is the dependency of respiration on temperature.

Several mathematical formulations of *B<sup>M</sup>* have been proposed in literature and implemented in the [EFDC+](#page-11-0) code. According to the Korean National Institute of Fisheries Science [\(Kim,](#page-262-27) [2019\)](#page-262-27):

$$B_M = \begin{cases} \alpha_R \cdot \theta^{T - T_B}, & T > T_B \\ 0, & T \le T_B \end{cases}$$
 (11.26)

where,

*T<sup>B</sup>* is the base temperature for respiration (◦C),

α*<sup>R</sup>* metabolism rate at reference temperature (day−<sup>1</sup> ), and

θ is a temperature coefficient for respiration.

[Cerco and Noel](#page-259-24) [\(2007\)](#page-259-24) considered basal metabolism to be an exponentially increasing function of temperature

$$B_M = \alpha_R \cdot \exp(K_{Tb} \cdot (T - T_r)) \tag{11.27}$$

where,

*Tr* is the reference temperature for specification of metabolism (◦C),

α*<sup>R</sup>* metabolism rate at reference temperature (day−<sup>1</sup> ),

*KT b* is a constant that relates metabolism to temperature (◦C −1 ).

For *C. virginica* oyster, respiration rate as a function of temperature and shellfish dry meat weight can be also obtained from [Dame](#page-259-25) [\(1972\)](#page-259-25):

<span id="page-255-1"></span>
$$R = (12.6 \cdot T + 69.7) \cdot W_d^{-0.25} \tag{11.28}$$

According to [Hofmann et al.](#page-261-28) [\(1992\)](#page-261-28), salinity effects on oyster respiration over a range of temperature, were parameterized using data given in [\(Shumway and Koehn,](#page-264-28) [1982\)](#page-264-28):

{256}------------------------------------------------

<span id="page-256-2"></span>
$$R_R = \begin{cases} 0.007 \cdot T + 2.099, & T < 20^{\circ} \text{C} \\ 0.0915 \cdot T + 1.324, & T \ge 20^{\circ} \text{C} \end{cases}$$
 (11.29)

Where, *R<sup>R</sup>* is the ratio of respiration at 10 ppt to respiration at 20 ppt: *R<sup>R</sup>* = *R*10ppt/*R*20ppt. Equations [\(11.28\)](#page-255-1) and [\(11.29\)](#page-256-2) were combined to obtain respiration over a range of salinity as follows:

$$R = \begin{cases} R, & S \ge 15 \text{ ppt} \\ R(1 + (R_R - 1)\frac{15 - S}{5}), & 10 < S < 15 \text{ ppt} \\ RR_R, & S \le 10 \text{ ppt} \end{cases}$$
(11.30)

[Shumway and Koehn](#page-264-28) [\(1982\)](#page-264-28) identified effects of salinity on respiration at 20 ppt.

Finally, the energy consumed by respiration is given by:

$$E_R = \frac{24}{1000} \times C_R \times R \times W_d \tag{11.31}$$

where,

*E<sup>R</sup>* is the respiration energy (calories per individual day−<sup>1</sup> ),

*C<sup>R</sup>* is the caloric conversion factor (calories per ml oxygen), and

*R* is the respiration rate (µl oxygen per g dry weight h−).

## <span id="page-256-0"></span>11.6. Reproduction

For adult shellfish greater or equal to a certain size, net production was apportioned into growth and reproduction by using a temperature-dependent reproduction efficiency of the form:

$$P_r = R_{eff} \cdot NP \tag{11.32}$$

where *Re f f* is the temperature-dependent reproduction efficiency.

A formulation of *Re f f* , derived empirically from observations, was reported in [Kobayashi et al.](#page-262-23) [\(1997\)](#page-262-23):

$$R_{eff} = \begin{cases} 0.8, & T \ge 27^{\circ} \text{C} \\ 0.2 \cdot T - 4.6, & 23 < T < 27^{\circ} \text{C} \\ 0, & T \le 23^{\circ} \text{C} \end{cases}$$
(11.33)

In cases where *NP* < 0, a preferential resorption of gonadal tissue is assumed to cover the deficit.

#### <span id="page-256-1"></span>11.7. Spawning

Spawning occurs when the environmental conditions (temperature and salinity) are in the suitable ranges and the cumulative production biomass exceeds a certain fraction of shellfish total biomass. Once spawning occurs, the total reproductive biomass is apportioned into male and female biomass. The ratio of females to males is calculated as e.g., [\(Powell et al.,](#page-263-28) [1994\)](#page-263-28):

$$f_{ratio} = 0.021 \cdot L_b - 0.62 \tag{11.34}$$

{257}------------------------------------------------

where *fratio* is the ratio of females to males and *L<sup>b</sup>* is the shell length in mm. Then, the female portion of reproductive biomass can be calculated and converted into eggs spawned as follows:

$$n_{eggs} = R_f \cdot \frac{1}{E_{egg}} \cdot \frac{1}{W_{egg}} \tag{11.35}$$

where,

*neggs* is the number of eggs spawned,

*Rf* is the female portion of reproductive biomass,

*Weggs* is the egg weight, and

*Eeggs* is the egg's caloric content (cal. g dry weight−<sup>1</sup> ).

For oysters, the egg weight can be estimated from egg volume as:

$$W_{eggs} = 2.14 \times 10^{-14} \cdot V_{egg} \tag{11.36}$$

where *Vegg* is the oyster egg volume (µm<sup>3</sup> ).

{258}------------------------------------------------

## <span id="page-258-0"></span>Chapter 12

## References

- <span id="page-258-11"></span>Abramowitz, M. (1964). Handbook of mathematical functions, national bureau of standards. *Applied Mathematics Series* (55).
- <span id="page-258-8"></span>Ackers, P. and W. R. White (1973). Sediment transport: new approach and analysis. *Journal of the Hydraulics Division 99*(11), 2041–2060.
- <span id="page-258-6"></span>Anderson, E. et al. (1954). Water loss investigations: Lake hefner studies. *US Department of the Interior, Geol*.
- <span id="page-258-4"></span><span id="page-258-3"></span>Anderson, R. (1993). A study of wind stress and heat flux over the open ocean by the inertial-dissipation.
- Arakawa, A. and V. R. Lamb (1977). Computational design of the basic dynamical processes of the ucla general circulation model. *General circulation models of the atmosphere 17*(Supplement C), 173–265.
- <span id="page-258-7"></span>Bagnold, R. A. (1956). The flow of cohesionless grains in fluids. *Philosophical Transactions of the Royal Society of London. Series A, Mathematical and Physical Sciences 249*(964), 235–297.
- <span id="page-258-17"></span>Banks, R. B. and F. F. Herrera (1977). Effect of wind and rain on surface reaeration. *Journal of the Environmental Engineering Division 103*(3), 489–504.
- <span id="page-258-18"></span>Barrow, N. (1983). A mechanistic model for describing the sorption and desorption of phosphate by soil. *Journal of soil science 34*(4), 733–750.
- <span id="page-258-12"></span>Belov, A. P. and J. D. Giles (1997, Aug). Dynamical model of buoyant cyanobacteria. *Hydrobiologia 349*(1), 87–97.
- <span id="page-258-1"></span>Blumberg, A. F. and G. L. Mellor (1987). A description of a three-dimensional coastal ocean circulation model. *Three-dimensional coastal ocean models 4*, 1–16.
- <span id="page-258-15"></span>Boni, L., E. Carpene, D. Wynne, and M. Reti (1989). Alkaline phosphatase activity in protogonyaulax tamarensis. *Journal of plankton research 11*(5), 879–885.
- <span id="page-258-19"></span>Boudreau, B. P. (1991). Modelling the sulfide-oxygen reaction and associated ph gradients in porewaters. *Geochimica et Cosmochimica Acta 55*(1), 145–159.
- <span id="page-258-16"></span>Bowie, G. L., W. B. Mills, D. B. Porcella, C. L. Campbell, J. R. Pagenkopf, G. L. Rupp, K. M. Johnson, P. Chan, S. A. Gherini, C. E. Chamberlin, et al. (1985). Rates, constants, and kinetics formulations in surface water quality modeling. *EPA 600*, 3–85.
- <span id="page-258-5"></span>Brady, D. K., W. L. Graves, Jr, and J. C. Geyer (1969, 11). Surface heat exchange at power plant cooling lakes. report no. 5. eei publication no. 69-901. Technical report.
- <span id="page-258-13"></span>Bunch, B. W., C. F. Cerco, M. S. Dortch, B. H. Johnson, and K. W. Kim (2000). Hydrodynamic and water quality model study of san juan bay estuary. Technical report, Army Engineer Waterways Experiment Station Vicksburg Ms Engineer Research.
- <span id="page-258-9"></span>Burban, P.-Y., W. Lick, and J. Lick (1989). The flocculation of fine-grained sediments in estuarine waters. *Journal of Geophysical Research: Oceans 94*(C6), 8323–8330.
- <span id="page-258-10"></span>Burban, P.-Y., Y.-J. Xu, J. McNeil, and W. Lick (1990). Settling speeds of floes in fresh water and seawater. *Journal of Geophysical Research: Oceans 95*(C10), 18213–18220.
- <span id="page-258-20"></span>Buzzelli, C., P. Gorman, P. Doering, Z. Chen, and Y. Wan (2015). The application of oyster and seagrass models to evaluate alternative inflow scenarios related to everglades restoration. *Ecological Modelling 297*, 154–170.
- <span id="page-258-2"></span>Canuto, V. M. and Y. Cheng (1997). Determination of the smagorinsky–lilly constant CS. *9*(5), 1368–1378.
- <span id="page-258-14"></span>Carritt, D. E. and S. Goodgal (1954). Sorption reactions and some ecological implications. *Deep Sea Research (1953) 1*(4), 224–243.

{259}------------------------------------------------

<span id="page-259-12"></span>Caupp, C. L., J. T. Brock, and H. M. Runke (1991). *Application of the dynamic stream simulation and assessment model (DSSAM III) to the Truckee River below Reno, Nevada: Model formulation and program description*. Rapid Creek Water Works.

- <span id="page-259-0"></span>Cerco, C. and T. Cole (1994). Three-dimensional model of cheasapeake bay. *Vicksburg: US Army Corps of Engineers Technical Report EL-94-4*.
- <span id="page-259-21"></span>Cerco, C. and M. Noel (2005, 07). Assessing a ten-fold increase in the chesapeake bay native oyster population - a report to the epa chesapeake bay program. Technical report, US Army Engineer Research and Development Center, Vicksburg MS.
- <span id="page-259-24"></span>Cerco, C. and M. Noel (2007). Can oyster restoration reverse cultural eutrophication in chesapeake bay? *Estuaries and Coasts 30*(2), 43–61.
- <span id="page-259-11"></span>Cerco, C. F., B. W. Bunch, A. M. Teeter, and M. S. Dortch (2000). Water quality model of florida bay. Technical report, Engineer Research and Development Center Vicksburg MS Environmental Lab.
- <span id="page-259-15"></span>Cerco, C. F. and T. Cole (1993). Three-dimensional eutrophication model of chesapeake bay. *Journal of Environmental Engineering 119*(6), 1006–1025.
- <span id="page-259-8"></span>Cerco, C. F. and T. Cole (1995). User's guide to the ce-qualicm three-dimensional eutrophication model. *US Army Corps of Engineers, Waterways Experiment Station, Technical report EL-95-15, Vicksburg, Mississippi*.
- <span id="page-259-13"></span>Cerco, C. F., L. Linker, J. Sweeney, G. Shenk, and A. J. Butt (2002). Nutrient and solids controls in virginia's chesapeake bay tributaries. *Journal of Water Resources Planning and Management 128*(3), 179–189.
- <span id="page-259-10"></span>Cerco, C. F., M. R. Noel, et al. (2004). *The 2002 Chesapeake Bay Eutrophication Model*. Citeseer.
- <span id="page-259-9"></span>Cerco, C. F., M. R. Noel, and S.-C. Kim (2004). Three-dimensional eutrophication model of lake washington, washington state. Technical report, Engineer Research And Development Center Vicksburg Ms Environmental Lab.
- <span id="page-259-17"></span>Chapra, S. (1997). *Surface Water-quality Modeling*. McGraw-Hill series in water resources and environmental engineering. McGraw-Hill.
- <span id="page-259-18"></span>Chapra, S. C., L. A. Camacho, and G. B. McBride (2021). Impact of global warming on dissolved oxygen and bod assimilative capacity of the world's rivers: modeling analysis. *Water 13*(17), 2408.
- <span id="page-259-6"></span>Chapra, S. C., R. P. Canale, and G. L. Amy (1997). Empirical models for disinfection by-products in lakes and reservoirs. *Journal of Environmental Engineering 123*(7), 714–715.
- <span id="page-259-5"></span>Cheng, N.-S. (1997). Simplified settling velocity formula for sediment particle. *Journal of hydraulic engineering 123*(2), 149–152.
- <span id="page-259-16"></span>Chrost, R. J. and J. Overbeck (1987). Kinetics of alkaline phosphatase activity and phosphorus availability for phyto- ´ plankton and bacterioplankton in lake plusee (north german eutrophic lake). *Microbial ecology 13*(3), 229–248.
- <span id="page-259-3"></span>Clark, T. L. (1977). A small-scale dynamic model using a terrain-following coordinate transformation. *Journal of Computational Physics 24*(2), 186–215.
- <span id="page-259-2"></span>Clark, T. L. and W. D. Hall (1991). Multi-domain simulations of the time dependent navier-stokes equations: Benchmark error analysis of some nesting procedures. *Journal of Computational Physics 92*(2), 456–481.
- <span id="page-259-19"></span>Cline, J. D. and F. A. Richards (1969). Oxygenation of hydrogen sulfide in seawater at constant salinity, temperature and ph. *Environmental Science & Technology 3*(9), 838–843.
- <span id="page-259-23"></span>Cloern, J. (1982). Does the benthos control phytoplankton biomass in south san francisco bay? *Marine Ecology - Progress Series 9*, 191–202.
- <span id="page-259-22"></span>Coughlan, J. and A. D. Ansell (1964). A direct method for determining the pumping rate of siphonate bivalves. *ICES Journal of Marine Science 29*(2), 205–213.
- <span id="page-259-7"></span>Covar, A. P. (1976). Selecting the proper reaeration coefficient for use in water quality models. In *Proceedings of the Conference on Environmental Modeling and Simulation. Cincinnati, OH, EPA-600/9-76-016, Environmental Protection Agency, Washington, DC*, pp. 340–3.
- <span id="page-259-1"></span>Craig, P., D. Chung, N. Lam, P. Son, and N. Tinh (2014). Sigma-zed: A computationally efficient approach to reduce the horizontal gradient error in the efdc's vertical sigma grid. In *Proceedings of the 11th International Conference on Hydrodynamics, Singapore*.
- <span id="page-259-25"></span>Dame, R. F. (1972). The ecological energies of growth, respiration, and assimilation in the intertidal american oyster crassostrea virginica. *Marine Biology 17*, 243–250.
- <span id="page-259-20"></span><span id="page-259-4"></span>Deacon, E. and E. Webb (1962). Physical oceanography: Ii. interchange of properties between sea and air.
- Di Toro, D. and J. Fitzpatrick (1993). Chesapeake bay sediment flux model. final report. Technical report, Hydroqual, Inc., Mahwah, NJ (United States).
- <span id="page-259-14"></span>Di Toro, D. M. (1980). Applicability of cellular equilibrium and monod theory to phytoplankton growth kinetics. *Ecological Modelling 8*, 201–218.

{260}------------------------------------------------

- <span id="page-260-21"></span><span id="page-260-20"></span>Di Toro, D. M. et al. (2001). *Sediment flux modeling*, Volume 116. Wiley-Interscience New York.
- Di Toro, D. M., P. R. Paquin, K. Subburamu, and D. A. Gruber (1990). Sediment oxygen demand model: methane and ammonia oxidation. *Journal of Environmental Engineering 116*(5), 945–986.
- <span id="page-260-22"></span>Diaz, R. J., R. Rosenberg, et al. (1995). Marine benthic hypoxia: a review of its ecological effects and the behavioural responses of benthic macrofauna. *Oceanography and marine biology. An annual review 33*, 245–03.
- <span id="page-260-7"></span>Dill, N. (Ed.) (2011, 11). *Modeling Hydraulic Control Structures in Estuarine Environments with EFDC*. International Conference on Estuarine and Coastal Modeling: The name of the publisher.
- <span id="page-260-16"></span>DiToro, D. and J. Fitzpatrick (1993). Chesapeake bay sediment flux model. prepared for the us army corps of engineer waterways experiment station. vicksburg, ms. Technical report.
- <span id="page-260-26"></span>Doering, P. and C. Oviatt (1986). Application of filtration rate models to field populations of bivalves: an assessment using experimental mesocosms. *Marine Ecology - Progress Series 31*, 265–275.
- <span id="page-260-23"></span><span id="page-260-8"></span>DSI (2009, June). Implementation of a Lagrangian Particle Tracking Sub-Model for the EFDC Code (Draft).
- DSI (2021). EFDC+ propeller wash module white paper.
- <span id="page-260-24"></span>Dunsbergen, D. W. and G. Stelling (1993). A 3d particle model for transport problems in transformed coordinates. *Communications on hydraulic and geotechnical engineering, No. 1993-07*.
- <span id="page-260-15"></span>Dwight, H. B. (1947). Tables of integrals and other mathematical data. *New York: The MacMillan Company,— c1947, Revised Edition*.
- <span id="page-260-10"></span>Edinger, J., D. Brady, and J. Geyer (1974). Heat exchange and transport in the environment. report no. 14. Technical report, Johns Hopkins Univ., Baltimore, MD (USA). Dept. of Geography and.
- <span id="page-260-4"></span>Edson, J. B., V. Jampana, R. A. Weller, S. P. Bigorre, A. J. Plueddemann, C. W. Fairall, S. D. Miller, L. Mahrt, D. Vickers, and H. Hersbach (2013). On the exchange of momentum over the open ocean. *Journal of Physical Oceanography 43*(8), 1589–1610.
- <span id="page-260-12"></span>Engelund, F. and E. Hansen (1967). A Monograph on Sediment Transport in Alluvial Streams. Technical report, Technical University of Denmark.
- <span id="page-260-0"></span>Fainchtein, R. (2014). *Intermediate MPI:Domain Decomposition*. MIT Press.
- <span id="page-260-2"></span>Fairall, C., E. Bradley, D. Rogers, J. Edson, and G. Young (1996). The toga coare bulk flux algorithm. *J. Geophys. Res 101*, 3747–3764.
- <span id="page-260-3"></span>Fairall, C. W., E. F. Bradley, J. Hare, A. A. Grachev, and J. B. Edson (2003). Bulk parameterization of air–sea fluxes: Updates and verification for the coare algorithm. *Journal of climate 16*(4), 571–591.
- <span id="page-260-9"></span>Fletcher, C. (1988). *AJ. Computational Techniques for Fluid Dynamics. Fundamental and general techniques*. Berlin, Germany: Springer-Verlag, Berlin.
- <span id="page-260-5"></span>Francis, J. (1951). The aerodynamic drag of a free water surface.
- <span id="page-260-17"></span>Froelich, P. N. (1988). Kinetic control of dissolved phosphate in natural rivers and estuaries: a primer on the phosphate buffer mechanism 1. *Limnology and oceanography 33*(4part2), 649–668.
- <span id="page-260-11"></span>Fulford, J. M. and T. W. Sturm (1984). Evaporation from flowing channels. *Journal of Energy Engineering 110*(1), 1–9.
- <span id="page-260-27"></span>Fulford, R., D. Breitburg, R. E. Newell, W. M. Kemp, and M. Luckenbach (2007). Effects of oyster population restoration strategies on phytoplankton biomass in chesapeake bay: a flexible modeling approach. *Marine Ecology Progress Series 336*, 43–61.
- <span id="page-260-1"></span>Galperin, B., L. Kantha, S. Hassid, and A. Rosati (1988). A quasi-equilibrium turbulent energy model for geophysical flows. *Journal of the Atmospheric Sciences 45*(1), 55–62.
- <span id="page-260-25"></span>Galperin, B. and S. A. Orszag (1993). *Large eddy simulation of complex engineering and geophysical flows*. Cambridge University Press.
- <span id="page-260-19"></span>Garcia, H. E. and L. I. Gordon (1992). Oxygen solubility in seawater: Better fitting equations. *Limnology and Oceanography 37*(6), 1307–1312.
- <span id="page-260-13"></span>Garcia, M. and G. Parker (1991). Entrainment of bed sediment into suspension. *Journal of Hydraulic Engineering 117*(4), 414–435.
- <span id="page-260-18"></span><span id="page-260-6"></span>Garratt, J. (1977). Review of drag coefficients over oceans and continents. *Mon. Weather Rev. 105*, 915–929.
- Genet, L., D. Smith, and M. Sonnen (1974). Computer program documentation for the dynamic estuary model. *US Environmental Protection Agency, Systems Development Branch, Washington, DC*.
- <span id="page-260-14"></span>Gessler, J. (1967). The beginning of bedload movement of mixtures investigated as natural armoring in channels (translated by ea prych, california institute of technology), swiss federal institute of technology, zurich, laboratory of hydraulic research and soil mechanics.

{261}------------------------------------------------

<span id="page-261-21"></span>Gibbs, R. J. (1985). Estuarine flocs: their size, settling velocity and density. *Journal of Geophysical Research: Oceans 90*(C2), 3249–3251.

- <span id="page-261-26"></span><span id="page-261-24"></span>Giordani, P. and M. Astorri (1986). Phosphate analysis of marine sediments. *Chemistry in Ecology 2*(2), 103–111.
- Green, S. (1992). Modeling turbulent air flow in a stand of widely spaced trees. *PHOENICS Journal Computational Fluid Dynamics and its Applications 5*, 294–312.
- <span id="page-261-4"></span>Gropp, W., T. Hoefler, R. Thakur, and E. Lusk (2014). *Using advanced MPI: Modern features of the message-passing interface*. MIT Press.
- <span id="page-261-20"></span>Gulliver, J. S. and H. G. Stefan (1984). Stream productivity analysis with dorm—i: Development of computational model. *Water Research 18*(12), 1569–1576.
- <span id="page-261-1"></span>Guy, H. P., D. B. Simons, and E. V. Richardson (1966). *Summary of alluvial channel data from flume experiments, 1956-61*, Volume 462. US Government Printing Office.
- <span id="page-261-17"></span>Hageman, L. and M. Young (1981). Applied iterative methods academic. *New York*.
- <span id="page-261-16"></span><span id="page-261-15"></span>Haltiner, G. J. and R. T. Williams (1980). Numerical prediction and dynamic meteorology. Technical report.
- Hamill, G. A. and C. Kee (2016). Predicting axial velocity profiles within a diffusing marine propeller jet. *Ocean Engineering 124*, 69–88.
- <span id="page-261-8"></span>Hamrick, J. and T. Wu (1997). Computational design and optimization of the efdc/hem3d surface water hydrodynamic and eutrophication models. In *Next generation environmental models and computational methods*, pp. 143–161. Society for Industrial and Applied Mathematics Pennsylvania.
- <span id="page-261-9"></span>Hamrick, J. M. (1986). Long-term dispersion in unsteady skewed free surface flow. *Estuarine, Coastal and Shelf Science 23*(6), 807–845.
- <span id="page-261-3"></span>Hamrick, J. M. (1992). A three-dimensional environmental fluid dynamics computer code: Theoretical and computational aspects. Technical report, Virginia Institute of Marine Science, College of William and Mary.
- <span id="page-261-7"></span>Hamrick, J. M. (1996). User's manual for the environmental fluid dynamics computer code. *Special Reports in Applied Marine Science and Ocean Engineering (SRAMSOE) No. 33*.
- <span id="page-261-6"></span>Hamrick, J. M. (2006). A generic rooted aquatic plant and epiphyte algae sub-model for EFDC.
- <span id="page-261-19"></span>Harbeck Jr, G. (1964). Estimating forced evaporation from cooling ponds. *J. Power Div., Am. Soc. Civ. Eng.;(United States) 90*.
- <span id="page-261-13"></span>Heaps, N. (1965). Storm surges on a continental shelf.
- <span id="page-261-12"></span>Hersbach, H. (2011). Sea surface roughness and drag coefficient as functions of neutral wind speed. *Journal of Physical Oceanography 41*(1), 247–251.
- <span id="page-261-28"></span>Hofmann, E., E. Powell, J. Klinck, and E. Wilson (1992). Modeling oyster populations iii. critical feeding periods, growth and reproduction. *Shellfish Res. 11*(2), 399––416.
- <span id="page-261-14"></span>Hunt, J. N. (1979). Direct solution of wave dispersion equation. *Journal of the Waterway, Port, Coastal and Ocean Division 105*(4), 457–459.
- <span id="page-261-25"></span>Huu Chung, D. and D. P. Eppel (2008). Effects of some parameters on numerical simulation of coastal bed morphology. *International Journal of Numerical Methods for Heat & Fluid Flow 18*(5), 575–592.
- <span id="page-261-22"></span>Hwang, K.-N. and A. J. Mehta (1989). *Fine sediment erodibility in Lake Okeechobee, Florida*. Coastal & Oceanographic Engineering Department, University of Florida.
- <span id="page-261-2"></span>James, S. C., E. Seetho, C. Jones, and J. Roberts (2010). Simulating environmental changes due to marine hydrokinetic energy installations. In *OCEANS 2010 MTS/IEEE SEATTLE*, pp. 1–10. IEEE.
- <span id="page-261-18"></span><span id="page-261-0"></span>Jerlov, N. G. (1968). *Optical oceanography*. Elsevier Pub. Co. OCLC: 316568666.
- Ji, Z. (2008). *Hydrodynamics and water quality: modeling rivers, lakes, and estuaries*. John Wiley & Sons.
- <span id="page-261-5"></span>Jones, C. and W. Lick (2000). Effects of bed coarsening on sediment transport. In *Estuarine and Coastal Modeling*, pp. 915–930. ASCE.
- <span id="page-261-23"></span>Jones, C. and W. Lick (2001). SEDZLJ: A sediment transport model. *Final Report. University of California, Santa Barbara, California*.
- <span id="page-261-29"></span>Jordan, S. (1987). *Sedimentation and Remineralization Associated with Biodeposition by the American Oyster Crassostrea Virginica (Gmelin)*. University of Maryland, College Park.
- <span id="page-261-11"></span>Kantha, L. H. (2003, September). On an Improved Model for the Turbulent PBL. *Journal of the Atmospheric Sciences 60*(17), 2239–2246.
- <span id="page-261-10"></span>Kantha, L. H. and C. A. Clayson (1994). An improved mixed layer model for geophysical applications. *Journal of Geophysical Research: Oceans 99*(C12), 25235–25266.
- <span id="page-261-27"></span>Katul, G. G., L. Mahrt, D. Poggi, and C. Sanz (2004). One-and two-equation models for canopy turbulence. *Boundary-Layer Meteorology 113*(1), 81–109.

{262}------------------------------------------------

<span id="page-262-2"></span>Kee, C., G. A. Hamill, W. H. Lam, and P. W. Wilson (2006). Investigation of the velocity distributions within a ship's propeller wash. In *The 16th International Offshore and Polar Engineering Conference*, San Francisco, CA, pp. 451–456.

- <span id="page-262-12"></span>Kim, J., J. Jones, and D. Seo (2021). Factors affecting harmful algal bloom occurrence in a river with regulated hydrology. *Journal of Hydrology: Regional Studies 33*, 100769.
- <span id="page-262-14"></span>Kim, J. and D. Seo (2024). Three-dimensional augmentation for hyperspectral image data of water quality: An integrated approach using machine learning and numerical models. *Water Research 251*, 121125.
- <span id="page-262-11"></span>Kim, J., D. Seo, M. Jang, and J. Kim (2021). Augmentation of limited input data using an artificial neural network method to improve the accuracy of water quality modeling in a large lake. *Journal of Hydrology 602*, 126817.
- <span id="page-262-13"></span>Kim, J., D. Seo, and J. Jones (2022). Harmful algal bloom dynamics in a tidal river influenced by hydraulic control structures. *Ecological Modelling 467*, 109931.
- <span id="page-262-27"></span>Kim, J. H. (2019). *Ecological indices-based modelling of oyster aquaculture sustainability*. Ph. D. thesis, Pukyong National University, Republic of Korea.
- <span id="page-262-21"></span>Kim, T.-H., C.-S. Yang, J.-H. Oh, and K. Ouchi (2014). Analysis of the contribution of wind drift factor to oil slick movement under strong tidal condition: Hebei spirit oil spill case. *PloS one 9*(1), e87393.
- <span id="page-262-23"></span>Kobayashi, M., E. Hofmann, E. Powell, J.M.Klinck, and K. Kusaka (1997). A population dynamics model for the japanese oyster, crassostrea gigas. *Aquaculture 149*(3–4), 285–321.
- <span id="page-262-5"></span>Kraus, E. B. and J. A. Businger (1994). *Atmosphere-ocean interaction* (2nd ed ed.). Number no. 27 in Oxford monographs on geology and geophysics. Oxford University Press ; Clarendon Press.
- <span id="page-262-15"></span>Kremer, J. and S. Nixon (1978). A coastal marine ecosystem, 217 pp.
- <span id="page-262-16"></span>Kromkamp, J. C. and L. R. Mur (1984, 11). Buoyant density changes in the cyanobacterium Microcystis aeruginosa due to changes in the cellular carbohydrate content. *FEMS Microbiology Letters 25*(1), 105–109.
- <span id="page-262-8"></span>Krone, R. B. (1962). Flume studies of transport of sediment in estrarial shoaling processes. *Final Report, Hydr. Engr. and Samitary Engr. Res. Lab., Univ. of California*.
- <span id="page-262-0"></span>Large, W. and S. Pond (1981). Open ocean momentum flux measurements in moderate to strong winds.
- <span id="page-262-6"></span>Laursen, E. M. (1958). The total sediment load of streams. *Journal of the Hydraulics Division 84*(1), 1–36.
- <span id="page-262-4"></span>Lee, J. H. and V. Cheung (1990). Generalized lagrangian model for buoyant jets in current. *Journal of environmental engineering 116*(6), 1085–1106.
- <span id="page-262-9"></span>Leinonen, P. and D. Mackay (1975). A mathematical model of evaporation and dissolution from oil spills on ice, land, water and under ice. *Water Quality Research Journal 10*(1), 132–141.
- <span id="page-262-7"></span>Lick, W. and J. Lick (1988). Aggregation and disaggregation of fine-grained lake sediments. *Journal of Great Lakes Research 14*(4), 514–523.
- <span id="page-262-20"></span>Lijklema, L. (1980). Interaction of orthophosphate with iron (iii) and aluminum hydroxides. *Environmental Science & Technology 14*(5), 537–541.
- <span id="page-262-22"></span>Liu, J., J. Chen, T. Black, and M. Novak (1996). E-ε modelling of turbulent air flow downwind of a model forest edge. *Boundary-Layer Meteorology 77*(1), 21–44.
- <span id="page-262-1"></span>Longuet-Higgins, M. S. and R. Stewart (1964). Radiation stresses in water waves; a physical discussion, with applications. In *Deep Sea Research and Oceanographic Abstracts*, Volume 11, pp. 529–562. Elsevier.
- <span id="page-262-24"></span>Loosanoff, V. (1958). Some aspects of behavior of oysters at different temperatures. *Biol. Bull. 114*, 57–70.
- <span id="page-262-26"></span>Loosanoff, V. and F. Tommers (1948). Effect of suspended silt and other substances on rate of feeding of oysters. *Science 107*(2768), 69–70.
- <span id="page-262-10"></span>Mackay, D. and A. T. Yeun (1983). Mass transfer coefficient correlations for volatilization of organic solutes from water. *Environmental Science & Technology 17*(4), 211–217.
- <span id="page-262-3"></span>Madala, R. V. and S. A. Piacseki (1977). A semi-implicit numerical model for baroclinic oceans. *Journal of Computational Physics 23*(2), 167–178.
- <span id="page-262-17"></span>Madden, C. J., A. A. McDonald, and D. Gruber (2018). Florida bay seacom: Seagrass ecological assessment and community organization model documentation v. 15.1b. Technical report, South Florida Water Management District Technical Publication, Everglades Systems Assessment Division.
- <span id="page-262-19"></span>Mancini, J. L. (1983). A method for calculating effects, on aquatic organisms, of time varying concentrations. *Water Research 17*(10), 1355–1362.
- <span id="page-262-25"></span>Mann, R., E. M. Burreson, and P. K. Baker (1991). The decline of the virginia oyster fishery in chesapeake bay considerations for introduction of a non-endemic species, crassostrea gigas (thunberg, 1793). *Journal of Shellfish Research 10*(2), 379–388.
- <span id="page-262-18"></span>Matisoff, G. (1982). Mathematical models of bioturbation. In *Animal-sediment relations*, pp. 289–330. Springer.

{263}------------------------------------------------

<span id="page-263-17"></span>McIntire, C. D. (1973). Diatom associations in yaquina estuary, oregon: A multivariate analysis 1. *Journal of Phycology 9*(3), 254–259.

- <span id="page-263-13"></span>Mehta, A. J., E. J. Hayter, W. R. Parker, R. B. Krone, and A. M. Teeter (1989). Cohesive sediment transport. i: Process description. *Journal of Hydraulic Engineering 115*(8), 1076–1093.
- <span id="page-263-3"></span>Mellor, G. L. (1991). An equation of state for numerical models of oceans and estuaries. *Journal of Atmospheric and Oceanic Technology 8*(4), 609–611.
- <span id="page-263-9"></span>Mellor, G. L. and A. F. Blumberg (1985). Modeling vertical and horizontal diffusivities with the sigma coordinate system. *Monthly Weather Review 113*(8), 1379–1383.
- <span id="page-263-11"></span>Mellor, G. L., T. Ezer, and L.-Y. Oey (1994). The pressure gradient conundrum of sigma coordinate ocean models. *Journal of atmospheric and oceanic technology 11*(4), 1126–1134.
- <span id="page-263-4"></span>Mellor, G. L. and T. Yamada (1982). Development of a turbulence closure model for geophysical fluid problems. *Reviews of Geophysics 20*(4), 851–875.
- <span id="page-263-7"></span>Mengguo, L. and Q. Chongren (2003). Numerical simulation of wave-induced nearshore current. In *Proceedings of the International Conference on Estuaries and Coasts*. Citeseer.
- <span id="page-263-12"></span>Meyer-Peter, E. and R. Muller (1948). Formulas for bed-load transport. In ¨ *IAHSR 2nd meeting, Stockholm, appendix 2*. IAHR.
- <span id="page-263-5"></span>Meyers, J. and P. Sagaut (2006). On the model coefficients for the standard and the variational multi-scale smagorinsky model. *569*, 287.
- <span id="page-263-24"></span>Millero, F. J. (1986). The thermodynamics and kinetics of the hydrogen sulfide system in natural waters. *Marine Chemistry 18*(2-4), 121–147.
- <span id="page-263-20"></span>Morel, F. M. (1983). Principles of aquatic chemistry. *John Wiley and Sons, New York NY. 1983. 446*.
- <span id="page-263-23"></span>Morse, J. W., F. J. Millero, J. C. Cornwell, and D. Rickard (1987). The chemistry of the hydrogen sulfide and iron sulfide systems in natural waters. *Earth-science reviews 24*(1), 1–42.
- <span id="page-263-6"></span>Nezu, I. (1993). Turbulence in open-channel flows. *IAHR-monograph*.
- <span id="page-263-21"></span>O'Connor, D. J. and W. E. Dobbins (1958). Mechanism of reaeration in natural streams. *Transactions of the American Society of Civil Engineers 123*(1), 641–666.
- <span id="page-263-15"></span>Odum, E. P. (1971). Fundamentals of ecology–wb saunders company. *Philadelphia, London, Toronto*.
- <span id="page-263-26"></span>Officer, C. B., T. J. Smayda, and R. Mann (1982). Benthic filter feeding: A natural eutrophication control. *Marine Ecology - Progress Series 9*, 203–210.
- <span id="page-263-16"></span>Overman, C. and S. Wells (2022). Modeling cyanobacteria vertical migration. *Water 14*(6).
- <span id="page-263-2"></span>Park, K., A. Y. Kuo, J. Shen, and J. M. Hamrick (1995). A three-dimensional hydrodynamic-eutrophication model (hem-3d): Description of water quality and sediment process submodels. Technical report, Virginia Institute of Marine Science.
- <span id="page-263-14"></span>Parker, G., C. Paola, and S. Leclair (2000). Probabilistic exner sediment continuity equation for mixtures with no active layer. *Journal of Hydraulic Engineering 126*(11), 818–826.
- <span id="page-263-0"></span>Paulson, C. A. and J. J. Simpson (1977). Irradiance measurements in the upper ocean. *Journal of Physical Oceanography 7*(6), 952 – 956.
- <span id="page-263-8"></span>Peyret, R. and T. Taylor (1983). *Computational Methods for Fluid Flow*. Springer-Verlag.
- <span id="page-263-18"></span>Pfeifer, R. and W. McDiffett (1975). Some factors affecting primary productivity of stream riffle communities. *Archiv Fur Hydrobiologie*.
- <span id="page-263-25"></span>Poggi, D., A. Porporato, L. Ridolfi, J. Albertson, and G. Katul (2004). The effect of vegetation density on canopy sub-layer turbulence. *Boundary-Layer Meteorology 111*(3), 565–587.
- <span id="page-263-28"></span>Powell, E., J. Klinck, E. Hofmann, and S. Ray (1994, 01). Modeling oyster populations. iv: Rates of mortality, population crashes, and management. *Fishery Bulletin 92*.
- <span id="page-263-10"></span>Press, W., B. Flannery, S. Teukolsky, W. Vetterling, and J. Chipperfield (1986). *Numerical recipes: the art of scientific computing*. Cambridge University Press.
- <span id="page-263-27"></span>Quayle, D. (1988). *Pacific oyster culture in British Columbia*. Department of Fisheries and Oceans.
- <span id="page-263-19"></span>Redfield, A. C. (1963). The influence of organisms on the composition of seawater. *The sea 2*, 26–77.
- <span id="page-263-22"></span>Robbins, J., T. Keilty, D. White, and D. Edgington (1989). Relationships among tubificid abundances, sediment composition, and accumulation rates in lake erie. *Canadian Journal of Fisheries and Aquatic Sciences 46*(2), 223–231.
- <span id="page-263-1"></span>Roberts, J., R. Jepsen, D. Gotthard, and W. Lick (1998). Effects of particle size and bulk density on erosion of quartz particles. *Journal of Hydraulic Engineering 124*(12), 1261–1267.

{264}------------------------------------------------

<span id="page-264-11"></span>Rosati, A. and K. Miyakoda (1988). A general circulation model for upper ocean simulation. *Journal of Physical Oceanography 18*(11), 1601–1626.

- <span id="page-264-23"></span>Ross, M. J. and G. R. Ultsch (1980). Temperature and substrate influences on habitat selection in two pleurocerid snails (goniobasis). *American Midland Naturalist*, 209–217.
- <span id="page-264-22"></span>Runke, H. (1985). *Simulation of the lotic periphyton community of a small mountain stream by digital computer*. Ph. D. thesis, Thesis presented to Utah State University, Logan, Utah, in partial fulfill.
- <span id="page-264-15"></span>Sanford, L. P. and J. P.-Y. Maa (2001). A unified erosion formulation for fine sediments. *Marine Geology 179*(1-2), 9–23.
- <span id="page-264-27"></span>Sanz, C. (2003). A note on k-ε modelling of vegetation canopy air-flows. *Boundary-Layer Meteorology 108*(1), 191–197.
- <span id="page-264-2"></span>Semtner Jr, A. (1974). An oceanic general circulation model with bottom topography. Technical report.
- <span id="page-264-20"></span><span id="page-264-5"></span>Seo, D. (2019). Personal communication.
- Sheppard, P. (1958). Transfer across the earth's surface and through the air above.
- <span id="page-264-16"></span>Shields, A. (1936). Application of similarity principles and turbulence research to bed-load movement. Technical report.
- <span id="page-264-19"></span>Shiferaw, N., J. Kim, and D. Seo (2022). Identification of pollutant sources and evaluation of water quality improvement alternatives of a large river. *Environmental Science and Pollution Research 30*, 31546–31560.
- <span id="page-264-14"></span>Shrestha, P. L. and G. T. Orlob (1996). Multiphase distribution of cohesive sediments and heavy metals in estuarine systems. *Journal of Environmental Engineering 122*(8), 730–740.
- <span id="page-264-28"></span>Shumway, S. and R. Koehn (1982). Oxygen consumption in the american oyster crassostrea virginica. *Marine Ecology - Progress Series 9*(1), 59–68.
- <span id="page-264-8"></span>Simons, T. J. et al. (1973). Development of three-dimensional numerical models of the great lakes. In *IWD Scientific Series*, Volume 12. Inland Waters Directorate.
- <span id="page-264-4"></span>Smagorinsky, J. (1963). General circulation experiments with the primitive equations: I. the basic experiment. *Monthly weather review 91*(3), 99–164.
- <span id="page-264-13"></span>Smith, J. D. and S. McLean (1977). Spatially averaged flow over a wavy surface. *Journal of Geophysical Research 82*(12), 1735–1746.
- <span id="page-264-6"></span>Smith, S. and E. Banke (1975). Variation of the sea surface drag coefficient with wind speed. *Q. J. R. Meteorol. Soc. 101*, 665––673.
- <span id="page-264-9"></span>Smolarkiewicz, P. K. and T. L. Clark (1986). The multidimensional positive definite advection transport algorithm: Further development and applications. *Journal of Computational Physics 67*(2), 396–438.
- <span id="page-264-12"></span>Smolarkiewicz, P. K. and W. W. Grabowski (1990). The multidimensional positive definite advection transport algorithm: Nonoscillatory option. *Journal of Computational Physics 86*(2), 355–375.
- <span id="page-264-17"></span>Soulsby, R., R. Whitehouse, et al. (1997). Threshold of sediment motion in coastal environments. In *Pacific Coasts and Ports' 97: Proceedings of the 13th Australasian Coastal and Ocean Engineering Conference and the 6th Australasian Port and Harbour Conference; Volume 1*, pp. 145. Centre for Advanced Engineering, University of Canterbury.
- <span id="page-264-26"></span><span id="page-264-21"></span>Steele, J. H. (1962). Environmental control of photosynthesis in the sea. *Limnology and oceanography 7*(2), 137–150. Stewart, P. S., D. J. Tedaldi, A. R. Lewis, and E. Goldman (1993). Biodegradation rates of crude oil in seawater. *Water environment research 65*(7), 845–848.
- <span id="page-264-25"></span>Stiver, W. and D. Mackay (1984). Evaporation rate of spills of hydrocarbons and petroleum mixtures. *Environmental Science & Technology 18*(11), 834–840.
- <span id="page-264-10"></span>Stuart Churchill, H. C. (1975). Correlating equations for laminar and turbulent free convection from a vertical plate. *International Journal of Heat and Mass Transfer 18*(11), 1323–1329.
- <span id="page-264-24"></span>Stumm, W., J. J. Morgan, et al. (1970). *Aquatic chemistry; an introduction emphasizing chemical equilibria in natural waters*. Wiley-Interscience.
- <span id="page-264-0"></span>SWAN Team (2019). *Implementation Manual Swan Cycle III* (41.31 ed.). Delft University of Technology, Department of Civil Engineering.
- <span id="page-264-7"></span>Swart, D. H. (1974). Offshore sediment transport and equilibrium beach profiles.
- <span id="page-264-1"></span>Tetra Tech (2002a). Theoretical and computational aspects of sediment and contaminant transport in the efdc model. Technical report, US Environmental Protection Agency.
- <span id="page-264-18"></span>Tetra Tech (2002b). User's Manual for Environmental Fluid Dynamics Code. *Tetra Tech, Inc 1*.
- <span id="page-264-3"></span>Tetra Tech (2007a). The environmental fluid dynamics code theory and computation volume 2: Sediment and contaminant transport and fate.

{265}------------------------------------------------

<span id="page-265-10"></span>Tetra Tech (2007b). The environmental fluid dynamics code theory and computation volume 3: Water quality module. *Technical report, Tetra Tech, Inc., Fairfax, VA*.

- <span id="page-265-0"></span>Thanh, P. H. X., M. D. Grace, and S. C. James (2008). Sandia National Laboratories Environmental Fluid Dynamics Code: Sediment Transport User Manual. Technical Report SAND2008-5621, Sandia National Laboratories.
- <span id="page-265-20"></span>Thomann, R. V. and J. A. Mueller (1987). *Principles of surface water quality modeling and control*. Harper & Row Publishers.
- <span id="page-265-18"></span>Tillman, D. H., C. F. Cerco, M. R. Noel, J. L. Martin, and J. Hamrick (2004). Three-dimensional eutrophication model of the lower st. john river, florida. Technical report, Engineer Research And Development Center Vicksburg Ms Environmental Lab.
- <span id="page-265-22"></span>Troup, B. N. (1974). *The interaction of iron with phosphate, carbonate and sulfide in Chesapeake Bay interstitial waters: A thermodynamic interpretation*. Ph. D. thesis, Johns Hopkins University.
- <span id="page-265-12"></span>Tsai, C., S. Iacobellis, and W. Lick (1987). Flocculation of fine-grained lake sediments due to a uniform shear stress. *Journal of Great Lakes Research 13*(2), 135–146.
- <span id="page-265-2"></span>UNESCO (1981). *Background papers and supporting data on the international equation of state of seawater 1980*, Volume 38. Joint Panel on Oceanographic Tables and Standards and Centre interuniversitaire d'etudes europ ´ eennes ´ and International Council of Scientific Unions. Scientific Committee on Oceanic Research and International Association for the Physical Sciences of the Ocean.
- <span id="page-265-13"></span>van Niekerk, A., K. R. Vogel, R. L. Slingerland, and J. S. Bridge (1992). Routing of heterogeneous sediments over movable bed: Model development. *Journal of Hydraulic Engineering 118*(2), 246–262.
- <span id="page-265-11"></span>van Rijn, L. C. (1984). Sediment transport, part ii: suspended load transport. *Journal of hydraulic engineering 110*(11), 1613–1641.
- <span id="page-265-5"></span>Villemonte, J. R. (1947). Submerged weir discharge studies. *Engineering News-Record 139*(26), 54–56.
- <span id="page-265-1"></span>Vinokur, M. (1974). Conservation equations of gasdynamics in curvilinear coordinate systems. *Journal of Computational Physics 14*(2), 105–125.
- <span id="page-265-15"></span>Visser, P., J. Passarge, and L. Mur (1997, 08). Visser pm, passarge j, mur lr.. modelling vertical migration of the cyanobacterium microcystis. hydrobiologia 349: 99-109. *Hydrobiologia 349*, 99–109.
- <span id="page-265-8"></span>Ward, G. H. (1980). Hydrography and circulation processes of gulf estuaries. In *Estuarine and Wetland Processes*, pp. 183–215. Springer.
- <span id="page-265-16"></span>Warwick, J., D. Cockrum, and M. Horvath (1997). Estimating non-point-source loads and associated water quality impacts. *Journal of Water Resources Planning and Management 123*(5), 302–310.
- <span id="page-265-9"></span>Webster, I. T. and B. S. Sherman (1995). Evaporation from fetch-limited water bodies. *Irrigation Science 16*(2), 53–64.
- <span id="page-265-7"></span>Wells, S. A. and T. M. Cole (2000). Ce-qual-w2, version 3. Technical report, Army Engineer Waterways Experiment Station Vicksburg Ms Engineer Research.
- <span id="page-265-21"></span>Westrich, J. T. and R. A. Berner (1984). The role of sedimentary organic matter in bacterial sulfate reduction: The g model tested 1. *Limnology and oceanography 29*(2), 236–249.
- <span id="page-265-19"></span>Wezenak, C. T. and J. J. Gannon (1968). Evaluation of nitrification in streams. *Journal of the Sanitary Engineering Division 94*(5), 883–896.
- <span id="page-265-24"></span>White, M., E. Powell, and S. Ray (1988). Effect of parasitism by the pyramidellid gastropod boonea impressa on the net productivity of oysters (crassostrea virginica. *Estuarine, Coastal and Shelf Science 26*(4), 359 – 377.
- <span id="page-265-17"></span>Whitford, L. and G. Schumacher (1964). Effect of a current on respiration and mineral uptake in spirogyra and oedogonium. *Ecology 45*(1), 168–170.
- <span id="page-265-14"></span>Whitman, W., R. Russell, C. Welling, and J. Cochrane (1923). The effect of velocity on the corrosion of steel in sulfuric acid. *Industrial & Engineering Chemistry 15*(7), 672–677.
- <span id="page-265-3"></span>Wilson, B. (1960). Note on surface wind stress over water at low and high wind speeds. *J. Geophys. Res. 65*, 3377–3382.
- <span id="page-265-23"></span>Wilson, J. D., J. J. Finnigan, and M. R. Raupach (1998). A first-order closure for diturbed plant-canopy flows, and its application to winds in a canopy on a ridge. *Quarterly Journal of the Royal Meteorological Society 124*(547), 705–732.
- <span id="page-265-6"></span>Winiarski, L. D. and W. F. Frick (1976). *Cooling tower plume model*. US Environmental Protection Agency, Office of Research and Development.
- <span id="page-265-4"></span>Wu, J. (1982). Wind stress coefficients over sea surface from breeze to hurricane. *J. Geophys. Res. Oceans 87*, 9704–9706.

{266}------------------------------------------------

<span id="page-266-5"></span>Wu, W., S. S. Wang, and Y. Jia (2000). Nonuniform sediment transport in alluvial rivers. *Journal of hydraulic research 38*(6), 427–434.

- <span id="page-266-11"></span><span id="page-266-2"></span>Xiao, H. and P. Cinnella (2019). Quantification of model uncertainty in RANS simulations: A review. *108*, 1–31.
- Yamamoto, S., J. B. Alcauskas, and T. E. Crozier (1976). Solubility of methane in distilled water and seawater. *Journal of Chemical and Engineering Data 21*(1), 78–80.
- <span id="page-266-6"></span>Yang, C. T. (1973). Incipient motion and sediment transport. *Journal of the hydraulics division 99*(10), 1679–1704.
- <span id="page-266-7"></span>Yang, C. T. and A. Molinas (1982). Sediment transport and unit stream power function. *Journal of the Hydraulics Division 108*(6), 774–793.
- <span id="page-266-4"></span>Yelland, M., B. Moat, P. Taylor, R. Pascal, J. Hutchings, and V. Cornell (1998). Wind stress measurements from the open ocean corrected for airflow distortion by the ship.
- <span id="page-266-3"></span>Yelland, M. and P. Taylor (1996). Wind stress measurements from the open ocean. *J. Phys. Oceanogr. 26*(4), 541–558.
- <span id="page-266-0"></span>Ziegler, C. K. and W. Lick (1988). The transport of fine-grained sediments in shallow waters. *Environmental Geology and Water Sciences 11*(1), 123–132.
- <span id="page-266-1"></span>Ziegler, C. K. and W. J. Lick (1986). *A numerical model of the resuspension, deposition and transport of fine-grained sediments in shallow water*. Department of Mechanical & Environmental Engineering, University of California.
- <span id="page-266-8"></span>Ziegler, C. K. and B. Nisbet (1994). Fine-grained sediment transport in pawtuxet river, rhode island. *Journal of Hydraulic Engineering 120*(5), 561–576.
- <span id="page-266-9"></span>Ziegler, C. K. and B. S. Nisbet (1995). Long-term simulation of fine-grained sediment transport in large reservoir. *Journal of Hydraulic Engineering 121*(11), 773–781.
- <span id="page-266-10"></span>Zison, S. (1978). *Rates, Constants, and Kinetics Formulations in Surface Water Quality Modeling*. Ecological research series. Environmental Protection Agency, Office of Research and Development, Environmental Research Laboratory.