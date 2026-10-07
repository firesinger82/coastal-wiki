<<<PAGE 1>>>

## www.dsi.llc

<<<PAGE 2>>>

This document has been published by: DSI LLC Address: 110 W. Dayton Street #202, Edmonds, WA-98020, USA. Website: https://dsi.llc Email: info@dsi.llc Phone: +1 425 728 8440

Please cite this document as follows:

DSI LLC. 2024. EFDC+ Theory, Version 12. Published by DSI LLC, Edmonds WA. Available at https:// www.eemodelingsystem.com/wp-content/Download/Documentation/EFDC Theory Document Ver 12.pdf

<<<PAGE 3>>>

# Acknowledgement

DSI, LLC would like to acknowledge the contributions of numerous authors to the Environmental Fluid Dynamics Code Plus (EFDC+) Theory Document. The first version of the Theory Document was published by Dr. John Hamrick in 1992, with the release of the Environmental Fluid Dynamics Code (EFDC). After joining Tetra Tech, Dr. Hamrick added several enhancements to EFDC, along with documentation. Kyeong Park, along with several other authors, added the initial version of the CE-QUAL-ICM (ICM) kinetics for eutrophication, with accompanying documentation. Craig Jones added the initial SEDiment dynamics algorithms as developed by Ziegler, Lick, and Jones (SEDZLJ) implementation, along with separate documentation. Jeff Ji added Rooted Plant Epiphytes Module (RPEM) to EFDC and developed separate documentation, Finally, Scott James contributed to a number of other code and documentation enhancements. Of course, EFDC source code has been publicly available since the early 2000s, so there have been numerous other contributors, resulting in a large number of versions of EFDC.

Over the years, DSI has significantly expanded the original code, now referred to as EFDC+, improving its speed, stability, and accuracy and integrating it into a complete modeling package for hydrodynamics, sediment transport, toxics transport, and eutrophication. DSI has assembled many of the various theory documents and has developed an updated single comprehensive theory document for EFDC+.

Since 2009, the engineers at DSI have been the primary contributors to the updates and maintenance of this document. The primary DSI authors in this effort have been Paul Craig, Thomas Mathis, Tran Duc Kien, Jeffrey Jung, Kester Scandrett, and Anurag Mishra. These authors have brought their in-depth knowledge and careful documentation of all aspects of EFDC+ to the preparation and maintenance of this document, for the benefit of all EFDC+ users.

We would also like to express our acknowledgments to the EFDC+ user community who have provided us with multiple feedbacks that have helped shape EFDC+.

###### i

<<<PAGE 4>>>

# Contents

List of Abbreviations ix

- 1 INTRODUCTION 1

- 1.1 Development History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
- 1.2 EFDC+ Advancements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
- 1.3 Enhancements to EFDC+ since EEMS10.3 . . . . . . . . . . . . . . . . . . . . . . . . . . 4
- 1.4 EFDC+ Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
- 1.5 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7


- 2 HYDRODYNAMICS 8


- 2.0.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

- 2.1 Governing Equations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

2.1.1 Horizontal and Vertical Coordinate Systems . . . . . . . . . . . . . . . . . . . . . 9

- 2.1.2 Basic Hydrodynamic Equations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
- 2.1.3 Equation of State . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
- 2.1.4 Vertical Turbulent Closure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
- 2.1.5 Horizontal Turbulence Closure . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16


- 2.2 Boundary Conditions and External Forcings . . . . . . . . . . . . . . . . . . . . . . . . . . 16

- 2.2.1 Bottom Friction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
- 2.2.2 Vegetation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
- 2.2.3 Wind Forcings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
- 2.2.4 Wave Action . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
- 2.2.5 Local Wind-Generated Waves . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
- 2.2.6 Harmonic Forcings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
- 2.2.7 Hydraulic Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
- 2.2.8 Propeller Wash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30


- 2.3 Numerical Solution for the Equations of Motion . . . . . . . . . . . . . . . . . . . . . . . 32
- 2.4 Computational Aspects of the Three Time Level External Mode Solution . . . . . . . . . . 37
- 2.5 Computational Aspects of the Three-Time Level Internal Mode Solution . . . . . . . . . . 42
- 2.6 Vertical Layering Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

- 2.6.1 Standard Sigma (SIG) Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
- 2.6.2 Sigma-Zed Approach (SGZ) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47


- 2.7 Near-Field Discharge Dilution and Mixing Zone Analysis . . . . . . . . . . . . . . . . . . 48

- 2.7.1 Shear-Induced Entrainment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
- 2.7.2 Forced Entrainment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
- 2.7.3 Model Implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50


- 2.8 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52




###### ii

<<<PAGE 5>>>

###### CONTENTS EFDC+ Theory



###### 3 CONSERVATIVE CONSTITUENTS TRANSPORT 53

- 3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
- 3.2 Basic Equation of Advection-Diffusion Transport . . . . . . . . . . . . . . . . . . . . . . . 53
- 3.3 Numerical Solution for Transport Equations . . . . . . . . . . . . . . . . . . . . . . . . . . 54


###### 4 DYE MODULE 57

- 4.1 Decay . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
- 4.2 Age of Water . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58


###### 5 TEMPERATURE AND HEAT TRANSFER 59

- 5.1 Surface Heat Exchange . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

- 5.1.1 Full Heat Balance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
- 5.1.2 COARE 3.6 Bulk Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
- 5.1.3 Equilibrium Temperature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62


- 5.2 Short Wave Radiation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63

- 5.2.1 One-band Light Attenuation Model . . . . . . . . . . . . . . . . . . . . . . . . . . 63
- 5.2.2 Two-band Light Attenuation Model . . . . . . . . . . . . . . . . . . . . . . . . . 64
- 5.2.3 Water Quality Linked Light Attenuation . . . . . . . . . . . . . . . . . . . . . . . 64


- 5.3 Bed Heat Exchange . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
- 5.4 Ice Formation and Melt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

- 5.4.1 Heat Balance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
- 5.4.2 Ice Surface Temperature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
- 5.4.3 Freezing Temperature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
- 5.4.4 Ice Melt at Air/Water Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
- 5.4.5 Ice Growth/Melt at Bottom of Ice . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
- 5.4.6 Solar Radiation at Bottom of Ice . . . . . . . . . . . . . . . . . . . . . . . . . . . 69


- 5.5 Water Volume Evaporative Losses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70


###### 6 SEDIMENT TRANSPORT 72

- 6.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
- 6.2 Suspended Sediment Transport . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72

- 6.2.1 Governing Equations for Suspended Sediment Transport . . . . . . . . . . . . . . 72
- 6.2.2 Numerical Solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74


- 6.3 EFDC Sediment Transport Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

- 6.3.1 Non-Cohesive Sediment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
- 6.3.2 Cohesive Sediments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
- 6.3.3 Consolidation of Mixed Cohesive and Non-Cohesive Sediment Beds . . . . . . . . 92


- 6.4 SEDZLJ Sediment Transport Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95


- 6.4.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
- 6.4.2 Bed Shear Stress . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
- 6.4.3 Erosion Rate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
- 6.4.4 Suspended Load . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
- 6.4.5 Bedload . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
- 6.4.6 Bed Armoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107


###### 7 CHEMICAL FATE AND TRANSPORT 110

- 7.1 Development Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
- 7.2 Basic Equations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111


###### iii

<<<PAGE 6>>>

###### CONTENTS EFDC+ Theory



- 7.3 Chemical Partitioning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
- 7.4 Water Column Chemical Transport and Boundary Conditions . . . . . . . . . . . . . . . . 115

- 7.4.1 Numerical Solution to the Water Column Chemical Transport Equations . . . . . . 118

7.5 Sediment Bed Chemical Processes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121

- 7.5.1 Bedload Transport . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123


- 7.5.2 Numerical Solution to the Bed Chemical Process Equations . . . . . . . . . . . . . 123

7.6 Chemical Loss Terms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127

- 7.6.1 Bulk Degradation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127


- 7.6.2 Biodegradation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
- 7.6.3 Volatilization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128


###### 8 EUTROPHICATION 135

- 8.1 Water Column Eutrophication Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . 138

- 8.1.1 Model State Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
- 8.1.2 Conservation of Mass Equation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
- 8.1.3 Kinetic Equations for State Variables . . . . . . . . . . . . . . . . . . . . . . . . . 142
- 8.1.4 Settling, Deposition and Resuspension of Particulate Matter . . . . . . . . . . . . . 182
- 8.1.5 Method of Solution for Kinetics Equations . . . . . . . . . . . . . . . . . . . . . . 183


- 8.2 Rooted Aquatic Plants Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184

- 8.2.1 State Variable Equations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184

8.3 Sediment Diagenesis and Flux Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . 202

- 8.3.1 Depositional Flux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205


- 8.4 Appendix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222


- 8.3.2 Diagenesis Flux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
- 8.3.3 Sediment Flux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
- 8.3.4 Silica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218
- 8.3.5 Sediment Temperature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220
- 8.3.6 Method of Solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220


###### 9 LAGRANGIAN PARTICLE TRACKING 230 9.1 Basic Equations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230 9.2 Oil Spill Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233

- 9.2.1 Wind Drag . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
- 9.2.2 Loss Terms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233


###### 10 MARINE HYDROKINETICS 234

- 10.1 Theory of Marine Hydrokinetics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234
- 10.2 Implementation in EFDC+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235


###### 11 SHELLFISH FARMING 239

- 11.1 Governing Equation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239
- 11.2 Length - Weight Relation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240
- 11.3 Filtration Rate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240


- 11.3.1 Maximum Filtration Rate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240
- 11.3.2 Temperature Effect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
- 11.3.3 Salinity Effect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
- 11.3.4 Suspended Solids Effect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242
- 11.3.5 Dissolved Oxygen (DO) Effect . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242


###### iv

<<<PAGE 7>>>

###### CONTENTS EFDC+ Theory



- 11.4 Ingestion and Assimilation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242
- 11.5 Respiration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243
- 11.6 Reproduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244
- 11.7 Spawning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244


- 12 References 246


###### v

<<<PAGE 8>>>

# List of Tables

- 2.1 Parameters for Different Turbulent Models. . . . . . . . . . . . . . . . . . . . . . . . . . . 15
- 2.2 Values of Different Linear Wind Drag Relationships. . . . . . . . . . . . . . . . . . . . . . 21


- 5.1 Values of parameters determined by fitting the sum of two exponentials to observations of downward irradiance. Table adapted from Paulson and Simpson (1977). . . . . . . . . . . . 64
- 5.2 List of Evaporation Calculation Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . 71


- 7.1 Volatilization Input Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
- 8.1 Environmental Fluid Dynamics Code Plus (EFDC+) Water Quality State Variables . . . . . 137


- 8.2 Basal Metabolism Formulations and Parameter in Integrated Compartment Model or CEQUAL-ICM (ICM) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
- 8.3 Generic and Florida Bay Seagrass Model Parameters for Thalassia and Halodule species . . 185
- 8.4 Generic and Florida Bay Seagrass Model Parameters for Epiphytes . . . . . . . . . . . . . 186
- 8.5 Maximum Growth Rate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
- 8.6 List of Nutrient Limitation Parameters for the Florida Bay Seagrass Model . . . . . . . . . 187
- 8.7 Epiphyte Light Attenuation Parameter for Florida Bay Seagrass Model . . . . . . . . . . . 190
- 8.8 Parameters for Temperature Effect on Growth for Equation 8.150 . . . . . . . . . . . . . . 191
- 8.9 Parameters for Plant Density Effect on Growth for Equation 8.152 . . . . . . . . . . . . . . 192
- 8.10 Parameters for Shoot Respiration in the Florida seagrass model . . . . . . . . . . . . . . . 192
- 8.11 Parameters for Shoot Mortality of non-respiration loss in the Florida seagrass model . . . . 193
- 8.12 Root to Shoot Transport Parameters in Equation 8.157 . . . . . . . . . . . . . . . . . . . . 194
- 8.13 Parameters for Root Respiration in Equation 8.158 . . . . . . . . . . . . . . . . . . . . . . 194
- 8.14 Parameters for Root Mortality in Equation 8.159 . . . . . . . . . . . . . . . . . . . . . . . 194
- 8.15 EFDC+ Sediment Diagenesis Model State Variables . . . . . . . . . . . . . . . . . . . . . 203
- 8.16 Parameters Related to Algae in Water Column . . . . . . . . . . . . . . . . . . . . . . . . 222
- 8.17 Parameters Related to Zooplankton in Water Column . . . . . . . . . . . . . . . . . . . . . 223
- 8.18 Parameters Related to Organic Carbon (OC) in Water Column . . . . . . . . . . . . . . . . 225
- 8.19 Parameters Related to Phosphorus (P) in Water Column . . . . . . . . . . . . . . . . . . . 226
- 8.20 Parameters Related to Nitrogen (N) in Water Column . . . . . . . . . . . . . . . . . . . . . 227
- 8.21 Parameters Related to Silica (SiO2) in Water Column . . . . . . . . . . . . . . . . . . . . . 228
- 8.22 Parameters Related to Carbonaceous Oxygen Demand (COD) and Dissolved Oxygen (DO) in Water Column . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228
- 8.23 Parameters Related to Total Active Metals (TAM) and Fecal Coliform Bacteria in Water Column . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229
- 8.24 Assignment of Water Column Particulate Organic Matter (POM) to Sediment G Classes used in (Cerco and Cole, 1994) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229
- 8.25 Sediment Burial Rates (W) Used in (Cerco and Cole, 1994) . . . . . . . . . . . . . . . . . 229


###### vi

<<<PAGE 9>>>

# List of Figures

1.1 Overview of EFDC+ development history . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2 Primary Modules of the EFDC+ Model. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

- 2.1 Conceptual Overview of the EFDC+ Model. . . . . . . . . . . . . . . . . . . . . . . . . . 9
- 2.2 The Stretched Vertical Coordinate System. . . . . . . . . . . . . . . . . . . . . . . . . . . 10
- 2.3 Conceptual Framework for Vegetation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
- 2.4 Conceptual Framework for Wind-Generated Waves. . . . . . . . . . . . . . . . . . . . . . 24
- 2.5 Diagrams for propeller wash-induced momentum (a) coupling with an EFDC+ model grid cell and (b) splitting over vertical water layers. . . . . . . . . . . . . . . . . . . . . . . . . 32
- 2.6 Free Surface Displacement Centered Horizontal Grid. . . . . . . . . . . . . . . . . . . . . 33
- 2.7 U-centered grid in the horizontal (x, y) plane. . . . . . . . . . . . . . . . . . . . . . . . . . 41
- 2.8 U-centered Grid in the Vertical (x,z) Plane. . . . . . . . . . . . . . . . . . . . . . . . . . . 42
- 2.9 An Illustration of EFDC+ Layering Options for a Model with K = 10. (a) Standard Sigma (SIG), (b) Sigma Zed (SGZ)-Specified Bottom, and (c) SGZ-Uniform Layering. . . . . . . 47
- 2.10 Near field Jet Plume mixing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49


- 3.1 S-centered Grid in the Vertical (x,z)-Plane . . . . . . . . . . . . . . . . . . . . . . . . . . 54
- 3.2 Sigma Coordinate and Variable Center (Ji, 2008). . . . . . . . . . . . . . . . . . . . . . . . 55


- 5.1 Conceptual Framework for Temperature. . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
- 6.1 Structure of the Environmental Fluid Dynamics Code (EFDC) Sediment Transport Model. . 73

- 6.2 Structure of the SEDZLJ Sediment Transport Model. . . . . . . . . . . . . . . . . . . . . . 73
- 6.3 Conceptual Framework for EFDC Sediment Transport Module. . . . . . . . . . . . . . . . 77
- 6.4 Critical Shield’s shear velocity and settling velocity as a function of sediment grain size. . . 80
- 6.5 Schematic of the SEDFlume Apparatus. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
- 6.6 SEDFlume Data for Conowingo Reservoir (DNR Maryland). . . . . . . . . . . . . . . . . 98
- 6.7 Critical Shear Stresses for Erosion and Suspension of Quartz Particles. . . . . . . . . . . . 101
- 6.8 Results from Flume Measurements of Suspended Load and Bedload (Guy et al., 1966). . . . 103
- 6.9 Sample Probability Distributions for Cohesive and Non-Cohesive Particles. . . . . . . . . . 105
- 6.10 Diagram of SEDflume Layering System. . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
- 6.11 Erosion Rates Versus Particle Size and Shear Stress for a Bulk Density of 1.9 g/cm2, adapted from Roberts et al. (1998) by James et al. (2010). . . . . . . . . . . . . . . . . . . . . . . . 109


- 7.1 Conceptual Model of Chemical Fate and Transport in EFDC+. . . . . . . . . . . . . . . . 110

- 7.2 Linkage Between Hydrodynamic, Sediment Transport, and Chemical Fate and Transport Model. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
- 7.3 Covar Method (1976). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131


- 8.1 Structure of the EFDC+ Water Quality Model. . . . . . . . . . . . . . . . . . . . . . . . . 136


###### vii

<<<PAGE 10>>>

LIST OF FIGURES EFDC+ Theory

- 8.2 Schematic Diagram of EFDC+ Water Quality Model Structure. . . . . . . . . . . . . . . . 138
- 8.3 Interaction of Zooplankton with Eutrophication components. . . . . . . . . . . . . . . . . . 139
- 8.4 Velocity limitation function for (Option 1) the Monod equation where KMV = 0.25m/s and KMVmin = 0.15m/s, and (Option 2) the 5-parameter logistic function where a = 1.0, b = 12.0, c = 0.3, d = 0.35, and e = 3.0 (high velocities are limiting). . . . . . . . . . . . . 150
- 8.5 a) Macrophytes grow in vertical columns from bottom upwards and its impact on flow velocity. b) Plan view of macrophyte’s impact on flow velocity . . . . . . . . . . . . . . . . 152
- 8.6 Sediment Layers and Processes Included in Sediment Process Model . . . . . . . . . . . . 204
- 8.7 Schematic Diagram for Sediment Process Model . . . . . . . . . . . . . . . . . . . . . . . 205
- 8.8 Benthic stress (a) and its effect on particle mixing (b) as a function of overlying water column Dissolved Oxygen (DO) concentration. . . . . . . . . . . . . . . . . . . . . . . . . 212


viii

<<<PAGE 11>>>

# List of Abbreviations

C Carbon CH4 Methane CO2 Carbon dioxide Fe Iron FeS Iron monosulfide Mn Manganese

- N Nitrogen

NH4+ Ammonium NO−

- 2 Nitrite

NO−

- 3 Nitrate

O Oxygen P Phosphorus PO−3

- 4 Phosphate




Rq Richardson Number Rw Wave Reynolds Number SO−2

4 Sulfate S−

2 Sulfide SiO2 Silica

- 2D two-dimensional
- 3D three-dimensional


BOD Biological Oxygen Demand

CFD Computational Fluid Dynamics chl a Chlorophyll a COD Chemical Oxygen Demand

###### ix

<<<PAGE 12>>>

###### List of Abbreviations EFDC+ Theory



CSOD Carbonaceous Sediment Oxygen Demand

DO Dissolved Oxygen DOC Dissolved Organic Carbon DON Dissolved Organic Nitrogen DOP Dissolved Organic Phosphorus DSI DSI, LLC

EE EFDC+ Explorer EEMS EFDC+ Explorer Modeling System EFDC Environmental Fluid Dynamics Code EFDC+ Environmental Fluid Dynamics Code Plus EPA Environmental Protection Agency

###### ferric oxide Fe2O3(s)

ICM Integrated Compartment Model or CE-QUAL-ICM

LHS Left Hand Side LPOC Labile Particulate Organic Carbon LPON Labile Particulate Organic Nitrogen LPOP Labile Particulate Organic Phosphorus LPT Lagrangian Particle Tracking

MHK Marine and Hydro-Kinetic MPDATA Multidimensional Positive Definite Advection Transport Algorithm MPI Message Passing Interface

NetCDF Network Common Data Form NSOD Nitrogenous Sediment Oxygen Demand

OC Organic Carbon ON Organic Nitrogen OpenMP Open Multi-Processing

PO4d Dissolved Phosphate as Phosphorus PO4p Sorbed Phosphate as Phosphorus PO4t Total Phosphate as Phosphorus

###### x

<<<PAGE 13>>>

###### List of Abbreviations EFDC+ Theory



POC Particulate Organic Carbon

- POM Particulate Organic Matter
- PON Particulate Organic Nitrogen POP Particulate Organic Phosphorus


RHS Right Hand Side RPEM Rooted Plant and Epiphyte Model RPOC Refractory Particulate Organic Carbon RPON Refractory Particulate Organic Nitrogen RPOP Refractory Particulate Organic Phosphorus

SEDZLJ SEDiment dynamics algorithms as developed by Ziegler, Lick, and Jones SGZ Sigma Zed SiA Dissolved Available Silica SIG Standard Sigma SiP Particulate Biogenic Silica SNL-EFDC Sandia National Laboratory version of EFDC SOD Sediment Oxygen Demand

TAM Total Active Metals TMDL Total Maximum Daily Load TSS Total Inorganic Suspended Solids

W2 CE-QUAL-W2

###### xi

<<<PAGE 14>>>

# Chapter 1 INTRODUCTION

Environmental Fluid Dynamics Code Plus (EFDC+) is a surface water modeling system encompassing one-, two- and/or three-dimensional hydrodynamics and water column constituent transport. The hydrodynamics are internally coupled using an integrated, single source code implementation to multiple modules (including sediment erosion/deposition, propeller wash, chemical fate and transport, eutrophication kinetics, sediment diagenesis, particle tracking and oil spill). EFDC+ and its predecessor, EFDC has been used worldwide in support of environmental assessment, management and regulatory requirements for hundreds of water bodies such as rivers, lakes, reservoirs, wetlands, estuaries, and coastal ocean regions.

##### 1.1. Development History

EFDC+ is based on the public-domain, open-source version of EFDC (Hamrick, 1992) originally developed at the Virginia Institute of Marine Science (VIMS) and School of Marine Science of The College of William and Mary, by Dr. John M. Hamrick beginning in 1988. The historical evolution of EFDC+ has to a great extent been application driven by a diverse group of modelers in the academic, governmental, and private sectors, as highlighted in Figure 1.1.

Since 2000, DSI, LLC (DSI) has provided ongoing enhancement and development to EFDC for various surface water, sediment transport, and water quality projects. This includes adding multiple new features based on the theory described in this document. DSI’s improvements to the EFDC code are so extensive that in 2016, the DSI version of EFDC was renamed as EFDC+.

###### 1



<<<PAGE 15>>>

###### 1. INTRODUCTION EFDC+ Theory



Fig. 1.1. Overview of EFDC+ development history

##### 1.2. EFDC+ Advancements

EFDC+ reflects the following key enhancements over EFDC:

- • Open Multi-Processing (OpenMP) - Multithreading: Integration of OpenMP into EFDC+ provides vastly improved model run times. The Intel® OpenMP Runtime Library binds OpenMP threads to physical processing units. EFDC+ typically produces run times up to four times faster on a six-core processor than the conventional single-threaded EFDC model.
- • Dynamic Memory Allocation: Dynamic memory allocation eliminates the need to re-compile EFDC for distinct applications. Previously, due to the limitations of Fortran 77, different maximum array sizes were required to specify computational grid domain and time series input data sets. Dynamic allocation also helps mitigate array indexing errors and provides better traceability for source code development and testing.
- • Domain Decomposition and Message Passing Interface (MPI): Domain decomposition in EFDC+ can significantly increase the model execution time. This is accomplished by splitting up the domain of a model into several smaller ones, referred to as subdomains (Fainchtein, 2014). Each subdomain executes like a traditional EFDC+ run, except that each subdomain exchanges information with its neighboring subdomain at each time step (Gropp et al., 2014). This information exchange is accomplished by leveraging Intel’s version of MPI to communicate between domains.
- • Sigma Zed (SGZ) Layering: EFDC+ avoids the pressure gradient errors that occur in model simulations of steep changes in bed elevation by using the SGZ layering option. Unlike the original EFDC,


###### 2



<<<PAGE 16>>>

###### 1. INTRODUCTION EFDC+ Theory



- which uses a Sigma (SIG) coordinate transformation in the vertical direction and the same number of layers for all cells in the domain, SGZ in EFDC+ allows the number of vertical layers to vary over the model domain. This approach is computationally efficient and significantly improves the simulation of density stratification.
- • Hydraulic Structures: EFDC+ implements equations governing hydraulic structures such as culverts, weirs, sluice gates, and orifices, which differs from the previous approach which only allowed rating curves for hydraulic structures. Additionally, the modeler can specify rules of operations that depend on the model hydrodynamics.
- • Enhanced Heat Exchange: EFDC+ includes heat exchange options that use equilibrium temperatures for the water and atmospheric interface and spatially variable sediment bed temperatures. The water column concentrations in the eutrophication and sediment transport modules are now coupled with the heat module by including spatially and temporally varying light extinction.
- • Ice Formation and Melt: EFDC+ includes a heat-coupled ice formation and melt approach to handle cold climates. Surface processes are controlled by the presence or absence of a dynamically computed ice cover.
- • Multiple Dyes: EFDC+ can simulate an unlimited number of user-defined dye classes, including “Age of Water”. Decay and/or growth and settling can be added to any dye class.
- • Lagrangian Particle Tracking (LPT): An LPT module has been added to EFDC+, which allows simulation of track releases/discharges and mixing studies. Particle settling, decay, and other processes are user configurable. LPT modeling applications include oil spill and emergency response simulations, among many others.
- • SEDZLJ Sediment Transport Implementation: Sandia National Laboratory version of EFDC (SNL-EFDC) (Thanh et al., 2008) contains the SEDiment dynamics algorithms as developed by Ziegler, Lick, and Jones (SEDZLJ) (Jones and Lick, 2000; Ziegler and Lick, 1988, 1986) for sediment transport computation. DSI further enhanced this model in EFDC+ and implemented significant improvements for mass balance, hard bottom bypass, and computational efficiency. The SEDZLJ model is linked to the Chemical Fate and Transport module in EFDC+.
- • Propeller Wash Module: EFDC+ includes a propeller wash module, which uses a subgrid-based velocity/erosion field tracking to simulate the impacts of ship movement on hydrodynamics and sediment transport.
- • Internal Wind Wave Generation: A wind-generated wave module has been added to EFDC+ to enable the computation of wind wave-generated bed shear stress on sediment resuspension, with or without wave-induced currents.
- • External Wave Model Linkage: Linkage to SWAN (SWAN Team, 2019) and other external wave models has been simplified and improved in EFDC+.
- • Rooted Plant and Epiphyte Model (RPEM) Module: An RPEM module was incorporated into a version of EFDC to better simulate water quality interactions with submerged aquatic vegetation such as epiphytic algae and macrophytes (Hamrick, 2006). This was also subsequently incorporated into EFDC+.


###### 3



<<<PAGE 17>>>

###### 1. INTRODUCTION EFDC+ Theory



- • Shellfish Farming Module: A shellfish farming module was added to EFDC+ to simulate the kinetic processes of shellfish, including filtering, ingestion, assimilation, respiration, mortality, and spawning.
- • Marine and Hydro-Kinetic (MHK) Linkage: EFDC+ includes an MHK module for simulating the potential effects of installing and operating turbines and wave energy converters in rivers, tidal channels, ocean currents, and other water bodies. This code is adapted from SNL-EFDC (Thanh et al., 2008).
- • Run Continuation: If the model crashes or the user wishes to extend the period of simulation, the EFDC+ model can be configured as a continuation run, where the model outputs are seamlessly appended to the previous run.
- • Spatially and Temporally Varying Fields: Pressure fields, bathymetry, and/or other data such as roughness and vegetation can be dynamically adjusted during the model run in EFDC+. This allows for dredging scenarios and seasonal vegetation patterns. In addition, the boundary conditions can also be input as spatially and temporally varying fields. This helps connect EFDC+ with external sources or numerical models.
- • Network Common Data Form (NetCDF) Output: EFDC+ can output results in NetCDF file formats. NetCDF is a community standard for sharing scientific data.
- • High-Frequency Output: New output snapshot controls are available to target specific periods for high-frequency output within the standard output frequency.
- • Code Streamlining: The code has been converted to Fortran 90 and streamlined for quicker execution times.
- • Model Linkages: Users can customize the linkage of model results for use with the Windows-based EFDC+ Explorer (EE) graphical pre- and post-processor.


##### 1.3. Enhancements to EFDC+ since EEMS10.3

Enhancement of EFDC+ has since the previous iteration of this theory document for EEMS10.3. Many of the changes do not involve changes to theory, but rather provide improved processes within modules and increased interactions between modules. Improvements have been made to the propeller wash module and the jet and plume module. Some of the significant additions include:

- • The ICM kinetics have been rewritten to allow unlimited phytoplankton, periphyton, and macrophyte classes. Additionally, zooplankton has been added as an integrated part of algal dynamics.
- • Macrophyte growth capability has been added between layers and for the base of the macrophytes to be in any layer. This allows for floating macrophytes to start at the surface and drape down into the water column.
- • “Fast settling” of cohesive classes eroded by propwash have been added to the SEDZLJ sediment transport module. The fast settling classes reflect the process of mass erosion due to a more turbulent and energetic flow field in the propwash plume. These mass eroded sediments then behave differently in the water column than the original sediment classes, as larger chunks settle faster than the discrete particle erosion of more uniform flow patterns. This option was added to address different settling rates of material eroded by mass or bulk erosion of a cohesive bed (i.e., eroded chunks).


###### 4



<<<PAGE 18>>>

###### 1. INTRODUCTION EFDC+ Theory



- • The “fast settling” approach has also been fully integrated into the ChemFate module.
- • ChemFate partitioning options have been supplemented. This new feature allows the user to control partitioning on a cell-by-cell basis to better represent spatially varying site conditions. There are now two new files, PARTITIONB.INP and PARTITIONW.INP to allow for spatial varying of toxic partition coefficients in the sediment bed and water column.
- • A tropical cyclone module has been added, and the performance of the associated wind field boundary condition option has been improved.
- • A user-defined wind drag option has been added.
- • Two new open boundary condition types have been added. A free tangential and a zero tangential anti-reflection boundary condition were needed to improve the propagation of waves out of the model domain without reflecting off the open boundary.
- • The use of harmonics for defining open boundary water levels for zero tangential and free tangential radiation boundary conditions have been improved to handle non-zero average tidal levels.
- • Withdrawal layers have been limited to only active layers. This check was needed because the SigmaZed vertical layering approach can use different numbers of layers per cell.
- • Horizontal eddy diffusivity and viscosity have been disabled for large aspect ratio cells on the open boundary.
- • The NetCDF output has been updated to the latest format, UGRID. It also writes the Lagrangian particle tracking output, which is now a separate file.
- • EFDC+ is now linked to the WASP8 water quality model. EFDC+ now writes out the *.HYD file, allowing WASP to use the hydrodynamics to run the model.


##### 1.4. EFDC+ Overview

EFDC+ is the most up-to-date, enhanced version of EFDC, which is one of the most popular threedimensional (3D) hydrodynamic and water quality models available. The U.S. Environmental Protection Agency (EPA) describes the original EFDC as “a state-of-the-art hydrodynamic model that can be used to simulate aquatic systems in one, two, and three dimensions. It has evolved over the past two decades to become one of the most widely used and technically defensible hydrodynamic models in the world.” DSI created EFDC+ by taking the original version of EFDC and vastly improving its speed, stability, and accuracy. Since 1998, DSI has continually upgraded the model’s hydrodynamics and stability while also decreasing run times. EFDC+ now far surpasses the features and performance of the legacy code.

EFDC+ contains multiple modules and features, which are highlighted in Figure 1.2 and described in subsequent chapters.

###### 5



<<<PAGE 19>>>

###### 1. INTRODUCTION EFDC+ Theory



###### Fig. 1.2. Primary Modules of the EFDC+ Model.

###### 6



<<<PAGE 20>>>

###### 1. INTRODUCTION EFDC+ Theory



##### 1.5. Conclusion

EFDC+ is a surface water modeling system developed by DSI, and is built upon the original EFDC software developed by Hamrick (1992). EFDC+ includes many new features and bug fixes over the original EFDC code. This document describes the mathematical details of all modules available in EFDC+.

EFDC+ executable is available as a part of the EFDC+ Explorer Modeling System (EEMS) package available through DSI. For more details about EEMS, please visit https://www.eemodelingsystem.com/. EFDC+ source code is open source and is available on our public repository (https://github.com/dsi-llc/EFDCPlus). We encourage and seek inputs from the user community and partnership with the research community in improving EFDC+.

###### 7



<<<PAGE 21>>>

# Chapter 2 HYDRODYNAMICS

##### 2.0.1 Overview

The EFDC+ hydrodynamics module simulates near-field plume, wind-generated, and externally linked wave models. In the hydrodynamics module, temperature and salinity may be optionally incorporated to address density effects. The hydrodynamics module is linked to other modules, such as dye/age of water, sediments, chemicals, water quality, LPT and propeller wash, as illustrated in Figure 1.2. EFDC+ is a coupled model which solves hydrodynamics, transport, and kinetics in an integrated code, thus eliminating the need for external coupling between hydrodynamics and transport modules.

This section is primarily based on Hamrick (1992) and Ji (2008) with updates from DSI and others. The basic governing equations for the EFDC+ hydrodynamics are presented and discussed. The primary sources used for this document are:

- 1. A Three-Dimensional Environmental Fluid Dynamics Computer Code: Theoretical and Computational Aspects (Hamrick, 1992).
- 2. A User’s Manual for the Environmental Fluid Dynamics Computer Code (EFDC), (Hamrick, 1996).
- 3. A Three-dimensional Hydrodynamic-Eutrophication model (HEM3D): Description of Water Quality and Sediment Processes Submodels (Park et al., 1995).
- 4. Theoretical and Computational Aspects of Sediment and Contaminant Transport in the EFDC Model (Tetra Tech, 2002a).
- 5. Sandia National Laboratories Environmental Fluid Dynamics Code: Sediment Transport User Manual (Thanh et al., 2008).


##### 2.1. Governing Equations

The fundamental principles of the hydrodynamic model in EFDC+ are the laws of conservation for mass, momentum, and energy for the flows. With the basic assumption that ambient environmental flows are characterized by horizontal length scales which are orders of magnitude greater than their vertical length scales, the formulation of the governing equations begins with the vertically hydrostatic, boundary layer

###### 8



<<<PAGE 22>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



form of the turbulent equations of motion for an incompressible, variable density fluid. The governing equations of EFDC+ include Navier-Stokes for fluid flow, the advection-diffusion equations for salinity, temperature, dye, toxicants, eutrophication constituents and suspended sediment transport (Hamrick and Wu, 1997; Hamrick, 1992, 1996). In the horizontal direction, the equations are presented in the curvilinear coordinate system and SIG or SGZ (Craig et al., 2014) transformation (at the bed and at the water surface) for the vertical direction. They are discretized with the finite difference method based on an explicit scheme.

- Figure 2.1 shows the basic concepts of the EFDC+ model domain.


A

TMOSPHERE

Evaporation

τsy τsx

Wind Shear

Precipitation

1.0

Wave

WATERCOLUMN

V

SIGMA

W

- U

W

- V


U

τby τbx

V

0.0

W

BottomShear

U

BED

Groundwater

DX

DY

Fig. 2.1. Conceptual Overview of the EFDC+ Model.

##### 2.1.1 Horizontal and Vertical Coordinate Systems

To accommodate realistic horizontal boundaries, it is convenient to formulate the equations such that the horizontal coordinates, x and y, are curvilinear and orthogonal.

To provide uniform resolution in the vertical direction, aligned with the gravitational vector and bounded by bottom topography and a free surface permitting long wave motion, a time variable mapping or stretching transformation is desirable. The mapping or stretching is given by

###### 9



<<<PAGE 23>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



where,

z∗ +h ζ +h

z =

z∗ +h H

=

(2.1)

z is the sigma coordinate (dimensionless), z∗ is the vertical coordinate with respect to the vertical reference level (datum) (m), h is the water depth below the vertical reference level (m), ζ is the water surface elevation above the vertical reference level (m), and H is the total depth of water columns (m), defined as or ζ + h.

- Figure 2.2 provides a schematic of the vertical coordinate system in the physical space in the left panel and the sigma space in the right panel.


Fig. 2.2. The Stretched Vertical Coordinate System.

EFDC+ supports SIG stretched and SGZ grids for the vertical discretization of the water column. Details of the sigma transformation may be found in Blumberg and Mellor (1987); Hamrick (1986); Vinokur (1974). Details on the SGZ vertical layering options are described in Section 2.6.2

##### 2.1.2 Basic Hydrodynamic Equations

Transforming the vertically hydrostatic boundary layer form of the turbulent equations of motion and utilizing the Boussinesq approximation for variable density results in the momentum and continuity equations and the transport equations for salinity and temperature shown in the following equations.

- The momentum equation in the x direction:


###### 10



<<<PAGE 24>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



∂ ∂t

∂ ∂x

∂ ∂y

(mxmyHu)+

(myHuu)+

∂my ∂x −u

∂mx ∂y

−mxmy fHv− v

∂ ∂x

(gζ + p+Patm)−my

=−myH

∂u ∂y

∂ ∂z

∂ ∂y

mxmy H

mx my

HAH

+

+

(mxHvu)+

Hv

∂ ∂z

(mxmywu)

∂h ∂x −z

∂u ∂x

∂H ∂x

∂ p ∂z

∂ ∂x

my mx

HAH

+

∂u ∂z −mxmycpDpu u2 +v2 +Su

Av

(2.2)

- The momentum equation in the y direction: ∂

∂t

(mxmyHv)+

∂ ∂x

(myHuv)

+

∂ ∂y

(mxHvv)+

∂ ∂z

(mxmywv)+mxmy fHu+ v

∂my ∂x −u

∂mx ∂y

Hu

=−mxH

∂ ∂y

(gζ + p+Patm)−mx

∂h ∂y −z

∂H ∂y

∂ p ∂z

+

∂ ∂x

my mx

HAH

∂v ∂x

+

∂ ∂y

mx my

HAH

∂v ∂y

+

∂ ∂z

mxmy H

Av

∂v ∂z −mxmycpDpv u2 +v2 +Sv

(2.3)

- The momentum equation in the z direction:


ρ −ρ0 ρ0

∂ p ∂z

= −gHb (2.4) The continuity equations (internal and external modes):

= −gH

∂ ∂t

(mxmyζ)+

∂ ∂t

(mxmyζ)+

∂ ∂x

∂ ∂y

(myHu)+

∂ ∂x

(myHU)+

∂ ∂z

(mxHv)+

(mxmyw) = Sh (2.5)

∂ ∂y

(mxHV) = Sh (2.6)

where U and V are the depth-integrated horizontal velocities,

U =

1 0

udz, V =

1 0

vdz (2.7)

The equation of state for the density of water:

ρ = ρ (p,S,T,C) (2.8)

The continuity equations for salinity S and temperature T:

and

∂ ∂t

(mHS)+

∂ ∂t

(mHT)+

∂ ∂x

(myHuS)+

∂ ∂x

∂ ∂y

(myHuT)+

∂ ∂y

(mxHvS)+

(mxHvT)+

∂ ∂z

(mwS) =

∂ ∂z

(mwT) =

∂ ∂z

(mH−1Ab

∂ ∂z

S)+QS (2.9)

∂ ∂z

(mH−1Ab

∂ ∂z

T)+QT (2.10)

###### 11



<<<PAGE 25>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



- u, v are the horizontal velocity components in the curvilinear coordinates (m/s), x, y are the orthogonal curvilinear coordinates in the horizontal direction (m), z is the sigma coordinate (dimensionless), t is time (s), mx, my are the square roots of the diagonal components of the metric tensor (dimensionless), m is the Jacobian of the metric tensor determinant (dimensionless), m = mxmy, p is the physical pressure in excess of the reference density hydrostatic pressure (m2/s2), Patm is the barotropic pressure normalized by the reference water density (m2/s2), ρo is the reference water density (kg/m3), b is the buoyancy, f is the Coriolis parameter (1/s), AH is the horizontal momentum and mass diffusivity (m2/s), Av is the vertical turbulent eddy viscosity (m2/s), cp is the vegetation resistance coefficient (dimensionless), Dp is the projected vegetation area normal to the flow per unit horizontal area (dimensionless),


Su, Sv are the source/sink terms for the horizontal momentum in the x and y directions, respectively (m2/s2),

Sh is the source/sink terms for the mass conservation equation (m3/s),

- S is salinity (ppt),
- T is temperature (◦C), C is Total Inorganic Suspended Solids (TSS) (g/m3), and
- U, V are the depth averaged velocity components in the x and y directions, respectively (m/s).


The vertical velocity, with physical units, in the stretched, dimensionless vertical coordinate z is w, and is related to the physical vertical velocity w∗ by:

w = w∗ −z

∂ζ ∂t

∂ζ ∂x

∂ζ ∂y

u mx

v my

+

+

+(1−z)

∂h ∂x

∂h ∂y

u mx

v my

+

(2.11)

where,

w is the vertical velocity component in SIG coordinate (m/s) and w∗ is the physical vertical velocity (m/s).

The pressure p is the physical pressure in excess of the reference density hydrostatic pressure, ρogH(1−z) divided by the reference density, ρo. In the momentum equation (2.2) and (2.3), the momentum source/sink terms Su and Sv are later modeled as subgrid scale horizontal diffusion. The density ρ is in general a function of temperature T and salinity S for hydrospheric flows and water vapor for atmospheric flows. Density can be a weak function of pressure but water is treated as an incompressible fluid in the continuity equation under the anelastic approximation (Clark and Hall, 1991; Mellor, 1991).

###### 12



<<<PAGE 26>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



The buoyancy, b as defined in equation (2.4) is the normalized deviation of density from the reference value. The continuity equation (2.5) has been integrated with respect to z over the interval (0,1) to produce the depth integrated continuity equation (2.6) using the vertical boundary conditions, w = 0, at z = (0,1), which follows from the kinematic conditions and equation (2.7). It is noted that constraining the free surface displacement to be time independent and spatially constant, yields the equivalent of the rigid lid ocean circulation equations employed by Semtner Jr (1974) and equations similar to the terrain following equations used by Clark (1977) to model mesoscale atmospheric flow.

##### 2.1.3 Equation of State

In case the water density is dependent on temperature and salinity, the UNESCO’s equation of state (UNESCO, 1981) reads

ρ =999.842594+6.793952×10−2T−9.095290×10−3T2 (2.12)

+1.001685×10−4T3−1.120083×10−6T4+6.536332×10−9T5

+ 0.824493−4.0899×10−3T+7.6438×10−5T2 −8.2467×10−7T3+5.3875×10−9T4 S

+ −5.72466×10−3+1.0227×10−4T−1.6546×10−6T2 S1.5+4.8314×10−4S2 where,

ρ is the water density (kg/m3), T is the water temperature (◦C), and S is the water salinity (ppt).

With the presence of sediment in the water column, the water density and the buoyancy are corrected using a correction factor. The correction factor, per Tetra Tech (2007a), for the water density is

where,

N

CTSS = 1−

N

### ∑

ρs,jCj +

j

### ∑

(sj −1)ρs,jCj (2.13)

j

CTSS is the correction factor that considers the influence of sediment on water density (dimensionless), ρs,j is the sediment density of the sediment class j (kg/m3), Cj is the concentration of the sediment class j (g/m3), sj is the specific gravity of the sediment class j (dimensionless), and N is the number of sediment classes.

###### 13



<<<PAGE 27>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



- 2.1.4 Vertical Turbulent Closure The system of eight equations from equations (2.2) to (2.11) provides a closed system for the variables u,


- v, w, p, ζ, ρ, and C, provided that the vertical turbulent viscosity and diffusivity, and the source and sink terms are specified. To provide the vertical turbulent viscosity and diffusivity, the second moment turbulence closure model developed by Mellor and Yamada (1982) and modified by Galperin et al. (1988) can be used. The model relates the vertical turbulent viscosity and diffusivity to the turbulent intensity (q2), turbulent length scale (l), and Richardson Number (Rq) as shown in the following equations. The vertical turbulent momentum diffusion coefficient is:


Av = φAA0ql, (2.14) where, φA is the stability viscosity coefficient and can be defined as:

(1+Rq/R1) (1+Rq/R2)(1+Rq/R3)

φA =

Additionally, the following definitions for variables in equations (2.14) and (2.15) are given as:

(2.15)

6A1 B1

A0 =A1 1−3C1 −

1 B11/3

=

(2.16)

1

- R1

=3A2

(B2 −3A2) 1− 6BA11 −3C1(B2 +6A1) 1−3C1 − 6BA11

(2.17) 1

- R2

=9A1A2 (2.18) 1

- R3


=3A2[6A1 +B2(1−C3)]. (2.19)

The vertical mass diffusion coefficient is defined as:

Ab = ρKK0ql (2.20) where, φK is the stability diffusivity coefficient given by

1 (1+Rq/R3)

φK =

(2.21)

and K0 is the dimensionless coefficient:

6A1 B1

K0 = A2 1−

The Richardson number can be calculated as,

l2 H2

∂b ∂z

gH q2

Rq =

where,

(2.22)

(2.23)

###### 14



<<<PAGE 28>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



- q2 is the turbulent intensity (m2/s2), l is the turbulent length scale (m), and Rq is the Richardson number.


Mellor and Yamada (1982) specify the constants A1 = 0.92, B1 = 16.6,C1 = 0.08, A2 = 0.74, and B2 = 10.1. However, the values of R1, R2, R3 calculated by Galperin et al. (1988) and Kantha and Clayson (1994) are different from Mellor and Yamada (1982) as in Table 2.1.

Table 2.1. Parameters for Different Turbulent Models.

Formulation K0 R−1

1 R−1

2 R−1

3

Mellor and Yamada (1982) 0.493928 7.846436 34.676400 6.127200 Galperin et al. (1988) 0.493928 7.760050 34.676440 6.127200 Kantha and Clayson (1994) 0.493928 8.679790 30.192000 6.127200 Kantha (2003) 0.490025 14.509100 24.388300 3.236400

The stability functions φA and φK account for the reduced and enhanced vertical mixing or transport in stable and unstable vertically density stratified environments, respectively. The turbulence intensity and the turbulence length scale are determined by a pair of Mellor and Yamada (1982) equations:

∂ ∂t

∂ ∂z

=

∂ ∂x

∂ ∂y

mHq2 +

Pq2 +

∂q2 ∂z

∂u ∂z

Aq H

Av H

m

2m

∂ ∂z

Qq2 +

2

∂v ∂z

+

mwq2

2

Hq3 B1l

∂b ∂z −2m

+Sb

+2mgAb

(2.24)

∂ ∂t

∂ ∂z

=

∂ ∂x

∂ ∂y

mHq2l +

Pq2l +

∂ ∂z

Aql H

q2l +mlE1

m

Hq3 B1

−mE2

1+E4

l κHz

2

∂ ∂z

Qq2l +

2

∂u ∂z

Av H

+

mwq2l

∂v ∂z

+E5

l κH(1−z)

2

2

∂b ∂z

+E3gAb

+Sl

(2.25)

where,

1 L

1 H

=

1 z

1 1−z

+

, (2.26)

E1 = 1.8, E2 = 1.0, E3 = 1.8, E4 = 1.33, and E5 = 0.25 are empirical constants, Sq is the source-sink term for turbulent intensity equation, Sl is the source-sink term for turbulent length scale equation,

###### 15



<<<PAGE 29>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



Aq is the vertical turbulent diffusivity for turbulent intensity equation, and Aql is the vertical turbulent diffusivity for turbulent length scale equation.

The vertical diffusivity for turbulence intensity, Aq is set to 0.2ql following Mellor and Yamada (1982). For stable stratification, Galperin et al. (1988) suggested limiting the length scale such that the square root of Rq is less than 0.53.

##### 2.1.5 Horizontal Turbulence Closure

When horizontal turbulent viscosity, AH and diffusivity are included in the momentum and transport equations, they are determined independently using Smagorinsky’s subgrid scale closure formulation (Smagorinsky, 1963):

2

2

2

∂v ∂y

∂u ∂x

∂u ∂y

∂v ∂x

- 1

- 2


AH = Cs∆x∆y

, (2.27)

+

+

+

where Cs is the horizontal mixing constant referred to as the Smagorinsky coefficient, ∆x and ∆y are the grid sizes in x and y directions, respectively. Values of Cs range from 0.1 to 0.2 and has the effect of determining the strength of subgrid scale dissipation (Xiao and Cinnella, 2019).

Canuto and Cheng (1997) recommended a constant value of 0.11. However Canuto and Cheng (1997) also advised against the view that this is a universal value. Instead,Cs reflects a combination of physical processes that differ from flow to flow. That Cs is actually a dynamical variable that adjusts itself to each flow has already been observed. Meyers and Sagaut (2006) derived the exact expression of Cs which demonstrated Cs depends on both the specific flow and on the grid size, indiciating that it should be treated as an uncertain quantity.

##### 2.2. Boundary Conditions and External Forcings

The vertical boundary conditions for the solution of the momentum equations (2.2) and (2.3) are based on the specification of the kinematic shear stresses at the free water surface and at the bed.

Vertical boundary conditions for the turbulent kinetic energy and length scale equations are:

q2 = B21/3 tsx2 +tsy2 , l = 0, at z = 1 (2.28) q2 = B21/3 tbx2 +tby2 , l = 0, at z = 0 (2.29)

Equation (2.29) can become inappropriate under several conditions associated with high near bottom sediment concentrations and/or high frequency surface wave activity.

##### 2.2.1 Bottom Friction

At the bed, the stress components are related to the near bed or bottom layer velocity components by the quadratic resistance formulation:

- τbx
- τby


1 ρw

- u1
- v1


= Cb u21 +v21

(2.30)

###### 16



<<<PAGE 30>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



where,

ρw is the density of water, τbx and τby are the bottom drag due to friction in x and y directions, respectively, and u1 and v1 are the velocities of water for layer 1 in x and y directions, respectively.

where the subscript 1 denotes bottom layer values. Under the assumption that the near bottom velocity profile is logarithmic at any instant of time, the bottom stress coefficient is given by Nezu (1993).

2

κ ln(∆1/2z0)+(Π−1)

Cb =

(2.31)

where, κ is von Karman constant, ∆1 is dimensionless thickness of the bottom layer, zo = zo ∗/H is dimensionless roughness height, and Π is wake strength parameter. Π varies from 0 at low Reynolds numbers to 0.2 with fully turbulent

flow. The Π is assumed to be 0.0.

##### 2.2.2 Vegetation

##### 2.2.2.1 Hydrodynamic Feedback

Drag exerted by plants reduces the mean flow within vegetated regions. Vegetation affects the mean velocity, as well as the turbulence intensity and its diffusion. The conceptual framework for vegetation in EFDC+ is shown in Figure 2.3.

To capture vegetation effects on flow dynamics, an additional drag term Dp is included in the momentum equations (2.2) and (2.3) to represent physical obstructions to flow. The vegetation impacts on the turbulent intensity and the turbulent length scale are represented by adding the additional canopy related turbulence terms in the equations (2.24) and (2.25) as:

∂t(mxmyHq2)+∂x(myHuq2)+∂y(mxHvq2)+∂z(mxmywq2)

Hq3 B1l

Aq H

∂zq2)−2mxmy

=∂z(mxmy

Av H

(∂zu)2 +(∂zv)2 +gKv∂zb+∂pcpDp u2 +v2 3/2 +Qq

+2mxmy

∂t(mxmyHq2l)+∂x(myHuq2l)+∂y(mxHvq2l)+∂z(mxmywq2l)

2

2

Hlq3 lB1

Aql H

l κKz

l κH (1−z)

∂z q2l −mxmyE2

=∂z mxmy

1+E4

+E5

Av H

(∂zu)2 +(∂zv)2 +E3gKv∂zb+E1ηpcpDp u2 +v2 3/2 +Ql

+mxmyl E1

(2.32)

(2.33)

###### 17



<<<PAGE 31>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



Fig. 2.3. Conceptual Framework for Vegetation.

In the equations (2.32) and (2.33), the second term on the last line represents net turbulent energy production by vegetation drag where cp is a production efficiency factor having a value less than one.

##### 2.2.2.2 Drag Coefficient Estimations

Specification of the drag coefficient is critical to describe the canopy behavior. Factors influencing the characterization of drag coefficient include flow conditions, canopy density and the shape of the canopy elements (Ghisalberti & Nepf, 2004). For submerged and suspended canopies, the finite cylinder has an effect on the drag coefficient. On the other hand, in depth-averaged models of emergent canopies, an increase of the drag coefficients with canopy density was reported by Wu et al. and O’Donncha et al.

An expression for the bulk drag coefficient as a function of dimensionless aquaculture canopy density can be obtained by fitting to the experimental data from (Plew, 2011) and (Scott and O’Donncha, 2019) as:

C¯D = 2.0−67ad (2.34) where ad is the dimensionless canopy density.

###### 18



<<<PAGE 32>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



The depth-varying drag coefficients along normalized lengths of the canopy cylinders can be expressed as

CD(ζ) = C¯D 1.2+0.8ζ −0.5ζ2 (2.35) where ζ is distance from the water surface, normalized by the emerged part of the canopy’s length.

##### 2.2.3 Wind Forcings

The influence of wind on hydrodynamics are due to the wind shear stresses exerted on the water surface. At the free surface, the x and y components of the stress are specified by the wind stress:

1 ρw

- τsx
- τsy


ρa ρw

= CD

Ws

- Wsx
- Wsy


(2.36)

Ws = Wsx2 +Wsy2 (2.37) where,

Ws, Wsx and Wsy are the wind velocity and x− and y− components of the wind velocity (m/s) at 10

meters above the water surface, respectively, τsx, and τsy are the surface drag due to wind in x and y directions, respectively, CD is the wind drag coefficient, and ρa and ρw are air and water densities, respectively.

EFDC+ provides four options for calculating wind drag coefficient.

- 1. In case of magnitude sheltering and no directional sheltering, the original wind drag coefficient can be calculated as

CD =







3.83111×10−5W−3

s −0.000308715W−2

s

+0.00116012W−1

s +0.000899602, Ws < 5m/s −5.37642×10−6Ws3+0.000112556Ws2

−0.000721203Ws+0.00259657, 5m/s ≤ Ws < 7m/s −3.99677×10−7Ws2+7.32937×10−5Ws

+0.000726716, Ws ≥ 7m/s

(2.38)

- 2. The second option is a modification of the original EFDC wind drag (Option 1) where the wind speed is calculated as relative to the water velocity.


- Wsx = Wsx −us (2.39)
- Wsy = Wsy −vs (2.40)


where, us and vs are the surface water velocities in x and y directions, respectively.

###### 19



<<<PAGE 33>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



- 3. The third option is from the European Centre for Medium-Range Weather Forecasts (ECMWF) which has determined a wind speed-dependent drag coefficient based on the wave age-dependent surface roughness computed with their coupled atmospheric wave model (Hersbach, 2011). The wind speeddependent formulation is given by

CD = [c1 +c2(Ws)p1]/(Ws)p2 (2.41) where, c1 = 1.03×10−3, c2 = 0.04×10−3, p1 = 1.48, and p2 = 0.21.

- 4. The fourth option is the COARE 3.6 approach based on the bulk momentum and heat flux algorithm described by Fairall et al. (1996), Fairall et al. (2003), and Edson et al. (2013). The approach implemented in EFDC+ is simplified by assuming neutral atmospheric conditions during the simulation. Edson et al. (2013) described the basic equations used under this assumption as follows.

Based on dimensional arguments, the exchange of momentum at the water surface is expected to scale as wind speed squared:

τ = ρaCDUr2 (2.42)

where, τ is the momentum flux or surface stress; ρa is the density of air; CD is the transfer coefficient for momentum (i.e., the drag coefficient); Ur is the wind speed relative to water (i.e., the air-water velocity difference).

Under the assumption of neutral atmospheric conditions, CD is computed as a function of the measurement height (z) and the surface roughness (z0):

CD =

κ ln(zz

0

)

2

(2.43)

The COARE algorithm parameterizes the surface roughness by separating it into two terms:

z0 = zsmooth0 +zrough0 = γ

ν u∗

+α

u2∗ g

(2.44)

where zsmooth0 accounts for “roughness” of the ocean when it is aerodynamically smooth and the surface stress is supported by viscous shear. The second term zrough0 accounts for the actual roughness element driven by the wind stress in the form of surface gravity waves (Fairall et al., 1996). γ is the roughness Reynolds number for smooth flow, which has been determined to be 0.11 from laboratory experiments; ν is the kinematic viscosity; α is the Charnock coefficient; u∗ is the friction velocity.

- 5. There is a new option in EFDC+ version 10.4 that allows a user-defined wind drag relationship in the form of:


where,

CD =

 

C1, Ws ≤ W1 C1 + WC2−C1

2−W1(Ws −W1), W1 < Ws < W2 C2, Ws ≥ W2



(2.45)

###### 20



<<<PAGE 34>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



W1 and W2 are the lower and upper bounds wind velocities of the linear wind drag relationship, respectively, and

C1 and C2 the lower and upper bounds wind drag coefficients of the linear wind drag relationship, respectively.

The values for some linear wind drag relationships can be found in Table 2.2.

Table 2.2. Values of Different Linear Wind Drag Relationships.

Formulation W1(m/s) W2(m/s) C1(10−3) C2(10−3) Francis (1951) 1 25 1.3 32.5 Sheppard (1958) 1 20 0.914 3.08 Wilson (1960) 2.8 20 1.1 2.6 Deacon and Webb (1962) 1 14 1.07 1.98 Heaps (1965) 5 19.2 0.565 2.513 Smith and Banke (1975) 6 21 1.06 2.185 Garratt (1977) 4 21 1.018 2.157 Large and Pond (1981) 10 26 1.14 2.18 Wu (1982) 1 80 0.865 6.0 Anderson (1993) 4.5 21 0.81 1.98 Yelland and Taylor (1996) 6 26 1.02 2.42 Yelland et al. (1998) 6 26 0.926 2.346

##### 2.2.4 Wave Action

The action of short waves on the field velocity of flow in a large water body could be an important aspect that may not be ignored, especially in estuaries and coastal areas. As is commonly known, both longshore currents and undertow are generated by waves. The asymmetry of wave velocity in its orbital plane is one of the causes of mass transport, such as sediment. Waves may be generated either by local wind or by distant storms with longer time periods. In this document, wind-induced wave theory is presented as applied in EFDC+. In EFDC+, there are two options to include wave effects; 1) by a Sverdrup, Munk and Bretschneider (SMB) wind-wave module inside EFDC+, and 2) by an external Simulating WAves Nearshore (SWAN) wave model (SWAN Team, 2019).

In the case of waves, apart from the forces from currents, it is also necessary to add the forces from waves for the whole water column, such as radiation stresses or stresses due to the roller in breaking waves (Mengguo and Chongren, 2003). However, the internal EFDC+ wave module only considers radiation stresses, which is the additional wave-induced momentum exerted on the flow field (Longuet-Higgins and Stewart, 1964):

- 1

- 2


Sxx = ncos2θ +n−

E (2.46) Sxy = Syx = (ncosθsinθ)E (2.47)

- 1

- 2


Syy = nsin2θ +n−

E (2.48)

###### 21



<<<PAGE 35>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



where,

Sxx, Sxy, Syx, Syy are the components of wave radiation stresses, E is the wave energy (kg/s2),

1 8

ρgHS2 (2.49) where,

E =

Hs is the significant wave height (m), θ is the radian measure of the wave direction angle with respect to the x axis (counterclockwise),

and k is the wave number

2π L

(2.50) where

k =

L is the wavelength (m),

and n is the ratio of group velocity to wave celerity

where

Cg C

- 1

- 2


n =

=

2kh sinh(2kh)

1+

h is the water depth (m)

(2.51)

In general, the wavelength L (m) can be computed by solving the non-linear equation for the dispersion relation shown in equation (2.52).

gT2 2π

L =

tanh(kh) (2.52)

This dispersion relation can be solved for the wavelength using approximations or iterative methods, for example, EFDC+ computes wavelength by using an approximate formula (Hunt, 1979):

L ≈ T

1 d

gh, (2.53)

where,

1 (1+0.6522γ +0.4622γ2 +0.0864γ4 +0.0675γ5)

d = γ +

, (2.54) and

h g

γ = ω2

(2.55)

###### 22



<<<PAGE 36>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



where ω is the wave angular frequency (1/s)

2π T

ω =

. (2.56)

The regime of flow is determined through the Wave Reynolds Number (Rw), and the relative bed roughness

- r :


UbA ν

A ks

Rw =

(2.57)

, r =

in which A is the semi-orbital excursion, ks is the Nikuradse equivalent sand grain roughness, and Ub is the wave maximum orbital velocity near the bed.

Hs 2sinh(kh)

A =

ωHs 2sinh(kh)

Ub = Aω =

(2.58)

(2.59)

The bottom friction, the bed forms (such as ripples) and the characteristics of bed materials are strongly interdependent in case of wave actions. The friction coefficient due to waves according to Swart (1974) is given in equation (2.60).

fw =

e(5.21r−0.19−6.0) r > 1.57 0.3r r = 1.57

(2.60)

##### 2.2.5 Local Wind-Generated Waves

The force applied by wind constitutes an important mechanism which drives the hydrodynamic processes as well as sediment transport in lakes, estuaries, and coastal areas. Wind effects do not only induce the flow current through the vertical boundary conditions at water surface, but also generate surface waves with wave height of several meters. Consequently, the calculation of the total bed shear stress should take the wave factor into account. The conceptual framework for wind-generated waves in EFDC+ is shown in Figure 2.4.

Waves with periods of 3 to 25 seconds are primarily caused by winds. Therefore, wind-generated waves play an important role in hydrodynamic modeling. The advantage of this wind-wave sub-model is that it can be easily incorporated into the source code of a hydrodynamic model instead of running a separate wave model. This means that the changes in hydrodynamic parameters are immediately updated in the wave calculations. Additionally, the calculation time is reduced compared to other wave models.

This section presents the details of the theoretical basis and tests of the wind wave module that is incorporated into EFDC+. The mathematical formulae are empirical equations called the SMB (Sverdrup, Munk and Bretschneider) model (Ji, 2008).

The basic assumptions of the SMB model for wind-generated waves are: a) the duration of wind blowing along one direction is long enough to attain the equilibrium condition, b) the wind speed and water depth are spatially uniform over the fetch. The main wave parameters can be determined including wave height, wave direction and wave period, c) the wave direction is the same as the wind direction, and d) the effects of refraction, diffraction and reflection are not considered. Wave height and period can be defined in the SMB

###### 23



<<<PAGE 37>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



Fig. 2.4. Conceptual Framework for Wind-Generated Waves.

model as:

where

where,

Ws2 g

Hs = 0.283α

tanh

0.0125 α

Ws g

Tp = 7.54β

tanh

0.077 β

α = tanh 0.53

gH Ws2

β = tanh 0.833

gH Ws2

gF Ws2

gF Ws2

0.42

0.25

(2.61)

(2.62)

0.75

, and (2.63)

0.375

(2.64)

Hs is the wave height (m), Tp is the wave period (s), H is the water depth (m), Ws is the wind velocity (m/s), and F is the fetch length (m) from the land boundary to the cell in the upwind direction and is calculated

for 16 directions.

###### 24



<<<PAGE 38>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



##### 2.2.6 Harmonic Forcings

The open boundary conditions in EFDC+ support a combination of forcings defined as a time series and harmonic forcings. This allows the user to model the situations in estuaries or coastal areas where the influences of tides and river flows or storm surges may occur.

The harmonic representation of a time series ζ(t) can be approximated as a combination of sine and cosine functions:

where,

ζ(t) = ζ0(t)+a0 +

N

### ∑

[akcos(ωkt) +bksin(ωkt)] (2.65)

k=1

t is the time (s), ζ0(t) is the residual signal other than the periodic components (m), a0 is the mean value of the periodic components (m), N is the number of the harmonic constituents, ak, bk are the harmonic constant of the constituent k (m), and ωk is the angular speed of constituent k (radians/s).

The angular speed of the constituent k can be calculated as

2π Tk

ωk =

where, Tk is the period constituent k (s). Equation (2.65) can be also rewritten in another common form as

(2.66)

ζ(t) = ζ0(t)+a0 +

N

### ∑

Akcos(ωkt −φk) (2.67)

k=1

where, Ak is the amplitude of the harmonic constituent k (m):

Ak = a2k +b2k (2.68) and φk is the phase lag the harmonic constituent k (radians):

fk = arctan

bk ak

(2.69)

###### 25



<<<PAGE 39>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



##### 2.2.7 Hydraulic Structures

Hydraulic structures can be modeled in EFDC+ by rating curves or hydraulic equations. A rating curve is a lookup table which presents a relationship between the flow rate through the structure and the water heads. Depending on the actual water heads of the structure at a certain time step, the flow rate is determined using the lookup table. EFDC+ allows a variety of rating curves in which the flow discharge can be determined from; a) upstream water depth, b) the head difference (between upstream and downstream), c) the head difference and flow accelerations, d) the upstream and downstream water surface elevations, e) upstream water depth for a low chord structure, and f) head difference for a low chord structure.

The last two types of rating curves use low chord structures such as bridges. With the low chord structures, when flows are below the deck, they may be bi-directional, i.e., water can flow from upstream toward downstream or vice-versa. However, once the bridge is overtopped, flows only go from upstream to downstream.

##### 2.2.7.1 Rating Curves

If the flow through a structure is uni-directional, i.e., the flow direction is from upstream to downstream of the structures only. The rating curve is a lookup table which composes of a single column for water head and a corresponding single column for flow rate.

If the flow through a structure is bi-directional, the rating curve is a two-dimensional lookup table where the flow rates can be determined based on both upstream and downstream water surface elevations.

Beside using lookup tables, EFDC+ can also simulate internally different types of hydraulic structures. This allows the user to model hydraulic structures rapidly and with ease in EFDC+. The built-in modeling codes for hydraulic structures includes culverts, weirs, sluice gates, and orifices.

##### 2.2.7.2 Culverts

Flow rate through a culvert or sluice gate is calculated in EFDC+ based on the water levels at both sides of the structure at its configuration. In a tidal region, the water levels on two sides of the structure are constantly changing, which can result in bi-directional flows. The characteristics of flow through a culvert are complicated and are determined by the inlet geometry, slope, shape, size, roughness, approach, and headwater and tailwater conditions. Dill (2011) described six different types of culvert flows based on the location of the control section within the culvert and the relative elevations of the headwater, tailwater, and culvert invert and crown elevations. The discharge through a culvert can be expressed as:

Q = AV = AC√RS = K√S (2.70)

where Q is the flow discharge (m3/s), A is the cross-sectional flow area (m2), R is the hydraulic radius (m), S is the culvert slope (fraction), K is the conveyance (m3/s), and C is the Ch´ezy coefficient (m0.5/s) which can be calculated by using the Manning’s formula

1 n

R16 (2.71)

C =

where, n is Manning’s roughness coefficient. Four distinct conditions arise depending on elevation of the tailwater and headwater compared to the height of the culvert. The handling of these conditions are described in case “a” through “d” below:

###### 26



<<<PAGE 40>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



- a) If the tailwater is greater than the culvert height or the headwater is greater than 1.5 times the culvert height, the culvert outlet is submerged, and the culvert is assumed to flow full. The slope is estimated as the difference in headwater and tailwater elevation divided by the culvert length, L (m), the conveyance is determined for the full culvert, and discharge is calculated by equation (2.70).
- b) If both the inlet and outlet are not submerged, the critical depth (yc) is computed, assuming free flow through the culvert inlet. In this case, it is assumed that the approach velocity is negligible so that total energy at the culvert inlet is equal to the headwater. Thus,

HHW = yc +

Vc2 2g

(2.72) where,

HHW is the headwater (m), Vc is the critical velocity (m/s), yc is the critical depth (m), and g is acceleration due to gravity.

In the case of critical flow through the culvert:

Vc2 2g

=

D 2

(2.73) where D is the hydraulic depth (m):

D =

A T

(2.74)

and T is the flow top width (m). Combining equations (2.72) and (2.73) yields an expression for the critical depth,

yc = HHW −

D 2

(2.75) where HTW is the tailwater (m).

Once the critical depth is determined, the critical velocity Vc, critical discharge Qcr, and critical slope Scr are also calculated. The critical discharge represents the maximum possible flow through the culvert for the given headwater as shown in equation (2.76)

Qcr = VcA (2.76)

If the culvert slope is greater than the critical slope, the culvert can convey more flow than the inlet will allow. As such, the inlet controls the flow and the discharge is assumed to be equal to the critical discharge Qcr calculated as equation (2.76).

- c) If the culvert slope is less than the critical slope, the control section may be at the culvert outlet or downstream of the culvert. The critical depth is then compared to the tailwater, and if the tailwater is greater than the critical depth, the tailwater elevation is used to determine the flow area and hydraulic radius, and the flow through the culvert is calculated using the equation (2.70).


###### 27



<<<PAGE 41>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



- d) If the tailwater depth is less than the critical depth, but the slope is less than the critical slope, it is assumed that uniform flow will occur within the culvert. In this case potential energy is balanced by head loss due to friction in the culvert and conservation of energy between the control section and inlet can be expressed as;


V2 2g

HHW = yn +

(2.77)

where, yn is the normal depth (m) in the culvert and V is the average velocity at the control section. It is also assumed that the approach velocity is negligible, and the slope is small such that the normal depth is approximately equal to the vertical depth.

Equation (2.70) can be re-written as an expression of the velocity head at the control section as;

√S (2.78) Combining equations (2.77) and (2.78) yields an equation for the normal depth

1 n

R23

V =

- 1

- 2g


yn = HHW −

1 n2

R43S (2.79)

Because R is a function of depth, an adaptive procedure is employed to determine the normal depth. In culverts that experience bi-directional flow, the slope may be adverse or zero. In either case, the assumption of uniform flow is problematic because the water surface slope cannot be equal to the culvert slope. In this case, the water surface slope, as determined from the difference in headwater and tailwater elevations, is used in the equation (2.79).

- 2.2.7.3 Weirs A general formula for free flow through a weir can be expressed as

Q = CdW 2gHHW3 (2.80)

where, W is the width of weir (m) and Cd is weir discharge coefficient. This coefficient depends on the type of weir (broad crested or sharp-/narrow-crested, ogee), shape of opening (rectangular, triangular, trapezoidal), and other weir parameters.

For submerged flow through a weir, an adjustment factor is applied to equation (2.80) to account for the submergence and is given in equation (2.81) (Villemonte, 1947)

Q = 1−

HTW HHW

0.385

CdW 2gHHW3 (2.81)

- 2.2.7.4 Sluice Gates


Flow through a sluice gate can be characterized by two basic parameters: the tranquility of the flow (i.e., subcritical or supercritical flow) and the water depth (i.e., gate is submerged or not). For super-critical weir flow the following equation is used

###### 28



<<<PAGE 42>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



3

2 3

(2.82) and for sub-critical weir flow

Q = C1W g

HHW

Q = C2WHTW 2g(HHW −HTW) (2.83) where,

C1 is the supercritical discharge coefficient, C2 is the subcritical discharge coefficient, HHW is the headwater (m), HTW is the tailwater (m), W is the width of the gate (m), and g is acceleration due to gravity.

When the water surface is determined to be below the top of the gate, the gate is modeled as a broad crested weir and equation (2.80) is used. When the gate is submerged, the appropriate equation for either free sluice flow (supercritical) or submerged orifice flow (subcritical) is applied. To determine the flow through the sluice gate at a given model time step, the headwater is compared to the tailwater.

For free sluice flow the equation (2.84) is used:

Q = C3A 2gHHW (2.84) Similarly, for submerged orifice flow equation (2.85) is used.

Q = C4A 2g(HHW −HTW) (2.85) where,

C3 is the discharge coefficient for free sluice flow, C4 is the discharge coefficient for submerged orifice flow, and A is the gate opening (m2).

If the ratio of tailwater to headwater is less than 0.64, equation (2.82) for supercritical flow is applied. If the ratio of tailwater to headwater is greater than 0.68, equation (2.83) for subcritical flow is applied. This is either a free sluice for supercritical flow, or a submerged orifice for subcritical flow. In cases when the tailwater to headwater ratio is between 0.64 and 0.68 both discharges are computed and a weighted average of the two is used.

###### 29



<<<PAGE 43>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



##### 2.2.7.5 Orifices

If the headwater is lower than the opening of an orifice, the flow through the orifice is treated as weir flow, and the equation (2.80) is used. If the tailwater is higher than the opening of an orifice, then equation (2.85) submerged flow through the orifice is applied. If the headwater is higher than the opening of an orifice but the tailwater is lower than the opening of an orifice, the free jet flow through the orifice is calculated as

Q = C2A 2g(HHW +0.5B) (2.86)

where, B is the height of the orifice opening (m), and HHW is calculated based on the center line of the orifice.

##### 2.2.7.6 Masks

In EFDC+, “masks” are implemented as barriers across cell flow faces in order to fully or partially block flow between cells in the model domain. At U or V face of a cell with mask, a “Draft Depth” and a “Bottom Sill Height” are defined as the thickness of a floating or fixed object at the water surface, and the thickness of a structure at the bed, respectively. If the space between “Draft” and “Bottom Sill” is equal to 0, the cell face is fully blocked, otherwise it is partially blocked.

The blocking mask is useful to simulate structural obstacles such as breakwaters and causeways locally aligning with the model grid, but have widths much less than the cell size or grid spacing in one direction.

##### 2.2.8 Propeller Wash

The EFDC+ propeller wash module simulates sediment resuspension and transport processes due to ship traffic, with a fully coupled representation of hydrodynamics, sediment transport, and propeller wash effects. Using ship traffic data, this module computes each ship’s propeller wash effects (e.g., flow velocity, shear stress, sediment erosion rate) based on an independent sub-grid, representing a propeller wash jet area behind the ship. The momentum flux induced by the propeller rotation is also calculated for the ship locations during the simulation. The propeller wash results are then linked to model grid cells for every time step of the hydrodynamics and sediment transport computation in the model simulation. The details for the theoretical basis and algorithmic structure of the EFDC+ propeller wash module are described in DSI (2021).

Propeller wash may significantly impact the hydrodynamics and transport processes of constituents in the water column, especially in areas of substantial ship traffic. The EFDC+ propeller wash module has the option to add the momentum associated with the propeller efflux velocity to a 3D hydrodynamic flow field as a source term. If this option is activated, the EFDC+ hydrodynamic model includes the propeller wash momentum effects when it computes the 3D hydrodynamic flow field for the next time step. The resulting flow velocities then impact the movement of the suspended sediments and other constituents in the water layers of the EFDC+ model grid.

Figure 2.5(a) shows a two-dimensional (2D) conceptual diagram for the velocity vector components of a ship passing through an EFDC+ model grid cell. Based on the angle between the ship’s heading and the EFDC+ model grid rotation, the EFDC+ propeller wash module vectorially splits the propeller efflux velocityV0 into the computational grid space (in i and j directions) as:

Vi = V0 ×cos(θ3 −θ1) (2.87)

###### 30



<<<PAGE 44>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



where,

Vj = V0 ×sin(θ3 −θ1) (2.88)

π 2

θ3 = θ2 −

(2.89)

V0 is the propeller efflux velocity from the propeller plane (m/s) Vi is the grid-oriented efflux velocity component in the i direction (m/s) Vj is the grid-oriented efflux velocity component in the j direction (m/s)

- θ1 is the EFDC+ model grid cell rotation (radian)
- θ2 is the ship heading in compass orientation (radian)
- θ3 is the propeller wash efflux angle (radian)


Given the velocity components Vi and Vj, the EFDC+ propeller wash module computes the specific momentum flux due to propeller wash for each direction as follows:

where,

- Mpi = |Vi ×AP|×Vi × fp (2.90)
- Mpj = |Vj ×AP|×Vj × fp (2.91)


- MPi is the specific momentum flux due to propeller wash in the i direction (m4/s2)
- MPj is the specific momentum flux due to propeller wash in the j direction (m4/s2) AP is the area of propeller wash face in the efflux zone (m2) fp is the momentum effect factor (dimensionless)


The EFDC+ propeller wash module then incorporates the resultant momentum flux MPi and MPj into the momentum equations of EFDC+ hydrodynamic model computations as a source term. The EFDC+ propeller wash module also applies a factor fp to adjust the propeller wash-induced momentum flux to account for losses and turbulence that are not directly simulated. This factor is a user-defined input parameter of the EFDC+ propeller wash module, which can range between 0.3 and 0.7 according to observations from Kee et al. (2006) and Hamill and Kee (2016) that the actual cross-sectional area of the efflux velocity plane can be smaller than the propeller face area Ap.

Vertically, the EFDC+ propeller wash module distributes the propeller wash-induced momentum effects proportionately across the EFDC+ model grid water layers that the propeller intersects. The vertical splitting process for the momentum change rates MPi and MPj is implemented with relative to the ship draft, propeller diameter, water depth, and the number of the model grid water layers where the propeller is located. Figure 2.5(b) shows an example of vertical fractions (%) for the propeller wash-induced momentum change rates over the EFDC+ model grid water layers.

###### 31



<<<PAGE 45>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



Fig. 2.5. Diagrams for propeller wash-induced momentum (a) coupling with an EFDC+ model grid cell and (b) splitting over vertical water layers.

##### 2.3. Numerical Solution for the Equations of Motion

The equations of motion, shown previously in equations (2.2) and (2.3) are solved in a region subdivided into six faced cells. The projection of the vertical cell boundaries to a horizontal plane forms a curvilinear, orthogonal grid in the orthogonal coordinate system (x,y). In a vertical (x,z) or (y,z) plane, the cells bounded by the same constant z surfaces are referred to as cell layers. The equations are solved using a combination of finite volume and finite difference techniques, with the variable locations shown in Figure 2.6.

The staggered grid location of variables is often referred to as the Arakawa C grid (Arakawa and Lamb, 1977) or the MAC grid (Peyret and Taylor, 1983). To proceed, it is convenient to modify equations (2.2) and (2.3) by eliminating the vertical pressure gradients using equation (2.4). After some manipulation, the horizontal momentum equations are given in the equations (2.92) and (2.93).

∂ ∂x

∂ ∂y

∂ ∂z

∂ ∂t

(mxmyHu)+

(myHuu)+

(mxHvu)+

∂my ∂x −u

∂mx ∂y

− v

Hv−mxmy fHv

∂ζ ∂x

∂h ∂x −myHgbz

∂ p ∂x −myHg

+myHgb

=−myH

(mxmywu)

∂H ∂x

∂ ∂z

+

∂u ∂z

mxmyAv H

+Su

(2.92)

###### 32



<<<PAGE 46>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



Fig. 2.6. Free Surface Displacement Centered Horizontal Grid.

∂ ∂t

∂ ∂x

∂ ∂y

∂ ∂z

(mxmyHv)+

(myHuv)+

(mxHvv)+

∂my ∂x −u

∂mx ∂y

+ v

Hu+mxmy fHu

∂ p ∂y −mxHg

∂ζ ∂y

∂h ∂y −mxHgbz

=−mxH

+mxHgb

(mxmywv)

∂H ∂y

∂ ∂z

+

∂v ∂z

mxmyAv H

+Sv

(2.93)

First, the vertical discretization of equations (2.92) and (2.93) is performed. The equations are integrated with respect to z over a cell layer assuming that vertically defined variables (at the cell or layer centers) are constant. Additionally, these variables must be defined vertically at the cell layer interfaces or boundaries. Using the notation for mass fluxes,

Pk = myHuk,Qk = mxHvk (2.94) equations (2.92) and (2.93) are redefined as;

∂ ∂x

∂ ∂y

∂ ∂t

(mxPk∆k)+

(Pkuk∆k)+

(Qkuk∆k)+m (wu)k −(wu)k−1

∂my ∂x −uk

∂mx ∂y

Hvk∆k −my fQk∆k

− vk

∂ ∂x

∂ζ ∂x

∂h ∂x

- 1

- 2


myH∆k

(pk + pk−1)−myH∆kg

+myH∆kgbk

=−

∂H ∂x

−0.5myH∆kgbk(zk +zk−1)

+m (τxz)k −(τxz)k−1 +(Su∆)k

(2.95)

###### 33



<<<PAGE 47>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



∂ ∂t

∂ ∂x

∂ ∂y

(myQk∆k)+

(Pkvk∆k)+

(Qkvk∆k)

∂my ∂x −uk

∂mx ∂y

Huk∆k +mx fPk∆k

+m (wv)k −(wv)k−1 + vk

(2.96)

∂ ∂y

∂ζ ∂y

∂h ∂y

1 2

mxH∆k

(pk + pk−1)−mxH∆kg

+mxH∆kgbk

=−

∂H ∂y

+m (tyz)k −m(tyz)k−1 +(Sv∆)k

−0.5mxH∆kgbk(zk +zk−1)

where, ∆k is the vertical cell or layer thickness, and the turbulent shear stresses at the cell layer interfaces are defined by:

(τxz)k =

2 H

uk+1 −uk ∆k+1 +∆k

(Av)k

(2.97)

(tyz)k =

2 H

vk+1 −vk ∆k+1 +∆k

(Av)k

(2.98)

If there are K cells in the z direction, the hydrostatic equation can be integrated from a cell layer interface to the surface to give:

pk = gH

K

### ∑

bj∆j−bk∆k + ps (2.99)

j=k

where, ps is the physical pressure at the free surface or under the rigid lid divided by the reference density. The continuity equation (2.5) is also integrated with respect to z over a cell or layer to give:

∂ ∂t

(mζ∆k)+

∂ ∂x

(Pk∆k)+

∂ ∂y

(Qk∆k)+m(wk +wk−1) = Sh (2.100)

The numerical solution of the vertically discrete momentum equations (2.92) and (2.93) proceeds by splitting the external depth-integrated mode (associated with external long surface gravity waves) from the internal mode (associated with vertical current structure).

The external mode equations are obtained by summing equations (2.92) and (2.93) over K cells or layers in the vertical utilizing equation (2.99), and are given by:

K

∂my ∂x −uk

∂ ∂x

∂ ∂y

∂ ∂t

### ∑

mxPˆ +

(Pkuk∆k)+

(Qkuk∆k)− vk

k=1

K

∂ζ ∂x −myH

∂ ps ∂x

∂h ∂x −myHg

- 1

- 2


### ∑

+myHgbˆ

βk∆k +

=−myHg

k=1

K

∂ ∂x

### ∑

βk∆k +m[(τxz)K −(τxz)0]+Sˆu

−mygH2

k=1

∂mx ∂y

Hvk∆k −my fQk∆k

(zk +zk−1)bk∆k

∂H ∂x

(2.101)

###### 34



<<<PAGE 48>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



K

∂my ∂x −uk

∂ ∂x

∂ ∂t

∂ ∂y

### ∑

mxQˆ +

(Pkvk∆k)+

(Qkvk∆k)− vk

k=1

K

∂ ps ∂y

∂h ∂y −mxHg

∂ζ ∂y −mxH

- 1

- 2


### ∑

+mxHgbˆ

βk∆k +

=−mxHg

k=1

K

∂ ∂y

### ∑

βk∆k +m (τyz)K −(τyz)0 +Sˆu

−mxgH2

k=1

∂mx ∂y

Huk∆k −mx fPk∆k

(zk +zk−1)bk∆k

∂H ∂y

(2.102)

∂ ∂t

∂ ∂x

(mζ)+

∂ ∂y

Q¯ = Sh (2.103)

P¯ +

where the over bar indicates an average over the depth as reiterated in equation (2.104). Additionally, equation (2.105) is introduced to simplify equations (2.101) and (2.102).

Pˆ = myHuˆ,Qˆ = mxHvˆ (2.104)

K

### ∑

βk =

bj∆j −

j=k

- 1

- 2


bk∆k (2.105)

The depth integrated continuity equation, equation (2.103), follows from equation (2.6) and provides the continuity constraint for the external mode. Consistent with the form of equation (2.103) the external mode variables are chosen to be the free surface displacement, ζ and the volumetric transports, P = myHu and Q = mxHv. Details of the solution of the external mode equations (2.101) to (2.103) are presented in Section 2.4. Several formulations are possible for the internal mode equations. Equations (2.92) and (2.93) have K degrees of freedom for each of the horizontal velocity components. However, the summation of these equations over K cells or layers in the vertical to form the external mode equations (2.101) and (2.102) effectively removes a degree of freedom since the constraints

K

### ∑

uk∆k = uˆ, and (2.106)

k=1

K

### ∑

vk∆k = vˆ (2.107)

k=1

must be satisfied. One approach to the internal mode is to solve equations (2.92) and (2.93) using the free surface slopes, or the surface pressure gradients in the rigid lid case, from the external solution and distribute the error such that equations (2.106) and (2.107) are satisfied. A second approach is to form equations for the deviations of the velocity components from their vertical means by subtracting the external equations (2.101) and (2.102) from the layer integrated equations (2.92) and (2.93). However, it will still be necessary to satisfy the constraints (2.106) and (2.107). The approach proposed herein is to reduce the systems of

###### 35



<<<PAGE 49>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



K layer averaged equations (2.95) and (2.96) to systems of K −1 equations and use equations (2.106) and (2.107) to provide the Kth equation consistent with the actual degrees of freedom.

The internal mode equations are formed by first dividing equations (2.95) and (2.96) by the cell layer thickness (∆k). Next, the equations for cell layer k is subtracted from the equations for cell layer k + 1. The resulting equation from these two operations is divided by the average thickness (∆k+1,k) of the two cell layers resulting in:

∂ ∂t

∂ ∂x

∂ ∂y

Pk+1 −Pk ∆k+1,k

Pk+1uk+1 −Pkuk ∆k+1,k

Qk+1uk+1 −Qkuk ∆k+1,k

mx

+

+

(wu)k −(wu)k−1

(wu)k+1 −(wu)k

m ∆k+1,k

Qk+1 −Qk ∆k+1,k −

∆k −my f

∆k+1 −

+

∂my ∂x −uk+1

∂my ∂x −uk

∂mx ∂y

∂mx ∂y

1 ∆k+1,k

vk+1

Hvk+1 − vk

Hvk

myH2 ∆k+1,k

∂h ∂x −zk

∂H ∂x

∂bk+1 ∂x

∂bk ∂x

- 1

- 2


bk+1 −bk ∆k+1,k

g ∆k+1

+∆k

g

= myH

+

(τxz)k −(τxz)k−1 ∆k

(τxz)k+1 −(τxz)k

(Su)k+1 −(Su)k ∆k+1,k

m ∆k+1,k

∆k+1 −

+

+

(2.108)

∂ ∂x

∂ ∂y

∂ ∂t

Qk+1 −Qk ∆k+1,k

Pk+1vk+1 −Pkvk ∆k+1,k

Qk+1vk+1 −Qkvk ∆k+1,k

my

+

+

(wv)k −(wv)k−1 ∆k

(wv)k+1 −(wv)k

m ∆k+1,k

Pk+1 −Pk ∆k+1,k

+mx f

∆k+1 −

+

∂my ∂x −uk+1

∂my ∂x −uk

∂mx ∂y

∂mx ∂y

1 ∆k+1,k

vk+1

Huk+1 − vk

Huk

+

mxH2 ∆k+1,k

∂h ∂y −zk

∂H ∂y

∂bk+1 ∂y

∂bk ∂y

bk+1 −bk ∆k+1,k

- 1

- 2


g ∆k+1

+∆k

=mxH

g

+

(τyz)k −(τyz)k−1 ∆k

(τyz)k+1 −(τyz)k

(Sv)k+1 −(Sv)k ∆k+1,k

m ∆k+1,k

∆k+1 −

+

+

(2.109)

∆k+1,k =

- 1

- 2


(∆k+1 +∆k) (2.110)

Inspection of equations (2.108) and (2.109) reveals that they could have also been obtained by differentiating the horizontal momentum equations (2.92) and (2.93) with respect to z and introducing a finite difference discretion in z. Using equations (2.97) and (2.98) to relate the shear stresses to the velocity differences across the interior interfaces suggests that the equations (2.108) and (2.109) be interpreted as a system of K −1 equations for either the K −1 interfacial velocity differences or the K −1 interior interfacial shear stresses. Details of the solution of the internal mode equations (2.108) and (2.109) is presented in Section 2.5.

The solution of the vertical velocity, w, employs the continuity equations. Dividing equation (2.100) by ∆k, and subtracting equation (2.102) yields

∆k m

wk = wk−1 −

∂ ∂x

∂ ∂y

Pk −Pˆ +

Qk −Qˆ . (2.111)

###### 36



<<<PAGE 50>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



Since wo = 0, the solution proceeds from the first cell layer to the surface. Provided the constraints (equations (2.106) and (2.107)) are satisfied, the surface velocity at k = K will be zero and satisfy the boundary condition.

##### 2.4. Computational Aspects of the Three Time Level External Mode Solution

The formulation of a computational algorithm for the numerical solution of the external mode equations (2.101) to (2.103) begins by introducing modified variables and reorganizing the equations to give:

- ∂Pˆ

∂t

= −

my mx

Hg

∂ζ ∂x −

my mx

H

∂ ps ∂x

+

my mx

Hg b ˆ

∂h ∂x −Bˆ

∂H ∂x −H

∂βˆ ∂x

−

1 mx

K

∑

k=1

∆k

∂ ∂x

(Pkuk)+

∂ ∂y

(Qkuk) +

1 mx

K

∑

k=1

∆k vk

∂my ∂x −uk

∂mx ∂y

Hvk +my fQk

+

1 mx

K

∑

k=1

∂ ∂x

my mx

HAHk∆k

∂uk ∂x

+

∂ ∂y

mx my

HAHk∆k

∂uk ∂y

+my(τxz)K −my(τxz)0 +

1 mx

Sˆu

(2.112)

- ∂Qˆ


∂ζ ∂y −

mx my

mx my

Hg

= −

∂t

∂ ps ∂y

H

mx my

Hg b ˆ

+

K

∂ ∂x

∂ ∂y

1 my

1 my

### ∑

(Pkvk)+

(Qkvk) +

−

k

k=1

K

∂ ∂x

∂vk ∂x

∂ ∂y

my mx

1 my

### ∑

HAHk∆k

+

+

k=1

1 my

Sˆv

+mx(τyz)K −mx(τyz)0 +

∂βˆ ∂y

∂h ∂y −Bˆ

∂H ∂y −H

K

∂my ∂x −uk

∂mx ∂y

### ∑

∆k vk

k=1

∂vk ∂y

mx my

HAHk∆k

Huk +mx fPk

(2.113)

∂Qˆ ∂y

∂Pˆ ∂x

∂ζ ∂t

1 m

= Sh (2.114) where,

+

+

K

### ∑

βˆ =

βk∆k, and (2.115)

k=1

K

### ∑

βˆ =

k=1

βk∆k +

- 1

- 2


(zk +zk−1)bk∆k . (2.116)

Equations (2.112) and (2.113) now equate the time rate of change of the external or depth integrated volumetric transports to the pressure gradients associated with the free surface slope, atmospheric pressure and

###### 37



<<<PAGE 51>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



buoyancy, the advective accelerations, the Coriolis and curvature accelerations, the free surface and bottom tangential stresses, and the general source, sink terms. The staggered location of variables on the computational grid (Figure 2.6) allows most horizontal spatial derivatives in equations (2.112) to (2.114) to be represented by second order accurate central differences and results in conservation of volume, mass, momentum and energy in the limit of exact integration of the equations in time (Haltiner and Williams, 1980; Simons et al., 1973). When a variable is not located at a point required for implementation of central difference operators, averaging in either or both spatial directions is appropriate. The use of the spatial averaging scheme of Arakawa and Lamb (1977) to represent the Coriolis and curvature accelerations also guarantees energy conservation.

Following the introduction of discrete finite difference and averaging representations in space, equations (2.112) to (2.114), for a horizontal grid of L cells, may be viewed as a system of 3L ordinary differential equations in time for the volumetric transport and the free surface displacement. The numerous techniques available to solve these equations generally fall within the categories of explicit and semi-implicit. The most frequently used explicit scheme is the three-time level leapfrog scheme where the time derivatives are approximated between the time levels n+1 and n−1, and the remaining terms are evaluated at time level n. Although computationally simple to implement, the maximum time step is restricted by the CourantFredrick-Levy condition based on the gravity wave phase speed. An alternate approach allowing larger time steps is the semi-implicit three-time level scheme (Madala and Piacseki, 1977), which when implemented for equations (2.112) to (2.114) is

u

u

my mx

my mx

- Pˆn+1 = Pˆn−1 −∆t


gdxu ζn+1 +ζn−1 −2∆t

dxups

H

H

u

my mx

g b ˆudxuh−BˆudxuH −Hudxuβˆ

+2∆t

H

u K

1 mx

### ∑

∆k dxu(Pkuk)+dyu(Qkuk)

−2∆t

k=1

u K

u

∂my ∂x −uk

∂mx ∂y

1 mx

### ∑

+2∆t

∆k vk

Hvk +my fQk

k=1

u

+2∆tmuy tn−1

xz K − tn−1

xz 0

u K

∂ ∂x

∂ ∂y

1 mx

### ∑

myHtn−1

mxHtn−1

∆k

+2∆t

xx +

xy

k=1

u

∂ ∂y

∂ ∂x

mxHtn−1

myHtn−1

xy −

+

yy

k

(2.117)

###### 38



<<<PAGE 52>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



v

mx my

mx my

- Qˆn+1 = Qˆn−1 −∆t


gδyu ζn+1 +ζn−1 −2∆t

H

H

v

mx my

g b ˆvdyvh−BˆvδyvH −Hvδyvβˆ

+2∆t

H

u K

1 my

### ∑

∆k dxv(Pkvk)+dyv(Qkvk)

−2∆t

k=1

v K

∂my ∂x −uk

∂mx ∂y

1 my

### ∑

∆k vk

−2∆t

Huk +mx fPk

k=1

v

+2∆tmvx τn−1

yz K − τn−1

yz 0

v K

∂ ∂y

∂ ∂x

1 my

### ∑

myHtn−1

mxHtn−1

∆k

+2∆t

yx +

yy

k=1

v

∂ ∂y

∂ ∂x

mxHtn−1

myHtn−1

xx −

yx

k

v

δyups

v

(2.118)

ζn+1 −ζn−1 +∆t

1 m

ζ

δxζ P ˆn+1 +Pˆn−1 +δyζ Q ˆn+1 +Qˆn−1 = Sh∆t (2.119)

where, ∆t indicates the time step. All terms in equations (2.117) to (2.119) are understood to be evaluated at the center time level n except those evaluated at the forward and backward time levels, n+1 and n−1, which are denoted by superscripts. The u, v, and ζ superscripts indicate that a variable is evaluated, or that a spatial derivative is centered, at the corresponding spatial point.

The subscript of the spatial central difference operator δ indicates direction. The grid cells are presumed to be bounded in the horizontal by lines of constant integer values of the dimensionless orthogonal coordinates x and y, resulting in the central spatial differences having the forms given in equations (2.120) and (2.121).

- δx φi,j,k =

1 ∆x

φi+1

2,j,k −φi−1

2,j,k (2.120)

- δy φi,j,k =


1 ∆y

φi,j+1

2,k −φi,j−1

2,k (2.121)

Application of these finite difference operators to the advective accelerations is illustrated by,

1 ∆x

δxu Pi,j,kui,j,k =

2,j,kui+1

2,j,k −Pi−1

2,j,kui−1

2,j,k , (2.122)

Pi+1

where the constant y dependence of the variables is implied. Since the u type variables are located at integer values of x, averaging is necessary to obtain values at half intervals. Averaging both the transport and the velocity yields,

1 ∆x

δxu Pi,j,kui,j,k =

ui+1,j,k +ui,j,k 2 −

Pi,j,k +Pi−1,j,k 2

ui,j,k +ui−1,j,k 2

Pi+1,j,k +Pi,j,k 2

, (2.123)

###### 39



<<<PAGE 53>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



which is consistent with a central difference approximation of the non-conservative form of this portion of the advective acceleration. Averaging the transport and allowing the velocity to be advected from the upwind direction gives,

δxu Pi,j,kui,j,k = ∆1x max Pi+1,j,k2+Pi,j,k,0 un−1

i,j,k −max Pi,j,k+Pi−1,j,k

2 ,0 un−1

i−1,j,k

(2.124)

+∆1x min Pi+1,j,k2+Pi,j,k,0 un−1

i+1,j,k −min Pi,j,k+Pi−1,j,k

2 ,0 un−1

i,j,k

which is consistent with an upwind or backward difference approximation of the non-conservative form of this portion of the advective acceleration. In equation (2.124), the transport is still at time level n, while the velocity is at time level n−1, for both stability and accuracy (Smolarkiewicz and Clark, 1986). The preference for the use of equation (2.123) or equation (2.124) generally depends upon the physical situation being simulated. The central difference form introduces no numerical diffusion, but may produce solution fields which exhibit cell to cell spatial oscillations. These oscillations can be eliminated by the addition of horizontal diffusion terms to the momentum equations. Specification of the horizontal diffusivity allows the degree of spatial smoothing to be controlled. The upwind difference form introduces numerical diffusion and does not produce spatial oscillations in the solution field. The Coriolis and curvature terms in equations (2.117) and (2.118) are discretized using an energy conserving spatial averaging and differencing (Arakawa and Lamb, 1977; Haltiner and Williams, 1980). For example, the Coriolis and curvature term in equation (2.117) is given by:

∂my ∂x −uk

∂mx ∂y

my fQk + vk

Hvk

u

- 1

- 2


=

(my)i+1,j −(my)i,j ∆x

Rζi+1

vζi+1

2,j = (mf)i+1

2,j +

(RH)ζi+1

2,jvζi+1

2,j,k +(RH)ζi−1

2,jvζi−1

2,j,k (2.125)

(mx)i+1

###### 2,j+12 −(mx)i+1

2,j−21

2,j,k −

∆y

uζi+1

2,j,k (2.126)

- 1

- 2


vζi+1

2,j,k =

2,j+21,k +vi+1

vi+1

2,j−21,k (2.127)

- 1

- 2


uζi+1

ui+1,j,k +ui,j,k (2.128) where the variables locations are shown in Figure 2.7.

2,j,k =

Since the bottom tangential stresses in equations (2.117) and (2.118) must be supplied from the internal mode solution which follows the external solution, it is lagged at the backward time level. The general source, sink term has been replaced by horizontal diffusion terms having the form proposed by Mellor and Blumberg (1985). The horizontal stress tensors are shown in equations (2.129) to (2.131).

∂uk ∂x

1 mx

(τxx)k = 2AH

(2.129)

(τxy)k = (tyx)k = 2AH

∂vk ∂x

∂uk ∂y

1 my

1 mx

+

(2.130)

###### 40



<<<PAGE 54>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



Fig. 2.7. U-centered grid in the horizontal (x, y) plane.

1 my

(tyy)k = 2AH

∂vk ∂y

. (2.131)

The horizontal diffusion coefficient, AH is often specified as a minimum constant value necessary to smooth cell to cell spatial oscillations in the solution field when the central difference form of the advective acceleration, equation (2.123) is used. When the horizontal turbulent diffusion is used to represent subgrid scale mixing, AH may be determined as suggested by (Smagorinsky, 1963).

The solution scheme for equations (2.117) to (2.119) requires first, the evaluation of all terms in the three equations at time levels n and n−1. On boundaries where the transports are specified, the specified values at time level n+1 are inserted into equation (2.119). Equations (2.117) and (2.118) are then used to eliminate the unknown transports at time level n+1, from equation (2.119). The result is a discrete Helmholtz type elliptic equation for the free surface displacement at time level n+1, having the general form

ζ

u

v

my mx

1 m

mx my

δxζ H

δxuζn+1 +δxζ H

ζn+1 −g∆t2

δyvζn+1 −φ = 0 (2.132)

with the term φ containing all previously evaluated terms and transport boundary conditions. For cells where the free surface displacement is specified, equation (2.132) is replaced by an equation which enforces the specified boundary condition at time level n+1. For the rigid lid case where the free surface displacement is constant in time and space, equation (2.132) is modified to give an equation for the unknown surface pressure, ps by eliminating the first term, replacing gζ in the discrete elliptic operator by ps, and appropriately modifying the last term. In the computer code, the system of equations corresponding to equation

###### 41



<<<PAGE 55>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



- (2.132) is solved by a reduced system conjugate gradient scheme with a multicolor or red-black ordering of the cells (Hageman and Young, 1981). The conjugate gradient iterations continue until the sum of the squared residuals is less than a specified value. The free surface displacements or surface pressures are then substituted into equations (2.117)-(2.118) to determine the transports at time level n+1. Since the solution of equation (2.132) is approximate, equation (2.119) may not be identically satisfied upon substitution of the time level n+1 transports and free surface displacement. To ensure that the equation (2.119) is identically satisfied in the case of a dynamic free surface, it is solved for a revised value of the time level n+1, free surface displacement after introduction of the time level n+1 transports. For the rigid lid case, an external divergence error is calculated and compensated for by adding appropriate volumetric source or sink terms to equation (2.119) during the next time step.


##### 2.5. Computational Aspects of the Three-Time Level Internal Mode Solution

The internal mode equations (2.108) and (2.109) are solved using a fractional step scheme (Peyret and Taylor, 1983) with the first step being explicit and the second step being implicit. Figure 2.8 illustrates the location variables in the x, z plane for the x component of the internal mode equations.

Fig. 2.8. U-centered Grid in the Vertical (x,z) Plane.

###### 42



<<<PAGE 56>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



The computational equations for the three-time level explicit step are;

(Pk+1 −Pk)∗∗ = (Pk+1 −Pk)n−1 −2∆t

u

1 mx

δxu(Pk+1uk+1 −Pkuk)+δyu(Qk+1uk+1 −Qkuk)

u

u (Wu)k+1 −(Wu)k ∆k+1 −

(Wu)k −(Wu)k−1 ∆k

1 mx

−2∆t

u

1 mx

[my fQk+1 −my fQk]u

+2∆t

u

∂my ∂x −uk+1

∂my ∂x −uk

∂mx ∂y

∂mx ∂y

1 mx

+2∆t

vk+1

Hvk+1 − vk

Hvk

u

my mx

- 1

- 2


g (bk+1 −bk)uδxu(h−zkH)+

Huδxu(bk+1∆k+1 +bk∆k)

+2∆t

H

u

1 mx

(Su)k+1 −(Su)k u

+2∆t

u

###### (Qk+1 −Qk)∗∗ = (Qk+1 −Qk)n−1 −2∆t

v

1 my

δyv(Pk+1vk+1 −Pkvk)+δyv(Qk+1vk+1 −Qkvk)

v

v (Wv)k+1 −(Wv)k ∆k+1 −

(Wv)k −(Wv)k−1 ∆k

1 my

−2∆t

v

1 my

[mx fPk+1 −mx fPk]v

−2∆t

v

∂my ∂x −uk+1

∂my ∂x −uk

∂mx ∂y

∂mx ∂y

1 my

−2∆t

vk+1

Huk+1 − vk

Huk

v

- 1

- 2


mx my

g (bk+1 −bk)vδyv(h−zkH)+

Hvδyv(∆k+1bk+1 +∆kbk)

+2∆t

H

v

1 my

(Sv)k+1 −(Sv)k v

+2∆t

v

(2.133)

(2.134)

W = mxmyw = mw, (2.135)

where the superscript ∗∗ denotes the provisional solution, and all the terms that don’t have a specified time level are at the centered time level n. The horizontal volume transport, P and Q are defined by the equation (2.94), and W is the vertical volume transport. The horizontal difference operations on the horizontal advection terms are identical to those presented in Section 2.3, equations (2.122) to (2.124). The vertical momentum flux terms may be represented in forms consistent with central or upwind differencing as shown in equations (2.136) and (2.137).

(Wu)ui,j,k = max

2,j,k +Wi+1

Wi−1

ui,j,k +ui,j,k+1 2

2,j,k

(Wu)ui,j,k =

2

(2.136)

2,j,k +Wi+1

Wi−1

2,j,k

,0 un−1

i,j,k +min

2

Wi−1

2,j,k +Wi+1

2,j,k

,0 un−1

i,j,k+1 (2.137)

2

###### 43



<<<PAGE 57>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



where the advected velocity is in the upwind form, equation (2.137) is evaluated at time level n−1 for stability. The horizontal difference operations on the buoyancy and mean and total depths are central difference operators defined by equations (2.120) and (2.121). The inclusion of horizontal diffusion in the source, sink terms in equations (2.133) and (2.134) would follow from its inclusion in equations (2.117) and (2.118). The Coriolis and curvature terms are averaged and differenced by the energy conserving scheme presented in the Section 2.3, equations (2.125) to (2.128). The stability of the explicit fractional step (Equations

- (2.133) and (2.134)) is governed by the stability of the discretization of the horizontal and vertical advective accelerations, which will be discussed in Section 2.5, and the discretization of the Coriolis and curvature terms. The results of the Fourier stability analysis of the external mode scheme, with respect to the Coriolis acceleration, can be shown to apply to the internal mode scheme as well. The computational equations for the second step of the three-time level scheme are:


(Pk+1 −Pk)n+1 muy∆k+1,k

(Pk+1 −Pk)∗∗ muy∆k+1,k

+2∆t

=

(τxz)k −(τxz)k−1 ∆k∆k+1,k

(τxz)k+1 −(τxz)k

∆k+1∆k+1,k −

n+1

(2.138)

(Qk+1 −Qk)n+1 mvx∆k+1,k

(Qk+1 −Qk)∗∗ mvx∆k+1,k

+2∆t

=

(tyz)k −(tyz)k−1 ∆k∆k+1,k

###### (tyz)k+1 −(tyz)k

∆k+1∆k+1,k −

n+1

(2.139)

Using equations (2.97) and (2.98), the turbulent shear stresses are related to the horizontal transports by:

(τxz)nk+1 =

Auv Hu

n

k

Pk+1 −Pk ∆k+1,k

1 muyHu

n+1

(2.140)

(tyz)nk+1 =

Avv Hv

n

k

Qk+1 −Qk ∆k+1,k

1 mvxHv

n+1

(2.141)

Equations (2.140) and (2.141) could be used to eliminate the turbulent shear stresses from equations (2.138) and (2.139) to give a pair of K−1 systems of equations for the transport differences between layers, however, the resulting equations are poorly conditioned. Instead, equations (2.140) and (2.141) are used to eliminate the horizontal transport differences at time level n+1 from equations (2.138) and (2.139) to give a pair of K −1 equations for the turbulent shear stresses.

1 ∆k∆k+1,k

(τxz)nk−+11 +

−

n

(Hu)n+1 2∆t

Hu Auv

1 ∆k∆k+1,k

1 ∆k+1∆k+1,k

(τxz)nk+1

+

+

k

(Pk+1 −Pk)∗∗ ∆k+1,k

1 ∆k+1∆k+1,k

- 1

- 2∆tmuy


(τxz)nk++11 =

−

(2.142)

1 ∆k∆k+1,k

(tyz)nk−+11 +

−

n

(Hv)n+1 2∆t

Hv Avv

1 ∆k+1∆k+1,k

1 ∆k∆k+1,k

(tyz)nk+1

+

+

k

(Qk+1 −Qk)∗∗ ∆k+1,k

1 ∆k+1∆k+1,k

- 1

- 2∆tmvx


(tyz)nk++11 =

−

(2.143)

###### 44



<<<PAGE 58>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



These equations are diagonally dominant and well conditioned, and can be solved independently at each of the horizontal velocity locations. Since equations (2.142) and (2.143) represent fully implicit, backward difference in time, schemes for one dimensional parabolic diffusion equations, the solutions are unconditionally stable (Fletcher, 1988). Given the solutions of the equations (2.142) and (2.143), the shear stresses, the K−1 transport differences, Pk+1−Pk, and Qk+1−Qk, are determined from equations (2.140) and (2.141) and combined with the continuity constraints, equations (2.106) and (2.107), to form a pair of K equations for the horizontal transports in each cell layer. To illustrate, the horizontal transports in the surface cell layer are determined analytically and given as

K−1

### ∑

Pk = Pˆ +

k=1

k

### ∑

∆j (Pk+1 −Pk). (2.144)

j=1

A similar expression can be derived for QK. Working down from the surface using the K − 1 transport differences allows the remaining transports to be determined. It is noted for later use that the bottom cell layer transports can be expressed in terms of the depth integrated transports and the transport differences using:

K−1

### ∑

P1 = Pˆ −

k=1

k

### ∑

∆j (Pk+1 −Pk), (2.145)

1−

j=1

and an identical equation for Q1.

The solution of equations (2.142) and (2.143) requires specification of bottom and surface stresses at k = 0 and k = K, respectively. On the free surface, (k = K) the surface wind stress components are specified. On the bottom fluid-solid boundary, (k = 0) the bottom stress must be specified. The simplest approach to specifying the bottom stress components utilizes the velocity component in the bottom cell layer and the quadratic friction relations shown in equations (2.146) and (2.146).

(τxz)n0+1 = Cb (u1)2 +(vu1)2

n P1 muyHu

n+1

(2.146)

(tyz)n0+1 = Cb (uv1)2 +(v1)2

n Q1 mvxHv

n+1

(2.147)

Assuming a logarithmic velocity profile between the solid bottom and the middle of the bottom cell layer gives the bottom stress coefficient:

κ2

2 (2.148)

Cb =

ln ∆21zH∗0

where z∗o is the dimensional bottom roughness height. Inserting equation (2.145) and a corresponding equation for Q1 into equations (2.146) and (2.147), respectively allows the bottom stresses at time level n+1

###### 45



<<<PAGE 59>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



to be expressed in terms of the depth integrated transport components, known from the external mode solution, and the unknown transport differences at time level n+1. However, the transport differences at time level n+1 are related to the shear stress components by equations (2.140) and (2.141), allowing the bottom stresses to be expressed in terms of the depth integrated transports and the internal shear stresses by:

  

  , (2.149)

n+1

n

∆k+1,k(τxz)nk+1

P ˆ muyHu

K−1

k

### ∑

### ∑

(τxz)n0+1 = Cb (u1)2 +(vu1)2

∆j

1−

−

n k

Auv Hu

j=1

k=1

and a similar expression for the y component. Inserting equation (2.149) and the corresponding y component equation for the bottom stress components into the k = 1 pair of equations (2.142) and (2.143) results in a nearly tri-diagonal system with a fully populated first row. The systems of equations are still efficiently solved using a tri-diagonal equation solver and the Sherman-Morrison formula (Press et al., 1986).

The internal mode solution is completed by the determination of the vertical velocity using:

∆k mζ

wk = wk−1 −

δxζ Pk −Pˆ +δyζ Qk −Qˆ (2.150)

which follows from the equation (2.111). The solution of equation (2.150), where all variables are at time level n+1, proceeds from k = 1 since wo = 0. A two time level correction step is also periodically inserted into the internal mode time integration on the same time step as the external mode correction. The computational equations follow directly from the three time level equations using the details of the external mode presented in Section 2.4..

##### 2.6. Vertical Layering Options

This section summarizes the vertical coordinate options in EFDC+. It supplements the theoretical and computational description of the basic EFDC+ hydrodynamic and transport model components. The EFDC+ model was originally formulated with a SIG stretched vertical coordinate. Later, more efficient vertical layering options, namely SGZ options have been implemented to reduce the error due to the horizontal pressure gradients and to reduce the number of computational cells.

##### 2.6.1 Standard Sigma (SIG) Approach

The SIG approach is a topographically conformal vertical coordinate system which is widely used in threedimensional hydrodynamic models. In this vertical coordinate system, the number of vertical levels in the water column is the same everywhere in the domain irrespective of the depth of the water column (Figure

- 2.9(a)). This can resolve the water column equally well and equally efficiently in both shallow and deep regions of a computational domain simultaneously and it is suitable for a water body with complicated geometry and large changes in bottom elevation. The transformation of the governing equations using sigma-coordinate in the vertical is described in the Section 2.1.


In the SIG coordinate formulation, the number of vertical layers is the same at all horizontal locations in the model grid. Although this formulation is widely accepted, conceptually attractive and adequate for a large range of applications, there are numerous application classes where a traditional z or physical vertical

###### 46



<<<PAGE 60>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



Fig. 2.9. An Illustration of EFDC+ Layering Options for a Model with K = 10. (a) SIG, (b) SGZ-Specified Bottom, and (c) SGZ-Uniform Layering.

grid is desirable, such as deep reservoirs with rapid and large lateral bathymetric changes. There are also applications where the ability to use a combination of SIG and physical z vertical layering in different regions of the horizontal domain would be desirable. An example would be a deep navigation channel in an otherwise shallow estuary. The SIG stretched vertical grid formulation may also be subject to internal pressure gradient errors (Mellor et al., 1994) providing another motivation for having alternative options to the sigma formulation.

##### 2.6.2 Sigma-Zed Approach (SGZ)

The SIG grid used for the transformation of the vertical coordinate introduces a well-known error in the horizontal gradient terms including the concentration, velocity, and pressure (Mellor et al., 1994). In general, this error is significant only in the regions with steeply varying bathymetry. In order to overcome this weakness, two new vertical layering approaches that are computationally efficient have been developed and applied in EFDC+ model (Craig et al., 2014). The vertical layering scheme has been modified to allow the number of layers to vary over the model domain based on the water depth. Consequently, each cell can have a different number of layers. The z coordinate system varies for each cell face, matching the number of active layers to the adjacent cells (face matching of layering is a fundamental difference with the GVC approach). Such a transformation is referred to as the SGZ coordinate. The differences in the two optional SGZ approaches relate to the SIG layer thickness computed for each cell. Figure 2.9 shows a schematic demonstrating the layering options. Panel (a) represents a SIG stretch grid with 10 layers. Panels (b) represents the specified bottom approach which allows a user specified number of layers in each horizontal cell. Figure 2.9(c) represent SGZ options with uniform layering where the bottom of each vertical layer are aligned in the horizontal direction. It should be noted that, in SGZ coordinate the number of vertical layers can be very large, but the computational time is shorter in comparison with a similarly configured SIG coordinate model.

A new vertical layering option following the Sigma-Zed (SGZ Specified Thickness from Top ) approach has recently been added to EEMS 12.1. When using this approach, the user can configure the model layers not

- as relative splits but as actual layer thicknesses in meters. The layers are built starting from the top, and the


###### 47



<<<PAGE 61>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



bottom of each layer is aligned in the horizontal direction. Similar to a Z grid, this option gives the user the flexibility to specify the layer thickness and the maximum depth of the model domain to generate an appropriate vertical layering scheme.

For SGZ transformation, the equations are still the same as the SIG transformation, however, the number of layers at each cell differs based on a factor determined based on the ratio between bed elevation and the minimum elevation. In addition, the thickness of layers at each cell must satisfy

KC

### ∑

∆zk = 1, (2.151)

k=n

in which KC is the maximum number of layers, n the index of bottom layer and ∆zk the thickness of layer k. For the original SIG the index of the bed layer always is equal to n = 1 while in the SGZ this value can vary in the range 1 ≤ n ≤ K depending on the number of layers due to the rescaling. This requirement improves the accuracy of the horizontal gradient calculation for the variable Ci,j,k of the cell L(i, j) at layer k :

Ci,j,k −Ci−1,j,k ∆x

pd[Ci,j,k]x =

. (2.152)

When sediment transport is simulated and bed morphology is considered, the determination of the new indices of bottom layers should be implemented at every time step. This is because currently the ratios between water depths and the maximum are changing due to erosion or deposition compared to the previous time step. Therefore, an update of layering for the whole domain is important and necessary for SGZ. However, the re-layering is only an optional approach.

The other necessary modification for SGZ coordinate system is the treatment on wet/dry in 3-D calculation of the horizontal gradient when the number of layers at cell L(i − 1, j) is less than that at cell L(i, j). It should be noted that this problem does not appear for SIG coordinates, because the number of layers is the same for every cell. This means that the SIG model requires more calculation time than the model with SGZ approach.

##### 2.7. Near-Field Discharge Dilution and Mixing Zone Analysis

The calculation procedure of the jet/plume submodel is mainly based on Lee and Cheung (1990). The trajectory of a group of plume particles is traced in time using a Lagrangian formulation. The plume puff gains mass as ambient fluid is entrained and mixed within it, but once entrained, the new mass becomes an indistinguishable part of the plume puff. In the simplest version, the plume is assumed to be essentially a cylindrical segment whose radius grows as mass is entrained. The initial plume mass is identified as the mass issuing from a diffuser with radius b0 :

M0 = ρ0πb20h0, (2.153)

where, M0 is the initial mass, ρ0 is the initial density, b0 is the diffuser radius, h0 is the length of the plume mass and is chosen to be comparable to b0. For example, h0 = r and b0 = r, where r is the radius of the diffuser. The initial length of the plume can be estimated from the initial plume velocity V0 and time ∆t:

###### 48



<<<PAGE 62>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



h0 = V0∆t (2.154)

The increment in the plume mass at the time step nth is evaluated as the sum of the plume mass increment due to the shear-induced entrainment and the forced entrainment.

∆Mn = ∆Ms +∆Mf (2.155)

In equation (2.155) ∆Ms is the increase in mass due to shear entrainment, and ∆Mf is the increase in mass due to forced entrainment. A schematic of a rising plume discharged into a water body is shown in Figure

- 2.10.


Fig. 2.10. Near field Jet Plume mixing.

##### 2.7.1 Shear-Induced Entrainment

The increase in mass of the plume element is due to turbulent entrainment of the ambient flow. Close to the discharge point, or in a very weak current, shear-induced entrainment dominates. In general, however, the forced entrainment of the cross flow dominates, except very close to the source. In the model, assuming the total entrainment is a function of the horizontal currents and a shearing action of the plume relative to the currents, the increase in mass due to shear entrainment, ∆Ms, is written as

∆Ms = ρa2πbnhnE |Vn −uacosφncosθn |∆t. (2.156)

Where the jet axis makes an angle of φn with the horizontal plane, and θn is the angle between the x-axis and the projection of the jet axis on the horizontal plane. ρa is the ambient density and ua is the ambient current.

###### 49



<<<PAGE 63>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



The subscript n denotes the value of plume element at nth step of calculation, the subscript a denotes the local ambient value, E is the entrainment coefficient which is dependent on the local densimetric Froude number F1 and jet orientation

0.057−0.554sinFθ2n

√2

E =

, (2.157)

1

1+5|V uacosφn cosθn

n−uacosφn cosθn |

where, F1 is the local densimetric Froude number, and is given by

and α is a proportionality constant.

F1 = α |Vn −uacosφn cosθn | g∆ρρn

, (2.158)

bn

a

##### 2.7.2 Forced Entrainment

Experimental observations by Chu and Goldberg (1984) and Stuart Churchill (1975) have shown that the transfer of horizontal momentum is complete beyond a few jet diameters. We assume that all the ambient flow on the downdrift side of the plume is entrained into the plume element. This forced entrainment of the ambient flow into an arbitrarily inclined plume element can be formulated as

∆Mf = ρaua 2b∆s 1−cos2φ cos2θ +πb∆bcosφ cosθ +

- 1

- 2


πb2∆(cosφ cosθ) (2.159)

In the equation 2.159, the first term represents the forced entrainment due to the projected plume area normal to the cross flow; the second term is a correction due to the growth of plume radius; and the third term is a correction due to the curvature of the trajectory. ∆s is the arc length of the centerline axis of the plume element subtending an angle ∆φ at the center of curvature.

An initial estimate of ∆Mf can be obtained as

∆Mf = ρauahnbn 2 sin2φ +sin2θ −sin2φ sin2θ n

(cosφ cosθ)n −(cosφ cosθ)n−1 ∆sn

∆b ∆s

πbn 2

+ π

cosφ cosθ

+

n

∆t

(2.160)

##### 2.7.3 Model Implementation

At the nth step, consider a plume element located at (xn, yn, zn) with the velocity (un, vn, wn) and its magnitude Vn. The jet axis makes an angle of φn with the horizontal plane, and θn is the angle between the x-axis and the projection of the jet axis on the horizontal plane. The half-width or radius of the plume element

###### 50



<<<PAGE 64>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



is bn; hn is the thickness, defined as proportional to the magnitude of the local jet velocity, hn = Vn∆t. The mass of the plume element is then given by

Mn = ρnπb2nhn (2.161)

Given the increase in mass due to turbulent entrainment, ∆Mn the plume element characteristics at the next step are obtained by applying conservation of mass, horizontal and vertical momentum, energy, and tracer mass to the discrete element. For completeness, the self-explanatory equations of the generalized Lagrangian model, essentially similar to its original two-dimensional counterpart (Winiarski and Frick, 1976) are summarized as follows:

Mass conservation:

Mn+1 = Mn +∆Mn (2.162)

Mn+1 = ρn+1πb2n+1hn+1 (2.163)

The concentration of the tracer, salinity, temperature and water density:

MnCn +∆MnCa Mn+1

Cn+1 =

(2.164)

MnSn +∆MnSa Mn+1

Sn+1 =

MnTn +∆MnTa Mn+1

Tn+1 =

(2.165)

(2.166)

The horizontal momentum:

ρn+1 = ρ (Sn+1,Tn+1) (2.167)

The vertical momentum

Mnun +∆Mnua Mn+1

un+1 =

Mnvn Mn+1

vn+1 =

(2.168)

(2.169)

Mnwn +∆Mn+1 ∆ρρ

g∆t Mn+1

n+1

wn+1 =

(2.170)

###### 51



<<<PAGE 65>>>

###### 2. HYDRODYNAMICS EFDC+ Theory



(Mw)n+1 = (Mw)n +(∆ρV)n+1g∆t (2.171) where,

Vn+1 = u2n+1 +v2n+1 +w2n+1, and (2.172)

Un+1 = u2n+1 +v2n+1 (2.173) The new thickness and radius of the plume element:

The jet orientation:

hn+1 =

Vn+1 Vn

hn (2.174)

bn+1 =

Mn+1 πρn+1hn+1

(2.175)

φn+1 = arctan

θn+1 = arctan

The new location of the plume element:

wn+1 Un+1

vn+1 un+1

(2.176)

(2.177)

The distance along the trajectory:

xn+1 = xn +un+1∆t (2.178) yn+1 = yn +vn+1∆t (2.179) zn+1 = zn +wn+1∆t (2.180)

∆sn+1 = Vn+1∆t (2.181)

The time step ∆t can be fixed or variable; its is chosen via a “prediction-correction” procedure to attain a prescribed fractional change in mass (typically of the order of 1%) at each step.

##### 2.8. Conclusion

In this chapter, the theoretical aspect of basic for the EFDC+ hydrodynamics are presented, including the governing equations, vertical layering options, near-field discharge, and external forcing options, such as wave models. The following chapters describe how the density effects for temperature and salinity may be incorporated into the hydrodynamic module, as well as linkage to constituent transport modules.

###### 52



<<<PAGE 66>>>

# Chapter 3

# CONSERVATIVE CONSTITUENTS TRANSPORT

##### 3.1. Introduction

This section summarizes the theoretical and computational aspects of the transport formulations for passive scalar transport used in EFDC+. Theoretical and computational aspects for the EFDC generic transport model components are presented in Hamrick (1992).

##### 3.2. Basic Equation of Advection-Diffusion Transport

The generic transport equation for a dissolved or suspended material is shown in equation (3.1):

∂ ∂t

∂ ∂x

∂ ∂y

∂ ∂z

∂ ∂z

(mxmyHC)+

(myHuC)+

(mxHvC)+

(mxmywC)−

(mxmywscC)

∂ ∂x

∂ ∂y

∂ ∂z

my mx

mxmy H

dC dx

mx my

dC dy

dC dz

+SC (3.1) where,

HAH

HAH

Ab

=

+

+

x, y are the orthogonal curvilinear coordinates in the horizontal direction (m), z is the sigma coordinate (dimensionless),

- t is time (s), mx, my are the square roots of the diagonal components of the metric tensor (dimensionless), m is the Jacobian of the metric tensor determinant (dimensionless), m = mxmy,

C is the concentration or intensity of transport constituent (g/m3 for concentration of dis-

solved/suspended material, ◦C for temperature, ppt for salinity), H is the total water depth (m),

- u, v are the horizontal velocity components in the curvilinear coordinates (m/s),


###### 53



<<<PAGE 67>>>

###### 3. CONSERVATIVE CONSTITUENTS TRANSPORT EFDC+ Theory



w is the vertical velocity component (m/s), AH is the horizontal turbulent eddy diffusivity (m2/s), Ab is the vertical turbulent eddy diffusivity (m2/s), wsc is a positive settling velocity when C represents a suspended material, and Sc is the source/sink term for the constituent that includes subgrid scale horizontal diffusion and

thermal sources and sinks.

##### 3.3. Numerical Solution for Transport Equations

In this section, solutions techniques for the transport equations for salinity, temperature, turbulence intensity, and turbulence length scale are presented. Stability and accuracy aspects of the advection schemes common to the transport equations and the external and internal horizontal momentum equations are also discussed. The salinity transport equation (3.2) is used as a generic example and the location of variables is shown in Figure 3.1.

Fig. 3.1. S-centered Grid in the Vertical (x,z)-Plane

The salinity transport equation (3.2) is integrated over a cell layer to give:

∂ ∂t

∂ ∂x

∂ ∂y

(WC)k −(WC)k−1

(mHCk)+

(PkCk)+

(QkCk)+

dk −

m dk

Ab H

dC dz k −

Ab H

dC dz k−1 −(SC)k = 0 (3.2)

where, Pk, Qk, and Wk are defined by equations (2.94) and (2.135). The source, sink, advection, and vertical diffusion portions of equation (3.2) are treated in separate fractional steps, as was done for the internal mode momentum equations in Section 2.4.

###### 54



<<<PAGE 68>>>

###### 3. CONSERVATIVE CONSTITUENTS TRANSPORT EFDC+ Theory



Fig. 3.2. Sigma Coordinate and Variable Center (Ji, 2008).

The three time level fractional step sequence is given by:

2dt mHn−1

Ck∗ = Cn−1

k +

(SC)nk−1 (3.3)

(WC)k −(WC)k−1 dk

(mH)n+1Ck∗∗ = (mH)n−1Ck∗ − 2dt dxd (PkCk)+dyd (QkCk)+

(3.4)

(HCk)n+1 − 2dt

Ab H

n

(Ck+1 −Ck)n+1

dkdk+1,k −

k

Ab H

n

(Ck −Ck−1)n+1 dkdk,k−1

k−1

= Hn+1Ck∗∗ (3.5)

The source, sink step (see equation (3.3)) is explicit and involves no changes in cell volumes. When the source, sink term represents horizontal turbulent diffusion, it is evaluated at time level n−1, for stability (Fletcher, 1988). The advection step, equation (3.4), is explicit and involves changes in cell volumes. The vertical diffusion step, equation (3.5), which involves no changes in cell volumes, is fully implicit and unconditionally stable (Fletcher, 1988).

Rearranging equation (3.5), the vertical diffusion step, gives:

2dt dkdk,k−1

−

Ab H

n

Ckn−+11 +

k−1

2dt dkdk,k−1

Ab H

n

n

2dt dkdk+1,k

Ab H

+Hn+1 +

Ckn+1− 2dt dkdk+1,k

k−1

k

n

Ab H

Ckn++11 = Hn+1Ck∗∗ (3.6)

k

For salinity, temperature, and suspended sediment concentration, the generic variable C is defined vertically

- at cell layer centers, and the diffusivity is defined at cell layer interfaces. Equation (3.6) then represents


###### 55



<<<PAGE 69>>>

###### 3. CONSERVATIVE CONSTITUENTS TRANSPORT EFDC+ Theory



a system of K equations and the boundary conditions are generally of the specified flux type. Specified surface and bottom flux boundary conditions are most conveniently incorporated in the surface and bottom cell layer source and sink terms allowing Ab at the bottom boundary (k = 0) and the surface boundary (k = k + 1) to be set to zero making equation (3.6) tri-diagonal. For turbulence intensity and turbulence length scale, equations (2.24) and (2.25), the generic variable C is defined vertically at cell layer interfaces and the diffusivity is defined at cell layer centers. Equation (3.6) then represents a system of K−1 equations for the variables at internal interfaces with the variable values at the free surface and bottom being provided as boundary conditions. For the turbulence intensity and length scale, the boundary conditions are:

q20 = B21/3 tbx2 +tby2 ,l0 = 0, atz= 0 (3.7)

q2K = B21/3 tsx2 +tsy2 ,lK = 0, atz= 1 (3.8)

where, τb and τs are the bottom and surface stress vectors, respectively. Insertion of these boundary conditions results in equation (3.6) representing tri-diagonal systems of K − 1 equations for the turbulence intensity and length scale.

Without loss of generality, the notation used in analyzing the three time level advection step, equation (3.4), is simplified by replacing the double and single asterisk intermediate time level indicators by n+1 and n−1, respectively to give:

dt dx

(mHCk)n+1 = (mHCk)n−1 −2

(PC)i+1

###### 2,j,k −(PC)i−1

2,j,k − 2

dt dk

dt dy

(QC)i,j+1

2,k −(QC)i,j−1

2,k −2

(WC)k −(WC)k−1 (3.9)

where the horizontal central difference operators have been expanded about the cell volume centroid (x,y), according to equations (2.120) and (2.121). The cell face fluxes can be represented consistent with centered in time and space differencing as was illustrated by equations (2.122), (2.123) and (2.136) or forward in time and backward or upwind in space as was illustrated by equations (2.124) and (2.137) for the x momentum fluxes. For the centered in time and space form, equation (3.9) becomes:

(mHCk)n+1 = (mHCk)n−1−

dt dx

P ˜i+1

dt dy

Q ˜i,j+1

2,j,k Ci+1,j,k +Ci,j,k −P˜i−1

2,j,k Ci,j,k +Ci−1,j,k −

2,k Ci,j+1,k +Ci,j,k −Q˜i,j−1

2,k Ci,j,k +Ci,j−1,k −

dt dk

W ˜i,j,k Ci,j,k+1 +Ci,j,k −W˜i,j,k−1 Ci,j,k +Ci,j,k−1 (3.10)

The transports in equation (3.10) are evaluated at the centered time level when used in the external and internal momentum equations, and are averaged to the centered time level using

- 1

- 2


P˜k =

Pkn+1 +Pn−1

k (3.11) when used in the transport equations for scalar variables.

###### 56



<<<PAGE 70>>>

# Chapter 4 DYE MODULE

The dye constituent in EFDC+ represents a dissolved substance in the water column that does not impact the hydrodynamics (i.e. no impact on thermal physical properties such as density and viscosity) or any other water column process (e.g. light extinction). This constituent can be used as a tracer, with or without decay, or it can also be used to compute the age of water in days.

The dye is transported in the water column as determined by the equation (4.1).

∂ ∂t

(mxmyHC)+

∂ ∂x

(myHuC)+

∂ ∂x

my mx

=

∂ ∂y

(mxHvC)+

∂ ∂y

dC dx

HAH

+

∂ ∂z

(mxmywC)−

mx my

dC dy

HAH

∂ ∂z

(mxmywscC)

∂ ∂z

mxmy H

dC dz

Ab

+

dC dt

###### +S

+

C

(4.1)

##### 4.1. Decay

The dye constituent can be configured to decay with a zeroth or first order approach, as shown in the equations (4.2) and (4.3), respectively.

dC dt

= −K (4.2)

dC dt

= −KC (4.3)

In equations 4.2 and 4.3, C is the dye concentration in g/m3, K is the first order decay rate in 1/s and t is time is seconds.

Additionally, dye decay rate can be a function of water temperature using the equation (4.4).

dC dt

= −Kθ(T−Tref)C (4.4)

###### 57



<<<PAGE 71>>>

- 4. DYE MODULE EFDC+ Theory


##### 4.2. Age of Water

- As mentioned, the dye constituent may be used to calculate the age of water (in days). With this option, a zero-order kinetic rate approach is used:


dC dt

= −K (4.5)

where C is “age” in days, t is time in days and K is in units of 1/day. By averaging cell ages over all or parts of the model domain, residence times can be computed. If the model is run sufficiently long enough to achieve a dynamic steady state, the hydraulic residence time can be computed.

###### 58



<<<PAGE 72>>>

# Chapter 5 TEMPERATURE AND HEAT TRANSFER

This chapter presents an overview of heat transfer implemented in EFDC+, including the energy equation and heat transfer options. Additional details are given regarding the processes for water column temperature, surface and bed heat exchange, and ice formation and melt. The sources of heat in the system include surface heat exchange, short wave radiation absorption, bottom heat exchange, and any inflow or outflow (e.g. boundary condition). The conceptual framework for temperature is shown in Figure 5.1.

Fig. 5.1. Conceptual Framework for Temperature.

The basic equation for heat transfer in curvilinear and sigma coordinates is the generic transport equation 3.1. To solve the equation for heat transport; hydrodynamic transport, turbulent mixing, and horizontal diffusion are provided by the hydrodynamic module.

###### 59



<<<PAGE 73>>>

###### 5. TEMPERATURE AND HEAT TRANSFER EFDC+ Theory



##### 5.1. Surface Heat Exchange

- At the water surface (z = 1), the boundary condition for the heat exchange can be calculated as


ρcpAb H

∂T ∂z

= HL +HE +HC (5.1) where,

−

ρ is the water density (kg/m3), cp is the specific heat of water (J/kg/◦C)), Ab is the vertical eddy diffusivity (m2/s), H is the water depth (m), HL is the surface heat exchange flux due to long wave back radiation (W/m2), HE is the surface heat exchange flux due to latent heat (W/m2), and HC is the surface heat exchange flux due to sensible heat (W/m2).

The surface heat exchange is calculated using three methods:

- 1. Full Heat Balance
- 2. COARE 3.6 bulk algorithm
- 3. Equilibrium Temperature


##### 5.1.1 Full Heat Balance

In the full heat balance method, the heat exchange flux due to long wave back radiation, latent heat, and sensible heat are calculated based on the approach proposed by Rosati and Miyakoda (1988) and Hamrick (1992).

HL = εσ(Ts +273.15)4(0.39−0.05√ea)(1+BcC)+4εσ(Ts +273.15)3(Ts −Ta) (5.2) HE = ceρaLEWs(es −ea)

0.622 Pa

(5.3)

HC = chρacpaWs(Ts −Ta) (5.4) where,

ε is the emissivity of the waterbody (ε = 0.97), σ is the Stefan–Boltzmann constant (σ = 5.67×10−8 W/m2/K4), C is the cloud fraction (C = 0 : cloudless, C = 1 : full cloud coverage), Bc is an empirical constant (Bc = 0.8),

###### 60



<<<PAGE 74>>>

###### 5. TEMPERATURE AND HEAT TRANSFER EFDC+ Theory



Ts is the water surface temperature (◦C), Ta is the air temperature (◦C), ce,ch are the turbulent exchange coefficients, ρa is the atmospheric density (ρa = 1.2 kg/m3), cpa is the specific heat of air (cpa = 1005 J/kg/K), LE is the latent heat of evaporation (LE = 2.501×106 J/kg), Ws is the wind speed (m/s),

- es is the saturation vapor pressure at surface water temperature (mb), ea is the actual vapor pressure (mb), and Pa is the atmospheric pressure (mb).


The full heat balance method in the EFDC+ (non-legacy option) is fully linked with the ice module that incorporates ice growth and melt processes.

##### 5.1.2 COARE 3.6 Bulk Algorithm

From EFDC+ 12.1, the Coupled Ocean–Atmosphere Response Experiment (COARE) module version 3.6 has been implemented in the EFDC+ code as a new option for the calculation of water surface heat exchange. The algorithm of COARE, developed by C. Fairall, E. F. Bradley, and D. Rogers (see Fairall et al. (1996), Fairall et al. (2003)), follows the standard Monin-Obukhov similarity theory (MOST) for near-surface meteorological measurements and is designed to give estimates of the turbulent fluxes of sensible and latent heat and the stress from inputs of bulk variables.

Bulk algorithms are based upon MOST representations of the fluxes in terms of mean quantities:

w′x′ = c1x/2c1d/2S∆X = CxS∆X (5.5)

Where x can be wind components, the potential temperature, the water vapor specific humidity, etc. Here cx is the bulk transfer coefficient for the variable x and Cx is the total transfer coefficient. Here ∆X is the air-sea difference in the mean value of x, and S is the mean wind speed. As a result, sensible heat HC, and latent heat HE are defined by the normal Reynolds averages,

HC = ρacpaw′T′ = ρacpaChS(Ts −θ) (5.6) HE = ρaLew′q′ = ρaLeCeS(qs −q) (5.7)

WhereCh andCe are the transfer coefficients for sensible heat, and latent heat, respectively; θ is the potential temperature, q is the water vapor mixing ratio, and ui is one of the horizontal wind components. S is the average value of the wind speed; Ts is the water surface temperature; usi is the surface current; and qs is the interfacial value of the water vapor mixing ratio.

The water surface is characterized by the velocity roughness, specified as Charnock’s expression plus a smooth flow limit,

αu2∗ g

0.11ν u∗

(5.8) Where u∗ is the friction velocity, and is water kinetic viscosity.

z0 =

+

###### 61



<<<PAGE 75>>>

###### 5. TEMPERATURE AND HEAT TRANSFER EFDC+ Theory



##### 5.1.3 Equilibrium Temperature

A computed equilibrium temperature can be used for the surface heat exchange in EFDC+. The approach used here is based on the equilibrium temperature computation approach in the CE-QUAL-W2 (W2) (Wells and Cole, 2000). Equilibrium temperature module is fully linked with ice module that incorporates ice growth and ice melt processes.

Because some of the terms in the term-by-term heat balance equation are surface temperature dependent and others are measurable or computable input variables, the most direct route to simplify computation is to define an equilibrium temperature, Te as the temperature at which the net rate of surface heat exchange is zero.

Linearization of the term-by-term heat balance along with the definition of equilibrium temperature allows for expression of the net rate of surface heat exchange, Hn as:

Hn = −Kaw (Ts − Te ) (5.9) where,

Hn is the rate of surface heat exchange (W/m2), Kaw is the coefficient of surface heat exchange (W/m2/◦C), Ts is the water surface temperature (◦C), and Te is the equilibrium temperature (◦C).

Seven separate heat exchange processes are summarized in the coefficient of surface heat exchange and equilibrium temperature. In EFDC+, Te and Kaw are computed from heat flux equation where Hn = 0 or approximate technique (Brady et al., 1969).

where,

Isw 23+ f(W)(β +0.255)

Te =

+Td (5.10)

Te is the equilibrium temperature in ◦F, Isw is the solar radiation at the water surface (Btu/ft2/day), β = 0.255−0.0085T∗ +0.000204T∗2,

T∗ = 0.5(Ts +Td), Ts is the water surface temperature in ◦F, Td is the dew point temperature in ◦F, W2 is the wind speed at 2m in mph, and K is computed from the slope of the net flux vs temperature or using the approximate formula in

units of Btu/ft2/day/◦F.

K = 23+(βw +0.225)17W2 (5.11)

###### 62



<<<PAGE 76>>>

###### 5. TEMPERATURE AND HEAT TRANSFER EFDC+ Theory



where,

βw = 0.255−0.0085Tw −0.000204Tw2 (5.12)

It must be noted that the equations for heat flux in this method are English units. EFDC+ internally converts the SI units to English units and then converts them back to SI units after the calculation.

##### 5.2. Short Wave Radiation

Short wave solar radiation is an important contributor to the heat balance in water. As the short wave radiation passes from the surface (liquid or ice), the The light extinction coefficient (also referred to as the light attenuation coefficient) is the measure for the reduction (absorption) of light intensity within a water column. The solar radiation at the surface Isw is a function of location, time of the year, time of day, meteorological conditions, and shading due to terrain and vegetation. The incident solar radiation I0 is a function of location, time of the year, time of day, and meteorological conditions. The light intensity at the water surface Isw, is given by:

Isw = I0Sf min{exp[−Ke,me(Hrps −H)],1}min{exp[−Ke,iceHice],1} (5.13) where,

I0 is the measured solar radiation at the Earth’s surface (W/m2), Sf is the tree canopy and/or terrain shading factor (dimensionless), Hice is the ice thickness (m), Ke,ice is the light extinction coefficient for ice cover (1/m), Ke,me is the light extinction coefficient for emergent shoots (1/m), Hrps is the rooted plant shoot height (m), and H is the water column depth (m).

##### 5.2.1 One-band Light Attenuation Model

Solar radiation that penetrates the surface of water is absorbed by water. The absorption heats the water column and radiation penetration depends on the light extinction coefficient, ζ. In the water columns, the depth distribution of short-wave radiation is exponential and can be expressed as Beer’s Law:

I(z) = Iswexp(−ζz) (5.14) where,

I(z) is the solar radiation at depth z below the surface (W/m2), Isw is the solar radiation at the water surface (W/m2), z is the depth below water surface (m), and ζ is the light extinction coefficient (1/m).

###### 63



<<<PAGE 77>>>

###### 5. TEMPERATURE AND HEAT TRANSFER EFDC+ Theory



##### 5.2.2 Two-band Light Attenuation Model

In this method, the extinction coefficient is constant spatially and temporally, and this method is available for the legacy version of EFDC. The depth distribution of the solar radiation heating is an exponential function using two attenuation coefficients, and is expressed as:

I(z) = Isw[Rexp(zζf)+(1−R)exp(zζs)] (5.15) where,

I(z) is the solar radiation at water depth z (W/m2), Isw is the solar radiation at water surface (W/m2), ζf is the fast attenuation coefficients (1/m), ζs is the slow attenuation coefficients (1/m), and R is the fraction of solar radiation fast attenuation, and varies between 0 and 1.

In equation (5.15), the first exponential term characterizes the rapid attenuation in the upper 5 meters due to absorption of the red end of the spectrum; the second exponential represents the attenuation of the blue-green light below 10 meters. The selection of R, ζf, and ζs as constant values depends largely on the characteristic optical properties of the water body being simulated. Several authors have derived these parameters based on observed conditions (Table 5.1).

Table 5.1. Values of parameters determined by fitting the sum of two exponentials to observations of downward irradiance. Table adapted from Paulson and Simpson (1977).

Author Water R ζf ζs

Type (1/m) (1/m) Paulson and Simpson (1977) Run 1 0.74 0.588 0.063

Composite 0.62 0.667 0.050 Kraus and Businger (1994) Very Clear Water 0.4 0.200 0.025 Jerlov (1968) Type I 0.58 2.857 0.043

- Type I (upper 50 m) 0.68 0.833 0.036 Type IA 0.62 1.667 0.050 Type IB 0.67 1.000 0.059
- Type II 0.77 0.667 0.071
- Type III 0.78 0.714 0.127


##### 5.2.3 Water Quality Linked Light Attenuation

This method is used for light attenuation for the Full Heat Exchange and Equilibrium Temperature option. In the Equilibrium Temperature heat exchange option, a constant fraction of the solar radiation is always absorbed in the top layer, regardless of how thick it is or what the extinction coefficient is. This is described by the Beer’s law with the additional term β :

###### 64



<<<PAGE 78>>>

###### 5. TEMPERATURE AND HEAT TRANSFER EFDC+ Theory



I(z) = (1−β)Iswexp(−Kez) (5.16) where,

I(z) is the short wave radiation at depth z (W/m2), β is the fraction absorbed at the water surface (dimensionless),

Ke is the extinction coefficient (1/m), and Isw is the short wave radiation reaching the water surface (W/m2).

##### 5.2.3.1 Light Extinction Factors

The standard EFDC+ term by term full heat balance surface heat exchange processes are the same as the full heat balance (legacy) option. The major difference between these two options is that the standard EFDC+ full heat balance uses variable light extinction factors. A general formulation of the total light extinction including rooted aquatic plants in the model is given by:

where,

Kess =Ke,b+Ke,TSSTSS+Ke,POCPOC+Ke,DOCDOC+Ke,Chl∑Chl+Ke,MACMAC (5.17)

Kess is the total light extinction coefficient (1/m), Ke,TSS is the light extinction coefficient for TSS (1/m per g/m3), Ke,b is the background light extinction (1/m), TSS is the TSS concentration (g/m3) provided from the sediment transport module, POC is the total Particulate Organic Carbon (POC) concentration (labile and refractory) (g/m3) pro-

vided from the water quality module, Ke,POC is the light extinction factor as a function of POC concentrations (1/m per g/m3), DOC is the Dissolved Organic Carbon (DOC) concentration (Labile and Refractory) (g/m3) provided

from the water quality module, Ke,DOC is the light extinction factor as a function of DOC concentrations (1/m per g/m3), Ke,Chl is the light extinction coefficient for floating algae Chlorophyll a (chl a) (1/m per mg Chl per m2), Chl is the chl a concentration of the floating algae group m, Bm is the concentration of algae group m (g C per ml), CChlm is the carbon-to-chlorophyll ratio in algal group m (g C per mg Chl), Ke,MAC is the light extinction coefficient for fixed biota or rooted plant shoots (1/m per gm C per m2),

and MAC is the concentration of fixed biota or plant shoots (g C per m2).

###### 65



<<<PAGE 79>>>

###### 5. TEMPERATURE AND HEAT TRANSFER EFDC+ Theory



If only hydrodynamics and temperature are simulated in the EFDC+ model, then the background light extinction coefficient is used. If hydrodynamics, temperature, and TSS are simulated, then the total light extinction coefficient is a function of the background extinction coefficient and light extinction coefficient due to TSS. If a full water quality model is simulated with TSS then the total light extinction coefficient is the function of background extinction, TSS, POC, DOC and chl a.

Full heat balance with variable light extinction option is fully coupled with ice sub-model and accounts for the ice melt and ice growth. Finally, the surface heat exchange coefficients for latent and sensible heat exchange can be spatially variable.

##### 5.3. Bed Heat Exchange

Sediment bed and water interface heat exchange is typically small compared to water and air interface heat exchange, therefore it is frequently neglected. However, including sediment bed heat exchange can improve the simulation of temperature in deep lakes and reservoirs. The heat exchange between the sediment bed and the bottom layer of the water column can be described as

Hb = −(Kb,vU +Kb,c)(Tw −Tb) (5.18)

U = u21 +v21 (5.19) where,

Hb is the sediment bed-water heat exchange (W/m2), Kb,v is the convective heat exchange coefficient (W −s/m3 −◦C), Kb,c is the conductive heat exchange coefficient (W/m2 −◦C),

- u1 is the u component water velocity in layer 1 (m/s),
- v1 is the v component water velocity in layer 1 (m/s), Tw is the water temperature in layer 1 (◦C), and Tb is the sediment bed temperature (◦C)


In EFDC+ code implementation, both sides are divided by water density and specific heat of water, and therefore the units of Kb,c is in m/s and Kb,v is dimensionless. Typical applications have used a value of 0.3 W/m2−◦C for Kb,c that is approximately two orders of magnitude smaller than the surface heat exchange coefficient. Kb,c is often not used (i.e. equal to zero) but can be in the range of 0 to 10. Average yearly air temperature is a good initial estimate of Tb.

Optionally, the bed temperature (Tb) can change with time due to the heat exchange.

δ (DbTb) δt

= −(Kb,vU +Kb,c)(Tb −Tw) (5.20)

where, DB is the sediment bed-thermal thickness (m). Selection of the thermal thickness is subject to initial approximation and subsequent calibration. The larger the thermal thickness is, the slower the bed temperature will change.

###### 66



<<<PAGE 80>>>

###### 5. TEMPERATURE AND HEAT TRANSFER EFDC+ Theory



##### 5.4. Ice Formation and Melt

The ice module implemented in EFDC+ is based on the W2 (Wells and Cole, 2000) ice module. In this module, ice formation and melt is simulated by EFDC+ using a coupled heat approach. However, ice dynamics (i.e. movement of ice block/chunks) have not yet been implemented.

- 5.4.1 Heat Balance The heat balance for the water-to-ice air system is given by:


dh dt

ρiLf

= hai(Ti −Te)−hwi(Tw −Tm) (5.21) where,

ρi is the density of ice (kg/m3), Lf is the latent heat of fusion of ice (J/kg), dh/dt is the change in ice thickness (h) with time (t) (m/s), hai is the coefficient of ice-to-air heat exchange (W/m2/◦C), hwi is the coefficient of water-to-ice heat exchange through the melt layer (W/m2/◦C), Ti is the ice temperature (◦C), Te is the equilibrium temperature of ice to air heat exchange (◦C), Tw is the water temperature below ice (◦C), and Tm is the melt temperature (◦C).

Formation of ice requires lowering the surface water temperature to the freezing point by normal surface heat exchange processes. With further heat removal, ice begins to form on the water surface. This is indicated by a negative water surface temperature. The negative water surface temperature is then converted to equivalent ice thickness and equivalent heat is added to the heat source and sink term for water. The thickness of ice formation is calculated as

Twnρwcpwh ρiLf

θ0 = −

(5.22) where,

θ0 is the thickness of initial ice formation during a time step (m), Twn is the local temporary negative water temperature (◦C), h is the layer thickness (m),

ρw is the density of water (kg/m3), cpw is the specific heat of water (J/kg/◦C), ρi is the density of ice (kg/m3), and Lf is the latent heat of fusion (J/kg).

###### 67



<<<PAGE 81>>>

###### 5. TEMPERATURE AND HEAT TRANSFER EFDC+ Theory



- 5.4.2 Ice Surface Temperature The ice surface temperature is given by the equations:

Tsn =

θn−1 Ki

[Hsnn +Hann −Hbr (Tsn)−Hc(Tsn)] (5.23)

Hsn +Han −Hbr −He −Hc +qi = ρiLf

dθai dt

, for Ts = 0◦C (5.24)

qi = Ki

Tf −Ts(t) θ(t)

(5.25) where,

Ki is the thermal conductivity of ice (W/m/◦C), Tf is the freezing point temperature (◦C), n is the time level, qi is the heat flux through ice (W/m2), Hn is the net rate of heat exchange across the water surface (W/m2), Hs is the incident short wave solar radiation (W/m2), Ha is the incident long wave radiation (W/m2), Hsr is the reflected short wave solar radiation (W/m2), Har is the reflected long wave radiation (W/m2), Hbr is the back radiation from the water surface (W/m2), He is the evaporative heat loss (W/m2), and Hc is the heat conduction (W/m2).

- 5.4.3 Freezing Temperature The freezing temperature relationship is described as below:


where,

Tf = −0.0545 TDS , TDS < 35 ppt −0.3146−0.0417 TDS−0.000166 TDS2 , TDS > 35 ppt

Tf is the freezing point temperature (◦C), and TDS is the total dissolved solids (ppt).

(5.26)

###### 68



<<<PAGE 82>>>

###### 5. TEMPERATURE AND HEAT TRANSFER EFDC+ Theory



- 5.4.4 Ice Melt at Air/Water Interface The ice melt at the air/water interface is described by the equation below:

ρicpi

Ts(t) 2

θ(t) = ρiLf∆θai (5.27) where,

cpi is the specific heat of ice (J/kg/◦C), and θai is the ice melt at the air-ice interface (1/m).

- 5.4.5 Ice Growth/Melt at Bottom of Ice The ice growth/melt at the bottom of the ice is described by the equation below:

qi −qiw = ρiLf

dθiw dt

(5.28) where,

qi is the heat flux through the ice (W/m2), qiw is the heat flux at the ice/water interface (W/m2), and θiw is the ice growth/melt at the ice-water interface.

∆θiwn =

1 ρiLf

Ki

Tf −Tsn θn−1 −hwi(Twn −Tf) (5.29)

- 5.4.6 Solar Radiation at Bottom of Ice Solar radiation at the bottom of the ice is given by the equation below:


Hps = Hs(1−αi)(1−βi)exp[−γiθ(t)] (5.30) where,

Hps is the solar radiation at the ice-water interface (W/m2), Hs is the incident solar radiation (W/m2), αi is the ice albedo, βi is the fraction of the incoming solar radiation absorbed in the ice surface, and γi is the ice extinction coefficient (1/m).

###### 69



<<<PAGE 83>>>

###### 5. TEMPERATURE AND HEAT TRANSFER EFDC+ Theory



##### 5.5. Water Volume Evaporative Losses

Although the Heat flux due to evaporation is included for the Full Heat and the Equilibrium Temperature (W2) option, it does not calculate the volume of water lost from the waterbody due to the evaporation process. User may choose to not calculate evaporative losses or use the input evaporation data to calculate these losses.

User may select other options including EFDC original approach where the latent heat estimated using the full heat balance is used to calculate evaporation and consequently water volume loss due to evaporation. EFDC+, however allows the user to have a different turbulent exchange coefficient for evaporation. The water depth change due to evaporation can be calculated as

where,

∆z = E∆t =

HE ρLE

∆t (5.31)

HE is the latent heat flux due to evaporation (W/m2), ρ is the water density (kg/m3),

LE is the latent heat of water (J/kg), E is the evaporation rate (m/s),

∆t is the time interval (s) and ∆z is the water depth change over the period ∆t

For evaporation, the latent heat flux may also be estimated using the empirical formula proposed by Edinger

- et al. (1974), as


HE = f(W)(es −ea) (5.32)

where, f(W) is the wind speed function, es is the saturated vapor pressure at water surface temperature (mbar), and ea is the actual vapor pressure in the overlying air.

The wind speed function has the general form,

f(W) = a+bW +cW2 (5.33) where,

a, b, c are the wind coefficients (Table 5.2), and W is the windspeed in m/s.

The value of the coefficients is a function of the method selected for evaporative loss (Table 5.2).

###### 70



<<<PAGE 84>>>

###### 5. TEMPERATURE AND HEAT TRANSFER EFDC+ Theory



Table 5.2. List of Evaporation Calculation Methods

IEAVAP Evaporation Approach General Usage a b c

- 0 Do Not Include Evaporation
- 1 Use Evaporation from ASER Measured or Externally Estimated
- 2 EFDC Original
- 3 Ward (1980) Cooling Lake 0.0 3.534 0.0
- 4 Harbeck Jr (1964) Cooling Lake 0.0 3.818 0.0
- 5 Brady et al. (1969) Cooling Pond 6.442 0.0 0.322
- 6 Anderson et al. (1954) Large Lake 0.0 2.403 0.0
- 7 Webster and Sherman (1995) Lakes 2.717 2.743 0.0
- 8 Fulford and Sturm (1984) Rivers 8.359 2.090 0.0
- 9 Gulliver and Stefan (1984) Streams 7.732 1.672 0.0
- 10 Edinger et al. (1974) Lakes/Rivers 6.9 0.0 0.345


###### 71



<<<PAGE 85>>>

# Chapter 6 SEDIMENT TRANSPORT

##### 6.1. Introduction

EFDC+ supports two separate options for sediment transport computation:

- 1. EFDC Sediment Transport module based on Hamrick’s work (Tetra Tech, 2007b).
- 2. SEDZLJ Sediment Transport module that came from SNL-EFDC (Jones and Lick, 2000; Thanh et al., 2008; Ziegler and Lick, 1988, 1986).


Both approaches compute the suspended sediment transport in the water column in the same way. Still, they present distinct differences in (1) how they treat cohesive sediment and non-cohesive sediment and (2) how they compute sediment mass exchange between the water column and sediment bed. The EFDC Sediment Transport module applies separate computation processes for cohesive and non-cohesive sediments (see Figure 6.1); this method simulates the erosion process using a user-defined constant erosion rate parameter of each sediment class. The SEDZLJ Sediment Transport module uses a unified treatment for multiple sediment classes regardless of cohesiveness (see Figure 6.2); this approach can apply spatially-varied erosion properties by using site-specific erosion rate data acquired from the SEDFlume apparatus. Both sediment transport modules are dynamically linked to the hydrodynamics module. Therefore, EFDC+ can implement direct geomorphic feedback between flow field and sediment bed changes in a simulation. This chapter presents the theoretical basis for the sediment transport computation in EFDC+.

- 6.2. Suspended Sediment Transport


- 6.2.1 Governing Equations for Suspended Sediment Transport


The transport equation for the suspended sediments in the water column follows the generic transport equation (3.1) for a dissolved or suspended material. For the EFDC+ implementation, the physical horizontal diffusion terms in equation (3.1) are omitted due to the small inherent numerical diffusion encountered. This yields the following form of the suspended sediment transport equation:

###### 72



<<<PAGE 86>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



Dynamics

Hydrodynamic Model

Original Sediment Transport Module

Morphological Feedback

Non-cohesive #1 Non-cohesive #2 Non-cohesive #3

- Cohesive #1
- Cohesive #2


###### ...

...

Water Column Sediment Bed

Fig. 6.1. Structure of the EFDC Sediment Transport Model.

|SEDZLJ Sediment Transport Module<br><br>User Defined Sediment Class #1<br>User Defined Sediment Class #2<br>User Defined Sediment Class #3<br><br><br>...<br><br>Dynamics<br><br>Morphological Feedback<br><br>Hydrodynamic<br><br>Model<br><br>Water Column Sediment Bed<br><br>Fig. 6.2. Structure of the SEDZLJ Sediment Transport Model.|
|---|


###### 73



<<<PAGE 87>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



∂ ∂t

(mxmyHCj)+

where

∂ ∂x

(myHuCj)+

∂ ∂y

(mxHvCj)+

∂ ∂z

(mxmywCj)−

∂ ∂z

=

∂ ∂z

(mxmyws,jCj)

∂ ∂z

mxmy H

Cj +SsE,j +SsI,j (6.1)

Ab

x, y are the orthogonal curvilinear coordinates in the horizontal direction (m), z is the sigma coordinate (dimensionless),

- t is time (s), mx, my are the square roots of the diagonal components of the metric tensor (dimensionless), Cj is the concentration of sediment class j in the water column (g/m3), H is the total water column depth (m),
- u, v are the horizontal velocity components in the curvilinear coordinates (m/s), w is the vertical velocity component (m/s), ws,j is a settling velocity of suspended sediment class j (m/s), Ab is the vertical turbulent eddy diffusivity (m2/s), SsE,j is the external source-sink term of sediment class j (g/m2/s), and SsI,j is the internal source-sink term of sediment class j (g/m2/s).


The source-sink term has been split into two terms: the external term would include point and non-point source loads, and the internal term could include reactive decay of organic sediments or mass exchange between sediment classes if floc formation and destruction are simulated.

The boundary conditions in the vertical direction for equation (6.1) are:

∂ ∂z

Ab H

Cj −ws,jCj = Jo,j at z = 0 (6.2)

−

∂ ∂z

Ab H

Cj −ws,jCj = 0 at z = 1 (6.3)

−

where Jo,j is the net exchange flux of sediment class j (g/m2/s) between the water column-sediment bed, defined as positive into the water column.

##### 6.2.2 Numerical Solution

The general procedure follows that for the salinity transport equation, which uses a high order upwind difference discretization scheme for the advective terms, described in Hamrick (1992). The numerical solution of equation (6.1) utilizes a fractional step procedure.

###### 74



<<<PAGE 88>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



The first step advances the concentration due to advection and external sources and sinks having corresponding volume fluxes by:

∆t mxmy

Hn+1C∗ = HnCn +

−

1 2

SsE n+

∆t mxmy

∂ ∂x

∂ ∂y

1 2Cn +

my(Hu)n+

∂ ∂z

- 1

- 2Cn +


mx(Hv)n+

- 1

- 2Cn (6.4)


mxmywn+

where the superscripts n and n+1 denote the old and new time levels, and the superscript ∗ denotes the intermediate fractional step results. Note that the sediment class subscript j has been dropped to simplify the equation. The source and sink term portion, associated with volumetric sources and sinks, is included in the advective step for consistency with the continuity constraint. This source-sink term, as well as the advective field (u, v, w,), is defined as an intermediate in time between the old and new time levels consistent with the temporal discretization of the continuity equation. The advection step uses the anti-diffusive Multidimensional Positive Definite Advection Transport Algorithm (MPDATA) scheme (Smolarkiewicz and Clark, 1986) with optional flux corrected transport (Smolarkiewicz and Grabowski, 1990).

The second fractional step, or settling step, is given by:

∆t Hn+1

C∗∗ = C∗ +

∂ ∂z

(wsC∗∗) (6.5)

, which is solved by a fully implicit upwind difference scheme as below:

where

Ck∗∗ = Ck∗ +

∆t ∆zHn+1

CKC∗∗ = CKC∗ +

(wsC∗∗)KC (6.6)

∆t ∆kHn+1

∆t ∆1Hn+1

(wsC∗∗)k+1 −

(wsC∗∗)k for 2 ≤ k ≤ KC−1 (6.7)

∆t ∆zHn+1

C1∗∗ = C1∗ +

(wsC∗∗)2 (6.8)

k is the water column layer index, KC is the maximum number of water column layers, CKC is the top layer concentration (g/m3), Ck is the concentration in each layer k (g/m3), and C1 is the bottom layer concentration (g/m3).

For the second fractional step, the solution starts at the top layer (k = KC) and marches down to the bottom layer (k = 1). The implicit solution includes an optional anti-diffusion correction across internal water column layer interfaces.

###### 75



<<<PAGE 89>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



The third fractional step accounts for water column-sediment bed exchange by resuspension and deposition as follows:

∆t ∆zHn+1

LoJo∗∗∗ (6.9)

C1∗∗∗ = C1∗∗ +

where Lo is a flux limiter (dimensionless) such that only the current top layer of the sediment bed can be completely resuspended in a single time step.

For resuspension and deposition of suspended non-cohesive sediment, the bed flux is given by:

J0∗∗∗ = ws(Ceq −C1∗∗∗) (6.10)

where Ceq is the equilibrium concentration (g/m3) with respect to hydrodynamic and sediment physical parameters.

For cohesive sediment resuspension, the bed flux is specified as a function of the bed shear stress and bed geomechanical properties. For cohesive sediment deposition, the bed flux is typically given by:

J0∗∗∗ = −PdwsC1∗∗∗ (6.11)

where Pd is a probability of deposition. The representation of the water column-sediment bed exchange by a distinct fractional step is equivalent to a splitting of the bottom boundary condition equation (6.2) such that the bed flux is imposed at the intermediate step between settling and vertical diffusion.

The remaining step is an implicit vertical turbulent diffusion step corresponding to:

∂ ∂z

Cn+1 = C∗∗∗ +∆t

Ab H2

n+1 ∂ ∂z

Cn+1 (6.12)

with zero diffusive fluxes at the bed and water surface.

###### 76



<<<PAGE 90>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



##### 6.3. EFDC Sediment Transport Module

The implementation of EFDC Sediment Transport module applies separate computation processes for noncohesive and cohesive sediments. The conceptual framework of the sediment transport processes is illustrated in Figure 6.3.

Fig. 6.3. Conceptual Framework for EFDC Sediment Transport Module.

##### 6.3.1 Non-Cohesive Sediment

##### 6.3.1.1 Settling Velocity

Non-cohesive inorganic sediments settle as discrete particles under low sediment concentration conditions, with hindered settling and multi-phase interactions becoming important in regions of high sediment concentrations near the bed. At low sediment concentrations, the settling velocity for the non-cohesive sediment class j corresponds to the settling velocity of a discrete particle as:

wsj = wsoj (6.13)

###### 77



<<<PAGE 91>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



where, wsoj is the discrete particle settling velocity (m/s) that depends on the sediment particle density ρs, effective grain diameter, and fluid kinematic viscosity ν. A piece-wise relation for wsoj by van Rijn (1984) is as follows:

 

Rd j 18 , d ≤ 100 µm 10 Rd j 1+0.01R2d j −1 , 100µm < dj ≤ 1000 µm

wsoj = g′dj



1.1 , dj > 1000µm

where g′ is the reduced gravitational acceleration presented as:

(6.14)

g′ = g

ρsj ρw −1 (6.15)

and Rd j is the sediment grain densimetric Reynolds number calculated as:

dj g′dj ν

Rd j =

(6.16)

At higher concentrations and hindering settling conditions, the settling velocity is less than the discrete velocity and can be expressed in the form:

I

Ci ρsi

### ∑

wsj = 1−

i

n

wsoj (6.17)

where ρs is the sediment particle density with values of n ranging from 2 to 4 (van Rijn, 1984). The expression (6.14) is approximated to within 5 percent by:

I

Ci ρsi

### ∑

wsj = 1−n

i

wsoj (6.18)

for total sediment concentrations up to 200,000 mg/l. For total sediment concentrations less than 25,000 mg/l, neglecting the hindered settling correction results in less than a 5% error in the settling velocity, which is well within the range of uncertainty in parameters used to estimate the discrete particle settling velocity.

##### 6.3.1.2 Critical Thresholds of Transport and Erosion

In the EFDC Sediment Transport module, the preceding set of rules is used to determine the mode of transport of multiple-size classes of non-cohesive sediment. Non-cohesive sediment is transported as bedload and suspended load. The initiation of both transport modes begins with erosion or resuspension of sediments from the bed when the bed stress τb exceeds a critical stress referred to as the Shield’s stress τcs. The Shield’s stress τcs depends upon the density and diameter of the sediment particles and the kinematic viscosity of the fluid and can be expressed in empirical dimensionless relationships of the form:

u2∗csj g′dj

τcsj g′dj

θcsj =

= f Rd j (6.19)

=

###### 78



<<<PAGE 92>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



Useful numerical expressions of the relationship of equation (6.19), provided by van Rijn (1984) are:

θcsj =



0.24 R2d j/3

0.14 R2d j/3



0.04 R2d j/3

−1

−0.64

−0.1

0.013 R2d j/3

0.29

for R2d j/3 < 4

for 4 ≤ R2d j/3 < 10

for 10 ≤ R2d j/3 < 20

for 20 ≤ R2d j/3 < 150

(6.20)



0.055 for 150 ≤ R2d j/3

Several approaches have been used to distinguish whether a particular sediment size class is transported as bedload or suspended load under specific local flow conditions characterized by bed shear velocity u∗:

u∗ = √τb (6.21)

The approach proposed by van Rijn (1984) is used in the EFDC Sediment Transport module and is as follows. When the bed shear velocity is less than the critical shear velocity u∗csj for sediment class j:

u∗csj = √τcsj = g′djθcsj (6.22)

no erosion or resuspension takes place, and there is no bedload transport. Sediment in suspension in the water column under this condition will deposit to the sediment bed.

When the bed shear velocity exceeds the critical shear velocity but remains less than the settling velocity:

u∗csj < u∗ < wsoj (6.23)

sediment will be eroded from the bed and transported as bedload. Sediment in suspension in the water column under this condition will deposit to the bed. When the bed shear velocity exceeds both the critical shear velocity and the settling velocity, bedload transport ceases, and the eroded or resuspended sediments will be transported as a suspended load. These various transport modes are further illustrated by reference to Figure 6.4, which shows dimensional forms of the settling velocity relationship equation (6.14), and the critical Shield’s shear velocity equation (6.22) determined using equation (6.20) for sediment with a specific gravity of 2.65.

For grain diameters less than 1.3×10−4 m (130 µm), the settling velocity is less than the critical shear velocity. So, when the bed shear velocity exceeds the critical shear velocity, the sediments will be resuspended from the bed and transported entirely as a suspended load. For grain diameters greater than 1.3×10−4 m, eroded sediment can be transported by bedload in the region corresponding to equation (6.23) and then as a suspended load when the bed shear velocity exceeds the settling velocity.

###### 79



<<<PAGE 93>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



Fig. 6.4. Critical Shield’s shear velocity and settling velocity as a function of sediment grain size.

- 6.3.1.3 Bedload Bedload transport is determined using a general bedload transport rate formula:


qB ρsd√g′d

= Φ(θ,θcs) (6.24)

where qB is the bedload transport rate (mass per unit time per unit width) in the direction of the near bottom horizontal flow velocity vector. The function Φ depends on the Shield’s parameter θ:

u2∗ g′dj

τb g′dj

θ =

=

and the critical Shield’s parameter θcs defined by the equations (6.19) and (6.20).

(6.25)

###### 80



<<<PAGE 94>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



In EFDC+, bedload transport formulations have the general form, which conforms to equation (6.25):

Φ(θ,θcs) = φ (θ −θcs)α

√θ −γ θcs

β

(6.26)

The bedload transport parameter φ is specified as a function of the critical Shield’s parameter θcs and/or grain densimetric Reynolds number Rd following van Rijn (1984) formulation:

0.053 R1d/5θcs2.1

φ =

(6.27)

The bedload constants α, β, and γ are treated as user-defined parameters, which can be specified following the literature listed below.

van Rijn (1984) formulation:

Φ = φ (θ −θcs)2.1 (6.28) Engelund and Hansen (1967) formulation:

Φ = φ (θ)2.1

###### √θ

β

(6.29)

Meyer-Peter and M¨uller (1948) formulation:

Φ = φ (θ −θcs)1.5 (6.30) Bagnold (1956) formulation:

Wu et al. (2000) formulation:

Φ = φ (θ −θcs)

√θ (6.31)

Φ = φ (θ −θcs)2.2 (6.32)

Additionally, there are also other bedload formulations that were developed for riverine prediction (Ackers and White, 1973; Laursen, 1958; Yang, 1973; Yang and Molinas, 1982); however, they do not readily conform to equation (6.25) so those approaches are not incorporated in the EFDC+ model.

The procedure for coupling bedload transport with the sediment bed in the EFDC+ model is as follows. First, the magnitude of the bedload mass flux per unit width is calculated according to equation (6.25) at horizontal model cell centers, denoted by the subscript C. The cell center flux is then transformed into cell center vector components using:

u √u2 +v2

qbc qbcy =

qbcx =

v √u2 +v2

qbc

(6.33)

###### 81



<<<PAGE 95>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



where u and v are the cell center horizontal velocities near the bed. Cell face mass fluxes are determined by downwind projection of the cell center fluxes

qbfx = (qbcx)upwind qbfy = qbcy upwind

(6.34)

where the subscript upwind denotes the cell center upwind of the x normal and y normal cell faces. The net removal or accumulation rate of sediment material from the deposited bed underlying a water cell is then given by:

mxmyJb = myqbfx e − myqbfx w + mxqbfy n − mxqbfy s (6.35) where,

Jb is the net removal rate (gm/m2 −sec) from the bed, mx and my are x and y dimensions of the cell, and e,w,n,s represent the compass direction subscripts, which define the four cell faces.

The implementation of equations (6.33) through (6.35) in the EFDC+ includes logic to limit the out fluxes equation (6.34) over a time step, such that the time-integrated mass flux from the bed does not exceed bed sediment available for erosion or resuspension.

##### 6.3.1.4 Suspended Load

Under conditions when the bed shear velocity exceeds the settling velocity and critical Shield’s shear velocity, non-cohesive sediment will be resuspended and transported as a suspended load in the water column. When the bed shear velocity falls below both the settling velocity and the critical Shield’s shear velocity, suspended sediments in the water column will deposit into the bed.

A consistent formulation of these processes is developed using the concept of a near-bed equilibrium sediment concentration. Under steady, uniform flow and sediment loading conditions, an equilibrium distribution of sediment in the water column tends to be established, with the resuspension and deposition fluxes canceling each other. Using a number of simplifying assumptions, the equilibrium sediment concentration distribution in the water column can be expressed analytically in terms of the near bed reference or equilibrium concentration, the settling velocity, and the vertical turbulent diffusivity. For unsteady or spatially varying flow conditions, the water column sediment concentration distribution varies in space and time in response to sediment load variations, changes in hydrodynamic transport, and associated nonzero fluxes across the water column-sediment bed interface. An increase or decrease in the bed stress and the intensity of vertical turbulent mixing will result in net erosion or deposition, respectively, at a particular location or time.

To illustrate how an appropriate suspended non-cohesive sediment bed flux boundary condition can be established, consider the approximation to the sediment transport equation (6.1) for nearly uniform horizontal conditions:

∂ ∂t

∂ ∂z

(HC) =

∂C ∂z

Ab H

+wzC (6.36)

###### 82



<<<PAGE 96>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



Integrating equation (6.36) over the depth of the bottom hydrodynamic model layer gives:

∂ ∂t

∆HC¯ = J0 −J∆ (6.37)

where the overbar denotes the mean over the dimensionless layer thickness ∆. Subtracting equation (6.37) from equation (6.36) gives:

∂ ∂t

∂ ∂z

HC′ =

∂C ∂z

Ab H

+wzC −

J0 −J∆ ∆

(6.38)

By assuming that the rate of change of the deviation of the sediment concentration from the mean is small,

∂ ∂t

∂ ∂t

HC′ <<

HC¯ (6.39)

equation (6.38) can be approximated by:

∂ ∂z

Integrating equation (6.40) once gives:

∂C ∂z

Ab H

+wzC =

J0 −J∆ ∆

(6.40)

∂C ∂z

z ∆ −J0 (6.41)

Ab H

+wzC = (J0 −J∆)

Very near the bed, equation (6.41) can be approximated by:

∂C ∂z

Ab H

+wzC = −J0 (6.42)

Neglecting stratification effects and using the results of Section 5.1.1, the near-bed diffusivity is approximately:

l H

Ab H

∼= u∗κz (6.43) Integrating equation (6.43) into (6.42) gives:

= Koq

∂C ∂z

+

where R is the Rouse parameter calculated as:

The solution of equation (6.44) is:

R z

R z

Jo ws

C = −

ws u∗κ

R =

(6.44)

(6.45)

###### 83



<<<PAGE 97>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



Jo ws

C0 zR

C = −

+

(6.46)

The constant of integration is evaluated by setting the near-bed sediment concentration to an equilibrium value, defined just above the bed under no net flux condition as:

C = Ceq at z = zeq and Jo = 0 (6.47) Using equation (6.47), equation (6.46) becomes

C =

zeq z

R

Jo ws

Ceq −

(6.48)

For non-equilibrium conditions, the net flux is given by evaluating equation (6.48) at the equilibrium level

Jo = ws(Ceq −Cne) (6.49)

where Cne is the actual concentration at the reference equilibrium level. Equation (6.49) clearly indicates that when the near bed sediment concentration is less than the equilibrium value, a net flux from the bed into the water column occurs. Likewise, when the concentration exceeds equilibrium, a net flux to the bed occurs. When Cne is greater than Ce, equation (6.49) can be rewritten as:

Ceq Cne

Jo = −wsCne 1−

(6.50)

and the term inside the parenthesis in the equation (6.50) can be considered as the deposition factor, which does not exceed unity.

For the relationship equation (6.49) to be useful in a three-dimensional numerical model, the bed flux must be expressed in terms of the model layer mean concentration as:

Jo = ws C ¯eq −C¯ (6.51) where

ln ∆z−1

eq ∆z−1

C¯eq =

Ceq , R = 1

eq −1

1−R −1 (1−R) ∆z−1

∆z−1

eq

C¯eq =

Ceq , R ̸= 1

eq −1

(6.52)

, which defines an equivalent layer’s mean equilibrium concentration in terms of the near-bed equilibrium concentration. The corresponding quantities in the numerical solution for bottom boundary condition equation (6.9) are:

###### 84



<<<PAGE 98>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



wrCr =wsC¯eq Pdws =ws

(6.53)

If the dimensionless equilibrium elevation, zeq exceeds the dimensionless layer thickness, equation (6.33) can be modified to:

ln M∆z−1

eq M∆z−1

C¯eq =

Ceq , R = 1

eq −1

1−R −1 (1−R) M∆z−1

M∆z−1

eq

C¯eq =

Ceq , R ̸= 1

eq −1

(6.54)

where the over bars in equations (6.51) and (6.53) implying a concentration average of the first M layers above the bed.

For two-dimensional depth-averaged model application, a number of additional considerations are necessary. For depth average modeling, the equivalent of equation (6.41) is:

∂C ∂z

Ab H

+wsC = −Jo(1−z) (6.55)

Neglecting stratification effects and using the results of the sediment boundary layers, the diffusivity is:

Ab H

1 H

∼= u∗κz(1−z)λ (6.56) Integrating equation (6.56) into equation (6.55) gives:

= Koq

R(1−z)1−λ z

∂C ∂z

R z(1−z)λ

Jo ws

C = −

(6.57)

+

A closed form solution of equation (6.57) is possible for λ equal to zero. Although the resulting diffusivity is not as reasonable as the choice of λ equal to one, the resulting vertical distribution of sediment is much more sensitive to the near-bed diffusivity distribution than the distribution in the upper portions of the water column. For λ equal to zero, the solution of equation (6.57) is:

Rz (1+R)

C = − 1−

Jo ws

C0 zR

+

Evaluating the constant of integration using equation (6.56) gives:

(6.58)

C =

zeq z

R

Rz (1+R)

Ceq − 1−

Jo ws

(6.59)

For non-equilibrium conditions, the net flux is given by evaluating equation (6.59) at the equilibrium level:

###### 85



<<<PAGE 99>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



1+R 1+R(1−zeq)

Jo = ws

(Ceq −Cne) (6.60)

where Cne is the actual concentration at the reference equilibrium level. Since zeq is on the order of the sediment grain diameter divided by the depth of the water column, equation (6.60) is essentially equivalent to equation (6.49). To obtain an expression for the bed flux in terms of the depth average sediment concentration, equation (6.59) is integrated over the depth to give

2(1+R) 2+R(1−zeq)

C ¯eq −C¯ (6.61) where

Jo = ws

ln z−1

eq z−1

C¯eq =

Ceq, R = 1

eq −1

zR−1

eq −1 (1−R) z−1

C¯eq =

Ceq, R ̸= 1

eq −1

(6.62)

The corresponding quantities in the numerical solution bottom boundary condition equation (6.9) are

wrsr = ws

Pdws =

2(1+R) 2+R(1−zeq)

2(1+R) 2+R(1−zeq)

C ¯eq

ws

(6.63)

When multiple sediment size classes are simulated, the equilibrium concentrations given by equations (6.52), (6.54), and (6.62) are adjusted by multiplying by their respective sediment volume fractions in the surface layer of the bed.

The specification of the water column-bed flux of non-cohesive sediment has been reduced to the specification of the near-bed equilibrium concentration and its corresponding reference distance above the bed. Garcia and Parker (1991) evaluated seven relationships, derived by combinations of analysis and experiment correlation, for determining the near bed equilibrium concentration as well as proposing a new relationship. All of the relationships essentially specify the equilibrium concentration in terms of hydrodynamic and sediment physical parameters

Ceq = Ceq(d,ρs,ρw,ws,u∗,v) (6.64)

including the sediment particle diameter, the sediment and water densities, the sediment settling velocity, the bed shear velocity, and the kinematic molecular viscosity of water. Garcia and Parker concluded that the representations of Smith and McLean (1977) and van Rijn (1984), as well as their own proposed representation, perform acceptably when tested against experimental and field observations.

Smith and McLean (1977) formula for the equilibrium concentration, which requires the critical Shields stress to be specified for each sediment size class, as:

###### 86



<<<PAGE 100>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



0.65γoT 1+γoT

Ceq = ρs

where γo is a constant equal to 2.4×10−3 and T is given by

where

τb −τcs τcs

T =

u2∗ −u2∗cs u2∗cs

=

τb is the bed stress, and τcs is the critical Shields stress.

van Rijn (1984) formula is

(6.65)

(6.66)

where

Ceq = 0.015ρs

d z∗eq

T3/2R−d 1/5 (6.67)

z∗eq = Hzeq is the dimensional reference height, and Rd is a sediment grain Reynolds number.

When van Rijn’s formula is selected for use in EFDC+, the critical Shields stress is internally calculated using relationships from van Rijn (1984), which suggests setting the dimensional reference height to threegrain diameters. In the EFDC+ model, the user specifies the reference height as a multiple of the largest non-cohesive sediment size class diameter.

Garcia and Parker (1991) general formula for multiple sediment size classes is

A(λZj)5 1+3.33A(λZ)5

Cjeq = ρs

(6.68)

u∗ wsj

R3d j/5FH (6.69)

Zj =

where

FH =

σφ σφo

λ = 1+

dj d50

1/5

(6.70)

(λo −1) (6.71)

A is a constant equal to 1.3×10−7, d50 is the median grain diameter based on all sediment classes,

###### 87



<<<PAGE 101>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



λ is a straining factor, FH is a hiding factor, and σø is the standard deviation of the sedimentological phi scale of sediment size distribution.

Garcia and Parker (1991) formulation is unique in that it can account for armoring effects when multiple sediment classes are simulated. For the simulation of a single non-cohesive size class, the straining factor and the hiding factor are set to one. EFDC+ has the option to simulate armoring with Garcia and Parker’s formulation. For armoring simulation, the current surface layer of the sediment bed is restricted to a thickness equal to the dimensional reference height.

##### 6.3.2 Cohesive Sediments

##### 6.3.2.1 Settling Velocity

The settling of cohesive inorganic sediments and organic particulate materials is an extremely complex process. Inherent in the process of gravitational settling is the process of flocculation, where individual cohesive sediment particles and particulate organic particles aggregate to form larger groupings (or flocs) having settling characteristics significantly different from those of the component particles (Burban et al., 1989, 1990; Gibbs, 1985; Mehta et al., 1989). Floc formation is dependent upon the type and concentration of the suspended materials, the ionic characteristics of the environment, and the fluid shear and turbulence intensity of the flow environment. Progress has been made in first principles mathematical modeling of floc formation or aggregation and disaggregation by intense flow shear (Lick and Lick, 1988; Tsai et al., 1987). However, the computational cost of such approaches precludes direct simulation of flocculation in operational cohesive sediment transport models.

An alternative approach, which has been applied with reasonable success, is the parameterization of the settling velocity of flocs in terms of cohesive and organic material fundamental particle size d, concentration C, and flow characteristics such as vertical shear of the horizontal velocity du/dz, shear stress Avdu/sz, or turbulence intensity in the water column or near the sediment bed q. This implementation has allowed semi-empirical expressions with the functional form:

wse = wse d,C,

du dz

,q (6.72)

to be developed to represent the effective settling velocity. In EFDC+, the settling velocity of each cohesive sediment class is determined by either a user-defined constant or one of the approaches described below.

- 6.3.2.1.1 Option 1 Hwang and Mehta (1989) proposed the following:


aC′′ (C2 +b2)m

ws =

(6.73)

based on observations of settling at six sites in Lake Okeechobee. This equation has a general parabolic shape with the settling velocity decreasing with decreasing concentration at low concentrations and decreasing with increasing concentration at high concentrations. Least squares analysis for the parameters a, m, n,

###### 88



<<<PAGE 102>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



in equation (6.73) was shown to agree well with observational data. Equation (6.73) does not have a dependence on flow characteristics but is based on data from an energetic field condition having both currents and high-frequency surface waves.

##### 6.3.2.1.2 Option 2

The formulation given by Shrestha and Orlob (1996) and as subsequently modified by Mehta et al. (1989) has the form:

where

cws = Cα exp(−4.21+0.147G) (6.74) α = 1.11075+0.0386G (6.75)

G =

2

2

∂u ∂z

∂v ∂z

+

(6.76)

is the magnitude of the vertical shear of the horizontal velocity. It is noted that all of these formulations are based on specific dimensional units for input parameters and predicted settling velocities and that appropriate unit conversions are made internally in the implementation in the EFDC+ model.

##### 6.3.2.1.3 Option 3

Ziegler and Nisbet (1994, 1995) proposed a formulation to express the effective settling as a function of the floc diameter df

ws = adbf (6.77) with the floc diameter given by:

where

df =

αf C τxz2 +τyz2

(6.78)

C is the sediment concentration, αj is an experimentally determined constant, and τxz and τyz are the x and y components of the turbulent shear stress at a given position in the water

column.

Other quantities in equation (6.77) have been experimentally determined to fit the relationships:

a = B1 C τxz2 +τyz2

−0.85

(6.79)

###### 89



<<<PAGE 103>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



b = −0.8−0.5log C τxz2 +τyz2 −B2 (6.80)

where B1 and B2 are experimental constants.

- 6.3.2.1.4 Option 4 The generalized approach to computing settling velocities based on shear stress is as follows:


 

1.510×10−5(C′)0.45 , C′ < 40 8×10−5 , 40 ≤ C′ ≤ 400 0.893×10−6(C′)0.75 , C′ > 400

ws =

(6.81)



C′ = τC (6.82) where τ is shear stress (cm2/s2), and C is total cohesive concentration (g/m3).

##### 6.3.2.2 Deposition

Water column-sediment bed exchange of cohesive sediments and organic solids is controlled by the nearbed flow environment and the geomechanics of the deposited bed. Net deposition to the bed occurs as the flow-induced bed surface stress decreases. The most widely used expression for the depositional flux is:

where

Jod = −wsCd τcdτ−τb

= −wsPdCd , τb < τcd 0 , τb ≥ τcd

cd

(6.83)

τb is the stress exerted by the flow on the bed, τcd is a critical stress for deposition which depends on sediment material and floc physiochemical

properties (Mehta et al., 1989), and Cd is the near-bed depositing sediment concentration.

The probability of deposition Pd is based on the linear term, (τcd −τb)/τcd. The critical deposition stress is generally determined from laboratory or in situ field observations and values ranging from 0.06 to 1.1 N/m2 have been reported in the literature. Given this wide range of reported values, in the absence of site-specific data, the depositional stress is generally treated as a calibration parameter. The depositional critical stress is an input parameter for each cohesive sediment class in EFDC+.

###### 90



<<<PAGE 104>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



##### 6.3.2.3 Erosion

Cohesive bed erosion occurs in two distinct modes, mass erosion, and surface erosion. Mass erosion occurs rapidly when the bed stress exerted by the flow exceeds the depth-varying shear strength τs of the bed at a depth Hme below the bed surface. Surface erosion occurs gradually when the flow-exerted bed stress is less than the bed shear strength near the surface but greater than critical erosion stress τce, which is dependent on the shear strength and density of the bed. A typical scenario under conditions of accelerating flow and increasing bed stress would involve first the occurrence of gradual surface erosion, followed by a rapid interval of mass erosion, followed by another interval of surface erosion. Alternately, if the bed is well consolidated with a sufficiently high shear strength profile, only gradual surface erosion would occur.

Surface erosion is generally represented by relationships of the form:

α

τb −τce τce

dme dt

Jor = wrCr =

, τb ≥ τce (6.84) or

γ

τb −τce τce

dme dt

Jor = wrCr =

, τb ≥ τce (6.85) where,

exp −β

dme

dt is the surface erosion rate per unit surface area of the bed, τce is the critical stress for surface erosion or resuspension.

The critical erosion rate and stress and the parameters α, β, and γ are generally determined from laboratory or in situ field experimental observations. Equation (6.84) is more appropriate for consolidated beds, while (6.85) is appropriate for soft partially consolidated beds. The base erosion rate and the critical stress for erosion depend upon the type of sediment, the bed water content, total salt content, ionic species in the water, pH, and temperature (Mehta et al., 1989) and can be measured in laboratory and sea bed flumes.

Surface erosion rates ranging from 0.005 to 0.1 gs−1m−2 have been reported in the literature, and it is generally accepted that the surface erosion rate decreases with increasing bulk density. The critical erosion stress is related to but generally less than the shear strength of the bed, which in turn depends upon the sediment type and the state of consolidation of the bed. Experimentally determined relationships between the critical surface erosion stress and the dry density of the bed of the form

τce = cρsd (6.86)

have been presented (Mehta et al., 1989). EFDC+ allows a user-defined constant critical stress for surface erosion or the use of a computed τce based on one of the following options.

- 6.3.2.3.1 Option 1 Hwang and Mehta (1989) proposed the relationship


###### 91



<<<PAGE 105>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



a(ρb −ρl)b +c, ρb > 1.065 0, ρb ≤ 1.065

τce =

(6.87)

between the critical surface erosion stress and the bed bulk density with a = 0.883, b = 0.2, c = 0.05, and ρl = 1.065 for the stress in N/m2 and the bulk density in g/cm3.

- 6.3.2.3.2 Options 2 and 3 Sanford and Maa (2001) proposed the relationship

τce = τci

(1+εr) (1+εb)

(6.88)

where

τci is the critical shear stress normalized by water density (m2/s2), εr is the reference void ratio (dimensionless), and εb is the void ratio of the sediment bed (dimensionless).

The void ratio, ε is defined as the ratio of the volume of voids, φ to the total volume of the sediment (dimensionless).

ε =

φ 1−φ

(6.89)

For Option 2, εb is specified using the void ratio of the top sediment bed layer. Option 3 computes εb for the void ratio of the top sediment bed layer with cohesive sediment fraction.

- 6.3.2.3.3 Option 4


This option is governed by the relationship:

τce = τci (6.90) where τci is the critical shear stress normalized by water density (m2/s2).

##### 6.3.3 Consolidation of Mixed Cohesive and Non-Cohesive Sediment Beds

This section presents a methodology for representing the consolidation of sediment beds containing both cohesive and non-cohesive sediments. The methodology allows for both cohesive and non-cohesive sediment in any bed layer and is based on the following assumptions. First, it is assumed that during the consolidation step, a fraction of the bed pore water volume per unit horizontal area is associated with each sediment type or

εHbed 1+ε

= (ψwc +ψwn)Hbed (6.91) where,

###### 92



<<<PAGE 106>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



ε is the porosity of the sediment bed (dimensionless), Hbed is the bed thickness (m), ψ is the volume fraction of water with the subscripts, and wc and wn denote cohesive and non-cohesive sediment, respectively.

Likewise, the volume of sediment per unit horizontal area can be fractionally partitioned between cohesive and non-cohesive,

where,

Hbed 1+ε

= (ψsc +ψsn)Hbed (6.92)

sc and sn denote the cohesive and non-cohesive sediment for volume fractions, respectively.

Following the Lagrangian formulation of the previous section, the total volume of sediment and the fractional sediment volume in a bed layer remain constant during a consolidation step.

∂ ∂

∂ ∂

(Hbedψsn) = 0 (6.93) Fractional void ratios can also be defined

(Hbedψsc) =

ψwc ψsc

εc =

ψwn ψsn

εn =

and using equations (6.91) and (6.92), the void ratio of the mixture is

(6.94)

(6.95)

ψscεc +ψsnεn ψsc +ψsn

ε =

(6.96) which is the sediment volume-weighted average of the void ratios of the two sediment types.

The second assumption is that during the consolidation time step, the fraction of water associated with noncohesive sediment remains constant, as does the fractional void ratio. This is equivalent to assuming that the portion of the bed layer associated with non-cohesive sediment is incompressible and that the pore water associated with the non-cohesive sediment is specified by εn.

Consistent with the preceding assumptions, the thickness of the bed layer can be divided into cohesive and non-cohesive fractions Hbed,c and Hbed,n, respectively.

Hbed,c =(ψwc +ψsc)Hbed = (1+εc)ψscHbed Hbed,n =(ψwn +ψsn)Hbed = (1+εn)ψsnHbed

(6.97)

The hydraulic conductivity of the layer can be expressed by

###### 93



<<<PAGE 107>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



(Hbed,c +Hbed,n)

K =

Hbed,c

Kc + HKbed,n

n

(6.98)

which is equivalent to an infinite number of alternating infinitesimal cohesive and non-cohesive sublayers of proportional thickness comprising the mixed bed layer. Equation (6.98) can be written as

where,

K (1+ε)

1 fsc(1+Kεc)

=

+ fsn(1+Kεn)

c

n

(6.99)

ψsc (ψsc +ψsn)

fsc =

, and

ψsn (ψsc +ψsn)

fsn =

(6.100)

are the time-invariant total cohesive and non-cohesive sediment fractions in the bed layer. Likewise, equation (6.96) can be written as

ε = fscεc + fsnεn (6.101)

The final assumption for the mixed material consolidation formulation is that changes in effective stress are due entirely to changes in the cohesive void ratio. Under this assumption, the specific discharge can be written as

and

q = −

2λk+1 2

K

1+ε k+1 2

(∆k+1 +∆k)

(fscεc)k+1 −(fscεc)k +

K

1+ε k+1 2

ρ ¯s ρw −1

- 1

- 2


k+

(6.102)

σe,k+1 −σe,k (fscεc)k+1 −(fscεc)k

1 gρw

λk+1 2

= −

When the depositional void ratio is specified for the surface layer specific discharge becomes

(6.103)

qw:kt+ = −

2λkt+ ∆kt

K 1+ε kt+

(εc)dep −(εc)k +

ρ ¯s ρw −1

kt+

K 1+ε kt+

When the zero excess pore pressure boundary condition at the bed surface is used

(6.104)

qw:kt+ =

K 1+ε Kt

2 ∆Kt

λ∗ fscεcn+1 Kt

+

K 1+ε Kt

ρ ¯s ρw −1

−

Kt

K 1+ε Kt

2 ∆Kt

σen gρw

+λ∗ fscε∗

Kt

(6.105)

###### 94



<<<PAGE 108>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



The equation for updating the void ratio is modified using equation (6.101) to give

∆t 2

(fscεc)∗∗k = (fscεc)∗k +

1+ε Hbed

∗∗

(qw:k−qw:k+) (6.106)

k

Thus the mixed bed layer consolidation formulation essentially solves the space and time evolution of fscεc with the continuum constitutive relationship for λ given by

∂ ∂ε

σ gρw

1 fsc

λ = −

(6.107)

The formulation has the desirable characteristic of reducing to the well-established cohesive formulation in the absence of non-cohesive material. The solution for fscεc proceeds by introducing equations (6.92) and (6.94) or (6.95) into (6.96) and solving the resulting tri-diagonal system of equations. The new specific discharges are then directly calculated using equations (6.92) and (6.94) or (6.95) and used to update the layer thickness

Hbedn+1,k = Hbed∗ ,k +∆t (qw:k− −qw:k+) (6.108) The ratio Hbed/(1+ε) can then be updated

Hbed 1+ε

n+1

=

k

Hbed 1+ε

∗

k

Followed by the solution of equation (6.101) for the cohesive void ratio

ε − fsnεn fsc

εc =

(6.109)

(6.110)

##### 6.4. SEDZLJ Sediment Transport Module

The mathematical framework for the unified treatment of erosion, deposition, and bedload transport is referred to as the SEDZLJ model (Jones and Lick, 2000; Ziegler and Lick, 1988, 1986), which incorporates physical and erosion properties of sediment beds measured from an erosion rate measurement apparatus referred to as SEDFlume (Jones and Lick, 2001). EFDC+ incorporates the SEDZLJ module for sediment transport computation with significant enhancements for mass balance, hard bottom bypass, and computational efficiency. This section of the EFDC+ theory document provides the summary of the SEDZLJ’s theory (James et al., 2010; Jones and Lick, 2001; Thanh et al., 2008).

##### 6.4.1 Background

Most models are calibrated using hindcasting techniques which can have limitations when extending the simulation to future conditions. The most typically available sediment transport indicator measured in aquatic systems is the suspended sediment concentration. Unfortunately, many different combinations of erosion and deposition rates can be used to reach the same suspended sediment concentration. This can be illustrated as follows.

###### 95



<<<PAGE 109>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



In the steady state, an equilibrium exists between erosion and deposition. The deposition is generally described as D = PwsC where P is a probability of deposition, ws is the settling speed of the sediment particles, and C is the sediment concentration in the water. Equilibrium then gives

E −PwsC = 0 (6.111) This can be solved by the sediment concentration, which is

E Pws

C =

(6.112)

From this equation, it is seen that any suspended sediment concentration can be matched with an infinite number of erosion rates and deposition parameters by adjusting both accordingly. For example, the observed value of C can be obtained by high values of E and high values of Pws or by low values of E and low values of Pws. In other words, measurements of suspended sediment concentrations are not sufficient to determine erosion and/or deposition. Historically, erosion was constrained by theoretical relationships between shear stress and grain sizes, however, there is still a range of parameters that would produce the same suspended concentrations. In order to predict erosion and deposition accurately, these quantities should be determined

- as functions of sediment characteristics and hydrodynamic variables by means of experiments or theory based on experiments.


The SEDZLJ approach (Jones and Lick, 2000; Ziegler and Lick, 1988, 1986) incorporates the erosion rates directly measured from the sediment core samples using SEDFlume apparatus (Jones and Lick, 2001). The SEDFlume consists of a straight flume with an open bottom through which a rectangular cross-section core tube containing sediment can be inserted. The main components of the flume are the core tube and sediment, the test section, the inlet section for uniform, fully developed, turbulent flow, the flow exit section, the water storage tank, and the pump (which forces water through the system). A schematic of the SEDFlume is shown in Figure 6.5. Data produced from these tests produce erosion rates, critical shear stress, and bulk density by depth in a core.

###### 96



<<<PAGE 110>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



Fig. 6.5. Schematic of the SEDFlume Apparatus.

##### 6.4.2 Bed Shear Stress

In EFDC, the SEDZLJ module computes the bed shear stress τb (dynes/cm2) as:

τb = ρwcfV2 (6.113)

where ρw is the density of water (g/cm3) and V is the flow velocity magnitude (cm/s). The bottom shear stress friction factor cf (dimensionless) is calculated using a log-layer distribution of velocity as:

where

 

cf =



κ2 ln112zH

2 for H ≥ Hmin 0.0 for H < Hmin

b

κ is von Karman’s constant (κ=0.42), zb is bottom skin friction based on the d50 at the sediment surface (m), and Hmin is the minimum depth to allow shear computations (m).

(6.114)

The bottom skin friction is assumed to be equal to the average particle diameter of the surface of the sediment bed at any given location. Therefore, the bottom shear stress friction factor cf increases as the particle size

- at the sediment bed surface increases or as the depth of water decreases.


###### 97



<<<PAGE 111>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



##### 6.4.3 Erosion Rate

Results of a typical application of SEDFlume are shown in Figure 6.6, where erosion rates E in units of cm/s are plotted as a function of bed depth (cm) with shear stress τ (N/m2). Erosion rates are generally highest at the surface and decrease with depth; they also increase with shear stress. In general, information of this type for sediments throughout the system is necessary for accurate predictions of sediment transport (Jones and Lick, 2000). The availability of this type of data is assumed and is used in SEDZLJ.

Fig. 6.6. SEDFlume Data for Conowingo Reservoir (DNR Maryland).

Information on erosion rates is generally reported in units of cm/s. In order to convert this to a mass flux in units of g/cm2/s, which is needed in the modeling, the mass of solids within a sediment volume is needed. This quantity, for a sediment consisting of solids and water only (i.e., no gas), can be determined in terms of the bulk density of the sediments ρ as follows:

ρ = ρsxs +ρwxw = ρsxs +ρw(1−xs) (6.115)

###### 98



<<<PAGE 112>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



where

ρs is the density of solids (g/cm3),

xs is the volume fraction of the solids, ρw is the density of water (g/cm3), and xw is the volume fraction of water.

Since xw = 1 − xs, the mass of solids per unit volume is xsρs, which can be determined from the above equation as:

ρs(ρ −ρw) ρs −ρw

2.6 1.6

xsρs =

(ρ −1) (6.116)

=

where it is assumed that ρs = 2.6g/cm3 and ρw = 1.0 g/cm3. Once the bulk density of the sediments is known, the erosion rate in units of g/cm2/s can be determined by multiplying the erosion rate in units of cm/s by xsρs.

As indicated above, erosion rates change as a function of bed depth. This variation is incorporated into the sediment bed model through a discrete layering system where the erosion rate is defined at each layer interface, and the particle size distribution and bulk density are defined as constant throughout the layer. Any number and thickness of layers required to approximate the variation of sediment properties with depth can be introduced as necessitated by field data.

The SEDZLJ sediment transport model can incorporate erosion rate data collected in the field that are typically spatially discrete and at specific depths but can also be interpolated where no direct data are available. The total erosion rate is interpolated across sediment layer thicknesses and shear stresses. Linear interpolation is used to calculate an erosion rate at a specified shear stress τ as:

τi+1 −τ τi+1 −τi

τ −τi τi+1 −τi

E (τ) =

Ei +

Ei+1 (6.117)

where subscript i denotes data for a shear stress less than τ and i+1 denotes measured data for a shear stress greater than τ, with τi<τ<τi+1. Because E often changes rapidly with depth, the logarithmic interpolation between data points best represents erosion rates as a function of depth:

ln[E (T)] =

T0 −T T0

ln(E j)+

T T0

ln E j+1 (6.118)

where T is the actual sediment bed layer thickness, T0 is the initial bed layer thickness, and the superscripts j and j +1 denote data for the interface at the top and the bottom of the specific layer where the erosion rate is required, respectively. Equations (6.117) and (6.118) are combined so that the erosion rates may be calculated as a function of shear stress and depth.

###### 99



<<<PAGE 113>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



##### 6.4.3.1 Critical Shear Stress for Erosion

In addition to erosion rates, another parameter of significance in modeling is the critical stress for erosion, τce. Consider the flow of water over a sediment bed. As the rate of flow is increased starting from rest, there is a range of velocities (or shear stresses) at which the movement of the easiest-to-move particles (generally the smallest) is first noticeable to an observer. These eroded particles then travel a relatively short distance until they come to rest in a new location. This initial motion tends to occur only at a few isolated spots. As the flow velocity and shear stress increase further, more particles participate in this process of erosion, transport, and deposition, and the movement of the particles becomes more sustained.

Because of this gradual increase in sediment erosion as the shear stress increases, it is difficult to precisely define a critical velocity or critical shear stress at which sediment erosion is first initiated. More quantitatively and with less ambiguity, critical shear stress for erosion can be defined as the shear stress at which a small but accurately measurable rate of erosion occurs. Roberts et al. (1998) defined this rate as 10−6 m/s represented by approximately 1 mm of erosion in 15 minutes, though different rates have been used to define τce.

Critical shear stresses for erosion as a function of particle diameter d are shown in Figure 6.7. For d ¿ 200 µm, the sediments behave in a non-cohesive manner, i.e., they consolidate rapidly, and they erode particle by particle. For d ¡ 200 µm, cohesive effects between particles become significant. The sediments consolidate relatively slowly with time, and the critical stresses depend not only on particle diameter but also on the bulk density of the sediments. For these cohesive sediments, τce increases as d decreases and as bulk density increases.

For non-cohesive sediment beds, the curve of Shields (1936), or any approximation thereof van Rijn (1984) could be used to define the critical shear stress for erosion. Soulsby et al. (1997) approximated the critical shear for erosion as:

where

τce = ρgdθ = ρgd

0.3 1+1.2d∗

+0.055[1−exp(−0.02d∗) ] (6.119)

d∗ = d (ρsd/ρw−1)g/v2 1/3 (6.120)

g is the acceleration due to gravity, d is the sediment particle diameter, d∗ is the non-dimensional particle diameter, v is the kinematic fluid viscosity, and θ is the critical Shields parameter, represented by the algebraic fit shown in the parenthesis in equa-

tion (6.119)

###### 100



<<<PAGE 114>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



Fig. 6.7. Critical Shear Stresses for Erosion and Suspension of Quartz Particles.

##### 6.4.3.2 Erosion into Suspended Load versus Bedload

As bottom sediments are eroded, a fraction of the sediments are suspended into the overlying water and are transported as suspended loads; the rest of the eroded sediments move by rolling and/or sliding in a thin layer near the bed in what is called bedload. The fraction in each of the transport modes depends on the particle size and shear stress.

For fine-grained particles (which are generally cohesive), erosion occurs both as individual particles and in the form of chunks or small aggregates of particles. The individual particles move as a suspended load. The aggregates tend to move downstream near the bed but generally seem to disintegrate into small particles in the high-stress boundary layer near the bed as they move downstream. These disaggregated particles then move as suspended loads. For this reason, it is assumed that fine-grained sediments less than 200 µm are completely transported as suspended load.

Coarser, non-cohesive particles (defined here as those particles with diameters greater than about 200 µm) can be transported both as suspended load and bedload, with the fraction in each dependent on particle diameter and shear stress. For particles of a particular size, the shear stress at which the suspended load (or sediment suspension) is initiated is defined as τcs (N/m2). This shear stress τcs, can be defined from the van Rijn (1984) formulations as:

where

 

τcs =



2

4ws d∗

1 ρw

, for d ≤ 400 µm

ρw(0.4ws)2, for d > 400 µm

1

(6.121)

###### 101



<<<PAGE 115>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



1/3

d∗ is the non-dimensional particle diameter calculated from d∗ = d (ρsρ−ρ) νg2

where d is the particle diameter (cm), and

ws is the particle settling speed (cm/s)

For τb > τcs, sediments are transported both as bedload and suspended load with the fraction in suspended load f increasing with τb from f = 0 until f reaches 1. For τb greater than this, sediments are transported completely as suspended load.

In EFDC+, the settling speed of each sediment class is determined as a user-specified input parameter, which can be specified based on Cheng (1997) and van Rijn (1984). Cheng’s formula for settling speed is

v d

ws =

25+1.2d∗2 −5

1.5

(6.122)

where ν is the kinematic fluid viscosity (cm2/s).

Since Cheng’s formula is based on the observations of the settling of real sediment particles, it produces settling speeds lower than Stoke’s law. This is because real sediments are often irregular in shape and have a greater hydrodynamic resistance to settling than perfect spheres as in Stoke’s law.

van Rijn (1984) computes the settling velocity as

where

 

(s−1)gD2s

1 18

ν , Ds < 100µm 10Dν

0.5

3 s

1+ 0.01(s−1)gD

ws =

−1 , 100µm ≤ Ds < 1000µm 1.1[(s−1)gDs]0.5 , Ds ≥ 1000µm

ν2

s



(6.123)

Ds is the representative particle size (m), s is the specific density, g is the acceleration due to gravity (m/s2), and ν is the kinematic viscosity coefficient and ws is in m/s.

Guy et al. (1966) performed detailed flume measurements of suspended load and bedload transport for sediments ranging in median diameter d50, from 190 µm to 930 µm. They found that, as the ratio of shear velocity (defined as u∗ = τb/ρw) to settling velocity increases, the proportion of suspended load to total load transport, qs/qt increases. An approximation of their data can be made with the following function:

 

- 0, τb < τcs

ln(u∗/ws)−ln

√

τcs/ρw/ws ln(4)−ln

√

τcs/ρw/ws

, τb > τcs and u∗

ws < 4

- 1, u∗ ws > 4


- qs

- qt


(6.124)

=



###### 102



<<<PAGE 116>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



This approximation is used in the EFDC+ implementation. The original data is shown with the result given by the above equation in Figure 6.8.

Fig. 6.8. Results from Flume Measurements of Suspended Load and Bedload (Guy et al., 1966).

Although sediments in nature have a continuous size distribution, physical quantities in numerical models are inherently discrete; hence, sediment particle sizes are discretized. The discretization of particle size classes j is done by measuring the different sediment sizes in a site-specific sediment core and grouping them into appropriate size classes. The sediment bed in the model is described as the product of the particle size class and the corresponding mass fraction. By multiplying the total erosion flux of a particular size class j by qs/qt, the erosion flux of that class into suspended load Es,j can be calculated. The corresponding erosion flux into bedload Eb,j is also calculated by multiplying the total erosion flux of the size class by the factor (1−qs/qt). Thus, the erosion flux for any size class j is

Es,j =

0, τb < τce

- qs

- qt fjE , rτb ≥ τce


(6.125)

Eb,j =

0, τb < τce 1− qqst fjE, τb ≥ τce

where fj is the mass fraction of the jth sediment size class.

(6.126)

###### 103



<<<PAGE 117>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



##### 6.4.4 Suspended Load

For suspended sediments, the three-dimensional, time-dependent transport equation in the water over the bed is shown in equation (6.1). The net sediment flux into suspension Qs is calculated as the total erosion flux into suspended load Es,j minus the deposition flux from suspended load Ds,j for each sediment size class j:

Qs,j=Es,j−Ds,j (6.127) where

Qs=∑

Qs,j (6.128)

j

In a quiescent fluid where no shear stress is present, the deposition flux for suspended sediments can be described as the product of the settling speed of the sediment and the concentration of the sediment in the overlying water. However, in flowing water, the deposition is affected by the fluid turbulence, quantified as shear stress. In this case, a probability of deposition for each size class j, Pk can be included in the formulation to account for the effects of the shear stress to yield:

Dsj=PjwsjCsj (6.129)

This probability would be unity in the case of quiescent flow and decrease as the flow, turbulence, and shear stress increase. The probability for suspended load deposition seems to differ for cohesive and non-cohesive particle sizes. For cohesive particles (size classes with effective diameters less than 200 µm), Krone (1962) found that the probability of deposition varied approximately as:

Pj =

- 0 for τbτcs,j
- 1− ττcsb,j for τb > τcs,j


(6.130)

For larger non-cohesive particles (size classes with an effective diameter greater than 200 µm), Gessler (1967) showed that the probability of deposition could be described with a Gaussian distribution or error function given by:

where

Pj (Y)=erf

Y 2

2 √π

=

Y/2 0

exp −ξ2 dξ (6.131)

1 σ

Y=

τcs,j τb −1 (6.132)

where τcs,j is the critical shear stress for suspension for size class j and σ is the standard deviation for shear stress variation, which Gessler (1967) determined to be about 0.57.

An approximation to this function for Y > 0 with an error of less than 0.001 % is found to be (Abramowitz, 1964; Dwight, 1947):

###### 104



<<<PAGE 118>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



Pj= 1−F(Y)(0.4632X−0.1202X2+0.9373X3) (6.133) where

When Y < 0

1 (2π)1/2

e−12Y2 (6.134)

F (Y)=

1 (1+0.33267Y)

X=

(6.135)

Pj= 1−P(|Y|) (6.136)

Figure 6.9 shows sample probability distributions using the formulations for cohesive and non-cohesive particles.

Fig. 6.9. Sample Probability Distributions for Cohesive and Non-Cohesive Particles.

##### 6.4.5 Bedload

For the description of bedload transport, the van Rijn (1984) approach is used. To calculate the concentration of particles moving in bedload, a mass balance equation can be written as:

where

∂(mCb) ∂t

=

∂(mqbx) ∂x

+

∂(mqby) ∂y

+Qb (6.137)

###### 105



<<<PAGE 119>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



Cb is the bedload concentration (g/cm2), qb is the horizontal bedload flux in the x or y directions (g/s/cm), m is the cell area (cm2), and Qb is the net vertical flux of sediments between the sediment bed and bedload (g/s).

This equation is solved using a central difference approximation for the fluxes in the x and y directions. The horizontal bedload flux in general is calculated as

qb=ubCb (6.138)

where ub is the bedload velocity (cm/s) in the direction of interest. The bedload velocity and thickness can be calculated from van Rijn (1984) using formulations as follows:

ub= 1.5T0.6[(ρs−1)gd]0.5 (6.139)

hb=3dd∗0.6T0.9 (6.140) The transport parameter T is calculated as:

τb−τce τce

T=

(6.141)

The flux of sediments between the bottom sediments and bedload Qb is calculated as the erosion of sediments into bedload Eb minus the deposition of sediments from bedload Db and is

Qb=Eb−Db (6.142) where Db is given by:

Db=PwsCb (6.143)

In steady state equilibrium, the concentration of sediments in bedload, Ce is due to a dynamic equilibrium between erosion and deposition:

Eb=PwsCe (6.144) From this, the probability of deposition can be written as:

Eb wsCe

P=

(6.145)

The erosion rate can be determined from SEDFlume, while the settling speed can be calculated from equation (6.123). The equilibrium concentration Ce has been investigated by several authors; the formulation by van Rijn (1984) will be used here and is calculated as:

###### 106



<<<PAGE 120>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



ρsT d∗

(6.146)

Ce= 0.117

Once Eb, ws, and Ce are known as a function of particle diameter and shear stress, P can be calculated from equation (6.145). It is then assumed that this probability is also valid for the non-steady case so that the deposition rate can be calculated in this case.

The equilibrium concentration Ce is based on experiments with uniform sediments. In general, the sediment bed must be represented by more than one size class. In this case, the erosion rate for each size class is given by fjEb, and the probability of deposition for the size class j is then given by:

fjEb wsj f jCej

Pj=

Eb wsjCej

=

(6.147)

In equation (6.147), it is implicitly assumed that there is a dynamic equilibrium between erosion and deposition for each size class j.

##### 6.4.6 Bed Armoring

A decrease in sediment erosion rates with time, or bed armoring, can occur due to (1) the consolidation of cohesive sediments with depth and time, (2) the deposition of coarser sediments on the sediment bed during a flow event, and (3) the erosion of finer sediments from the surface sediment, leaving coarser sediments behind, again during a flow event. The consolidation of sediments and subsequent change in erosion rates with depth can be determined by SEDFlume in-situ measurements. The consolidation of sediment and increase of erosion rates with time can be determined approximately from consolidation studies, again by means of SEDFlume.

Here we are concerned about bed armoring due to processes (2) and (3). In order to describe these processes, it is assumed in the present model that a thin mixing layer, or active layer, is formed at the surface of the bed. The existence and properties of this have been discussed by previous researchers (Parker et al., 2000; van Niekerk et al., 1992). The presence of this active layer permits the interaction of depositing and eroding sediments to occur in a discrete layer without allowing deposited sediments to affect the undisturbed sediments below. The authors in van Niekerk et al. (1992) have suggested that the thickness Ta can be approximated by:

τb τce

Ta= 2d50

(6.148)

This formulation takes into account the deeper penetration of turbulence into the bed with increasing shear stress. In the present calculations, d50 is approximated by the average diameter in the interest of computational efficiency.

###### 107



<<<PAGE 121>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



Fig. 6.10. Diagram of SEDflume Layering System.

Since the active layer is kept at a constant thickness (Ta), three possible states of the active layer must be considered. The first state is a net erosion of the active layer, where there may be deposition occurring, but the net flux is erosional. If the thickness of the active layer after this net erosion is T then a thickness of material equal to Ta−T is added to the active layer so that a thickness of Ta can be maintained. This material is added from the layer below in size class proportions equivalent to that in the layer below. The second possible state of the active layer is a net depositional state where the thickness of the active layer exceeds Ta. In this case, the excess material T −Ta is put into a newly deposited material layer just below the active layer but above the parent bed. This material is added to the deposited layer in size class proportions equal to the active layer. The third state of the active layer is where T is equal in thickness to Ta. In this case, no action is taken. Figure 6.10 shows a diagram of the layering system.

The erosion rates for this active layer are dependent on its average particle size. Figure 6.11 shows the erosion rate vs. particle diameter for quartz sediment. It is seen that as the particle diameter increases beyond 200 µm, the erosion rate decreases. This demonstrates how bed coarsening affects erosion rates. A dataset of this type can be constructed utilizing laboratory and field cores to determine erosion rates as a function of particle size for any particular site. The erosion rate for an active or deposited layer can then be calculated from the average particle size of the layer with an interpolation similar to equation (6.117) with particle size in place of thickness.

###### 108



<<<PAGE 122>>>

###### 6. SEDIMENT TRANSPORT EFDC+ Theory



###### Fig. 6.11. Erosion Rates Versus Particle Size and Shear Stress for a Bulk Density of 1.9 g/cm2, adapted from Roberts et al. (1998) by James et al. (2010).

###### 109



<<<PAGE 123>>>

# Chapter 7 CHEMICAL FATE AND TRANSPORT

This chapter presents processes associated with the fate and transport of organic and metallic compounds and their mathematical modeling in water and sediments. It starts with the basic equations and their numerical aspects, then follows by characteristics of organic chemicals and metals, and the sorption and desorption processes. Figure 7.1 provides an outline of the conceptual model for the chemical fate and transport in EFDC+.

Fig. 7.1. Conceptual Model of Chemical Fate and Transport in EFDC+.

###### 110



<<<PAGE 124>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



##### 7.1. Development Overview

When the ”original” sediment transport capability was added, chemical fate and transport was also added (Tetra Tech, 2002b). This module allows for optional chemical partitioning onto water columns and sediment bed solids. Prior to 2015, even though multiple partitioning options were available, only one approach could be used for all the chemicals included in a simulation. DSI updated the chemical partitioning module to allow each chemical constituent to use its own unique partitioning approach. Figure 7.2 provides a schematic of the basic approach.

Fig. 7.2. Linkage Between Hydrodynamic, Sediment Transport, and Chemical Fate and Transport Model.

##### 7.2. Basic Equations

The transport of a sorptive chemical in the water column is governed by transport equations for the chemical dissolved in the water phase, sorbed to material effectively dissolved in the water phase, and sorbed to the suspended sediment particles. Note that the equations below have been generalized for water column processes with general source terms neglected for simplicity.

For the portion of the chemical dissolved in the water phase, the transport can be described as

∂ ∂t

(mHCw)+

∂ ∂x

(myHuCw)+

∂ ∂z

Ab H

m

∂ ∂y

∂ ∂z

(mxHvCw)+

(mwCw) =

∂ ∂z

Cw +mH ∑

KdSi SiχSi +∑

KdDj DjχDj

i

j

Cw φ

−mH∑

χSi −χSi

KaSi Si ψw

i

Cw φ

−mH∑

KaDj Dj ψw

j

χDj −χDj −mHγCw (7.1)

###### 111



<<<PAGE 125>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



The transport equation for the portion of material sorbed to a dissolved constituent D is,

∂ ∂t

∂ ∂x

mHDjχDj +

=

myHuDjχDj +

∂ ∂z

∂ ∂z

Ab H

m

∂ ∂y

∂ ∂z

mxHvDjχDj +

mwDjχDj

Cw φ

DjχDj +mH KsDj Dj ψw

χDj −χDj

−mH KdDj +γ DjχDj (7.2)

The transport equation for the portion of material sorbed to a suspended constituent S is,

∂ ∂t

∂ ∂x

mHSiχSi +

myHuSiχSi

∂ ∂z

=

Ab H

m

∂ ∂y

∂ ∂z

mxHvSiχSi +

mwSiχSi

+

∂ ∂z

Cw φ

SiχSi +mH KaSi Si ψw

χSi −χSi

−mH KaSi +γ SiχSi (7.3)

###### 112



<<<PAGE 126>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



where,

Cw is the mass of a dissolved chemical per unit total volume (mg/m3), Si is the mass of sediment class i (g/m3), Dj is the mass of the dissolved substance class j (i.e. DOC) (g/m3),

χSi is the mass of contaminant sorbed to sediment class i per mass of sediment (mg/g), χDj is the mass of contaminant sorbed to dissolved material j per unit mass of dissolved material (i.e.

sorbed to DOC) (mg/g), χ is the saturation sorbed mass per carrier mass, with subscripts denoting sediment S or dissolved

material D and superscripts denoting the class of sediment i or class of dissolved material j (mg/g), φ is the porosity (dimensionless), ψw is the fraction of the water dissolved contaminant available for sorption (dimensionless), KaS is the sorption rate of sediment (/s), KaD is the sorption rate of dissolved material (/s), KdS is the desorption rate of sediment (/s), KdD is the desorption rate of dissolved material (/s), γ is the net loss rate due to biodegradation, volatilization, and/or decay.

##### 7.3. Chemical Partitioning

The sorption kinetics are based on the Langmuir isotherm (Chapra et al., 1997). Introducing sorbed concentrations defining sorbed mass per unit total volume

CDj = DjχDj (7.4)

CSi = SiχSi (7.5)

The EFDC+ sorbed contaminant transport formulation currently employs equilibrium partitioning with the sorption and desorption terms

Cw φ

KsDj Dj ψw

χDj −χDj = KdDj CDj (7.6)

Cw φ

χSi −χSi = KdSi CSi (7.7) Solving equations (7.6) and (7.7) for the sorbed to water phase concentration ratios gives

KaSi Si ψw

###### 113



<<<PAGE 127>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



CDj Cw

fDj fw

Dj φ

= PDj

=

Cw χDj φ

PDj = PDoj 1+PDoj

ψwKaDj χDj KdDj

PDoj =

−1

(7.8)

fSi fw

CSi Cw

Si φ

= PSi

=

Cw χSiφ

PSi = PSoi 1+PSoi

ψwKaSi χSi KdSi

PSoi =

−1

(7.9)

where, P denotes the partition coefficient, and Po is its linear equilibrium value. For linear equilibrium partitioning, P is set to Po, which in effect approximates

1+PSoi

Cw χSiφ

−1

terms in equations (7.8) and (7.9) as unity. Requiring the mass fractions to sum to unity

fw+∑

fSi+∑

fDj = 1 (7.10) gives

i

j

φ φ +∑iPSiSi +∑j PDjDj fDj =

Cw C

fw =

=

CDj C

PDjDj φ +∑iPSiSi +∑j PDjDj fSi =

=

CSi C

PSiSi φ +∑iPSiSi +∑j PDjDj

=

(7.11)

The dissolved concentrations can be alternately expressed by mass per unit volume of the water phase

with equation (7.11) becoming

Cw φ

Cw:w =

CDj φ DJ:w =

CDj:w =

Dj φ

(7.12)

###### 114



<<<PAGE 128>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



1 φ +∑iPSiSi +∑j PDjφD:jw CDj:w C

Cw:w C

=

PDjD:jw φ +∑iPSiSi +∑j PDjφD:jw

=

CSi C

PSiSi φ +∑iPSiSi +∑j PDjφD:jw

=

which is a generalization of the Chapra et al. (1997) formulation for adsorption to DOC and POC.

(7.13)

##### 7.4. Water Column Chemical Transport and Boundary Conditions

The partitioning relationships shown in equation (7.4) and equation (7.5) allows equations (7.1), (7.2), and (7.3) to be expanded into the transport equation for each contaminant fractions

∂ ∂t

(mHCw)+

∂ ∂x

(myHuCw)+

∂ ∂z

mxmy

=

∂ ∂y

∂ ∂z

(mxHvCw)+

(mxmywCw)

∂ ∂z

Ab H

KdSj CSi +∑

(Cw) +mH ∑

j

i

−mH ∑

i

Cw ø

KaSi Si (ψw

)( χSi −χSi)

### + ∑

j

Cw ø

KaDj Dj (ψw

KdDj CDi

)( χDj −χDj )+γCw (7.14)

∂ ∂t

∂ ∂x

mHCDj +

myHuCDj +

∂ ∂z

=

Ab H

m

∂ ∂y

∂ ∂z

mxHvCDj +

mwCDj

∂ ∂z

Cw φ

(CDj ) +mH KsDj Dj ψw

χDj −χDj

−mH KdDj +γ CDj (7.15)

∂ ∂t

∂ ∂x

mHCSi +

∂ ∂y

myHuCSi +

∂ ∂z

m

=

∂ ∂z

∂ ∂z

mxHvCSi +

mwCSi +

∂ ∂z

Ab H

CSi +mH KaSi Si ψw

mwiSCSi

Cw φ

χSi −χSi

−mH KdSi +γ CSi (7.16)

Where, equation (7.14) is for the dissolved fraction, equation (7.15) is for the fraction sorbed to the dissolved material and equation (7.16) is for the fraction sorbed to the sediments.

###### 115



<<<PAGE 129>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



Adding equations (7.14), (7.15), and (7.16), using the equilibrium partitioning relationship equations (7.6) and (7.7) gives

∂ ∂t

1 m

(mHC)+

∂ ∂x

1 m

(myHuC)+

+

∂ ∂y

(mxvC)

∂ ∂z

∂ ∂z

(mxmywC)−

### m∑

wiS fSiC

i

∂ ∂z

=

∂C ∂z −mHγC (7.17)

Ab H

m

the equation for the total concentration C. The boundary condition at the water column-sediment bed interface, z = 0 is

∂C

Ab H

∂z −∑

wiS fSiC

−

i

Cw +∑jCDj φ

JSBSi ρSi

### =∑

max JSBSi χSi,0 +ε max

,0

i

SB

Cw +∑jCDj φdep

JSBSi ρSi

### +∑

min JSBSi χSi,0 +εdepmin

,0

i

WC

Cw +∑jCDj φ

JSBBi ρSi

### +∑

ε max

,0

i

SB

Cw +∑jCDj φdep

JSBBi ρSi

### +∑

εdepmin

,0

i

WC

Cw +∑jCDj φdep

Cw +∑jCDj φ

+ min(qw,0)

+ max(qw,0)

WC −qdif

SB

Cw +∑jCDj φ

Cw +∑jCDj φdep

−

WC

SB

where,

(7.18)

JSBS and JSBB are the suspended load and bedload sediment fluxes between the sediment bed and the

water column, defined as positive from the bed, ρs is the sediment density in g/m3, qw is the water specific discharge due to bed consolidation and groundwater interaction, defined as

positive from the bed in m3/s, and qdif is a diffusion velocity incorporating the effects of molecular diffusion, hydrodynamic dispersion, and biological induced mixing in m/s.

The subscript SB denotes conditions in the top layer of the sediment bed, while the subscript WC denotes condition in the water column immediately above the bed, with the exception that the specific discharge and

###### 116



<<<PAGE 130>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



diffusion velocity are defined at the water column-bed interface. The subscript dep is used to denote the void ratio and porosity of newly deposited sediment. Equation (7.13) indicates that the contaminant flux between the bed and water column includes a flux of suspended sediment sorbed material; fluxes of water dissolved and sorbed to water dissolved material due to the specific discharge of water associated with consolidation and ground water interaction and water entrainment and expulsion associated with both suspended and bedload sediment deposition and resuspension; and a flux of water dissolved and sorbed to water dissolved material due to diffusion like processes. Transport of bedload sediment sorbed material is represented by direct transport between horizontally adjacent top bed layers and is included in the contaminant mass conservation equations for the sediment bed. The boundary condition at the water free surface is

∂C

Ab H

∂z −∑

wiS fSiC = 0 : z = 1 (7.19) Using the relationship between the porosity and void ratio

−

i

ε 1+ε

φ =

(7.20) and equation (7.5) allows equation (7.18) to be written as

∂C

Ab H

∂z −∑

wiS fSiC

−

i

CSi Si

JSBi ρSi

### =∑

,0 Cw+∑

CDj

max JSBSi

,0 +(1+ε)max

i

j

SB

JSBSi ρSi

CSi Si

,0 Cw+∑

### + ∑

CDj

min JSBSi

,0 + 1+εdep min

j

i

WC

JSBBi ρSi

,0 Cw+∑

### +∑

CDj

(1+ε)max

j

i

SB

jSBBi ρSi

,0 Cw+∑

### +∑

CDj

1+εdep min

j

i

WC

1 φ

Cw+∑

CDj

+ max(qw,0) +qdif

j

SB

1 φ

Cw+∑

CDj

+ min(qw,0) −qdif

j

WC

The sediment concentration can be expressed in terms of the sediment density and void ratio by

(7.21)

Fiρsi 1+ε

Si =

(7.22) where, Fi is the fraction of the total sediment volume occupied by each sediment class.

Fi = ∑

i

Si ρsi

−1

Si ρsi

(7.23)

###### 117



<<<PAGE 131>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



Introducing equations (7.11) and (7.22) into equation (7.21) gives the final form of the bottom boundary

∂C

Ab H

∂z −∑

wiS fSiC

−

i

FiJSBSi Si

JSBSi fSi Si

,0 fw+∑

### =∑

fDj C

,0 C+max

max

j

i

SB

Fdepi JSBSi Sdepi

JSBSi fSi Si

### +∑

,0 fw+∑

fDj C

min

,0 C+min

i

j

WC

JSBBi ρSi

### +∑

,0 Cw+∑

CDj

(1+ε)max

i

j

SB

JSBBi ρSi

### +∑

,0 Cw+∑

CDj

1+εdep min

i

j

WC

1 φ

fw+∑

fDj C

+ max(qw,0) +qdif

j

SB

1 φ

fw+∑

fDj C

+ min(qw,0) −qdif

j

WC

(7.24)

Note that the form of the bed flux associated with bedload transport remains unmodified since the sediment concentration in the water column cannot be readily defined for sediment being transported as bedload.

##### 7.4.1 Numerical Solution to the Water Column Chemical Transport Equations

The transport equation (7.17) for the total contaminant concentration in the water column is solved using a fractional step procedure:

- 1. advection;
- 2. settling, deposition, and resuspension;
- 3. pore water advection and diffusion; and
- 4. reactions.


The fractional phase distribution of the contaminant is recalculated between each steps above using equation (7.11).

##### 7.4.1.1 Advection The advection step is

∆t m

(HC)n+1/4 −(HC)n +

∂ ∂x

∆t m

(myHuC)+

∂ ∂y

∂(wC) ∂z

(mxHvC)+∆t

= 0 (7.25)

###### 118



<<<PAGE 132>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



with the vertical boundary conditions

wC = 0 : z = 0, 1 (7.26)

The fractional time level in equation (7.25) and subsequent equations is used to denote an intermediate result in the fractional step procedure. The spatially discrete form of equation (7.25) is solved using one of the standard high order, flux limited, advective transport solvers in EFDC+.

##### 7.4.1.2 Settling, Deposition, and Resuspension The settling, deposition, and resuspension step is

∂

(H)n+1/2 −(HC)n+1/4 = ∆t

with the boundary conditions

### ∂z ∑

wiS fSiC (7.27)

i

### −∑

wiSfSiC=∑

i

i

max

### +∑

i

FiJSBSi Si

JSBSi fSi Si

,0 fw+∑

fDj C

,0 C+max

j

SB

Fdepi JSBSi Sdepi

JSBSi fSi Si

,0 fw+∑

fDj C

,0 C+min

min

j

JSBBi ρSi

### +∑

,0 Cw+∑

CDj

(1+ε)max

i

j

SB

JSBBi ρSi

### =∑

,0 Cw+∑

CDj

1+εdep min

i

j

WC

: z = 0 (7.28)

WC

wiS fSiC = 0 : z = 1 (7.29) Integrating equation (7.27) over a water column layer and using upwind differencing for the settling gives,

- 1

- 2


1 4

∆k(HC)n+

k −∆k(HC)n+

k =∆t∑

i

wiSSi k+ H

fSi Si k+1

for a layer not adjacent to the bed (i.e., k > 1), and,

n+12

- 1

- 2


(HC)n+

k+1

−∆t∑

i

wiSSi k− H

fSi Si k

n+12

- 1

- 2


(HC)n+

k (7.30)

###### 119



<<<PAGE 133>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



1 2

1 4

∆1(HC)n+

1 −∆1(HC)n+

1

+∆t∑

i

max

+∆t∑

i

min

+∆t∑

i

n+12

fSi Si 2

1 2

Cn+

=∆t∑

wiSSi 1+

2

i

n+12

JSBSi fSi Si

JSBSi Fi Si

Cn+

,0 fw+∑

fDj

,0 +max

sb

j

sb

n+12

JSBSi fSi Si

JSBSi Fi Si

Cn+

,0 fw+∑

fDj

,0 +min

1

j

1

n+12

JSBBi ρSi

- 1

- 2


Cn+

,0 fw+∑

fDj

(1+ε)max

sb

j

sb

+∆t∑

i

(1+ε)min

JSBBi ρSi

,0 fw+∑

fDj

j

- 1

- 2


- 1

- 2


n+21

- 1

- 2


Cn+

1 (7.31)

1

for the first layer adjacent to the bed (i.e, k = 1). Note that equation (7.31) is also the appropriate form for single layer or depth average application. Since the sediment settling flux is zero at the top of the free surface adjacent layer, equation (7.27) is integrated downward from the top layer to the bottom layer. The bottom layer equation (7.31) is solved simultaneously with a corresponding equation for the top layer of the sediment bed. The settling fluxes, wSS and water column-sediment bed fluxes, JSB(S/B) in equations (7.30) and (7.31) are known from the preceding solution for sediment settling, deposition and resuspension. Terms containing the sediment sorbed fraction divided by the sediment concentration in equations (7.30) and (7.31)

fSi Si

PSi φ +∑iPSiSi +∑j PDjDj

=

(7.32)

##### 7.4.1.3 Porewater Advection and Diffusion The diffusion step is given by

∂ ∂z

∂ ∂z

Ab H

- 3

- 4 −(HC)n+


- 1

- 2 = ∆t


(HC)n+

C (7.33) with boundary conditions

∂C ∂z

Ab H

= max(qw,0) +qdif

−

1 φ

fw+∑

fDj C

j

SB

+ min(qw,0) −qdif

1 φdep

fw+∑

fDj C

j

WC

: z = 0 (7.34)

###### 120



<<<PAGE 134>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



For the first layer adjacent to the bed

∂C ∂z

Ab H

= 0 : z = 1 (7.35)

−

(HC)n1+3/4 −(HC)n1+1/2 =

∆t ∆1

+

∆t ∆1

∂C ∂z

Ab H

n+34

1+

max(qw,0) +qdif fw+∑

fDj

j

1 φ

n+12

3 4

Cn+

SB

SB

∆t ∆1

+

min(qw,0) −qdif fw+∑

fDj

j

1 φdep

n+12

- 1

- 2


Cn+

1 (7.36)

1

It is noted that the bed concentrations are advanced to the n+3/4 intermediate time level before the advance of the water column concentrations. While for layers not adjacent to the bed,

∆t ∆1

- 3

- 4


- 1

- 2


(HC)n+

k −(HC)n+

k =

∂C ∂z

Ab H

n+34

∆t ∆1

−

k+

∂C ∂z

Ab H

n+34

k−

- 7.4.1.4 Reactions The solution is completed by

(HC)nk+1 −(H)nk+3/4 = −∆tγ(HC)nk+1 (7.38) an implicit reaction step.

- 7.5. Sediment Bed Chemical Processes


(7.37)

Chemical transport in the sediment bed is represented using the discrete layer formulation developed for bed geomechanical processes. The conservation of mass for the total chemical concentration in a layer of the sediment bed is given by

###### 121



<<<PAGE 135>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



∂ ∂t

(BC)k = −γ(BC)k

JSBSi Fi BSi

JSBSi fSi BSi

−δ(k,kt)∑

,0 fw+∑

fDj

,0 +max

max

i

j

kt

JSBSi Fdepi Sdepi

JSBSi fSi Si

−δ(k,kt)∑

,0 fw+∑

fDj C

min

,0 C+min

i

j

JSBBi BρSi

min(JSBBi χSBLi ,0 −δ(k,kt)∑

−δ(k,kt)∑

,0 fw+∑

fDj

(1+ε)max

i

i

j

−δ(k,kt)∑

i

1+εdep min

JSBBi ρSi

,0 fw+∑

j

− max(qw,0) +qdif k+ − min(qw,0) −qdif k−

1 φB

fDj C

WC

fw+∑

fDj

j

−δ (k,kt) min(qw,0) −qdif kt+

1 φ

−(1−δ (k,kt)) min(qw,0)−qdif k+

1 φB

fw+∑

j

fw+∑

j

+ max(qw,0) +qdif k−

1 φB

fDj C

WC

fDj

(BC)k+1

k+1

fw+∑

fDj

j

(BC)kt

WC

(BC)kt

kt

(BC)k

k

(BC)k−1 (7.39)

k−1

where,

1 : k = kt 0 : k ̸= kt

δ (k,kt) =

(7.40)

is used to distinguish processes specific to the top, water column adjacent layer of the bed, kt. Advective fluxes associated with pore water advection in equation (7.39) are represented in upwind form. In the sediment bed, the actual computational variables for sediment, contaminant, and dissolved material are their concentrations times the thickness of the bed layer. Consistent with this formulation, the fractional phase components in the bed are defined by

Bφ

BCw BC k

(fw)k =

=

Bφ +∑iPSiBSi +∑j PDjBDj k fDj

BCDj BC

PDjBDj Bφ +∑iPSiBSi +∑j PDjBDj k

=

=

k

k

PSiBSi Bφ +∑iPSiBSi +∑j PDjBDj k

BCSi BC k

fSi k =

=

(7.41)

###### 122



<<<PAGE 136>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



- 7.5.1 Bedload Transport The contaminant fluxes associated bedload sediment transport are determined as follows.


∂ ∂x

∂ ∂x

myQiSBLx +

mxQiSBLy (7.42)

mJSBBi =

Equation (7.42) is used to evaluate the flux associated with pore water entrainment and expulsion in equations (7.25) and (7.39). The transport equation for material sorbed to the bedload is

∂ ∂x

∂ ∂x

myQiSBLxχSBLi +

mxQiSBLyχSBLi = mJSBBi χSBLi (7.43)

Since the contaminant mass per sediment mass in the transport divergence corresponds to conditions in the top layer of the sediment bed, equation (7.43) can be written as

fSi Si

fSi Si

∂ ∂x

∂ ∂x

C = mJSBBi χSBLi (7.44) and solved using an upwind approximation

myQiSBLx

mxQiSBLy

C +

fSi Si

fSi Si

mJSBi χSBLi = max myQiSBLx E

+min myQiSBLx E

C

C

E −max myQiSBLx W

C

fSi Si

fSi Si

−min myQiSBLx W

C

C

W

C

fSi Si

fSi Si C

+min mxQiSBy N

+max mxQiSBLy N

C

N −max mxQiSBLy S

fSi Si

−min mxQiSBLy S

C

S

fSi Si

C

C

(7.45)

to evaluate the transport of bedload sorbed material between horizontally adjacent top layers of the sediment bed.

##### 7.5.2 Numerical Solution to the Bed Chemical Process Equations

Equation (7.39) is solved using a fractional step procedure consistent with that used for the water column transport. Equation (7.41) is used to update the fractional distribution in the bed between the settling, deposition, and resuspension step and the pore water advection and diffusion step.

- 7.5.2.1 Settling, Deposition, and Resuspension The settling, deposition, and resuspension step applies only to the top layer of the bed and is


###### 123



<<<PAGE 137>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



1 2

(BC)n+

kt −(BC)nkt

=−∆t∑

i

max

−∆t∑

i

min

−∆t∑

i

n+21

JSBSi fSi BSi

JSBSi Fi BSi

,0 fw+∑

fDj

,0 +max

j

kt

JSBSi Fdepi Sdepi

JSBSi fSi Si

,0 fw+∑

fDj C

,0 C+min

j

−∆t ∑

JSBBi χSBLi ,0

i

n+12

JSBBi BρSi

- 1

- 2


(BC)n+

,0 fw+∑

fDj

(1+ε)max

kt

j

kt

- 1

- 2


(BC)n+

kt

n+21

WC

−∆t∑

i

1+εdep min

JSBBi ρSi

,0 fw+∑

fDj C

j

n+21

WC

(7.46)

This equation is solved simultaneously with equation (7.31) for the bottom layer of the water column. The solution is represented by

 

- 1

- 2


(BC)n+

a11 a12 a21 a22

kt

- 1

- 2


(HC)n+



1

where the coefficients are given by

 

1 2

JSiχSBLi n+

(BC)nkt −∆t ∑

 

i

i=ib ∆1Cn+



n+12

1 4

1 2

i S

Cn+

wiSSi 1+ f



1 +∆t ∑

2

Si 2

i

 



(7.47)

- a11 =1+∆t∑

i

max

JSBSi fSi BSi

,0 +max

JSBSi Fi BSi

,0 fw+∑

j

fDj

n+12

kt

+∆t∑

i

(1+ε)max

JSBBi BρSi

,0 fw+∑

j

fDj

n+12

kt

(7.48)

- a12 =


∆t

### H ∑

min

i

JSBSi fSi Si

,0 +min

JSBSi Fdepi Sdepi

,0 fw+∑

fDj

j

∆t

### H ∑

+

i

1+εdep min

n+12

1

JSBBi ρSi

,0 fw+∑

fDj

j

n+12

1

(7.49)

###### 124



<<<PAGE 138>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



- a21 =−∆t∑

i

max

JSBSi fSi BSi

,0 +max

JSBSi Fi BSi

,0 fw+∑

j

fDj

n+21

kt

−∆t∑

i

(1+ε)max

JSBBi BρSi

,0 fw+∑

j

fDj

n+12

kt

(7.50)

- a22 = ∆1 −


∆t

### H ∑

i

min

JSBSi fSi Si

,0 +min

∆t

−

Adding the two equations in (7.46) gives

JSBSi Fi Si

,0 fw+∑

fDj

j

n+12

1

### H ∑

i

(1+ε)min

JSBBi ρSi

,0 fw+∑

fDj

j

n+12

1

(7.51)

- 1

- 2


- 1

- 2


(BC)n+

kt +∆1(HC)n+

###### 1 =

1 4

(BC)nkt +∆1(HC)n+

1 +∆t∑

i

wiSSi 1+

fSi Si 2

n+12

- 1

- 2


Cn+

2

−∆t∑

i

- 1

- 2 (7.52)


JSiχSBLi n+

This equation verifies the consistency of the water column-sediment bed exchange since the source and sinks on the right side include only settling into the top of the water column layer, and transfer of bedload sediment sorbed contaminant between horizontal sediment bed cells.

- 7.5.2.2 Porewater Advection and Diffusion The pore water advection and diffusion step for the top, water column adjacent, layer is


(BC)nkt+3/4 = (BC)nkt+1/2

−∆t max(qw,0) +qdif kt+

1 φB

fw+∑

fDj

j

+∆t min(qw,0) −qdif kt−

1 φB

fw+∑

fDj

j

−∆t min(qw,0) −qdif kt+

1 φH

fw+∑

fDj

j

+∆t max(qw,0) +qdif kt−

1 φB

n+1/2

(BC)nkt+3/4

kt

n+1/2

(BC)nkt+3/4

kt

n+1/2

(HC)n1+1/2

1

n+1/2

fw+∑

(BC)nkt+−11/2 (7.53)

fDj

j

kt−1

###### 125



<<<PAGE 139>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



which is an implicit form. Writing equation (7.36) in the form

∆1(HC)n1+3/4 = ∆1(HC)n1+1/2 +∆t

∂C ∂z

Ab H

n+3/4

1+

+∆t max(qw,0) +qdif kt+

1 φB

fw+∑

fDj

j

+∆t min(qw,0) −qdif kt+

1 φH

and combining with equation (7.52) gives

n+1/2

(BC)nkt+3/4

SB

n+1/2

fw+∑

(HC)n1+1/2 (7.54)

fDj

j

1

(BC)nkt+3/4 +∆1(HC)n1+3/4

Ab H

= (BC)nkt+1/2 +∆1(HC)n1+1/2 +∆t

∂zC

1+

n+1/2

1 φB

fw+∑

fDj

+∆t min(qw,0) −qdif kt−

j

kt

+∆t max(qw,0) +qdif kt−

1 φB

fw+∑

j

n+3/4

(BC)nkt+3/4

fDj

n+1/2

(BC)nkt+−31/4 (7.55)

kt−1

This equation verifies the consistency of the representation of pore water advection and diffusion across water column-sediment bed interface since the source and sink terms on the right side of equation (7.55) represent fluxes at the top to the water column cell and the bottom of the bed cell.

The pore water diffusion and advection step for the remaining bed layers is given by

(BC)nk+3/4 = (BC)nk+1/2

−∆t min(qw,0) −qdif k+

1 φB

fw+∑

fDj

j

−∆t max(qw,0) +qdif k+

1 φB

fw+∑

fDj

j

+∆t min(qw,0) −qdif k−

1 φB

fw+∑

fDj

j

+∆t max(qw,0) +qdif k−

1 φB

n+1/2

(BC)nk++13/4

k+1

n+1/2

(BC)nk+3/4

k

n+1/2

(BC)nk+3/4

k

n+1/2

fw+∑

(BC)nk−+13/4 (7.56)

fDj

j

k−1

For the bottom-most layer (k = 1) layer-bottom boundary (denoted by k−), the specific discharge and diffusion velocity must be specified along with the total contaminant concentration, C0. The corresponding

###### 126



<<<PAGE 140>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



thickness of the unresolved layer k = 0, is set to unity without loss of generality. The system of equations represented by equations (7.52) and (7.55) is implicit and is solved using a tri-diagonal linear equation solver. It is noted that the n+3/4 time level layer thickness is actually the n+1 time level thickness determined by the solution of equation (7.23). The specific discharges in equations (7.52) and (7.55) are given by equation (7.41) and represent those appearing in equation (7.23) and guarantee mass conservation for the pore water advection.

- 7.5.2.3 Reactions The bed transport solution is completed by


(BC)nk+1 −(BC)nk+3/4 = −∆tγ(BC)nk+1 (7.57) an implicit reaction step.

- 7.6. Chemical Loss Terms


- 7.6.1 Bulk Degradation


Bulk degradation can be included in the water column and/or the sediment bed for any chemical constituent. The bulk degradation in the water column follows a first order decay rate

dCk dt

= −KCk (7.58) where,

C is the chemical concentration in mg/m3 in layer k, K is the first order decay rate in 1/s, and t is the time in seconds.

For bulk degradation there is no temperature effects on the degradation rate. In the sediment bed, bulk degradation can be applied for sediment thickness up to a maximum sediment depth

kt

dCb,k dt

### ∑

Hbed,k ≤ Dmax (7.59) where,

= −KCb,k, for

k

Cb,k is the sediment bed chemical contaminant concentration in layer k (mg/g), K is the bulk decay rate (1/s), Hbed,k is the sediment bed layer thickness (m), and Dmax is the maximum depth to use bulk degradation (m).

###### 127



<<<PAGE 141>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



##### 7.6.2 Biodegradation

Bacterial degradation, sometimes referred to as microbial transformation, biodegradation or biolysis, is the breakdown of a compound by the enzyme systems in bacteria. Although these transformations can detoxify and mineralize chemicals and defuse potential chemicals, they can also activate potential chemicals.

Biodegradation in EFDC+ follows the bulk degradation approach shown previously

dCk dt

= −Kw,bioCk (7.60) and

kt

dCb,k dt

∑

Hbed,k ≤ Dbio (7.61) where,

= −Kb,bioCb,k, for

k

Ck is the chemical concentration in the water column in layer k (mg/m3), Cb,k is the sediment bed chemical contaminant concentration in layer k (mg/g), Kw,bio is the water column biodegradation rate (1/s), Kb,bio is the sediment bed biodegradation rate (1/s), Hbed,k is the sediment bed layer thickness (m), and Dbio is the maximum depth to apply biodegradation (m).

And where the degradation coefficient is temperature dependent, it can be calculated as

Kbio = Kbio,refQ10(T−20)/10 (7.62) where,

Kbio,ref is respective reference biodegradation rate at 20◦C (1/s), Q10 is the temperature correction factor for biodegradation, and T is the current temperature (◦C).

The temperature correction factors represent the increase in the biodegradation rate constants resulting from a 10◦C temperature increase. Values in the range of 1.5 to 2.0 are common.

##### 7.6.3 Volatilization

Volatilization is the movement of chemical across the air-water interface as the dissolved neutral concentration attempts to equilibrate with the gas phase concentration. Equilibrium occurs when the partial pressure exerted by the chemical in solution equals the partial pressure of the chemical in the overlying atmosphere. The rate of exchange is proportional to the gradient between the dissolved concentration and the concentration in the overlying atmosphere and the conductivity across the interface of the two fluids. The conductivity

###### 128



<<<PAGE 142>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



is influenced by both chemical properties (molecular weight, Henry’s Law constant) and environmental conditions at the air-water interface (turbulence-controlled by wind speed, current velocity, and water depth).

In EFDC+, volatilization of a dissolved chemical constituent is computed by

where,

∂C ∂t volat

Kv HKC

=

Ca HL RTK

fdC−

(7.63)

C is the water column concentration in layer KC (mg/m3), KC is the top layer number (dimensionless), Kv is the transfer rate (m/day), Hkc is the water column thickness of the layer KC (m), fd is the fraction of the total chemical that is dissolved, Ca is the atmospheric concentration (mg/m3), R is the universal gas constant 8.206×10−5atm−m3/mole−K, TK is the water temperature in Kelvin (◦K), and HL is the Henry’s law coefficient for the air-water partitioning of the chemical (atm−m3/mole).

Equilibrium occurs when the dissolved concentration equals the partial pressure divided by the Henry’s Law Constant.

The dissolved concentration of a chemical in a surface water column segment can volatilize at a rate determined by the two-layer resistance model Whitman et al. (1923). The two-resistance method assumes that two “stagnant films” are bounded on either side by well mixed compartments. Concentration differences serve as the driving force for the water layer diffusion. Pressure differences drive the diffusion for the air layer. From mass balance considerations, it is obvious that the same mass must pass through both films, thus the two resistances combine in series, so that the conductivity is the reciprocal of the total resistance:

where,

HL RTK

Kv = (RL +RG)−1 = K−1

L + KG

−1 −1

(7.64)

RL is the liquid phase resistance (s/m), KL is the liquid phase transfer coefficient (s/day), RG is the gas phase resistance (s/m), and KG is the gas phase transfer coefficient (m/s).

There is yet another resistance involved, the transport resistance between the two interfaces, but it is assumed to be negligible. This may not be true in very turbulent conditions, and in the presence of surface-active contaminants. Although this two-resistance method, the Whitman model, is rather simplified in its assumption of uniform layers, it has been shown to be as accurate as more complex models.

###### 129



<<<PAGE 143>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



The value of Kv, the conductivity, depends on the intensity of turbulence in a water body and in the overlying atmosphere. Leinonen and Mackay (1975) have discussed conditions under which the value of Kv is primarily determined by the intensity of turbulence in the water. As the Henry’s Law coefficient increases, the conductivity tends to be increasingly influenced by the intensity of turbulence in water. As the Henry’s Law coefficient decreases, the value of the conductivity tends to be increasingly influenced by the intensity of atmospheric turbulence.

The computed volatilization rate from equation (7.64) is for a temperature of 20◦C. It is adjusted for water temperature using the equation:

Kv,T = KvΘT−20 (7.65) where,

Θ is the temperature correction factor, and T is the water temperature (◦C).

The liquid and gas film transfer coefficients computed under this option vary with the type of waterbody. The type of waterbody is specified as one of the volatilization constants and can either be a flowing stream, river or estuary or a stagnant pond or lake. The primary difference is that in a flowing waterbody the turbulence is primarily a function of the stream velocity, while for stagnant waterbodies wind shear may dominate. The formulations used to compute the transfer coefficients vary with the waterbody type as shown below.

EFDC+ automatically determines which flow regime to apply based on the following criteria

or

H > Hmax, Lake conditions H ≤ Hmax, River conditions

where,

U ≤ Umax, Lake conditions U > Umax, River conditions

H is total depth (m), Hmax is maximum depth allowed for river conditions (m), U is the depth averaged velocity magnitude (m/s), and Umax is the maximum lake velocity magnitude (m/s).

(7.66)

(7.67)

##### 7.6.3.1 Flowing Stream, River or Estuary

For a flowing system, the transfer coefficients are controlled by flow induced turbulence. For flowing conditions, the liquid film transfer coefficient (KL) is computed using the Covar method Fig. 7.3 (Covar, 1976) in which the equation used varies with the velocity and depth of the cell.

###### 130



<<<PAGE 144>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



Fig. 7.3. Covar Method (1976).

For cells with depths less than 0.61 m, the Owens formula is used to calculate the volatilization rate (7.68).

U0.67 H1.85

5.35 86400

H (7.68) where,

KL =

U is the depth averaged water velocity magnitude (m/s), and H is cell depth (m).

For segments with a cell depth greater than 0.61 m and cell depth (m) greater than 3.45U2.5 the O’ConnorDobbins formula is used:

(DwU)0.5 H1.5

H (7.69) where, Dw is the diffusivity of the chemical in water (m2/s), computed from

KL =

###### 131



<<<PAGE 145>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



22·10−9 Mw0.6667

Dw =

In all other cases, the Churchill formula is used to calculate volatilization rate:

(7.70)

U0.969 H1.673

5.049 86400

KL =

H (7.71)

The gas transfer coefficient (KG) is assumed constant at 100 m/day for flowing systems.

##### 7.6.3.2 Lake or Pond

For more quiescent conditions, the transfer coefficients are controlled by wind induced turbulence. For these systems, the liquid film transfer coefficient (KL) is computed using either the O’Connor equations or Mackay and Yeun (1983).

##### Option 1 O’Connor Approach

KL = u∗

ρa ρw

0.5κ0.33 λ2

S−0.67

cw (7.72)

κ0.33 λ2

S−0.67

KG = u∗

ca (7.73) where, u∗ is the shear velocity (m/s) computed from

u∗ = Cd0.5W10 (7.74) where,

Cd is the drag coefficient (0.0011), W10 is wind velocity at 10 m above the water surface (m/s), ρa is density of air, internally calculated from air temperature (kg/m3), ρw is density of water, internally calculated from water temperature (kg/m3), κ is von Karman’s constant, λ2 is dimensionless viscous sublayer thickness, and Sca and Scw are air and water Schmidt Numbers, computed from

µa ∂aDa

Sca =

(7.75)

µw ∂wDw

(7.76) where,

Scw =

###### 132



<<<PAGE 146>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



Da is diffusivity of chemical in air (m2/s), Dw is diffusivity of chemical in water (m2/s), µa is viscosity of air, internally calculated from air temperature (kg/m−sec), and µw is viscosity of water, internally calculated from water temperature (kg/m−sec).

The diffusivity of the chemical in water is computed using equation (7.70) while the diffusivity of the chemical in air (Da, m2/sec) is computed from

1.9·10−4 Mw2/3

Da =

Thus KG is proportional to wind and inversely proportional to molecular weight to the 4/9 power.

(7.77)

##### Option 2 Mackay and Yeun Approach

Under this option, the liquid and gas film transfer coefficients are computed using formulations described by Mackay and Yeun (1983). The Mackay equations are:

KL =

10−6 +0.00341u∗S−0.5

cw , u∗ > 0.3m/s 10−6 +0.01441u2∗.2S−0.5

cw , u∗ < 0.3m/s

(7.78)

KG = 10−3 +0.0462u∗S−0.67

ca (7.79)

##### Volatilization Input Data

Although there are many calculations involved in determining volatilization, most are performed internally using a small set of data. Volatilization data specifications are summarized in Table 7.1 Not all of the constants are required. Volatilization is only active for the surface layer.

###### 133



<<<PAGE 147>>>

###### 7. CHEMICAL FATE AND TRANSPORT EFDC+ Theory



Table 7.1. Volatilization Input Data

Description Notation Range Units

Measured or calibrated conductance Kv 0.6 — 25 m/day Henry’s Law Constant H 10−7 — 10−1 atm−m3/mole Concentration of chemical in atmosphere

Ca 0 — 1000 µg/L

Molecular weight Mw 10 — 103 g/mole Reaeration coefficient (conductance of oxygen)

Ka 0.6 — 25 m/day

Experimentally measured ratio of volatilization to reaeration

kvo 0 — 1

Current velocity ux 0.2 m/s Water depth D 0.1 — 10 m Water temperature T 4 — 30 ◦C Wind speed 10m above surface W10 0 — 20 m/s

###### 134



<<<PAGE 148>>>

# Chapter 8 EUTROPHICATION

In EFDC+, the eutrophication module refers to modeling aquatic plants, algae, zooplankton, and the biochemical transformation of nutrients during this process. Collectively, these biological organisms are referred to as “Biota” in the EFDC+ interface, although it does not include higher trophic level organisms that consume the zooplankton. This chapter summarizes the basic theory of these processes as they are modeled in EFDC+. The kinetic processes included in the EFDC+ eutrophication module are derived from the ICM water quality model (Cerco and Cole, 1995) as described in Park et al. (1995), and the formulation provided by Cerco et al. (2004). A sediment diagenesis process was also implemented in EFDC+, primarily based on the Chesapeake Bay Sediment Flux Model developed by DiToro and Fitzpatrick (1993). The coupling of the sediment diagenesis module with the water quality module enhances the model to simulate long-term changes in water quality conditions in response to changes in nutrient loading by sediment fluxes released from the bed.

Prior to EFDC+10.3, the eutrophication module could only simulate three groups of phytoplankton (freefloating), and one group of macroalgae (attached). The predation of phytoplankton by higher trophic level organisms such as zooplankton was modeled using a constant rate or a rate proportional to algal biomass. From EFDC+10.3, the eutrophication module was enhanced to model unlimited groups of aquatic plants and algae, and zooplankton groups.1 Users can differentiate between the “Biota” groups by names and parameters assigned to these groups. The model simulates spatial and temporal distributions of water quality parameters, including dissolved oxygen, floating or attached algae (unlimited species), zooplankton (unlimited species), various components of carbon, nitrogen, phosphorus, and silica cycles, and fecal coliform bacteria. Figure 8.1 illustrates the structure of the water quality model implemented in EFDC+ with the set of state variables listed in Table 8.1. The coupling between the water quality components is illustrated in Figure 8.2.

All the biota classes in EFDC+ are represented in Carbon (C) units. Organic Carbon (OC), Nitrogen (N), and Phosphorus (P) are represented by up to three reactive sub-classes, refractory particulate, labile particulate, and labile dissolved. The use of sub-classes allows a more realistic distribution of organic material by reactive classes when data is available to estimate distribution factors. The following sections discuss the role of each variable and summarize their kinetic interaction processes. Sediment diagenesis processes including the exchange of nutrient fluxes at the sediment-water interface and Sediment Oxygen Demand

1Professor Dongil Seo from Chungnam National University, South Korea, has made significant contributions to the development of the kinetic equations for phytoplankton and zooplankton modeling in EFDC+. Journal articles published by Professor Seo’s research group, based on their research using EFDC, include Kim et al. (2021a), Kim et al. (2021b), Shiferaw et al. (2022), Kim et al. (2022), and Kim and Seo (2024).

###### 135



<<<PAGE 149>>>

###### 8. EUTROPHICATION EFDC+ Theory



(SOD) are presented as a full sediment diagenesis model. A rooted plant and epiphytes sub-module is also described that can be used to model submerged macrophytes with shoots, roots, and epiphytes. The description of the EFDC+ eutrophication module in this section closely follows Park et al. (1995).

Fig. 8.1. Structure of the EFDC+ Water Quality Model.

###### 136



<<<PAGE 150>>>

###### 8. EUTROPHICATION EFDC+ Theory



Table 8.1. EFDC+ Water Quality State Variables

# Water quality state variable Acronyms Units Group

- 1 Refractory particulate organic carbon RPOC mg/l Organic carbon
- 2 Labile particulate organic carbon LPOC mg/l
- 3 Dissolved Organic Carbon DOC mg/l
- 4 Refractory particulate organic phosphorus RPOP mg/l Phosphorus
- 5 Labile particulate organic phosphorus LPOP mg/l
- 6 Dissolved organic phosphorus DOP mg/l
- 7 Total phosphate PO4t mg/l
- 8 Refractory particulate organic nitrogen RPON mg/l Nitrogen
- 9 Labile particulate organic nitrogen LPON mg/l
- 10 Dissolved Organic Nitrogen DON mg/l
- 11 Ammonium NH4 mg/l
- 12 Nitrate and Nitrite NO3, NO2 mg/l
- 13 Particulate biogenic silica SiP mg/l Silica
- 14 Dissolved available silica SiA mg/l
- 15 Chemical Oxygen Demand COD mg/l Others
- 16 Dissolved Oxygen DO mg/l
- 17 Total Active Metals TAM mole/m3
- 18 Fecal coliform bacteria FCB MPN/100ml
- 19 Carbon dioxide CO2 mg/l C
- 20 Aquatic Plants Ba mg/l C Algae and Macrophytes (Unlimited groups)
- 21 Aquatic Animals Zz mg/l C Zooplankton (Unlimited groups)


###### 137



<<<PAGE 151>>>

###### 8. EUTROPHICATION EFDC+ Theory



- Fig. 8.2. Schematic Diagram of EFDC+ Water Quality Model Structure.


##### 8.1. Water Column Eutrophication Formulation

##### 8.1.1 Model State Variables

##### 8.1.1.1 Algae and Macrophyte

Algae and macrophyte are a central part of the numerical eutrophication models. From the modeling point of view, algae are often grouped based on the distinctive characteristics and the significant role the characteristics play in the ecosystem. The legacy EFDC eutrophication module included three free-floating groups (cyanobacteria, diatoms, and greens) and a stationary or non-transported group (macroalgae).

Cyanobacteria, commonly called blue-green algae, are characterized by their abundance (as picoplankton) in saline water and by their bloom-forming characteristics in fresh water. Cyanobacteria are unique in that some species fix atmospheric nitrogen, although nitrogen fixers are not believed to be predominant in many river systems. Diatoms are distinguished by their requirement of silica as a nutrient to form cell walls. Diatoms are large algae, characterized by high settling velocities. Settling of spring diatom blooms to the sediments may be a significant source of carbon for SOD. Algae that do not fall into the preceding two groups are lumped into green algae. Green algae settle at a rate intermediate between cyanobacteria and diatoms, and are subject to greater grazing pressure than cyanobacteria.

###### 138



<<<PAGE 152>>>

###### 8. EUTROPHICATION EFDC+ Theory



Macrophyte group, defined as stationary or non-transported algae variables, can be included in the model to simulate macroalgae/periphyton groups. The stationary algae variables have the same kinetic formulation as the original algae groups, with the exception that they are not transported. The stationary algae groups can also be used to represent various types of bottom substrate attached or floating periphyton.

From EFDC+10.3 onwards, unlimited groups of algae and macrophyte could be modeled and are differentiated based on the label and parameters. Appendix 8.4 provides additional information regarding model configuration for eutrophication simulation.

##### 8.1.1.2 Zooplankton

Zooplankton consist of animal life that are adrift in a waterbody. They include the larval forms of large adult organisms (e.g., crabs, fish) and small animals that never get larger than several millimeters. Zooplankton form an important link in the food web. They consume algae by filtering the surrounding water and then clearing off the algae. They also consume bacteria, detritus, and sometimes other zooplankton, and are also predated by small fish. Zooplankton grazing can be a key loss mechanism for algae, depending on the time of the year, zooplankton population, and zooplankton grazing rate. From EFDC+10.3 onwards, an unlimited number of zooplankton groups can be included in the simulation through specification of their kinetics parameters. Kinetic equations of zooplankton and its interaction with the water quality components are derived from (Cerco et al., 2004; Seo, 2019). Figure 8.3 illustrates the interaction between zooplankton and other state variables.

Fig. 8.3. Interaction of Zooplankton with Eutrophication components.

##### 8.1.1.3 Organic Carbon (OC)

The three OC state variables considered in EFDC+ are; (DOC), Labile Particulate Organic Carbon (LPOC), and Refractory Particulate Organic Carbon (RPOC). Labile and refractory distinctions are based upon the

###### 139



<<<PAGE 153>>>

###### 8. EUTROPHICATION EFDC+ Theory



time scale of decomposition. Labile OC decomposes rapidly on a time scale of days to weeks, whereas refractory OC requires more time, and may take multiple years.

##### 8.1.1.4 Nitrogen (N)

N is first divided into organic and mineral fractions. Organic Nitrogen (ON) state variables are Dissolved Organic Nitrogen (DON), Labile Particulate Organic Nitrogen (LPON), and Refractory Particulate Organic Nitrogen (RPON). The mineral N forms are Ammonium (NH4+) and Nitrate (NO−

3 ). Both mineral forms

are utilized to satisfy algal nutrient requirements, although NH4+ is thermodynamically preferred. NH4+ is oxidized by nitrifying bacteria into NO−

3 . This oxidation can be a significant sink of Oxygen (O) in the water column and sediments. An intermediate in the complete oxidation of NH4+, Nitrite (NO−

2 ) also exists. NO−

2 concentrations are usually much less than NO−

3 , and for modeling purposes, NO−

2 is combined with NO−

3 . Hence, the NO−

3 state variable actually represents the sum of NO−

3 and NO−

2 .

##### 8.1.1.5 Phosphorus (P)

Organic P is also considered in three states; Dissolved Organic Phosphorus (DOP), Labile Particulate Organic Phosphorus (LPOP), and Refractory Particulate Organic Phosphorus (RPOP). Only a single mineral form, Phosphate (PO−3

4 ), is considered. PO−3

4 exists in several states within the model ecosystem; dissolved, sorbed to inorganic solids, and incorporated in the algal cells. Equilibrium partition coefficients are used to distribute the PO−3

4 among the three states.

##### 8.1.1.6 Silica (SiO2)

Silica (SiO2) is divided into two state variables; Dissolved Available Silica (SiA) and Particulate Biogenic Silica (SiP). SiA is primarily dissolved and can be utilized by diatoms. SiP cannot be utilized. In the model, SiP is produced through diatom mortality. SiP undergoes dissolution to SiA or else settles to the bottom sediments.

##### 8.1.1.7 Chemical Oxygen Demand (COD)

In EFDC+, Chemical Oxygen Demand (COD) is the concentration of reduced substances that are oxidizable by inorganic means. The primary component of COD is Sulfide (S−

2 ) released from sediments. Oxidation of S−

2 to Sulfate (SO−2

4 ) may remove substantial quantities of DO from the water column.

##### 8.1.1.8 Dissolved Oxygen (DO)

DO is required for the existence of higher life forms, and is a central component of the water quality model. DO availability determines the distribution of organisms and the flows of energy and nutrients in an ecosystem.

###### 140



<<<PAGE 154>>>

###### 8. EUTROPHICATION EFDC+ Theory



##### 8.1.1.9 Total Active Metal (TAM)

Both PO−3

4 and SiA adsorb to inorganic solids, primarily Iron (Fe) and Manganese (Mn). Sorption and subsequent settling is one pathway for removal of PO−3

4 and SiA from the water column. However, limited data does not allow a complete treatment of Fe and Mn chemistry. Rather, a single-state variable Total Active Metals (TAM), is defined as the total concentration of metals that are active in PO−3

4 and SiA. TAM is partitioned between particulate and dissolved phases by an oxygen-dependent partition coefficient. Inorganic suspended solids can be used, in lieu of TAM, as a sorption site for PO−3

4 and SiA. TSS concentration is provided by the sediment transport component of the EFDC+ modeling system.

##### 8.1.2 Conservation of Mass Equation

The conservation of mass accounts for the material entering/leaving a water body, transport of the material within the water body, and physical, chemical, biological transformation of material. Hence, the governing mass-balance equation for each of the water quality state variables with a concentration C can be expressed as:

∂ ∂x

∂ ∂t

(mxmyHC)+

∂ ∂y

∂ ∂z

(myHuC)+

(mxmywC)= ∂ ∂x

(mxHvC)+

∂C ∂x

∂ ∂y

∂C ∂y

myHAx mx

mxHAy my

+

∂ ∂z

+

∂C ∂z

Az H

mxmy

+mxmyHSC (8.1)

The last three terms on the Left Hand Side (LHS) of equation 8.1 account for the advective transport, and the first three terms on the Right Hand Side (RHS) account for the diffusive transport. These six terms for physical transport are analogous to, and thus the numerical method of solution is the same as, those in the mass-balance equation for salinity in the hydrodynamic model (Hamrick, 1992). The last term SC in the equation 8.1 is the internal and external sources and sinks per unit volume, represents the kinetic processes and external loads for each of the state variables.

EFDC+ solves equation 8.1 using a fractional step procedure which decouples the kinetic terms from the physical transport terms. The equation for physical transport is written as:

∂ ∂tp

(mxmyHC)+

∂ ∂x

∂ ∂y

∂ ∂z

(myHuC)+

(mxmywC) = ∂ ∂x

(mxHvC)+

∂C ∂x

∂ ∂y

∂C ∂y

∂ ∂z

myHAx mx

mxHAy my

+

+

∂C ∂z

Az H

mxmy

+mxmyHSCP (8.2)

The equation for kinetic processes and external loading, called kinetic equation, is:

∂C ∂tk

= SCK (8.3) with

∂ ∂t

(mxmyHC) =

∂ ∂tp

∂C ∂tk

(mxmyHC)+(mxmyH)

(8.4)

###### 141



<<<PAGE 155>>>

###### 8. EUTROPHICATION EFDC+ Theory



In the equations above, the subscript k refers to the kinetic processes while the subscript p refers to the physical transport of a water quality component.

The source sink term SC in equation 8.2, has been split into physical sources and sinks which are associated in volumetric inflows and outflows, and kinetic sources and sinks in equations 8.3 and 8.4, respectively. Since variations in the water column depth are coupled with the divergence of the volume transport field, the kinetic step is made at a constant water column depth corresponding to the depth field at the end for the physical transport step. This allows the depth and scale factors to be eliminated from the kinetic step in equation 8.3 which can be further split into reactive and internal sources and sinks as:

where,

∂C ∂tk

= K ·C+R (8.5)

K is the kinetic rate (time−1), and R represents internal source/sink term (mass volume−1time−1).

Equation 8.5 is obtained by linearizing some terms in the kinetic equations, mostly Monod type expressions. Hence, K and R are known values in equation 8.5. Equation 8.2 is identical to, and thus its numerical method of solution is the same as, the mass-balance equation for salinity (Hamrick, 1992). The solution scheme for both the physical transport (Hamrick, 1992) and the kinetic equations is second-order accurate.

##### 8.1.3 Kinetic Equations for State Variables

The remainder of this chapter details the kinetics portion of the mass-conservation equation for each state variable. Parameters are defined where they first appear. All parameters are listed, in alphabetical order, in Appendix (section 8.4). For consistency with reported rate coefficients, kinetics are detailed using a temporal dimension of days. Within the EFDC+ code, kinetic sources and sinks are converted to a dimension of seconds before they are used in the mass-conservation equations.

##### 8.1.3.1 Algae

EFDC+ simulates unlimited general autotroph groups that can be parameterized to represent any specific species or a group of species. Each group can be paramterized and labeled accordingly. For a general group, the kinetics in the model are governed by:

- 1. Growth (production)
- 2. Basal metabolism
- 3. Predation by zooplankton
- 4. Mortality
- 5. Settling
- 6. External loads


###### 142



<<<PAGE 156>>>

###### 8. EUTROPHICATION EFDC+ Theory



Since these processes are largely the same for all algal groups, the kinetics equation for a general algae x can be written as:

∂Bx ∂t

∂ ∂Z

WBx V

(8.6) where,

= (Px −BMx −Dx)Bx −PRx +

(WSxBx)+

Bx is the algal biomass of algal group x (g C/m3), t is the time (days), Px is the production rate of algal group x (1/day), BMx is the basal metabolism rate of algal group x (1/day), Dx is the mortality rate of algal group x (1/day), PRx is the predation rate of algal group x by zooplankton, WSx is the positive settling velocity of algal group x (m/day), WBx is the external loading of algal group x (g C/day), and V is the model cell volume (m3).

##### 8.1.3.1.1 Production (Algal Growth)

Algal growth depends on nutrient availability, ambient light, and temperature. The effects of these processes are considered to be multiplicative:

Px = PMx f1(N) f2(I) f3(T) f4(S) (8.7) where,

PMx is the maximum growth rate under optimal conditions for algal group x (1/day),

- f1(N) is the effect of suboptimal nutrient concentration (0 ≤ f1 ≤ 1),
- f2(I) is the effect of suboptimal light intensity (0 ≤ f2 ≤ 1),
- f3(T) is the effect of suboptimal temperature (0 ≤ f3 ≤ 1), and
- f4(S) is the effect of salinity on the growth (0 ≤ f4 ≤ 1),


For the freshwater organisms, the increased mortality is included in the model by the salinity toxicity term in the growth equation.

##### 8.1.3.1.1.1 Effect of Nutrients on Algal Growth

Using Liebig’s “law of the minimum” (Odum, 1971) algal growth is determined by the nutrient in least supply, the nutrient limitation for growth of an algal group is expressed as:

NH4+NO3 KHNx +NH4+NO3

PO4 KHPx +PO4

SAd KHS+SAd

f1(N) = min

(8.8) where,

,

,

###### 143



<<<PAGE 157>>>

###### 8. EUTROPHICATION EFDC+ Theory



NH4 is the NH4+ concentration as N (g N/m3), NO3 is the NO−

3 concentration as N (g N/m3), KHNx is the half-saturation constant for N uptake for algal group x (g N/m3), PO4 is the dissolved phosphate concentration as P (g P/m3), KHPx is the half-saturation constant for P uptake for algal group x (g P/m3), SAd is the concentration of dissolved available SiO2 (g Si/m3), and KHS is the half-saturation constant for SiO2 uptake for diatoms (g Si/m3).

Some cyanobacteria (e.g., Anabaena) can fix N from atmosphere and thus are not limited by N. In that case, N terms can be ignored for cyanobacteria. SiO2 is a limitation for diatoms only, and can be ignored for other groups.

##### 8.1.3.1.1.2 Effect of Light on Algal Growth

The effect of light on algal growth is calculated using daily and vertically integrated form of Steele’s equation (Cerco and Cole, 1995) as shown below:

exp(1) FD Kess (ZB−ZT)

(exp(−αb) −exp(−αT) ) (8.9)

f2(I) =

αB =

I0 FD·Isx

exp(−Kess ZB) (8.10)

I0 FD·Isx

αT =

exp(−Kess ZT) (8.11) where,

FD is the fractional day length (0 ≤ FD ≤ 1), Kess is the total light extinction coefficient (1/m), ZT is the distance from water surface to layer top (m), ZB is the distance from water surface to layer bottom (m), I0 is the daily total light intensity at water surface (langleys/day), and Isx is the optimal light intensity for algal group x (langleys/day).

The total light extinction Kess in the water column is calculated using equation 5.17. Optimal light intensity Isx for photosynthesis depends on algal taxonomy, duration of exposure, temperature, nutritional status, and previous acclimation. Variations in Isx are largely due to adaptations by algae intended to maximize production in a variable environment. Steele (1962) noted the result of adaptations is that the optimal intensity is a consistent fraction (approximately 50 %) of daily intensity. Kremer and Nixon (1978) reported an analogous finding that maximum algal growth occurs at a constant depth (approximately 1 m) in the water column. Their approach is adopted so that optimal intensity is expressed as:

###### 144



<<<PAGE 158>>>

###### 8. EUTROPHICATION EFDC+ Theory



Isx = max(I0avg ·exp(−Kess Doptx) , Isxmin) (8.12) where,

Doptx is the depth of maximum algal growth for algal group x (m), I0avg is the adjusted surface light intensity (W/m2), and Isxmin is the minimum optimum light intensity (W/m2).

A minimum Isxmin, in equation 8.12 is specified so that algae do not thrive at extremely low light levels. The time required for algae to adapt to changes in light intensity is recognized by estimating I0avg based on a time-weighted average of daily light intensity:

I0avg = CIaI0 +CIbI1 +CIcI2 (8.13) where,

I1 is the daily light intensity 1 day preceding model day (langleys/day), I2 is the daily light intensity 2 days preceding model day (langleys/day), and CIa, CIb, CIc are the weighting factors for I0,I1 and I2, respectively: CIa +CIb +CIc = 1.

- 8.1.3.1.1.3 Effect of Temperature on Algal Growth A Gaussian probability curve is used to represent temperature dependency of algal growth:


 

- exp(−KTG1x ·(T −TM1x)2), T ≤TM1x 1, TM1x < T < TM2x
- exp(−KTG2x ·(T −TM2x)2), T ≥TM2x


f3(T) =



where,

(8.14)

T is the temperature (◦C) provided from the hydrodynamic model, TM1x is the minimum optimal temperature for algal growth for algal group x (◦C), TM2x is the maximum optimal temperature for algal growth for algal group x (◦C), KTG1x is the effect of temperature below TM1x on growth for algal group x (1/◦C2), and KTG2x is the effect of temperature above TM2x on growth for algal group x (1/◦C2).

The formulation of equation 8.14 represents a modification to the ICM formulation to allow for temperature range specification of optimum growth.

###### 145



<<<PAGE 159>>>

###### 8. EUTROPHICATION EFDC+ Theory



##### 8.1.3.1.1.4 Effect of Salinity

For models that are simulating algal groups affected by salinity (e.g. cyanobacteria), the growth limitation due to salinity can be calculated as:

STOXS2 STOXS2 +S2

(8.15) where,

f4(S) =

STOXS is the salinity at which the algal group growth is halved (ppt), and S is the salinity in water column (ppt) provided from the hydrodynamic model.

##### 8.1.3.1.2 Basal Metabolism

Algal biomass in the model decreases through basal metabolism (respiration and excretion), predation and death. In basal metabolism, algal matter (C, N, P, and SiO2) is returned to organic and inorganic pools in the environment, mainly to dissolved organic and inorganic matter. Respiration, which may be viewed as a reversal of photosynthesis, consumes DO. Basal metabolism is considered to be an exponentially increasing function of temperature:

BMx = BMRxexp(KTBx[T −TRx]) (8.16) where,

TRx is the reference temperature for basal metabolism for algal group x (◦C). BMRx is the basal metabolism rate at TRx for algal group x (1/day), and KTBx is the effect of temperature on metabolism for algal group x (1/◦C).

##### 8.1.3.1.3 Algal Predation

In cases, where there is limited data available regarding zooplankton, a constant predation rate can be specified for each algal group, which implicitly assumes zooplankton biomass is a constant fraction of algal biomass. Alternately, the predation rate can be taken as proportional to the algae biomass. Using a temperature effect similar to that for metabolism, the predation rate is given as:

αP

Bx BxP

PRx = PRRx

exp(KTPx[T −TPx]) (8.17) where,

TPx is the reference temperature rate for predation for algal group x, BxP is the reference algae concentration for predation (g C/m3), PRRx is the reference predation rate at BxP and TPx for algal group x (1/day), αP is the exponential dependence factor, and KTPx is the effect of temperature on predation for algal group x (1/◦C).

###### 146



<<<PAGE 160>>>

###### 8. EUTROPHICATION EFDC+ Theory



When the model simulates zooplankton, the predation of algae group x is estimated based on the utilization of zooplankton as:

PAz KHCz +PAz ·RMAXz ·Zz ·

UBxz.Bx

PAz · f(T) (8.18) where,

PRx =

Zz is the concentration of zooplankton group z (gCm−3), PAz is the prey available to zooplankton group z (gCm−3), KHCz is the prey density at which grazing is halved (gCm−3), RMAXz is the maximum ration of zooplankton group z (g prey C g−1 zooplankton C day−1), UBxz is the utilization of algal group x by zooplankton group z,

f(T) is the effect of temperature on grazing

The difference between predation and basal metabolism lies in the distribution of the end products of the two processes. In predation, algal matter (C, N, P, and SiO2) is returned to the organic and inorganic pools in the environment, mainly to particulate organic matter, compared to metabolism where the algal matter is returned to dissolved organic and inorganic matter. This distribution can be specified by the modeler.

It is also noted that predation in the EFDC+ water quality model follows the original formulation in the ICM model (Cerco and Cole, 1995) which uses a predation rate constant with total predation loss being proportional to algae concentration. Subsequent ICM documentation Cerco et al. (2000), appear to define predation independent of algae concentration.

##### 8.1.3.1.4 Algal Vertical Migration

The vertical migration of algae includes the settling process which removes algae from the water column and deposits it onto the bottom of the waterbody. The settling algae can be a significant source of nutrients to the sediment bed and can play an important role in the sediment diagenesis process. The settled algal biomass undergoes bacterial and biochemical reactions in the bed, and then releases nutrients back to the water column.

Additionally, some cyanobacteria can move vertically in the water column, independent of water velocity. According to Kromkamp and Mur (1984), the daily pattern of cyanobacteria vertical migration can be explained by increased cell density due to carbohydrate accumulation by photosynthesis in the light and decreased cell density due to utilization of carbohydrates in the dark. The vertical migration of those cyanobacteria species is thought to facilitate these species’ alternating access to the surface layers of a waterbody, where light is abundant, and photosynthesis can occur, and lower, more nutrient-rich layers. This can result in the creation of surface accumulations known as harmful algae blooms (HABs), which lead to reducing sunlight penetration in the water and subsequent oxygen depletion, harming fish, and other aquatic organisms. From EFDC+ 12, different models for the vertical movement of algae that have been added to the Water Quality module.

##### 8.1.3.1.4.1 Predefined velocity model

The vertical migration of cyanobacteria can be simulated using a predefined velocity function based on their typical movement patterns. The first model approach, based on Overman and Wells (2022), simply assumes

###### 147



<<<PAGE 161>>>

###### 8. EUTROPHICATION EFDC+ Theory



that the cyanobacteria migrate vertically on a daily cycle with a velocity depends on time as:

2π 86400

cos

vs(t) = A

2π 86400

t +ϕ (8.19)

Where, vs(ms−1) is the algae settling velocity, A(m) is the migration amplitude and the period is assumed to be one day (86400 s), ϕ (rad) is the phase shift which depends on the initial location of the colony. The second model approach is slightly more complex by assuming the velocity function is dependent both on time and on space. Modifying Equation 8.19 to include the variation in space of the amplitude as in Belov and Giles (1997) gives:

vs(t) =

A864002π cos 86400 2π t +ϕ e−α(H−z), Is > 0 A864002π cos 86400 2π t +ϕ , Is ≤ 0

(8.20)

Where, α is the light attenuation coefficient and Is(Wm−2) is solar irradiance at the water surface, H (m) is the water depth, z(m) is the depth coordinate. The addition of the exponential term is only applied when there is sunlight present. During the dark periods, the equation reduced to the Equation 8.19.

##### 8.1.3.1.4.2 Dynamic Velocity model

The predefined velocity models can predict cyanobacteria movement based on their observed tendency of migration on a daily cycle; however, they do not reflect the response of cyanobacteria to variations in solar irradiance. To capture this behavior, a dynamic velocity model was implemented based on Visser et al. (1997). In this model, the settling velocity is calculated dynamically by Stokes’s law based on the timevarying density of the cyanobacteria cell. Equations of relationship between density changes and photon irradiance were established and applied based on laboratory experiment data.

During periods when photon irradiance is higher than a compensation value Ic, the rate of density change is estimated using Equation 8.21:

dρ dx

N0 60

Ie−I/I0 +c, I ≥ Ic (8.21)

=

where No is a regression coefficient, I(Wm−2) is the photon irradiance at depth of colony, c is the rate of density change when I = 0, and Io(Wm−2) is the light intensity corresponding to the maximum density.

During periods of darkness when the photon irradiance is lower than the compensation value Ic, the density decreases at a rate calculated as:

dρ dx

= f1ρi + f2 I < Ic (8.22)

where, ρi(kgm−3) is the cell density at the end of the preceding light period, and f1 and f2 are regression coefficients. The numerical solutions of Equations 8.21 and 8.22 are given as:

ρin+1 = c1Ie−I/I0 +c2 ∆t +ρin I ≥ Ic (8.23)

ρin+1 = (f1(ρin +ρ∗)+ f2)∆t +ρin I < Ic (8.24)

where, ρi(n+1) is the cyanobacteria density of cell i at time n+1, ρ∗ is a correction factor to reflect the difference between the buoyant density modeled here and the non-buoyant density.

###### 148



<<<PAGE 162>>>

###### 8. EUTROPHICATION EFDC+ Theory



Once the new density is updated, it will be introduced into a modified Stokes’s law to calculate the settling velocity vs(t):

(ρi −ρw)R 9φn

vs(t) = 2gr2

(8.25)

Where g(ms−2) is the gravity acceleration, r(m) is the cell radius for Stokes, R is the ratio of cell volume to colony volume, φ is the drag coefficient of a cell for Stokes, n(kgm−1s−1) is the water viscosity, and ρi and ρw(kgm−3) are the densities of the cyanobacteria and water, respectively.

##### 8.1.3.2 Algae (immobile)

EFDC+ simulates unlimited groups of algae and macrophytes and the specification of a class as mobile or immobile determines if the class is attached to the channel bottom or substrate. Macrophytes and periphyton are common immobile classes. The major difference between modeling techniques for attached and freefloating classes are as follows: (1) attached algal classes are expressed in terms of areal densities rather than volumetric concentrations, (2) the availability of nutrients to the attached classes can be influenced by stream velocity, and (3) these classes are not subject to hydrodynamic transport.

##### 8.1.3.2.1 Production of Algae (immobile)

A good description of periphyton kinetics as it relates to water quality modeling can be found in Warwick et al. (1997) and has been used to develop the current section of this document.

A mass balance approach is used to model attached algae growth with C serving as the measure of standing crop size or biomass. For each model grid cell, the equation for growth is slightly different than the one for free-floating algae (equation 8.7):

Pm = PMm ·min(f1(N), f4(V))· f2(I)· f3(T)· f5(D) (8.26) where,

PMm is the maximum growth rate under optimal conditions for macroalgae,

- f1(N) is the effect of suboptimal nutrient concentration (0 ≤ f1 ≤ 1),
- f2(I) is the effect of suboptimal light intensity (0 ≤ f2 ≤ 1),
- f3(T) is the effect of suboptimal temperature (0 ≤ f3 ≤ 1),
- f4(V) is the velocity limitation factor (0 ≤ f4 ≤ 1), and
- f5(D) is the density dependent growth rate reduction factor (0 ≤ f5 ≤ 1).


Above a certain level, stream velocity has a stimulating effect on periphyton metabolism by mixing the overlying waters with nutrient poor waters that develop around cells (Whitford and Schumacher, 1964). On the other hand, excess velocities can cause scour and loss of biomass.

The effects of suboptimal velocity upon growth rate are represented in the model by a velocity limitation function. Two options are available in the model for specifying the velocity limitation: (1) a MichaelisMenton (or Monod) equation 8.27, and (2) a five-parameter logistic function equation 8.28. The Monod equation limits attached algae growth due to low velocities, whereas the five-parameter logistic function can be configured to limit growth due to either low or high velocities (see Figure 8.4).

###### 149



<<<PAGE 163>>>

###### 8. EUTROPHICATION EFDC+ Theory



- Velocity limitation option 1, the Michaelis-Menton equation is written as follows:

f4(V) =

U KMV +U

(8.27)

where, U is the stream velocity (m/s), and KMV is the half-saturation velocity (m/s).

- Velocity limitation option 2, the five-parameter logistic function is as follows:


a−d 1+ Uc b

e (8.28)

f4(V) = d +

where, U is the stream velocity (m/s),

- a is the asymptote at minimum x,
- b is the slope after asymptote a,
- c is the x-translation,
- d is the asymptote at maximum x, and
- e is the slope before asymptote d.


|0.0<br><br>0.2<br><br>0.4<br><br>0.6<br><br>0.8<br><br>1.0<br><br>0.00 0.50 1.00 1.50 2.00<br><br>VelocityLimitationFactor<br><br>Velocity (m/s)<br><br>| | | |Lo<br><br>M|gistic Function onod Function|
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
|
|---|


- Fig. 8.4. Velocity limitation function for (Option 1) the Monod equation where KMV = 0.25m/s and KMVmin = 0.15m/s, and (Option 2) the 5-parameter logistic function where a = 1.0, b = 12.0, c = 0.3, d = 0.35, and e = 3.0 (high velocities are limiting).


###### 150



<<<PAGE 164>>>

###### 8. EUTROPHICATION EFDC+ Theory



The half-saturation velocity in equation 8.27 is the velocity at which half the maximum growth rate occurs. This effect is analogous to the nutrient limitation because at low stream velocity, the exchange of nutrients between the algal matrix and the overlying water (Runke, 1985) is lower, and it increases with the increase in stream velocity. However, this formula can be too limiting at low velocities or still water. Therefore, the function is applied only at velocities above a minimum threshold level (KMVmin). When velocities are at or below this lower level, the limitation function is applied at the minimum level. Above this velocity, the current produces a steeper diffusion gradient around the macrophytes and periphyton (Whitford and Schumacher, 1964). A minimum formulation is used to combine the limiting factors for N, P, velocity and the most severely limiting factor alone limits macrophytes and periphyton growth. Note that the equation 8.28 can be configured so that low velocities are limiting by setting parameter d greater than parameter a, and vice versa to limit growth due to high velocities. In waters that are rich in nutrients, low velocities will not limit growth. However, high velocities may cause scouring and detachment of the macroalgae resulting in a reduction in biomass. The five-parameter logistic function can be configured to approximate this reduction by limiting growth at high velocities.

Macrophytes and periphyton growth can also be limited by the availability of suitable substrate (Ross and Ultsch, 1980). Macroalgae communities reach maximum rates of primary productivity at low levels of biomass (McIntire, 1973; Pfeifer and McDiffett, 1975). The relationship between standing crop and production employs the Michaelis-Menton kinetic equation as shown below:

KBP KBP+MACm

f5(D) =

(8.29) where,

KBP is the half-saturation biomass level (g C/m2), and MACm is the macroalgae biomass level (g C/m2).

The half-saturation biomass level, KBP, is the biomass at which half the maximum growth rate occurs. Caupp et al. (1991) used a KBP value of 5.0g C/m2 (assuming 50% of ash free dry mass is C) for a region of the Truckee River system in California. The function in equation 8.29 allows maximum rates of primary productivity at low levels of biomass with decreasing rates of primary productivity as the community matrix expands.

##### 8.1.3.2.2 Growth and death between the cell layers

From EFDC+ 11, the kinetic of immobile or attached algae is handled to grow upwards from the bed layer through model layers. This feature provides an extension from the modeling of submerged macrophyte, which is originally attached and exists only at the bottom layer, to suspended canopy such as suspended aquaculture farms.

###### 151



<<<PAGE 165>>>

###### 8. EUTROPHICATION EFDC+ Theory



- Fig. 8.5. a) Macrophytes grow in vertical columns from bottom upwards and its impact on flow velocity. b) Plan view of macrophyte’s impact on flow velocity


- Figure 8.5a illustrates the macrophyte growing upwards from the bottom through model layers. A layered threshold value of biomass concentration is specified for the simulated macrophyte group. Growth upward is accomplished by moving the biomass of a layer to the layer above if the macrophyte concentration in the layer is greater than a threshold value and the concentration in the upper layer is less than the same threshold value. The canopy’s height HM is calculated as:

HM = min

∑KCK=1BM BMLim

,HMMax (8.30)

where HMMax is the maximum value of the canopy’s height and BMLim is the threshold biomass concentration.

Additionally, macrophyte shading is modeled by making light attenuation a function of macrophyte concentration.

8.1.3.2.3 Macrophyte hydrodynamics impacts

- Figure 8.5b illustrates the impact of macrophyte on the flow velocity. Similar to the vegetation drag described in Section 2.2.2, the resistance of flow through macrophyte is dependent on the flow velocity, macrophyte distribution and its hydrodynamic properties associated with stems and leaves. To model the additional flow resistance of macrophyte, drag of individual stems and leaves is summed to determine the total drag force in a model cell. Here, the drag force on a rigid obstacle has been introduced as a sink term in the momentum equations (2.2) and (2.3), and can be calculated as:


FD = ρ

U2 2

CDλ (8.31)

where U is the velocity averaged, CD is the experimental drag coefficient which corresponds to the shape and diameter of the macrophyte, λ is the stem density.

###### 152



<<<PAGE 166>>>

###### 8. EUTROPHICATION EFDC+ Theory



##### 8.1.3.3 Zooplankton

Zooplankton are assumed to be non-mobile and are transported only by advection and dispersion. Sources and sinks of zooplankton included in the model are;

- 1. Grazing
- 2. Basal metabolism
- 3. Mortality
- 4. Predation
- 5. External loads


Each zooplankton group is represented by an identical production equation. The kinetic equation describing this process is:

∂Zz ∂t

WZz V

(8.32) where,

= (Gz −BMz −Dz −PRz)Zz +

Zz is the zooplankton biomass of zooplankton group z (gCm−3), t is the time (day), Gz is the grazing rate of zooplankton group z (day−1), BMz is the basal metabolism rate of zooplankton group z (day−1), Dz is the mortality rate of zooplankton group z (day−1), PRz is the predation rate of zooplankton group z (day−1), WZz is the external loads of zooplankton group z (gCday−1), and V is the model cell volume (m3).

##### 8.1.3.3.1 Zooplankton growth

The growth rate of zooplankton is assumed to be a function of food and temperature. Food for zooplankton includes phytoplankton and detritus as POCs. Assimilation efficiency of zooplankton is applied under the assumption that all prey grazed is assimilated.

where,

PAz KHCz +PAz

.RMAXz.f(T) (8.33)

Gz =

PAz is the prey available to zooplankton group z (gCm−3), KHCz is the prey density at which grazing is halved (gCm−3), RMAXz is the maximum ration of zooplankton group z (g prey C g−1 zooplankton C day−1), and f(T) is the effect of temperature on grazing.

###### 153



<<<PAGE 167>>>

###### 8. EUTROPHICATION EFDC+ Theory



1. Available prey

Zooplankton are generally assumed to graze on phytoplankton and POC. To compute the available prey from phytoplankton for each zooplankton group, a threshold concentration CTz is defined below which prey is not grazed. The portion of phytoplankton group x as a food source for zooplankton group z then can be determined as:

BAxz = Max(Bxz −CTz,0) (8.34) where,

BAxz is the portion of phytoplankton group x available to zooplankton group z (gCm−3), CTz is the threshold concentration of zooplankton group z (gCm−3)

When the model simulates several zooplankton groups such as microzooplankton and mesozooplankton, the microzooplankton becomes an important prey for the mesozooplankton. For these cases, EFDC+ allows the user to classify all the zooplankton groups into two general groups; predator and prey. A general formulation of total available prey including the food source from POC for a zooplankton predator group is expressed as:

PAz =ULz.LPOCAz+URz.RPOCAz+∑UBxz.BAxz+UZz.ZA (8.35) PAz is the available prey to zooplankton predator group z (gCm−3), ULz is the utilization of LPOC by zooplankton predator group z, URz is the utilization of RPOC by zooplankton predator group z, UBxz is the utilization of phytoplankton group x by zooplankton predator group z, LPOCAz is the LPOC available to the zooplankton predator group z (gCm−3), RPOCAz is the RPOC available to the zooplankton predator group z (gCm−3), BAxz is the phytoplankton group x available to the zooplankton predator group z (gCm−3), ZA is the total zooplankton prey biomass (gCm−3), and UZz is the utilization of total zooplankton prey by zooplankton predator group z.

The total available prey for a zooplankton prey group can be obtained by simply removing the zooplankton prey biomass term in 8.35.

PAz =ULz.LPOCAz+URz.RPOCAz+∑UBxz.BAxz (8.36)

2. Temperature effect The effect of temperature on grazing is described as:

 

- exp(−KTg1·(T −Topt1)2), T ≤Topt1 1, Topt1 < T < Topt2
- exp(−KTg2·(T −Topt2)2), T ≥Topt2


f(T) =



where,

- KTg1 is the effect of temperature below optimal on grazing (◦C−2),
- KTg2 is the effect of temperature above optimal on grazing (◦C−2), and Topt is the optimal temperature for grazing (◦C).


(8.37)

###### 154



<<<PAGE 168>>>

###### 8. EUTROPHICATION EFDC+ Theory



- 8.1.3.3.2 Basal metabolism Basal metabolism of zooplankton is represented as an exponentially increasing function of temperature:

BMz = BMRz ·exp(KTBz ·(T −Trz)) (8.38) where,

Trz is the reference temperature for metabolism of zooplankton group z (◦C), BMRz is the metabolism rate of zooplankton group z at temperature Trz (day−1), and KTBz is the effect of temperature on metabolism of zooplankton group z (◦C−1)

- 8.1.3.3.3 Mortality

Zooplankton are subject to death at low DO concentration. The death term is zero at a threshold DO and increases as DO decreases. The death rate is calculated as:

Dz = DZEROz(1−

DOref DOCRITz

) (8.39)

where,

Dz is the death rate of zooplankton group z (day−1), DZEROz is the death rate of zooplankton group z at zero DO concentration (day−1), DOCRITz is the DO threshold below which zooplankton death occurs (gDOm−3), and DOref is the DO concentration when DO < DOCRIT, otherwise zero (gDOm−3)

- 8.1.3.3.4 Predation on Zooplankton


Zooplankton can be eaten by higher level predators that are not represented in the model (e.g., jellyfish, finfish). Zooplankton predation is calculated using an exponential function of temperature as:

PRz = PRRz ·exp(KTPz ·(T −Trz)) (8.40) where,

Trz is the reference temperature for predation of zooplankton group z (◦C), PRRz is the predation rate of zooplankton group z at temperature Trz (day−1), and KTPz is the effect of temperature on predation of zooplankton group z (◦C−1)

- 8.1.3.4 Organic Carbon (OC) EFDC+ models three state variables for OC: refractory particulate, labile particulate, and dissolved.


###### 155



<<<PAGE 169>>>

###### 8. EUTROPHICATION EFDC+ Theory



- 8.1.3.4.1 Particulate Organic Carbon (POC) For LPOC and RPOC, sources and sinks included in the model are (Figure 8.2);


- 1. Algal death and predation,
- 2. Zooplankton death and predation,
- 3. Uptake by zooplankton growth,
- 4. Dissolution to DOC,
- 5. Settling, and
- 6. External loads.


The governing equations for LPOC and RPOC are:

∂RPOC ∂t

### = ∑

FCRPx·Dx·Bx+ ∑

algae

zoopl

∂LPOC ∂t

### = ∑

FCLPx·Dx·Bx+ ∑

algae

zoopl

where,

URz ·RPOC

FCRDZz ·Dz +FCRPZz ·PRz −

PAz ·Rz ·Zz −KRPOC ·RPOC+

∂ ∂Z

WRPOC V

(WSRP ·RPOC)+

ULz ·LPOC

FCLDZz ·Dz +FCLPZz ·PRz −

PAz ·Rz ·Zz −KLPOC ·LPOC+

∂ ∂Z

WLPOC V

(WSLP ·LPOC)+

(8.41)

(8.42)

RPOC is the concentration of RPOC (g C/m3), LPOC is the concentration of LPOC (g C/m3), Dx is the death (predated) rate of algae group z (day−1), FCRPx is the fraction of dead (or predated) C produced as RPOC by algal group x, FCLPx is the fraction of dead (or predated) C produced as LPOC by algal group x, FCRDZz is the fraction of dead C produced as RPOC by zooplankton group z, FCLDZz is the fraction of dead C produced as LPOC by zooplankton group z, FCRPZz is the fraction of predated C produced as RPOC by zooplankton group z, FCLPZz is the fraction of predated C produced as LPOC by zooplankton group z URz is the utilization of RPOC by zooplankton group z, ULz is the utilization of LPOC by zooplankton group z, KRPOC is the dissolution rate of RPOC (1/day), KLPOC is the dissolution rate of LPOC (1/day), WSRP is the settling velocity of RPOC (m/day),

###### 156



<<<PAGE 170>>>

###### 8. EUTROPHICATION EFDC+ Theory



WSLP is the settling velocity of LPOC (m/day), WRPOC is the external loads of RPOC (g C/day), and WLPOC is the external loads of LPOC (g C/day.)

The rate of total C uptake by zooplankton group z is the product of the maximum ration Rz and its biomass. The ration Rz (g prey C g−1 zooplankton C day−1) can be calculated as:

PAz KHCz +PAz

.RMAXz.f(T) (8.43)

Rz =

where,

PAz is the prey available to zooplankton group z (gCm−3), KHCz is the prey density at which grazing is halved (gCm−3), RMAXz is the maximum ration of zooplankton group z (g prey C / g zooplankton C/day) f(T) is the effect of temperature on grazing

- 8.1.3.4.2 Dissolved Organic Carbon (DOC) Sources and sinks for DOC included in EFDC+ are (Figure 8.2);


- 1. Algal excretion (exudation) and death and predation,
- 2. Zooplankton predation and death,
- 3. Dissolution from LPOC and RPOC,
- 4. Heterotrophic respiration of DOC (decomposition),
- 5. Denitrification, and
- 6. External loads.


The rate of change in DOC can be calculated as:

∂DOC ∂t

### = ∑

algae

KHRx

KHRx+DO ·BMx·Bx+ ∑

FCDx +(1−FCDx)

FCDPx ·Dx ·Bx

algae

### + ∑

(FCDDZ ·Dz +FCDPZ ·PRz)·Zz +KRPOC ·RPOC

zoopl

WDOC V

+KLPOC ·LPOC−KHR ·DOC−Denit ·DOC+

where,

(8.44)

DOC is the concentration of DOC (g C/m3), FCDx is the fraction of basal metabolism exuded as DOC at infinite DO concentration for algal group x, KHRx is the half-saturation constant of DO for DOC excretion by group x (g O2/m3), DO is the DO concentration (g O2/m3),

###### 157



<<<PAGE 171>>>

###### 8. EUTROPHICATION EFDC+ Theory



FCDPx is the fraction of dead (or predated) C produced as DOC by algae group x, FCDDZz is the fraction of dead C produced as DOC by zooplankton group z, FCDPZz is the fraction of predated C produced as DOC by zooplankton group z, KHR is the heterotrophic respiration rate of DOC (1/day), Denit is the denitrification rate (1/day), and WDOC is the external loads of DOC (g C/day).

The remainder of this section explains each term in equations 8.41-8.44.

##### 8.1.3.4.3 Effect of Algae on Organic Carbon (OC) 8.1.3.4.3.1 Basal Metabolism

Basal metabolism, consisting of respiration and excretion, returns algal matter (C, N, P, and SiO2) back to the environment. Loss of algal biomass through basal metabolism is calculated as:

∂Bx ∂t

= −BMxBx (8.45)

The equation 8.45 indicates that the total loss of algal biomass due to basal metabolism is independent of ambient DO concentration. In EFDC+, it is assumed that the distribution of total loss between respiration and excretion is constant as long as there is sufficient DO for algae to respire. Under that condition, the losses by respiration and excretion may be written as:

(1−FCDx)BMxBx : respiration (8.46)

FCDxBMxBx : excretion (8.47) where, FCDx is a constant of value between 0 and 1.

Although the total loss of algal biomass due to basal metabolism is O independent (equation 8.45), the distribution of total loss between respiration and excretion is O-dependent, as algae cannot respire in absence of O. When O level is high, respiration is a large fraction of the total. As DO becomes scarce, excretion becomes dominant. Thus, equation 8.46 represents the loss by respiration only at high O levels. In general, equation 8.46 can be decomposed into two fractions as a function of DO availability:

(1−FCDx)

DO KHRx +DO

BMxBx : respiration (8.48)

KHRx KHRx +DO

(1−FCDx)

where, KHRx is the metabolic DO coefficient (g/m3 O2).

BMxBx : excretion (8.49)

Equation 8.48 represents the loss of algal biomass by respiration, and equation 8.49 represents additional excretion due to insufficient DO concentration. The parameter KHRx, which is defined as the half-saturation

###### 158



<<<PAGE 172>>>

###### 8. EUTROPHICATION EFDC+ Theory



constant of DO for algal DOC excretion in equation 8.44, can also be defined as the half-saturation constant of DO for algal respiration in equation 8.49.

Combining equations 8.47 and 8.49 the total loss due to excretion can be calculated as

FCDx +(1−FCDx)

KHRx KHRx +DO

BMxBx (8.50)

Equations 8.48 and 8.50 combine to give the total loss of algal biomass due to basal metabolism. The definition of the fraction FCDx in equation becomes apparent in equation 8.50, i.e., fraction of basal metabolism exuded as DOC at infinite DO concentration. At zero oxygen level, the total loss due to basal metabolism is by excretion regardless of FCDx.

The end C product of respiration is primarily Carbon dioxide (CO2), an inorganic form not considered in the present model, while the end C product of excretion is primarily DOC. Therefore, equation 8.50, that appears in equation 8.44, represents the contribution of excretion to DOC, and there is no source term for POC from algal basal metabolism in equations 8.41 and 8.42.

Although this general formulation is incorporated for consistency with the original CE-QUAL-IMC formulation (Cerco and Cole, 1995), most of the subsequent applications of ICM have simplified the basal metabolism in the published DOC and DO equations or specified input parameters which effectively set KHRx and FCDx to zero (see Table 8.2), which results in simplifying the DOC equation to:

∂DOC ∂t

### = ∑

FCDPxPRxBx +KRPOCRPOC+KLPOCLPOC

algae

WDOC V

−KHRDOC−Denit DOC+

(8.51)

Table 8.2. Basal Metabolism Formulations and Parameter in ICM

Study FCDx and KHRx in DOC Equation

FCDx and KHRx in from DO Equation

Cerco and Cole (1995) (Chesapeake Bay)

General General

Bunch et al. (2000) (San Juan Bay, PR)

General (used FCD = 0, KHRx = 0.5)

General (used FCD = 0, KHRx = 0.5)

Cerco et al. (2000) (Florida Bay) No BMx source in equation, implies FCDx = 0, KHRx = 0

Consistent with FCDx = 0, KHRx = 0

Cerco et al. (2002) (Chesapeake Bay, Trib. Refinements)

No BMx source in equation, implies FCDx = 0, KHRx = 0

Consistent with FCDx = 0, KHRx = 0

Cerco et al. (2004) (Lake Washington)

Equation implies KHRx = 0 (used FCDx = 0)

Consistent with KHRx = 0 (used FCDx = 0)

Tillman et al. (2004) (St. Johns River)

No BMx source in equation, implies FCDx = 0, KHRx = 0

Consistent with FCDx = 0, KHRx = 0

###### 159



<<<PAGE 173>>>

###### 8. EUTROPHICATION EFDC+ Theory



##### 8.1.3.4.3.2 Predation

Algae produce OC through the effects of predation. Zooplankton takes up and redistributes algal C through grazing, assimilation, respiration, and excretion. In case that zooplankton are not included in the model, routing of algal C through zooplankton predation is simulated by empirical distribution coefficients in equations 8.41 to 8.44; FCRPx, FCLPx and FCDPx. The sum of these three predation fractions for each algal class should be unity.

##### 8.1.3.4.4 Heterotrophic Respiration and Dissolution

The RPOC and LPOC equations 8.41 and 8.44 contain decay terms that represent dissolution of particulate material into dissolved material. These terms appear in equation 8.44 as sources. The third sink term in the DOC equation 8.44 represents heterotrophic respiration of DOC. The oxic heterotrophic respiration is a function of DO; the lower the DO, the smaller the respiration term becomes. Heterotrophic respiration rate, therefore, is expressed using a Monod function of DO;

where,

KHR =

DO KHORDO +DO

KDOC (8.52)

KHORDO is the oxic respiration half-saturation constant for DO (g O2/m3), and KDOC is the heterotrophic respiration rate of DOC at infinite DO concentration (1/day).

Dissolution and heterotrophic respiration rates depend on the availability of carbonaceous substrate and on heterotrophic activity. Algae produce labile C that fuels heterotrophic activity; dissolution and heterotrophic respiration do not require the presence of algae though, and may be fueled entirely by external C inputs. In the model, algal biomass, as a surrogate for heterotrophic activity, is incorporated into formulations of dissolution and heterotrophic respiration rates. Formulations of these rates require specification of algaldependent and algal-independent rates:

KRPOC = KRC+KRCalg ∑

Bx exp(KTHDR(T −TRHDR)) (8.53)

algae

KLPOC = KLC+KLCalg ∑

Bx exp(KTHDR(T −TRHDR)) (8.54)

algae

where,

KDOC = KDC+KDCalg ∑

Bx exp(KTMIN (T −TRMIN)) (8.55)

algae

KRC is the minimum dissolution rate of RPOC (1/day), KLC is the minimum dissolution rate of LPOC (1/day), KDC is the minimum respiration rate of DOC (1/day),

###### 160



<<<PAGE 174>>>

###### 8. EUTROPHICATION EFDC+ Theory



KRCalg,KLCalg are the constants that relate dissolution of RPOC and LPOC, respectively, to algal biomass

(1/day; per g C/m3), KDCalg is the constant that relates respiration to algal biomass (1/day per g C/m3), KTHDR is the effect of temperature on the hydrolysis of Particulate Organic Matter (POM) (1/◦C), TRHDR is the reference temperature for hydrolysis of POM (◦C), KTMIN is the effect of temperature on mineralization of dissolved organic matter (1/◦C), and TRMIN is the reference temperature for mineralization of dissolved organic matter (◦C).

Equations 8.53 to 8.55 have exponential functions that relate rates to temperature.

In EFDC+, the term “hydrolysis” is defined as the process by which POM is converted to dissolved organic form, and thus includes both dissolution of particulate C and hydrolysis of particulate P and N. Therefore, the parameters KTHDR and TRHDR, are also used for the temperature effects on hydrolysis of particulate P (equations 8.66 and 8.67) and N (equations 8.76 and 8.77). The term “mineralization” is defined as the process by which dissolved organic matter is converted to dissolved inorganic form, and thus includes both heterotrophic respiration of DOC and mineralization of DOP and DON. Therefore, the parameters, KTMIN and TRMIN, are also used for the temperature effects on mineralization of dissolved P 8.68 and N 8.78.

##### 8.1.3.4.5 Effect of Denitrification on Dissolved Organic Carbon (DOC)

As O is depleted from natural systems, organic matter is oxidized by the reduction of alternate electron acceptors. Thermodynamically, the first alternate acceptor reduced in the absence of O is NO−

3 . According to Stumm et al. (1970), the reduction of NO−

3 by a large number of heterotrophic anaerobes is referred to as denitrification, and the stoichiometry of this reaction is:

4NO−

3 +4H+ +5CH2O → 2N2 +7H2O+5CO2 (8.56)

The second last term in the equation 8.44 accounts for the effect of denitrification on DOC. The kinetics of denitrification in the model are first-order:

KHORDO KHORDO +DO

NO3 KHDNN +NO3

Denit =

AANOX ·KDOC (8.57) where,

KHORDO is the denitrification half-saturation constant for DO (g O/m3), KHDNN is the denitrification half-saturation constant for NO−

3 (g N/m3), and AANOX is the ratio of denitrification rate to oxic DOC respiration rate.

In equation 8.57, the DOC respiration rate KDOC, is modified so that significant decomposition via denitrification occurs only when NO−

3 is freely available and DO is depleted. The ratio AANOX, makes the anoxic respiration slower than oxic respiration. Note that KDOC, defined in equation 8.55, includes the temperature effect on denitrification.

###### 161



<<<PAGE 175>>>

###### 8. EUTROPHICATION EFDC+ Theory



##### 8.1.3.5 Phosphorus (P)

EFDC+ has four state variables for P; three organic forms (RPOP, LPOP, and DOP), and one inorganic form (Total Phosphate as Phosphorus (PO4t)). PO4t represents the sum of Dissolved Phosphate as Phosphorus (PO4d) and Sorbed Phosphate as Phosphorus (PO4p) in the water phase, but exclude PO−3

4 in algae cells.

- 8.1.3.5.1 Particulate Organic Phosphorus (POP) For RPOP and LPOP, sources and sinks included in EFDC+ are (Figure 8.2);


- 1. Algal basal metabolism, death and predation,
- 2. Zooplankton death and predation,
- 3. Uptake by zooolankton growth,
- 4. Dissolution to DOP,
- 5. Settling, and
- 6. External loads.


The kinetic equations for RPOP and LPOP are;

where,

∂RPOP ∂t

### = ∑

(FPRx·BMx+FPRPx·Dx)·APC·Bx+ ∑

FPRDZz ·Dz ·Zz ·APCz

algae

zoopl

URz ·RPOP

### + ∑

PAz ·Rz)·Zz ·APCz −KRPOP ·RPOP+

(FPRPZz ·PRz −

zoopl

∂ ∂Z

WRPOP V

(WSRP ·RPOP)+

∂LPOP ∂t

### = ∑

(FPLx·BMx+FPLPx·Dx)·APC·Bx+ ∑

FPLDZz ·Dz ·Zz ·APCz

algae

zoopl

ULz ·LPOP

### + ∑

PAz ·Rz)·Zz ·APCz −KLPOP ·LPOP+

(FPLPZz ·PRz −

zoopl

∂ ∂Z

WLPOP V

(WSLP ·LPOP)+

RPOP is the concentration of RPOP (g P/m3), LPOP is the concentration of LPOP (g P/m3),

FPRx is the fraction of metabolized P by algal group x produced as RPOP, FPLx is the fraction of metabolized P by algal group x produced as LPOP, FPRPx is the fraction of death (or predated) P produced as RPOP by algae group x, FPLPx is the fraction of death (or predated) P produced as LPOP by algae group x,

(8.58)

(8.59)

###### 162



<<<PAGE 176>>>

###### 8. EUTROPHICATION EFDC+ Theory



FPRDZz is the fraction of death P produced as RPOP by zooplankton group z, FPLDZz is the fraction of death P produced as LPOP by zooplankton group z, FPRPZz is the fraction of predated P produced as RPOP by zooplankton group z, FPLPZz is the fraction of predated P produced as LPOP by zooplankton group z, APC is the mean algal P-to-C ratio for all algal groups (g P per g C), APCz is the P-to-C ratio for zooplankton (g P per g C), KRPOP is the hydrolysis rate of RPOP (1/day), KLPOP is the hydrolysis rate of LPOP (1/day), WRPOP is the external loads of RPOP (g P/day), and WLPOP is the external loads of LPOP (g P/day).

- 8.1.3.5.2 Dissolved Organic Phosphorus (DOP) Sources and sinks for DOP included in the model are (Figure 8.2);


- 1. Algal basal metabolism, death and predation,
- 2. Zooplankton basal metabolism, death and predation,
- 3. Dissolution from RPOP and LPOP,
- 4. Mineralization to PO−3

4 , and

- 5. External loads.


The kinetic equation describing these processes is:

where

∂DOP ∂t

### = ∑

(FPDx BMx+FPDPx Dx)APC Bx+ ∑

FPDBZz ·BMz ·Zz ·APCz

algae

zoopl

### + ∑

(FPDDZ ·Dz +FPDPZ ·PRz)·Zz ·APCz

zoopl

WDOP V

+KRPOP ·RPOP+KLPOP ·LPOP−KDOP ·DOP+

(8.60)

DOP is the concentration of DOP (g P/m3), FPDx is the fraction of metabolized P produced as DOP by algal group x, FPDPx is the fraction of death (or predated) P produced as DOP by algal group x, FPDBZz is the fraction of metabolized P produced as DOP by zooplankton group z, FPDDZz is the fraction of death P produced as DOP by zooplankton group z, FPDPZz is the fraction of predated P produced as DOP by zooplankton group z, KDOP is the mineralization rate of DOP (1/day), and WDOP is the external loads of DOP (g P/day).

###### 163



<<<PAGE 177>>>

###### 8. EUTROPHICATION EFDC+ Theory



##### 8.1.3.5.3 Total Water Phase Phosphate

For PO4t that includes both PO4d and PO4p in the water phase, sources and sinks included in the model are;

- 1. Algal basal metabolism, predation, and uptake,
- 2. Zooplankton basal metabolism, death and predation,
- 3. Mineralization from DOP,
- 4. Settling of PO−3

4 ,

- 5. Sediment-water exchange of PO4d for the bottom layer only, and
- 6. External loads.


The kinetic equation describing these processes is:

where,

∂ ∂t

(PO4p+PO4d)= ∑

(FPIx BMx +FPIPx Dx −Px)APC·Bx +KDOP ·DOP

algae

### + ∑

(FPIBZz ·BMz +FPIDZz ·Dz +FPIPZz ·PRz)Zz ·APCz

zoopl

∂ ∂Z

BFPO4d ∆Z

WPO4p V

WPO4d V

(WSTSS ·PO4p)+

+

+

+

(8.61)

PO4t is PO4d + PO−3

4 ] (g P/m3), PO4d is the dissolved phosphate as P (g P/m3), PO4p is the sorbed phosphate as P (g P/m3), FPIx is the fraction of metabolized P by algal group x produced as inorganic P, FPIPx is the fraction of death (or predated) P produced as inorganic P by algal group x, FPIBZz is the fraction of metabolized P produced as PO−3

4 by zooplankton group z, FPIDZz is the fraction of P produced as PO−3

4 by zooplankton group z as a result of death, FPIPZz is the fraction of P produced as PO−3

4 by zooplankton group z as a result of predation, WSTSS is the settling velocity of suspended solid (m/day), provided by the hydrodynamic model, BFPO4d is the sediment-water exchange flux of PO−3

4 (g P/m2/day), applied to the bottom layer only, and

WPO4t is the external loads of PO4t (g P/day).

In equation 8.61, if the TAM is chosen as a measure of sorption site, the settling velocity of TSS WSTSS, is replaced by that of particulate metal WSs. The remainder of this section explains each term in equations 8.58 to 8.61. Alternate forms of the PO4t equation are discussed in next paragraph.

###### 164



<<<PAGE 178>>>

###### 8. EUTROPHICATION EFDC+ Theory



##### 8.1.3.5.4 Total Phosphate (PO4t)

Suspended and bottom sediment particles (clay, silt, and metal hydroxides) sorb and desorb PO−3

4 in river and estuarine waters. This sorption-desorption process buffers PO−3

4 concentration in the water column and enhances the transport of PO−3

4 away from its external sources (Carritt and Goodgal, 1954; Froelich, 1988). To ease the computational complication due to the sorption-desorption of PO−3

4 , PO4d and PO4p are treated and transported as a single state variable. Therefore, the model PO−3

4 state variable PO4t, is defined as the sum of PO4d and PO4p (equation 8.61), and the concentrations for each fraction are determined by equilibrium partitioning of their sum.

In ICM, sorption of PO−3

4 to particulate species of metals including Fe and Mn was considered based on a phenomenon observed in the monitoring data from the mainstem of the Chesapeake Bay, where the PO4p rapidly depleted from anoxic bottom waters during the autumn reaeration event (Cerco and Cole, 1994). Their hypothesis was that the reaeration of bottom waters caused dissolved Fe and Mn to precipitate, and PO−3

4 sorbed to newly formed metal particles and rapidly settled to the bottom. One state variable TAM was defined as the sum of all metals that acts as sorption sites, and the TAM was partitioned into particulate and dissolved fractions via an equilibrium partitioning coefficient. Then PO−3

4 was assumed to sorb to only the

particulate fraction of the TAM. In the treatment of PO−3

4 sorption in ICM, the particulate fraction of metal hydroxides was emphasized as a sorption site in bottom waters under anoxic conditions. Phosphorus is a highly particle-reactive element, and PO−3

4 in solution reacts quickly with a wide variety of surfaces, being taken up by and released from particles Froelich (1988). EFDC+ has two options, SED or TSS and TAM, as a measure of a sorption site for PO−3

4 , and dissolved and sorbed fractions are determined by equilibrium partitioning of their sum as a function of SED or TAM concentration:

where,

PO4p =

PO4d =

KPO4pSORPS 1+KPO4pSORPS

1 1+KPO4pSORPS

SORPS = SED or TAMP

(PO4p+PO4d)

(PO4p+PO4d)

(8.62)

KPO4p is the empirical coefficient relating PO−3

4 sorption to SED (per g/m3) or particulate TAM

(per mol/m3) concentration, SED is the total cohesive sediment concentration (mg/l), and TAMp is the particulate TAM (mol/m3).

The definition of the partition coefficient alternately follows from equation 8.62 as:

PO4p PO4d

1 SED

KPO4p =

PO4p PO4d

1 TAMp

KPO4p =

(8.63)

(8.64)

where the meaning of KPO4p becomes apparent, i.e., the ratio of PO4p to PO4d per unit concentration of SED or particulate TAM (i.e., per unit sorption site available).

###### 165



<<<PAGE 179>>>

###### 8. EUTROPHICATION EFDC+ Theory



##### 8.1.3.5.5 Algal Phosphorus-to-Carbon Ratio (APC)

Algal biomass is quantified in units ofC per volume of water. In order to express the effects of algal biomass on P and N, the ratios of P-to-C and N-to-C in algal biomass must be specified. Although global mean values of these ratios are well known (Redfield, 1963), algal composition varies especially as a function of nutrient availability. As P and N become scarce, algae adjust their composition so that smaller quantities of these vital nutrients are required to produce carbonaceous biomass (Di Toro, 1980). Examining the field data from the surface of upper Chesapeake Bay, Cerco and Cole (1993) showed that the variation of N-to-C stoichiometry was small and thus used a constant algal N-to-C ratio ANCx. Large variations, however, were observed for algal P-to-C ratio indicating the adaptation of algae to ambient P concentration (Cerco and Cole, 1993); algal P content is high when ambient P is abundant and is low when ambient P is scarce. Thus, a variable algal P-to-C ratio APC, is used in model formulation. A mean ratio for all algal groups APC, is described by an empirical approximation to the trend observed in field data (Cerco and Cole, 1994):

APC = (CP1prm +CP2prmexp(−CP3prmPO4d) )−1 (8.65) where

- CP1prm is the minimum C-to-P ratio (g C per g P),
- CP2prm is the difference between minimum and maximum C-to-P ratio (g C per g P), and
- CP3prm is the effect of dissolved phosphate concentration on C-to-P ratio (per g P/m3).


##### 8.1.3.5.6 Effect of Algae on Phosphorus

The terms within summation in equations 8.58 to 8.61 account for the effects of algae on P. Both basal metabolism (respiration and excretion) and predation are considered, and thus formulated, to contribute to organic and inorganic P. That is, the total loss by basal metabolism (BMx ·APC ·Bx) is distributed using distribution coefficients (FPRx, FPLx, FPDx, and FPIx). When the model does not include zooplankton, the total loss by predation (PRx·APC·Bx), is also distributed using distribution coefficients (FPRPx, FPLPx, FPDPx, and FPIPx). The sum of four distribution coefficients for basal metabolism should be unity, and as is the sum for predation. Algae take up dissolved PO−3

4 for growth, and algae uptake of PO−3

4 is represented by (∑Px ·APC·Bx) in equation 8.61.

##### 8.1.3.5.7 Mineralization and Hydrolysis

The third term on the RHS of equations 8.58 and 8.59 represents hydrolysis of Particulate Organic Phosphorus (POP) and the last term in equation 8.60 represents mineralization of DOP. Mineralization of organic P is mediated by the release of nucleotidase and phosphatase enzymes by bacteria Chr´ost and Overbeck (1987) and algae Boni et al. (1989). Since the algae themselves release the enzymes, and bacterial abundance is related to algal biomass, the rate of organic P mineralization is related to algal biomass in model formulation. This mechanism is included in the model formulation where the algae stimulate the production of an enzyme that mineralizes organic P to PO−3

4 when PO−3

4 is scarce (Boni et al., 1989; Chr´ost and Overbeck, 1987). The formulations for hydrolysis and mineralization rates, including these processes, are:

KRPOP = KRP +

KHP KHP+PO4d

KRPalg ∑

Bx exp(KTHDR(T −TRHDR)) (8.66)

algae

###### 166



<<<PAGE 180>>>

###### 8. EUTROPHICATION EFDC+ Theory



KLPOP = KLP +

KHP KHP+PO4d

KLPalg ∑

Bx exp(KTHDR(T −TRHDR)) (8.67)

alage

where,

KDOP = KDP +

KHP KHP+PO4d

KDPalg ∑

Bx exp(KTMIN (T −TRMIN)) (8.68)

algae

KRP is the minimum hydrolysis rate of RPOP (1/day), KLP is the minimum hydrolysis rate of LPOP (1/day), KDP is the minimum mineralization rate of DOP (1/day), KRPalg and KLPalg are the constants that relate hydrolysis of RPOP and LPOP, respectively, to algal

biomass (1/day per g C/m3), KDPalg is the constant that relates mineralization to algal biomass (1/day per g C/m3), and KHP is the mean half-saturation constant for algal phosphorus uptake (g P/m3).

∑algaeKHPx number algae

KHP =

(8.69)

When PO−3

4 is abundant relative to KHP, the rates are close to the minimum values with little influence from algal biomass. When PO−3

4 becomes scarce relative to KHP, the rates increase with the magnitude of increase depending on algal biomass. Equations 8.66 to 8.68 have exponential functions that relate rates to temperature.

##### 8.1.3.6 Nitrogen (N)

EFDC+ has five state variables for N; three organic forms (RPON, LPON, and DON) and two inorganic forms (NH4+ and NO−

3 and NO−

3 state variable in the model represents the sum of NO−

3 ). The NO−

2 .

- 8.1.3.6.1 Particulate Organic Nitrogen (PON) For RPON and LPON, sources and sinks included in the model are (Figure 8.2);


- 1. Algal basal metabolism, death and predation,
- 2. Zooplankton death and predation,
- 3. Dissolution to DON,
- 4. Settling, and
- 5. External loads.


###### 167



<<<PAGE 181>>>

###### 8. EUTROPHICATION EFDC+ Theory



The kinetic equations for RPON and LPON are:

∂RPON ∂t

### = ∑

(FNRx·BMx+FNRPx·Dx)·ANCx·Bx+ ∑

FNRDZz ·Dz ·Zz ·ANCz

algae

zoopl

URz ·RPON

### + ∑

(FNRPZz ·PRz −

PAz ·Rz)·Zz ·ANCz −KRPONRPON +

zoopl

∂ ∂Z

WRPON V

(WSRP ·RPON)+

where,

∂LPON ∂t

### = ∑

(FNLx·BMx+FNLPx·Dx)·ANCx·Bx+ ∑

FNLDZz ·Dz ·Zz ·ANCz

algae

zoopl

ULz ·LPON

### + ∑

PAz ·Rz)·Zz ·ANCz −KLPONLPON +

(FNLPZz ·PRz −

zoopl

∂ ∂Z

WLPON V

(WSLP ·LPON)+

RPON is the concentration of RPON (g N/m3), LPON is the concentration of LPON (g N/m3),

FNRx is the fraction of metabolized N by algal group x as RPON, FNLx is the fraction of metabolized N by algal group x as LPON, FNRPx is the fraction of death (or predated) N produced as RPON by algal group x, FNLPx is the fraction of death (or predated) N produced as LPON by algal group x, FNRDZx is the fraction of death N produced as RPON by zooplankton group z, FNLDZx is the fraction of death N produced as LPON by zooplankton group z, FNRPZx is the fraction of predated N produced as RPON by zooplankton group z, FNLPZx is the fraction of predated N produced as LPON by zooplankton group z, ANCx is the N-to-C ratio in algal group x (g; N; per g C), ANCz is the N-to-C ratio in zooplankton group z (g; N; per g C), KRPON is the hydrolysis rate of RPON (1/day), KLPON is the hydrolysis rate of LPON (1/day), WRPON is the external loads of RPON (g N/day), and WLPON is the external loads of LPON (g N/day).

- 8.1.3.6.2 Dissolved Organic Nitrogen (DON) Sources and sinks for DON included in the model are (Figure 8.2);


(8.70)

(8.71)

- 1. Algal basal metabolism, death and predation,
- 2. Zooplankton basal metabolism, death and predation,


###### 168



<<<PAGE 182>>>

###### 8. EUTROPHICATION EFDC+ Theory



- 3. Dissolution from RPON and LPON,
- 4. Mineralization to NH4+, and
- 5. External loads.


The kinetic equation describing these processes is:

∂DON ∂t

### = ∑

(FNDx BMx+FNDPx Dx)ANCx Bx+ ∑

FNDBZz ·BMz ·Zz ·ANCz

algae

zoopl

### + ∑

(FNDDZ ·Dz +FNDPZ ·PRz)·Zz ·ANCz

zoopl

WDON V

+KRPON ·RPON +KLPON ·LPON −KDON ·DON +

where, DON is the concentration of DON (g N/m3), FNDx is the fraction of metabolized N by algal group x produced as DON, FNDPx is the fraction of death (or predated) N produced as DON by algal group x, FNDBZz is the fraction of metabolized N produced as DON by zooplankton group z, FNDDZz is the fraction of death N produced as DON by zooplankton group z, FNDPZz is the fraction of predated N produced as DON by zooplankton group z, KDON is the mineralization rate of DON (1/day), WDON is the external loads of DON (g N/day).

(8.72)

- 8.1.3.6.3 Ammonium (NH4+) Sources and sinks for NH4+ included in the model are (Figure 8.2):


- 1. Algal basal metabolism, death, predation, and uptake,
- 2. Zooplankton basal metabolism, death and predation,
- 3. Mineralization from DON,
- 4. Nitrification to NO−

3 ,

- 5. Sediment-water exchange for the bottom layer only, and
- 6. External loads.


The kinetic equation describing these processes is:

∂NH4 ∂t

### = ∑

(FNIx BMx +FNIPx Dx −PNxPx)ANCx ·Bx +KDON ·DON

algae

### + ∑

(FNIBZz ·BMz +FNIDZz ·Dz +FNIPZz ·PRz)Zz ·ANCz

zoopl

BFNH4 ∆Z

WNH4 V

−KNit NH4+

+

where,

(8.73)

###### 169



<<<PAGE 183>>>

###### 8. EUTROPHICATION EFDC+ Theory



FNIx is the fraction of metabolized N by algal group x produced as inorganic N, FNIPx is the fraction of predated N produced as inorganic N, PNx is the preference for NH4+ uptake by algal group x (0 ≤ PNx ≤ 1), FNIBZz is the fraction of metabolized N produced as NH4+ by zooplankton group z, FNIDZz is the fraction of death N produced as NH4+ by zooplankton group z, FNIPZz is the fraction of predated N produced as NH4+ by zooplankton group z, Knit is the nitrification rate (1/day) given in equation 8.80, BFNH4 is the sediment-water exchange flux of NH4+ (g N/m2/day), applied to the bottom layer only WNH4 is the external loads of NH4+ (g N/day)

##### 8.1.3.6.4 Nitrate (NO−

3 )

Sources and sinks for NO−

3 included in the model are:

- 1. Algal uptake,
- 2. Nitrification from NH4+,
- 3. Denitrification to N gas,
- 4. Sediment-water exchange for the bottom layer only, and
- 5. External loads.


The kinetic equation describing these processes is:

∂NO3 ∂t

=− ∑

(1−PNX)PX ANCX BX +KNit NH4−

algae

BFNO3 ∆Z

WNO3 V

ANDC Denit DOC+

+

where,

(8.74)

ANDC is the mass of NO−

3 reduced per mass of DOC oxidized (0.933 g N per g C), BFNO3 is the sediment-water exchange flux of NO−

3 (g N/m2/day), applied to the bottom layer only, and

WNO3 is the external loads of NO−

3 (g N/day).

The remainder of this section explains each term in equations 8.70-8.74. It is noted that the form of the nitrification sink in 8.73 and the subsequent source in the NO−

3 equation 8.74 differ from that in ICM.

###### 170



<<<PAGE 184>>>

###### 8. EUTROPHICATION EFDC+ Theory



##### 8.1.3.6.5 Effect of Algae on Nitrogen

The terms within summation in equations 8.70 to 8.74 account for the effects of algae on N. As in P, both basal metabolism (respiration and excretion) and predation are considered, and thus formulated to contribute to ON and NH4+. That is, algal N released by both basal metabolism and predation are represented by distribution coefficients (FNRx, FNLx, FNDx, FNIx, FNRPx, FNLPx, FNDPx,and FNIPx). The sum of the four distribution coefficients for basal metabolism should be unity; the sum of the predation distribution coefficients should also be unity.

Algae takes up NH4+ and NO−

3 for growth, and NH4+ is preferred from thermodynamic considerations. The preference of algae for NH4+ is expressed as:

NO3 (KHNx +NH4)(KHNx +NO3)

PNx = NH4

KHNx (NH4+NO3)(KHNx +NO3)

+ NH4

(8.75)

This equation forces the preference for NH4+ to be unity when NO−

3 is absent, and to be zero when NH4+ is absent.

##### 8.1.3.6.6 Mineralization and Hydrolysis

The terms KRPON and KLPON on the RHS of equations 8.70 and 8.71 represent hydrolysis of the two states of Particulate Organic Nitrogen (PON) and the term of KDON in equation 8.72 represents mineralization of DON. The hydrolysis and mineralization rates can be specified by the following formulations:

KRPON = KRN +

KHN KHN +NH4+NO3

KRNalg ∑

Bx exp(KTHDR(T −TRHDR)) (8.76)

algae

KLPON = KLN +

KHN KHN +NH4+NO3

KLNalg ∑

Bx exp(KTHDR(T −TRHDR)) (8.77)

algae

KDON = KDN +

where,

KHN KHN +NH4+NO3

KDNalg ∑

Bx exp(KTMIN (T −TRMIN)) (8.78)

algae

KRN is the minimum hydrolysis rate of RPON (1/day), KLN is the minimum hydrolysis rate of LPON (1/day), KDN is the minimum mineralization rate of DON (1/day), KRNalg and KLNalg are the constants that relate hydrolysis of RPON and LPON, respectively, to algal

biomass (1/day per g C/m3), KDNalg is the constant that relates mineralization to algal biomass (1/day per g C/m3), and KHN is the mean half-saturation constant for algal N uptake (g N/m3).

###### 171



<<<PAGE 185>>>

###### 8. EUTROPHICATION EFDC+ Theory



∑algaeKHNx number of algae

KHN =

Equations 8.76 to 8.78 include exponential functions that relate rates to temperature.

(8.79)

##### 8.1.3.6.7 Nitrification

Nitrification is a process mediated by autotrophic nitrifying bacteria that obtain energy through the oxidation of NH4+ to NO−

2 and of NO−

2 to NO−

3 . According to Bowie et al. (1985), the stoichiometry of complete reaction is:

NH4+ +2O2 → NO−

3 +H2O+2H+ (8.80) The term of KNit in equations 8.73 and 8.74 represents the effect of nitrification on NH4+ and NO−

3 . The

kinetics of the complete nitrification process are formulated as a function of available NH4+, DO and temperature:

NH4 KHNitN +NH4

DO KHNitDO +DO

Nitm (8.81) and

KNit ·NH4 = fNit (T)

where,

 

fNit (T) =



- exp −KNit1(T −TNit)2) , T ≤ TNit
- exp −KNit2(TNit −T)2 , T > TNit


(8.82)

KHNitDO is the nitrification half-saturation constant for DO (g O2/m3), KHNitN is the nitrification half-saturation constant for NH4+ (g N/m3), Nitm is the maximum nitrification rate at TNit (g N/m3/day), TNit is the optimum temperature for nitrification (◦C),

- KNit1 is the effect of temperature below TNit on nitrification rate (1/◦C2), and
- KNit2 is the effect of temperature above TNit on nitrification rate (1/◦C2).


This follows the ICM model formulation for nitrification. The Monod function of DO in equation 8.79 indicates the inhibition of nitrification at low O level. The Monod function of NH4+ indicates that when NH4+ is abundant, the nitrification rate is limited by the availability of nitrifying bacteria.

In EFDC+, a reference value of KNit is input into the model instead of Nitm by writing equation 8.81 as:

KHNitN KHNitN +NH4

DO KHNitDO +DO

KNitm (8.83) where,

KNit = fNit (T)

###### 172



<<<PAGE 186>>>

###### 8. EUTROPHICATION EFDC+ Theory



Nitm KHNitN

KNitm =

(8.84)

KNitm is interpreted as the linear kinetic rate corresponding to KHNitN equal to unity, since NH4 in this case must less than unity, and DO effects eliminated by setting KHNitDO to zero. In certain applications, particularly those having long-term Biological Oxygen Demand (BOD) and nitrogen series test results, KNitm can be observed.

##### 8.1.3.6.8 Denitrification

The effect of denitrification on DOC was described in Section 8.1.3.4.5. Denitrification removes NO−

3 from the system in stoichiometric proportion to C removal as determined by equation 8.56. The sink term in 8.74 represents this removal of NO−

3 .

##### 8.1.3.7 Silica

EFDC+ models two different forms of silica; SiP and SiA. Although the description below uses diatoms as the biota that uses SiO2, EFDC+ allows modeler to include any number of biota groups and select the species that need SiO2 for growth.

- 8.1.3.7.1 Particulate Biogenic Silica (SiP) Sources and sinks for SiP included in the model are (Figure 8.2);


- 1. diatom basal metabolism, death and predation,
- 2. zooplankton death, and predation,
- 3. dissolution to available silica,
- 4. settling, and
- 5. external loads.


The kinetic equation describing these processes is:

∂SiP ∂t

UBd Bd PAz

=(FSPd·BMd+FSPPd·Dd)ASCd Bd+ ∑

FSPDZz ·Dz ·Z ·ASCz

zoopl

∂ ∂Z

UBd Bd PAz −KSUA ·SiP+

WSiP V

### + ∑

FSPPZz ·PRz ·Zz ·ASCz

(WSd ·SiP)+

zoopl

where,

(8.85)

SiP is the concentration of particulate biogenic silica (g Si/m3), FSPd is the fraction of metabolized SiO2 by diatoms produced as SiP, FSPPd is the fraction of death (or predated) diatom SiO2 produced as SiP, FSPDZz is the fraction of predated SiO2 produced as SiP by zooplankton group z,

###### 173



<<<PAGE 187>>>

###### 8. EUTROPHICATION EFDC+ Theory



FSPPZz is the fraction of death SiO2 produced as SiP by zooplankton group z, ASCd is the SiO2-to-C ratio of diatoms (g Si per g C), KSUA is the dissolution rate of SiP (1/day), and WSiP is the external loads of SiP (g Si/day).

- 8.1.3.7.2 Available Silica (SiA) Sources and sinks for SiA included in the model are;


- 1. diatom basal metabolism, death, predation, and uptake,
- 2. zooplankton basal metabolism, death and predation,
- 3. settling of sorbed (particulate) available SiO2,
- 4. dissolution from SiP,
- 5. sediment-water exchange of dissolved SiO2 for the bottom layer only, and
- 6. external loads.


The kinetic equation describing these processes is:

∂SiA ∂t

= (FSId BMd +FSIPd Dd −Pd)ASCd Bd +KSUA ·SiP

UBd Bd PAz

### + ∑

(BMz +FSADZz ·Dz +FSAPZz ·PRz)Zz ·ASCz ·

zoopl

∂ ∂Z

BFSiAd ∆Z

WSiA V

(WSTSSSiAp)+

+

+

where,

(8.86)

SiAd is the dissolved SiA (g Si/m3), SiAp is the particulate (sorbed) SiA (g Si/m3), SiA = SiAd +SiAp is the concentration of SiA (g Si/m3), FSId is the fraction of metabolized SiO2 by diatoms produced as SiA, FSIPd is the fraction of death (or predated) diatom SiO2 produced as SiA, FSADZz is the fraction of death SiO2 produced as SiA by zooplankton group z, FSAPZz is the fraction of predated SiO2 produced as SiA by zooplankton group z, BFSAd is the sediment-water exchange flux of SiA (g Si/m2/day), applied to bottom layer only, and WSiA is the external loads of SiA (g Si/day).

In equation 8.86, if TAM is chosen as a measure of sorption site, the settling velocity of total suspended solid WSTSS, is replaced by that of particulate metal WSs.

###### 174



<<<PAGE 188>>>

###### 8. EUTROPHICATION EFDC+ Theory



##### 8.1.3.7.3 Available Silica System

Analysis of Chesapeake Bay monitoring data indicates that silica shows similar behavior as PO−3

4 in the adsorption-desorption process (Cerco and Cole, 1993). As in PO−3

4 , therefore, SiA is defined to include both dissolved and sorbed fractions. Treatment of SiA is the same as PO4t, and the same method to partition PO4d and PO−3

4 is used to partition dissolved and sorbed SiA.

KSiAp SORPS 1+KSiAp SORPS

SiAp =

SiA (8.87)

1 1+KSiAp SORPS

SiA (8.88) SORPS = SED or TAMp (8.89)

SiAd =

SiA = SiAp+SiAd (8.90)

where, KSiAp is the empirical coefficient relating SiA sorption to SED (per g/m3) or particulate TAM (per mol/m3) concentration.

##### 8.1.3.7.4 Effect of Diatoms on Silica

In equations 8.85 and 8.87, those terms expressed as a function of diatom biomass (Bd) account for the effects of diatoms on silica. As in P and N, both basal metabolism (respiration and excretion) and predation are considered, and thus formulated, to contribute to SiP and SiA. That is, diatom silica released by both basal metabolism and predation are represented by distribution coefficients (FSPd, FSId, FSPP, and FSIP). The sum of two distribution coefficients for basal metabolism should be unity and so is that for predation. Diatoms require silica as well as P and N, and diatom uptake of SiA is represented by (−Pd ASCd Bd) in equation 8.86.

##### 8.1.3.7.5 Dissolution

The term (−KSUASiP) in equation 8.85 and its corresponding term in equation 8.86 represent dissolution of SiP to SiA. The dissolution rate is expressed as an exponential function of temperature

KSUA = KPSiexp(KTSUA(T −TRSUA)) (8.91) where,

KSiP is the dissolution rate of SiP at TRSUA (1/day), KTSUA is the effect of temperature on dissolution of SiP (1/◦C), and TRSUA is the reference temperature for dissolution of SiP (◦C).

##### 8.1.3.8 Chemical Oxygen Demand (COD)

In EFDC+, COD is the concentration of reduced substances that are oxidizable through inorganic means. The source of COD in saline water is S−

2 released from sediments. A cycle occurs in which SO−2

4 is reduced

###### 175



<<<PAGE 189>>>

###### 8. EUTROPHICATION EFDC+ Theory



2 in the sediments and reoxidized to SO−2

to S−

4 in the water column. In fresh water, Methane (CH4) is released to the water column by the sediment process model. Both S−

2 and CH4 are quantified in units of O demand and are treated with the same kinetic formulation. The kinetic equation, including external loads, if any, is:

∂COD ∂t

DO KHCOD +DO

WCOD V

BFCOD ∆Z

(8.92) where,

KCODCOD+

= −

+

COD is the concentration of COD (g O2 −equivalents/m2/day), KHCOD is the half-saturation constant of DO required for oxidation of COD (g O2/m3), KCOD is the oxidation rate of COD (1/day), BFCO is the sediment flux of COD (g O2 −equivalents/m2/day), applied to bottom layer only, and WCOD is the external loads of COD (g O2 −equivalents/day).

An exponential function is used to describe the temperature effect on the oxidation rate of COD;

KCOD = KCDexp(KTCOD(T −TRCOD)) (8.93) where,

KCD is the oxidation rate of COD at TRCOD (1/day), KTCOD is the effect of temperature on oxidation of COD (1/◦C), and TRCOD is the reference temperature for oxidation of COD (◦C).

- 8.1.3.9 Dissolved Oxygen (DO) Sources and sinks of DO in the water column included in the model are (Figure 8.2);


- 1. algal photosynthesis and respiration,
- 2. zooplankton basal metabolism,
- 3. nitrification,
- 4. heterotrophic respiration of DOC,
- 5. oxidation of COD,
- 6. surface reaeration for the surface layer only,
- 7. SOD for the bottom layer only, and
- 8. external loads.


###### 176



<<<PAGE 190>>>

###### 8. EUTROPHICATION EFDC+ Theory



The kinetic equation describing these processes is:

∂DO ∂t

DO

### = ∑

(1+0.3(1−PNx))Px −(1−FCDx)

KHRx +DO ·BMx AOCR Bx −AONT Nit NH4−AOCR KHRDOC−

algae

DO KHCOD +DO ·KCODCOD

SOD ∆Z

WDO V

− ∑

BMz ·Zz ·AOCR+KR(DOS −DO)+

+

zoopl

where,

(8.94)

AONT is the mass of DO consumed per unit mass of NH4+ as N nitrified (4.33 g O2 per g N), AOCR is the DO-to-C ratio in respiration (2.67 g O2 per g C), KR is the reaeration coefficient (1/day): the reaeration term is applied to the surface layer only, DOs is the saturated concentration of DO (g O2/m3), SOD is the SOD (g O2/m2/day), applied to the bottom layer only; positive is to the water column, WDO is the external loads of DO (g O2/day), and PNx is the preference for NH4+ uptake by algae group x (0 < PNx < 1).

The remainder of this section explains the effects of algae, nitrification, and surface reaeration.

##### 8.1.3.9.1 Dissolved Oxygen Saturation

The saturated concentration of DO can be determined based on temperature, salinity and elevation using an empirical formula in the form:

DOs = f (T)· f (S)· f (z) (8.95)

Where f (T) and f (S) indicate the dependencies of the saturated DO on temperature and salinity, which decreases as temperature and salinity increase, and f (z) is the influence of oxygen partial pressure on the saturated DO.

At sea-level, the saturated DO can be computed using several empirical formulae such as Genet et al. (1974), Garcia and Gordon (1992) and Chapra (1997).

The dependency of saturated DO on temperature according to Genet et al. (1974) is:

f (T) = 5.4258×10−3T2 −0.38217×T +14.5532 (8.96) Garcia and Gordon (1992) proposed formulae based on a fit to precise data selected from the literature as:

ln f (T) = 1.41575Ts5 +1.01567Ts4 +4.93845Ts3 +4.11890Ts2 +3.20684Ts +5.80818 (8.97)

ln f (S) = −10−3S× 1.32412×10−4S2+

5.54491Ts3 +7.93334Ts2 +7.25958Ts +7.01211 (8.98)

###### 177



<<<PAGE 191>>>

###### 8. EUTROPHICATION EFDC+ Theory



where Ts is the scaled temperature

Ts = log

298.15−T 273.15+T

(8.99)

The saturated concentration of DO is from µmol/L to mg/L using a factor of 32.0×10−3. The fractional reductions of DO saturation due to temperature and salinity at sea-level according to Chapra

(1997) are:

8.621949×1011 Ta4

ln f (T) = −

1.2438×1010 Ta3 −

6.642308×107 Ta2

+

+ 1.575701×105

Ta −139.34411 (8.100)

2140.7 Ta2

ln f (S) = −S× −

+

10.754 Ta

+1.7674×10−2 (8.101)

where Ta is the absolute temperature (◦K), Ta = T +273.15. The effect of atmospheric pressure on DO saturation at an elevation is based on the standard atmosphere as described by the cubic polynomial according to Chapra et al. (2021):

f (z) = 1−0.11988·z+6.10834×10−3 ·z2 −1.60747×10−4 ·z3 (8.102) Zison (1978) used a linear elevation adjustment factor of

f (z) = 1−0.1148·z (8.103) In these formulae, z is the elevation in km.

##### 8.1.3.9.2 Effect of Algae on Dissolved Oxygen (DO)

The first line on the RHS of equation 8.94 accounts for the effects of algae on DO. Algae produces O through photosynthesis and consumes O through respiration. The quantity produced depends on the form of N utilized for growth. Equations describing production of DO are (Morel, 1983);

106CO2 +16NH4+ +H2PO−

4 +106H2O → protoplasm+106O2 +15H+ (8.104)

106CO2 +16NO−

3 +H2PO−

4 +122H2O → protoplasm+138O2 (8.105) When NH4+ is the N source, one mole of O is produced per mole of CO2 fixed. When NO−

3 is the N source, 1.3 moles of O are produced per mole ofCO2 fixed. The quantity (1.3−0.3PNx), in the first term of equation 8.94 is the photosynthesis ratio and represents the molar quantity of O produced per mole of CO2 fixed. It approaches unity as the algal preference for NH4+ approaches unity.

###### 178



<<<PAGE 192>>>

###### 8. EUTROPHICATION EFDC+ Theory



The last term in the first line of equation 8.94 accounts for the O consumption due to algal respiration. A simple representation of respiration process is:

CH2O+O2 → CO2 +H2O (8.106) from which, AOCR = 2.67 g O2 per g C.

##### 8.1.3.9.3 Effect of Nitrification on Dissolved Oxygen (DO)

The stoichiometry of nitrification reaction equation 8.80, indicates that two moles of O are required to nitrify one mole of NH4+ into NO−

3 . However, cell synthesis by nitrifying bacteria is accomplished by the fixation of CO2 so that less than two moles of oxygen are consumed per mole NH4+ utilized (Wezenak and Gannon, 1968), i.e. AONT = 4.33 g O2 per g N.

##### 8.1.3.9.4 Effect of Surface Reaeration on Dissolved Oxygen (DO)

The reaeration rate of DO at the air-water interface is proportional to the O gradient across the interface (DOs−DO), assuming that the air is saturated with O. The term Kr on the RHS of equation 8.94 is reaeration rate which represents the reaeration process mathematically. The reaeration rate in natural waters depends on (1) water flow speed and wind speed, (2) water temperature and salinity, and (3) water depth. When wind effects are excluded, the empirical formula for the reaeration rate coefficient are based on velocity and depth:

VB HC

Kr(20◦C) = A.

(8.107) where,

Kr(20◦C) is the reaeration rate at 20 ◦C (1/day) V is water velocity (m/s) H is water depth or thickness of the top layer (m) A,B,C are empirical parameters

The effects of water temperature on the reaeration rate are expressed as:

Kr = Kr(20◦C)1.024T−20 (8.108) Where,

Kr is reaeration rate at T ◦C T is water temperature (◦C)

The reaeration coefficient includes the effect of turbulence generated by bottom friction (O’Connor and Dobbins, 1958) and that by surface wind stress (Banks and Herrera, 1977):

ueq heq

1 ∆z

+Wrea (KTr)T−20 (8.109)

Kro

Kr =

where,

###### 179



<<<PAGE 193>>>

###### 8. EUTROPHICATION EFDC+ Theory



Kro = 3.933 is the proportionality constant in SI units, ueq = ∑(ukVk)/3(Vk) is the weighted velocity over cross-section (m/s), heq = ∑(Vk)/B is the weighted depth over cross-section (m), B is the width at the free surface (m), and KTr is the constant for temperature adjustment of DO reaeration rate.

and the wind-induced reaeration Wrea (m/day) is expressed as:

Wrea = 0.728√Uw −0.317Uw +0.0372Uw2 (8.110) in which Uw is the wind speed (m/s) at the height of 10 m above surface.

The EFDC+ code provides several options for the calculation of the reaeration coefficient rate. These options varies from a constant value to complex formulas which include the effects of temperature, water and wind speed, water depth in the reaeration process.

- 8.1.3.9.5 Simplified Equation for Dissolved Oxygen The simplified DO equation for KHRx and FCDx equal to zero is:


∂DO ∂t

### = ∑

((1.3−0.3PNx)Px −BMx)AOCR Bx −AONT Nit NH4

algae

DO KHCOD +DO

−AOCR KHR DOC− ∑

BMz ·Zz ·AOCR−

KCODCOD+

zoopl

SOD ∆Z

WDO V

(8.111) which is consistent with equation 8.94.

KR(DOS −DO)+

+

##### 8.1.3.10 Total Active Metals (TAM)

EFDC+ requires simulation of TAM for adsorption of PO−3

4 , and SiO2 if that option is chosen. The TAM state variable is the sum of Fe and Mn concentrations, both particulate and dissolved. The origin of TAM is benthic sediments in EFDC+. Since sediment release of metal is not explicit in the sediment model (see Chapter 6), release is specified in the kinetic portion of the water column model. The only other term included is settling of the particulate fraction. Then the kinetic equation for TAM, including external loads, if any, may be written as:

∂TAM ∂t

=

KHbmf KHbmf +DO

BFTAM ∆z

(exp(Ktam(T −Ttam)) )

+

∂ ∂Z

WTAM V

(WSsTAMp)+

(8.112)

where,

###### 180



<<<PAGE 194>>>

###### 8. EUTROPHICATION EFDC+ Theory



TAM = TAMd +TAMp is the TAM concentration (mol/m3), TAMd is the dissolved TAM (mol/m3), TAMp is the particulate TAM (mol/m3), KHbmf is the DO concentration at which TAM release is half the anoxic release rate (g O2/m3), BFTAM is the anoxic release rate of TAM (mol/m2/day), applied to the bottom layer only, Ktam is the effect of temperature on sediment release of TAM (1/◦C), Ttam is the reference temperature for sediment release of TAM (◦C), WSs is the settling velocity of particulate metal (m/day), and WTAM is the external loads of TAM (mol/day).

In estuaries, Fe and Mn exist in particulate and dissolved forms depending on DO concentration. In oxygenated water, most of the Fe and Mn exist as particulate while under anoxic conditions, large fractions are dissolved. The partitioning between particulate and dissolved phases is expressed using a concept that TAM concentration must achieve a minimum level, which is a function of DO, before precipitation occurs:

TAMd = min(TAMdmxexp(−Kdotam DO) , TAM) (8.113)

TAMp = TAM −TAMd (8.114) where,

TAMdmx is the solubility of TAM under anoxic conditions (mol/m3), and Kdotam is the constant that relates TAM solubility to DO (per g O2/m3).

##### 8.1.3.11 Fecal Coliform Bacteria

Fecal coliform bacteria are indicative of organisms from the intestinal tract of humans and other animals and can be used as an indicator bacteria as a measure of public health (Thomann and Mueller, 1987). EFDC+ includes fecal coliform variable in the eutrophication module for convenience in developing Total Maximum Daily Load (TMDL) applications and is completely decoupled from the rest of the water quality model. In EFDC+, fecal coliform bacteria have no interaction with other state variables, and have only one sink term, die-off. The kinetic equation, including external loads, may be written as:

∂FCB ∂t

WFCB V

= KFCB TFCBT−20 FCB+

(8.115) where,

FCB is the bacteria concentration (MPN per 100ml), KFCB is the first order die-off rate at 20 ◦C (1/day), TFCB is the effect of temperature on decay of bacteria (1/◦C), and WFCB is the external loads of fecal coliform bacteria (MPN per 100ml m3/day).

###### 181



<<<PAGE 195>>>

###### 8. EUTROPHICATION EFDC+ Theory



##### 8.1.4 Settling, Deposition and Resuspension of Particulate Matter

The kinetic equations for particulate matter, including particulate organic matter, PO−3

4 , the two SiO2 state variables, and TAM contain settling term. A representative generic equation is

∂PM ∂t

∂ ∂z

(WSPMPM)+PMSS (8.116)

=

where, PMSS represents the additional terms in the equation. Integration of equation 8.116 over the bottom layer gives

∂PM1 ∂t

WSPM ∆Z1

WSPM ∆Z1

PM2 −

PM1 +PMSS1 (8.117)

=

The original ICM and EFDC water quality models were formulated with settling velocities representing long-term average net settling. In the subsequent application of ICM to Florida Bay (Cerco et al., 2000), the resuspension or erosion of particulate material from the sediment bed was added and has also been added to the EFDC+ water quality model.

EFDC+ allows the use of the net settling formulation 8.117 and a formulation allowing resuspension with equation 8.117 modified

∂PM1 ∂t

PdepPMWSPM ∆Z1

WSPOM ∆Z1

EPM ∆Z1

PM2 −

PM1 +

+PMSS1 (8.118)

=

to include a probability of deposition factor and an erosion term EPM with units of mass per unit time-unit area. For EFDC+ applications with the erosion of particulate material in the water quality module, sediment transport must be active in the hydrodynamic model. The erosion term is then defined by

PMbed SEDbed

EPM =

max(JERO, 0) (8.119) where,

PMbed is the particulate material concentration in bed (g PM/m2 or g PM/m3), SEDbed is the concentration of finest sediment class in bed (g PM/m2 or g PM/m3), PdepPM is the probability of deposition of the specific particulate matter variable (0 ≤ PdepPM ≤ 1), and JERO is the mass rate of erosion or resuspension of the finest sediment class (g SED/day/m2).

Usage of the ratio of the water quality model particulate state variable concentration to the finest sediment size class concentration rather than the total solids concentration is based on the reality that the finest sediment class (generally less than 63µm) includes both inorganic and organic material and field observations of settling, deposition and resuspension, when available for model calibration, account for this. If simultaneous deposition and erosion are not permitted, the probability of deposition is defined as zero when the sediment erosion flux is greater than zero.

In conclusion, it is noted that in the ICM documentation which includes particulate matter resuspension (Cerco et al., 2000), resuspension is explicitly included in various state variable equations, while in this document it is included implicitly as described in the current section.

###### 182



<<<PAGE 196>>>

###### 8. EUTROPHICATION EFDC+ Theory



##### 8.1.5 Method of Solution for Kinetics Equations

The kinetic equations for the state variables, excluding fecal coliform, in the EFDC+ water column water quality model can be expressed in a system of n × n (where n = total number of state variables) partial differential equations in each model cell, after linearizing some terms, mostly Monod type expressions:

∂C ∂t

∂ ∂z

(WC)+R (8.120) where,

= KC +

C is the vector of concentration of water quality state variables in [ML−3], K is a matrix kinetic rate in [T−1], W is a vector of settling velocity in [LT−1], and R is a vector of source/sink term in [ML−3T−1].

The ordering of variables follows that in Table 8.1 which results in K being lower triangular. Integrating 8.120 over layer k, gives

Ck ∂t

= K1kCk +δkK2kCk+1 +Rk

1 ∆k

K1k = Kk −

(8.121)

W

1 ∆k

K2k =

W

which indicates that the settling of particulate matter from the overlying cell acts as an input for a given cell. For the layer of cells adjacent to the bed, the erosion term in 8.118 is included in the vector R. The matrices and vectors in 8.120 and 8.121 are defined in Appendix A of Park et al. (1995). The layer index k increases upward with KC vertical layers; k = 1 is the bottom layer and k = KC is the surface layer. Then δk = 0 for k = KC; otherwise, δk = 1. The matrix K2 is a diagonal matrix, and the non-zero elements account for the settling of particulate matter from the overlying cell.

Equation 8.121 is solved using a generalized trapezoidal scheme over a time step of θ, which may be expressed as:

Ckn+1 −Ckn = λθ K1nkCkn+1 +δkK2nkCkn++11 +Rkn+1

+(1−λ)θ K1nkCkn +δkK2nkCkn+1 +Rkn (8.122) or

(I −λθK1nk)Ckn+1 = (I +(1−λ)θK1nk)Ckn+

θδkK2nk λCkn++11 +(1−λ)Ckn+1 +θ λRkn+1 +(1−λ)Rkn (8.123) where,

###### 183



<<<PAGE 197>>>

###### 8. EUTROPHICATION EFDC+ Theory



λ is an implicitness factor (0 ≤ λ ≤ 1), θ = 2·m·∆t is the time step for the kinetic equations and

I is the identity matrix; the superscripts n and n+1 designate the variables before and after being adjusted for the relevant kinetic processes. Since equation 8.121 is solved from the surface layer downward, the term with Ckn++11 is known for the kth layer and thus placed on the RHS. In equation 8.122, inversion of a matrix can be avoided when the 20 state variables are solved in the order given in Table 8.1.

##### 8.2. Rooted Aquatic Plants Formulation

Rooted macrophyte beds are commonly observed along the banks of many rivers. The accuracy of a water quality model may be improved by simulating submerged aquatic vegetation (epiphytic algae and rooted macrophytes) if a waterbody has documented rooted macrophyte occurrences. EFDC+’s generic Rooted Aquatic Plant and Epiphyte Algae Sub-Model (RPEM) uses kinetic mass balance equations for rooted plant shoots, roots and epiphyte algae growing on the shoots. The user may enable or disable a variety of combinations for RPEM, including enabling simulation of rooted plants or epiphytes; enabling epiphytes growing on rooted plants; enabling the RPEM – Water Column Nutrient Interaction; and enabling RPEM – Sediment Diagenesis Interaction.

The focus of this section will be on the RPEM variables and their processes. The state variables in the submodel are rooted plant shoots, roots, epiphyte algae biomass and rooted plant shoot detritus biomass. The kinetic mass balance of these variables depends mainly on production, respiration and non-respiration loss rates. These rates in turn are mainly controlled by nutrients, C, O, light field, and temperature. Parameters for RPEM sub-model are highlighted by comparing with the Florida Bay seagrass model in which Thalassia and Halodule are selected as dominant species (Madden et al., 2018).

##### 8.2.1 State Variable Equations

The kinetic mass balance equations for rooted plant shoots, roots and epiphyte algae growing on the shoots are

∂ (RPS) ∂t

= ((1−FPRPR)·PRPS −RRPS −LRPS)RPS+JRPRS (8.124)

∂ (RPR) ∂t

= FPRPR ·PRPS ·RPS−(RRPR +LRPR)RPR+JRPRS (8.125)

∂ (RPE) ∂t

= (PRPE −RRPE −LRPE)RPE (8.126) where,

t is the time (day), RPS (Ta, Ha) is the Rooted Plant Shoot Biomass (g C/m2), FPRPR (χTa, χHa) is the fraction of production directly transferred to roots (0 < FPGR < 1),

###### 184



<<<PAGE 198>>>

###### 8. EUTROPHICATION EFDC+ Theory



PRPS (gTa, gHa) is the production rate for plant shoots (1/day), RRPS (rTa, rHa) is the respiration rate for plant shoots (1/day), LRPS (mTa, mHa) is the non-respiration loss rate for plant shoots (1/day), JRPRS (χTbTb, χHbHb) is the C transport positive from roots to shoots (g C/m2/day) , RPR (Tb, Hb) is the Rooted Plant Root Biomass (g C/m2), RRPR (rTb, rHb) is the respiration rate for plant roots (1/day), LRPR (mTb, mHb) is the non-respiration loss rate for plant roots (1/day) , RPE (E) is the Rooted Plant Epiphyte Biomass (g C/m2), PRPE (gE) is the production rate for epiphytes (1/day), RPRE(rEE) is the respiration rate for epiphytes (1/day), and LRPE (rTa +mE) is the non-respiration loss rate for epiphytes (1/day).

Equivalent notation used in the Florida Bay seagrass model appears in parentheses (), in which T is associated with Thalassia and H is associated with Halodule. For comparison, Table 8.3 and Table 8.4 show generic and Florida Bay seagrass model parameters.

Table 8.3. Generic and Florida Bay Seagrass Model Parameters for Thalassia and Halodule species

Parameter Dimension Generic Thalassia Halodule FPRPR (χTa, χHa)

none constant 0.4 0.34

Function of N, P, Light, Temp, Salt

Function of N, P, Light, Temp, Salt

PRPS (gTa, gHa)

1/day Function of N, P, Light, Temp, Salt

RRPS

- (rTa, rHa)

1/day Function of Temp

0.01 (base) Temperature Function

0.029 (base) Temperature Function

LRPS

- (mTa, mHa)

1/day Function of Temp

0.001 (base) Temperature Function

0.004 (base) Temperature Function

RRPR (rTb, rHb)

1/day Function of Temp

0.0025 (base) Temperature Function

0.011(base) Temperature Function

LRPR

- (mTb, mHb)




1/day Function of Temp

0.0001 (base) Temperature Function

0.0004 (base) Temperature Function

g C/m2/day KRPRS ·RPR χTbTb (χTb = 0.0005)

χHbHb (χHb = 1×10−5)

JRPRS (χTbTb, χHbHb)

###### 185



<<<PAGE 199>>>

###### 8. EUTROPHICATION EFDC+ Theory



Table 8.4. Generic and Florida Bay Seagrass Model Parameters for Epiphytes

Parameter Dimension Generic Epiphytes PRPE(gE) none Function of N, P, Light,

Function of N, P, Light, Temp, Salt

Temp, Salt

rEE rE = 0.01m2/g−day LRPE(mTa +mEE) 1/day constant

RRPE(rEE) 1/day Function of Temp

mTa +mEE rE = 0.05m2/g−day

An additional state variable is also added to account for shoot detritus at the bottom of the water column:

∂ (RPD) ∂t

= FPRSD ·PRPS ·RPS−LRPDRPS (8.127)

where, RPD is the Rooted Plant Shoot Detritus Biomass (g C/m2), FRPSD is the fraction of shoot loss to detritus (0 < FRPSD < 1), and LRPD is the decay rate of detritus (1/day).

It is noted that the Florida Bay seagrass model does not include this variable.

- 8.2.1.1 Production Rate for Plant Shoots The production or growth rate for plant shoots is given by:


PRPS = PMRPS · f1W (N)· f1B(N)· f2(I)· f3(T)· f4(S)· f5(RPS) (8.128) where,

PMRPS (VT, VH) is the maximum growth rate under optimal conditions for plant shoots (1/day),

- f1(N) is the effect of suboptimal nutrient concentration (0 ≤ f1 ≤ 1),
- f2(I) is the effect of suboptimal light intensity (0 ≤ f2 ≤ 1),
- f3(T) is the effect of suboptimal temperature (0 ≤ f3 ≤ 1),
- f4(S) is the effect of salinity on fresh water plant shoot growth (0 ≤ f4 ≤ 1), and
- f5(RPS) is the carrying capacity effect on shoot growth (0 ≤ f5 ≤ 1).


The subscripts ”W” and ”B” indicate the water column and the bed, respectively. Maximum growth rates for the Florida Bay seagrass model are shown in Table 8.5.

Table 8.5. Maximum Growth Rate

Parameter Units Generic Thalassia Halodule PMRPS (VT, VH) 1/day constant 0.208 0.29

###### 186



<<<PAGE 200>>>

###### 8. EUTROPHICATION EFDC+ Theory



- 8.2.1.1.1 Effect of Nutrients on Production Nutrient limitation is specified in terms of both water column and bed nutrient levels by:

f1W (N) = min

(NH4+NO3)W KHNRPS +(NH4+NO3)W

,

PO4dW KHPRPS +PO4dW f1B(N) = min

(NH4+NO3)B KHNRPS +(NH4+NO3)B

,

PO4dB KHPRPS +PO4dB

(8.129)

where,

NH4 is the NH4+ concentration as N (g N/m3), NO3 is the NO−

3 + NO−

2 concentration as N (g N/m3), KHNRPS is the half-saturation constant for N uptake from water column (g N/m3), KHNRPR (KTN,KHN) is the half-saturation constant for N uptake from bed (g N/m3), PO4d is the dissolved phosphate phosphorus concentration (g P/m3), KHPRPS is the half-saturation constant for phosphorus uptake from water column (g P/m3), and KHPRPR (KTP,KHP) is the half-saturation constant for phosphorus uptake from bed (g P/m3).

Parameter values from the Florida Bay Seagrass Model are provided in Table 8.6.

Table 8.6. List of Nutrient Limitation Parameters for the Florida Bay Seagrass Model

Parameter Units Generic Thalassia Halodule KHNRPS g N/m3 constant 0.0 0.0 KHNRPR g N/m3 constant 0.00056 0.00056 KHPRPS g P/m3 constant 0.0 0.0 KHPRPR g P/m3 constant 0.0031 0.0031

- 8.2.1.1.2 The Light Field The light field in the water column is governed by


∂I ∂Z∗

= −Kess ·I (8.130) where,

I is the light intensity (Langley/day), Kess is the light extinction coefficient (1/m), and Z∗ is the depth below the water surface (m).

###### 187



<<<PAGE 201>>>

###### 8. EUTROPHICATION EFDC+ Theory



With the light extinction coefficient being a function of the depth below the water surface. Integration of 8.130 gives

Z∗ 0

Kess ·dZ∗ (8.131) The light intensity at the water surface Iws, is given by

I = Iwsexp −

Iws = Iomin(exp(−Keme ·(HRPS −H)) ,1) (8.132) where,

Io is the light intensity at the top of the emergent shoot canopy for emergent shoots or the light

intensity at the water surface for submerged shoots (W/m2), Keme is the light extinction coefficient for emergent shoots (1/m), HRPS is the shoot height (m), and H is the water column depth (m).

For submerged shoots, it is assumed that the light extinction coefficient in the water column above the shoot canopy is given by

M

Bm CChlm

### ∑

Kessac = Keb +KeTSS ·TSS+KeVSS ·VSS+KeChl

m=1

And the light extinction coefficient in the water column within the canopy is given by

(8.133)

M

Bm CChlm

### ∑

+KeRPS ·RPS (8.134) where,

Kessic = Keb +KeTSS ·TSS+KeVSS ·VSS+KeChl

m=1

Keb is the background light extinction (1/m), KeTSS is the light extinction coefficient for inorganic suspended solid (1/m per g/m3), TSS is the total inorganic suspended solid concentration (g/m3) provided from the hydrodynamic

model, KeVSS is the light extinction coefficient for volatile suspended solid (1/m per g/m3), VSS is the volatile suspended solid concentration (g/m3) provided from the water quality model, CChlRPE is the C-to-chlorophyll ratio for epiphytes (g C per mg Chl), KeChl is the light extinction coefficient for algae chlorophyll (1/m per mg Chl/m3), Bm is the concentration of algae group m (g C per ml), CChlm is the C-to-chlorophyll ratio in algal group m (g C per mg Chl), KeRPS is the light extinction coefficient for rooted plant shoots (1/m per gm C/m2), and RPS is the concentration of plant shoots (g C per m2).

###### 188



<<<PAGE 202>>>

###### 8. EUTROPHICATION EFDC+ Theory



The forms of equations 8.133 and 8.134 readily allow for the inclusion of algae biomass into the volatile suspended solids or vice-versa. The form of equation 8.134 assumes that the shoots are primarily self shading and that epiphyte effect are manifest on the shoot surface.

The solutions of equation 8.131 above and in the canopy are

I = Iwsexp(−Kessac ·Z∗) ; 0 ≤ Z∗ ≤ H −HRPS (8.135) I = Ict ·exp(−Kessic ·(Z∗ −H +HRPS)) ; H −HRPS ≤ Z∗ ≤ H (8.136)

Ict = Iws ·exp(−Kessac ·(H −HRPS))

Since rooted plants are represented as C mass per unit area, the average light intensity over the shoot canopy is an appropriate light measure. For emergent shoots, the average of equation 8.135 over the water column depth, noting that H = HRPS, is

Iws Kessic ·H

Iicwa =

(1−exp(−Kessac ·H) ) (8.137)

For submerged shoots, the average over the canopy is

Iws Kessic ·HRPS

Iicwa =

exp(−Kessac ·(H −HRPS)) ·(1−exp(−Kessic ·HRPS) ) (8.138)

where Iicwa in both equation 8.137 and equation 8.138 is the average in canopy water column light intensity. When epiphytes grow on the shoot surface, the light intensity at the shoot surface is further reduced according to

IRPS = Iicwexp(−KeRPE ·RPE) (8.139) where,

IRPS is the light intensity on the plant shoots (W/m2), Iicw is the average water column light intensity in the shoot canopy (W/m2), and KeRPE is the light extinction coefficient for epiphyte (m2 per gm C).

For the Florida Bay seagrass model, the epiphyte light extinction coefficient is given by

where,

δRPE ∑Nspecies 2·RPSW ·δRPS

KeRPE = 0.11

RPS

δRPE is the epiphyte dry mass to C mass ratio, δRPS is the rooted plant shoot dry mass to C mass ratio, and WRPS is the rooted plant shoot mass per unit shoot area.

(8.140)

###### 189



<<<PAGE 203>>>

###### 8. EUTROPHICATION EFDC+ Theory



Values of these parameters for the Florida Bay model are listed in the Table 8.7. It is noted that the expression in equation 8.140 is not dimensionally homogeneous with the numerical coefficient 0.11 having implied units of (cm2 leaf sur face area )/( mg dry weight). Equation 8.140 can be made dimensionally consistent by use of the alternative form

RPE ∑Nspecies(KRPSE ·RPS)

KeRPE ·RPE =

Where the dimensionless parameter KRPSE is also defined in Table 8.7

Table 8.7. Epiphyte Light Attenuation Parameter for Florida Bay Seagrass Model

Parameter Units Thalassia Halodule δRPE Dry mass/ Carbon mass 9 9 δRPS Dry mass/ Carbon mass 2.94 2.4 WRPS Mg dry mass/ C-m2 leaf area 1.7 2 KRPSE Dimensionless 3.49 2.42

(8.141)

Using equations 8.139 and 8.135, the light intensity on the shoot surface can be expressed as

IRPS = Iws ·exp(−Kessac ·(H −HRPS)−KeRPE ·RPE) ·exp(−Kessic ·(Z∗ −H +HRPS)) (8.142) While equations 8.139 and 8.138 give the canopy average light intensity on the shoot surface

Iws Kessic ·HRPS

IRPSA =

exp(−Kessac ·(H −HRPS)−KeRPE ·RPE) ·(1−exp(−Kessic ·HRPS) ) (8.143)

##### 8.2.1.1.3 Effects of Light on Growth

In the EFDC+ generic rooted plant model, the effect of light on rooted plant growth is estimated based on Steele’s equation (Steele, 1962)

I IRSPopt

I IRSPopt

exp 1−

f2(I) =

which can be applied in terms of the average light intensity reaching the shoots to give

(8.144)

IRPSA IRSPopt

IRPSA IRSPopt

(8.145) or due to its unique mathematical form directly averaged over the shoot canopy. The average is given by

f2(I) =

exp 1−

F2 HRPS

f2avg(I) =

With the results being

H

exp

H−HRPS

1−Kessic ·(Z∗ −H +HRPS) −F2 ·exp(−Kessic ·(Z∗ −H +HRPS))

dZ∗ (8.146)

###### 190



<<<PAGE 204>>>

###### 8. EUTROPHICATION EFDC+ Theory



exp(1) Kessic ·HRPS

f2avg(I) =

[exp(−F2 ·exp(−Kessic ·HRPS) ) −exp(F2) ] (8.147)

Iws IRSPopt ·exp( −Kessac ·(H −HRPS)−KeRPE ·RPE) (8.148)

F2 =

- 8.2.1.1.4 Effect of Temperature on Shoot Growth The effect of temperature on shoot growth is given by a Gaussian function

f3(T) =

 



- exp −KTP1RPS[T −TP1RPS]2 if T ≤ TP1RPS 1 if TP1RPS < T < TP2RPS
- exp −KTP2RPS[T −TP2RPS]2 if T ≥ TP1RPS


(8.149)

where, T is the temperature (◦C) provided from the hydrodynamic model, TP1RPS < T < TP2RPS is the optimal temperature range for shoot production (◦C), KTP1RPS is the effect of temperature below TP1RPS on shoot production (1/◦C2), and KTP2RPS is the effect of temperature above TP2RPS on shoot production (1/◦C2).

or an exponential function.

f3(T) = exp(KTPRPS[T −TPREFRPS]) (8.150) where,

TPREFRPS is the reference temperature for shoot production (◦C), and KTPRPS is the effect of temperature on shoot production (1/◦C).

The parameters for the Florida Bay seagrass model given in Table 8.8.

Table 8.8. Parameters for Temperature Effect on Growth for Equation 8.150

Parameter Units Thalassia Halodule TPREFRPS ◦C 28 31 KTPRPS 1/◦C 0.07 0.07

- 8.2.1.1.5 Effect of Salinity The effect of salinity on fresh water plant shoot growth is given by


where,

STOXS2 STOXS2 +S2

f4(S) =

(8.151)

###### 191



<<<PAGE 205>>>

###### 8. EUTROPHICATION EFDC+ Theory



STOXS is the salinity at which growth is halved (ppt), and S is the salinity in water column (ppt) provided from the hydrodynamic model

- 8.2.1.1.6 Effect of Rooted Plant Density The effect of rooted plant density on growth is given by


RPS RPSsat

f5(RPS)=1− ∑

species

2

(8.152)

where RPSsat is the density saturation parameter (g C/m2). The summation indicates when multiple species are simulated, the total density of all species affects each individual species

Table 8.9. Parameters for Plant Density Effect on Growth for Equation 8.152

Parameter Units Thalassia Halodule RPSsat (g C/m2) 400 667

- 8.2.1.2 Respiration Rate for Plant Shoots The respiration rate for plant shoots is assumed to be temperature dependent


RRPS = RREFRPS ·exp(KTRRPS[T −TRREFRPS]) (8.153) where,

RREFRPS is the reference respiration rate for shoots (1/day), T is the temperature (◦C) provided from the hydrodynamic model, TRREFRPS is the reference temperature for shoot respiration (◦C), and KTRRPS is the effect of temperature on shoot respiration (1/◦C2).

Table 8.10. Parameters for Shoot Respiration in the Florida seagrass model

Parameter Units Thalassia Halodule RREFRPS 1/day 0.01 0.029 KTRRPS dimensionless 0.07 0.07 TRREFRPS ◦C 28 31

###### 192



<<<PAGE 206>>>

###### 8. EUTROPHICATION EFDC+ Theory



- 8.2.1.3 Non-Respiration Loss Rate for Plant Shoots The non-respiration loss rate for shoots is assumed to be temperature dependent.

LRPS = LREFRPS ·exp(KTLRPS[T −TLREFRPS]) (8.154) where,

LREFRPS is the reference loss rate for shoots (1/day), T is the temperature (◦C) provided from the hydrodynamic model, TLREFRPS is the reference temperature for shoot loss (◦C), and KTLRPS is the effect of temperature on shoot loss (1/◦C2).

Table 8.11. Parameters for Shoot Mortality of non-respiration loss in the Florida seagrass model

Parameter Units Thalassia Halodule LREFRPS 1/day 0.001 0.004 KLRRPS dimensionless 0.07 0.07 TLREFRPS ◦C 28 28

- 8.2.1.4 Carbon Transport from Roots to Shoots


The C transport from roots to shoots is defined as positive to the shoots. Two formulations can be utilized; the first is based on observed shoot to root biomass ratios

where,

JRPRS = KRPORS ·(RPR−RORS·RPS) (8.155) RORS =

RPRobs RPSobs

(8.156)

KRPORS is the root to shoot transfer rate to follow observed ratio (1/day), and RORS is the observed ratio of root C to shoot C (dimensionless).

and the second formulation transfers root C to shoot C under unfavorable light conditions for the shoots

ISS ISS +ISSS

JRPRS = KRPRS

RPR (8.157) where,

KRPRS (χTb,χHb) is the root to shoot transfer rate (1/day), ISS is the solar ratio at shoot surface (W/m2),

###### 193



<<<PAGE 207>>>

###### 8. EUTROPHICATION EFDC+ Theory



ISSS is the half-saturation solar ratio at shoot surface (W/m2).

Table 8.12. Root to Shoot Transport Parameters in Equation 8.157

Parameter Dimension Generic Thalassia Halodule KRPORS 1/day constant 5E-4 1E-5 RORS dimensionless constant 0.0 0.0 KRPRS 1/day constant 5E-4 1E-5 ISSS W/m2 constant 0.0 0.0

- 8.2.1.5 Respiration Rate for Plant Roots The respiration rate for plant roots is assumed to be temperature dependent

RRPR = RREFRPR ·exp(KTRRPR[T −TRREFRPR]) (8.158)

where, RREFRPR is the reference respiration rate for roots (1/day), T is the temperature (◦C) provided from the hydrodynamic model, TRREFRPR is the reference temperature for root respiration (◦C), and KTRRPR is the effect of temperature on shoot respiration (1/◦C2).

Table 8.13. Parameters for Root Respiration in Equation 8.158

Parameter Units Thalassia Halodule RREFRPR 1/day 0.0025 0.011 KTRRPR dimensionless 0.07 0.07 TRREFRPR ◦C 28 31

- 8.2.1.6 Non-Respiration Loss Rate for Plant Roots The non-respiration loss rate for shoots is assumed to be temperature dependent.


LRPR = LREFRPR ·exp(KTLRPR[T −TLREFRPR]) (8.159) Table 8.14. Parameters for Root Mortality in Equation 8.159

Parameter Units Thalassia Halodule LREFRPR 1/day 1E-4 4E-4 KLRRPR dimensionless 0.07 0.07 TLREFRPR ◦C 28 28

###### 194



<<<PAGE 208>>>

###### 8. EUTROPHICATION EFDC+ Theory



- 8.2.1.7 Production Rate for Epiphytes The production or growth rate for epiphytes on plant shoots is given by


PRPE = PMRPE · fW (N)· f2(I)· f3(T)· f4(RPE,RPS) (8.160) where ,

PMRPE is the maximum growth rate under optimal conditions for plant shoots (1/day),

- f1(N) is the effect of suboptimal nutrient concentration (0≤f1≤1),
- f2(I) is the effect of suboptimal light intensity (0≤f2≤1),
- f3(T) is the effect of suboptimal temperature (0≤f3≤1), and
- f4(RPE,RPS) is the effect of epiphyte and host rooted density (0 ≤ f4 ≤ 1).


##### 8.2.1.7.1 Effect of Nutrients on Epiphyte Growth Nutrient limitation for epiphytes is given by

PO4d KHPRPE +PO4d

NH4+NO3 KHNRPE +NH4+NO3

(8.161) where,

f1(N) = min

,

NH4 is the NH4+ concentration as N (g N/m3), NO3 is the NO−

2 concentration as N (g N/m3), KHNRPE is the half-saturation constant for N uptake for epiphytes (g N/m3), PO4d is the dissolved PO−3

3 + NO−

4 concentration as P (g P/m3), and KHPRPE is the half-saturation constant for P uptake for epiphytes (g P/m3).

###### 8.2.1.7.2 Effect of Light on Epiphyte Growth Light limitation for epiphyte growth is based on a Monod type equation (e.g., Bunch et al., 2000):

IRPE IRPE +KHIRPE

(8.162) where,

f2(I) =

KHIRPE is the half-saturation constant for epiphyte light limitation (W/m2).

The average light intensity over the shoot canopy

Iws Kessic ·HRPS

exp(−Kessac ·(H −HRPS)) ·(1−exp(−Kessic ·HRPS) ) (8.163)

IRPEA =

###### 195



<<<PAGE 209>>>

###### 8. EUTROPHICATION EFDC+ Theory



which follows from equation 8.143 with KeRPE = 0. Equation 8.162 can be averaged over the shoot canopy to give

1 Kessic ·HRSP

f2avg(I) =

ln

KHIRPE +Ictexp(−Kessic ·(H −HRSP)) KHIRPE +Ictexp(−Kessic ·H)

(8.164) Ict = Iws ·exp(−Kessic ·(H −HRSP)) (8.165)

##### 8.2.1.7.3 Effect of Temperature on Epiphyte Growth The effect of temperature on epiphyte growth is given by

where,

f3(T) =

 

exp(−KTP1RPE[T −TP1RPE]2), T ≤TP1RPE 1, TP1RPE < T < TP2RPE exp(−KTP2RPE[T −TP2RPE]2), T ≥TP1RPE



T is the temperature (◦C) provided from the hydrodynamic model, TP1RPE < T < TP2RPE is the optimal temperature range for epiphyte production (◦C),

- KTP1RPE is the effect of temperature below TP1RPE on epiphyte production (1/◦C2), and
- KTP2RPE is the effect of temperature above TP2RPE on epiphyte production (1/◦C2)


##### 8.2.1.7.4 Effect of Epiphyte and Rooted Plant Density on Epiphyte Growth The effect of rooted plant density on growth is given by

where

######  

  RPE ·δRPE

2

f4(RPE,RPS) = 1−

WRPE ∑Nspecies 2·RPSW ·δRPS

RPS

δRPE is the Epiphyte dry mass to C mass ratio WRPE is the maximum epiphyte mass per unit shoot area

(8.166)

(8.167)

- 8.2.1.8 Respiration Rate for Epiphytes The respiration rate for epiphytes is assumed to be temperature dependent:


RRPE = RREFRPE ·exp KTRRPE [T −TRREFRPE]2 (8.168) where,

###### 196



<<<PAGE 210>>>

###### 8. EUTROPHICATION EFDC+ Theory



RREFRPE is the reference respiration rate for epiphytes (1/day), T is the temperature (◦C) provided from the hydrodynamic model, TRREFRPE is the reference temperature for epiphytes respiration (◦C), and KTRRPE is the effect of temperature on epiphytes respiration (1/◦C2).

- 8.2.1.9 Coupling with Organic Carbon (OC) The interaction between rooted plants and epiphytes and water column (W) and bed OC species is given by:


∂RPOCW ∂t

=

1 H

(FCRRPS ·RRPS +(1−FRPSD)·FCRLRPS ·LRPS)RPS

1 H

(FCRRPE ·RRPE +FCRLRPE ·LRPE)RPE +

+

1 H

FCRLRPD ·LRPD ·RPD (8.169)

∂RPOCB ∂t

=

1 B

(FCRRPR ·RRPR +FCRLRPR ·LRPR)RPR (8.170)

∂LPOCW ∂t

=

1 H

(FCLRPS ·RRPS +(1−FRPSD)·FCLLRPS ·LRPS)RPS

1 H

(FCLRPE ·RRPE +FCLLRPE ·LRPE)RPE +

+

1 H

FCLLRPD ·LRPD ·RPD (8.171)

∂LPOCB ∂t

=

1 B

(FCLRPR ·RRPR +FCLLRPR ·LRPR)RPR (8.172)

∂DOCW ∂t

=

1 H

(FCDRPS ·RRPS +(1−FRPSD)·FCDLRPS ·LRPS)RPS

1 H

(FCDRPE ·RRPE +FCDLRPE ·LRPE)RPE +

+

1 H

FCDLRPD ·LRPD ·RPD (8.173)

∂DOCB ∂t

1 B

(FCDRPR ·RRPR +FCDLRPR ·LRPR)RPR (8.174) where,

=

RPOC is the concentration of RPOC (g C/m3), LPOC is the concentration of LPOC (g C/m3), DOC is the concentration of DOC (g C/m3), FCR is the fraction of respired C produced as RPOC, FCL is the fraction of respired C produced as LPOC,

###### 197



<<<PAGE 211>>>

###### 8. EUTROPHICATION EFDC+ Theory



FCD is the fraction of respired C produced as DOC, FCRL is the fraction of non-respired C produced as RPOC, FCLL is the fraction of non-respired C produced as LPOC, FCDL is the fraction of non-respired C produced as DOC, H is the depth of water column, and B is the depth of bed.

- 8.2.1.10 Coupling with Dissolved Oxygen (DO) The interaction between rooted plants and epiphytes and DO is given by

∂DOW ∂t

=

1 H

(PRPS ·RPSOC·RPS+PRPE ·RPEOC·RPE) (8.175) where,

DO is the concentration of DO (g O2/m3), RPSOC is the O to C ratio for plant shoots (g O2 per g C), and RPEOC is the O to C ratio for epiphytes (g O2 per g C).

- 8.2.1.11 Coupling with Phosphorous (P) The interaction between rooted plants and epiphytes and water column and bed P is given by


∂RPOPW ∂t

1 H

(FPRRPS ·RRPS +(1−FRPSD)·FPRLRPS ·LRPS)·RPSPC·RPS

=

1 H

(FPRRPE ·RRPE +FPRLRPE ·LRPE)·RPEPC·RPE

+

1 H

FPRLRPD ·LRPD ·RPSPC·RPD (8.176)

+

∂RPOPB ∂t

=

1 B

(FPRRPR ·RRPR +FPRLRPR ·LRPR)RPRPC·RPR (8.177)

∂LPOPW ∂t

1 H

(FPLRPS ·RRPS +(1−FRPSD)·FPLLRPS ·LRPS)·RPSPC·RPS

=

1 H

(FPLRPE ·RRPE +FPLLRPE ·LRPE)·RPEPC·RPE

+

1 H

FPLLRPD ·LRPD ·RPSPC·RPD (8.178)

+

∂LPOPB ∂t

=

1 B

(FPLRPR ·RRPR +FPLLRPR ·LRPR)RPRPC·RPR (8.179)

###### 198



<<<PAGE 212>>>

###### 8. EUTROPHICATION EFDC+ Theory



∂DOPW ∂t

1 H

(FPDRPS ·RRPS +(1−FRPSD)·FPDLRPS ·LRPS)·RPSPC·RPS

=

1 H

(FPDRPE ·RRPE +FPDLRPE ·LRPE)·RPEPC·RPE

+

1 H

FCDLRPD ·LRPD ·RPSPC·RPD (8.180)

+

∂DOPB ∂t

1 B

(FPDRPR ·RRPR +FPDLRPR ·LRPR)RPRPC·RPR (8.181)

=

∂PO4tW ∂t

1 H

(FPIRPS ·RRPS +(1−FRPSD)·FPILRPS ·LRPS)·RPSPC·RPS

=

1 H

(FPIRPE ·RRPE +FPILRPE ·LRPE)·RPEPC·RPE

+

1 H

1 H

FCILRPD ·LRPD ·RPSPC·RPD−

FRPSPW ·RRPS ·RPSPC·RPS

+

1 H

PRPE ·RPEPC·RPE (8.182)

−

∂PO4tB ∂t

1 B

(FPIRPR ·RRPR +FPILRPR ·LRPR)RPRPC·RPR−

=

1 H

(1−FRPSPW)PRPS ·RPRPC·RPS (8.183)

KHPRPRP04dw KHPRPRPO4dw +KHPRPSP04db

(8.184) where,

FRPSPW =

RPOP is the concentration of RPOP (g P/m3), LPOP is the concentration of LPOP (g P/m3), DOP is the concentration of DOP (g P/m3), PO4t = PO4d +PO4p is the PO4t (g P/m3), PO4d is the concentration of dissolved PO−3

4 (g P/m3), PO4p is the concentration of sorbed PO−3

4 (g P/m3), FPR is the fraction of respired P produced as RPOP, FPL is the fraction of respired P produced as LPOP, FPD is the fraction of respired P produced as DOP, FPI is the fraction of respired P produced as PO4t, FPRL is the fraction of non-respired P produced as RPOP,

###### 199



<<<PAGE 213>>>

###### 8. EUTROPHICATION EFDC+ Theory



FPLL is the fraction of non-respired P produced as LPOP, FPDL is the fraction of non-respired P produced as DOP, FPIL is the fraction of non-respired P produced as PO4t, RPSPC is the plant shoot P to C ratio (g P per g C), RPRPC is the plant root P to C ratio (g P per g C), RPEPC is the epiphyte P to C ratio (g P per g C), FRPSPW is the fraction of PO4d uptake from water column, KHPRPS is the half-saturation constant for P uptake from water column (g P/m3), and KHPRPR is the half-saturation constant for P uptake from bed (g P/m3).

- 8.2.1.12 Coupling with Nitrogen (N) The interaction between rooted plants and epiphytes and water column and bed N is given by


∂RPONW ∂t

1 H

(FNRRPS ·RRPS +(1−FRPSD)·FNRLRPS ·LRPS)·RPSNC·RPS

=

1 H

(FNRRPE ·RRPE +FNRLRPE ·LRPE)·RPENC·RPE

+

1 H

FNRLRPD ·LRPD ·RPSNC·RPD (8.185)

+

∂RPONB ∂t

=

1 B

(FNRRPR ·RRPR +FNRLRPR ·LRPR)RPRNC·RPR (8.186)

∂LPONW ∂t

1 H

(FNLRPS ·RRPS +(1−FRPSD)·FNLLRPS ·LRPS)·RPSNC·RPS

=

1 H

(FNLRPE ·RRPE +FNLLRPE ·LRPE)·RPENC·RPE

+

1 H

FNLLRPD ·LRPD ·RPSNC·RPD (8.187)

+

∂LPONB ∂t

=

1 B

(FNLRPR ·RRPR +FNLLRPR ·LRPR)RPRNC·RPR (8.188)

∂DONW ∂t

1 H

(FNDRPS ·RRPS +(1−FRPSD)·FNDLRPS ·LRPS)·RPSNC·RPS

=

1 H

(FNDRPE ·RRPE +FNDLRPE ·LRPE)·RPENC·RPE

+

1 H

FNDLRPD ·LRPD ·RPSNC·RPD (8.189)

+

###### 200



<<<PAGE 214>>>

###### 8. EUTROPHICATION EFDC+ Theory



∂DONB ∂t

1 B

(FNDRPR ·RRPR +FNDLRPR ·LRPR)RPRNC·RPR (8.190)

=

∂NH4W ∂t

1 H

(FNIRPS ·RRPS +(1−FRPSD)·FNILRPS ·LRPS)·RPSNC·RPS

=

1 H

(FNIRPE ·RRPE +FNILRPE ·LRPE)·RPENC·RPE

+

1 H

FNILRPD ·LRPD ·RPSNC·RPD −

+

1 H

PNRPS ·FRPSNW ·RRPS ·RPSNC·RPS

1 H

PNRPE ·PRPE ·RPENC·RPE (8.191)

−

∂NH4B ∂t

1 B

(FNIRPR ·RRPR +FNILRPR ·LRPR)RPRNC·RPR −

=

1 H

PNRPE (1−FRPSPW)PRPS ·RPSNC·RPS (8.192)

∂NO3W ∂t

= −

1 H

(1−PNRPS)FRPSNW ·PRPS ·RPSNC·RPS

−

1 H

(1−PNRPE)PRPE ·RPENC·RPE (8.193)

∂NO3B ∂t

1 H

(1−PNRPS)(1−FRPSNW)PRPS ·RPSNC·RPS (8.194)

= −

NH4·NO3 (KHNPRPS +NH4)(KHNPRPS +NO3)

PNRPS =

+

NH4·KHNPRPS (NH4+NO3)(KHNPRPS +NO3)

NH4·NO3 (KHNPRPE +NH4)(KHNPRPE +NO3)

PNRPE =

+

NH4·KHNPRPE (NH4+NO3)(KHNPRPE +NO3)

(8.195)

(8.196)

KHNRPR(NH4+NO3)w KHNRPR(NH4+NO3)w +KHNRPS(NH4+NO3)b

(8.197) where,

FRPSNW =

RPON is the concentration of RPON (g N/m3), LPON is the concentration of LPON (g N/m3), DON is the concentration of DON (g N/m3),

NH4 is the concentration of NH4+ as N (g N/m3),

###### 201



<<<PAGE 215>>>

###### 8. EUTROPHICATION EFDC+ Theory



2 as N (g N/m3), FNR is the fraction of respired N produced as RPON, FNL is the fraction of respired N produced as LPON, FND is the fraction of respired N produced as DON, FNI is the fraction of respired N produced as NH4+, FNRL is the fraction of non-respired N produced as RPON, FNLL is the fraction of non-respired N produced as LPON, FNDL is the fraction of non-respired N produced as DON, FNIL is the fraction of non-respired N produced as NH4+, RPSNC is the plant shoot N to C ratio (g; N; per g C), RPRNC is the plant root N to C ratio (g; N; per g C), FRPSNW is the plant shoot fraction of NH4 and NOX uptake from water column, PNRPS is the NH4+ preference fraction for plant shoots, KHNPRPS is the saturation coefficient for N preference for plant shoots (g; N; per g C), PNRPE is the NH4+ preference fraction for epiphytes, KHNPRPE is the saturation coefficient for N preference for epiphytes (g; N; per g C), KHNRPS is the half-saturation constant for N uptake from water column (g N/m3), and KHNRPR is the half-saturation constant for N uptake from bed (g N/m3).

NO3 is the concentration of NO−

3 + NO−

##### 8.3. Sediment Diagenesis and Flux Formulation

EFDC+ water quality model provides three options for defining the sediment-water interface fluxes for nutrients and DO. The options are; (1) externally forced spatially and temporally constant fluxes, (2) externally forced spatially and temporally variable fluxes, and (3) internally coupled fluxes simulated with the sediment diagenesis model. The water quality state variables that are controlled by diffusive exchange across the sediment-water interface include PO−3

4 , NH4+, NO−

3 , SiO2, COD and DO. The first two options require that the sediment fluxes be assigned as spatial/temporal forcing functions based on either observed sitespecific data from field surveys or best estimates based on the literature and sediment bed characteristics. The first two options, although acceptable for model calibration against historical data sets, do not provide the cause-effect predictive capability that is needed to evaluate future water quality conditions that might result from implementation of pollutant load reductions from watershed runoff. The third option, activation of the sediment diagenesis model developed by Di Toro et al. (2001) does provide the cause-effect predictive capability to evaluate how water quality conditions might change with implementation of alternative load reduction or management scenarios.

Living and non-living particulate OC deposition, simulated in the EFDC+ water quality model, is internally coupled with the EFDC+ sediment diagenesis model. The sediment diagenesis model, based on the sediment flux model of Di Toro et al. (2001), describes the decomposition of POM in the sediment bed, the consumption of DO at the sediment-water interface (SOD) and the exchange of dissolved constituents (NH4+, NO−

3 , PO−3

4 , SiO2, COD) across the sediment-water interface. State variables of the EFDC+ sediment flux model are sediment bed temperature, sediment bed POC, PON, POP, porewater concentrations

###### 202



<<<PAGE 216>>>

###### 8. EUTROPHICATION EFDC+ Theory



of PO−3

4 , NH4+, NO−

3 , SiO2 and S−

2 /CH4. The sediment diagenesis model computes sediment-water fluxes of COD, SOD, PO−3

4 , NH4+, NO−

3 , and SiO2. The state variables modeled for a typical lake sediment flux model are listed and described in Table 8.15. An overview of the source and sink terms is presented with a description of each state variable group in this section. The details of the state variable equations, kinetic terms and numerical solution methods for the sediment diagenesis model are presented in Di Toro et al. (2001); Ji (2008); Park et al. (1995).

Table 8.15. EFDC+ Sediment Diagenesis Model State Variables

# Name Bed Layer Units

- 1 POC-G1 Layer-2 g/m3
- 2 POC-G2 Layer-2 g/m3
- 3 POC-G3 Layer-2 g/m3
- 4 PON-G1 Layer-2 g/m3
- 5 PON-G2 Layer-2 g/m3
- 6 PON-G3 Layer-2 g/m3
- 7 POP-G1 Layer-2 g/m3
- 8 POP-G2 Layer-2 g/m3
- 9 POP-G3 Layer-2 g/m3
- 10 SiP Layer-2 g/m3
- 11 S−

- 2 /CH4 Layer-1 g/m3

12 S−

- 2 /CH4 Layer-2 g/m3

13 NH4+ Layer-1 g/m3 14 NH4+ Layer-2 g/m3 15 NO−

- 3 Layer-1 g/m3


- 16 NO−

- 3 Layer-2 g/m3

17 PO−3

- 4 Layer-1 g/m3


- 18 PO−3

4 Layer-2 g/m3

- 19 Available-SiO2 Layer-1 g/m3
- 20 Available-SiO2 Layer-2 g/m3
- 21 NH4+-Flux g/m2 −day
- 22 NO−

- 3 -Flux g/m2 −day

23 PO−3

- 4 -Flux g/m2 −day


- 24 SiO2 Flux g/m2 −day
- 25 SOD g/m2 −day
- 26 COD Flux g/m2 −day
- 27 Sediment Temperature ◦C


A sediment process model developed by DiToro and Fitzpatrick (1993) hereinafter referred to as D&F was coupled with ICM for the Chesapeake Bay water quality modeling (Cerco and Cole, 1994). The sediment process model was slightly modified and incorporated into the EFDC+ water quality model to simulate the processes in the sediment and at the sediment-water interface. The description of the EFDC+ sediment process model in this section is from Park et al. (1995).

The NO−

3 state variables (15, 16 and 22 in Table 8.15), represent the sum of NO−

3 and NO−

2 in the model.

###### 203



<<<PAGE 217>>>

###### 8. EUTROPHICATION EFDC+ Theory



The difference in decay rates of POM is accounted for by assigning a fraction of POM to various decay classes (Westrich and Berner, 1984). POM in the sediments is divided into three G classes, or fractions, representing three scales of reactivity. The G1 (labile) fraction has a half life of 20 days, and the G2 (refractory) fraction has a half life of one year. The G3 (inert) fraction is non-reactive, i.e., it undergoes no significant decay before burial into deep, inactive sediments. The varying reactivity of the G classes controls the time scale over which changes in depositional flux is reflected in changes in diagenesis flux. If the G1 class would dominate the POM input into the sediments, then there would be no significant time lag introduced by POM diagenesis and any changes in depositional flux would be readily reflected in diagenesis flux.

In the sediment model, benthic sediments are represented as two layers (Figure 8.6). Details of the processes shown in Figure 8.6 will be discussed in the next sections. The upper layer (Layer 1) is in contact with the water column and may be oxic or anoxic depending on DO concentration in the overlying water. The lower layer (Layer 2) is permanently anoxic. The upper layer depth, which is determined by the penetration of oxygen into the sediments, is at its maximum only a small fraction of the total depth. Because H1 (∼ 0.1cm) << H2,

H = H1 +H2 ≈ H2 (8.198) where,

H is the total depth (approximately 10cm), H1 is the upper layer depth, and H2 is the lower layer depth.

Fig. 8.6. Sediment Layers and Processes Included in Sediment Process Model

###### 204



<<<PAGE 218>>>

###### 8. EUTROPHICATION EFDC+ Theory



The model incorporates three basic processes (Figure 8.7); (1) depositional flux of POM, (2) the diagenesis of POM, and (3) the resulting sediment flux. The sediment model is driven by the net settling of POC, PON, POP and PSi from the overlying water to the sediments (depositional flux). Because of the negligible thickness of the upper layer (equation 8.198), deposition proceeds from the water column directly to the lower layer. Within the lower layer, the model simulates the diagenesis (mineralization or decay) of deposited POM, which produces O demand and inorganic nutrients (diagenesis flux). The third basic process is the flux of substances produced by diagenesis (sediment flux). O demand, as S−

2 (in saltwater) or CH4 (in freshwater), takes three paths out of the sediments; (1) oxidation at the sediment-water interface as SOD, (2) export to the water column as COD, or (3) burial to deep, inactive sediments. Inorganic nutrients produced by diagenesis take two paths out of the sediments; (1) release to the water column or (2) burial to deep, inactive sediments (Figure 8.7).

Fig. 8.7. Schematic Diagram for Sediment Process Model

This section describes the three basic processes with reactions and sources/sinks for each state variable. The method of the solution includes finite difference equations, solution scheme, boundary, and initial conditions. Complete model documentation can be found in DiToro and Fitzpatrick (1993).

##### 8.3.1 Depositional Flux

Deposition is one process that couples the water column model with the sediment model. Consequently, deposition is represented in both the water column and sediment models. In the water column model, the governing mass-balance equations for the following state variables contain settling terms, which represent the depositional fluxes:

- 1. algal groups (equation 8.6)
- 2. RPOC and LPOC (equations 8.41 and 8.42)
- 3. RPOP and LPOP (equations 8.58 and 8.59 and PO4t (equation 8.61)
- 4. RPON and LPON (equations 8.70 and 8.71)
- 5. SiP (equation 8.85) and SiA (equation 8.86)


The sediment model receives these depositional fluxes of POC, PON, POP and SiP. Because of the negligible thickness of the upper layer (equation 8.198), deposition is considered to proceed from the water column

###### 205



<<<PAGE 219>>>

###### 8. EUTROPHICATION EFDC+ Theory



directly to the lower layer. Since the sediment model has three G classes of POM depending on the time scales of reactivity (Section 8.3.1), the POM fluxes from the water column should be mapped into three G classes based on their reactivity. Then, the depositional fluxes for the ith G class (i = 1, 2 or 3) may be expressed as:

JPOC,i =FCLPi·WSLP·LPOCN+FCRPi·WSRP·RPOCN+ ∑

FCBx,i ·WSx ·BNx (8.199)

algae

JPON,i = FNLPi ·WSLP ·LPONN +FNRPi ·WSRP ·RPONN

### + ∑

FNBx,i ·ANCx ·WSx ·BNx (8.200)

algae

JPOP,i = FPLPi ·WSLP ·LPOPN +FPRPi ·WSRP ·RPOPN

### + ∑

FPBx,i ·APC·WSx ·BNx +γi ·WSTSS ·PO4Np (8.201)

algae

JPSi = WSd ·PSiN +ASCd ·WSd ·BNd +WSTSS ·SANp (8.202) where,

JPOM,i is the depositional flux of POM (M = C, N or P) routed into the ith G class (g/m2/day), JPSi is the depositional flux of SiP (g Si/m2/day), FCLPi,FNLPi and FPLPi are the fraction of water column LPOC, LPON, and LPOP respectively, routed

into the ith G class in sediment, FCRPi, FNRPi and FPRPi are the fraction of water column RPOC, RPON and RPOP respectively, routed into the ith G class in sediment, FCBx,i, FNBx,i and FPBx,i are the fraction of POC, PON and POP, respectively, in the algal group x

routed into the ith G class in sediment, and γi = 1 for i = 1,γi = 0 for i = 2 or 3.

In the source code, the sediment process model is solved after the water column water quality model. The calculated fluxes using the water column conditions at t = tn are used for the computation of the water quality variables at t = tn +θ, where θ = 2·m·∆t is the time step for the kinetic equations. The superscript

- N in equation 8.199 to 8.202 indicates the variables after being updated for the kinetic processes.


The settling of sorbed PO−3

4 is considered to contribute to the labile G1 pool in equation 8.201, and settling of sorbed SiO2 contributes to JPSi in equation 8.202 to avoid creation of additional depositional fluxes for inorganic particulates. The sum of distribution coefficients should be unity:

### ∑

FCLPi =∑

FNLPi =∑

FPLPi =∑

FCRPi =

i

i

i

i

### ∑

FNRPi =∑

FPRPi =∑

FCBx,i =∑

FNBx,i =∑

FPBx,i = 1.

i

i

i

i

i

###### 206



<<<PAGE 220>>>

###### 8. EUTROPHICATION EFDC+ Theory



The settling velocities, WSLP, WSRP, WSx, and WSTSS, as defined in the EFDC+ water column model (Section 8.1.3.2), are net settling velocities. If TAM is selected as a measure of sorption site, WSTSS is replaced by WSs in Equations 8.201 and 8.202.

##### 8.3.2 Diagenesis Flux

Another coupling point of the sediment model to the water column model is the sediment flux. The computation of sediment flux requires that the magnitude of the diagenesis flux be known. The diagenesis flux is explicitly computed using mass-balance equations for deposited POC, PON, and POP. Dissolved SiO2 is produced in the sediments as a result of the dissolution of SiP. Since the dissolution process is different from the bacterial-mediated diagenesis process, it is presented separately. In the mass-balance equations, the depositional fluxes of POM are the source terms and the decay of POM in the sediments produces the diagenesis fluxes. The integration of the mass-balance equations for POM provides the diagenesis fluxes that are the inputs for the mass-balance equations for NH4+, NO−

3 , PO−3

4 and S−

2 /CH4 in the sediments.

As the upper layer thickness is negligible (equation 8.198) the depositional flux is considered to proceed directly to the lower layer (equations 8.199, to 8.202), and diagenesis is considered to occur only in the lower layer. The mass-balance equations are similar for POC, PON, and POP, and for different G classes. The mass-balance equation in the anoxic lower layer for the ith G class (i = 1, 2 or 3) may be expressed as:

∂GPOM,i ∂t

= −KPOM,i ·θT−20

H2

POM,i ·GPOM,i ·H2 −W ·GPOM,i +JPOM,i (8.203) where,

GPOM,i is the concentration of POM(M = C, N or P) in the ith G class in Layer 2 (g/m3) KPMO,i is the decay rate of the ith G class POM at 20◦C in Layer 2 (1/day) θPOM,i is the constant for temperature adjustment for KPOM,i T is the sediment temperature (◦C) W is the burial rate (m/day)

Since the G3 class is inert KPOM,3 = 0. Once the mass-balance equations for GPOM,1 and GPOM,2 are solved, the diagenesis fluxes are computed from the rate of mineralization of the two reactive G classes:

JM =

2

∑

KPOM,i ·θT−20

POM,i ·GPOM,i ·H2 (8.204)

i=1

JM is the diagenesis flux (g/m2/day) of M = C, N or P

##### 8.3.3 Sediment Flux

##### 8.3.3.1 Basic Equations

The mineralization of POM produces soluble intermediates, which are quantified as diagenesis fluxes in the previous section. The intermediates react in the oxic and anoxic layers, and portions are returned to the

###### 207



<<<PAGE 221>>>

###### 8. EUTROPHICATION EFDC+ Theory



overlying water as sediment fluxes. Computation of sediment fluxes requires mass-balance equations for NH4+, NO−

3 , PO−3

4 , S−

2 /CH4 and available SiO2. This section describes the flux portion for NH4+, NO−

3 , PO−3

4 and S−

2 /CH4 of the model. In the upper layer, the processes included in the flux portion are:

- 1. exchange of dissolved fraction between Layer 1 and the overlying water,
- 2. exchange of dissolved fraction between Layer 1 and 2 via diffusive transport,
- 3. exchange of particulate fraction between Layer 1 and 2 via particle mixing,
- 4. loss by burial to the lower layer (Layer 2),
- 5. removal (sink) by reaction, and
- 6. internal sources.


Since the upper layer is quite thin (H1 ∼ 0.1 cm, equation 8.198) and the surface mass transfer coefficient (s) is on the order of 0.1 m/day, the residence time of dissolved nutrient in the upper layer is: H/s ∼ 10−2 days. Hence, a steady-state approximation is made in the upper layer. Then the mass-balance equation for NH4+, NO−

3 , PO−3

4 or S−

2 /CH4 in the upper layer is:

∂Ct1 ∂t

= 0 = s(fd0 ·Ct0 − fd1 ·Ct1)+KL(fd2 ·Ct2 − fd1 ·Ct1)

H1

K12 s

+ω (f p2 ·Ct2 − f p1 ·Ct1)−W ·Ct1 −

Ct1 +J1 (8.205) where,

Ct1 and Ct2 are the total concentrations in Layer 1 and 2, respectively (g/m3), Ct0 is the total concentrations in the overlying water (g/m3), s is the surface mass transfer coefficient (m/day), KL is the diffusion velocity for dissolved fraction between Layer 1 and 2 (m/day), ω is the particle mixing velocity between Layer 1 and 2 (m/day),

fd0 is the dissolved fraction of total substance in the overlying water (0 ≤ fd0 ≤ 1), fd1 is the dissolved fraction of total substance in Layer 1 (0 ≤ fd1 ≤ 1),

- f p1 is the particulate fraction of total substance in Layer 1 (= 1− fd1), fd2 is the dissolved fraction of total substance in Layer 2 (0 ≤ fd2 ≤ 1),
- f p2 is the particulate fraction of total substance in Layer 2 (= 1− fd2), K1 is the reaction velocity in Layer 1 (m/day), and J1 is the sum of all internal sources in Layer 1 (g/m2/day).


The first term on the RHS of equation 8.205 represents the exchange across sediment-water interface. Then the sediment flux from Layer 1 to the overlying water, which couples the sediment model to the water column model, may be expressed as:

###### 208



<<<PAGE 222>>>

###### 8. EUTROPHICATION EFDC+ Theory



Jaq = s(fd1 ·Ct1 − fd0 ·Ct0) (8.206) where, Jaq is the sediment flux of NH4+, NO−

3 , PO−3

2 /CH4 to the overlying water (g/m2/day). The convention used in equation 8.206 is that the positive flux is from the sediment to the overlying water. In the lower layer, the processes included in the flux portion are (Figure 8.6):

4 or S−

- 1. exchange of dissolved fraction between Layer 1 and 2 via diffusive transport,
- 2. exchange of particulate fraction between Layer 1 and 2 via particle mixing,
- 3. deposition from Layer 1 and burial to the deep inactive sediments,
- 4. removal (sink) by reaction, and
- 5. internal sources including diagenetic source.


3 , PO−3

The mass-balance equation for NH4+, NO−

4 or S−

2 /CH4 in the lower layer is

∂Ct2 ∂t

= −KL(fd2 ·Ct2 − fd1 ·Ct1)

H2

−ω (f p2 ·Ct2 − f p1 ·Ct1)+W (Ct1 −Ct2)− K2 ·Ct2 +J2 (8.207) where,

K2 is the reaction velocity in Layer 2 (m/day), and J2 is the sum of all internal sources including diagenesis in Layer 2 (g/m2/day).

The substances produced by mineralization of POM in sediments may be present in both dissolved and particulate phases. This distribution directly affects the magnitude of the substance that is returned to the overlying water. In equations 8.205 to 8.207, the distribution of a substance between the dissolved and particulate phases in a sediment is parameterized using a linear partitioning coefficient.

The dissolved and particulate fractions are computed from the partitioning equations:

1 1+m1 ·π1

f p1 = 1− fd1 (8.208)

fd1 =

1 1+m2 ·π2

f p2 = 1− fd2 (8.209) where,

fd2 =

m1 and m2 are the solid concentrations in Layer 1 and 2, respectively (kg/l), and

- π1 and π2 are the partition coefficient in Layer 1 and 2, respectively (per kg/l).


The partition coefficient is the ratio of particulate to dissolved fraction per unit solid concentration (i.e. per unit sorption site available).

All terms, except the last two terms, in equations 8.205 and 8.207 are common to all state variables and are described in Section 5.3.1. The last two terms represent the reaction and source/sink terms, respectively.

###### 209



<<<PAGE 223>>>

###### 8. EUTROPHICATION EFDC+ Theory



##### 8.3.3.2 Common Parameters for Sediment Flux

Parameters that are needed for the sediment fluxes are s, ω, KL, W,H2, m1, m2, π1,

- π2, κ1, κ2, J1,and J2 in equations 8.205 to 8.209. Of these, κ1, κ2, J1 and J2 are variable-specific. Among the other common parameters, W, H2, m1 and m2, are specified as input. The modeling of the remaining three parameters, s, ω, KL, are described in this section.


##### 8.3.3.2.1 Surface Mass Transfer Coefficient

The surface mass transfer coefficient, s can be estimated from the ratio of SOD and overlying water O concentration (Di Toro et al., 1990):

SOD DO0

D1 H1

s =

=

where, D is the diffusion coefficient in Layer 1 (m2/day). It is possible to estimate other model parameters, once s has been calculated.

(8.210)

###### 8.3.3.2.2 Particulate Phase Mixing Coefficient The particle mixing velocity ω between Layer 1 and 2 is parameterized as:

Dp ·θT−20

GPOC,1 GPOC,R

DO0 KMDp +DO0

Dp H2

ω =

(8.211) where,

Dp is the apparent diffusion coefficient for particle mixing (m2/day), θDp is the constant for temperature adjustment for Dp, GPOC,R is the reference concentration for GPOC,1 (g C/m3), and KMDp is the particle mixing half-saturation constant for oxygen (g O2/m3).

The enhanced mixing of sediment particles by macrobenthos (bioturbation) is quantified by estimating Dp. The particle mixing appears to be proportional to the benthic biomass (Matisoff, 1982), which is correlated to theC input to the sediment (Robbins et al., 1989). This is parameterized by assuming that benthic biomass is proportional to the available labileC. GPOC,1, and GPOC,R is the reference concentration at which the particle mixing velocity is at its nominal value. The Monod-type O dependency accounts for the O dependency of benthic biomass.

It has been observed that a hysteresis exists in the relationship between the bottom water O and benthic biomass. Benthic biomass increases as the summer progresses. However, the occurrence of anoxia/hypoxia reduces the biomass drastically and also imposes stress on benthic activities. After full overturn, the bottom water O increases but the population does not recover immediately. Hence, the particle mixing velocity, which is proportional to the benthic biomass, does not increase in response to the increased bottom water

- O. Recovery of benthic biomass following hypoxic events depends on many factors including severity and longevity of hypoxia, constituent species, and salinity (Diaz et al., 1995).


###### 210



<<<PAGE 224>>>

###### 8. EUTROPHICATION EFDC+ Theory



This phenomenon of reduced benthic activities and hysteresis is parameterized based on the idea of stress that low O imposes on the benthic population. It is analogous to the modeling of the toxic effect of chemicals on organisms (Mancini, 1983). A first order differential equation is employed, in which the benthic stress 1) accumulates only when overlying O is below KMDp and 2) is dissipated at a first order rate (Figure 8.8a):

where,

= −KST ·ST + 1− KMDODp0 , if DO0 < KMDp −KST ·ST , if DO0 > KMDp

∂ST ∂t

(8.212)

ST is the accumulated benthic stress (day), and KST is the first order decay rate for ST (1/day).

The behavior of this formulation can be understood by evaluating the steady-state stresses at two extreme conditions of overlying water oxygen, DO0 as:

DO0 = 0, KST ·ST = 1 f(ST) = (1−KST ·ST) = 0 DO0 ≥ KMDp, KST ·ST = 0 f(ST) = (1−KST ·ST) = 1

The dimensionless expression, f(ST) = 1−KST ·ST, appears to be the proper variable to quantify the effect of benthic stress on benthic biomass and thus particle mixing (Figure 8.8b).

The final formulation for the particle mixing velocity including the benthic stress is:

Dp ·θT−20

Dpmin H2

GPOC,1 GPOC,R

DO0 KMDp +DO0

Dp H2

ω =

f (ST)+

where Dpmin is the minimum diffusion coefficient for particle mixing (m2/day).

(8.213)

The reduction in particle mixing due to the benthic stress, f(ST) is estimated by employing the following procedure. The stress, ST is normally calculated using equation 8.212. Once DO0 drops below a critical concentration DOST,c, for NChypoxia consecutive days or more, the calculated stress is not allowed to decrease until tMBS days of DO0 > DOST,c. That is, only when hypoxic days are longer than critical hypoxia days (NChypoxia), the maximum stress, or minimum (1−KST ·ST), is retained for a specified period (tMBS days) after DO0 recovery (Figure 8.8). No hysteresis occurs if DO0 does not drop below DOST,c or if hypoxia lasts less than NChypoxia days. When applying maximum stress for tMBS days, the subsequent hypoxic days are not included in tMBS. This parameterization of hysteresis essentially assumes seasonal hypoxia, i.e., one or two major hypoxic events during summer, and might be unsuitable for systems with multiple hypoxic events throughout the year.

###### 211



<<<PAGE 225>>>

###### 8. EUTROPHICATION EFDC+ Theory



Fig. 8.8. Benthic stress (a) and its effect on particle mixing (b) as a function of overlying water column DO concentration.

Three parameters relating to hysteresis DOST,c, NChypoxia, and tMBS are functions of many factors including severity and longevity of hypoxia, constituent species and salinity, and thus have site-specific variabilities (Diaz et al., 1995). The critical overlying DO concentration DOST,c, also depends on the distance from the bottom of the location of DO0. The critical hypoxia days NChypoxia, depends on tolerance of benthic organisms to hypoxia and thus on benthic community structure (Diaz et al., 1995). The time lag for the recovery of benthic biomass following hypoxic events, tMBS tends to be longer for higher salinity. The above three parameters are considered to be spatially constant input parameters.

##### 8.3.3.2.3 Dissolved Phase Mixing Coefficient

Dissolved phase mixing between Layer 1 and 2 is via passive molecular diffusion, which is enhanced by the mixing activities of the benthic organisms (bio-irrigation). This is modeled by increasing the diffusion coefficient relative to the molecular diffusion coefficient:

###### 212



<<<PAGE 226>>>

###### 8. EUTROPHICATION EFDC+ Theory



Dd ·θT−20

Dd H2

+RBI,BT ·ω (8.214) where,

KL =

Dd is the diffusion coefficient in pore water (m2/day), θDd is the constant for temperature adjustment for Dd, and RBI,BT is the ratio of bio-irrigation to bioturbation.

The last term in equation 8.214 accounts for the enhanced mixing by organism activities.

##### 8.3.3.3 Ammonia Nitrogen

Diagenesis is assumed not to occur in the upper layer because of its shallow depth, and NH4+ is produced by diagenesis in the lower layer:

J1,NH4 = 0 J2,NH4 = JN (8.215)

where JN is from equation 8.204. NH4+ is nitrified to NO−

3 in the presence of O. A Monod-type expression is used for the NH4+ and O

dependency of the nitrification rate. Then, the oxic layer reaction velocity in equation 8.205 for NH4+ may be expressed as:

DO0 2·KMNH4,O2 +DO0

KMNH4 KMNH4 +NH41

K12,NH4 =

KNH2 4 ·θT−20

NH4 (8.216) and then the nitrification flux becomes:

K12,NH4

JNit =

s ·NH41 (8.217) where,

KMNH4,O2 is the nitrification half-saturation constant for DO (g O2/m3), NH41 is the total NH4+ concentration as N in Layer 1 (g N/m3), KMNH4 is the nitrification half-saturation constant for NH4+ (g N/m3), KNH4 is the optimal reaction velocity for nitrification at 20◦C (m/day), θNH4 is the constant for temperature adjustment for KNH4, and JNit is the nitrification flux (g N/m2/day).

Nitrification does not occur in the anoxic lower layer:

K2,NH4 = 0 (8.218)

###### 213



<<<PAGE 227>>>

###### 8. EUTROPHICATION EFDC+ Theory



Once equations 8.205 and 8.207 are solved for NH41 and NH42, the sediment flux of NH4+ to the overlying water Jaq,NH4, can be calculated using equation 8.206. Note that it is not NH41 and NH42 that determine the magnitude of Jaq,NH4 (DiToro and Fitzpatrick (1993, Section X-B-2)), but the magnitude is determined by (1) the diagenesis flux, (2) the fraction that is nitrified, and (3) the surface mass transfer coefficient (s) that mixes the remaining portion.

##### 8.3.3.4 Nitrate Nitrogen

Nitrification flux is the only source of NO−

3 in the upper layer, given by Equation 8.217, and there is no diagenetic source for NO−

3 in both layers:

- J1,NO3 = JNit
- J2,NO3 = 0


(8.219)

3 is present in sediments as a dissolved substance, i.e., π1,NO3 = π2,NO3 = 0, making fd1,NO3 = fd2,NO3 = 1 (Equations 8.208 and 8.209): it also makes R meaningless, hence R = 0. NO−

NO−

3 is removed by denitrification in both oxic and anoxic layers with the C required for denitrification supplied by C diagenesis. The reaction velocities in equations 8.205 and 8.207 for NO−

3 may be expressed as:

K12,NO3 = KNO2 3,1 ·θT−20

NO3 (8.220)

K2,NO3 = KNO2 3,2 ·θT−20

NO3 (8.221) and the denitrification flux out of sediments as a N gas becomes:

K12,NO3 s

NO31 +K2,NO3 ·NO32 (8.222) where,

JN2(g) =

- KNO3,1 is the reaction velocity for denitrification in Layer 1 at 20◦C (m/day),
- KNO3,2 is the reaction velocity for denitrification in Layer 2 at 20◦C (m/day), θNO3 is the constant for temperature adjustment for KNO3,1 and KNO3,2, JN2(g) is the denitrification flux (g N/m2/day),


- NO31 is the total NO−

3 concentration as N in Layer 1 (g N/m3), and

- NO32 is the total NO−


3 concentration as N in Layer 2 (g N/m3). Once equations 8.205 and 8.207 are solved for NO31 and NO32, the sediment flux of NO−

3 to the overlying water Jaq,NO3, can be calculated using equation 8.206. The steady-state solution for NO−

3 showed that the NO−

3 flux is a linear function of NO30 (DiToro and Fitzpatrick, 1993, equation III-15); the intercept

quantifies the amount of NH4+ in the sediment that is nitrified but not denitrified (thus releases as Jaq,NO3), and the slope quantifies the extent to which overlying water NO−

3 is denitrified in the sediment. It also revealed that if the internal production of NO−

3 is small relative to the flux of NO−

3 from the overlying water,

###### 214



<<<PAGE 228>>>

###### 8. EUTROPHICATION EFDC+ Theory



the normalized NO−

3 flux to the sediment −Jaq,NO3/NO30, is linear in s for small s and constant for large s (DiToro and Fitzpatrick, 1993, Section III-C ). For small s (∼ 0.01m/day), H is large (equation 8.210) so that oxic layer denitrification predominates and Jaq,NO3 is essentially zero independent of NO30 (DiToro and Fitzpatrick, 1993, Figure III-4).

- 8.3.3.5 Phosphate Phosphorus Phosphate is produced by the diagenetic breakdown of POP in the lower layer:

- J1,PO4 = 0
- J2,PO4 = JP


(8.223)

where JP is the diagenesis flux of phosphorus obtained from equation 8.204. A portion of the liberated PO−3

4 remains in the dissolved form and a portion becomes particulate PO−3

4 , either via precipitation of PO−3

4 containing minerals (Troup, 1974) (e.g. vivianite, Fe3(PO4)2(s)), or by partitioning to PO−3

4 sorption sites (Barrow, 1983; Giordani and Astorri, 1986; Lijklema, 1980). The extent of particulate formation is determined by the magnitude of the partition coefficients π1,PO4 and π2,PO4 in equations 8.208 and 8.209. PO−3

4 flux is strongly affected by DO0, the overlying water DO concentration. As DO0 approaches zero, the PO−3

4 flux from the sediments increases. This mechanism is incorporated by making π1,PO4 larger, under oxic conditions, than π2,PO4. In the model, when DO0 exceeds a critical concentration (DO0)crit,PO4, sorption in the upper layer is enhanced by an amount ∆πPO4,1:

π1,PO4 = π2,PO4 ·(∆πPO4,1) DO0 > (DO0)crit,PO4 (8.224) When DO falls below (DO0)crit,PO4, then:

π1,PO4 = π2,PO4 ·(∆πPO4,1)

DO0

(DO0)crit,PO4 DO0 ≤ (DO0)crit,PO4 (8.225) which smoothly reduces π1,PO4 to π2,PO4 as DO0 goes to zero. There is no removal reaction for PO−3

4 in both layers:

κ1,PO4 = κ2,PO4 = 0 (8.226) Once equations 8.205 and 8.207 are solved for PO41 and PO42, the sediment flux of PO−3

4 to the overlying water Jaq,PO4, can be calculated using equation 8.206.

- 8.3.3.6 Sulfide/Methane and Oxygen Demand


##### 8.3.3.6.1 Sulfide

No diagenetic production of S−

2 occurs in the upper layer. In the lower layer, S−

2 is produced by carbon diagenesis (equation 8.204) and is decremented by the OC consumed due to denitrification (equation 8.222). Then:

###### 215



<<<PAGE 229>>>

###### 8. EUTROPHICATION EFDC+ Theory



where,

- J1,H2S = 0
- J2,H2S = aO2,C ·JC −aO2,NO3 ·JN2(g)


(8.227)

aO2,C is the stoichiometric coefficient for carbon diagenesis consumed by S−

2 oxidation (2.6667g O2 − equivalents per g C), and

aO2,NO3 is the stoichiometric coefficient for carbon diagenesis consumed by denitrification (2.8571g O2 −equivalents per g N).

A portion of the dissolved S−

2 that is produced in the anoxic layer reacts with the Fe to form particulate Iron monosulfide (FeS) (Morse et al., 1987). The particulate fraction is mixed into the oxic layer where it can be oxidized to Fe2O3(s) (ferric oxide). The remaining dissolved fraction also diffuses into the oxic layer where it is oxidized to SO−2

4 . Partitioning between dissolved and particulate S−

2 in the model represents the formation of FeS(s), which is parameterized using partition coefficients π1,H2S and π2,H2S, in equations 8.208 and 8.209.

EFDC+ has three pathways for S−

2 , the reduced end product of C diagenesis: (1) S−

2 oxidation, (2) aqueous S−

2 flux, and (3) burial. The distribution of S−

2 among the three pathways is controlled by the partitioning coefficients and the oxidation reaction velocities (Section V-E in DiToro and Fitzpatrick (1993)). Both dissolved and particulate S−

2 are oxidized in the oxic layer, consuming O in the process. In the oxic upper layer, the oxidation rate that is linear in O concentration is used (Boudreau, 1991; Cline and Richards, 1969; Millero, 1986). In the anoxic lower layer, no oxidation can occur. Then, the reaction velocities in equations 8.205 and 8.207 may be expressed as:

DO0 2·KMH2S,O2

K12,H2S = KH22S,d1 · fd1,H2S +KH22S,p1 · f p1,H2S θT−20

H2S

(8.228)

K22,H2S = 0 (8.229) where,

KH2S,d1 is the reaction velocity for dissolved S−

2 oxidation in Layer 1 at 20◦C (m/day), KH2S,p1 is the reaction velocity for particulate S−

2 oxidation in Layer 1 at 20◦C (m/day), θH2S is the constant for temperature adjustment for KH2S,d1 and KH2S,p1, and KMH2S,O2 is the constant to normalize the S−

2 oxidation rate for O (g O2/m3).

The constant KMH2S,O2, which is included for convenience only, is used to scale the O concentration in the overlying water. At DO0 = KMH2S,O2, the reaction velocity for S−

2 oxidation rate is at its nominal value.

The oxidation reactions in the oxic upper layer cause O flux to the sediment, which exerts SOD. By convention, SOD is positive: SOD = −Jaq,O2. The SOD in the model consists of two components, Carbonaceous Sediment Oxygen Demand (CSOD) due to S−

2 oxidation and Nitrogenous Sediment Oxygen Demand (NSOD) due to nitrification:

###### 216



<<<PAGE 230>>>

###### 8. EUTROPHICATION EFDC+ Theory



K12,H2S s

H2S1 +aO2,NH4 ·JNit (8.230) where,

SOD = CSOD+NSOD =

2 concentration in Layer 1 (g O2 −equivalents/m2/day), and aO2,NH4 is the stoichiometric coefficient for O consumed by nitrification (4.33 g O2 per g N).

H2S1 is the total S−

Equation 8.230 is nonlinear for SOD because the RHS contains s (= SOD/DO0) so that SOD appears on both sides of the equation: note that JNit (equation 8.217) is also a function of s. A simple back substitution method is used to solve this equation.

If the overlying water DO is low, then the S−

2 that is not completely oxidized in the upper layer can diffuse into the overlying water. This aqueous S−

2 flux out of the sediments, which contributes to the COD in the water column model, is modeled using

Jaq,H2S = s(fd1,H2S ·H2S1 −COD) (8.231) The S−

2 released from the sediment reacts very quickly in the water column when O is available, but can accumulate in the water column under anoxic conditions. The COD, quantified as O equivalents, is entirely supplied by benthic release in the water column model (equation 8.92). Since S−

2 also is quantified as O equivalents, COD is used as a measure of S−

2 in the water column in equation 8.231.

##### 8.3.3.6.2 Methane

When SO−2

4 is used up, CH4 can be produced by carbon diagenesis and CH4 oxidation consumes O (Di Toro et al., 1990). Owing to the abundant SO−2

4 in the saltwater, only the aforementioned S−

2 production and oxidation are considered to occur in the saltwater. Since the SO−2

4 concentration in the freshwater is generally insignificant, CH4 production is considered to replace S−

2 production in the freshwater. In the freshwater, CH4 is produced by carbon diagenesis in the lower layer and is decremented by the OC consumed due to denitrification. No diagenetic production of CH4 occurs in the upper layer (equation 8.227):

- J1,CH4 = 0
- J2,CH4 = aO2,C ·JC −aO2,NO3 ·JN2(g)


(8.232)

The dissolved CH4 produced takes two pathways; (1) oxidation in the oxic upper layer causing CSOD, or

(2) escape from the sediment as aqueous flux or as gas flux:

J2,CH4 = CSOD+Jaq,CH4 +JCH4(g) (8.233) where,

Jaq,CH4 is the aqueous CH4 flux (g O2 −equivalents/m2/day), and JCH4(g) is the gaseous CH4 flux (g O2 −equivalents/m2/day).

###### 217



<<<PAGE 231>>>

###### 8. EUTROPHICATION EFDC+ Theory



A portion of dissolved CH4 that is produced in the anoxic layer diffuses into the oxic layer where it is oxidized. This CH4 oxidation causes CSOD in the freshwater sediment (Di Toro et al., 1990) :

CSOD = CSODmax · 1−sech

KCH4 ·θT−20

CH4

s

(8.234)

where,

CSODmax = minimum 2·KL·CH4sat ·J2,CH4, J2,CH4 (8.235)

h+H2 10

CH4sat = 100 1+

1.02420−T (8.236)

CSODmax is the maximum CSOD occurring when all the dissolved CH4 transported to the oxic layer is

oxidized, KCH4 is the reaction velocity for dissolved CH4 oxidation in Layer 1 at 20◦C (m/day), θH2S is the constant for temperature adjustment for KCH4 , and CH4sat is the saturation concentration of CH4 in the pore water (g O2 −equivalents/m3).

The term, (h+H2)/10 where h and H2 are in meters, in equation 8.236 is the depth from the water surface that corrects for the in situ pressure. Equation 8.236 is accurate to within 3% of the reported CH4 solubility between 5 and 20◦C (Yamamoto et al., 1976).

If the overlying water O is low, the CH4 that is not completely oxidized can escape the sediment into the overlying water either as aqueous flux or as gas flux. The aqueous CH4 flux, which contributes to the COD in the water column model, is modeled using (Di Toro et al., 1990):

Jaq,CH4 = CSODmax ·sech

KCH4 ·θT−20

CH4

s

= CSODmax −CSOD (8.237)

CH4 is only slightly soluble in water. If its solubility CH4sat given by equation 8.236 is exceeded in the pore water, it forms a gas phase that escapes as bubbles. The loss of CH4 as bubbles, i.e. the gaseous CH4 flux, is modeled using equation 8.233 with J2,CH4 from equation 8.232, CSOD from equation 8.234 and Jaq,CH4 from equation 8.237 (Di Toro et al., 1990).

##### 8.3.4 Silica

3 and PO−3

The production of NH4+, NO−

4 in sediments is the result of the mineralization of POM by bacteria. The production of dissolved SiO2 in sediments is the result of the dissolution of SiP or opaline SiO2, which is thought to be independent of bacterial processes. The depositional flux of SiP from the overlying water to the sediments is modeled using equation 8.202. With this source, the mass-balance equation for SiP may be written as:

∂PSi ∂t

= −SSi ·H2 −W ·PSi+JPSi +JDSi (8.238)

H2

###### 218



<<<PAGE 232>>>

###### 8. EUTROPHICATION EFDC+ Theory



where,

Psi is the concentration of SiP in the sediment (g Si/m3), SSi is the dissolution rate of PSi in Layer 2 (g Si/m3/day), JPsi is the depositional flux of PSi (g Si/m3/day) given by the equation 8.202, and JDSi is the detrital flux of PSi (g Si/m3/day) to account for PSi settling to the sediment that is not

associated with the algal flux of biogenic silica.

The processes included in equation 8.238 are dissolution (i.e., production of dissolved silica), burial, and depositional and detrital fluxes from the overlying water. Equation 8.238 can be viewed as the analog of the diagenesis equations for POM (equation 8.203). The dissolution rate is formulated using a reversible reaction that is first order in SiO2 solubility deficit and follows a Monod-type relationship in SiP:

PSi PSi+KHPSi

SSi = KSi ·θT−20

(Sisat − fd2,Si ·Si2) (8.239) where,

Si

KSi is the first order dissolution rate for SiP at 20◦C in Layer 2 (1/day), θSi is the constant for temperature adjustment for KSi, KMPSi is the SiO2 dissolution half-saturation constant for PSi (g Si/m3), and Sisat is the saturation concentration of SiO2 in the pore water (g Si/m3).

The mass-balance equations for mineralized SiO2 can be formulated using the general forms, equations 8.205 and 8.207. There is no source/sink term and no reaction in the upper layer:

J1,Si = κ1,Si = 0 (8.240)

In the lower layer, SiO2 is produced by the dissolution of SiP, which is modeled using equation 8.239. The two terms in equation 8.239 correspond to the source term and reaction term in equation 8.207:

PSi PSi+KMPSi

J2,Si = KSi ·θT−20

Sisat ·H2 (8.241)

Si

PSi PSi+KMPSi

κ2,Si = KSi ·θT−20

fd2,Si ·H2 (8.242)

Si

A portion of SiO2 dissolved from particulate SiO2 sorbs to solids and a portion remains in the dissolved form. Partitioning using the partition coefficients π1,Si and π2,Si, in Equations 8.208 and 8.209 controls the extent to which dissolved SiO2 sorbs to solids. Since SiO2 shows similar behavior as PO−3

4 in the adsorptiondesorption process, the same partitioning method as applied to PO−3

4 is used for SiO2. That is, when DO0 exceeds a critical concentration (DO0)crit,Si, sorption in the upper layer is enhanced by an amount ∆πSi,1:

π1,Si = π2,Si ·(∆πSi,1) DO0 > (DO0)crit,Si (8.243)

When O falls below (DO0)crit,Si, then:

###### 219



<<<PAGE 233>>>

###### 8. EUTROPHICATION EFDC+ Theory



DO0

π1,Si = π2,Si ·(∆πSi,1)

(DO0)crit,Si DO0 ≤ (DO0)crit,Si (8.244) which smoothly reduces π1,Si to π2,Si as DO0 goes to zero. Once equations 8.205 and 8.207 are solved for Si1 and Si2, the sediment flux of SiO2 to the overlying water Jaq,Si, can be calculated using equation 8.206.

##### 8.3.5 Sediment Temperature

All rate coefficients in the aforementioned mass-balance equations are expressed as a function of sediment temperature, T. The sediment temperature is modeled based on the diffusion of heat between the water column and sediment:

∂T ∂t

DT H2

(TW −T) (8.245) where,

=

DT is the heat diffusion coefficient between the water column and sediment (m2/s), and TW is the temperature in the overlying water column (◦C) calculated by equation 8.121.

The model application in (Di Toro and Fitzpatrick, 1993) and (Cerco and Cole, 1994) used DT = 1.8×10−7 m2/s.

##### 8.3.6 Method of Solution

##### 8.3.6.1 Finite-Difference Equations and Solution Scheme

An implicit integration scheme is used to solve the governing mass-balance equations for ammonium, nitrate, phosphate or sulfide/methane in the upper and lower layer. The finite difference form of equation 8.205 may be expressed as:

0 = s fd0 ·Cto′ − fd1 ·Ct1′ +KL fd2 ·Ct2′ − fd1 ·Ct1′

K12 s

+ω f p2 ·Ct2′ − f p1 ·Ct1′ −W ·Ct1′ −

Ct1′ +J1′ (8.246)

where the primed variables designate the values evaluated at t+ and the unprimed variables are those at t, where θ is defined in equation 8.121.

The finite difference form of equation 8.207 may be expressed as:

0 = −KL fd2 ·Ct2′ − fd1 ·Ct1′ −ω f p2 ·Ct2′ − f p1 ·Ct1′

H2 θ

+W Ct1′ −Ct2′ − K2 +

Ct2′ + J2′ +

H2 θ

Ct2 (8.247)

###### 220



<<<PAGE 234>>>

###### 8. EUTROPHICATION EFDC+ Theory



The two terms −(H2/θ)Ct2′ and (H2/θ)Ct2, are from the derivative term H2(∂Ct2/∂t) in equation 8.207. Each of these terms simply add to the Layer 2 removal rate and the forcing function, respectively. Setting

these two terms equal to zero results in the steady-state model. The two unknowns Ct1′ and Ct2′ , can be calculated at every time step using:

2 1

s· fd1 +a1 + K

s −a2

−a1 a2 +W +K2 + Hθ2

- Ct1′
- Ct2′


=

- J1′ +s· fd0 ·Ct0′
- J2′ + Hθ2Ct2


(8.248)

a1 = KL· fd1 +ω · f p1 +W a2 = KL· fd2 +ω · f p2

(8.249)

The solution of equation 8.248 requires an iterative method since the surface mass transfer coefficient, s is a function of the SOD (equation 8.210), which is also a function of s (equation 8.230). A simple back substitution method is used:

- 1. Start with an initial estimate of SOD, for example, SOD = aO2,CJC or the previous time step SOD.
- 2. Solve equation 8.248 for NH4+, NO−

3 , and S−

2 /CH4.

- 3. Compute the SOD using equation 8.230.
- 4. Refine the estimate of SOD: a root finding method (Brent’s method in Press et al. (1986)) is used to make the new estimate.
- 5. Go to (2) if no convergence.
- 6. Solve equation 8.248 for PO−3


4 and SiO2.

For the sake of symmetry, the equations for diagenesis, SiP and sediment temperature are also solved in implicit form. The finite difference form of the diagenesis equation (equation 8.203) may be expressed as:

G′POM,i = GPOM,i +

θ H2

θ H2

JPOM,i 1+θ ·KPOM,i ·θT−20

W

POM,i +

−1

The finite difference form of the SiP equation (equation 8.238) may be expressed as:

(8.250)

PSi′ = PSi+

θ H2

θ H2

Sisat − fd2,Si ·Si2 PSi+KMPSi

(JPSi +JDSi) 1+θ ·KSi ·θT−20

W

+

Si

−1

(8.251)

using equation 8.233 for the dissolution term, in which PSi in the Monod-type term has been kept at time level t to simplify the solution. The finite difference form of the sediment temperature, shown in equation

- 8.245, may be expressed as:


T′ = T +

θ H2

θ H2

DT ·TW 1+

DT

−1

(8.252)

###### 221



<<<PAGE 235>>>

###### 8. EUTROPHICATION EFDC+ Theory



##### 8.3.6.2 Boundary and Initial Conditions

The above finite difference equations constitute an initial boundary-value problem. The boundary conditions are the depositional fluxes (JPOM,i and JPSi) and the overlying water conditions (Ct0 and TW) as a function of time, which are provided from the water column water quality model. The initial conditions are the concentrations at t = 0, GPOM,i(0), PSi(0), Ct1(0), Ct2(0) and T(0), to start the computations. Strictly speaking, these initial conditions should reflect the past history of the overlying water conditions and depositional fluxes, which is often impractical because of lack of field data for these earlier years.

##### 8.4. Appendix

The appendix includes values of some parameters based on literature review and professional experiences. Parameters of three legacy algae groups cyanobacteria (C), diatoms (D), and green algae (G) are presented in Table 8.16. These values may be used as a starting point for the model calibration process.

Table 8.16. Parameters Related to Algae in Water Column

Parameter Valuea Equation Numberb ∗PMc (1/day) 2.5 (upper Potomac only) 8.7 ∗PMd (1/day) 2.25 8.7 ∗PMg (1/day) 2.5 8.7 KHNx (g N/m3) 0.01 (all groups) 8.8 KHPx (g P/m3) 0.001 (all groups) 8.8 KHS (g Si/m3) 0.05 8.8 FD Temporally-varying input 8.9 Isx (langleys/day) Temporally-varying input 8.10 ∗Keb (1/m) spatially-varying input 8.134 KeISS (1/m per m3) NAc 8.134 KeChl (1/m per mg Chl/m3) 0.017 8.134 CChlx (g C per mg Chl) 0.06 (all groups) 8.134 (Dopt)x (m) 1.0 (all groups) 8.12 (Is)min (langleys/day) 40.0 8.12 CIa, CIb and CIc 0.7, 0.2 & 0.1 8.13 TMc, TMd and TMg (oC) 27.5, 20.0 & 25.0 8.14 KTG1c and KTG2c (oC−2) 0.005 & 0.004 8.14 KTG1d and KTG2d (oC−2) 0.004 & 0.006 8.14 KTG1g and KTG2g (oC−2) 0.008 & 0.01 8.14 STOX (ppt) 1.0 8.15 ∗BMRc (1/day) 0.04 8.16 ∗BMRd (1/day) 0.01 (0.03 during Jan.-May in saltwater only) 8.16 ∗BMRg (1/day) 0.01 8.16 TRx, (oC) 20.0 (all groups) 8.16 KTBx (oC−1) 0.069 (all groups) 8.16

Continued on next page

222



<<<PAGE 236>>>

###### 8. EUTROPHICATION EFDC+ Theory

Table 8.16 – continued from previous page



Parameter Valuea Equation Numberb ∗PRRc (1/day) 0.01 8.17 ∗PRRd (1/day) 0.215 (0.065 during Jan-May in saltwater only) 8.17 ∗PRRg (1/day) 0.215 8.17 ∗WSc (m/day) 0.0 8.6 ∗WSd (m/day) 0.35 (Jan-May), 0.1 (Jun-Dec) 8.6 ∗WSg (m/day) 0.1 8.6

a The evaluation of these values is detailed in Chapter IX of (Cerco and Cole, 1994). b The equation number where the corresponding parameter is first shown and defined. c Not available in (Cerco and Cole, 1994) since their formulations do not include these parameters.

* The parameters are declared as an array in the source code.

Table 8.17. Parameters Related to Zooplankton in Water Column

Parameter Valuea Equation Numberb ANCz (gN g−1C) 0.2 8.7 APCz (gP g−1C) 0.02 8.8 BMRz (1/day) 0.254 8.8 CTz (mgC/l) 0.01 8.8 DOCRITz (mgDO/l) 2 8.9 FCRDZz 0 ≤ FCRDZz ≤ 1 8.10 FCRPZz 0 ≤ FCRPZz ≤ 1 8.10 FCLDZz 0 ≤ FCLDZz ≤ 1 8.10 FCLPZz 0 ≤ FCLPZz ≤ 1 8.10 FCDDZz 0 ≤ FCDDZz ≤ 1 8.10 FCDPZz 0 ≤ FCDPZz ≤ 1 8.10 FPRDZz 0 ≤ FPRDZz ≤ 1 8.10 FPRPZz 0 ≤ FPRPZz ≤ 1 8.10 FPLDZz 0 ≤ FPLDZz ≤ 1 8.10 FPLPZz 0 ≤ FPLPZz ≤ 1 8.10 FPDBZz 0 ≤ FPDBZz ≤ 1 8.10 FPDPZz 0 ≤ FPDDZz ≤ 1 8.10 FPDPZz 0 ≤ FPDPZz ≤ 1 8.10 FPIBZz 0 ≤ FPIBZz ≤ 1 8.10 FPIPZz 0 ≤ FPIDZz ≤ 1 8.10 FPIPZz 0 ≤ FPIPZz ≤ 1 8.10 FNRDZz 0 ≤ FNRDZz ≤ 1 8.10 FNRPZz 0 ≤ FNRPZz ≤ 1 8.10 FNLDZz 0 ≤ FNLDZz ≤ 1 8.10 FNLPZz 0 ≤ FNLPZz ≤ 1 8.10

Continued on next page

223



<<<PAGE 237>>>

###### 8. EUTROPHICATION EFDC+ Theory

Table 8.17 – continued from previous page



FNDBZz 0 ≤ FNDBZz ≤ 1 8.10 FNDPZz 0 ≤ FNDDZz ≤ 1 8.10 FNDPZz 0 ≤ FNDPZz ≤ 1 8.10 FNIBZz 0 ≤ FNIBZz ≤ 1 8.10 FNIDZz 0 ≤ FNIDZz ≤ 1 8.10 FNIPZz 0 ≤ FNIPZz ≤ 1 8.10 FSPDZz 0 ≤ FSPDZz ≤ 1 8.10 FSPPZz 0 ≤ FSPPZz ≤ 1 8.10 FSADZz 0 ≤ FSADZz ≤ 1 8.10 FSAPZz 0 ≤ FSAPZz ≤ 1 8.10 KHCz, (mgC/l) 0.05 8.16 KTBz (oC−1) 0.069 8.16 KTg1 (oC−2) 0.0035 8.16 KTg2 (oC−2) 0.025 8.16 DZEROz (1/day) 4.0 8.17 RMAXz (g preyCg−1zooplCd−1) 2.25 8.6 Topt1 (oC) 25 8.6 Topt2 (oC) 25 8.6 TRz (oC) 20 8.6 UBzs (oC) 0 ≤ UBzs ≤ 1 8.6 ULz (oC) 0 ≤ ULz ≤ 1 8.6 URz (oC) 0 ≤ URz ≤ 1 8.6

- a The evaluation of these values is detailed in Chapter VIII of (Cerco and Cole, 2004).
- b The equation number where the corresponding parameter is first shown and defined.


###### 224



<<<PAGE 238>>>

###### 8. EUTROPHICATION EFDC+ Theory



Table 8.18. Parameters Related to Organic Carbon (OC) in Water Column

Parameter Valuea Equation Numberb FCRPx 0.35 (all groups) 8.41 FCLPx 0.55 (all groups) 8.42 FCDPx 0.10 (all groups) 8.44 FCDx 0.0 (all groups) 8.44 ∗WSRP (m/day) 1.0 8.41 ∗WSLP (m/day) 1.0 8.42 KHRx (g O2/m3) 0.5 (all groups) 8.44 KHORDO (g O2/m3) 0.5 8.52 KRC (1/day) 0.005 8.53 KLC (1/day) 0.075 8.54 KDC (1/day) 0.01 8.55 KRCalg (1/day per g C/m3) 0.0 8.53 KLCalg (1/day per g C/m3) 0.0 8.54 KDCalg (1/day per g C/m3) 0.0 8.55 TRHDR (OC) 20.0 8.53 TRMIN (OC) 20.0 8.55 KTHDR (OC−1) 0.069 8.53 KTMIN (OC−1) 0.069 8.55 KHDNN (g N/m3) 0.1 8.57 AANOX 0.5 8.57 a The evaluation of these values is detailed in Chapter IX of (Cerco and Cole, 1994). b The equation number where the corresponding parameter is first shown and defined.

* The parameters are declared as an array in the source code.

###### 225



<<<PAGE 239>>>

###### 8. EUTROPHICATION EFDC+ Theory



Table 8.19. Parameters Related to Phosphorus (P) in Water Column

Parameter Valuea Equation Numberb FPLPx 0.2 (all groups) 8.59 FPDPx 0.5 (all groups) 8.60 FPIPx 0.2 (all groups) 8.61 FPRx 0.0 (all groups) 8.58 FPLx 0.0 (all groups) 8.59 FPDx 1.0 (all groups) 8.60 FPIx 0.0 (all groups) 8.61 ∗WSs (m/day) 1.0 8.61 KPO4p (per g/m3) for TSS NA 8.62 KPO4p (per mol/m3) for TAM 6.0 8.62 CPprm1 (g C per g P) 42.0 8.65 CPprm2 (g C per g P) 85.0 8.65 CPprm3 (per g P/m3) 200.0 8.65 KRP (1/day) 0.005 8.66 KLP (1/day) 0.075 8.67 KDP (1/day) 0.1 8.68 KRPalg (1/day per g C/m3) 0.0 8.66 KLPalg (1/day per g C/m3) 0.0 8.67 KDPalg (1/day per g C/m3) 0.2 8.68

- a The evaluation of these values are detailed in Chapter IX of (Cerco and Cole, 1994).
- b The equation number where the corresponding parameter is first shown and defined.
- c Not available in (Cerco and Cole, 1994) since their formulations do not include these parameters.


: FPIx is estimated from FPRx +FPLx +FPDx +FPIx = 1.

* The parameters declared as an array in the source code.

###### 226



<<<PAGE 240>>>

###### 8. EUTROPHICATION EFDC+ Theory



Table 8.20. Parameters Related to Nitrogen (N) in Water Column

Parameter Valuea Equation Numberb FNLPx 0.55 (all groups) 8.71 FNDPx 0.1 (all groups) 8.72 FNIPx 0.0 (all groups) 8.73 FNRx 0.0 (all groups) 8.70 FNLx 0.0 (all groups) 8.71 FNDx 1.0 (all groups) 8.72 FNIx 0.0 (all groups) 8.73 ANCx (g; N; per g C) 0.167 (all groups) 8.70 ANDC (g; N; per g C) 0.933 8.74 KRN (1/day) 0.005 8.76 KLN (1/day) 0.075 8.77 KDN (1/day) 0.015 8.78 KRNalg (1/day per g C/m3) 0.0 8.76 KLNalg (1/day per g C/m3) 0.0 8.77 KDNalg (1/day per g C/m3) 0.2 8.78 Nitm (g N/m3/day) 0.07 8.81 KHNitDO (g N/m3) 1.0 8.81 KHNitN (g O2/m3) 1.0 8.81 TNit (oC) 27.0 8.82 KNit (oC−2) 0.0045 8.82 KNit (oC−2) 0.0045 8.82 a The evaluation of these values are detailed in Chapter IX of (Cerco and Cole, 1994).

b The equation number where the corresponding parameter is first shown and defined.

###### 227



<<<PAGE 241>>>

###### 8. EUTROPHICATION EFDC+ Theory



Table 8.21. Parameters Related to Silica (SiO2) in Water Column

Parameter Valuea Equation Numberb FSPPd 1.0 8.85 FSIPd 0.0 8.86 FSPd 1.0 8.85 FSId 0.0 8.86 ASCd (g Si per g C) 0.5 8.85 KSAp (per g/m3) for TSS NA 8.87 KSAp (per mol/m3) for TAM 6.0 8.87 KSU (1/day) 0.03 8.91 TRSUA (oC) 20.0 8.91 KTSUA (oC−1) 0.092 8.91

- a The evaluation of these values are detailed in Chapter IX of (Cerco and Cole, 1994).
- b The equation number where the corresponding parameter is first shown and defined.
- c Not available in (Cerco and Cole, 1994) since their formulations do not include these parameters. : FSPPd and FSIPd are estimated from FSPPd +FSIPd = 1. : FSPd and FSId are estimated from FSPd +FSId = 1.


- Table 8.22. Parameters Related to Carbonaceous Oxygen Demand (COD) and Dissolved Oxygen (DO) in Water Column


Parameter Valuea Equation Numberb KHCOD (g O2/m3) 1.5 8.92 KCD (1/day) 20.0 8.93 TRCOD (oC) 20.0 8.93 KTCOD (oC−1) 0.041 8.93 AOCR (g O2 per g C) 2.67 8.94 AONT (g O2 per g N) 4.33 8.93 KR (in MKS unit) 3.933 8.94 KTr 1.024 (1.005-1.030) 8.109

- a The evaluation of these values are detailed in Chapter IX of Cerco and Cole

(1994).

- b The equation number where the corresponding parameter is first shown and defined.
- c Not available in (Cerco and Cole, 1994) since their formulations do not include these parameters. : Kro is from O’Connor & Dobbins O’Connor and Dobbins (1958). : KTr is from Thomann & Mueller Thomann and Mueller (1987).


###### 228



<<<PAGE 242>>>

###### 8. EUTROPHICATION EFDC+ Theory



- Table 8.23. Parameters Related to Total Active Metals (TAM) and Fecal Coliform Bacteria in Water Column

Parameter Valuea Equation Numberb KHbmf (g O2/m3) 0.5 8.112 BFTAM (mol/m2/day) 0.01 8.112 Ttam (oC) 20.0 8.112 Ktam (oC−1) 0.2 8.112 TAMdmx (mol/m3) 0.015 8.113 Kdotam (per g O2/m3) 1.0 8.113 KFCB (1/day) 0.0 - 6.1 (seawater) 8.115 TFCB (oC−1) 1.07 8.115 a The evaluation of these values is detailed in Chapter IX of Cerco and Cole (1994). b The equation number where the corresponding parameter is first shown and defined. c Not available in Cerco and Cole (1994) since their formulations do not include these parameters. : KFCB and TFCB are from Thomann and Mueller (1987).

- Table 8.24. Assignment of Water Column Particulate Organic Matter (POM) to Sediment G Classes used in (Cerco and Cole, 1994)


WCM Variable Carbon & Phosphorus Nitrogen G1 G2 G3 G1 G2 G3

- A. “stand alone” model 0.65 0.20 0.15 0.65 0.25 0.10
- B. coupled model Labile Particulate 1.0 0.0 0.0 1.0 0.0 0.0 Refractory Particulatea : Bay and Tributary Zones 1 0.0 0.11 0.89 0.0 0.26 0.74 : Bay Zones 2 and 10 0.0 0.43 0.57 0.0 0.54 0.46 : All Other Zones 0.0 0.73 0.27 0.0 0.82 0.18 Algae 0.65 0.255 0.095 0.65 0.28 0.07 a See (Cerco and Cole, 1994, Figure 10-6) for the Zones definition.


Table 8.25. Sediment Burial Rates (W) Used in (Cerco and Cole, 1994)

Bay Zonesa Rate (cm/yr) Tributary Zonesa Rate (cm/yr) 1, 2, 10 0.50 1 0.50 3, 6, 9 0.25 2, 3 0.25 7, 8 0.37

a See (Cerco and Cole, 1994, Figure 10-6) for the definition of Zones.

###### 229



<<<PAGE 243>>>

# Chapter 9 LAGRANGIAN PARTICLE TRACKING

The Lagrangian Particle Tracking (LPT) module in EFDC+ is developed as an effective tool for solving numerous problems in fluid dynamics related to the simulation and prediction of the trajectory of objects traveling in rivers, lakes, and marine systems. DSI has calibrated EFDC+ with LPT module using a simple analytical calculation for quasi-steady state and uniform flow in an open channel. In addition, several tests with different hydrodynamic regimes and geometries have been performed. The soundness of this module was also demonstrated in a variety of applications (DSI, 2009). Through the simulations, it was found that not only the velocity field but also the randomness and diffusion due to turbulence also considerably impact the dispersion of the cluster and behavior of drifter trajectories.

Study of the trajectories of movement of solid particles in a fluid environment appeared very early in mechanics and was considered as a movement in a Lagrangian approach. The advantage of this method is that it is possible to track the process of movement for each specific particle in more detail and more accurately in comparison with the method of determining average concentration for grid cells. However, the solution was too difficult to implement in practice when the number of particles was very large because of computation costs. With the reduction in computing costs it is now easier to implement the solutions to these problems. The movement of solid particles is decided by a field of fluid velocity, therefore it is necessary to couple it to a fluid flow model.

##### 9.1. Basic Equations

The governing equations used in EFDC+ are Navier-Stokes for fluid flow, the advection-diffusion equations for salinity, temperature, dye, toxic substances and suspended sediment transport (Hamrick and Wu, 1997; Hamrick, 1992, 1996). The equations are presented in curvilinear coordinate system for 2DH and SIG coordinates for the vertical direction. They are discretized with the finite difference method with explicit scheme. It should be noted that the hypothesis of hydrostatic pressure is used in EFDC+. However, the effect of non-hydrostatic pressure is not important when the vertical velocity of flow is not very large in comparison with the horizontal components as mentioned in Huu Chung and Eppel (2008).

The advection-diffusion equation for mass transport in a three dimensional curvilinear orthogonal coordinate system is:

∂C ∂t

∂(uC) ∂x

∂(vC) ∂y

∂(wC) ∂z

∂ ∂x

∂C ∂x

∂ ∂y

∂C ∂y

∂ ∂z

∂C ∂z

(9.1) where,

AH

AH

Ab

+

+

+

=

+

+

t is time, (x,y,z) are Lagrangian coordinates of a particle,

###### 230



<<<PAGE 244>>>

###### 9. LAGRANGIAN PARTICLE TRACKING EFDC+ Theory



C is concentration, (u,v,w) are velocity components of fluid flow, and AH and Ab are the horizontal and vertical diffusion coefficients, respectively.

The differential equations for the Lagrangian movement of particles is consistent with the equation (9.1) and are as follows:

∂AH ∂x

dx = u+

dt +(2p−1) 2AHdt (9.2)

∂AH ∂y

dy = v+

dt +(2p−1) 2AHdt (9.3)

∂Ab ∂z

dz = w+

dt +(2p−1) 2Abdt (9.4)

In which dt is the time step and p is a random number from a uniformly distributed random variable generator with a mean value of 0.5. When transformed using 2p−1, the random component has a mean of zero and a range from -1 to 1. The transformed random value allows the diffusion term to move particles +/− about the advected position. Equations (9.2) to (9.4) follow the 3D random walk approach used by Dunsbergen and Stelling (1993).

In order to determine the Lagrangian trajectory of the particle, the equations (9.2) to (9.4) were incorporated into EFDC+ model. The numerical solution was separately divided into the advective transport and random components as described above. This approach allows the user to enable (i.e. turn on random walk) or disable (advective transport only) the random components for either the horizontal and/or the vertical directions.

Three options are available for the solution of the differential equations (9.2) to (9.4). They are explicit Euler, predictorcorrector Euler, and forth order Runge-Kutta. Their discretization for the equations are as follows:

Explicit Euler method: This method is very simple with the approximation of O(∆t)

xn+1 = xn +u(tn,xn,yn,zn)∆t (9.5)

yn+1 = yn +v(tn,xn,yn,zn)∆t (9.6)

zn+1 = zn +w(tn,xn,yn,zn)∆t (9.7) Predictor-corrector Euler method: This method has the advantage of explicit and implicit features with the approx-

imation of O(∆t2)

1 2

xn+1 = xn +

u(tn,xn,yn,zn)+u tn+1,xnp+1,ynp+1,znp+1 ∆t (9.8)

- 1

- 2


yn+1 = yn +

v(tn,xn,yn,zn)+v tn+1,xnp+1,ynp+1,znp+1 ∆t (9.9)

- 1

- 2


w(tn,xn,yn,zn)+w tn+1,xnp+1,ynp+1,znp+1 ∆t (9.10) where , xnp+1,ynp+1,znp+1 are calculated by equations (9.4) to (9.6)

zn+1 = zn +

Runge-Kutta 4 method: This method has the approximation of O(∆t4) and has been shown in testing that it is the

best option of the three solution techniques provided

###### 231



<<<PAGE 245>>>

###### 9. LAGRANGIAN PARTICLE TRACKING EFDC+ Theory



xn+1 = xn +

1 6

(∆x1 +2∆x2 +2∆x3 +∆x4) (9.11)

yn+1 = yn +

1 6

(∆y1 +2∆y2 +2∆y3 +∆y4) (9.12)

1 6

(∆z1 +2∆z2 +2∆z3 +∆z4) (9.13) in which

zn+1 = zn +

- ∆x1 = u(tn,xn,yn,zn)∆t (9.14)
- ∆y1 = v(tn,xn,yn,zn)∆t (9.15)
- ∆z1 = w(tn,xn,yn,zn)∆t (9.16)


- ∆x2 = u tn +

- 1

- 2


∆t,xn +

- 1

- 2


∆x1,yn +

- 1

- 2


∆y1,zn +

1 2

∆z1 ∆t (9.17)

- ∆y2 = v tn +

1 2

∆t,xn +

1 2

∆x1,yn +

1 2

∆y1,zn +

- 1

- 2


∆z1 ∆t (9.18)

- ∆z2 = w tn +


1 2

∆t,xn +

1 2

∆x1,yn +

1 2

∆y1,zn +

1 2

∆z1 ∆t (9.19)

- ∆x3 = u tn +

1 2

∆t,xn +

- 1

- 2


∆x2,yn +

1 2

∆y2,zn +

1 2

∆z2 ∆t (9.20)

- ∆y3 = v tn +

1 2

∆t,xn +

- 1

- 2


∆x2,yn +

- 1

- 2


∆y2,zn +

- 1

- 2


∆z2 ∆t (9.21)

- ∆z3 = w tn +


- 1

- 2


∆t,xn +

- 1

- 2


∆x2,yn +

- 1

- 2


∆y2,zn +

- 1

- 2


∆z2 ∆t (9.22)

- ∆x4 = u(tn +∆t,xn +∆x3,yn +∆y3,zn +∆z3)∆t (9.23)
- ∆y4 = v(tn +∆t,xn +∆x3,yn +∆y3,zn +∆z3)∆t (9.24)
- ∆z4 = w(tn +∆t,xn +∆x3,yn +∆y3,zn +∆z3)∆t (9.25)


###### 232



<<<PAGE 246>>>

###### 9. LAGRANGIAN PARTICLE TRACKING EFDC+ Theory



##### 9.2. Oil Spill Model

EFDC+ allows for the simulation of oil spills using the same net transport approach used for the drifters. Each oil spill ”particle” (referred to here as a ”packet”) is assigned a mass based on the total mass spilled or discharged and the number of packets defined for that event. Packets can be released all at once or over a specified time interval. The oil packets will be maintained near the water surface (5 mm below) if settling or rising rates are set to zero. Additional processes unique to the oil spill module include direct wind drag (in addition to wind drag induced surface currents), evaporation and biodegradation.

##### 9.2.1 Wind Drag

If the oil spill is located at the surface, wind drag can be added to the advective transport component of the oil spill following (Kim et al., 2014).

Voil = Vcurrent +(CD×Vwind) (9.26)

where Voil and Vcurrent are the velocities of the oil spill and tidal current respectively, Vwind is the wind speed at a height of 10 m, and CD is the wind drag coefficient . In EFDC+, this basic equation is implemented with two options.

- Option 1 CD = A×Vwindmag +B (9.27)
- Option 2 CDX = A×Vwindx +B (9.28) CDY = A×Vwindy +B (9.29)


Finally, the actual displacement due to wind drag is calculated using:

dx = CDX ×Vwindx ×∆t (9.30) dy = CDY ×Vwindy ×∆t (9.31)

Where coefficient A has units of s/m, coefficient B is dimensionless, CD is dimensionless and the velocity terms are all in m/s. If A is zero then a constant drag coefficient is used, similar to Kim et al. (2014). The range of values for CD can vary from 0.0 to 0.1, with a typical value of 0.02 to 0.03.

##### 9.2.2 Loss Terms

The mass of the oil spill can be impacted by a number of processes, two of which are currently in EFDC+, evaporation and biodegradation. If the mass in a packet is less than 1e-9 kg, EFDC+ will deactivate that packet for future processing.

For simulation of the oil evaporation process, the theory of surface evaporation presented in the paper by Stiver and Mackay (1984) is used. If water temperature is being simulated, then the oil packet temperature is assumed to be the same as the surrounding water. If temperature is not simulated, then the specified temperature is used as a constant value for the evaporation process.

Biodegradation of an oil packet uses a simple first order decay approach based on Stewart et al. (1993). As an example, a biodegradation rate of 0.011 day−1 is approximately equal to the half-life of two months. If water temperature is being simulated, then the spill temperature specified by the user is the biodegradation rate reference temperature for the optimal biodegradation. If water temperature is not being simulated, the user input degradation rate is applied as a constant.

To ignore evaporation, set the vapor pressure to zero. To ignore biodegradation, set the degradation rate to zero.

###### 233



<<<PAGE 247>>>

# Chapter 10 MARINE HYDROKINETICS

Marine hydrokinetic (MHK) devices extract energy from ocean currents and tides, thereby altering water velocities and currents in the project sites. These hydrodynamic changes can potentially affect the ecosystem, both near the MHK installation and in surrounding (i.e., far field) regions. In both marine and freshwater environments, devices will remove energy (momentum) from the system, potentially altering water quality and sediment dynamics. In estuaries, tidal ranges and residence times could change (either increasing or decreasing depending on system flow properties and where the effects are being measured). Effects will be proportional to the number and size of structures installed, with large MHK projects having the greatest potential effects and requiring the most in-depth analyses. The theory and implementation of MHK in SNL-EFDC+ is presented by James et al. (2010).

##### 10.1. Theory of Marine Hydrokinetics

MHK devices remove momentum from a system, but also alter the turbulent kinetic energy K, and turbulent kinetic energy dissipation rate ε. These effects are captured with appropriate sink terms. SQ (m4/s2) is the volumetric momentum extraction rate by the MHK device due to energy removal, as well as due to form and viscous drag from the MHK structure. SK (m5/s3) represents the volumetric change in net turbulent kinetic energy in the appropriate model cell due to the MHK device (support), with Sε (m5/s3) as its analogous term for the volumetric kinetic energy dissipation rate equation (Poggi et al., 2004). These quantities are advected and dispersed downstream of the MHK device according to the standard conservation equations used in EFDC+. The standard calculation for SQ neglects viscous drag relative to energy removal and form drag by the MHK device, thereby resulting in

1 2

CTAMU2 (10.1) where,

SQ = −

CT is the MHK thrust coefficient (drag coefficient, CD, for the support) (dimensionless), AM is the MHK-device flow-facing area (support flow-facing area) (m2), and U is the local flow speed in a cell (u2 +v2) (m/s).

Here, MHK-device power PM (kgm2/s3) is defined as

1 2

CTAMρU3 (10.2) where, ρ (kg/m3) is the water density.

PM =

###### 234



<<<PAGE 248>>>

###### 10. MARINE HYDROKINETICS EFDC+ Theory



The term SK arises because MHK devices break up the mean flow motion and generate wake turbulence (≈ 12CTAMU3). However, such wakes dissipate fairly rapidly, speculatively within about 30 MHK device lengths (turbine diameters).

Preliminary MHK Computational Fluid Dynamics (CFD) models showed overly persistent wakes, perhaps in part because this term was not taken into account. The canonical (or physics-based) form for SK reflecting the effects of a momentum sink (or partial flow obstruction) is (Sanz, 2003):

1 2

CTAM βpU3 −βdUK (10.3) where,

SK =

K is the wake-generated turbulent kinetic energy (m2/s2), βp (≈ 1.0) is the fraction of mean flow kinetic energy converted to K by drag (i.e., a source term in the K

budget) (dimensionless), and βd (≈ 1.0 − 5.0) is the fraction of K dissipated by conversion to kinetic energy (i.e., a sink term in the K budget) (dimensionless).

The most obvious weakness of the K −ε approaches is its least understood term Sε (Wilson et al., 1998). Over the last decade or so, various models have been proposed for Sε (Green, 1992; Katul et al., 2004; Liu et al., 1996), but the simplest is used in this model:

e K

SK (10.4) where Cε4 is a closure constant (Katul et al., 2004).

Se = Ce4

The formulation for equation (10.4) is based on standard dimensional analysis common to all K −ε approaches. Upon adding equations (10.1) to (10.4) to the momentum and K − ε equations, it is possible to solve for momentum K, and ε if appropriate upper and lower boundary conditions are specified. For this implementation, Cε4 = 0.9, βp = 1.0 and βd = 5.1. In SNL-EFDC+, momentum is defined as the product of flow depth H, and velocity u and v; conservation of kinetic energy is solved in terms of 12HQ2, where q is the turbulent intensity, and conservation of turbulent energy dissipation rate takes the form HQ2l, where l is the turbulence length scale.

##### 10.2. Implementation in EFDC+

The simplified kinetic energy equation for an MHK device in a model σ layer is

∂ ∂t

u2 +v2 2

mxmyρH∆k

1 2

= −

ρCTAM u2 +v2

3

2 = −PM (10.5)

AM = WMH∆k (10.6) where,

mx, my are the (horizontal) x and y dimensions of a model cell (m), ∆k is the fraction of total water depth assigned to the kth σ layer, AM is the frontal flow area of the device (m2), WM is the device or support width (m), and H∆k is the layer thickness (m).

###### 235



<<<PAGE 249>>>

###### 10. MARINE HYDROKINETICS EFDC+ Theory



The corresponding components of the momentum equations, simplified to exclude advective and diffusive terms are (Galperin and Orszag, 1993),

∂ ∂t

∂ζ ∂x −

(mxmyH∆ku) = −gmyH∆k

- 1

- 2


CTAM u2 +v2

- 1

- 2u (10.7)


∂ ∂t

∂ζ ∂y −

1 2

CTAM u2 +v2 where,

(mxmyH∆kv) = −gmxH∆k

- 1

- 2v (10.8)


g is acceleration due to gravity (m/s2), and ζ is the free-surface potential (m), or the difference between the hydrostatic water level and the flow depth

(this is how water elevation or pressure head drives flow). Solutions of the x- and y-momentum equations in EFDC+ use the form,

∂ ∂t

H mx

(Hu) = −g

∂ζ ∂x −

1 2mxmy∆k

CTAM u2 +v2

- 1

- 2 u (10.9)


∂ ∂t

∂ζ ∂y −

H my

1 2mxmy∆k

- 1

- 2 v (10.10) which can be written in terms of MHK device power (and equivalently for support-structure momentum removal) as


CTAM u2 +v2

(Hv) = −g

∂ ∂t

∂ζ ∂x −

H mx

(Hu) = −g

1 mxmy∆k

PM ρ (u2 +v2)

u (10.11)

∂ζ ∂y −

∂ ∂t

H my

(Hv) = −g

1 mxmy∆k

PM ρ (u2 +v2)

v (10.12)

The solution procedure begins by introducing the σ layer notation based on ∆k:

∂ ∂t

H mx

(∆kHuk) = −g∆k

∂ζ ∂x −

1 mxmy∆k

PM ρ (u2 +v2) k

∆kuk (10.13)

∂ ∂t

H my

(∆kHvk) = −g∆k

∂ζ ∂y −

1 mxmy∆k

PM ρ (u2 +v2) k

∆kvk (10.14)

The momentum conservation equations are

∂ ∂t

H mx

(∆kHuk) = −g∆k

∂ζ ∂x −∆k Qk −Qˆ uk −∆kQuˆ k (10.15)

where volumetric fluxes Q are

∂ ∂t

H my

(∆kHvk) = −g∆k

∂ζ ∂y −∆k Qk −Qˆ vk −δkQvˆ k (10.16)

Qk =

1 mxmy∆k

PM ρ (u2 +v2) k

(10.17)

###### 236



<<<PAGE 250>>>

###### 10. MARINE HYDROKINETICS EFDC+ Theory



KC

#### ∑

Qˆ =

∆kQk (10.18)

k=1

From this point, the solution procedure is illustrated using only the u equation, which is summed over all KC layers to give

∂ζ ∂x −

∂ ∂t

H mx

(Huˆ) = −g

KC

#### ∑

∆k Qk −Qˆ uk −Qˆuˆ (10.19)

k=1

KC

#### ∑

∆kuk (10.20)

uˆ =

k=1

which is the simplified external mode equation. This equation is solved with the continuity equation for the depthaveraged velocity components, uˆ and v−, and the water surface elevation H, using the time-differenced form

Qˆ H

∂ζn+1 ∂x

∆t 2

H mx

∆t (Huˆ)n+1 +

g

1+

###### =

KC

∂ζn ∂x −∆t

∆t 2

H mx

∆k Qk −Qˆ uk n (10.21)

#### ∑

(Huˆ)n −

g

k=1

where ∆t is the time step. The internal-mode equation solution is based on considering the difference between equations for two adjacent layers

which has the remainder as

∂ ∂t

H mx

(Huk+1) = −g

∂ζ ∂x − Qk+1 −Qˆ uk+1 −Quˆ k+1 (10.22)

∂ ∂t

H mx

(Huk) = −g

∂ζ ∂x − Qk −Qˆ uk −Quˆ k (10.23)

Qˆ H

∂ ∂t

(Huk+1 −Huk) = − Qk+1 −Qˆ uk+1 + Qk −Qˆ uk (10.24) Time differencing yields

(Huk+1 −Huk)+

Qˆ H

1+∆t

(Huk+1 −Huk)n+1 =

(Huk+1 −Huk)n −∆t Qk+1 −Qˆ uk+1 − Qk −Qˆ uk n (10.25)

The system of KC −1 layer-interface equations can be solved for the velocity differences across the layer and used with the definition of the depth-averaged velocity to determine the actual layer velocities.

The MHK device effect in the turbulent kinetic energy (turbulent intensity) equation is given by

∂ ∂t

q2 2

H

= βp

- 1

- 2


1 mxmy∆k

CTAM u2 +v2

- 1

- 2 u2 +v2 −


βd

1 2

1 mxmy∆k

CTAM u2 +v2

- 1

- 2 q2 2 −


H B1l

q3 (10.26)

###### 237



<<<PAGE 251>>>

###### 10. MARINE HYDROKINETICS EFDC+ Theory



where, B1 = 16.6 (dimensionless) is a turbulence closure coefficient from Mellor and Yamada (1982). The dissipation effect of the device is combined with the standard flow dissipation term to give

∂ ∂t

q2 2

H

 βd

+

- 1

- 2


CTAM mxmy∆k

1 2

u2 +v2

H

 Hq2 =

q B1l

+

βp

1 2

CTAM mxmy∆k

u2 +v2

- 1

- 2 u2 +v2 (10.27)


where the total dissipation has been moved to the left side of the equation to emphasize that it must be treated implicitly in the numerical solution procedure given by

 

 βd

1+∆t



CTAM mxmy∆k

1 2

u2 +v2

H

 

 

2q B1l

+



Hq2 n+1 =

Hq2 n +∆tβp

CTAM mxmy∆k

The turbulent length scale equation (turbulent kinetic energy dissipation rate) is

u2 +v2

- 1

- 2 u2 +v2 (10.28)


∂ ∂t

 Ce4βd

Hq2l +

1 2

CTAM mxmy∆k

- 1

- 2


u2 +v2 H

######  Hq2l =

q B1l

+

Ce4βp

which is solved similar to the turbulent kinetic energy equation using

- 1

- 2


CTAM mxmy∆k

u2 +v2

- 1

- 2 u2 +v2 l (10.29)


 

 Ce4βd

1+∆t



1 2

CTAM mxmy∆k

1 2

u2 +v2

+

H

q B1l

 

 

Hq2l n+1 =



Hq2l n +∆tCe4βp

- 1

- 2


CTAM mxmy∆k

u2 +v2

- 1

- 2 u2 +v2 l (10.30)


###### For completeness, vegetative resistance effects on K −ε were also included in the SNL-EFDC+ coding.

###### 238



<<<PAGE 252>>>

# Chapter 11 SHELLFISH FARMING

This section summarizes the basic theory of the shellfish module implemented in the EFDC+ code. DSI appreciates ongoing collaboration with the Marine Environment Research Division of Korea’s National Institute of Fisheries Science for developing this module. Shellfish filter feeders interact with multiple components of the eutrophication model. These organisms remove POM from the water column for ingestion and assimilation and deposit a portion of it in the bottom sediments as feces. (Cerco and Noel, 2005). In EFDC+, the kinetic processes of the shellfish include filtering, ingestion, assimilation, respiration, mortality, and spawning. A shellfish individual is quantified as the OC incorporated in soft tissue which is computed as a function of food availability, respiration, and mortality. The environmental effects on shellfish life processes are considered by its interactions with the water quality model.

##### 11.1. Governing Equation

For each shellfish individual, the change of its weight with time is the result of changes in net production. Therefore, a fundamental growth equation for filter feeder biomass can be written as:

dWd dt

= NP (11.1) where,

t is the time (s), Wd is the dry meat weight (g C), and NP is the net production (g C).

According to White et al. (1988) and Kobayashi et al. (1997), the net production is the sum of somatic and reproductive tissue production, which is assumed to be the difference between assimilation and respiration:

NP = Pg +Pr = A−R (11.2) where,

Pg is the somatic production (g C), Pr is the reproductive tissue production (g C), and A is the assimilation (g C) and R is the respiration (g C).

###### 239



<<<PAGE 253>>>

###### 11. SHELLFISH FARMING EFDC+ Theory



##### 11.2. Length - Weight Relation

The relationship between shell length and live weight is routinely used as an index of oyster growth. It is well known with an equation of the form:

L = A·WdB (11.3) where,

L is the shell length (cm), and A,B are constants parameters.

By fitting this equation to the experimental measurements, Kobayashi et al. (1997) gave A = 77.9 and B = 0.291 for the Japanese oyster, Crassostrea gigas.

##### 11.3. Filtration Rate

Shellfish filtration rate is quantified as water volume cleared of particles per individual per unit time. It is the major determinant of growth that in turn affects changes in shellfish biomass. In EFDC+, filtration rate is represented as a maximum or optimal rate that is modified by ambient temperature, suspended solids, salinity, and dissolved oxygen:

where,

FR = FRW · f1(T)· f2(S)· f3(TSS)· f4(DO) (11.4)

FR is the filtration rate (l filtered per individual h−1), FRW is the maximum filtration rate (l filtered per individual h−1),

- f1(T) is the effect of temperature on filtration rate (0 < f1(T) ≤ 1),
- f2(S) is the effect of salinity on filtration rate (0 < f2(S) ≤ 1),
- f3(TSS) is the effect of suspended solids on filtration rate (0 < f3(TSS) ≤ 1), and
- f4(DO) is the effect of dissolved oxygen on filtration rate (0 < f4(DO) ≤ 1).


##### 11.3.1 Maximum Filtration Rate

The maximum filtration rate is commonly estimated from the dry meat weight Wd. Coughlan and Ansell (1964) provides the following relationship for siphonate bivalves:

FRW = 2.59·Wd0.73 (11.5)

Another formulation was used by Cloern (1982) for studying of bivalves in South San Francisco Bay:

FRW = 7.0·Wd0.67 (11.6)

For the Japanese oyster, Crassostrea gigas, Kobayashi et al. (1997) proposed the following formula for the maximum filtration rate:

FRW =

2.51·Wd0.279, Wd ≥2g 0.117·Wd3 −1.05·Wd2 +3.09·Wd +0.133, Wd < 2g

(11.7)

###### 240



<<<PAGE 254>>>

###### 11. SHELLFISH FARMING EFDC+ Theory



Cerco and Noel (2007) used a constant factor for the maximum filtration rate while studying the native oysters, Crassostrea virginica in Chesapeake Bay:

1000

24 ·Wd = 22.917·Wd (11.8) On the other hand, Officer et al. (1982) determined the maximum filtration rate from the total weight W:

FRW = 0.55·

FRW = 0.76·W0.60 (11.9)

The temperature effect on the maximum filtration rate can be also included as (Doering and Oviatt, 1986):

L0.96T0.95 2.95

60 1000

FRW =

(11.10)

##### 11.3.2 Temperature Effect

From Kobayashi et al. (1997), the effect of temperature on filtration rate is modeled as:

f1(T) =

T0.5 4.47, T≥7◦C

0.59, T < 7◦C

(11.11)

Cerco and Noel (2007) considered the temperature effect as an exponentially increasing function of temperature :

f1(T) = exp(−Ktg·(T −Topt)2) (11.12) where,

T is the temperature (◦C), Topt is the temperature for optimal filtration (◦C), and Ktg is the coefficient for the effect of temperature on filtration.

##### 11.3.3 Salinity Effect

According to Loosanoff (1958), the filtration rate decreases below 7.5 ppt and ceases at 3.5 ppt. A linear relationship was also introduced for the salinity effect between these threshold values:

 

1, S ≥ 7.5ppt

S−3.5 7.5−3.5, 3.5 < S < 7.5ppt 0, S ≤ 3.5ppt

f2(S) =

(11.13)



where S is the ambient salinity (ppt). A similar mathematical formulation for the salinity effect was reported by Quayle (1988) and Mann et al. (1991) but different threshold salinity values:

 

1, S ≥ 20ppt

S−10 20−10, 10 < S < 20ppt

(11.14)

f2(S) =



0, S ≤ 10ppt

###### 241



<<<PAGE 255>>>

###### 11. SHELLFISH FARMING EFDC+ Theory



In Cerco and Noel (2005), the authors proposed a tanh functional from for the effect of salinity on filtration rate:

f2(T) = 0.5·(1+tanh(S−SKH)) (11.15) with SKH is the the salinity at which the filtration rate is halved (ppt). Fulford et al. (2007) adjusted the salinity effect as a linear function salinity based on data measurement for oyster Crassostrea virginica in Chesapeake Bay, USA:

f2(T) = 0.0926·S−0.139 (11.16)

Buzzelli et al. (2015) included the effect of salinity on filtration rate simulation of oyster in south Florida estuaries as:

- f2(T) = −0.0017·S2 +0.0084·S−0.1002 (11.17)

11.3.4 Suspended Solids Effect

The effect of high suspended solids concentrations on oyster filtration rate has been long recognized through experiments by Loosanoff and Tommers (1948). From the given data, Hofmann et al. (1992) deduced a formulation as follows:

- f3(TSS) = 1−0.001.


log10(TSS)+3.38 0.418

(11.18)

Cerco and Noel (2005) applied a piecewise function, obtained though visual fit to the data from Jordan (1987) and supplement with the results from Loosanoff and Tommers (1948):

 

- 0.1, TSS < 5mg/l
- 1.0, 5 < TSS < 25mg/l 0.2, 25 < TSS < 100mg/l 0.0, TSS ≥ 100mg/l


(11.19)

f3(TSS) =



Fulford et al. (2007) modeled the effect of suspended solid as a power function derived from the data measured by the EPA Chesapeake Bay Monitoring Program:

f3(TSS) = 10.364·ln(TSS)−2.0477, TSS > 25mg/l (11.20)

##### 11.3.5 Dissolved Oxygen (DO) Effect

The model formulation incorporates DO effects on filtration rate which are expressed as proposed in Cerco and Noel

(2005):

1 1+exp(1.1×

f4(DO) =

(11.21)

DOhx −DO DOhx −DOqx

)

where DO is the dissolved oxygen concentration (mg/l); DOhx and DOqx are the DO concentrations (mg/l) at which the filtration rates are 50% and 25% of maximum, respectively.

##### 11.4. Ingestion and Assimilation

Shellfish ingestion capacity is given by multiplying the filtration rate by the food concentration:

24 1000×f×FR (11.22)

I =

###### 242



<<<PAGE 256>>>

###### 11. SHELLFISH FARMING EFDC+ Theory



where, I is the ingestion (g dry weight per individual day−1) and f is the food concentration (measured food value) (mg dry weight l−1).

Shellfish assimilation is obtained from ingestion using an assimilation efficiency. It is noted that the fraction of ingested carbon assimilated by shellfish depends on the carbon source.

A = α×I (11.23) in which A is the assimilation rate (g dry weight per individual day−1) and α is the assimilation efficiency. Shellfish assimilation can be converted into energy via:

EA = CE×A (11.24)

where EA is the assimilation energy (calories per individual day−1) and CE is the caloric conversion factor (5210 calories per g dry weight).

##### 11.5. Respiration

Shellfish respiration is commonly represented as a function of temperature and the dry meat weight:

R = BM·Wd (11.25) where BM is the dependency of respiration on temperature. Several mathematical formulations of BM have been proposed in literature and implemented in the EFDC+ code. According to the Korean National Institute of Fisheries Science (Kim, 2019):

where,

BM =

αR·θT−TB, T > TB 0, T≤TB

(11.26)

TB is the base temperature for respiration (◦C), αR metabolism rate at reference temperature (day−1), and θ is a temperature coefficient for respiration.

Cerco and Noel (2007) considered basal metabolism to be an exponentially increasing function of temperature

BM = αR·exp(KTb·(T −Tr)) (11.27) where,

Tr is the reference temperature for specification of metabolism (◦C), αR metabolism rate at reference temperature (day−1), KTb is a constant that relates metabolism to temperature (◦C−1).

For C. virginica oyster, respiration rate as a function of temperature and shellfish dry meat weight can be also obtained from Dame (1972):

R = (12.6·T +69.7)·Wd−0.25 (11.28)

According to Hofmann et al. (1992), salinity effects on oyster respiration over a range of temperature, were parameterized using data given in (Shumway and Koehn, 1982):

###### 243



<<<PAGE 257>>>

###### 11. SHELLFISH FARMING EFDC+ Theory



0.007·T +2.099, T < 20◦C 0.0915·T +1.324, T ≥ 20◦C

(11.29)

RR =

Where, RR is the ratio of respiration at 10ppt to respiration at 20ppt: RR = R10ppt/R20ppt. Equations (11.28) and (11.29) were combined to obtain respiration over a range of salinity as follows:

 

R, S ≥ 15ppt R(1+(RR −1)155−S), 10 < S < 15ppt RRR, S ≤ 10ppt

R =

(11.30)



Shumway and Koehn (1982) identified effects of salinity on respiration at 20ppt. Finally, the energy consumed by respiration is given by:

24

1000×CR×R×Wd (11.31) where,

ER =

ER is the respiration energy (calories per individual day−1), CR is the caloric conversion factor (calories per ml oxygen), and R is the respiration rate (µl oxygen per g dry weight h−).

##### 11.6. Reproduction

For adult shellfish greater or equal to a certain size, net production was apportioned into growth and reproduction by using a temperature-dependent reproduction efficiency of the form:

Pr = Ref f·NP (11.32) where Ref f is the temperature-dependent reproduction efficiency. A formulation of Ref f, derived empirically from observations, was reported in Kobayashi et al. (1997):

 

0.8, T≥27◦C 0.2·T −4.6, 23 < T < 27◦C 0, T≤23◦C

Ref f =

(11.33)



In cases where NP < 0, a preferential resorption of gonadal tissue is assumed to cover the deficit.

##### 11.7. Spawning

Spawning occurs when the environmental conditions (temperature and salinity) are in the suitable ranges and the cumulative production biomass exceeds a certain fraction of shellfish total biomass. Once spawning occurs, the total reproductive biomass is apportioned into male and female biomass. The ratio of females to males is calculated as e.g., (Powell et al., 1994):

fratio = 0.021·Lb −0.62 (11.34)

###### 244



<<<PAGE 258>>>

###### 11. SHELLFISH FARMING EFDC+ Theory



where fratio is the ratio of females to males and Lb is the shell length in mm. Then, the female portion of reproductive biomass can be calculated and converted into eggs spawned as follows:

1 Eegg ·

1 Wegg

neggs = Rf·

(11.35)

where,

neggs is the number of eggs spawned, Rf is the female portion of reproductive biomass, Weggs is the egg weight, and Eeggs is the egg’s caloric content (cal. g dry weight−1).

For oysters, the egg weight can be estimated from egg volume as:

Weggs = 2.14×10−14·Vegg (11.36) where Vegg is the oyster egg volume (µm3).

###### 245



<<<PAGE 259>>>

# Chapter 12 References

Abramowitz, M. (1964). Handbook of mathematical functions, national bureau of standards. Applied Mathematics Series (55). Ackers, P. and W. R. White (1973). Sediment transport: new approach and analysis. Journal of the Hydraulics

Division 99(11), 2041–2060. Anderson, E. et al. (1954). Water loss investigations: Lake hefner studies. US Department of the Interior, Geol. Anderson, R. (1993). A study of wind stress and heat flux over the open ocean by the inertial-dissipation. Arakawa, A. and V. R. Lamb (1977). Computational design of the basic dynamical processes of the ucla general

circulation model. General circulation models of the atmosphere 17(Supplement C), 173–265. Bagnold, R. A. (1956). The flow of cohesionless grains in fluids. Philosophical Transactions of the Royal Society of London. Series A, Mathematical and Physical Sciences 249(964), 235–297. Banks, R. B. and F. F. Herrera (1977). Effect of wind and rain on surface reaeration. Journal of the Environmental Engineering Division 103(3), 489–504. Barrow, N. (1983). A mechanistic model for describing the sorption and desorption of phosphate by soil. Journal of

soil science 34(4), 733–750. Belov, A. P. and J. D. Giles (1997, Aug). Dynamical model of buoyant cyanobacteria. Hydrobiologia 349(1), 87–97. Blumberg, A. F. and G. L. Mellor (1987). A description of a three-dimensional coastal ocean circulation model.

Three-dimensional coastal ocean models 4, 1–16. Boni, L., E. Carpene, D. Wynne, and M. Reti (1989). Alkaline phosphatase activity in protogonyaulax tamarensis. Journal of plankton research 11(5), 879–885. Boudreau, B. P. (1991). Modelling the sulfide-oxygen reaction and associated ph gradients in porewaters. Geochimica et Cosmochimica Acta 55(1), 145–159.

Bowie, G. L., W. B. Mills, D. B. Porcella, C. L. Campbell, J. R. Pagenkopf, G. L. Rupp, K. M. Johnson, P. Chan, S. A. Gherini, C. E. Chamberlin, et al. (1985). Rates, constants, and kinetics formulations in surface water quality modeling. EPA 600, 3–85.

Brady, D. K., W. L. Graves, Jr, and J. C. Geyer (1969, 11). Surface heat exchange at power plant cooling lakes. report no. 5. eei publication no. 69-901. Technical report.

Bunch, B. W., C. F. Cerco, M. S. Dortch, B. H. Johnson, and K. W. Kim (2000). Hydrodynamic and water quality model study of san juan bay estuary. Technical report, Army Engineer Waterways Experiment Station Vicksburg Ms Engineer Research.

Burban, P.-Y., W. Lick, and J. Lick (1989). The flocculation of fine-grained sediments in estuarine waters. Journal of Geophysical Research: Oceans 94(C6), 8323–8330. Burban, P.-Y., Y.-J. Xu, J. McNeil, and W. Lick (1990). Settling speeds of floes in fresh water and seawater. Journal of Geophysical Research: Oceans 95(C10), 18213–18220. Buzzelli, C., P. Gorman, P. Doering, Z. Chen, and Y. Wan (2015). The application of oyster and seagrass models to

evaluate alternative inflow scenarios related to everglades restoration. Ecological Modelling 297, 154–170. Canuto, V. M. and Y. Cheng (1997). Determination of the smagorinsky–lilly constant CS. 9(5), 1368–1378. Carritt, D. E. and S. Goodgal (1954). Sorption reactions and some ecological implications. Deep Sea Research

(1953) 1(4), 224–243.

###### 246



<<<PAGE 260>>>

###### REFERENCES EFDC+ Theory



Caupp, C. L., J. T. Brock, and H. M. Runke (1991). Application of the dynamic stream simulation and assessment model (DSSAM III) to the Truckee River below Reno, Nevada: Model formulation and program description. Rapid Creek Water Works.

Cerco, C. and T. Cole (1994). Three-dimensional model of cheasapeake bay. Vicksburg: US Army Corps of Engineers Technical Report EL-94-4.

Cerco, C. and M. Noel (2005, 07). Assessing a ten-fold increase in the chesapeake bay native oyster population - a report to the epa chesapeake bay program. Technical report, US Army Engineer Research and Development Center, Vicksburg MS.

Cerco, C. and M. Noel (2007). Can oyster restoration reverse cultural eutrophication in chesapeake bay? Estuaries and Coasts 30(2), 43–61. Cerco, C. F., B. W. Bunch, A. M. Teeter, and M. S. Dortch (2000). Water quality model of florida bay. Technical report, Engineer Research and Development Center Vicksburg MS Environmental Lab. Cerco, C. F. and T. Cole (1993). Three-dimensional eutrophication model of chesapeake bay. Journal of Environmental Engineering 119(6), 1006–1025. Cerco, C. F. and T. Cole (1995). User’s guide to the ce-qualicm three-dimensional eutrophication model. US Army Corps of Engineers, Waterways Experiment Station, Technical report EL-95-15, Vicksburg, Mississippi. Cerco, C. F., L. Linker, J. Sweeney, G. Shenk, and A. J. Butt (2002). Nutrient and solids controls in virginia’s

chesapeake bay tributaries. Journal of Water Resources Planning and Management 128(3), 179–189. Cerco, C. F., M. R. Noel, et al. (2004). The 2002 Chesapeake Bay Eutrophication Model. Citeseer. Cerco, C. F., M. R. Noel, and S.-C. Kim (2004). Three-dimensional eutrophication model of lake washington, washington state. Technical report, Engineer Research And Development Center Vicksburg Ms Environmental Lab. Chapra, S. (1997). Surface Water-quality Modeling. McGraw-Hill series in water resources and environmental engi-

neering. McGraw-Hill. Chapra, S. C., L. A. Camacho, and G. B. McBride (2021). Impact of global warming on dissolved oxygen and bod assimilative capacity of the world’s rivers: modeling analysis. Water 13(17), 2408. Chapra, S. C., R. P. Canale, and G. L. Amy (1997). Empirical models for disinfection by-products in lakes and reservoirs. Journal of Environmental Engineering 123(7), 714–715. Cheng, N.-S. (1997). Simplified settling velocity formula for sediment particle. Journal of hydraulic engineering 123(2), 149–152.

Chr´ost, R. J. and J. Overbeck (1987). Kinetics of alkaline phosphatase activity and phosphorus availability for phytoplankton and bacterioplankton in lake plusee (north german eutrophic lake). Microbial ecology 13(3), 229–248. Clark, T. L. (1977). A small-scale dynamic model using a terrain-following coordinate transformation. Journal of

Computational Physics 24(2), 186–215. Clark, T. L. and W. D. Hall (1991). Multi-domain simulations of the time dependent navier-stokes equations: Benchmark error analysis of some nesting procedures. Journal of Computational Physics 92(2), 456–481. Cline, J. D. and F. A. Richards (1969). Oxygenation of hydrogen sulfide in seawater at constant salinity, temperature and ph. Environmental Science & Technology 3(9), 838–843. Cloern, J. (1982). Does the benthos control phytoplankton biomass in south san francisco bay? Marine Ecology Progress Series 9, 191–202. Coughlan, J. and A. D. Ansell (1964). A direct method for determining the pumping rate of siphonate bivalves. ICES Journal of Marine Science 29(2), 205–213.

Covar, A. P. (1976). Selecting the proper reaeration coefficient for use in water quality models. In Proceedings of the Conference on Environmental Modeling and Simulation. Cincinnati, OH, EPA-600/9-76-016, Environmental Protection Agency, Washington, DC, pp. 340–3.

Craig, P., D. Chung, N. Lam, P. Son, and N. Tinh (2014). Sigma-zed: A computationally efficient approach to reduce the horizontal gradient error in the efdc’s vertical sigma grid. In Proceedings of the 11th International Conference on Hydrodynamics, Singapore.

Dame, R. F. (1972). The ecological energies of growth, respiration, and assimilation in the intertidal american oyster

crassostrea virginica. Marine Biology 17, 243–250. Deacon, E. and E. Webb (1962). Physical oceanography: Ii. interchange of properties between sea and air. Di Toro, D. and J. Fitzpatrick (1993). Chesapeake bay sediment flux model. final report. Technical report, Hydroqual,

Inc., Mahwah, NJ (United States). Di Toro, D. M. (1980). Applicability of cellular equilibrium and monod theory to phytoplankton growth kinetics. Ecological Modelling 8, 201–218.

###### 247



<<<PAGE 261>>>

###### REFERENCES EFDC+ Theory



Di Toro, D. M. et al. (2001). Sediment flux modeling, Volume 116. Wiley-Interscience New York. Di Toro, D. M., P. R. Paquin, K. Subburamu, and D. A. Gruber (1990). Sediment oxygen demand model: methane

and ammonia oxidation. Journal of Environmental Engineering 116(5), 945–986. Diaz, R. J., R. Rosenberg, et al. (1995). Marine benthic hypoxia: a review of its ecological effects and the behavioural responses of benthic macrofauna. Oceanography and marine biology. An annual review 33, 245–03. Dill, N. (Ed.) (2011, 11). Modeling Hydraulic Control Structures in Estuarine Environments with EFDC. International Conference on Estuarine and Coastal Modeling: The name of the publisher. DiToro, D. and J. Fitzpatrick (1993). Chesapeake bay sediment flux model. prepared for the us army corps of engineer waterways experiment station. vicksburg, ms. Technical report. Doering, P. and C. Oviatt (1986). Application of filtration rate models to field populations of bivalves: an assessment

using experimental mesocosms. Marine Ecology - Progress Series 31, 265–275. DSI (2009, June). Implementation of a Lagrangian Particle Tracking Sub-Model for the EFDC Code (Draft). DSI (2021). EFDC+ propeller wash module white paper. Dunsbergen, D. W. and G. Stelling (1993). A 3d particle model for transport problems in transformed coordinates.

Communications on hydraulic and geotechnical engineering, No. 1993-07. Dwight, H. B. (1947). Tables of integrals and other mathematical data. New York: The MacMillan Company,— c1947, Revised Edition. Edinger, J., D. Brady, and J. Geyer (1974). Heat exchange and transport in the environment. report no. 14. Technical report, Johns Hopkins Univ., Baltimore, MD (USA). Dept. of Geography and.

Edson, J. B., V. Jampana, R. A. Weller, S. P. Bigorre, A. J. Plueddemann, C. W. Fairall, S. D. Miller, L. Mahrt, D. Vickers, and H. Hersbach (2013). On the exchange of momentum over the open ocean. Journal of Physical Oceanography 43(8), 1589–1610.

Engelund, F. and E. Hansen (1967). A Monograph on Sediment Transport in Alluvial Streams. Technical report,

Technical University of Denmark. Fainchtein, R. (2014). Intermediate MPI:Domain Decomposition. MIT Press. Fairall, C., E. Bradley, D. Rogers, J. Edson, and G. Young (1996). The toga coare bulk flux algorithm. J. Geophys.

Res 101, 3747–3764. Fairall, C. W., E. F. Bradley, J. Hare, A. A. Grachev, and J. B. Edson (2003). Bulk parameterization of air–sea fluxes: Updates and verification for the coare algorithm. Journal of climate 16(4), 571–591. Fletcher, C. (1988). AJ. Computational Techniques for Fluid Dynamics. Fundamental and general techniques. Berlin,

Germany: Springer-Verlag, Berlin. Francis, J. (1951). The aerodynamic drag of a free water surface. Froelich, P. N. (1988). Kinetic control of dissolved phosphate in natural rivers and estuaries: a primer on the phosphate

buffer mechanism 1. Limnology and oceanography 33(4part2), 649–668. Fulford, J. M. and T. W. Sturm (1984). Evaporation from flowing channels. Journal of Energy Engineering 110(1), 1–9.

Fulford, R., D. Breitburg, R. E. Newell, W. M. Kemp, and M. Luckenbach (2007). Effects of oyster population restoration strategies on phytoplankton biomass in chesapeake bay: a flexible modeling approach. Marine Ecology Progress Series 336, 43–61.

Galperin, B., L. Kantha, S. Hassid, and A. Rosati (1988). A quasi-equilibrium turbulent energy model for geophysical flows. Journal of the Atmospheric Sciences 45(1), 55–62. Galperin, B. and S. A. Orszag (1993). Large eddy simulation of complex engineering and geophysical flows. Cambridge University Press. Garcia, H. E. and L. I. Gordon (1992). Oxygen solubility in seawater: Better fitting equations. Limnology and Oceanography 37(6), 1307–1312. Garcia, M. and G. Parker (1991). Entrainment of bed sediment into suspension. Journal of Hydraulic Engineer-

ing 117(4), 414–435. Garratt, J. (1977). Review of drag coefficients over oceans and continents. Mon. Weather Rev. 105, 915–929. Genet, L., D. Smith, and M. Sonnen (1974). Computer program documentation for the dynamic estuary model. US

Environmental Protection Agency, Systems Development Branch, Washington, DC.

Gessler, J. (1967). The beginning of bedload movement of mixtures investigated as natural armoring in channels (translated by ea prych, california institute of technology), swiss federal institute of technology, zurich, laboratory of hydraulic research and soil mechanics.

###### 248



<<<PAGE 262>>>

###### REFERENCES EFDC+ Theory



Gibbs, R. J. (1985). Estuarine flocs: their size, settling velocity and density. Journal of Geophysical Research:

Oceans 90(C2), 3249–3251. Giordani, P. and M. Astorri (1986). Phosphate analysis of marine sediments. Chemistry in Ecology 2(2), 103–111. Green, S. (1992). Modeling turbulent air flow in a stand of widely spaced trees. PHOENICS Journal Computational

Fluid Dynamics and its Applications 5, 294–312. Gropp, W., T. Hoefler, R. Thakur, and E. Lusk (2014). Using advanced MPI: Modern features of the message-passing interface. MIT Press. Gulliver, J. S. and H. G. Stefan (1984). Stream productivity analysis with dorm—i: Development of computational model. Water Research 18(12), 1569–1576. Guy, H. P., D. B. Simons, and E. V. Richardson (1966). Summary of alluvial channel data from flume experiments,

1956-61, Volume 462. US Government Printing Office. Hageman, L. and M. Young (1981). Applied iterative methods academic. New York. Haltiner, G. J. and R. T. Williams (1980). Numerical prediction and dynamic meteorology. Technical report. Hamill, G. A. and C. Kee (2016). Predicting axial velocity profiles within a diffusing marine propeller jet. Ocean

Engineering 124, 69–88.

Hamrick, J. and T. Wu (1997). Computational design and optimization of the efdc/hem3d surface water hydrodynamic and eutrophication models. In Next generation environmental models and computational methods, pp. 143–161. Society for Industrial and Applied Mathematics Pennsylvania.

Hamrick, J. M. (1986). Long-term dispersion in unsteady skewed free surface flow. Estuarine, Coastal and Shelf Science 23(6), 807–845. Hamrick, J. M. (1992). A three-dimensional environmental fluid dynamics computer code: Theoretical and computational aspects. Technical report, Virginia Institute of Marine Science, College of William and Mary. Hamrick, J. M. (1996). User’s manual for the environmental fluid dynamics computer code. Special Reports in Applied

Marine Science and Ocean Engineering (SRAMSOE) No. 33. Hamrick, J. M. (2006). A generic rooted aquatic plant and epiphyte algae sub-model for EFDC. Harbeck Jr, G. (1964). Estimating forced evaporation from cooling ponds. J. Power Div., Am. Soc. Civ. Eng.;(United

States) 90. Heaps, N. (1965). Storm surges on a continental shelf. Hersbach, H. (2011). Sea surface roughness and drag coefficient as functions of neutral wind speed. Journal of

Physical Oceanography 41(1), 247–251. Hofmann, E., E. Powell, J. Klinck, and E. Wilson (1992). Modeling oyster populations iii. critical feeding periods, growth and reproduction. Shellfish Res. 11(2), 399––416. Hunt, J. N. (1979). Direct solution of wave dispersion equation. Journal of the Waterway, Port, Coastal and Ocean Division 105(4), 457–459. Huu Chung, D. and D. P. Eppel (2008). Effects of some parameters on numerical simulation of coastal bed morphology. International Journal of Numerical Methods for Heat & Fluid Flow 18(5), 575–592. Hwang, K.-N. and A. J. Mehta (1989). Fine sediment erodibility in Lake Okeechobee, Florida. Coastal & Oceanographic Engineering Department, University of Florida. James, S. C., E. Seetho, C. Jones, and J. Roberts (2010). Simulating environmental changes due to marine hydrokinetic

energy installations. In OCEANS 2010 MTS/IEEE SEATTLE, pp. 1–10. IEEE. Jerlov, N. G. (1968). Optical oceanography. Elsevier Pub. Co. OCLC: 316568666. Ji, Z. (2008). Hydrodynamics and water quality: modeling rivers, lakes, and estuaries. John Wiley & Sons. Jones, C. and W. Lick (2000). Effects of bed coarsening on sediment transport. In Estuarine and Coastal Modeling,

pp. 915–930. ASCE. Jones, C. and W. Lick (2001). SEDZLJ: A sediment transport model. Final Report. University of California, Santa Barbara, California. Jordan, S. (1987). Sedimentation and Remineralization Associated with Biodeposition by the American Oyster Crassostrea Virginica (Gmelin). University of Maryland, College Park. Kantha, L. H. (2003, September). On an Improved Model for the Turbulent PBL. Journal of the Atmospheric Sciences 60(17), 2239–2246. Kantha, L. H. and C. A. Clayson (1994). An improved mixed layer model for geophysical applications. Journal of Geophysical Research: Oceans 99(C12), 25235–25266. Katul, G. G., L. Mahrt, D. Poggi, and C. Sanz (2004). One-and two-equation models for canopy turbulence. BoundaryLayer Meteorology 113(1), 81–109.

###### 249



<<<PAGE 263>>>

###### REFERENCES EFDC+ Theory



Kee, C., G. A. Hamill, W. H. Lam, and P. W. Wilson (2006). Investigation of the velocity distributions within a ship’s propeller wash. In The 16th International Offshore and Polar Engineering Conference, San Francisco, CA, pp. 451–456.

Kim, J., J. Jones, and D. Seo (2021). Factors affecting harmful algal bloom occurrence in a river with regulated hydrology. Journal of Hydrology: Regional Studies 33, 100769. Kim, J. and D. Seo (2024). Three-dimensional augmentation for hyperspectral image data of water quality: An integrated approach using machine learning and numerical models. Water Research 251, 121125. Kim, J., D. Seo, M. Jang, and J. Kim (2021). Augmentation of limited input data using an artificial neural network method to improve the accuracy of water quality modeling in a large lake. Journal of Hydrology 602, 126817. Kim, J., D. Seo, and J. Jones (2022). Harmful algal bloom dynamics in a tidal river influenced by hydraulic control structures. Ecological Modelling 467, 109931. Kim, J. H. (2019). Ecological indices-based modelling of oyster aquaculture sustainability. Ph. D. thesis, Pukyong National University, Republic of Korea. Kim, T.-H., C.-S. Yang, J.-H. Oh, and K. Ouchi (2014). Analysis of the contribution of wind drift factor to oil slick movement under strong tidal condition: Hebei spirit oil spill case. PloS one 9(1), e87393. Kobayashi, M., E. Hofmann, E. Powell, J.M.Klinck, and K. Kusaka (1997). A population dynamics model for the japanese oyster, crassostrea gigas. Aquaculture 149(3–4), 285–321. Kraus, E. B. and J. A. Businger (1994). Atmosphere-ocean interaction (2nd ed ed.). Number no. 27 in Oxford

monographs on geology and geophysics. Oxford University Press ; Clarendon Press. Kremer, J. and S. Nixon (1978). A coastal marine ecosystem, 217 pp. Kromkamp, J. C. and L. R. Mur (1984, 11). Buoyant density changes in the cyanobacterium Microcystis aeruginosa

due to changes in the cellular carbohydrate content. FEMS Microbiology Letters 25(1), 105–109. Krone, R. B. (1962). Flume studies of transport of sediment in estrarial shoaling processes. Final Report, Hydr. Engr.

and Samitary Engr. Res. Lab., Univ. of California. Large, W. and S. Pond (1981). Open ocean momentum flux measurements in moderate to strong winds. Laursen, E. M. (1958). The total sediment load of streams. Journal of the Hydraulics Division 84(1), 1–36. Lee, J. H. and V. Cheung (1990). Generalized lagrangian model for buoyant jets in current. Journal of environmental

engineering 116(6), 1085–1106. Leinonen, P. and D. Mackay (1975). A mathematical model of evaporation and dissolution from oil spills on ice, land, water and under ice. Water Quality Research Journal 10(1), 132–141. Lick, W. and J. Lick (1988). Aggregation and disaggregation of fine-grained lake sediments. Journal of Great Lakes Research 14(4), 514–523. Lijklema, L. (1980). Interaction of orthophosphate with iron (iii) and aluminum hydroxides. Environmental Science & Technology 14(5), 537–541. Liu, J., J. Chen, T. Black, and M. Novak (1996). E-ε modelling of turbulent air flow downwind of a model forest edge. Boundary-Layer Meteorology 77(1), 21–44. Longuet-Higgins, M. S. and R. Stewart (1964). Radiation stresses in water waves; a physical discussion, with appli-

cations. In Deep Sea Research and Oceanographic Abstracts, Volume 11, pp. 529–562. Elsevier. Loosanoff, V. (1958). Some aspects of behavior of oysters at different temperatures. Biol. Bull. 114, 57–70. Loosanoff, V. and F. Tommers (1948). Effect of suspended silt and other substances on rate of feeding of oysters.

Science 107(2768), 69–70. Mackay, D. and A. T. Yeun (1983). Mass transfer coefficient correlations for volatilization of organic solutes from water. Environmental Science & Technology 17(4), 211–217. Madala, R. V. and S. A. Piacseki (1977). A semi-implicit numerical model for baroclinic oceans. Journal of Computational Physics 23(2), 167–178.

Madden, C. J., A. A. McDonald, and D. Gruber (2018). Florida bay seacom: Seagrass ecological assessment and community organization model documentation v. 15.1b. Technical report, South Florida Water Management District Technical Publication, Everglades Systems Assessment Division.

Mancini, J. L. (1983). A method for calculating effects, on aquatic organisms, of time varying concentrations. Water Research 17(10), 1355–1362.

Mann, R., E. M. Burreson, and P. K. Baker (1991). The decline of the virginia oyster fishery in chesapeake bay considerations for introduction of a non-endemic species, crassostrea gigas (thunberg, 1793). Journal of Shellfish Research 10(2), 379–388.

Matisoff, G. (1982). Mathematical models of bioturbation. In Animal-sediment relations, pp. 289–330. Springer.

###### 250



<<<PAGE 264>>>

###### REFERENCES EFDC+ Theory



McIntire, C. D. (1973). Diatom associations in yaquina estuary, oregon: A multivariate analysis 1. Journal of Phycology 9(3), 254–259. Mehta, A. J., E. J. Hayter, W. R. Parker, R. B. Krone, and A. M. Teeter (1989). Cohesive sediment transport. i: Process description. Journal of Hydraulic Engineering 115(8), 1076–1093. Mellor, G. L. (1991). An equation of state for numerical models of oceans and estuaries. Journal of Atmospheric and Oceanic Technology 8(4), 609–611. Mellor, G. L. and A. F. Blumberg (1985). Modeling vertical and horizontal diffusivities with the sigma coordinate system. Monthly Weather Review 113(8), 1379–1383. Mellor, G. L., T. Ezer, and L.-Y. Oey (1994). The pressure gradient conundrum of sigma coordinate ocean models. Journal of atmospheric and oceanic technology 11(4), 1126–1134. Mellor, G. L. and T. Yamada (1982). Development of a turbulence closure model for geophysical fluid problems. Reviews of Geophysics 20(4), 851–875. Mengguo, L. and Q. Chongren (2003). Numerical simulation of wave-induced nearshore current. In Proceedings of the International Conference on Estuaries and Coasts. Citeseer. Meyer-Peter, E. and R. M¨uller (1948). Formulas for bed-load transport. In IAHSR 2nd meeting, Stockholm, appendix

2. IAHR. Meyers, J. and P. Sagaut (2006). On the model coefficients for the standard and the variational multi-scale smagorinsky model. 569, 287. Millero, F. J. (1986). The thermodynamics and kinetics of the hydrogen sulfide system in natural waters. Marine

Chemistry 18(2-4), 121–147. Morel, F. M. (1983). Principles of aquatic chemistry. John Wiley and Sons, New York NY. 1983. 446. Morse, J. W., F. J. Millero, J. C. Cornwell, and D. Rickard (1987). The chemistry of the hydrogen sulfide and iron

sulfide systems in natural waters. Earth-science reviews 24(1), 1–42. Nezu, I. (1993). Turbulence in open-channel flows. IAHR-monograph. O’Connor, D. J. and W. E. Dobbins (1958). Mechanism of reaeration in natural streams. Transactions of the American

Society of Civil Engineers 123(1), 641–666. Odum, E. P. (1971). Fundamentals of ecology–wb saunders company. Philadelphia, London, Toronto. Officer, C. B., T. J. Smayda, and R. Mann (1982). Benthic filter feeding: A natural eutrophication control. Marine

Ecology - Progress Series 9, 203–210. Overman, C. and S. Wells (2022). Modeling cyanobacteria vertical migration. Water 14(6). Park, K., A. Y. Kuo, J. Shen, and J. M. Hamrick (1995). A three-dimensional hydrodynamic-eutrophication model

(hem-3d): Description of water quality and sediment process submodels. Technical report, Virginia Institute of Marine Science.

Parker, G., C. Paola, and S. Leclair (2000). Probabilistic exner sediment continuity equation for mixtures with no active layer. Journal of Hydraulic Engineering 126(11), 818–826. Paulson, C. A. and J. J. Simpson (1977). Irradiance measurements in the upper ocean. Journal of Physical Oceanog-

raphy 7(6), 952 – 956. Peyret, R. and T. Taylor (1983). Computational Methods for Fluid Flow. Springer-Verlag. Pfeifer, R. and W. McDiffett (1975). Some factors affecting primary productivity of stream riffle communities. Archiv

Fur Hydrobiologie. Poggi, D., A. Porporato, L. Ridolfi, J. Albertson, and G. Katul (2004). The effect of vegetation density on canopy sub-layer turbulence. Boundary-Layer Meteorology 111(3), 565–587. Powell, E., J. Klinck, E. Hofmann, and S. Ray (1994, 01). Modeling oyster populations. iv: Rates of mortality, population crashes, and management. Fishery Bulletin 92. Press, W., B. Flannery, S. Teukolsky, W. Vetterling, and J. Chipperfield (1986). Numerical recipes: the art of scientific

computing. Cambridge University Press. Quayle, D. (1988). Pacific oyster culture in British Columbia. Department of Fisheries and Oceans. Redfield, A. C. (1963). The influence of organisms on the composition of seawater. The sea 2, 26–77. Robbins, J., T. Keilty, D. White, and D. Edgington (1989). Relationships among tubificid abundances, sediment

composition, and accumulation rates in lake erie. Canadian Journal of Fisheries and Aquatic Sciences 46(2), 223–231.

Roberts, J., R. Jepsen, D. Gotthard, and W. Lick (1998). Effects of particle size and bulk density on erosion of quartz particles. Journal of Hydraulic Engineering 124(12), 1261–1267.

###### 251



<<<PAGE 265>>>

###### REFERENCES EFDC+ Theory



Rosati, A. and K. Miyakoda (1988). A general circulation model for upper ocean simulation. Journal of Physical Oceanography 18(11), 1601–1626. Ross, M. J. and G. R. Ultsch (1980). Temperature and substrate influences on habitat selection in two pleurocerid snails (goniobasis). American Midland Naturalist, 209–217. Runke, H. (1985). Simulation of the lotic periphyton community of a small mountain stream by digital computer. Ph. D. thesis, Thesis presented to Utah State University, Logan, Utah, in partial fulfill. Sanford, L. P. and J. P.-Y. Maa (2001). A unified erosion formulation for fine sediments. Marine Geology 179(1-2), 9–23. Sanz, C. (2003). A note on k-ε modelling of vegetation canopy air-flows. Boundary-Layer Meteorology 108(1),

191–197. Semtner Jr, A. (1974). An oceanic general circulation model with bottom topography. Technical report. Seo, D. (2019). Personal communication. Sheppard, P. (1958). Transfer across the earth’s surface and through the air above. Shields, A. (1936). Application of similarity principles and turbulence research to bed-load movement. Technical

report. Shiferaw, N., J. Kim, and D. Seo (2022). Identification of pollutant sources and evaluation of water quality improvement alternatives of a large river. Environmental Science and Pollution Research 30, 31546–31560. Shrestha, P. L. and G. T. Orlob (1996). Multiphase distribution of cohesive sediments and heavy metals in estuarine systems. Journal of Environmental Engineering 122(8), 730–740. Shumway, S. and R. Koehn (1982). Oxygen consumption in the american oyster crassostrea virginica. Marine Ecology

- Progress Series 9(1), 59–68. Simons, T. J. et al. (1973). Development of three-dimensional numerical models of the great lakes. In IWD Scientific Series, Volume 12. Inland Waters Directorate. Smagorinsky, J. (1963). General circulation experiments with the primitive equations: I. the basic experiment. Monthly weather review 91(3), 99–164. Smith, J. D. and S. McLean (1977). Spatially averaged flow over a wavy surface. Journal of Geophysical Research 82(12), 1735–1746. Smith, S. and E. Banke (1975). Variation of the sea surface drag coefficient with wind speed. Q. J. R. Meteorol. Soc. 101, 665––673. Smolarkiewicz, P. K. and T. L. Clark (1986). The multidimensional positive definite advection transport algorithm: Further development and applications. Journal of Computational Physics 67(2), 396–438. Smolarkiewicz, P. K. and W. W. Grabowski (1990). The multidimensional positive definite advection transport algorithm: Nonoscillatory option. Journal of Computational Physics 86(2), 355–375.

Soulsby, R., R. Whitehouse, et al. (1997). Threshold of sediment motion in coastal environments. In Pacific Coasts and Ports’ 97: Proceedings of the 13th Australasian Coastal and Ocean Engineering Conference and the 6th Australasian Port and Harbour Conference; Volume 1, pp. 145. Centre for Advanced Engineering, University of Canterbury.

Steele, J. H. (1962). Environmental control of photosynthesis in the sea. Limnology and oceanography 7(2), 137–150. Stewart, P. S., D. J. Tedaldi, A. R. Lewis, and E. Goldman (1993). Biodegradation rates of crude oil in seawater. Water

environment research 65(7), 845–848. Stiver, W. and D. Mackay (1984). Evaporation rate of spills of hydrocarbons and petroleum mixtures. Environmental Science & Technology 18(11), 834–840. Stuart Churchill, H. C. (1975). Correlating equations for laminar and turbulent free convection from a vertical plate. International Journal of Heat and Mass Transfer 18(11), 1323–1329. Stumm, W., J. J. Morgan, et al. (1970). Aquatic chemistry; an introduction emphasizing chemical equilibria in natural waters. Wiley-Interscience. SWAN Team (2019). Implementation Manual Swan Cycle III (41.31 ed.). Delft University of Technology, Department

of Civil Engineering. Swart, D. H. (1974). Offshore sediment transport and equilibrium beach profiles. Tetra Tech (2002a). Theoretical and computational aspects of sediment and contaminant transport in the efdc model.

Technical report, US Environmental Protection Agency. Tetra Tech (2002b). User’s Manual for Environmental Fluid Dynamics Code. Tetra Tech, Inc 1.

- Tetra Tech (2007a). The environmental fluid dynamics code theory and computation volume 2: Sediment and contaminant transport and fate.


###### 252



<<<PAGE 266>>>

###### REFERENCES EFDC+ Theory



- Tetra Tech (2007b). The environmental fluid dynamics code theory and computation volume 3: Water quality module. Technical report, Tetra Tech, Inc., Fairfax, VA.


Thanh, P. H. X., M. D. Grace, and S. C. James (2008). Sandia National Laboratories Environmental Fluid Dynamics Code: Sediment Transport User Manual. Technical Report SAND2008-5621, Sandia National Laboratories. Thomann, R. V. and J. A. Mueller (1987). Principles of surface water quality modeling and control. Harper & Row Publishers.

Tillman, D. H., C. F. Cerco, M. R. Noel, J. L. Martin, and J. Hamrick (2004). Three-dimensional eutrophication model of the lower st. john river, florida. Technical report, Engineer Research And Development Center Vicksburg Ms Environmental Lab.

Troup, B. N. (1974). The interaction of iron with phosphate, carbonate and sulfide in Chesapeake Bay interstitial waters: A thermodynamic interpretation. Ph. D. thesis, Johns Hopkins University. Tsai, C., S. Iacobellis, and W. Lick (1987). Flocculation of fine-grained lake sediments due to a uniform shear stress. Journal of Great Lakes Research 13(2), 135–146.

UNESCO (1981). Background papers and supporting data on the international equation of state of seawater 1980, Volume 38. Joint Panel on Oceanographic Tables and Standards and Centre interuniversitaire d’´etudes europ´eennes and International Council of Scientific Unions. Scientific Committee on Oceanic Research and International Association for the Physical Sciences of the Ocean.

van Niekerk, A., K. R. Vogel, R. L. Slingerland, and J. S. Bridge (1992). Routing of heterogeneous sediments over movable bed: Model development. Journal of Hydraulic Engineering 118(2), 246–262. van Rijn, L. C. (1984). Sediment transport, part ii: suspended load transport. Journal of hydraulic engineering 110(11),

1613–1641. Villemonte, J. R. (1947). Submerged weir discharge studies. Engineering News-Record 139(26), 54–56. Vinokur, M. (1974). Conservation equations of gasdynamics in curvilinear coordinate systems. Journal of Computa-

tional Physics 14(2), 105–125. Visser, P., J. Passarge, and L. Mur (1997, 08). Visser pm, passarge j, mur lr.. modelling vertical migration of the cyanobacterium microcystis. hydrobiologia 349: 99-109. Hydrobiologia 349, 99–109. Ward, G. H. (1980). Hydrography and circulation processes of gulf estuaries. In Estuarine and Wetland Processes, pp. 183–215. Springer. Warwick, J., D. Cockrum, and M. Horvath (1997). Estimating non-point-source loads and associated water quality impacts. Journal of Water Resources Planning and Management 123(5), 302–310. Webster, I. T. and B. S. Sherman (1995). Evaporation from fetch-limited water bodies. Irrigation Science 16(2), 53–64. Wells, S. A. and T. M. Cole (2000). Ce-qual-w2, version 3. Technical report, Army Engineer Waterways Experiment Station Vicksburg Ms Engineer Research. Westrich, J. T. and R. A. Berner (1984). The role of sedimentary organic matter in bacterial sulfate reduction: The g model tested 1. Limnology and oceanography 29(2), 236–249. Wezenak, C. T. and J. J. Gannon (1968). Evaluation of nitrification in streams. Journal of the Sanitary Engineering Division 94(5), 883–896. White, M., E. Powell, and S. Ray (1988). Effect of parasitism by the pyramidellid gastropod boonea impressa on the net productivity of oysters (crassostrea virginica. Estuarine, Coastal and Shelf Science 26(4), 359 – 377. Whitford, L. and G. Schumacher (1964). Effect of a current on respiration and mineral uptake in spirogyra and oedogonium. Ecology 45(1), 168–170. Whitman, W., R. Russell, C. Welling, and J. Cochrane (1923). The effect of velocity on the corrosion of steel in sulfuric acid. Industrial & Engineering Chemistry 15(7), 672–677. Wilson, B. (1960). Note on surface wind stress over water at low and high wind speeds. J. Geophys. Res. 65, 3377–3382.

Wilson, J. D., J. J. Finnigan, and M. R. Raupach (1998). A first-order closure for diturbed plant-canopy flows, and its application to winds in a canopy on a ridge. Quarterly Journal of the Royal Meteorological Society 124(547), 705–732.

Winiarski, L. D. and W. F. Frick (1976). Cooling tower plume model. US Environmental Protection Agency, Office of Research and Development. Wu, J. (1982). Wind stress coefficients over sea surface from breeze to hurricane. J. Geophys. Res. Oceans 87, 9704–9706.

###### 253



<<<PAGE 267>>>

###### REFERENCES EFDC+ Theory



Wu, W., S. S. Wang, and Y. Jia (2000). Nonuniform sediment transport in alluvial rivers. Journal of hydraulic

research 38(6), 427–434. Xiao, H. and P. Cinnella (2019). Quantification of model uncertainty in RANS simulations: A review. 108, 1–31. Yamamoto, S., J. B. Alcauskas, and T. E. Crozier (1976). Solubility of methane in distilled water and seawater. Journal

of Chemical and Engineering Data 21(1), 78–80. Yang, C. T. (1973). Incipient motion and sediment transport. Journal of the hydraulics division 99(10), 1679–1704. Yang, C. T. and A. Molinas (1982). Sediment transport and unit stream power function. Journal of the Hydraulics

Division 108(6), 774–793. Yelland, M., B. Moat, P. Taylor, R. Pascal, J. Hutchings, and V. Cornell (1998). Wind stress measurements from the open ocean corrected for airflow distortion by the ship.

Yelland, M. and P. Taylor (1996). Wind stress measurements from the open ocean. J. Phys. Oceanogr. 26(4), 541–558. Ziegler, C. K. and W. Lick (1988). The transport of fine-grained sediments in shallow waters. Environmental Geology

and Water Sciences 11(1), 123–132.

Ziegler, C. K. and W. J. Lick (1986). A numerical model of the resuspension, deposition and transport of fine-grained sediments in shallow water. Department of Mechanical & Environmental Engineering, University of California. Ziegler, C. K. and B. Nisbet (1994). Fine-grained sediment transport in pawtuxet river, rhode island. Journal of

Hydraulic Engineering 120(5), 561–576. Ziegler, C. K. and B. S. Nisbet (1995). Long-term simulation of fine-grained sediment transport in large reservoir. Journal of Hydraulic Engineering 121(11), 773–781.

Zison, S. (1978). Rates, Constants, and Kinetics Formulations in Surface Water Quality Modeling. Ecological research series. Environmental Protection Agency, Office of Research and Development, Environmental Research Laboratory.

###### 254



