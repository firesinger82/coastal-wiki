<<<PAGE 1>>>

# EFDC+ Propeller Wash Module White Paper

August 17, 2021

DSI, LLC Edmonds, WA USA www.ds-intl.biz

<<<PAGE 2>>>

##### This page left intentionally blank.

<<<PAGE 3>>>

# Abstract

DSI, LLC has developed a numerical algorithm for propeller wash modeling to simulate ﬂow and sediment transport patterns due to ship trafﬁc in urban waterfronts, integrating this algorithm into Environmental Fluid Dynamics Code Plus (EFDC+). This method computes propeller wash velocity proﬁles for each ship based on Hamill’s approaches (Hamill, 1987; Hamill and Kee, 2016; Hamill et al., 2015) and other empirical equations (Fuehrer and R¨omisch, 1977; Hashmi et al., 2007; Lam et al., 2011; Maynord, 2000; Stewart, 1992; Toutant, 1982). Using these velocity proﬁles, the resultant shear stress at the water-sediment interface is calculated using the Maynord (2000) method. Given the bottom shear stress, sediment transport processes due to the propeller wash are then computed following either van Rijn’s sediment transport equations (Van Rijn, 1984a,b,c) or the Sediment Dynamics Algorithms developed by Ziegler, Lick, and Jones (SEDZLJ) (Jones and Lick, 2001). These propeller wash results are fully coupled to the three-dimensional hydrodynamic and sediment transport computation in EFDC+. As a result, EFDC+ propeller wash models can dynamically simulate combinations of propeller wash-induced processes, such as sediment resuspension and bed scour due to ship movement, subsequent transport behaviors in the water column (e.g., advection, diffusion, settling), and redeposition in the sediment bed.

Several case studies, including a ﬂume experiment (Hong et al., 2016), a San Diego Bay ﬁeld test (Wang et al., 2016), and Washington State ferry operations (Kastner et al., 2019), demonstrated that the EFDC+ model can reasonably reproduce observed propeller wash data (i.e., ﬂow velocity, shear stress, and erosion depth). Other case studies presented here also conﬁrmed that the EFDC+ propeller wash approach works correctly with van Rijn’s sediment transport theories (Van Rijn, 1984a,b,c) and SEDZLJ method (Jones and Lick, 2001). Based on these ﬁndings, it can be concluded that the EFDC+ model provides a reliable representation of the sediment transport processes induced by propeller wash, including scour, bedload, sediment resuspension, and movements of the resuspended sediments under various conditions. The EFDC+ propeller wash modeling approach will be beneﬁcial for researchers, engineers, and regulators in their efforts to properly evaluate propeller wash effects for contaminant remediation planning, scour mitigation, and structure design.

<<<PAGE 4>>>

# Contents

List of Figures iii List of Tables v List of Abbreviations vi

- 1 Introduction 1-1

- 1.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1-1
- 1.2 Objective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1-2


- 2 Theoretical Approach 2-1

- 2.1 Efﬂux Zone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2-3
- 2.2 Zone of Flow Establishment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2-4
- 2.3 Zone of Established Flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2-5
- 2.4 Computation of Velocity at Water-Sediment Interface . . . . . . . . . . . . . . . . 2-6


- 3 EFDC+ Algorithm Implementation 3-1
- 4 EFDC+ Input Requirements 4-1

- 4.1 efdc.inp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4-1
- 4.2 propwash conﬁg.jnp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4-2

- 4.3 propwash ships.jnp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4-3

- 4.4 propwash tracks.jnp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4-5

- 4.5 Data Input Guidelines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4-8


- 4.5.1 Ship Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4-8
- 4.5.2 Propeller Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .4-15
- 4.5.3 Applied Power for Tracking Data . . . . . . . . . . . . . . . . . . . . . . .4-16


- 5 Case Studies 5-1


- 5.1 Validation Using Flume Experiment Data . . . . . . . . . . . . . . . . . . . . . . 5-1
- 5.2 Validation Using San Diego Bay Field Data . . . . . . . . . . . . . . . . . . . . . 5-3

- 5.2.1 Near-bed Flow Velocity . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5-5
- 5.2.2 Bottom Shear Stress . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5-7
- 5.2.3 Erosion Depth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5-9


- 5.3 Demonstration of Sediment Transport Processes . . . . . . . . . . . . . . . . . . .5-12


- 5.3.1 Original EFDC Sediment Transport Module . . . . . . . . . . . . . . . . .5-14
- 5.3.2 SEDZLJ Sediment Transport Module . . . . . . . . . . . . . . . . . . . .5-22


##### DSI, LLC i EFDC+ Propeller Wash



<<<PAGE 5>>>

CONTENTS

- 5.4 Demonstration of Sediment Resuspension . . . . . . . . . . . . . . . . . . . . . .5-27

- 5.4.1 Long Straight Channel with Two Moving Ships . . . . . . . . . . . . . . .5-27
- 5.4.2 San Diego Bay Tugboat Test Site . . . . . . . . . . . . . . . . . . . . . . .5-31


- 5.5 Application to Kingston Ferry Terminal . . . . . . . . . . . . . . . . . . . . . . .5-33


- 5.5.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5-33
- 5.5.2 Model Development . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5-35
- 5.5.3 Model Results and Discussion . . . . . . . . . . . . . . . . . . . . . . . .5-37


#### References

##### DSI, LLC ii EFDC+ Propeller Wash



<<<PAGE 6>>>

# List of Figures

- 1.1 Schematic diagram of propeller wash-induced sediment transport processes. . . . . 1-2
- 1.2 Deﬁnition for key ship properties (side view). The ship image is adapted from

- Damen Shipyards (2021). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1-4

1.3 Deﬁnition for key ship properties (back view). The ship image is adapted from

- Damen Shipyards (2021). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1-5




- 2.1 Adopted formulations for the three propeller wash zones in EFDC+. . . . . . . . . 2-2
- 3.1 Flow chart of the EFDC+ propeller wash computation process. . . . . . . . . . . . 3-2

- 3.2 Hydrodynamic velocity ﬁeld for model grid cells and speciﬁcation of ship position based on a ship path (plan view). . . . . . . . . . . . . . . . . . . . . . . . . . . . 3-3
- 3.3 Generation of sub-grid mesh behind ship and determination of bottom elevation for each sub-grid point (plan view). . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3-4
- 3.4 Sub-grid points for velocity computation at water-sediment bed interface (side view). 3-5
- 3.5 Superposition of propeller wash velocities for a two-propeller ship (back view). . . 3-5
- 3.6 Propeller wash velocities at sub-grid points and ambient current velocity vectors for model grid cells (plan view). . . . . . . . . . . . . . . . . . . . . . . . . . . . 3-6
- 3.7 Shear stress or erosion rate induced by propeller wash at sub-grid points (plan view). 3-7
- 3.8 Sub-grid points, sub-grid area, and model grid cells for propeller wash-induced erosion mass calculation (plan view). . . . . . . . . . . . . . . . . . . . . . . . . . 3-8
- 3.9 Conceptual diagram for EFDC+ sediment transport processes (side view). . . . . . 3-9
- 3.10 Diagrams for propeller wash-induced momentum (a) coupling with a model grid cell and (b) splitting over vertical water layers. . . . . . . . . . . . . . . . . . . . .3-11
- 3.11 Example of a moving ship with a sub-grid mesh at time step ti+1 (plan view). . . .3-12
- 3.12 Example of a moving ship with a sub-grid mesh at time step ti+2 (plan view). . . .3-13
- 3.13 Example of a moving ship with a sub-grid mesh at time step ti+3 (plan view). . . .3-13


- 4.1 Example of the propwash tracks.jnp ﬁle format. . . . . . . . . . . . . . . . . . . . 4-6


- 4.2 Length and draft of fully loaded ships according to PIANC (2015) data. . . . . . . 4-9
- 4.3 Hull depth and draft of fully loaded ships according to PIANC (2015) data. . . . .4-10
- 4.4 Propeller offset parameter for distance from the hull bottom to the propeller shaft. .4-11
- 4.5 Length and deadweight tonnage based on PIANC (2015) data. . . . . . . . . . . .4-13
- 4.6 Installed engine power as a function of deadweight tonnage per PIANC (2015) data.4-13
- 4.7 Installed engine power as a function of ship beam per TugboatInformation.com


(2021) data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .4-14

##### DSI, LLC iii EFDC+ Propeller Wash



<<<PAGE 7>>>

LIST OF FIGURES

- 5.1 Velocity proﬁles from EFDC+ propeller wash computations compared to Hong et al. (2016) experiment data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5-2
- 5.2 Conﬁguration of tugboat propeller wash measurements. . . . . . . . . . . . . . . . 5-4
- 5.3 EFDC+ model conditions for the San Diego Bay ﬁeld test case. . . . . . . . . . . . 5-5
- 5.4 Propeller wash velocity from ADV-measured data and EFDC+ model results at 110 m behind tugboat Tractor C-14. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5-6
- 5.5 Propeller wash shear stress from modiﬁed TKE method-based data and EFDC+ model results at 110 m behind tugboat Tractor C-14. . . . . . . . . . . . . . . . . . 5-8
- 5.6 Erosion depth from PIV-measured data and EFDC+ model results at 110 m behind tugboat Tractor C-14. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5-10
- 5.7 Channel dimensions used for sediment transport demonstration models. . . . . . .5-13
- 5.8 Plan view of bottom elevations simulated from a cohesive sediment bed model. . .5-15
- 5.9 Scour proﬁles at different times from the cohesive sediment bed simulation. . . . .5-15
- 5.10 Time series of bed layer thickness at the maximum scour cell from the cohesive sediment bed simulation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5-16
- 5.11 Plan view of bottom elevations simulated from a non-cohesive sediment bed model.5-18
- 5.12 Scour proﬁles at different times from the non-cohesive sediment bed simulation. . .5-19
- 5.13 Scour proﬁles of non-cohesive sediment bed simulated by different propeller powers.5-20
- 5.14 Scour proﬁles of non-cohesive sediment bed simulated by different particle sizes. .5-21
- 5.15 Plan view of bottom elevations simulated from a SEDZLJ sediment transport model.5-23
- 5.16 Scour proﬁles at different times from the SEDZLJ sediment transport simulation. .5-23
- 5.17 Time series of sediment bed layer thickness at the maximum scour cell from the SEDZLJ sediment transport simulation. . . . . . . . . . . . . . . . . . . . . . . .5-25
- 5.18 TSS concentrations and velocity ﬁeld from a straight channel simulation without

- propeller momentum effects. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5-29

5.19 TSS concentrations and velocity ﬁeld from a straight channel simulation including

- propeller momentum effects. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5-30


- 5.20 TSS concentrations and velocity ﬁeld from San Diego Bay tugboat simulations without vs. with propeller momentum. . . . . . . . . . . . . . . . . . . . . . . . .5-32
- 5.21 Aerial image of Kingston ferry terminal, AIS-tracked ship paths for three ferries on March 18, 2018, with ADV sensor location diagram (after Kastner et al., 2019). 5-34
- 5.22 Side view of M/V Puyallup. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5-35
- 5.23 EFDC+ model conditions for the Kingston ferry terminal case. . . . . . . . . . . .5-36
- 5.24 Near-bed ﬂow velocity due to M/V Walla Walla at 10:26 on March 18th, 2018. . . .5-38
- 5.25 ADV data and EFDC+ model results for near-bed ﬂow velocity at the south piling. .5-38
- 5.26 Simulated depth-averaged ﬂow velocity ﬁeld due to departure of M/V Walla Walla at 10:28 on March 18th, 2018. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5-39
- 5.27 Simulated bottom shear stress at north and south pilings, tide data, and critical shear stress ranges for each sediment size classiﬁcation. . . . . . . . . . . . . . . .5-40


##### DSI, LLC iv EFDC+ Propeller Wash



<<<PAGE 8>>>

# List of Tables

- 4.1 Propeller wash module control ﬁelds in efdc.inp ﬁle. . . . . . . . . . . . . . . . . . 4-1
- 4.2 Propeller wash conﬁguration parameters in propwash conﬁg.jnp ﬁle. . . . . . . . . 4-2

- 4.3 Ship and propeller speciﬁcation parameters in propwash ships.jnp ﬁle. . . . . . . . 4-4

- 4.4 Ship track data ﬁelds in the propwash tracks.jnp ﬁle. . . . . . . . . . . . . . . . . 4-6

- 4.5 Ship status code descriptions for parameter “n”. . . . . . . . . . . . . . . . . . . . 4-7
- 4.6 Characteristics of self-propelled oil tankers per NYSDOT (2005). . . . . . . . . . . 4-9


- 5.1 Modeled propeller properties used for the Hong et al. (2016) experiment case. . . . 5-2
- 5.2 Tugboat Tractor C-14 information and ﬁeld study conditions. . . . . . . . . . . . . 5-4
- 5.3 Propeller speciﬁcations used for the sediment transport demonstration models. . . .5-13
- 5.4 Sediment mass distributions at the beginning and end of the cohesive sediment bed simulation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5-17
- 5.5 Sediment mass distributions at the beginning and end of the SEDZLJ sediment transport simulation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5-25
- 5.6 Properties of Tractor C-13 and Tractor C-14. . . . . . . . . . . . . . . . . . . . . .5-27
- 5.7 Ship and propeller characteristics of three ferries on the Kingston-Edmonds route. .5-34


##### DSI, LLC v EFDC+ Propeller Wash



<<<PAGE 9>>>

# List of Abbreviations

- 2D two-dimensional
- 3D three-dimensional


ADV Acoustic Doppler Velocimeter ADVP Acoustic Doppler Velocity Proﬁler AIS Automatic Identiﬁcation System

CRADA Cooperative Research and Development Agreement

DEM Digital Elevation Model DSI DSI, LLC

EEMS EFDC Explorer Modeling System EFDC Environmental Fluid Dynamics Code EFDC+ Environmental Fluid Dynamics Code Plus

GUI Graphic User Interface

hp horsepower

M/V Motor Vessel MLLW Mean Lower Low Water MMSI Maritime Mobile Service Identity

NIWC-Paciﬁc Naval Information Warfare Center Paciﬁc NSE Nash-Sutcliffe Efﬁciency

PIV Particle Image Velocimetry

##### DSI, LLC vi EFDC+ Propeller Wash



<<<PAGE 10>>>

List of Abbreviations

rpm revolutions per minute rps revolutions per second

SEDZLJ Sediment Dynamics Algorithms developed by Ziegler, Lick, and Jones

TKE Turbulent Kinetic Energy TSS Total Suspended Sediments

USEPA United States Environmental Protection Agency UTM Universal Transverse Mercator UW University of Washington

WSDOT Washington State Department of Trasnportation WSF Washington State Ferries

##### DSI, LLC vii EFDC+ Propeller Wash



<<<PAGE 11>>>

# Chapter 1 Introduction

## 1.1. Background

Propeller wash is the ﬂow generated behind a rotating propeller. The propeller wash from ships may signiﬁcantly impact the sediment bed in water systems, especially in areas of substantial ship trafﬁc. The propeller wash can cause resuspension and redistribution of contaminated sediments bedded in urban waterfronts, as documented in numerous ﬁeld studies over the years (e.g., San Diego Bay, Gowanus Canal, Newtown Creek, Lower Duwamish River, and Portland Harbor Superfund sites). One such study conducted in San Diego Bay demonstrated that berthing/docking at only three naval piers resuspended a total of 26 tons per day of sediments into the water column (Wang et al., 2016). The resuspended contaminated sediments can be further transported by ship trafﬁc-induced currents in addition to ambient ﬂows, acting as a signiﬁcant source of recontamination at other locations nearby (Michelsen et al., 1998). In addition, propeller wash has been identiﬁed as the primary cause of scour around quay structures (e.g., piers and docks); such scour may result in structural instability, or even failure (PIANC, 2015). Research on propeller washinduced scour at the Kingston Ferry Terminal in Washington state (Kastner et al., 2019) observed that an undersea cliff face at a ferry slip had migrated shoreward in recent years; the study then showed that the propeller wash associated with ferries’ arrivals and departures had 10 to 30 times higher water velocities and 10 to 100 times higher resulting shear stresses than ambient conditions, with serious potential impacts for the seabed.

Over the decades, several approaches have been proposed to estimate the impacts of propeller wash on sediment resuspension (Garcia et al., 1999; Gucinski, 1982; Hong et al., 2016) and seabed scours around quay walls (Blaauw and van de Kaa, 1978; Fuehrer and R¨omisch, 1977; Hamill, 1987; Hong et al., 2013; Verhey et al., 1987). These studies have relied primarily on experiment results and have provided laboratory-based empirical formulations for propeller wash effect estimation. Recently, numerical modeling studies of propeller wash have been conducted to compute ﬂow and sediment transport patterns due to propeller wash in nearshore areas, linking them to numerical sediment transport models (Chadwick et al., 2008; Maynord, 2000; Wang et al., 2016). However, most modeling approaches have been limited to uncoupled representations of propeller wash to the sediment transport models. Speciﬁcally, the existing approaches are established based

##### DSI, LLC 1-1 EFDC+ Propeller Wash



<<<PAGE 12>>>

##### 1. Introduction



on empirical formulations that only address propeller wash-induced velocity and shear stress at the sediment bed, which prevents dynamic coupling to the far-ﬁeld transport processes. For example, the modelers calculated the propeller wash sediment resuspension using the empirical equations externally (i.e., by hand), and then they manually added this as a source term to a far-ﬁeld model simulation for subsequent sediment transport (Chadwick et al., 2008). Additionally, most current modeling efforts are limited to steady-state ﬂow conditions, neglecting propeller wash-induced momentum for hydrodynamic ﬂow ﬁeld computation. Moreover, their applications are frequently limited to a single type of vessel, with additional limitations in modeling ship paths.

## 1.2. Objective

DSI, LLC (DSI) has developed a numerical algorithm for propeller wash modeling, integrating this algorithm into Environmental Fluid Dynamics Code Plus (EFDC+) as a module. This algorithm is fully coupled to a three-dimensional (3D) hydrodynamic and sediment transport computation in EFDC+. Therefore, EFDC+ with the propeller wash module can dynamically simulate combinations of propeller wash-induced processes, such as sediment resuspension and bed scour due to ship trafﬁc, subsequent transport processes in the water column (e.g., advection, diffusion, settling), and redeposition in the sediment bed, as illustrated in Figure 1.1.

Figure 1.1: Schematic diagram of propeller wash-induced sediment transport processes.

##### DSI, LLC 1-2 EFDC+ Propeller Wash



<<<PAGE 13>>>

##### 1. Introduction



Major capabilities of the EFDC+ propeller wash modeling features are highlighted below.

- • Computes propeller wash effects based on an independent sub-grid mesh for each ship and integrates them into general model grid cells;
- • Addresses any number of ships simultaneously for the characteristics of ship and propeller properties illustrated in Figures 1.2 and 1.3;
- • Speciﬁes ship paths by interpolating Automatic Identiﬁcation System (AIS) or user-deﬁned ship tracking data;
- • Calculates propeller wash-induced shear stress, including ambient currents;
- • Applies a superposition approach to address multiple-propeller impacts;
- • Computes sediment transport processes linked to the Original Environmental Fluid Dynamics Code (EFDC) Sediment Transport module (Van Rijn, 1984a,b,c) and the Sediment Dynamics Algorithms developed by Ziegler, Lick, and Jones (SEDZLJ) module (Jones and Lick, 2001);
- • Simulates bedload and geomorphic feedback for both sediment transport modules; and
- • Incorporates propeller wash momentum into the 3D hydrodynamic ﬂow ﬁeld.


The fully coupled modeling features of the EFDC+ propeller wash module will be beneﬁcial for researchers, engineers, and regulators in their efforts to properly evaluate propeller wash effects for contaminant remediation planning, scour mitigation, and structure design. To assist in developing, running, and analyzing EFDC+ propeller wash models, EFDC Explorer Modeling System (EEMS) software provides pre-and post-processing tools with a Graphic User Interface (GUI). More information about the EEMS software is available online (www.eemodelingsystem.com).

This document provides comprehensive information on the EFDC+ propeller wash module as follows. Chapter 2 describes the theoretical basis for the propeller wash velocity solutions used in the EFDC+ propeller wash module. Chapter 3 addresses the algorithmic structures and implementation procedures of the EFDC+ propeller wash module. Chapter 4 provides the details of four input ﬁles required for the propeller wash simulation using EFDC+, and this chapter also suggests general guidelines for ship and propeller speciﬁcations that can be used as model inputs when the required information is not available. Chapter 5 presents several case studies that demonstrate and validate the EFDC+ propeller wash modeling features coupled to hydrodynamic and sediment transport processes.

##### DSI, LLC 1-3 EFDC+ Propeller Wash



<<<PAGE 14>>>

- DSI,LLC1-4EFDC+PropellerWash


- Figure 1.2: Deﬁnition for key ship properties (side view). The ship image is adapted from Damen Shipyards (2021).


1.Introduction

<<<PAGE 15>>>

- DSI,LLC1-5EFDC+PropellerWash


- Figure 1.3: Deﬁnition for key ship properties (back view). The ship image is adapted from Damen Shipyards (2021).


1.Introduction

<<<PAGE 16>>>

# Chapter 2 Theoretical Approach

Over the decades, through laboratory experiments and ﬁeld measurements, numerous studies have proposed empirical relationships to represent the ﬂow velocity ﬁeld induced by the rotation of a propeller. The studies to identify the main variables inﬂuencing propeller wash calculations have been conducted based on traditional dimensional analysis techniques for physical modeling. The advent of laser-based technologies for measurements has improved the data precision and has facilitated the development of various empirical relationships. These empirical studies have found that propeller wash velocity ﬁelds depend primarily on two parameters: propeller diameter and applied power to the propeller. The studies also established that propeller wash forms a symmetrical velocity distribution with respect to the propeller shaft axis.

The EFDC+ propeller wash module computes analytical propeller wash velocity proﬁles by adopting Hamill’s approaches (Hamill, 1987; Hamill and Kee, 2016; Hamill et al., 2015) and other empirical equations (Fuehrer and R¨omisch, 1977; Hashmi et al., 2007; Lam et al., 2011; Maynord, 2000; Stewart, 1992; Toutant, 1982). Figure 2.1 presents a schematic diagram summarizing the adopted equations for the following three propeller wash zones:

- • Efﬂux Zone
- • Zone of Flow Establishment
- • Zone of Established Flow


The propeller wash formation and diffusion processes differ explicitly among these three zones. As the propeller is rotating, the maximum propeller wash velocity occurs at the face of the propeller, which is termed the efﬂux velocity. This velocity does not decay within the efﬂux zone, which is a short distance behind the propeller. All subsequent velocity values (at any location within the diffusing propeller wash) are dependent on the magnitude of this initial maximum propeller wash velocity. As the propeller wash moves beyond the efﬂux zone, it enters the zone of ﬂow establishment, where the propeller wash becomes established and the diffusion occurs both inward and outward. Beyond the zone of ﬂow establishment, the propeller wash subsequently decays to merge with any background ﬂow in the zone of established ﬂow. The length of each propeller wash zone can be speciﬁed relative to the propeller diameter, Dp. The following sections describe the empirical formulations for each of the three zones adopted in the EFDC+ propeller wash module.

##### DSI, LLC 2-1 EFDC+ Propeller Wash



<<<PAGE 17>>>

DSI,LLC2-2EFDC+PropellerWash

Figure 2.1: Adopted formulations for the three propeller wash zones in EFDC+.

2.TheoreticalApproach

<<<PAGE 18>>>

##### 2. Theoretical Approach



## 2.1. Efﬂux Zone

The maximum velocity at the face of the propeller is termed the efﬂux velocity, V0 (Fuehrer and R¨omisch, 1977). Hamill (1987) suggested that there is no decay of the efﬂux velocity within a short distance of approximately x/Dp = 0.35 behind the propeller (the efﬂux zone). Beyond this distance, through direct measurements, Hamill (1987) concluded the maximum axial velocities within the propeller wash decreased with distance from the propeller as a result of lateral mixing. Additionally, the ﬂume experiments reported by Hamill and Kee (2016) suggested that the efﬂux velocity is distributed approximately uniformly along the efﬂux plane.

Therefore, for the analytical velocity proﬁle, EFDC+ applies the efﬂux velocity V0, which is laterally uniform with no decay within the efﬂux zone (x/Dp < 0.35), as shown in Figure 2.1. The following describes how EFDC+ calculates the magnitude of the efﬂux velocity using either an applied propeller rotational speed or an applied ship engine power.

When a propeller rotational speed is applied, the propeller efﬂux velocity V0 is computed as suggested by Fuehrer and R¨omisch (1977):

V0 = 1.59×n×Dp ×Ct0.5 (2.1) where,

V0 : propeller efﬂux velocity (m/s) n : propeller rotational speed (revolutions per second, rps) Dp : propeller diameter (m) Ct : propeller thrust coefﬁcient (dimensionless), typically 0.35

Fuehrer and R¨omisch (1977) derived the above equation from axial momentum theory, and this approach has been widely accepted to predict the propeller efﬂux velocity (Jiang et al., 2019). In this equation, the propeller’s rotational speed, diameter, and thrust coefﬁcient are user-deﬁned model input parameters (see Chapter 4).

When a ship engine power is applied, the propeller efﬂux velocity V0 is determined regarding the propeller thrust T (or effective push EP). Given the applied engine power, the effective push EP (in pounds-force, lbf) is calculated using Toutant equations (1982):

 

23.57P0.974 −2.3Vw2P0.5 for non-ducted propeller

EP =

(2.2)



31.82P0.974 −5.4Vw2P0.5 for ducted propeller

Vw = |Va −Vg| (2.3) where,

##### DSI, LLC 2-3 EFDC+ Propeller Wash



<<<PAGE 19>>>

##### 2. Theoretical Approach



EP : effective push equivalent to thrust (lbf) P : applied engine power (horsepower, hp) Va : ambient current velocity (mph), which is close to zero in tidal environments Vg : ship speed relative to ground (mph)

The effective push EP in pounds-force is then converted to the thrust T in newtons as:

T(N) = 4.45×EP(lbf) (2.4)

After that, the propeller efﬂux velocity V0 is computed as a function of the thrust T and contracted propeller wash diameter D0 (Maynord, 2000) as:

where,

1 D0 ×

V0 = 1.13×

T ρw

(2.5)

T : thrust (N) D0 : propeller wash diameter (0.71Dp for non-ducted propeller and Dp for ducted propeller) ρw : water density (kg/m3)

## 2.2. Zone of Flow Establishment

Beyond the efﬂux zone, the propeller wash forms the zone of ﬂow establishment. In this region, the maximum axial velocities decrease with distance from the propeller due to lateral mixing. Due to the hub’s inﬂuence at the center of the propeller, the propeller wash has a low-velocity core along the axis of rotation within the zone of ﬂow establishment. Consequently, the lateral velocity proﬁles within the zone of ﬂow establishment form two peaks, as shown in Figure 2.1. The ﬂuid is mixing with the surrounding water both inwardly and outwardly along the axis of rotation. The hub’s inﬂuence then disappears gradually along the longitudinal axis due to the penetration of high-velocity ﬂuid into the low-velocity central core.

Fuehrer and R¨omisch (1977) and Blaauw and van de Kaa (1978) found the end of the zone of ﬂow establishment occurred at a relative distance of x/Dp = 2.6 from the propeller face. Verhey et al. (1987) suggested the zone length was x/Dp = 2.77, while Stewart (1992) proposed the zone extended to approximately x/Dp = 3.25 from the propeller face. EFDC+ allows modelers to determine the length for the zone of ﬂow establishment as a model input parameter; the value of x/Dp = 3.25 (Stewart, 1992) is recommended per Hamill and Kee (2016).

For outside of the efﬂux zone, as per Hamill and Kee (2016), the EFDC+ velocity proﬁle applies the maximum axial velocity decreasing linearly with distance and computes its magnitude dependent on the initial efﬂux velocity magnitude V0 as:

##### DSI, LLC 2-4 EFDC+ Propeller Wash



<<<PAGE 20>>>

##### 2. Theoretical Approach



Vx,max V0

x

= 1.51−0.175

Dp −0.46P (2.6) where,

Vmax : maximum velocity at an axial distance x (m/s) x : distance from the propeller face (m) P : propeller pitch to diameter ratio (dimensionless)

The lateral distribution of the velocity in the zone of ﬂow establishment is then computed as suggested in Hamill and Kee (2016):

where,

where

Vx,r Vx,max

- 1

- 2


= exp −

r−Rmo σ

2

 

0.5Rmo for x/Dp < 0.5

σ =



0.5Rmo +0.075(x+0.5Dp) for x/Dp ≥ 0.5

(2.7)

(2.8)

Rmo = 0.67(Rp −Rh) (2.9) where,

Vx,r : velocity at an axial distance x and at a radial distance r (m/s) r : radial distance from the propeller shaft axis (m) Rmo : radial distance of maximum velocity from propeller shaft axis (m) Rp : radius of propeller (m) Rh : radius of propeller hub (m)

## 2.3. Zone of Established Flow

At a certain distance downstream, the ﬂow will only be mixing outwardly; this is referred to as the zone of established ﬂow. In this region, there is only one maximum velocity peak located at the

##### DSI, LLC 2-5 EFDC+ Propeller Wash



<<<PAGE 21>>>

##### 2. Theoretical Approach



axis of rotation. Through direct experimental measurements and based on propeller blade characteristics, Hamill (1987) proposed the following empirical equation for the decay of the maximum axial velocity in the zone of established ﬂow:

Vx,max V0

= A

x Dp

B

(2.10)

- A = −11.4Ct +6.65β +2.16P (2.11)
- B = −C−0.216


t ×β1.024 ×P −1.87 (2.12) where,

β : propeller blade area ratio, usually referred to as disk area coefﬁcient (dimensionless)

The lateral distribution of the velocity proﬁle in the zone of established ﬂow is then computed according to Fuehrer and R¨omisch (1977), per the recommendation of Hamill and Kee (2016):

Vx,r Vx,max

= exp −22.2

r x

2

(2.13)

## 2.4. Computation of Velocity at Water-Sediment Interface

The propeller wash velocity at the water-sediment interface for a speciﬁc location is then calculated based on Equations 2.7 and 2.13 by specifying the longitudinal distance x and radial distance r from the propeller as:

x = Xp (2.14)

r = YP2 +HP2 (2.15) where,

Xp : longitudinal distance from the propeller (m) YP : lateral distance from the propeller shaft axis (m) Hp : vertical distance from the propeller shaft axis to sediment bed (m)

##### DSI, LLC 2-6 EFDC+ Propeller Wash



<<<PAGE 22>>>

# Chapter 3 EFDC+ Algorithm Implementation

This chapter describes the algorithmic structure and implementation processes for EFDC+ propeller wash computation. Overall, EFDC+ implements the propeller wash computation based on an independent sub-grid for each ship. It can simulate multiple ships with a single model and specify the ship paths by utilizing ship tracking data (derived from AIS or user-deﬁned). EFDC+ then dynamically links the propeller wash sub-grids and model grid cells to compute hydrodynamic and sediment transport processes for every sediment time step.

Figure 3.1 shows the ﬂow chart for the EFDC+ propeller wash implementation procedures. The white-ﬁlled boxes indicate the general EFDC+ computation steps based on model grid cells, whereas the blue-ﬁlled boxes indicate the propeller wash module processes. The following provides the conceptual and mathematical details for each computation step, presenting the related schematic diagrams sequentially.

##### DSI, LLC 3-1 EFDC+ Propeller Wash



<<<PAGE 23>>>

##### 3. EFDC+ Algorithm Implementation



##### Figure 3.1: Flow chart of the EFDC+ propeller wash computation process.

##### DSI, LLC 3-2 EFDC+ Propeller Wash



<<<PAGE 24>>>

##### 3. EFDC+ Algorithm Implementation



#### Step 1. Compute Hydrodynamic Flow Field

When a simulation starts, EFDC+ computes a 3D hydrodynamic ﬂow ﬁeld at the general model grid cell resolution. Figure 3.2 displays an example of a two-dimensional (2D) plan view for model grid cells and depth-averaged ambient current velocity vectors simulated at a time step.

#### Step 2. Specify Ship Position

Propeller wash computation starts with specifying the location, heading, speed, and applied power of the ships to be considered. For each ship, EFDC+ establishes this information by interpolating ship tracking data, which are derived from AIS or manually deﬁned by the modeler (see details in Section 4.4). Figure 3.2 shows a ship heading west within a model grid cell, along with a ship path.

Figure 3.2: Hydrodynamic velocity ﬁeld for model grid cells and speciﬁcation of ship position based on a ship path (plan view).

#### Step 3. Generate Sub-grid Points

After specifying the ship positions, EFDC+ generates an independent 2D sub-grid behind each ship, as shown in Figure 3.3. The sub-grid points are used for the propeller wash computation for each ship, as described in the following steps. The modeler can deﬁne the sub-grid dimensions as a function of the propeller diameters (see details for the sub-grid conﬁguration in Section 4.2).

##### DSI, LLC 3-3 EFDC+ Propeller Wash



<<<PAGE 25>>>

##### 3. EFDC+ Algorithm Implementation



#### Step 4. Determine Bottom Elevation

The bottom elevations of the sub-grid points are determined based on the bottom elevation of the model grid cells. For each sub-grid point, EFDC+ uses an inverse distance squared scheme to interpolate the bottom elevation of the center of each surrounding model grid cell. Figure 3.3 presents an example of resultant sub-grid bottom elevations.

- Figure 3.3: Generation of sub-grid mesh behind ship and determination of bottom elevation for each sub-grid point (plan view).


#### Step 5. Compute Propeller Wash Velocity at the Bottom

Given the bottom elevation, EFDC+ computes the propeller wash velocities at the bottom (watersediment interface) for each sub-grid point using the approach described in Chapter 2. Figure

- 3.4 presents a vertical side view of conceptual diagrams summarizing the velocity formulations for the three propeller wash zones and indicating sub-grid points for velocity computation at the water-sediment bed interface.


For ships with multiple propellers, EFDC+ computes the propeller wash velocity ﬁeld for each propeller separately, then superposes them according to the distance between propellers. In this case, the ship with multiple propellers still has a single sub-grid mesh, indicating the velocity caused by multiple propellers. Figure 3.5 illustrates the superposition process for a two-propeller ship from a vertical back view.

##### DSI, LLC 3-4 EFDC+ Propeller Wash



<<<PAGE 26>>>

##### 3. EFDC+ Algorithm Implementation



##### Figure 3.4: Sub-grid points for velocity computation at water-sediment bed interface (side view).

##### Figure 3.5: Superposition of propeller wash velocities for a two-propeller ship (back view).

##### DSI, LLC 3-5 EFDC+ Propeller Wash



<<<PAGE 27>>>

##### 3. EFDC+ Algorithm Implementation



#### Step 6. Combine Propeller Wash and Ambient Velocities

Figure 3.6 displays the ambient current velocity vectors for model grid cells computed from Step 1 and the propeller wash velocities for sub-grid points (red for high values and blue for low values) computed from Step 5. Prior to computing a bottom shear stress, EFDC+ calculates a near-bed velocity for each sub-grid point, combining the ambient current and propeller wash velocities.

- Figure 3.6: Propeller wash velocities at sub-grid points and ambient current velocity vectors for model grid cells (plan view).


#### Step 7. Compute Shear Stress at the Bottom

Given the near-bed velocity, EFDC+ computes bottom shear stress τp (N/m2) for each sub-grid point using the Maynord (2000) approach as follows:

τp = 0.5×ρw ×Cf ×(Vbed)2 (3.1)

where, ρw : water density (kg/m3)

Dp Hp

Cf = 0.01×

(3.2)

##### DSI, LLC 3-6 EFDC+ Propeller Wash



<<<PAGE 28>>>

##### 3. EFDC+ Algorithm Implementation



Cf : friction coefﬁcient (dimensionless) Vbed : near-bed velocity (m/s) Dp : propeller diameter (m) Hp : distance between propeller shaft and sediment bed (m)

#### Step 8. Compute Erosion Rate at the Bottom

Given the bottom shear stress, EFDC+ computes an erosion rate Erate for each sub-grid point. The propeller wash erosion rate is calculated using either the Original EFDC Sediment Transport approach (in g/m2/s) (Van Rijn, 1984a,b,c) or the SEDZLJ Sediment Transport approach (in g/cm2/s) (Jones and Lick, 2001) in accordance with the approach used for the general EFDC+ sediment transport processes at the model grid cells (in Step 11). Additionally, this step computes the erosion rates for bedload and suspended load separately with respect to the applied bottom shear stress, critical shear stress of bed materials, and particle settling velocities. EFDC+ Theory Document Chapter 6 (DSI, 2020) provides detailed theories and mathematical descriptions for the Original EFDC and SEDZLJ Sediment Transport approaches. In Figure 3.7, the sub-grid points with a color ramp show an example of the resultant bottom shear stress or erosion rate, where red indicates high value and blue indicates low value.

- Figure 3.7: Shear stress or erosion rate induced by propeller wash at sub-grid points (plan view).


##### DSI, LLC 3-7 EFDC+ Propeller Wash



<<<PAGE 29>>>

##### 3. EFDC+ Algorithm Implementation



- Step 9. Calculate Erosion Mass for Sub-grid Areas
- Figure 3.8 displays sub-grid points and sub-grid areas, indicating the associated erosion quantities with colors. EFDC+ applies an assumption that the erosion rate at the sub-grid point represents the


erosion amount within the surrounding sub-grid area. It then calculates the erosion mass Em (g) for each sub-grid area during a sediment time step using the erosion rate (g/m2/s for the Original EFDC Sediment Transport approach or g/cm2/s for the SEDZLJ Sediment Transport approach) of each sub-grid point as follows.

Em = Erate ×Asub ×Tsed (3.3) where,

Em : erosion mass at a sub-grid area (g) Erate : erosion rate at a sub-gird point (g/m2/s or g/cm2/s) Asub : area of a sub-grid area (m2 or cm2) Tsed : sediment time step (s)

Figure 3.8: Sub-grid points, sub-grid area, and model grid cells for propeller wash-induced erosion mass calculation (plan view).

##### DSI, LLC 3-8 EFDC+ Propeller Wash



<<<PAGE 30>>>

##### 3. EFDC+ Algorithm Implementation



#### Step 10. Aggregate Sub-grid Erosion Mass to the Model Grid

Once the erosion mass (g) is calculated for each sub-grid area, EFDC+ computes a total erosion mass (g) at each model grid cell by aggregating the sub-grid area erosion masses within the corresponding model grid cell. Figure 3.8 shows the sub-grid points, sub-grid areas, and model grid cells that are related to the total erosion mass calculation.

#### Step 11. Compute the Sediment Transport Process

EFDC+ then simulates the sediment transport processes for the model grid cells via a user-deﬁned approach: either Original EFDC Sediment Transport or SEDZLJ Sediment Transport. Figure 3.9 conceptually illustrates the general sediment transport processes that EFDC+ simulates for the water column and the sediment bed. The sediments eroded from the bed (computed from Step 10) are transported as bedload and suspended load, as speciﬁed from Step 8. For the bedload computation, the eroded sediments are transported to the top sediment bed layer of the adjacent model cell downstream, which represents the process of sediments rolling or sliding along the sediment bed surface. For the suspended load computation, the eroded sediments are distributed into the water column (i.e., resuspension), and subsequent transport processes (i.e., advection, mixing, settling, and deposition) of the resuspended sediments are then simulated in response to the hydrodynamic ﬂow ﬁeld. Theories and mathematical descriptions for the sediment transport processes are described in detail in EFDC+ Theory Document Chapter 6 (DSI, 2020).

Figure 3.9: Conceptual diagram for EFDC+ sediment transport processes (side view).

##### DSI, LLC 3-9 EFDC+ Propeller Wash



<<<PAGE 31>>>

##### 3. EFDC+ Algorithm Implementation



#### Step 12. Add Propeller Momentum to the Flow Field (Optional)

EFDC+ has an option to add the momentum associated with the propeller efﬂux velocity V0 (calculated from Equation 2.1 or 2.5) to a 3D hydrodynamic ﬂow ﬁeld as a source term (see EFDC+ Theory Document Chapter 2 [DSI, 2020] for the momentum equations in detail). If this option is activated, EFDC+ includes the propeller wash momentum effects when it computes the hydrodynamic ﬂow ﬁeld for the next time step. The resulting ﬂow velocities then impact the movement of the resuspended sediments in the water column. Section 4.1 describes the input model parameter requirements to activate this option, and Section 5.4 demonstrates the propeller wash momentum effects on the ﬂow velocity ﬁeld and sediment transport processes.

Figure 3.10(a) shows a conceptual diagram of the various components of a ship passing through a model grid cell. Based on the angle between the ship’s heading and the grid rotation, EFDC+ vectorially splits the propeller efﬂux velocity V0 into the computational grid space (in i and j directions) as:

Vi = V0 ×cos(θ3 −θ1) (3.4)

Vj = V0 ×sin(θ3 −θ1) (3.5)

π 2

θ3 = θ2 −

(3.6) where,

V0 : propeller efﬂux velocity from the propeller plane (m/s) Vi : grid-oriented efﬂux velocity component in the i direction (m/s) Vj : grid-oriented efﬂux velocity component in the j direction (m/s)

- θ1 : EFDC+ model grid cell rotation (radian)
- θ2 : ship heading in compass orientation (radian)
- θ3 : propeller wash efﬂux angle (radian)


Given the velocity components Vi and Vj, EFDC+ computes the rate of momentum change (i.e., mass × velocity / time) due to propeller wash for each direction as follows:

where,

- Mpi = |Vi ×A|×Vi ×ρw (3.7)
- Mpj = |Vj ×A|×Vj ×ρw (3.8)


- MPi : rate of momentum change due to propeller wash in the i direction (kg·m/s2)


##### DSI, LLC 3-10 EFDC+ Propeller Wash



<<<PAGE 32>>>

##### 3. EFDC+ Algorithm Implementation



- MPj : rate of momentum change due to propeller wash in the j direction (kg·m/s2) A : area of propeller wash face in the efﬂux zone (m2) ρw : water density (kg/m3)


EFDC+ then incorporates the resultant momentum change rates MPi and MPj into the momentum equations of hydrodynamic computations as a source term (see EFDC+ Theory Document Chapter 2 [DSI, 2020]). EFDC+ also applies a factor to adjust the propeller wash-induced momentum change rates to account for losses and turbulence that are not directly simulated. This factor is a user-deﬁned input parameter of EFDC+, and the default factor, which is dimensionless, is 0.75

- (see Section 4.2).


Vertically, the the propeller wash-induced momentum effects are proportionately distributed across water layers the propeller intersects. Figure 3.10(b) shows a conceptual diagram of the vertical splitting process of the momentum change rates MPi and MPj for the water column layers. The vertical splitting process is implemented with respect to the ship position, draft, propeller diameter, water depth, and the number of water layers for the model grid cell where the propeller is located.

Figure 3.10: Diagrams for propeller wash-induced momentum (a) coupling with a model grid cell and (b) splitting over vertical water layers.

##### DSI, LLC 3-11 EFDC+ Propeller Wash



<<<PAGE 33>>>

##### 3. EFDC+ Algorithm Implementation



#### Repeat Propeller Wash Computation Every Sediment Time Step

The EFDC+ propeller wash module repeats the above processes for every sediment transport time step while the ships are located within the model domain. Figures 3.11 to 3.13 provide an example of how a ship with a sub-grid mesh is moving along a ship path and ambient currents vary sequentially during a simulation.

Additionally, EFDC+ can implement direct geomorphic feedback between hydrodynamic and sediment transport processes during a simulation. Speciﬁcally, the bed elevation changes predicted by the propeller wash-induced sediment transport computation update the bathymetry (i.e., bottom elevations) used in the hydrodynamic computation for the next time step. This modeling capability would lead to a more reasonable representation of ﬂow ﬁeld and sediment transport behaviors due to ship trafﬁc.

- Figure 3.11: Example of a moving ship with a sub-grid mesh at time step ti+1 (plan view).


##### DSI, LLC 3-12 EFDC+ Propeller Wash



<<<PAGE 34>>>

##### 3. EFDC+ Algorithm Implementation



##### Figure 3.12: Example of a moving ship with a sub-grid mesh at time step ti+2 (plan view).

##### Figure 3.13: Example of a moving ship with a sub-grid mesh at time step ti+3 (plan view).

##### DSI, LLC 3-13 EFDC+ Propeller Wash



<<<PAGE 35>>>

# Chapter 4 EFDC+ Input Requirements

EFDC+ performs a propeller wash simulation by reading four input ﬁles, which contain module control parameters, sub-grid conﬁguration, ship and propeller properties, and ship tracking data. First, this chapter provides the details of the model parameters and input data necessary for the four input ﬁles. Then, we suggest general guidelines for ship and propeller speciﬁcations, which can be used as the model inputs when the required information is missing or unavailable.

## 4.1. efdc.inp

“efdc.inp” is the master input ﬁle of EFDC+. It is an ASCII-formatted ﬁle containing computational options and data setting parameters, structured into card groups with respect to input objectives. In card group 14, the parameter “ISPROPWASH” offers options for whether the propeller wash module is activated for a simulation, as described in Table 4.1. When “ISPROPWASH” = 0, the propeller wash module is deactivated, so the simulation does not implement the propeller wash computation at all. When “ISPROPWASH” = 1, the propeller wash module is activated, so the simulation computes the propeller wash-induced sediment transport processes following Steps 1 to 11 in Chapter 3, but no impact on the ﬂow ﬁeld. When “ISPROPWASH” = 2, the simulation incorporates the propeller momentum effects into the hydrodynamic ﬂow ﬁeld computation (Step 12 in Chapter 3) so that the resulting ﬂow velocities impact the movement of resuspended sediments in the water column.

Table 4.1: Propeller wash module control ﬁelds in efdc.inp ﬁle.

Card Field Value Description C14 ISPROPWASH 0 No propeller wash

- 1 Activate propeller wash computation
- 2 Activate propeller wash computation with propeller efﬂux momentum


##### DSI, LLC 4-1 EFDC+ Propeller Wash



<<<PAGE 36>>>

##### 4. EFDC+ Input Requirements



## 4.2. propwash conﬁg.jnp

“propwash conﬁg.jnp” speciﬁes the general settings for propeller wash simulation in JSON format. These settings are separated into “mesh” and “parms” groups, as shown in Table 4.2.

The “mesh” group parameters are to specify the propeller wash sub-grid mesh conﬁguration. The longitudinal and lateral dimensions of the sub-grid mesh are determined by multiplying “mesh length” and “mesh width” parameters by a propeller diameter Dp, respectively. For twopropeller ships, the lateral dimension of the sub-grid mesh can be determined as “mesh width” × (Dp + distance between two propellers). The number of sub-grid points is deﬁned by “num axial elems” for the longitudinal dimension and “radial elems per-axial” for the lateral dimension.

In the “parms” group, three distance multipliers are applied to the propeller diameter Dp to deﬁne the lengths for the efﬂux zone, zone of ﬂow establishment, and zone of established ﬂow, as described in Figure 2.1. The default values are also given in Figure 2.1, and users may adjust them regarding the several suggestions described in Chapter 2.

“efﬂux mag mult” is a multiplier factor to adjust the efﬂux velocity momentum MP to account for losses and turbulence, as described in Step 12 in Chapter 3. This parameter is used only when the simulation adds the propeller efﬂux momentum to the hydrodynamic ﬂow ﬁeld (i.e., when ISPROPWASH = 2), with a default of 0.75.

Table 4.2: Propeller wash conﬁguration parameters in propwash conﬁg.jnp ﬁle.

Group Field Description mesh num axial elems Number of sub-grid points in the axial direction

num radial elems Number of sub-grid points in the radial direction mesh length Multiplier for sub-grid length in the axial direction mesh width Multiplier for sub-grid length in the radial direction

parms efﬂux zone mult Distance multiplier for the efﬂux zone

- ﬂow est zone1 mult Distance multiplier for the zone of ﬂow establishment

- ﬂow est zone2 mult Distance multiplier for the zone of established ﬂow efﬂux mag mult Efﬂux velocity momentum factor (for ISPROPWASH = 2)


##### DSI, LLC 4-2 EFDC+ Propeller Wash



<<<PAGE 37>>>

##### 4. EFDC+ Input Requirements



## 4.3. propwash ships.jnp

“propwash ships.jnp” contains the ship characteristics and propeller speciﬁcations in JSON format. EFDC+ performs the propeller wash computation for multiple ships (no limitation in numbers) in a single simulation, so this input ﬁle should include the information for all the ships being modeled. Table 4.3 lists the ship and propeller speciﬁcation parameters required for each ship (refer also to Figures 1.2 and 1.3 for illustrations of these ship features). In a simulation, EFDC+ identiﬁes each ship using the parameter “mmsi”, which indicates a Maritime Mobile Service Identity (MMSI) number. The parameter “mmsi” is used to link the ship characteristics in this input ﬁle to the corresponding ship tracking records in the “propwash tracks.jnp” ﬁle (see Section 4.4).

In Table 4.3, essential parameters are marked with an asterisk. Unfortunately, public and commercial databases generally provide only basic ship data (e.g., MMSI, vessel type, length, beam, gross tonnage), which are not sufﬁcient to specify the parameter values required for model simulations. For instance, the installed engine power (max power or max rps) is the most important piece of ship information for the propeller wash computation, but it is rarely available. To overcome such limitations in data availability, we devised several approaches to estimate the properties of the most common ships and propellers using only public and commercial databases; these approaches are described in Section 4.5.

##### DSI, LLC 4-3 EFDC+ Propeller Wash



<<<PAGE 38>>>

##### 4. EFDC+ Input Requirements



Table 4.3: Ship and propeller speciﬁcation parameters in propwash ships.jnp ﬁle.

Field Description mmsi* MMSI number IMO International Maritime Organization (IMO) identiﬁcation number USCG United States Coast Guard (USCG) documentation number name Ship name call sign Radio transmission license identiﬁer type Vessel type year built Year the ship was built length* Ship length overall: distance between bow and stern (m) beam* Ship width at its widest point (m) hull depth Depth of the watertight body of the ship (draft + freeboard) (m) gross tonnage Overall internal volume of the ship (all enclosed spaces) net tonnage Molded volume of the cargo spaces (dimensionless) max rps* Maximum propeller rotation speed in revolutions per second (rps) max power* Maximum installed engine power in horsepower (hp) max draft Maximum distance between the waterline and hull bottom (m) min draft Minimum distance between the waterline and hull bottom (m) ais to stern Distance between the AIS antenna location and stern (m) dist from stern Distance between the propeller and stern (m) dist between props* Distance between propeller shafts (for multiple propellers) (m) prop offset Distance from the hull bottom to the propeller shaft (m) num props* Number of propellers num blades* Number of propeller blades ducted* 0 for non-ducted propeller, 1 for ducted propeller thrust coeff* Propeller thrust coefﬁcient prop diam* Propeller diameter (m) prop hub diam* Propeller hub diameter (m) blade area ratio* Blade area ratio (dimensionless) pitch ratio* Pitch ratio (dimensionless) freq out* Frequency for propeller wash sub-grid output (in minutes) active ﬂag* 0 for deactivation, 1 for activation of the ship simulation num ﬁxed cells Number of model cells for a ﬁxed ship simulation ﬁxed cells I and J of the model cells for the ﬁxed ship simulation ﬁxed frac Cell fractions of propeller impacts for the ﬁxed ship simulation

*Essential model parameters

##### DSI, LLC 4-4 EFDC+ Propeller Wash



<<<PAGE 39>>>

##### 4. EFDC+ Input Requirements



## 4.4. propwash tracks.jnp

“propwash tracks.jnp” contains the tracking records for all the ships being simulated in JSON format. Figure 4.1 shows an example of the “propwash tracks.jnp” ﬁle format, and Table 4.4 provides the descriptions for each ﬁeld grouping with respect to hierarchical levels.

At the general level, “name” is for the title of ship tracking datasets recorded in this input ﬁle; “utm zone” deﬁnes the Universal Transverse Mercator (UTM) coordinate zone for ship locations; and “base date” sets the base date (Julian day time) applied to the tracking records in this ﬁle.

Under the “all ship tracks” ﬁeld, “mmsi” is used to identify each ship being modeled and links to the ship characteristics and propeller speciﬁcations deﬁned in the “propwash ships.jnp” ﬁle

- (see Section 4.3). Each ship can have multiple tracks under the “ship tracks” ﬁeld, where a track indicates a series of continuous ship path records (“track ﬁeld”).


The “track” ﬁeld contains a series of time records for each track. Each record speciﬁes a set of ship data at a given time “t”, including ship status “n”, speed “s”, course “c”, heading “h”, draft “d”, applied engine power “p”, and location “x” and “y”. The “track” ﬁeld also contains the parameter “o”, which can specify the sub-grid computation output frequency for a certain track duration. Unless it is set to zero, this parameter will override the general sub-grid output frequency “freq out” in “propwash ships.jnp”. Additionally, Table 4.5 provides the ship status code descriptions available for the parameter “n”.

In the “track” ﬁeld, the applied power “p” is deﬁned as a fraction of the maximum installed engine power in horsepower (hp) if the “p” value is positive. Otherwise, it is deﬁned as a fraction of the maximum propeller rotation speed in revolutions per second (rps) if the “p” value is negative. The maximum installed engine power (max power) and maximum propeller rotation speed (max rps) are recorded in “propwash ships.jnp” (see Section 4.3).

##### DSI, LLC 4-5 EFDC+ Propeller Wash



<<<PAGE 40>>>

##### 4. EFDC+ Input Requirements



Figure 4.1: Example of the propwash tracks.jnp ﬁle format.

Table 4.4: Ship track data ﬁelds in the propwash tracks.jnp ﬁle.

Level Field Description General name Title of ship track datasets

utm zone UTM coordinate zone for ship locations x, y base date Base date for Julian date track time t all ship tracks Field to contain track datasets for all ships

All Ship mmsi MMSI number for each ship Tracks ship tracks Field to contain multiple tracks for each ship

Ship track Field to contain a series of time records for each track Tracks n Ship Status Code (see Table 4.5)

- s Speed (m/s) c Course (degree): direction of travel through the water h Heading (degree): direction the ship is pointing d Draft (m): distance between the waterline and hull bottom

- o Sub-grid output frequency (minutes)
- p Applied power as a fraction of max power (+) or max rps (-)


- t Time (Julian date)


- x Ship location in x-coordinate (UTM-based)
- y Ship location in y-coordinate (UTM-based)


##### DSI, LLC 4-6 EFDC+ Propeller Wash



<<<PAGE 41>>>

##### 4. EFDC+ Input Requirements



Table 4.5: Ship status code descriptions for parameter “n”. n Ship Status Description

- 0 Under way using its engine
- 1 Anchored
- 2 Not under command
- 3 Has restricted maneuverability
- 4 Ship draft is limiting its movement
- 5 Moored
- 6 Aground
- 7 Engaged in ﬁshing
- 8 Under way sailing
- 9 & 10 Reserved for modifying reported status of ships carrying dangerous goods / harmful substances / marine pollutants


- 11 Power-driven ship towing astern
- 12 Power-driven ship pushing ahead/towing alongside
- 13 Reserved for future use
- 14 Any of the following are active: AIS-SART (Search and Rescue Transmitter) AIS-MOB (Man Overboard) AIS-EPIRB (Emergency Position Indicating Radio Beacon)
- 15 Undeﬁned (default)


##### DSI, LLC 4-7 EFDC+ Propeller Wash



<<<PAGE 42>>>

##### 4. EFDC+ Input Requirements



## 4.5. Data Input Guidelines

This section provides general guidelines for ship and propeller speciﬁcations to be used as model inputs for EFDC+ propeller wash simulations. In general, public and commercial AIS databases provide only basic information such as ship ID, vessel type, length, beam, gross tonnage, and time track records (location, speed, and heading direction). Such basic information is insufﬁcient to specify the detailed ship characteristics and operations required for model simulations. To overcome the limitation in data availability, we ﬁrst collected public and commercial data associated with ship and propeller properties from various sources, including PIANC (2015), NYSDOT (2005), MAN (2018), and TugboatInformation.com (2021). We then devised several approaches to estimate the most important properties of ships and propellers based on the basic ship information (refer to Figures 1.2 and 1.3 for illustrations of ship features). The guidelines described in this section will be beneﬁcial to modelers when the information needed for model inputs is not available.

### 4.5.1 Ship Properties

#### 4.5.1.1 Draft

A ship’s draft is the distance between the waterline and the hull bottom. Modelers can specify the maximum draft as a function of a ship’s length. Figure 4.2 shows the relationship between the overall length and the draft of fully loaded ships from PIANC (2015) data for different vessel types (e.g., tankers, carriers, container ships, cargo ships, passenger ships, and small boats). Overall, the fully loaded draft usually falls within 2.5% to 6.5% of the length. The ratio varies slightly depending on the vessel type (higher for tankers and lower for passenger ships). Therefore, modelers may choose a ratio between 2.5% and 6.5% of the ship’s length when estimating the maximum draft of the ship.

Table 4.6 presents the light draft and loaded draft of self-propelled oil tankers provided by NYSDOT (2005). Modelers may estimate the minimum draft as about 45% to 70% of the maximum draft based on this information.

#### 4.5.1.2 Hull Depth

The parameter hull depth refers to the depth of the watertight body of a ship, which includes the draft and freeboard. Figure 4.3 shows the relationship between the hull depth and the draft of fully loaded ships from the PIANC (2015) data. Generally, the hull depth is 1.2 to 2.4 times greater than the fully loaded draft. The ratio varies depending on the vessel type (higher for cargo ships and lower for tankers). Based on this, modelers may estimate the hull depth as a function of the maximum draft according to the vessel type.

##### DSI, LLC 4-8 EFDC+ Propeller Wash



<<<PAGE 43>>>

##### 4. EFDC+ Input Requirements



Figure 4.2: Length and draft of fully loaded ships according to PIANC (2015) data.

Table 4.6: Characteristics of self-propelled oil tankers per NYSDOT (2005). Light to Loaded

Length Beam Light Draft Loaded Draft Draft Ratio Ship Name (m) (m) (m) (m) (%) Kiristin Poling 85.6 12.2 2.7 5.2 52.3 Coral Queen 57.3 8.5 2.3 3.7 63.3 John B. Caddell 56.4 11.0 2.1 3.6 58.8 Patricia Gellatly 55.2 9.1 2.6 4.3 61.4 Patrick Sky 38.4 9.4 1.7 3.8 44.4 Scott Sky 35.7 9.8 1.7 3.2 52.8 Great Gull 84.1 16.8 2.9 5.1 57.8 Newtown Creek 98.8 15.2 3.4 5.1 65.5 North River 98.8 15.2 3.4 5.1 65.5 Owls Head 86.3 14.0 2.7 4.0 69.2

##### DSI, LLC 4-9 EFDC+ Propeller Wash



<<<PAGE 44>>>

##### 4. EFDC+ Input Requirements



Figure 4.3: Hull depth and draft of fully loaded ships according to PIANC (2015) data.

#### 4.5.1.3 Distance from AIS Antenna to Stern

The AIS antenna generally stands above the central control room of a ship. Modelers may estimate the distance between the AIS antenna and stern (rear end of the ship) according to the vessel type. For tankers, carrier ships, container ships, and cargo ships, the AIS antenna is usually located nearer to the ship’s stern. In this case, the distance from the AIS antenna to the stern is estimated to be 15% to 30% of the ship length. In contrast, passenger ships and smaller boats have the AIS antenna toward the bow, then the distance from the AIS antenna to the stern may be 70% to 85% of the ship length. If no information is available, modelers may specify the AIS antenna as located in the middle of the ship (setting the distance as 50% of the ship length).

#### 4.5.1.4 Distance from Stern to Propeller

Most ships have their main propeller(s) near the stern, so the modeler may specify the distance from the stern to propeller as about 2% of the ship length. However, some tugboats have their main propeller toward the bow or in the middle of the ship and a rudder-shaped ﬁn on the aft side, so the distance from the stern to propeller can be set as 50% to 70% of the ship length in this case. The distance from the AIS antenna to the stern “ais to stern” and the distance from the stern to the propeller “dist from stern” are used during a simulation to identify the propeller location relative to the AIS tracking records.

##### DSI, LLC 4-10 EFDC+ Propeller Wash



<<<PAGE 45>>>

##### 4. EFDC+ Input Requirements



#### 4.5.1.5 Distance from Hull Bottom to Propeller Shaft

The parameter “prop offset” indicates the vertical distance between the hull bottom and the propeller shaft (see Figure 4.4). Modelers should use a positive value for “prop offset” if the propeller shaft is located lower than hull bottom (the hull’s deepest point). In contrast, the “prop offset” value should be negative if the propeller shaft is located higher than the hull bottom.

For merchant ships (tankers, carriers, container ships, cargo ships, and passenger ships), the propeller is not allowed to extend below the hull bottom. A small margin is included to ensure that the propeller is not damaged in the event of grounding, dry docking, or similar. Interference between the propeller and the seabed or a rock can damage the propeller blades, the propeller shaft, the gearbox, and the main engine itself. Therefore, if the hull bottom and propeller shaft distance is unknown, the modeler may specify this parameter value based on an estimate of the main propeller size and the ship’s draft.

- Figure 4.4: Propeller offset parameter for distance from the hull bottom to the propeller shaft.


##### DSI, LLC 4-11 EFDC+ Propeller Wash



<<<PAGE 46>>>

##### 4. EFDC+ Input Requirements



#### 4.5.1.6 Main Engine Power

Since ship owners in competitive markets are reluctant to disclose detailed information about their ships, it is difﬁcult for the modeler to identify the installed power of the main propulsion systems for the ship of interest. Therefore, this section suggests some approaches to predict the installed main engine power based on ship dimensions. For instance, modelers may compute the deadweight tonnage using the identiﬁed vessel type and length, and then estimate the installed engine power using the computed deadweight tonnage. The following describes the suggested process to estimate a ship’s installed engine power.

- Figure 4.5 shows data from PIANC (2015) on ships’ overall length and deadweight tonnage. The deadweight represents the ship’s loading capacity, including bunkers, fuel, lube oils, and other supplies necessary for the ship’s operation. With these datasets, we identiﬁed the relationship between ship length (L) and deadweight tonnage (DWT) using the power function regression for ships overall and for each vessel type separately, as:




0.0021×L3.10 for All Vessels

0.0003×L3.52 for Tankers

0.0002×L3.50 for Carriers

DWT =

0.0335×L2.57 for Container Ships



0.0028×L3.09 for General Cargo Ships

(4.1)

0.0160×L2.65 for Roll-on/Roll-off Cargo Ships

0.0037×L2.97 for Passenger Ships



0.0018×L3.15 for Boats Under 100 m in Length

PIANC (2015) includes some samples that relate the installed engine power (in hp) and deadweight tonnage at design draught, as shown in Figure 4.6. We conducted a regression analysis to deﬁne the installed engine power (P) as a function of deadweight tonnage (DWT) for these samples. In this case, the relationship shows different behaviors when the deadweight tonnage is greater than 50,000 tons vs. less than 50,000 tons, so we applied different regression functions for each condition. The regression results are presented in Equation 4.2 and Figure 4.6.

 

0.0326×DWT1.3167 for DWT < 50,000

P(hp) =

(4.2)



64,696×ln(DWT)−650,483 for DWT ≥ 50,000

##### DSI, LLC 4-12 EFDC+ Propeller Wash



<<<PAGE 47>>>

##### 4. EFDC+ Input Requirements



Figure 4.5: Length and deadweight tonnage based on PIANC (2015) data.

- Figure 4.6: Installed engine power as a function of deadweight tonnage per PIANC (2015) data.


##### DSI, LLC 4-13 EFDC+ Propeller Wash



<<<PAGE 48>>>

##### 4. EFDC+ Input Requirements



As a result of this analysis, modelers seeking to estimate missing ship data can use Equation 4.1 to calculate the deadweight tonnage using the identiﬁed vessel type and length, and then can employ Equation 4.2 to estimate the installed engine power using the previously calculated deadweight tonnage.

The PIANC (2015) data does not include sufﬁcient information for ships with a length of less than 50 m (see Figure 4.5). Typically, deadweight tonnage information is not available for such small vessels, so the approach suggested above might not apply to small tugboats, which may also represent a large portion of ship trafﬁc in harbor or bay areas. To ﬁll the data gap, we collected 110 samples of ship dimensions and engine power for tugboats smaller than 50 m from a tugboat database website, TugboatInformation.com (2021). The collected tugboat dataset indicates a positive correlation between installed engine power (P) and ship beam (B), which can be expressed

- as the exponential function regression shown in Equation 4.3 and Figure 4.7. Therefore, modelers may employ this approach when estimating the installed engine power (in hp) for such small-sized ships.


P(hp) = 828.31×exp(0.1587×B) (4.3)

- Figure 4.7: Installed engine power as a function of ship beam per TugboatInformation.com


(2021) data.

##### DSI, LLC 4-14 EFDC+ Propeller Wash



<<<PAGE 49>>>

##### 4. EFDC+ Input Requirements



### 4.5.2 Propeller Properties

#### 4.5.2.1 Propeller Diameter

PIANC (2015) includes an empirical relation between propeller diameter Dp (m) and installed engine power P (hp), which is generally applicable to various vessel types of propellers. Empirical Equation 4.4 can be used to estimate the diameter of both ducted and non-ducted propellers.

Dp = 0.1636×

P 1.341

0.3656

(4.4)

#### 4.5.2.2 Propeller Hub Diameter

Propeller hub diameter is usually 15% to 20% of the propeller diameter, retaining high propeller efﬁciency. Sometimes, the propeller has a relatively larger hub, with a hub/propeller diameter ratio of approximately 22% to 30%; in this case, the propeller efﬁciency would be slightly lower (MAN, 2018).

#### 4.5.2.3 Number of Blades

Propellers can have 2, 3, 4, 5, 6, or 7 blades. In general, the fewer blades, the higher the propeller efﬁciency will be. However, because of strength and vibration issues, 4-, 5-, and 6-bladed propellers are typically used on merchant ships, with four blades being the most common.

#### 4.5.2.4 Pitch Ratio

The pitch ratio expresses the ratio of pitch to the diameter of the propeller. The propeller pitch indicates the distance the propeller screws itself forward through the water per revolution. Generally, the propeller manufacturer’s manual provides the pitch ratio information. The pitch ratio typically falls between 0.5 and 2.5, with an optimal value for most ships closer to between 0.8 and 1.8 (MAN, 2018).

#### 4.5.2.5 Blade Area Ratio

The blade area ratio (usually referred to as disk area coefﬁcient) deﬁnes the developed surface area of the propeller in relation to its blade area. This area must be sufﬁciently large to avoid harmful cavitation that can lead to erosion, but not too large, as this will increase the frictional drag on the propeller. A ratio of 0.4 to 0.6 is typical for 4-bladed propellers. Highly loaded single screw container ships can see values as high as 1.0 (MAN, 2018).

##### DSI, LLC 4-15 EFDC+ Propeller Wash



<<<PAGE 50>>>

##### 4. EFDC+ Input Requirements



### 4.5.3 Applied Power for Tracking Data

The ship track ﬁle (“propwash track.jnp”) requires speciﬁcation of the applied power for each track point as a fraction of either maximum engine power or maximum revolution speed. Modelers may specify the applied power based on the general engine operation guidelines for vessel types and sailing conditions described below.

For regular sailing, ships typically use about 75% of the installed engine power when they operate

- at the design service speed under normal load and weather conditions.


For berthing and departure maneuvering, PIANC (2015) recommends the applied power as about

- 5% to 15% of the installed engine power for the main propellers of large ships (e.g., tankers, carriers, container ships, and passenger cruises). A value of 5% might be applied for sheltered berth locations with bed protection and no currents (e.g., berthing in harbor basins). A value of 15% is recommended for exposed berth locations with riverine or tidal currents and bed protection (e.g., quay walls along the river). For smaller ships, the applied power for berthing and departure may be 30% to 40% of the installed engine power. Additionally, tugboats can operate at 75% to 100% of the installed power.


The sailing speed of a ship during berthing and departure will be relatively low, so the ship’s maneuverability is signiﬁcantly reduced and the ship cannot rely on the rudder to the same degree

- as during normal sailing speeds. Because of this, ships commonly use their bow and/or stern thrusters during berthing and departure, applying 70% to 100% of the installed engine power.


##### DSI, LLC 4-16 EFDC+ Propeller Wash



<<<PAGE 51>>>

# Chapter 5 Case Studies

This chapter presents case studies conducted to demonstrate and validate the EFDC+ propeller wash modeling features coupled to hydrodynamic and sediment transport processes.

## 5.1. Validation Using Flume Experiment Data

The purpose of this analysis is to evaluate the velocity formulations used in the EFDC+ propeller wash module (described in Chapter 2) by comparing them to the observation data from a published paper.

Hong et al. (2016) conducted a ﬂume experiment to measure the ﬂow velocity introduced by propeller wash under ﬂat and non-erodible bed conditions. They used a recirculating ﬂume of 30 m long, 0.7 m wide, and 0.6 m deep, where water was pumped from a reservoir to the ﬂume slowly until the still water level was reached. A propeller was placed along the centerline of the ﬂume. The propeller had a diameter of 0.075 m with three blades and a hub diameter of 0.016 m, and the propeller shaft was placed 0.2 m above the bed surface. While the propeller was rotating at 1,000 revolutions per minute (rpm), they collected instantaneous 3D velocity components using an Acoustic Doppler Velocity Proﬁler (ADVP), measuring a water column over a 3-cm range with 1mm resolution, with a sampling rate of 100 Hz. They obtained time-averaged velocities by varying the measuring times between 3 and 10 minutes according to the turbulence intensity. Speciﬁcally, the measuring time was comparatively longer for locations near the propeller and bed than at other locations.

Figure 5.1 compares the velocity proﬁles computed by EFDC+ model formulations to the ADVP measurements along the longitudinal distances at x/Dp = 1.47, 2, 2.67, 6, and 8. In this ﬁgure, the

- x-axis represents the velocity magnitude at each longitudinal location, and the y-axis indicates the vertical distance from the propeller axis. Hong et al. (2016) did not provide detailed information about the propeller speciﬁcations such as thrust coefﬁcient, blade area ratio, and pitch ratio. Hence, this study computed the propeller wash velocity proﬁles by specifying the propeller parameters as presented in Table 5.1, which are within the typical value ranges (refer Section 4.5.2). In Figure 5.1, the results show reasonable agreements between the computed results and the measured data for


##### DSI, LLC 5-1 EFDC+ Propeller Wash



<<<PAGE 52>>>

##### 5. Case Studies



both the zone of ﬂow establishment (x/Dp < 3.25) and the zone of established ﬂow (3.25 < x/Dp). Speciﬁcally, the EFDC+ model formulations reproduced well the maximum measured velocities over all locations. The predictions are much better in the zone of established ﬂow, especially near the bottom, than in the zone of ﬂow establishment.

Table 5.1: Modeled propeller properties used for the Hong et al. (2016) experiment case.

Properties Values Propeller diameter 7.5 cm Propeller hub diameter 1.6 cm Thrust coefﬁcient 0.20 Blade area ratio 0.55 Pitch ratio 0.80 Applied revolution speed 1,000 rpm

Figure 5.1: Velocity proﬁles from EFDC+ propeller wash computations compared to Hong et al. (2016) experiment data.

##### DSI, LLC 5-2 EFDC+ Propeller Wash



<<<PAGE 53>>>

##### 5. Case Studies



## 5.2. Validation Using San Diego Bay Field Data

During the development of the EFDC+ propeller wash module, DSI collaborated with Naval Information Warfare Center Paciﬁc (NIWC-Paciﬁc) via a Cooperative Research and Development Agreement (CRADA). Under this agreement, NIWC-Paciﬁc provided propeller wash ﬁeld data collected at a U.S. Navy facility in San Diego Bay, as reported in Wang et al. (2016). DSI then used the San Diego Bay data to test and validate the EFDC+ propeller wash module. This section evaluates EFDC+ model performance for propeller wash-induced ﬂow velocity, shear stress, and erosion depth using the observation data provided by NIWC-Paciﬁc.

Wang et al. (2016) conducted a ﬁeld study to investigate propeller wash impacts under controlled conditions using a Navy-contracted tugboat (Tractor C-14). Figure 5.2 illustrates the conﬁguration of the tugboat propeller wash measurements, and Table 5.2 provides the details for the tugboat and propeller characteristics. In the ﬁeld study, the tugboat was moored between Piers 4 and 5 (San Diego Naval Base) with the bow pushing against the pier wall and the propellers thrusting toward the water. During the survey (13:50 to 14:30 on July 19, 2012), the propellers were operated at four different revolution speeds for different time periods, starting with a period of about 7 minutes at 20 rpm, which is the lowest rpm possible without stalling the tugboat engine. The revolution speed was then increased to 50 rpm for about 11 min, followed by subsequent increases to 100 rpm for about 9 min and 150 rpm for about 9 min. After the 150 rpm period, the propellers were brought to a stop. They installed an Acoustic Doppler Velocimeter (ADV) on the bottom at 110 meters behind the tugboat to measure the water velocity at 15 cm above the bottom during the study period. The ADV-measured velocity data were then used to estimate the bottom shear stress. Particle Image Velocimetry (PIV) was also deployed at the same location to capture the water velocity proﬁle near the bottom, but the PIV velocity data were not available for the high propeller speed conditions due to the interference by resuspended sediments. Instead, they used the PIV images to analyze the bottom elevation changes during the survey period.

DSI developed a propeller wash model using EFDC+ for the San Diego Bay tugboat test area.

- Figure 5.3 presents the model grid cells, bottom elevations, tugboat location, ADV and PIV locations, and sub-grid points (showing the simulated propeller wash velocities as an example). The model domain covered the area around Piers 4 and 5, using a Cartesian horizontal grid of 4,556 cells with a uniform cell dimension of 10 m × 10 m. A vertical grid used ten layers for the water column. Within the model domain, bottom elevations varied between -11.74 m and -8.00 m, with a mean elevation of -9.72 m based on the Mean Lower Low Water (MLLW) vertical datum. The bathymetry data was provided by NIWC-Paciﬁc.


For the hydrodynamic module, the model applied a time series of tidal conditions to open boundary cells. For the sediment transport module, the model used the SEDZLJ approach (see Steps 8 and 11 in Chapter 3). Because no data were available to determine sediment bed properties in this area (e.g., particle sizes, erodibility, porosity), we deﬁned a representative sediment bed conﬁguration by adopting sediment data sources from other harbor areas. Speciﬁcally, the sediment bed was assumed to have a 30 cm thickness using a vertical grid of ﬁve layers. The sediment content fractions were different for each layer to represent vertically-varied sediment properties. The average composition of the ﬁve sediment layers consisted of 60% clay, 20% silt, 10% ﬁne sand, and 10% coarse sand.

##### DSI, LLC 5-3 EFDC+ Propeller Wash



<<<PAGE 54>>>

##### 5. Case Studies



Figure 5.2: Conﬁguration of tugboat propeller wash measurements.

Table 5.2: Tugboat Tractor C-14 information and ﬁeld study conditions.

Characteristics Values Ship length 28.65 m Ship beam 10.36 m Ship draft 3.35 m Water depth 9.14 m Underkeel clearance 2.99 m Ship speed 0 m/s Installed engine power 4,800 hp Propeller type Ducted propellers Number of propellers 2 Propeller diameter 2.28 m Propeller thrust coefﬁcient 0.39 Distance from ship stern to propeller 15.24 m Distance between propellers 4.88 m Distance from water surface to propeller axis 4.88 m Distance from propeller axis to bottom 4.26 m Applied revolution speeds 20, 50, 100, 150 rpms

##### DSI, LLC 5-4 EFDC+ Propeller Wash



<<<PAGE 55>>>

##### 5. Case Studies



Figure 5.3: EFDC+ model conditions for the San Diego Bay ﬁeld test case.

For the propeller wash module, the model used the tugboat and propeller speciﬁcations presented in Table 5.2. The sub-grid conﬁguration for the tugboat was set as 225 m in length and 100 m in width, including 50 points in the longitudinal dimension and 20 points in the lateral dimension. The model simulated the propeller operations for different revolution speeds (20, 50, 100, and 150 rpms), as mentioned above.

### 5.2.1 Near-bed Flow Velocity

This study evaluated the propeller wash velocities simulated at a sub-grid point near the ADV location from the model, comparing them to the ADV-measured velocities. Both the sub-gridbased model results and the ADV data represented the propeller wash-induced velocities at the bottom of the waterbody (water-sediment interface). Figure 5.4 presents the ADV-measured data and EFDC+ model results for the propeller wash velocities at the ADV site. In this ﬁgure, the xaxis indicates relative times (in min) from the time the propeller-induced velocity was ﬁrst detected, and the y-axis shows velocity magnitudes. Vertical black lines represent the effective starting time for each rpm operation.

- In Figure 5.4, the ADV raw data (grey line) show near-bottom ﬂow velocities with large ﬂuctuations due to turbulence. It is important to note that the measured velocities with propeller operations may include inﬂuences from other sources. For example, the applied propeller revolution speeds (20, 50, 100, 150 rpms) were just estimated by the tugboat captain, so the actual rotat-


##### DSI, LLC 5-5 EFDC+ Propeller Wash



<<<PAGE 56>>>

##### 5. Case Studies



ing speeds could be unsteady and inconsistent, especially for lower speeds (Wang et al., 2016). Additionally, the ADV signals could have been disturbed by other ship trafﬁc nearby or by ﬂow circulation due to pier structures. To address such inﬂuences when analyzing the ADV-measured data, we considered the average and standard deviation of the ﬂuctuating velocities for each rpm run. Figure 5.4 uses red markers for the average data values and displays red whiskers for the standard deviation extending from the average points. Overall, the observed velocities increased with the propeller rpm, although the increase was not linear. For instance, when the propeller speed increased from 100 rpm to 150 rpm (a 50% increase), the average velocity increased only from

- 0.53 m/s to 0.57 m/s (an 8% increase).


- Figure 5.4: Propeller wash velocity from ADV-measured data and EFDC+ model results at 110 m behind tugboat Tractor C-14.


- Figure 5.4 shows the simulated propeller wash velocities for each propeller operation speed as a blue line. The model results are presented as a step function of the applied rpms because EFDC+ computed the ﬁxed tugboat’s propeller wash velocities at a sub-grid point using the analytical formulations in Chapter 2. Overall, the simulated propeller wash velocities increased linearly as the applied rpms increased. It is the expected result because the velocity magnitudes in a propeller


wash ﬁeld (see Equations 2.6 and 2.10) are dependent on the efﬂux velocity V0, which has a linear relationship with the applied propeller revolution speed, as described in Equation 2.1. For this simulation, the average propeller wash velocity magnitude observed for a rotational propeller speed of 100 rpm was reproduced by the model. The model underestimated the velocity magnitudes for lower rotational propeller speeds at 20 and 50 rpms, but the underestimation diminished as the rotational speed increased. For the 150 rpm period, the simulated velocity magnitudes exceeded

##### DSI, LLC 5-6 EFDC+ Propeller Wash



<<<PAGE 57>>>

##### 5. Case Studies



the measured values, but the model results were still within a standard deviation range from the average data value.

In addition to the rpm-based simulation, the model was also used to simulate propeller wash velocities when applying four different engine power levels (320, 800, 1600, 2400 hp); these model results are shown as the green lines in Figure 5.4. This hp-based simulation was implemented by assuming the applied engine power for each rpm condition as follows. Wang et al. (2016) stated that operating speeds for the tugboat Tractor C-14 typically range between 100 rpm and 200 rpm during ship husbanding tasks (e.g., customs formalities, fueling, supply activities, and repairs). Based on this information, we assumed that 50% of the installed engine power would be required for operating the propellers in the ship husbanding conditions, which indicates a median revolution speed of 150 rpm. The installed engine power of the tugboat is 4,800 hp as presented in Table 5.2. We then estimated the applied engine power for each of the four operation periods with respect to the applied rpm levels relative to the 150 rpm median, as follows: 320 hp for 20 rpm, 800 hp for 50 rpm, 1,600 hp for 100 rpm, and 2,400 hp for 150 rpm. The model results indicate that the engine power-based simulation performed much better in reproducing the ADV-measured velocities for all of the comparable propeller revolution speeds. The engine power-based model also simulated the velocity magnitudes increasing non-linearly with the applied engine power. These results are expected, because the efﬂux velocity and the applied engine power are non-linearly related for the EFDC+ analytical solutions as deﬁned through Equations 2.2 to 2.5.

Based on the model-to-ADV data comparison results, we conclude that the EFDC+ propeller wash model reasonably predicts propeller wash velocities at berthing/docking facilities in harbor areas.

### 5.2.2 Bottom Shear Stress

Using the ADV-measured velocity data, Wang et al. (2016) calculated the bottom shear stress based on a modiﬁed Turbulent Kinetic Energy (TKE) method (Kim et al., 2000), which is deﬁned as:

τb = 0.9×ρw ×w 2 (5.1) where,

τb : bottom shear stress (N/m2) ρw : water density (kg/m3) w : vertical velocity ﬂuctuation (m/s)

The modiﬁed TKE method requires only the vertical velocity ﬂuctuations to address the total energy balance regarding the propeller wash turbulence and the bottom shear stress dissipation. Hence, this approach has widely been used with ADV velocity data because the ADV provides a lower level of noise errors for vertical velocity variances compared to the noise errors associated with horizontal velocity ﬂuctuations (Voulgaris and Trowbridge, 1998). In Wang et al. (2016),

##### DSI, LLC 5-7 EFDC+ Propeller Wash



<<<PAGE 58>>>

##### 5. Case Studies



the vertical velocity ﬂuctuation statistics (w 2) were calculated over an averaging window of 10 seconds, which corresponded to 300 ADV data points with a sample rate of 30 Hz.

This study used the shear stress values estimated using the modiﬁed TKE method by Wang et al. (2016) as measurements for the bottom shear stress induced by the tugboat propeller wash. We then compared the measurements to the propeller wash shear stress simulated by the model (Equation 3.1) at a sub-grid point near the ADV location. Figure 5.5 presents the modiﬁed TKE methodbased measurements and EFDC+ model results for the bottom shear stress at the ADV site. In this ﬁgure, the x-axis shows relative times (in min) measured from when the propeller-induced velocity was ﬁrst detected, and the vertical black lines represent the effective starting time for each rpm operation. The left y-axis indicates the shear stress (in N/m2) as a gray line, and the right

- y-axis is used for the cumulative shear stress over time (in N/m2-Hour), presented with colored lines.


Figure 5.5: Propeller wash shear stress from modiﬁed TKE method-based data and EFDC+ model results at 110 m behind tugboat Tractor C-14.

- In Figure 5.5, the measured bottom shear stress (N/m2) from the modiﬁed TKE method (grey line) presents several spikes during the propeller operations. Overall, the measured data generally showed higher shear stresses at higher propeller rpm, but the peak magnitude was not proportional to the propeller speeds. Speciﬁcally, the peak magnitude of the observed shear stress varies at each rpm period as: 1.2 N/m2 for 20 rpm, 2.2 N/m2 for 50 rpm, 1.4 N/m2 for 100 rpm, and 2.6 N/m2 for 150 rpm. To examine the total effects of the propeller wash shear stress including the mean and temporal variations over time, we calculated the cumulative shear stress (N/m2-Hour) for the measurements during the study period, about 36 min. The red line with markers represents the


##### DSI, LLC 5-8 EFDC+ Propeller Wash



<<<PAGE 59>>>

##### 5. Case Studies



cumulative distribution of the measured shear stress (N/m2-Hour), which integrates the measured instantaneous shear stress (gray line). The cumulative shear stress curve presents higher increase rates (slope) as the propeller speeds increase, and it also shows several jumps at the 150 rpm period due to the high magnitude spikes. The total cumulative shear effects reached about 0.295 N/m2-Hour at the end of the propeller operations.

- Figure 5.5 also displays the model results for the bottom shear stress as the cumulative distribution: the blue line is for the propeller rotation speed-based simulation (20, 50, 100, 150 rpm) and the green line is for the engine power-based simulation (320, 800, 1600, 2400 hp). Recall that EFDC+ computes the propeller wash bottom shear stress as a function of the propeller wash velocity at the bottom (see Equations 3.1 and 3.2). So, for both rpm-and hp-based models, the slope of the cumulative shear stress curve increased as the applied propeller speed or engine power increased during the simulation. These model results are consistent with the behaviors observed from the cumulative shear stress data curve. At the end of the propeller operations, the rotation speed-based simulation result (0.272 N/m2-Hour) underestimated the measured cumulative effects by only 8%, and the engine power-based simulation result reached 0.296 N/m2-Hour, which is almost identical to the measured cumulative shear stress of 0.295 N/m2-Hour. These results support the conclusion that the EFDC+ model performs well in estimating propeller wash-induced bottom shear stress in harbor areas.

5.2.3 Erosion Depth

Wang et al. (2016) also collected PIV images from the bottom at 110 meters behind the tugboat Tractor C-14 during the study period and evaluated the bottom elevation changes due to the tugboat propeller wash using the PIV images captured at different times. In this study, we compared the erosion depths simulated for an EFDC+ model grid cell at a given PIV location to the PIVmeasured erosion depths. Note that the model-to-data comparison for erosion depths is conducted based on the model grid cell, whereas the comparison analyses for near-bed velocity and shear stress were performed based on the sub-grid point. Figure 5.3 displays the model grid cells, propeller wash sub-grid points, and PIV location speciﬁed in this study.

- Figure 5.6 compares the PIV-measured data and EFDC+ model results for the propeller washinduced erosion depth. In this ﬁgure, the x-axis shows relative times (in min) from the time the propeller-induced velocity was ﬁrst detected, and the vertical black lines represent the effective starting time for each rpm operation. The y-axis indicates the cumulative erosion depth (in mm) during the study period, showing the depths increasing from top to bottom.


- In Figure 5.6, the measured data (red markers) indicate that bed erosion did not occur during the 20 rpm period, likely due to low shear stress; erosion started while the propeller speed was at 50 rpm. The erosion depth then increased continuously while the propellers were rotating and reached


- 1.85 mm at 34 minutes. The erosion rate (curve slope) was notably higher at 150 rpm than during other periods. When the propellers were brought to a stop (after about 36 min), the erosion depth decreased (indicating bottom elevation increase) as the sediments resuspended during the propeller operations were re-deposited on the sediment bed. The blue line in Figure 5.6 represents the model results for erosion depths from the propeller


##### DSI, LLC 5-9 EFDC+ Propeller Wash



<<<PAGE 60>>>

##### 5. Case Studies



- Figure 5.6: Erosion depth from PIV-measured data and EFDC+ model results at 110 m behind tugboat Tractor C-14.


rotation speed-based simulation (20, 50, 100, 150 rpm), while the green line in the ﬁgure represents the engine power-based simulation (320, 800, 1600, 2400 hp). Overall, the measured erosion depths over the study period were well reproduced in the hp-based simulation (green line). The hp-based model simulated the propeller wash erosion starting at the 50 rpm (800 hp) period and predicted the erosion depth of 1.82 mm at 34 minutes, which is consistent with the observed erosion behavior. Additionally, the model reproduced the deposition of the resuspended sediment after the 36 minutes of the propeller operations. From the rpm-based simulation (blue line), the propeller wash erosion did not occur until 17 minutes after the start time, likely due to the low shear stress predicted for the 20 and 50 rpm periods. Consequently, the maximum erosion depth (1.55 mm) was also underestimated by about 16%, although the temporal trend of the erosion depth was sufﬁciently well reproduced by the rpm-based model.

This study also evaluated the model performance quantitatively using the Nash-Sutcliffe Efﬁciency (NSE) coefﬁcient, which is calculated as:

where,

N

(Mi −Oi)2 N

∑

i=1

NSE = 1−

(Oi −O)2

∑

i=1

(5.2)

##### DSI, LLC 5-10 EFDC+ Propeller Wash



<<<PAGE 61>>>

##### 5. Case Studies



- N : number of observations

- O : average of observed erosion depths Oi : observed erosion depth at ith data point Mi : simulated erosion depth corresponding to ith data point


The NSE coefﬁcient can range from -∞ to 1 where NSE of 1 indicates that the model reproduces the observed data perfectly and NSE of 0 indicates that the model prediction is as accurate as of the average of the observed values. The resultant NSE value was 0.80 for the propeller revolution speed-based simulation and 0.97 for the engine power-based simulation. Thus, the quantitative evaluation also suggests that the EFDC+ propeller wash model can accurately predict propeller wash-induced bed erosion at berthing/docking facilities in harbor areas.

##### DSI, LLC 5-11 EFDC+ Propeller Wash



<<<PAGE 62>>>

##### 5. Case Studies



## 5.3. Demonstration of Sediment Transport Processes

This section presents test cases that demonstrate how the propeller wash modeling features work with the two sediment transport modules available in EFDC+: Original EFDC Sediment Transport (Van Rijn, 1984a,b,c) and SEDZLJ Sediment Transport (Jones and Lick, 2001). This demonstration examines several components (i.e., scour proﬁle, erosion depth, and sediment mass balance) to evaluate whether the EFDC+ simulation results provide a good representation of the sediment transport processes induced by the propeller wash.

- Figure 5.7 illustrates the synthetic channel’s dimensions with the sediment bed and propeller setup used for the demonstration models. We determined these model conditions based on the site and propeller dimensions used in the San Diego Bay tugboat test case (see Section 5.2). Speciﬁcally, the modeled channel had a length of 500 m, a width of 100 m, a uniform 0 m elevation of the channel bottom (i.e., sediment bed surface), and a water depth of 10 m. The ambient background velocity of the water was 0.1 m/s ﬂowing from west to east, and the model allowed ﬂow and sediments to exit without reﬂection through an open boundary at the east end of the model domain. The horizontal model grid had a uniform cell size of 5 m × 5 m over the model domain, and the vertical grid used ﬁve layers for the water column. The channel’s sediment bed had a 0.1 m thickness using a vertical grid of ﬁve layers (2 cm thick each layer). The physical and erosional properties of the sediment bed (i.e., particle sizes, erodibility, and porosity) were speciﬁed differently for each demonstration model depending on the purpose of each test. The demonstration models implemented geomorphic feedback between hydrodynamic and sediment transport simulations (i.e., bed elevation changes predicted by the sediment transport computation update the bathymetry used in the hydrodynamic computation for the next time step), leading to more appropriate ﬂow ﬁeld and sediment transport behavior.


A four-blade propeller with a 2.5 m diameter was placed 5.5 m above the sediment bed surface at a ﬁxed location, as shown in Figure 5.7. Table 5.3 provides the detail speciﬁcations of the modeled propeller. The sub-grid conﬁguration for the propeller was set as 400 m in length and 100 m in width, including 160 points in the longitudinal dimension and 40 points in the lateral dimension. All test cases had the same total simulation period of 120 minutes. The propeller was operated

- at the ﬁxed location to generate a propeller wash eastward for the ﬁrst 30 minutes during the simulation; the propeller was then stopped, and the resuspended particles were re-deposited to the sediment bed for the remaining 90 minutes. For each test case, the demonstration models applied different fractions of the maximum engine power (5,000 hp) to examine the propeller wash effects on the sediment bed. Note that, all demonstration models were set to simulate a hydrodynamic ﬂow ﬁeld without propeller momentum effects (see “ISPROPWASH” = 1 in Section 4.1). Hence, during the simulation, the resuspended sediments in the water column were transported downstream only by the background ambient current (0.1 m/s ﬂowing from west to east).


##### DSI, LLC 5-12 EFDC+ Propeller Wash



<<<PAGE 63>>>

##### 5. Case Studies



Figure 5.7: Channel dimensions used for sediment transport demonstration models.

Table 5.3: Propeller speciﬁcations used for the sediment transport demonstration models.

Characteristics Values Number of blades 4 Propeller diameter 2.5 m Propeller hub diameter 0.2 m Blade area ratio 0.8 Pitch ratio 1.0 Thrust coefﬁcient 0.45 Maximum engine power 5,000 hp

##### DSI, LLC 5-13 EFDC+ Propeller Wash



<<<PAGE 64>>>

##### 5. Case Studies



### 5.3.1 Original EFDC Sediment Transport Module

The Original EFDC Sediment Transport approach applies separate computation processes for cohesive and non-cohesive sediments based on van Rijn’s sediment transport equations (Van Rijn, 1984a,b,c). Therefore, this study conducted separate demonstration tests for sediment beds with cohesive particles and non-cohesive particles.

#### 5.3.1.1 Cohesive Sediments

The ﬁrst demonstration model used a representative cohesive sediment bed condition consisting of 50% ﬁne silt (particle size ds = 16 µm) and 50% coarse silt (ds = 50 µm), with a porosity of 0.8. The physical and erosional properties of the cohesive sediment bed were set to be uniform horizontally and vertically. For the propeller wash computation, the model applied a constant engine power of 500 hp (i.e., 10% of the maximum engine power) for the ﬁrst 30 minutes of the simulation.

- Figure 5.8 displays the 2D plan view of the bottom elevations from the cohesive sediment bed simulation. The model provided a single value of bottom elevation for each grid cell, and this ﬁgure applies a smoothed color map for display purposes. In this ﬁgure, the colors represent the changes in bottom elevation following the 2-hour simulation; the red area indicates a decrease in bottom elevation (erosion), and the blue area indicates an increase in bottom elevation (deposition). A gray marker indicates the propeller location. The model results showed that the propeller wash formed a major scour area starting at about 20 m downstream of the propeller; the maximum scour depth of 6.7 cm was predicted at 45 m downstream. The propeller wash-induced erosion then decreased with distance and dispersed laterally until about 300 m away from the propeller. The simulation results also indicated that the sediments resuspended by the propeller wash were redeposited to the sediment bed outside the propeller wash-impacted erosional area, with the predicted deposition thickness reaching a maximum of 0.3 cm.
- Figure 5.9 presents the longitudinal proﬁles of the bottom elevations aligned with the propeller axis at different times (5, 10, 20, 30, and 120 minutes) during the simulation. Overall, the model provided similar longitudinal scour patterns at all the times considered. The propeller wash-induced scour started at 20 m behind the propeller, and the erosion depth increased dramatically until 45 m downstream, where the maximum scour depth of 6.7 cm occurred. After the maximum scour point, the erosion depth decreased with distance. In terms of temporal variation, the scour depth increased approximately linearly with the time during which the propeller was rotating (5, 10, 20, and 30 minutes). At the maximum erosion location, the model predicted scour of 2.2 cm for the ﬁrst 10 minutes, 2.3 cm for the next 10 minutes, and 2.2 cm for the last 10 minutes of the propeller rotating period. At the end of the simulation (120 minutes), the bottom elevations 100 m downstream and farther from the propeller increased slightly compared to the bottom elevations at 30 minutes. This result indicates that the propeller wash-induced resuspended sediments were transported downstream as suspended load and were redeposited to the sediment bed after the propeller stopped.
- Figure 5.10 presents the changes in thickness of the ﬁve sediment bed layers during the simulation at the cell where the maximum scour occurred (45 m behind the propeller), along with the


##### DSI, LLC 5-14 EFDC+ Propeller Wash



<<<PAGE 65>>>

##### 5. Case Studies



##### Figure 5.8: Plan view of bottom elevations simulated from a cohesive sediment bed model.

##### Figure 5.9: Scour proﬁles at different times from the cohesive sediment bed simulation.

##### DSI, LLC 5-15 EFDC+ Propeller Wash



<<<PAGE 66>>>

##### 5. Case Studies



corresponding bottom elevation changes. In this ﬁgure, Bed Layer 5 indicates the top layer, and Bed Layer 1 represents the bottom layer of the sediment bed (the Original EFDC Sediment Transport approach assigns a sediment bed layer number from bottom to top). At the beginning of the simulation, each bed layer had a 2 cm thickness speciﬁed as an initial model condition. When the simulation started, the thickness of Bed Layer 5 (top layer) decreased as the propeller wash caused the erosion at this cell (channel bottom elevation decrease). Once the top layer’s thickness reached zero (after about 8 minutes), Bed Layer 4 began to be eroded as this layer was exposed to the sediment bed surface (water-sediment interface). This erosion process continued for the bed layers below for the 30 minutes during which the propeller wash was applied. Bed Layers 2, 3, 4, and 5 showed an almost identical decrease rate (slope) of their thickness during the simulation, because this demonstration model deﬁned the physical and erosional properties of the sediment bed to be uniform horizontally and vertically. After the 30 minutes of propeller rotating, the total bed layer thickness was reduced from the original 10 cm to 3.3 cm (2 cm for Bed Layer 1 and 1.3 cm for Bed Layer 2), which is consistent with the resultant bottom elevation of -6.7 cm. Through this analysis, we were able to check how the sediment bed layers behaved vertically while the sediment bed was being scoured due to the propeller wash.

- Figure 5.10: Time series of bed layer thickness at the maximum scour cell from the cohesive sediment bed simulation.


Table 5.4 compares the sediment mass in water layers and sediment bed layers between the beginning and end of the simulation. This table also presents the total mass ﬂux of sediments exiting the model domain through the eastern open boundary during the simulation. Overall, both ﬁne silt and coarse silt classes showed a negligible difference between the beginning and end of the simulation (less than 0.01% of the total mass). The slight difference in the total mass occurred probably

##### DSI, LLC 5-16 EFDC+ Propeller Wash



<<<PAGE 67>>>

##### 5. Case Studies



because the cumulative mass ﬂux exiting the domain was calculated by integrating the 1-minute interval model outputs of instantaneous mass ﬂux. Therefore, the mass comparison results suggest that the total sediment mass is conserved within the system while EFDC+ implements the propeller wash computation linked with the sediment transport processes.

As shown in Table 5.4, at the beginning of the simulation, ﬁne silt and coarse silt materials were uniformly distributed over the ﬁve sediment bed layers, with no sediments in the water layers. At the end of the simulation, the water layers contained 3,253 kg of ﬁne silt and 44 kg of coarse silt; these materials are the resuspended sediments that were remaining the water column at the end of the simulation. The sediment bed layers showed more mass decrease for ﬁne silt than for coarse silt. Moreover, 28,312 kg of ﬁne silt left the model domain through the downstream end open boundary during the simulation, which was about four times more than the mass of coarse silt exiting the domain (7,059 kg). These results are consistent with expected sediment transport behaviors. Fine silt particles (ds = 16 µm) are more easily mobilized than coarse silt particles (ds = 50 µm). Furthermore, ﬁne silt particles have a much lower settling velocity (0.02 cm/s) than coarse silt particles (0.22 cm/s), so resuspended ﬁne silt stays longer in the water column and can travel further downstream with the ambient current.

- Table 5.4: Sediment mass distributions at the beginning and end of the cohesive sediment bed simulation.


Fine Silt Coarse Silt

Initial Mass Final Mass Initial Mass Final Mass (kg) (kg) (kg) (kg)

Water Layers 0 3,253 0 44 Bed Layer 5 (Top) 278,250 252,541 278,250 276,634 Bed Layer 4 278,250 273,451 278,250 273,805 Bed Layer 3 278,250 277,257 278,250 277,312 Bed Layer 2 278,250 278,117 278,250 278,130 Bed Layer 1 (Bottom) 278,250 278,250 278,250 278,250 Flux Exiting Domain 0 28,312 0 7,059

Total 1,391,250 1,391,181 1,391,250 1,391,234

Through this test case, we conﬁrmed that the EFDC+ propeller wash module can reliably simulate the resuspension processes for cohesive sediment particles based on van Rijn’s theory for suspended load transport (Van Rijn, 1984b).

##### DSI, LLC 5-17 EFDC+ Propeller Wash



<<<PAGE 68>>>

##### 5. Case Studies



#### 5.3.1.2 Non-cohesive Sediments

The second demonstration model used a representative non-cohesive sediment bed condition consisting of 10% ﬁne sand (ds = 200 µm), 25% medium sand (ds = 400 µm), 30% coarse sand (ds = 800 µm), and 35% very coarse sand (ds = 1,600 µm), with a porosity of 0.4. Like the cohesive sediment bed case, the physical and erosional properties of the non-cohesive sediment bed were set to be uniform horizontally and vertically. For the propeller wash computation, the model applied a constant engine power of 2,500 hp (50% of the maximum engine power) for the ﬁrst 30 minutes of the simulation. This demonstration model was also used for testing bedload transport processes of non-cohesive sediment particles induced by propeller wash.

- Figure 5.11 displays the 2D plan view of the bottom elevations from the non-cohesive sediment bed simulation. This ﬁgure presents the changes in bottom elevations following the 2-hour simulation using a smoothed color map; red for net erosion areas and blue for net deposition areas. A gray marker shows the propeller location. The model results indicate that the propeller wash formed a major scour area between approximately 20 m and 50 m downstream of the propeller; the predicted maximum scour depth in this area was 1.4 cm, occurring 35 m behind the propeller. The sediments eroded by the propeller wash were redeposited to the sediment bed from just behind the major scour hole until approximately 140 m from the propeller, and the predicted maximum crest in the deposition area was about 0.6 cm.


- Figure 5.11: Plan view of bottom elevations simulated from a non-cohesive sediment bed model.
- Figure 5.12 shows the bottom elevation proﬁles aligned with the propeller axis at different times (5, 10, 20, 30, and 120 minutes) during the simulation. Generally, the scour proﬁles from all the times


##### DSI, LLC 5-18 EFDC+ Propeller Wash



<<<PAGE 69>>>

##### 5. Case Studies



considered showed a scour hole between 20 m and 50 m behind the propeller and a deposition mound downstream of the scour hole. The scour hole size and maximum erosion depth increased with the amount of time the propeller was rotating (5, 10, 20, and 30 minutes). Unlike the cohesive sediment bed simulation, the bottom elevations at 120 minutes (end of the simulation) were almost identical to the bottom elevations at 30 minutes (i.e., the purple line overlaps the green line along their entire length). This result suggests that the non-cohesive sediments eroded by the propeller wash were transported downstream primarily as bedload (rolling or sliding along the sediment bed surface), so deposition of the resuspended sediments was not observed after the propeller stopped.

To examine the bedload effect, this study ran a model using the same conditions but deactivating the bedload computation process for the Original EFDC Sediment Transport module. In this case, the model was set up to simulate the sediment transport as a suspended load only if a shear velocity was greater than the settling velocity of non-cohesive sediment particles, which requires a higher shear velocity than bedload. The bottom elevation following the 2-hour simulation without bedload is shown as a gray dashed line in Figure 5.12, and the resultant scour proﬁle shows a negligible change in the bottom elevations (erosion less than 0.5 mm). This result supports the idea that the propeller wash would transport the non-cohesive sediments mainly as bedload, rather than resuspension, for this demonstration model condition.

- Figure 5.12: Scour proﬁles at different times from the non-cohesive sediment bed simulation.

This study investigated the propeller wash-induced scour proﬁles by varying the applied engine powers to the propeller based on the non-cohesive sediment bed model conditions presented above.

- Figure 5.13 presents the bottom elevations aligned with the propeller axis following the 2-hour simulations while applying ﬁve different engine power levels: 20%, 40%, 60%, 80%, and 100% of


##### DSI, LLC 5-19 EFDC+ Propeller Wash



<<<PAGE 70>>>

##### 5. Case Studies



the maximum engine power of 5,000 hp. The model results indicated that the scour hole depth increased with applied engine power, and all ﬁve simulations predicted the maximum scour location to be approximately 35 m behind the propeller. The deposition mound height also increased with applied power, and the predicted deposition crest was located farther downstream from the scour hole as the applied engine power increased. These simulated behaviors were the expected results, because a greater propeller wash would erode more particles from the sediment bed and transport them farther downstream as bedload.

- Figure 5.13: Scour proﬁles of non-cohesive sediment bed simulated by different propeller powers.

In addition to the applied power impact analysis, this study examined the bottom elevation changes due to propeller wash by applying different particle sizes to the non-cohesive sediment bed. This test used ﬁve representative models: each model deﬁned a sediment bed using a single particle size of ds = 500, 1000, 1500, 2000, and 2,500 µm, which covered the size ranges of medium sand to very ﬁne gravel. For the propeller wash simulation, the models applied a constant power of 4,000 hp (i.e., 80% of the maximum engine power) for the ﬁrst 30 minutes of the simulations.

- Figure 5.14 shows the bottom elevation proﬁles aligned with the propeller axis following the 2hour simulations for the sediment beds with different particle sizes. All ﬁve models predicted the maximum scour area to be about 35 m downstream of the propeller, and the predicted erosion depths were greater for the smaller particle condition, as expected. Accordingly, the deposition mound behind the scour hole had a higher crest and a longer tail downstream for the smaller sediment bed particle simulations. These results indicate that the propeller wash computation for the movements of non-cohesive sediments correctly reﬂected the behavior of different sediment particle sizes.


##### DSI, LLC 5-20 EFDC+ Propeller Wash



<<<PAGE 71>>>

##### 5. Case Studies



- Figure 5.14: Scour proﬁles of non-cohesive sediment bed simulated by different particle sizes.


Through this demonstration, we show that, following van Rijn’s approach (Van Rijn, 1984a), the EFDC+ model can provide a reasonable representation of propeller wash-induced scour for a noncohesive sediment bed, including bedload transport processes.

##### DSI, LLC 5-21 EFDC+ Propeller Wash



<<<PAGE 72>>>

##### 5. Case Studies



### 5.3.2 SEDZLJ Sediment Transport Module

The SEDZLJ approach (Jones and Lick, 2001) uses an advanced sediment transport algorithm that accounts for spatially varied erosion properties of sediment beds. For example, a modeler can determine the erosion rates for the modeled sediment bed as a function of bed depth and applied shear stress by employing ﬁeld core sample measurements (e.g., Sediment Erosion at Depth Flume [SEDFlume] data) or user-deﬁned data. The SEDZLJ method has been widely used with EFDC models because it can adequately represent site-speciﬁc erosion properties of sediment beds (Thanh et al., 2008). Currently, the United States Environmental Protection Agency (USEPA) considers the SEDZLJ algorithm as a preferred standard approach for modeling sediment transport processes in contaminated harbor sites, especially for cohesive sediment beds.

This study examined the EFDC+ propeller wash simulation linked to the SEDZLJ Sediment Transport module, focusing on how the model addresses the vertical variation of sediment bed properties. The SEDZLJ demonstration model used a cohesive sediment bed condition consisting of ﬁne silt (ds = 16 µm) and coarse silt (ds = 50 µm), with a porosity of 0.8. We then deﬁned the physical and erosional properties of the modeled sediment bed to vary vertically for this case. Speciﬁcally, for the ﬁve sediment bed layers, the fraction of ﬁne silt decreased from the top layer (70%) to the bottom layer (30%), whereas the fraction of coarse silt increased from the top layer (30%) to the bottom layer (70%). With regard to the sediment contents and consolidation effects, we also assigned higher erosion rates for upper bed layers and lower erosion rates for lower bed layers. Thus, the demonstration model represented a typical characteristic of a cohesive sediment bed: erodibility is highest at the sediment bed surface and tends to decrease with depth. As we did with the Original EFDC+ cohesive sediment simulation, we applied a constant engine power of 500 hp (i.e., 10% of the maximum engine power) during the ﬁrst 30 minutes of the simulation.

- Figure 5.15 displays the 2D plan view of the bottom elevations following the 2-hour propeller wash simulation using the SEDZLJ Sediment Transport module. A gray marker indicates the propeller location, and the colors represent the changes in bottom elevations: red for net erosion areas and blue for net deposition areas. Overall, the SEDZLJ simulation resulted in horizontal distributions for the bottom elevation changes that were similar to those produced by the Original EFDC cohesive sediment simulation (see Figure 5.8), since the two simulations used the same particle sizes (16 µm and 50 µm). In the case of the SEDZLJ simulation, the propeller washinduced erosion started at about 20 m downstream of the propeller, and the maximum scour of 6.2 cm was observed at 45 m behind the propeller. The erosion depth then decreased with distance and dispersed laterally until about 200 m away from the propeller. The model predicted the redeposition of the resuspended sediments outside the propeller wash-impacted erosion area, and the deposition thickness reached a maximum of 0.2 cm.
- Figure 5.16 presents the scour proﬁles aligned with the propeller axis at different times (5, 10, 20, 30, and 120 minutes) during the SEDZLJ simulation. Overall, the simulated bottom elevations showed similar longitudinal patterns over all the times considered here. The propeller washinduced erosion started at 20 m behind the propeller, and the scour depth increased dramatically until 45 m downstream. After the maximum scour point, the erosion depth decreased gradually with distance. The scour depth increased with the time during which the propeller was rotating (5, 10, 20, and 30 minutes). The bottom elevations then slightly increased at the end of the simulation


##### DSI, LLC 5-22 EFDC+ Propeller Wash



<<<PAGE 73>>>

##### 5. Case Studies



##### Figure 5.15: Plan view of bottom elevations simulated from a SEDZLJ sediment transport model.

##### Figure 5.16: Scour proﬁles at different times from the SEDZLJ sediment transport simulation.

##### DSI, LLC 5-23 EFDC+ Propeller Wash



<<<PAGE 74>>>

##### 5. Case Studies



(120 minutes) in the area 75 m downstream and farther from the propeller, which reﬂected the deposition of the resuspended particles after the propeller stopped. At the location of maximum scour (6.2 cm), the SEDZLJ model predicted more erosion for the earlier period and less erosion for the later period, whereas the Original EFDC cohesive bed model provided approximately constant erosion rates over time (see Figure 5.9). Notably, at the location of maximum scour, the SEDZLJ simulation predicted a scour depth of 3.1 cm for the ﬁrst 10 minutes, 1.9 cm for the next 10 minutes, and 1.2 cm for the last 10 minutes of the propeller rotating period. These results indicate that sediment erosion rates decreased as the scour hole got deeper; this behavior is consistent with the sediment bed conﬁguration of the SEDZLJ model in which we deﬁned upper bed layers to have higher erosion rates than lower bed layers.

- Figure 5.17 shows the changes in the sediment bed layer thickness during the SEDZLJ simulation at the maximum scour cell (45 m behind the propeller), along with the corresponding bottom elevation changes. Since the SEDZLJ approach assigns a sediment bed layer number from top to bottom, Bed Layer 1 indicates the top layer, and Bed Layer 5 represents the bottom layer of the sediment bed. The SEDZLJ approach also applies two additional layers on the top of the ﬁve bed layers to compute the sediment mass exchange process between the water column and sediment bed. The ﬁrst of these additional layers is the active layer, where bedload, suspension, and deposition from the water column occur. The second additional layer is the deposition layer; it receives the deposited sediments from the active layer or provides the sediments to the active layer for bedload or suspension. While these two additional layers have a zero thickness as an initial model condition, the active layer thickness varies from about 2 to 10 times the particle sizes, and the deposition layer thickness depends on the sediment transport conditions during the simulation.


- In Figure 5.17, Bed Layers 1 to 5 had a 2 cm thickness at the beginning of the simulation. Once the propeller wash started scouring the sediment bed at this cell, Bed Layer 1 was eroded ﬁrst, and the thickness of Bed Layer 2 decreased after Bed Layer 1 reached zero thickness. As we observed in the Original EFDC simulation (see Figure 5.10), this scour process continued for the bed layers below for the 30 minutes during which the propeller wash was applied. The active and deposition layers each had a thickness of less than 0.1 mm during the simulation. Notably, the SEDZLJ model results showed a different change rate in thickness for each of Bed Layers 1, 2, 3, and 4, with steeper decreases for the thickness of the upper layers. The thickness of Bed Layer 1 reached zero after only 6 minutes from the time this layer started to erode, whereas Bed Layer 3 took about 14 minutes to reach zero thickness. As discussed above, these results were also expected, because this demonstration model speciﬁed that the physical and erosional properties of the sediment bed vary vertically, having greater erosion rates in upper bed layers than in lower bed layers.


- Table 5.5 presents the sediment mass distribution in water layers and sediment bed layers from the SEDZLJ simulation, along with the total mass ﬂux of sediments exiting the model domain through the open boundary. Overall, these results indicate that the simulation conserved the total sediment mass for both ﬁne silt and coarse silt classes; the total mass difference between the beginning and end of the simulation is less than 0.01% of the total. As an initial condition, the upper bed layers contained more ﬁne silt than coarse silt, and the lower bed layers had the reverse. There were no sediments in the water, active, and deposition layers at the beginning. Following the 2-hour simulation, the water layers included 2,551 kg of ﬁne silt and 19 kg of coarse silt; these were the resuspended sediments remaining in the water column. The active layer had almost the same


##### DSI, LLC 5-24 EFDC+ Propeller Wash



<<<PAGE 75>>>

##### 5. Case Studies



- Figure 5.17: Time series of sediment bed layer thickness at the maximum scour cell from the SEDZLJ sediment transport simulation.


Table 5.5: Sediment mass distributions at the beginning and end of the SEDZLJ sediment transport simulation.

Fine Silt Coarse Silt

Initial Mass Final Mass Initial Mass Final Mass (kg) (kg) (kg) (kg)

Water layers 0 2,551 0 19 Active layer (Top) 0 656 0 698 Deposition layer 0 6,703 0 10,682

- Bed layer 1 389,550 358,753 166,950 158,349
- Bed layer 2 333,900 329,649 222,600 219,766
- Bed layer 3 278,250 277,409 278,250 277,409
- Bed layer 4 222,600 222,577 333,900 333,866
- Bed layer 5 (Bottom) 166,950 166,950 389,500 389,550 Flux exiting domain 0 25,889 0 867 Total 1,391,250 1,391,137 1,391,250 1,391,207


##### DSI, LLC 5-25 EFDC+ Propeller Wash



<<<PAGE 76>>>

##### 5. Case Studies



amount of coarse silt as ﬁne silt but these amounts were minimal. The deposition layer contained more coarse silt mass (10,682 kg) than ﬁne silt mass (6,703 kg), since coarse silt particles were more accessible to be redeposited than ﬁne silt particles. Additionally, about 30 times more ﬁne silt (25,889 kg) than coarse silt (867 kg) left the model domain through the downstream end during the simulation. These results also represent the expected sediment transport behaviors regarding the sediment particle sizes, as addressed earlier with respect to the Original EFDC cohesive sediment case (Table 5.4).

The ﬁndings from this test case demonstrated that the EFDC+ model was able to properly perform the propeller wash-induced scour and resuspension processes based on the SEDZLJ Sediment Transport approach (Jones and Lick, 2001), accounting for the vertical variability in sediment bed properties.

##### DSI, LLC 5-26 EFDC+ Propeller Wash



<<<PAGE 77>>>

##### 5. Case Studies



## 5.4. Demonstration of Sediment Resuspension

This section presents a demonstration of the EFDC+ modeling features for sediment resuspension processes induced by propeller wash from moving ships. For this analysis, we developed two demonstration models linked to the SEDZLJ Sediment Transport module. These test cases also examine the impacts of propeller momentum (see Step 12 in Chapter 3) on ﬂow velocity ﬁeld and the movement of resuspended sediments.

### 5.4.1 Long Straight Channel with Two Moving Ships

The ﬁrst demonstration model used a synthetic, long, straight channel with two tugboats moving. The modeled channel had a length of 3,000 m, a width of 200 m, and a water depth of 10 m. The channel’s sediment bed was 1.4 m deep and consisted of 31% coarse silt, 51% ﬁne sand, and 18% coarse sand. The horizontal model grid applied a uniform cell size of 10 m × 10 m over the model domain. The vertical grid used ten layers for the water column and ﬁve layers for the sediment bed. The background ambient velocity of the water was 0.1 m/s ﬂowing from east to west. Table 5.6 provides the characteristics of the two modeled tugboats (Tractor C-13 and Tractor C-14) moving in opposite directions.

Table 5.6: Properties of Tractor C-13 and Tractor C-14. Tractor C-13 Tractor C-14

Ship length 50.00 m 28.65 m Ship beam 18.00 m 10.36 m Ship draft 3.35 m 3.35 m Gross tonnage 300 190 Installed engine power 5,800 hp 4,800 hp Number of propellers 2 2 Propeller diameter 2.50 m 2.28 m Distance from water surface to propeller 4.88 m 4.88 m Applied revolution speed 130 rpm 120 rpm Moving direction East to West West to East Start position in x direction 2,800 m 100 m Start position in y direction 155 m 45 m

Figures 5.18 and 5.19 present the ﬂow velocity ﬁeld and Total Suspended Sediments (TSS) concentrations in water layers (at a time snapshot) from the model simulations when excluding and including the propeller momentum, respectively. In each ﬁgure, the top panel is the 2D horizontal view of the channel, showing depth-averaged TSS concentrations (in mg/l using a color ramp) and the two ship tracks (gray marker size reﬂecting the ship size). The middle and bottom panels show the vertical proﬁles through the paths of Tractor C-13 and Tractor C-14, respectively. The color ramp represents the TSS concentrations and the vector arrows indicate the magnitude and direction of the ﬂow velocity.

##### DSI, LLC 5-27 EFDC+ Propeller Wash



<<<PAGE 78>>>

##### 5. Case Studies



- In Figure 5.18, the top panel shows that the model simulated the depth-averaged TSS concentrations increasing behind the two ships as they traveled through the water. The simulated TSS concentrations behind the larger ship (Tractor C-13) were greater thant the smaller ship (Tractor C-14). In the two bottom panels, the vertical proﬁles show the sediment resuspension caused by the ship movement, which increased the TSS concentrations in water column. The propeller washinduced TSS concentrations were higher at the bottom than at the water surface, and they were also greater for the larger ship than the smaller ship. As the ships proceeded, the resuspended sediments in the path traveled behind the ships were redeposited to the sediment bed, causing a TSS concentration reduction in the water column. In this case, the velocity vectors represent only the ambient currents because the model computed the hydrodynamic ﬂow ﬁeld not including the propeller efﬂux momentum.


Figure 5.19 demonstrates that the model results for both TSS concentration and velocity distributions differ signiﬁcantly depending on whether the simulation added the propeller momentum to the ﬂow ﬁeld or not. In the top panel, the TSS concentrations dispersed more in both longitudinal and lateral directions, compared to Figure 5.18. In the two bottom panels, the vertical proﬁles show that the velocity vectors near the ships reﬂect the change in water ﬂow direction due to propeller movement. The highest velocities occurred at approximately at 5 m depth, which corresponds to the distance from the water surface to the propeller (4.88 m). They also show that the magnitude of the velocity vectors near the larger ship were greater than those near the smaller ship. The resultant ﬂow velocities notably affect the movement of the resuspended sediments (e.g., advection, dispersion, and diffusion). Speciﬁcally, the model simulated the TSS concentrations spreading much more in both longitudinal and vertical directions compared to the vertical proﬁles in Figure 5.18. The water velocities behind each ship stabilized after a few hundred meters; consequently, the TSS concentrations decreased with distance. Nevertheless, the TSS concentrations simulated at locations far behind the ship were quite high near the water surface in this case. These model results demonstrate that the EFDC+ can predict the sediment resuspension and subsequent transport processes associated with propeller wash-induced currents.

##### DSI, LLC 5-28 EFDC+ Propeller Wash



<<<PAGE 79>>>

DSI,LLC5-29EFDC+PropellerWash

Figure 5.18: TSS concentrations and velocity ﬁeld from a straight channel simulation without propeller momentum effects.

5.CaseStudies

<<<PAGE 80>>>

DSI,LLC5-30EFDC+PropellerWash

Figure 5.19: TSS concentrations and velocity ﬁeld from a straight channel simulation including propeller momentum effects.

5.CaseStudies

<<<PAGE 81>>>

##### 5. Case Studies



### 5.4.2 San Diego Bay Tugboat Test Site

The second demonstration model was developed based on the San Diego Bay tugboat model we used for the validation of near-bed velocity, bottom shear stress, and erosion depth. The speciﬁed model domain, bathymetry, hydrodynamic conditions, and sediment bed conﬁgurations were the same as described in Section 5.2. For the propeller wash simulation, the model also used the same tugboat and sub-grid conﬁgurations presented in Section 5.2, but this demonstration evaluated tugboat Tractor C-14 operating on an approximately circular path around the model domain at 105 rpm for two hours (12:00 to 14:00 on July 19th, 2012).

Figures 5.20 presents the model results for the velocity ﬁeld and TSS concentrations at 13:52 (near the end of the simulation), comparing two situations: when the model excluded (left panel) vs. included (right panel) the propeller momentum effects for the hydrodynamic ﬂow ﬁeld computation. In each panel, a black line shows the ship path during the two-hour simulation. Gray vector arrows represent the magnitude and direction of the depth-averaged ﬂow velocity, and a color ramp displays the depth-averaged TSS concentrations (in mg/l).

In Figure 5.20, both velocity distributions and TSS concentrations were signiﬁcantly different between the two simulations. When the model ignored the propeller momentum effects (left panel), the ﬂow velocities were negligible, since the ﬂow ﬁeld only represented the background tidal currents, and the TSS concentrations of the resuspended sediments were distributed along the ship’s path. As the resuspended sediments in the path behind the tugboat were redeposited to the sediment bed, the TSS concentrations in the water column decreased over time. On the other hand, when the propeller momentum effects were simulated (right panel), the model predicted high-velocity magnitudes behind the tugboat, reﬂecting the ﬂow direction due to the propeller movement. Consequently, the resuspended sediments were transported more actively, presenting more mixing and dispersion of the TSS concentrations behind the tugboat. Additionally, this simulation shows eddies at the southeast and north sides of the model domain, where the areas were restricted by the bank and pier structures. Moreover, the TSS concentration distributions indicate that the simulated eddies also notably inﬂuenced the movement of the resuspended sediments. These results would also support EFDC+’s modeling ability to predict the process of the propeller wash-induced currents conveying the resuspended sediments further, which might represent a meaningful sediment load to adjacent areas.

##### DSI, LLC 5-31 EFDC+ Propeller Wash



<<<PAGE 82>>>

DSI,LLC5-32EFDC+PropellerWash

- Figure 5.20: TSS concentrations and velocity ﬁeld from San Diego Bay tugboat simulations without vs. with propeller momentum.


5.CaseStudies

<<<PAGE 83>>>

##### 5. Case Studies



## 5.5. Application to Kingston Ferry Terminal

This case study presents the application of the EFDC+ model to estimate the impacts of propeller wash on scour around the docking facilities of a ferry terminal in Kingston, WA. For this study, DSI received propeller wash data from the Washington State Department of Trasnportation (WSDOT) and the University of Washington (UW) Applied Physics Lab, which were collected at the Kingston ferry terminal as reported in Kastner et al. (2019). The ﬁeld data include ADV measurements for near-bed ﬂow velocity, historical bottom elevation records at piling structures, and detailed speciﬁcations for three Kingston ferries. Additionally, through a conference call with a captain of Washington State Ferries (WSF), DSI obtained information on how the engines and propellers are operated while the ferries are arriving and departing at the terminal. This section provides the background of the Kingston ferry terminal propeller wash studies, model conﬁguration, and a discussion of the model results.

### 5.5.1 Background

The Kingston ferry terminal has three slips, which are docking facilities that can receive and launch ferry ships, as shown in Figure 5.21. WSDOT has monitored the bottom elevations around the structural pilings annually, observing severe seabed scour at Slip 1 in recent years. Speciﬁcally, a subsurface bench in the sediment bed near Slip 1 has eroded shoreward and migrated through the bridge seat toward the onshore structures, causing concern for terminal safety. Kingston ferry terminal Slip 1 is actively used for the Kingston-Edmonds ferry route across Puget Sound, operating a total of 46 trips between Kingston and Edmonds every day using three ferries: Motor Vessel (M/V) Puyallup, M/V Spokane, and M/V Walla Walla.

- Figure 5.21 shows the AIS-tracked ship paths of these three ferries on March 18, 2018, indicating that a majority of the ferry trafﬁc occurred in Slip 1. Table 5.7 presents the characteristics of the three ferries. M/V Puyallup can carry a maximum of 2,499 passengers and 202 vehicles with 16,000 hp engine power. Both M/V Spokane and M/V Walla Walla, which are smaller than M/V Puyallup, have a maximum capacity of 2,000 passengers and 188 vehicles with 11,500 hp engine power. These ferries are double-ended with symmetric propulsion systems, as shown in
- Figure 5.22, allowing the ferries to arrive and depart at the terminal without changing orientation. Propeller wash from the ferries directly impacts the slip, since the slip-facing propeller is active for braking on arrivals and propulsion on departures (Kastner et al., 2019).


As part of efforts to mitigate erosion at this site, Kastner et al. (2019) conducted a ﬁeld study to investigate the inﬂuence of ferry trafﬁc on the severe erosion at the Kingston ferry terminal. They deployed two ADVs on the base of the north and south bridge seat pilings at Slip 1 from March 15 to March 28, 2018, to measure the ﬂow velocities close to the seabed, as shown in Figure 5.21. The deployment elevation was -9.8 m for the north piling and -5.9 m for the south piling (MLLW vertical datum), which were dependent on the seabed bottom elevation at each location. During the measurement period (March 15-28, 2018), the ADVs collected the velocity data in 512-second bursts followed by 208 seconds of no collection, for a total cycle of 12 minutes at a frequency of 16 Hz. The survey found that the peak ﬂow velocities observed during the ferry

##### DSI, LLC 5-33 EFDC+ Propeller Wash



<<<PAGE 84>>>

##### 5. Case Studies



Figure 5.21: Aerial image of Kingston ferry terminal, AIS-tracked ship paths for three ferries on March 18, 2018, with ADV sensor location diagram (after Kastner et al., 2019).

Table 5.7: Ship and propeller characteristics of three ferries on the Kingston-Edmonds route.

M/V Spokane M/V Walla Walla

Ship Name M/V Puyallup

Class Jumbo Mark II Jumbo Passenger Capacity 2,499 2,000 Vehicle Capacity 202 188 Ship length 140 m 134 m Ship beam 28 m 26 m Ship draft 5.6 m 5.5 m Service speed 18 knots 18 knots Installed engine power 16,000 hp 11,500 hp Maximum propeller speed 210 rpm 180 rpm Propeller diameter 3.962 m 3.962 m Number of blades 5 4 Blade area ratio 0.75 0.6 Pitch ratio 0.96 1.05 Distance from ship stern to propeller 7.0 m 6.7 m Distance from ship stern to AIS antenna 114.5 m 110.0 m Distance from ship bottom to propeller axis -2.2 m -2.0 m

##### DSI, LLC 5-34 EFDC+ Propeller Wash



<<<PAGE 85>>>

##### 5. Case Studies



Figure 5.22: Side view of M/V Puyallup.

departures were 30 to 50 times greater than the ﬂow velocities under quiescent conditions. Using the ADV-measured velocity data, Kastner et al. (2019) also calculated the Reynolds shear stress (Chou, 1945), which addresses longitudinal and lateral velocity ﬂuctuations by assuming that the turbulence is isotropic and the ﬂow is steady. The bottom shear stresses during ferry arrivals and departures were estimated to be 10 to 100 times greater than during the quiescent periods. The estimated bottom shear stresses were higher during departures than during arrivals, which might be due to higher propeller speeds when accelerating the ferries for departures. Moreover, lower tidal stages corresponded to higher bottom shear stresses because the ferries’ propeller was closer to the seabed when the water level was low. Accordingly, the shallower seabed location (-5.9 m depth at the south piling) was also exposed to higher shear stress than the deeper seabed location (-9.8 m depth at the north piling).

### 5.5.2 Model Development

In this study, DSI developed an EFDC+ propeller wash model for the Kingston ferry terminal area to demonstrate the propeller wash effects of the ferry trafﬁc on the seabed at Slip 1. Figure 5.23 presents the model grid cells, bottom elevations, ADV locations, and a ferry moored at Slip 1 as an example. The model domain covered about 2.6 km2 using a telescoping horizontal grid with 34,456 cells, applying the smallest cell dimension of 4 m × 4 m to the ferry terminal area and increasing the cell sizes to the outer extents. The vertical grid used ﬁve layers for the water column. We speciﬁed the model bottom elevations combining the publicly available datasets: Digital Elevation

##### DSI, LLC 5-35 EFDC+ Propeller Wash



<<<PAGE 86>>>

##### 5. Case Studies



Model (DEM) data from January 2005 for the entire model domain (Finlayson, 2005) and bottom elevation records at structure pilings in 2018 for the terminal areas (Kastner et al., 2019). The bottom elevations over the entire model domain ranged from -81.21 m to 12.97 m, and the bottom elevations varied between -13.06 m and -0.10 m around the Kingston ferry terminal, based on the MLLW vertical datum.

Figure 5.23: EFDC+ model conditions for the Kingston ferry terminal case.

The study selected the period from 06:00 to 24:00 on March 18th, 2018, for the model simulation because all three ferries were actively running during this period and because ADV-measurements were available. For the hydrodynamic conditions, the model speciﬁed a higher bottom roughness for nearshore areas and applied a time series of tide data to the eastern and northern open boundary cells facing the ocean. Because no sediment data were available to deﬁne the physical or erosion properties of the seabed in the terminal area, the model did not simulate the sediment transport processes for this demonstration. This study compared the simulated bottom shear stress to critical shear stress by sediment size classiﬁcation to predict the approximate conditions for seabed scour due to propeller wash.

For the propeller wash module, the model deﬁned the three ferries and their propellers based on Table 5.7. The sub-grid conﬁguration for each ferry was determined as 1,200 m in length and 400 m in width, including 300 points in the longitudinal dimension and 100 points in the lateral dimension. In addition, the model was set to incorporate the propeller momentum effects into the hydrodynamic ﬂow ﬁeld computation (see “ISPROPWASH” = 2 in Section 4.1). The model simulated 22 departure trips of the three ferries; the ship paths were speciﬁed using the AIS tracking data for the simulation period. The arrival trips were not simulated because the EFDC+ model does

##### DSI, LLC 5-36 EFDC+ Propeller Wash



<<<PAGE 87>>>

##### 5. Case Studies



not perform the propeller wash computation for the braking operation on arrivals. As a reminder, previous measurements indicated higher shear stress for departures than for arrivals because of the higher propeller speeds for ferry propulsion. Per the WSF port captain, the ferries are usually operated with about 10 to 20% of total engine power when they are departing the terminal. Based on this information, the model determined the applied power for the departure moments of the three ferries as 20% of their installed engine power. The model then gradually increased the applied power as the ferries got farther away from the terminal, up to 75% of the engine power for sailing at service speed (see Section 4.5.3).

### 5.5.3 Model Results and Discussion

To begin with, the study compared the model results for propeller wash velocities at sub-grid points at the ADV locations to the ADV-measured velocities at those locations. Both the subgrid-based model results and the ADV data represented the propeller wash-induced velocities at the water-sediment interface. Figure 5.24 shows the simulated near-bed ﬂow velocity for sub-grid points behind M/V Walla Walla at 10:26 on March 18th, 2018 (indicating velocity magnitude with a color ramp), along with the ADV locations at the north and south pilings of Slip 1. The highest propeller wash velocity at the seabed appeared at approximately 80 m behind the ferry from this departure event in this ﬁgure. As the ferry moved forward, the sub-grid mesh also migrated, attaching behind the ferry for the subsequent propeller wash computation. Accordingly, this study collected the propeller wash velocities computed from the three ferries’ sub-grid points that passed the north and south ADV locations during the simulation (06:00 to 24:00 on March 18th, 2018) and compared them to the ADV-measured velocities.

Figure 5.25 compares the ADV data and EFDC+ model results for near-bed propeller wash velocity at the south piling (-5.9 m depth) of Slip 1 associated with the 22 ferry departures on March 18th, 2018. In this ﬁgure, red dots indicate the ADV-measured ﬂow velocities with 12-second low-pass ﬁltering, and blue dots represents the sub-grid-based simulation results from the trafﬁc of the three ferries. Overall, the model reasonably reproduced the ADV-observed velocities due to the ferries’ departure, since a strong correspondence is apparent in the timing of the velocity spikes between the data and model results. The difference in the peak velocity magnitude between the data and model results might be due to uncertainties from various sources. For example, the ADVs collected the velocity data in 512-second bursts followed by 208 seconds of no collection for a total cycle of 12 minutes, so the instruments might have failed to observe the peak magnitude if a ferry departure happened during the no ADV sampling period (208 seconds). The AIS data precision with respect to path and heading might cause uncertainty in the ferry positions, affecting the simulation results. Additionally, this study speciﬁed the applied power for the departure moments as 20% of the installed engine power of the three ferries, but the actual applied power could vary depending on weather conditions or the operators’ discretion (i.e., there is no standard procedure for embarking and disembarking, per the WSF port captain).

This study also analyzes the model results for the hydrodynamic ﬂow ﬁeld with the propeller momentum effects. Figure 5.26 displays the simulated depth-averaged ﬂow velocities at 10:28 on March 18th, 2018, when M/V Walla Walla was departing the Kingston ferry terminal. A color ramp indicates the magnitude of the depth-averaged ﬂow velocity at each model grid cell, and the

##### DSI, LLC 5-37 EFDC+ Propeller Wash



<<<PAGE 88>>>

##### 5. Case Studies



##### Figure 5.24: Near-bed ﬂow velocity due to M/V Walla Walla at 10:26 on March 18th, 2018.

##### Figure 5.25: ADV data and EFDC+ model results for near-bed ﬂow velocity at the south piling.

##### DSI, LLC 5-38 EFDC+ Propeller Wash



<<<PAGE 89>>>

##### 5. Case Studies



##### Figure 5.26: Simulated depth-averaged ﬂow velocity ﬁeld due to departure of M/V Walla Walla at 10:28 on March 18th, 2018.

black vector arrows indicate the magnitude and direction of the ﬂow velocities for the model grid cells. Figure 5.26 shows the high-velocity jet behind the ferry as the simulation incorporated the impacts of the propeller momentum into the 3D ﬂow velocity ﬁeld. The propeller momentuminduced velocities remained in the terminal area even after the ferry had traveled far away from the terminal. The remaining propeller-induced velocities dispersed with time and dissipated when the jet reached the nearshore areas.

The study then evaluates the propeller wash effects on seabed scour by investigating the model results for bottom shear stresses caused by the ferry propeller wash at the ADV locations. Figure 5.27 shows the sub-grid-based bottom shear stress (N/m2) simulated at the north and south pilings of Slip 1, along with the tide data. To generate this ﬁgure, we collected the propeller wash shear stress computed from the three ferries’ sub-grid points that passed the north and south ADV locations during the simulation. Overall, the shear stresses estimated at the south piling (-5.9 m depth) were generally greater than the shear stresses at the north piling (-9.8 m depth). The peak bottom shear stresses were predicted to reach 1.79 N/m2 at the south piling and 1.12 N/m2 at the north piling. The simulated bottom shear stresses were also higher for lower tidal periods than higher tidal periods because the ferries’ propeller was closer to the seabed. These model results are consistent with the observations from Kastner et al. (2019).

##### Figure 5.27 also includes horizontal dashed lines to indicate the critical shear stress (in N/m2) for each sediment size classiﬁcation, labeled on the left axis. The critical shear stress is the shear stress required to mobilize the sediments, and it is determined as a function of the sediment particle sizes.

##### DSI, LLC 5-39 EFDC+ Propeller Wash



<<<PAGE 90>>>

##### 5. Case Studies



According to Julien (2002), ﬁne sediments (clay + silt) can be mobilized even if the shear stress is less than 0.11 N/m2, while shear stress greater than 0.11 N/m2 can scour the sand-sized sediments. Shear stress greater than 1.26 N/m2 is required to erode gravel-sized sediments. Overall, the model results indicated that all ferry departures induce shear stress greater than 0.11 N/m2 for both the north and south pilings, which can cause severe scour in a sand bed. The model predicted shear stresses exceeding 1.26 N/m2 (up to 1.79 N/m2) at the south piling of Slip 1 due to several ferry departures during the low tide period. Such high shear stress is expected to cause signiﬁcant erosion even in a gravel bed. We should also note that the critical shear stress for each sediment size class (Julien, 2002) was developed by assuming a ﬂat sediment bed, so the sediments in this area would likely be even more easily eroded because of the bench face slope at Slip 1 (Kastner et al., 2019).

In conclusion, the ﬁndings from this analysis suggest that the propeller wash from ferry departures has a signiﬁcant impact on the seabed scour around the structural pilings of Slip 1 in the Kingston ferry terminal. Furthermore, through this case study, we demonstrated the functionality and capabilities of the EFDC+ propeller wash module as an effective tool for evaluating scour issues in harbor areas. Based on the ﬁndings from the case studies, it can be concluded that the EFDC+ propeller wash modeling approach will be beneﬁcial for researchers, engineers, and regulators in their efforts to properly evaluate propeller wash effects for contaminant remediation planning, scour mitigation, and structure design.

Figure 5.27: Simulated bottom shear stress at north and south pilings, tide data, and critical shear stress ranges for each sediment size classiﬁcation.

##### DSI, LLC 5-40 EFDC+ Propeller Wash



<<<PAGE 91>>>

# References

H. G. Blaauw and E. J. van de Kaa. Erosion of bottom and sloping banks caused by the screw race of manoeuvring ships. Technical Report 202, Delft Hydraulics Laboratory, Delft, Netherlands, 1978.

D.B. Chadwick, I. D. Rivera-Duarte, G. Rosen, P. F. Wang, R. C. Santore, A. C. Ryan, P. R. Paquin,

- S. D. Hafner, and W. Choi. Demonstration of an integrated compliance model for predicting copper fate and effects in DoD harbors. Technical Report ER-0523, Space and Naval Warfare Systems Center Paciﬁc, San Diego, CA, United States, 2008.


P. Y. Chou. On velocity correlations and the solutions of the equations of turbulent ﬂuctuation. Quarterly of Applied Mathematics, 3(1):38–54, 1945. Damen Shipyards. Design of Safety Standby Vessel 4711, 2021. URL https://products.damen. com/en/ranges/safety-standby-vessel/ssv-4711. [Online; accessed: 05.01.2021].

DSI. EFDC+ Theory Document, 2020. URL https://www.eemodelingsystem.com/wp-content/ uploads/EFDC Theory Document Ver 10.2 2020.05.21.pdf. [Online; accessed: 08.01.2021]. D. P. Finlayson. Combined bathymetry and topography of the Puget Lowland, Washington State. Technical report, School of Oceanography, University of Washington, WA, 2005. URL https: //www.ocean.washington.edu/data/pugetsound/psdem2005.html.

M. Fuehrer and K. R¨omisch. Effects of modern ship trafﬁc on inland and ocean waterways and their structures. Permanent International Association of Navigation Congresses (PIANC), 24: 79–94, 1977.

M. H. Garcia, D. M. Admiraal, and J. F. F. Rodriguez. Sediment entrainment functions for navigation-induced resuspension. Technical Report HES 61, Department of Civil and Environmental Engineering, University of Illinois at Urbana-Champaign, IL, 1999.

H. Gucinski. Sediment suspension and resuspension from small craft induced turbulence. Technical Report EPA-600/S3-82-084, United States Environmental Protection Agency, 1982. G. A. Hamill. Characteristics of the screw wash of a manouvering ship and the resulting bed scour. PhD thesis, Queen’s University of Belfast, 1987.

- G. A. Hamill and C. Kee. Predicting axial velocity proﬁles within a diffusing marine propeller jet. Ocean Engineering, 124:173–265, 2016.


- G. A. Hamill, C. Kee, and D. Ryan. 3D efﬂux velocity characteristics of marine propeller jets. Proceedings of the ICE - Maritime Engineering, 168(2):62–75, 2015.
- H. N. Hashmi, A. R. Ghumman, G. A. Hamill, and D. P. J. Stewart. Propeller-wash induced erosion and methods for its prediction. Technical Journal, 12:29–37, 2007.


J. H. Hong, Y. M. Chiew, S. C. Hsieh, N. S. Cheng, and P. H. Yeh. Propeller jet–induced suspendedsediment concentration. Journal of Hydraulic Engineering, ASCE, 142, 2016.

##### DSI, LLC 1 EFDC+ Propeller Wash



<<<PAGE 92>>>

##### References



J.H. Hong, Y.M. Chiew, and N.S. Cheng. Scour caused by a propeller jet. Journal of Hydraulic Engineering, ASCE, 139(9), 2013.

J. Jiang, W. Lam, Y. Cui, T. Zhang, C. Sun, J. Guo, Y. Ma, S. Wang, and G. Hamill. Ship twinpropeller jet model used to predict the initial velocity and velocity distribution within diffusing jet. KSCE Journal of Civil Engineering, 23, 2019.

C.A. Jones and W. Lick. SEDZLJ: A sediment transport model. Technical report, University of California, Santa Barbara, California, 2001. P. Y. Julien. River Mechanics. Cambridge University Press, 2002.

- S. E. Kastner, C. Stearns, A. R. Horner-Devine, and J. M. Thomson. Ferry vessel propeller wash effects on scour at the Kingston ferry terminal (WA, USA). Technical Report WA-RD 899.1, Washington State Department of Transportation, United States, 2019.


S. C. Kim, C. T. Friedrichs, J. P. Y. Maa, and L. D. Wright. Estimating bottom stress in tidal boundary layer from acoustic doppler velocimeter data. Journal of Hydraulic Engineering, ASCE, 126, 2000.

W. Lam, G. A. Hamill, Y. C. Song, D. J. Robinson, and S. Raghunathan. A review of the equations used to predict the velocity distribution within a ship’s propeller jet. Ocean Engineering, 38(1): 1–10, 2011.

MAN. Basic Principles of Ship Propulsion. MAN Energy Solutions, 2018.

- S. T. Maynord. Interim report for the upper Mississippi River - Illinois waterway system navigation study: Physical forces near commercial tows. Technical Report 19, US Army Corps of Engineers, 2000.
- T. C. Michelsen, C. D. Boatman, D. Norton, C. C. Ebbesmeyer, and M. D. Francisco. Transport of contaminants along the Seattle waterfront: effects of vessel trafﬁc and waterfront construction activities. Water Science and Technology, 37:9–15, 1998.


NYSDOT. Newtown Creek navigation analysis: Kosciuszko Bridge project. Technical report, New York State Department of Transportation, 2005. PIANC. Guidelines for Protecting Berthing Structures from Scour Caused by Ships. Permanent International Association of Navigation Congresses Secr´etariat G´en´eral, 2015. D. P. J. Stewart. Characteristics of a ship’s screw wash and the inﬂuence of quay wall proximity. PhD thesis, Queens University Belfast, 1992.

P. H. X. Thanh, M. D. Grace, and S. C. James. Sandia National Laboratories Environmental Fluid Dynamics Code: Sediment transport user manual. Technical Report SAND2008-5621, Sandia National Laboratories, 2008.

W.T. Toutant. Mathematical performance models for river tows. In Winter Meeting, Great Lakes and Great Rivers Section. Society of Naval Architects and Marine Engineers, Clarksville, IN, 1982.

TugboatInformation.com. Tugboat Information, 2021. URL https://www.tugboatinformation.com. [Online; accessed: 03.01.2021].

- Leo C Van Rijn. Sediment transport, Part I: Bed load transport. Journal of Hydraulic Engineering, ASCE, 110(10):1431–1456, 1984a.
- Leo C Van Rijn. Sediment transport, Part II: Suspended load transport. Journal of Hydraulic Engineering, ASCE, 110(11):1613–1641, 1984b.
- Leo C Van Rijn. Sediment transport, Part III: Bed forms and alluvial roughness. Journal of Hydraulic Engineering, ASCE, 110(12):1733–1754, 1984c.


- H. J. Verhey, T. Blokland, M. P. Bogaerts, D. Volger, and R. W. Weyde. Experiences in the Nether-


##### DSI, LLC 2 EFDC+ Propeller Wash



<<<PAGE 93>>>

##### References



lands with quay structures subjected to velocities created by bow thrusters and main propellers of mooring and unmooring ships. Permanent International Association of Navigation Congresses (PIANC), 58:69–88, 1987.

G. Voulgaris and G. H. Trowbridge. Evaluation of the acoustic doppler velocimeter (adv) for turbulence measurements. Journal of Atmospheric and Oceanic Technology, 15, 1998.

P. F. Wang, I. D. Rivera-Duarte, K. Richter, Q. Liao, K. Farley, H. C. Chen, J. Germano, K Markillie, and J. Gailani. Evaluation of resuspension from propeller wash in DoD harbors. Technical Report ER-201031, Department of Defense Environmental Security Technology Certiﬁcation Program, United States, 2016.

##### DSI, LLC 3 EFDC+ Propeller Wash



