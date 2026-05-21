

---PAGE-1---



###### LOUISIANA COASTAL PROTECTION AND RESTORATION FINAL TECHNICAL REPORT

# HYDRAULICS AND HYDROLOGY APPENDIX

### June 2009

U. S. Army Corps of Engineers New Orleans District Mississippi Valley Division



---PAGE-2---



## Hydraulics and Hydrology Appendix Volume I - Background and Methodology



---PAGE-3---



###### CONTENTS

###### Page

CONTENTS I

LIST OF FIGURES II

LIST OF TABLES III

LIST OF ANNEXES III

- 1 INTRODUCTION 1

- 1.1 Purpose 1
- 1.2 Planning area and planning units 1
- 1.3 Hydraulic evaluation 2
- 1.4 Outline of Volume I 4


- 2 SURGE AND WAVE MODELING 7

- 2.1 Description of the modeled hurricanes 8
- 2.2 Atmospheric-hydrodynamic modeling system 10
- 2.3 Modeling validation and datum considerations 15
- 2.4 Description of grids and/or conditions modeled 17
- 2.5 Storm selection 26
- 2.6 Point sets 30


- 3 FREQUENCY ANALYSIS WITH JPM-OS METHOD 32

- 3.1 JPM-OS method 33
- 3.2 Fit procedure for surge levels 35
- 3.3 Fit procedure for wave characteristics 39
- 3.4 Validity of fit procedure 42


- 4 DETERMINATION OF LEVEE HEIGHTS 44

- 4.1 Step-wise design approach 45
- 4.2 Design assumptions 47
- 4.3 Uncertainty analysis 49


- 5 OVERTOPPING RATES 51

- 5.1 Parametrical description of hydrographs 51
- 5.2 Overtopping volumes 55


- 6 INTERIOR DRAINAGE 59


- 6.1 Storage areas 59
- 6.2 Methodology 60
- 6.3 Rainfall 61
- 6.4 Overtopping 62


i



---PAGE-4---



- ii
- 6.5 Pumping 63
- 6.6 Flood volumes and stage frequencies 64


###### 7 REFERENCES 65 LIST OF FIGURES

- Figure 1.1 - LACPR planning units.............................................................................................................................1
- Figure 1.2 - Schematic overview of the step-wise approach in the hydraulic analysis in the framework of LACPR ...................................................................................................................................................2
- Figure 1.3 - Flow diagram of hydraulic analysis in LACPR framework (in blue).........................................................5


- Figure 2.1 - Flow diagram of hydraulic analysis in LACPR framework (Chapter 2)....................................................7
- Figure 2.2 - Storm tracks for eastern Louisiana..........................................................................................................9
- Figure 2.3 - Modelling system with the four modelling components and their interaction.........................................11
- Figure 2.4 - Example of the wind field of one storm at landfall from the entire suite of 152 storms..........................12
- Figure 2.5 - STWAVE grid coverage ........................................................................................................................13
- Figure 2.6 - ADCIRC grid coverage..........................................................................................................................14
- Figure 2.7 - Comparison between high water marks and ADCIRC results for Katrina .............................................16
- Figure 2.8 – Levee alignments in the East A and East B grids.................................................................................22
- Figure 2.9 – Levee alignments in the East C and East D grids ................................................................................23
- Figure 2.10 – Levee alignments in the West A and West B grids.............................................................................24
- Figure 2.11 – Alignments in the West C grid (upper panel) and Plaquemines 1 grid (lower panel)..........................25
- Figure 2.12 - Examples of storm tracks (storms 56 and 87).....................................................................................27
- Figure 2.13 - Point sets (east grid) ...........................................................................................................................30
- Figure 2.14 - Point sets (west grid)...........................................................................................................................31


- Figure 3.1 - Flow diagram of hydraulic analysis in LACPR framework (Chapter 3)..................................................32
- Figure 3.2 - Numerical results at Lake Pontchartrain (upper panel) and MRGO (lower panel) from ADCIRC and STWAVE (2007 base condition) .....................................................................................34
- Figure 3.3 - Correlation between maximum surge levels at Lake Pontchartrain for 2010 base condition

- and 2007 base condition ......................................................................................................................36

Figure 3.4 - Correlation between maximum surge levels at Lake Pontchartrain for 2010 base condition

- and 2007 base condition ......................................................................................................................37


- Figure 3.5 - Effect of maximum surge level at Lake Pontchartrain (2010 East A grid) with fit for all storms.............38
- Figure 3.6 - Effect of maximum surge level at Lake Pontchartrain (2010 East A grid) with fit for different storm tracks..........................................................................................................................................39
- Figure 3.7 - Wave characteristics at Lake Pontchartrain for 56 storms ....................................................................41
- Figure 3.8 - Wave characteristics at MRGO for 56 storms.......................................................................................41
- Figure 3.9 - Comparison between the 1% still water levels based on the full storm set of 152 storms and based on the 42 storms using the fit procedure....................................................................................43


- Figure 4.1 - Flow diagram of hydraulic analysis in LACPR framework (Chapter 4)..................................................44
- Figure 4.2 - Simplified levee cross section in LACPR evaluation .............................................................................47
- Figure 4.3 - Result for 100-year design height along MRGO levee (2010 base condition).......................................50


- Figure 5.1 - Flow diagram of hydraulic analysis in LACPR framework (Chapter 5)..................................................51
- Figure 5.2 - Example of hydrograph from ADCIRC results.......................................................................................52
- Figure 5.3 - Real hydrograph from ADCIRC (in red) and parameterized hydrograph (in red) ..................................54
- Figure 5.4 - Normalized surge from ADCIRC plotted against the normalized parameterized surge.........................54




---PAGE-5---



- Figure 5.5 - Width of the hydrograph plotted against the maximum surge level.......................................................55
- Figure 5.6 - Overtopping rates for different return periods (100-year, 400-year, 1000-year and 2000year) at a level with a 1% design elevation ..........................................................................................58


- Figure 6.1 - Flow diagram of hydraulic analysis in LACPR framework (Chapter 6)..................................................59
- Figure 6.2 - Principle water system ..........................................................................................................................60
- Figure 6.3 – Example internal planning subunit and stage storage relationship.......................................................61
- Figure 6.4 - Standardized rainfall hydrograph ..........................................................................................................62
- Figure 6.5 - Rainfall hydrograph of New Orleans East (100-year design standard) for a 100-year return period (left) and a 400-year return period (right)...................................................................................63
- Figure 6.6 - Water volumes flowing between adjacent subunits...............................................................................64


###### LIST OF TABLES

- Table 2.1 - Saffir-Simpson classification ....................................................................................................................8
- Table 2.2 - Description of grids/conditions and the number of storms used to model each......................................17
- Table 2.3 - Overview of measures in LACPR East grid models for Planning Units 1 and 2 .....................................21
- Table 2.4 - Overview of measures in LACPR West grid models for Planning Units 3a, 3b, and 4 ...........................21
- Table 2.5 - Selected storms for the East grids..........................................................................................................28
- Table 2.6 - Selected storms for West grids ..............................................................................................................29 Table 2.5 - Overview of point sets used ...................................................................................................................30 Table 4.1 – Step-wise approach...............................................................................................................................45 LIST OF ANNEXES


- ANNEX A Sea level rise
- ANNEX B The maximum possible intensity and its use for coastal hazard estimation


iii



---PAGE-6---



- 1 INTRODUCTION


- 1.1 Purpose

The Louisiana Coastal Protection and Restoration (LACPR) Technical Report has been developed by the United States Army Corps of Engineers (USACE) in response to Public Laws 109-103 and 109-148. Under these laws, Congress and the President directed the Secretary of the Army, acting through the Chief of Engineers, to:

- • Conduct a comprehensive hurricane protection analysis and design in close coordination with the State of Louisiana and its appropriate agencies;
- • Develop and present a full range of flood control, coastal restoration, and hurricane protection measures exclusive of normal policy considerations for South Louisiana;
- • Consider providing protection for a storm surge equivalent to a Category 5 hurricane; and
- • Submit preliminary and final technical reports.


The purpose of this appendix is to support the hydraulics and hydrology evaluation for LACPR, which is discussed in the main Technical Report.

- 1.2 Planning area and planning units


The LACPR planning area stretches across Louisiana’s coast from the Pearl River, on the Mississippi border, to the Sabine River, on the Texas border. The planning area is divided into five planning units (see Figure 1.1).

- Figure 1.1 - LACPR planning units




---PAGE-7---



###### 1.3 Hydraulic evaluation

- Volume I of this appendix describes the methodology for the hydraulic evaluation of the alternatives within the framework of the LACPR Technical Report. This hydraulic analysis has been visualized in Figure 1.2.

|Levee design<br><br>Interior stages<br><br>Overtopping rates<br><br>Rainfall<br><br>Surges and waves|
|---|


Figure 1.2 - Schematic overview of the step-wise approach in the hydraulic analysis in the framework of LACPR

In the framework of LACPR the hydraulic analysis plays a key role in the evaluation of the alternatives in the various planning units. Each levee alternative affects the surge and the waves during a storm in a different way. The differences in storm surge and wave characteristics result in varying overtopping volumes and stage frequency curves. The stage frequency curves are an important input for the economic analysis to estimate the damage in the planning subunits, and the levee heights need to be known for the cost estimates. This report describes the methodology of the hydraulic analysis that has been followed to determine the exterior and interior stages, and the levee heights. The results of this hydraulic analysis for the various planning units are described in

- Volume II of this appendix. The use of this data within the economic analysis and the cost estimates are described in separate appendices. The hydraulic analysis of each alternative in LACPR consisted of the following consecutive steps:


- 1. Numerical computations of surge levels and wave characteristics using ADCIRC, WAM and STWAVE;
- 2. Frequency analysis using the JPM-OS method and the determination of exterior stage frequency;
- 3. Determination of the levee heights and overtopping volumes;
- 4. Determination of the interior stages including rainfall;


To provide a range of alternatives for evaluation and to enable the economic evaluation it was decided to evaluate each levee alignment alternative for different risk reduction levels and event frequencies. A levee design was made for three different levels of risk reduction (100-year, 400year, 1000-design year). Given the level of risk reduction, the overtopping volumes were computed for four return periods of the outside surge level and wave characteristics (100-year, 400-year, 1000-year and 2000-year event). For all alternatives, the 10-year rainfall was added to the



---PAGE-8---



overtopping volume to establish the interior stage frequency curve and pumping was taken into account. The four steps in the hydraulic analysis are discussed in detail below.

- Step 1: Surge levels and wave characteristics

The numerical computations for the surge levels and the wave characteristics were carried out with the numerical models ADCIRC, for surge levels, and WAM/STWAVE, for the wave characteristics. These models are state-of-the art models and have already been applied extensively during the IPET and 100-year design for the hurricane risk reduction system around New Orleans. Two basic ADCIRC modeling grids were developed to cover the southern coast of Louisiana. Several wave grids were developed for STWAVE to compute the wave characteristics.

A base set of 56 hurricane conditions have been evaluated with the modeling suite ADCIRC/STWAVE for the 2010 base condition. The modeled storms are different in terms of the hurricane tracks, minimum pressure, and radius amongst other parameters. The 2010 base condition consists of the existing condition with a levee system with a 100-year risk reduction level including the barrier at MRGO. The different levee alignments for the various alternatives (e.g. barrier plan or West Bank alignment along GIWW) have been implemented in the model grids to evaluate the behavior of the surge levels and waves. In addition, computations have been carried out to evaluate the future effects of sea level rise and marsh improvement/degradation. For all of the alternatives, the number of storms that were evaluated was reduced because of time constraints.

- Step 2: Frequency analysis

Based on the results from ADCIRC and STWAVE in step 1, a frequency analysis has been carried out to determine the surge levels and wave characteristics for different return periods. The method adopted was the Joint Probability Method with Optimal Sampling (JPM-OS) that takes into account the joint probability of forward speed, size, minimum pressure, angle of approach and geographic distribution of the hurricanes. This method requires a set of 152 storms to establish the frequency curves for surge and waves. Since the various alternatives were only run for 56 or less storms, the results for the remaining storms were established using correlation techniques in order to carry out the frequency analysis with the JPM-OS method.

The frequency analysis has resulted in stage frequencies for the exterior areas, i.e. the areas that are not protected by the levees. Furthermore, this analysis has provided the surge levels and the wave characteristics for different return periods along the levee system as needed for the levee design and overtopping volumes in step 3.

- Step 3: Levee design and overtopping volumes


For the levee designs the step-wise procedure that was used for the 100-year design elevations has been followed in a slightly adapted way. In short, this procedure has been applied as follows in LACPR:



---PAGE-9---



- • Use the surge level and wave characteristics at the levees for a given level of risk reduction (e.g. 100-year) and assume a simplified levee design for this planning effort, i.e. a levee with a wave berm at the still water level and a constant slope near the crest of the levee of 1:4.
- • Determine the overtopping rate using empirical formulations. A Monte Carlo Simulation was adopted to compute the uncertainty in the overtopping rate given the uncertainties in the hydraulic boundary conditions and the empirical coefficients in the overtopping formulations.
- • Establish the levee height in such a way that the overtopping rate is less than 0.1 cft/s per ft with 90% confidence. The levee heights for the various alternatives have been used as an input for the interior drainage analysis and costs estimates.


The overtopping volumes were computed using the information on the surge level hydrographs from ADCIRC. Based on a statistical analysis, a correlation was established between the duration of the surge and the maximum surge level. This correlation has been applied to compute the overtopping rate during the storm assuming that the wave characteristics are constant around the peak of the storm.

- Step 4: Interior stage frequency


The final step was to determine the interior stage frequency for each planning subunit. Each subunit has been schematized as a box model for which a stage-storage curve has been established. This information has been extracted from existing rainfall-runoff models or from LIDAR data for these areas. The interior stage frequency has been based on the sum of the overtopping volume from step 3 together with the 10-year rainfall in the subunit. The effect of pumping has been taken into account if applicable. Where planning subunits join, flow of water has been allowed to occur above define thresholds.

###### 1.4 Outline of Volume I

The outline of this volume follows the structure of the flow chart in Figure 1.3, which visualizes in detail the various steps to facilitate the hydraulic evaluation of the various alternatives. To evaluate various alternatives numerical modeling with ADCIRC and STWAVE was carried out to simulate the water levels and wave heights (in yellow). The water levels and the waves are used in the hydraulic analysis to determine the levee heights, the exterior stage frequency curves and the interior stage frequency curves (in blue). Additionally, economic damage assessments, levee construction cost estimates as well as risk and reliability tasks can be performed with the resulting datasets (in green).



---PAGE-10---



chapter 2

|ADCIRC modelling|
|---|


|STWAVE modelling|
|---|


Water levels

Waves

chapter 5 chapter 3

|Analysis of storm hydrographs|
|---|


|Frequency analysis<br><br>JPM-OS method|
|---|


|Damage analysis exterior areas|
|---|


Exterior stage frequency curve

chapter 4

|Probabilistic determination of levee height using 0.1 cft/s per ft with 90% confidence|
|---|


Extreme waves and water leves near levees

Storm width parameters

|Generation of synthetic<br><br>hydrographs by Monte Carlo simulation|
|---|


|Determination of overtopping rates|
|---|


|Cost estimate levees/floodwalls|
|---|


Levee heights

Hydrographs

chapter 6

Overtopping rates

|Interior drainage analysis|
|---|


Stage storage curves sub basins

10-year rainfall event

|Damage analysis interior areas|
|---|


Interior stage frequency curve

###### Figure 1.3 - Flow diagram of hydraulic analysis in LACPR framework (in blue)



---PAGE-11---



Chapter 2 briefly describes the numerical modeling with ADCIRC and STWAVE. The background to the processes, the modeled alternatives and summaries of the model output are presented. The focus of Chapter 3 is to describe the frequency analysis undertaken to come up with the surge levels and wave characteristics for different return period events. Chapter 4 deals with the levee design procedure that has been applied within the LACPR framework and chapter 5 discusses the determination of the overtopping volumes. The development of the interior stage frequency curves is described in Chapter 6.

The work as presented in Chapter 3 through 6 of Volume I was undertaken from June to September 2007 as a joint effort between the United States Army Corps of Engineers, New Orleans District and Haskoning Inc1. The methods described within Volume I are limited to the hydraulic aspects only and no economic evaluation is provided. The main deliverables of this task were the stage frequency curves and the design heights of the levees. The stage frequency curves will be used for the economic evaluations and the damage studies. Note that the methodologies described within this appendix are developed to enable the relative comparison of various design alternatives. More detailed study will be needed for doing actual design.

- Annex A of Volume I describes the development of relative sea level rise projections for LACPR.
- Annex B of Volume I describes the background and characteristics of the theoretical maximum possible intensity hurricane and some of its implications for the Louisiana coastal area.


Volume II of this appendix presents the results of the hydraulic evaluation of the LACPR alternatives.

- 1 Chapter 2 is added to this report to present the complete picture of the hydraulic analysis in the framework of LACPR. The work as presented in Chapter 2 summarizes the result of a combined effort of FEMA and USACE, universities and various consultancy firms.




---PAGE-12---



###### 2 SURGE AND WAVE MODELING2

The surge level and wave computations with an atmospheric-hydrodynamic modeling system form the basis of the hydraulic analysis within the framework of LACPR (Figure 2.1). The main components and the validation of this modeling process are briefly summarized in Section 2.1 and Section 2.2. For more detailed information, the reader is referred to various earlier studies in which this modeling suite was applied (IPET, 2007; FEMA, 2007). The LACPR effort evaluates several alternative storm surge risk reduction systems using many levee alignments. For each of the main variations, a model grid has been created to model the system and provide results from which levee heights can be determined. These model grids are discussed in Section 2.3. Section 2.4 describes the selection of hurricanes that have been evaluated for the alternatives because it was impossible to run all hurricanes for all alternatives. Finally, the output locations and results of the modeling system at these points that have been used for LACPR are summarized in Section 2.5. These results are input into the frequency analysis (Chapter 3) and the determination of the overtopping volumes (Chapter 5).

chapter 2

|ADCIRC modelling|
|---|


|STWAVE modelling|
|---|


Water levels

Waves

chapter 5 chapter 3

|Frequency analysis|
|---|


|Damage analysis exterior areas|
|---|


chapter 4

|Overtopping analysis|
|---|


|Levee design|
|---|


|Cost estimate levees/floodwalls|
|---|


chapter 6

|Interior stages|
|---|


|Damage analysis interior areas|
|---|


###### Figure 2.1 - Flow diagram of hydraulic analysis in LACPR framework (Chapter 2)

- 2 The work as presented in Chapter 2 summarizes the result of a combined effort of FEMA and USACE, universities and various consultancy firms. Section 2.1 – 2.5 of this Chapter were written by the ADCIRC/STWAVE team (Joannes Westerink, Mary Cialone, Allison Sleith, John Atkinson, Jay Ratcliff).




---PAGE-13---



###### 2.1 Description of the modeled hurricanes

The LACPR authorization states that “……the Secretary shall consider providing protection for a storm surge equivalent to a Category 5 hurricane…”. Previously, it was believed that a single parameter, the Saffir-Simpson intensity scale (see Table 2.1), dictated the potential surge levels that a storm could generate. Based on this concept, previous design-storm concepts used terms such as a “Category 5 Storm” to denote a particular class of storm.

- Table 2.1 - Saffir-Simpson classification


|Saffir-Simpson Category|Wind speeds (m/s)|Pressure (mbar)|Historical examples at the Atlantic Ocean|
|---|---|---|---|
|1|33-42|980|Jerry (1989), Danny<br><br>(1997)|
|2|43-49|965-979|Diana (1990), Erin (1995)|
|3|50-58|945-964|Roxanne (1995), Isidore<br><br>(2002)|
|4|59-69|920-944|Galveston (1900), Betsy<br><br>(1965), Iris (2001), Charley (2004)|
|5|> 70 m/s|< 920|Camille (1969), Katrina<br><br>(2005), Rita (2005)|


Recent analyses have clearly demonstrated that coastal surge levels are significantly affected by storm size as well as storm intensity (Saffir-Simpson category). It is now recognized that a small “Category 5 Storm” will generate a smaller surge than a large “Category 3 Storm” in coastal areas where the offshore slope is very small, such as along much of the Louisiana-Mississippi coastline. Thus, it is important to consider a range of storm sizes in conjunction with a fixed “Category 5” intensity, in order to represent the actual range of conditions that a “Category 5 Storm” can generate. This insight changes the manner in which a storm must be specified for planning and design purposes.

A USACE and FEMA consensus procedure was developed in order to define the relevant storms that affect Southern Louisiana (FEMA, 2007). It was agreed that the Joint Probability Method (JPM) allows for the richest storm set but that many of the storms are either irrelevant or have a very low probability of occurrence due to dependencies in the parameter space. A set of 152 storms were developed for eastern Louisiana by combining the “probable” combinations of central pressure, radius to maximum winds, forward speed, angle of track relative to coastline, and track. Tracks were defined by 5 primary tracks and 4 secondary tracks (see Figure 2.2). Central pressure and radius to maximum relationships were also developed that modify the storms as the coastline is approached. A storm matrix was developed based on these parameters and proposed to FEMA and USACE for concurrence. A concurrent set of 152 storms was developed for western Louisiana.



---PAGE-14---



- Figure 2.2 - Storm tracks for eastern Louisiana


The storm set of 152 storms contains 50 “Category 3 storms”, 52 “Category 4” storms and 50 “Category 5” storms. As discussed above, these subsets of storms are classes of storms that can result in different hydrodynamic behavior depending on the storm size and other factors. The following ranges of storm sizes are considered in the set with 152 storms:

- • Category 3: 11 – 35 nautical miles
- • Category 4: 8 – 25 nautical miles
- • Category 5: 6 – 21 nautical miles


The probability of occurrence of the 152 storms covers a frequency range between approximately 1 in 50 years and 1 in 3,500 years.

In the framework of LACPR, hydraulic events with different return periods have been chosen as a basis for evaluation (and not the Saffir-Simpson Scale). These events are: 100-year event, 400year event, 1,000-year event and 2,000-year event. The 100-year event has been chosen because that return period serves as a basis for the current design effort for the Greater New Orleans Hurricane Storm Damage and Risk Reduction System. The 400-year event is a proxy for Katrina, because this is the estimated return period for this hurricane (see Resio et al., 2007). The 1,000year and 2,000-year event are chosen based on practical considerations. The maximum frequency of the storm set is approximately 3,500 year. The 1,000 year and 2,000 year events were considered appropriate choices to have enough coverage in the storm set. Note that all these events cover different “Cat 5 hurricanes” with increasing storm size. Apart from this, an additional



---PAGE-15---



analysis was done regarding the so-called maximum possible intensity hurricane. Annex B describes the background and characteristics of the theoretical maximum possible intensity hurricane and some of its implications for the Louisiana coastal area.

The storm set of 152 storms has been used as a starting point to analyze the surge levels and the waves at the Louisiana coastline. The setup and interaction between the various atmospheric and hydrodynamic models to compute the actual surge levels and waves is the topic of the next section.

###### 2.2 Atmospheric-hydrodynamic modeling system

In purse of a common technical framework of al Federal Agencies involved in assessing hurricane related threats to coastal communities, an atmospheric-hydrodynamic modeling system has been implemented. The goal of this hydrodynamic model development has been to implement a simulation capability that represents the basic physics of the system as it is observed and that does not require ad hoc tuning. Therefore the hydrodynamic models should define the physical system as it exists and should consider wind, atmospheric pressure, short period wind waves, tides, and riverine flows in a comprehensive way. In order to achieve the required accuracy, a sequence of state of the art, well verified and validated wind, short period wind wave and coastal circulation models were coupled together as an atmospheric-hydrodynamic modeling system and applied to Southern Louisiana and Mississippi.

The modeling suite consists of four major components:

- • Wind and pressure model (PBL)
- • Surge model (ADCIRC)
- • Deep water wave model (WAM)
- • Shallow water wave model (STWAVE)


The coherence and interaction between these models is visualized in Figure 2.3.

The first component in the modeling sequence is the wind and atmospheric pressure field model. For hindcasting historical storms, kinematic H*WIND and IOKA models that use data assimilation methods in order to define wind fields and pressure decay relationships in conjunction with observational data were employed. For synthetic hurricanes in the statistical storm set, a dynamic wind model, the Planetary Boundary Layer (PBL) model was applied. A comparative analysis was done between the PBL and Hurricane Boundary Layer (HBL). Models were run to determine the best fit for this analysis and the PBL was selected. An example of one storm track and its wind speed distribution is given in Figure 2.4.

It should be recognized that the wind forcing is not based on the ADCIRC grid geometry. Thus the surge responses that maintain similar topography in different grids (see section 2.4) will then be almost exactly the same from the same storm. The final maximum peak surge levels are the direct results of the wind forcing which is exactly the same in the base as well as the other geometry simulations. An introduction of levee barriers can and does produce non-similar results near and far from the geometry change. These changes are clearly seen in the analysis point locations,



---PAGE-16---



###### especially where surges are greatly reduced with a barrier in place. The surge results at point locations within and outside of alternative levee configurations are analyzed and used to quantify the economic benefits and also compute levee heights.

||Planet Boundary Layer model for wind and pressure|
|---|
<br><br>|ADCIRC model for surge levels|
|---|
<br><br>|WAM model for deep water waves|
|---|
<br><br>|STWAVE model for shallow water waves|
|---|
<br><br>wind velocity, pressure fields<br><br>wind velocity, pressure fields<br><br>wave forces<br><br>water levels<br><br>river discharge, tide<br><br>waves at boundaries|
|---|


- Figure 2.3 - Modelling system with the four modelling components and their interaction




---PAGE-17---



- Figure 2.4 - Example of the wind field of one storm at landfall from the entire suite of 152 storms Note: This specific storm has a minimum pressure of 900 mbar and a maximum radius of 17 nautical miles.


Once the winds are generated, the basin scale WAve prediction Model (WAM) is run in order to generate deep water waves in a Gulf of Mexico domain. These results are then applied as boundary conditions in a finer scale regional WAM model that covers the continental shelf in Southern Louisiana and Mississippi. The regional scale WAM results were then applied as boundary conditions in four to five regional finer scale STWAVE models that provide comprehensive coverage in Southern Louisiana (see Figure 2.5). The STWAVE computations also included water levels obtained from ADCIRC (see Figure 2.6). The last component to be applied was the ADCIRC hydrodynamic model, which is forced with wind and atmospheric pressure, wind wave radiation stresses from STWAVE, riverine flows and tides for hindcast cases.

There is significant interaction between the various component models. The wind models produce marine winds that are reduced for overland areas depending on the upwind roughness length scales and the existence of canopies. However, once an area is inundated, the physical



---PAGE-18---



roughness elements are subject to immersion, and the nominal roughness length scales are subsequently reduced. Upon full immersion of the physical roughness elements, marine winds are again applied.

- Figure 2.5 - STWAVE grid coverage


In addition to quantifying the wind waves themselves, wind-waves influence surge height with wind-wave radiation stress forcing, modify bottom friction as well as influence the sea surface roughness. Wind-waves reach shore prior to the peak surge driven by the strongest hurricane winds, so combined wind and wind-wave surge builds up earlier than solely wind driven surge. Furthermore, draw-down caused by winds coming from shore tends to be reduced by waves that are still coming into shore. In this modeling system, the interaction between the wind-waves and the surge is considered by applying wave radiation stress forcing. The effect on bottom friction or the influence of waves on surface roughness as they affect air-sea interaction, are not included since these effects are currently not well understood for hurricane conditions.

ADCIRC computations are forced with wave radiation stresses from the four to five localized STWAVE grid domains for western Louisiana, west of the Mississippi river, east of the Mississippi river, south of the Mississippi-Alabama coasts and within Lake Pontchartrain. The STWAVE computations themselves were made with boundary forcing information from the regional WAM model (which is forced with the Gulf wide WAM solution) as well as preliminary water level and current information from ADCIRC. The preliminary ADCIRC simulations included all forcing functions with the exception of the wave radiation stresses.



---PAGE-19---



- Figure 2.6 - ADCIRC grid coverage


In addition to the effects of waves, there can be significant effects on surge due to coastal tides and riverine currents. Because the tide range in Southern Louisiana is limited (about a 1.5 ft range), the nonlinear impact on the high water is limited. Therefore when looking at the statistical high water studies, tides can be linearly added in most areas without incurring significant error. However previous studies indicate that the shape of the tides themselves is significantly affected by the surge and therefore for purposes of model validation it is of significant interest to include them.

Finally it is noted that significant currents flow through the Mississippi and Atchafalaya Rivers and that these river currents strongly interact with tides and surge. For example, tides are substantially attenuated as they propagate up the Mississippi River for high flow/stages compared to low flow/stage. The level of interaction for storm surge wave propagating up the river is unknown but it may be important given the depth of the river and the magnitude of the currents. ADCIRC



---PAGE-20---



computations were therefore made simultaneously including wind, atmospheric pressure, riverine flows, wave radiation stresses and for hindcast studies tides so that all significant coastal and riverine currents could fully interact nonlinearly in the computation.

###### 2.3 Modeling validation and datum considerations

The effects of subsidence have created issues with the vertical datum that has plagued the engineering and surveying community in Southern Louisiana. Fortunately, in the last few years the National Geodetic Survey has developed a new method for updating vertical datum epochs to take into account subsidence and movement in control monuments. This new method has led to the creation of Vertical Time Dependent Positioning which requires the datum and its epoch to be listed together. At the time the LACPR effort began, the vertical datum in use was the NAVD 88 (2004.65) where 2004.65 is the datum epoch. This epoch has been superseded by a 2006.81 adjustment but to maintain continuity, the 2004.65 epoch will continue to be used for this effort. There are still many problems associated with trying to convert historical data such as gauge data, high water mark data, etc. into the new datum and epoch since the historical data is tied to older datum spanning numerous leveling epochs. The NAVD 88 (2004.65) datum will be used as the reference datum for all elevations in this report unless otherwise noted.

Design elevations referenced in this report were created using the same modeling, methodology, and data used to design the Greater New Orleans Hurricane and Storm Damage Risk Reduction System (HSDRRS) work and to perform the FEMA flood insurance studies for South Louisiana (reference USACE/FEMA Louisiana and Texas Joint Coastal Storm Surge Study). Elevations used in developing the models incorporated the latest information on the relationship between water level reference surface (local mean sea level) and geodetic datum. Details can be found in draft reports done for the Joint Surge effort. All elevations are provided in NAVD88 (2004.65) which is the datum currently being used for all HSDRRS work.

Future detailed design and construction will be done using the most current HSDRRS design procedures and standards. During the design phase, gaging requirements will be established and gage(s) will be installed as required. The gage(s) will be used for determining the tidal datum local mean sea level prior to construction. Additional temporary gages may be required depending on vertical accuracy requirements. The gage(s) can also be used to monitor future hydrologic conditions in the area. The datum of the gage(s) has been established to comply with criteria contained in the Vertical Control Requirements for Engineering, Design, Construction, and Operation of Flood Control, Shore Protection, Hurricane Protection, and Navigation Projects (Engineering Division Policy Memo #2).

The relationship between NAVD88 2004.65 and local mean sea level for the gage(s) will be reevaluated and reviewed by NOAA every 5 years (or more frequently if warranted based upon rate of subsidence). Vertical Datum Reports for each current HSDRRS polder are currently being prepared and will contain specific information on the gage network and the relationship between local mean sea level and NAVD 88 2004.65 for the project area. As new areas with HSDRRS projects are added reports for those areas will be produced.



---PAGE-21---



The atmospheric-hydrodynamic modeling system was extensively validated. A brief summary of the validation is given here. For complete documentation on system validation, the reader is referred to earlier studies in which the modeling suite was applied (IPET 2006, FEMA 2007). The surge model was validated for Hurricanes Katrina and Rita. These storms were selected due to the unprecedented quality of the system definition, storm data, resulting high water marks (HWM) and the vertical leveling information. In addition the extent of inland inundation was unprecedented allowing for a unique opportunity to validate the effectiveness of modeling the effects of topography, overland resistance, and decreases in overland wind speeds. The offshore wave model was validated with data from Hurricanes Rita, Ivan, Camille, Katrina, and Andrew and the wind model was validated with data from these storms plus Hurricane Betsy. The nearshore wave model was compared to available data in Lake Pontchartrain acquired during Hurricane Katrina.

For the surge model, maximum surge levels were compared to between 80 and 204 open water and inland HWM’s. Estimated model errors are based on these comparisons and the estimated accuracy of the HWM’s themselves. As an example, Figure 2.7 presents a comparison between the HWM’s and the ADCIRC results for Katrina. The resulting modeling system error standard deviations, which include inaccuracies in the kinematic wind models, air-sea momentum transfer, wave radiation forcing, system definition and the hydrodynamic model itself, are estimated to be

- 1.47 ft (IPET HWM for Katrina), 1.36 ft (FEMA HWM for Katrina), and 1.21 ft (FEMA HWM for Rita). This indicates that about 68% of the predictions can be expected to be within 1.3 ft and 95% of the predictions can be expected to be within 2.6 ft of accuracy.


HWM Error Analysis, Louisiana, Cf=0.003

25

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | |y = 0.9413x R2 = 0.815|
| | | | | | |
| | | | | | |
| | | | | | |


20

ADCIRC maximum surge,NAVD

15

10

5

0

0 5 10 15 20 25 High water marks, NAVD88 (ft)

###### Figure 2.7 - Comparison between high water marks and ADCIRC results for Katrina



---PAGE-22---



Winds were verified to point source measurements. The WAM model was validated to data from NOAA NDBC buoys for Hurricanes Rita, Katrina, Ivan, and Andrew and data from the Ocean Data Gathering Project for Hurricane Camille. The waves were validated against peak wave conditions and time variations during a storms passage. Few data are available to validate the nearshore wave model for hurricanes in Louisiana. However, two small wave buoys were deployed in Lake Pontchartrain during Katrina and results compared favorably to these data.

After completion of the surge and wave modeling, an independent analysis examined results from several nearshore wave models and a variety of conditions with a focus on wave energy dissipation effects. Careful review of simulated wave heights at some locations inshore of coastal marsh areas indicates that the with-friction STWAVE results may underestimate the wave height. In the interest of conservatism and in the absence of field-verified values for friction coefficients due to bottom and vegetation interaction, the design process applied STWAVE simulations without frictional dissipation. Uncertainty in future location and density of coastal marshes, in part due to local subsidence and lack of appropriated funding for marsh restoration, provides additional rationale for excluding the effects of friction in the nearshore wave simulations. Future planned efforts to obtain the necessary field data along with more accurate estimates of future wetland conditions should provide improved quantitative estimates of friction coefficients suitable for design purposes.

###### 2.4 Description of grids and/or conditions modeled

Various hydraulic conditions were modeled either for sensitivity analyses or to apply the results to the LACPR alternatives. The evaluated ADCIRC grids and/or conditions and the number of modeled storms are summarized in Table 2.2. These grids/conditions are discussed in further detail in the paragraphs following the table.

- Table 2.2 - Description of grids/conditions and the number of storms used to model each


|Grid/conditions|Short description|No. of storms|
|---|---|---|
|2007 Base Conditions (East and West grids)|Update to the 2005 hindcast grid. Represents the Greater New Orleans Hurricane and Storm Damage Risk Reduction System that existed in the summer of 2007.|152 (East) 152 (West)|
|2010 Base Conditions (East and West grids)|LACPR base condition for comparison to alternatives. The East grid models the Greater New Orleans levee system in 2011 with barrier at MRGO/IHNC and 100-year levee heights around the entire system. The 2010 West grid is the same as the 2007 West grid (no existing levees).|56 (East) 152 (West)|
|East A grid|Full closure of Lake Pontchartrain along US90; full closure of IHNC/GIWW along west shore of Lake Borgne; full closure West Bank from between Belle Chasse to Larose along GIWW.|48|
|East B grid|Weir closure of Lake Pontchartrain along US90 with structures in Chef and Rigolets tidal passes; full closure of IHNC/GIWW along west shore of Lake Borgne; weir closure West Bank from Belle Chasse to Larose along GIWW.|42 / 152|
|East C grid|Weir closure of Lake Pontchartrain along US90 without structures in Chef and Rigolets tidal passes; full closure of IHNC/GIWW along west shore of Lake Borgne; weir closure West Bank from Belle Chasse to Larose along GIWW.|48|
|East D grid|Isolating Lakes Pontchartrain and Borgne from each other by building a levee across Lake Borgne from Verret to Slidell; full closure West Bank from Belle Chasse to Larose along GIWW.|40|




---PAGE-23---



|West A grid|Non-overtopping levee alignment from Larose to Golden Meadow and along GIWW.|28|
|---|---|---|
|West B grid|100-year level alignment from Larose to Golden Meadow; a non-overtopping levee along the ridge and a ring levee alignment in the western part.|28|
|West C grid|Non-overtopping levee alignment from Larose to Golden Meadow and along the ridge, and an overtopping levee along GIWW with a ring levee around Lake Charles.|28|
|Plaquemines Parish|Option 1: Two spillways in the levee system along Plaquemines<br>Option 2: Full removal of levee system along Plaquemines to river embankment level (for sensitivity analysis only)<br><br><br>|17 17|
|Landscape Conditions|1) Degraded marshes 50 years from now without increased action<br>2) Restored marshes 50 years from now based on a hypothetical alternative (for sensitivity analysis only)<br>|174<br><br>46|
|Sea level Rise Sensitivity Analysis|1) +1 ft sea level rise<br>2) +2 ft sea level rise<br>3) +3ft sea level rise<br>|9 9 9|
|Barrier Islands Sensitivity Analysis|1) No barrier island<br>2) Restored island<br>3) Post-Katrina with forest<br>4) Restored island with forest<br>|15 15 15 15|




---PAGE-24---



2007 Base Conditions

In order to update the 2005 hindcast grid to the system that existed in the summer of 2007, levee definitions were updated to reflect the system upgrades that were implemented as part of the USACE Task Force Guardian and by the USACE Hurricane Protection Office and New Orleans District. This system was then run with the 152 storms for eastern Louisiana and 152 storms for western Louisiana in order to define 100- and 500-year water levels and corresponding wave conditions. This information served as a base condition for various sensitivity analyses that were performed prior to the development of the 2010 base grids. This grid was then replaced with the 2010 East and West base grids for evaluation of the LACPR alternatives as described below.

2010 Base Conditions

In addition to evaluating the 2007 system, the proposed system improvements anticipated for 2010 (now 2011) were investigated. This included raising levees across the system as well as a closure of the combined MRGO/GIWW east of Paris Road. Note that the area west of Larose to Golden Meadow is the same in both the 2007 and 2010 base case.

LACPR East Levee System Configurations in Planning Units 1 and 2

In order to understand the performance and implications of a variety of levee system improvements as developed by the USACE and the State of Louisiana’s Coastal Protection and Restoration Authority, four east levee configurations were evaluated for Planning Unit 1 and 2. The modeled levee configurations are the so-called East A, B, C and D grids. The east configurations included a variety of alignments and elements that are summarized in Table 2.3. Figure 2.8 and

- Figure 2.9 present the levee alignments for East A, B, C, D.


LACPR West Levee System Configurations in Planning Units 3a, 3b, and 4

Similar to the LACPR East alignments, three different west alignments were examined with various configurations including a solid line of levees that runs north of the bays and lakes of western Louisiana as well as more localized ring levees that locally protect the population centers. The west configurations considered included a variety of alignments and elements that are summarized in Table 2.4. Figure 2.10 and Figure 2.11 present the levee alignments for West A, B and C.

Plaquemines Parish River and Back Levees (Plaquemines-1 and Plaquemines-2)

In order to understand the influence of the Mississippi River levees and adjacent back levees in lower Plaquemines Parish, spillways were incorporated into these levees (option 1) and the levees were entirely eliminated (option 2). This study component was designed to understand how surge builds up along these levees from Breton Sound and propagates towards New Orleans and Baton Rouge in the Mississippi River. In addition, the effectiveness of building localized ring levees to provide a higher level of risk reduction in Lower Plaquemines Parish can be ascertained.

Landscape Conditions

The landscape conditions included a predicted wetland definition 50 years into the future for two cases: 1. no action and 2. a restored/improved marsh condition (for sensitivity analysis only).



---PAGE-25---



The no action condition was developed as part of the Coastal Louisiana Ecosystem Assessment and Restoration (CLEAR) Program. The forecasting model developed by CLEAR predicts physical processes, geomorphic features, water quality, and ecological succession. Geomorphic/bathymetric changes are based on the likelihood of discretized regions changing from open water to marsh or marsh to open water. The future condition of coastal Louisiana predicted by CLEAR, referred to as the degraded condition, in fact does predict degradation in southern Louisiana, but also predicts growth in the Atchafalaya basin and Plaquemines Parish. The CLEAR future condition bathymetry was applied to the model grids and mesh and a series of storm simulations was made.

The restored condition was developed by Engineer Research and Development Center’s Coastal and Hydraulics Laboratory (ERDC-CHL) as a sensitivity analysis. The District provided ERDC-CHL with marsh creation locations and type, freshwater diversion locations, and the volume of sediment diverted for a hypothetic alternative. ERDC-CHL implemented these restoration features into a marsh creation program and modifications were made to the bathymetry, Manning’s n values, and directional roughness lengths. These changes were applied to the model grids, mesh, and frictional files and a series of storm simulations was made.

Sea Level Rise Effects (Sensitivity Analysis)

Annex A describes an analysis of the relative sea level rise (includes subsidence) in detail for the Chenier Plain, the Delta Plain and the Pontchartrain Basin. The relative sea level rise is estimated at 1 – 3 ft based on two future projections. Based on this analysis, it was decided to evaluate the effect of sea level rise by applying a 1, 2, and 3-ft change in the vertical datum.

Influence of Barrier Islands (Sensitivity Analysis)

A sensitivity analysis was performed to assess the impact of bathymetric and frictional resistance changes for the barrier islands on ADCIRC-simulated peak surge elevations and STWAVEsimulated waves. The sensitivity storm suite consisted of fifteen storms of varying intensities and five barrier island configurations. The barrier island configurations modeled were:

- 1) no barrier islands with open water Manning's n value = 0.02;
- 2) a restored barrier island configuration of 12 ft (NAVD88 2004.65) for Cat Island, Ship Island, Horn Island, Petit Bois Island, and Dauphin Island and 6 ft (NAVD88 2004.65) for the Chandeleur Islands;
- 3) the existing Post-Katrina degraded condition with a forest Manning's n = 0.15;
- 4) a restored barrier island configuration with a forest Manning's n = 0.15.




---PAGE-26---



###### Table 2.3 - Overview of measures in LACPR East grid models for Planning Units 1 and 2

|Unit<br><br>Model grid|Planning Unit 1 (Lake Pontchartrain Basin)|Planning Unit 2 (Barataria Basin)|
|---|---|---|
|Base condition|Current levee system to 100-year level of risk reduction/authorized grade (whichever is greater) in combination with barrier at MRGO|Current levee system to 100-year level of risk reduction/authorized grade (whichever is greater)|
|East A|Modeling a non-overtopping levee adjacent to or on US 90 to close Lake Pontchartrain<br><br>Modeling a non-overtopping levee along the west shore of Lake Borgne|Modeling non-overtopping levees along the GIWW as well a closures further north<br><br>Modeling a non-overtopping levee following a southern alignment from Larose to Morgan City|
|East B|Modeling a weir at 12.5ft adjacent to or on US 90 and closure gates in the Rigolets and Chef Menteur Passes<br><br>Modeling a non-overtopping levee along the west shore of Lake Borgne|Modeling an overtopping levee at 12.5ft along the GIWW as well a closures further north<br><br>Modeling an overtopping levee at 100-year level following a southern alignment from Larose to Morgan City and a non-overtopping back levee along GIWW|
|East C|Modeling a non-overtopping levee adjacent to or on US 90 and openings in the Rigolets and Chef Menteur Passes<br><br>Modeling a non-overtopping levee along the west shore of Lake Borgne|Modeling a non-overtopping levee following the US90 alignment with a central overtopping weir<br><br>Modeling an overtopping levee at 100-year level following a southern alignment from Larose to Morgan City and a non-overtopping back levee along GIWW|
|East D|Modeling a non-overtopping levee across Lake Borgne from Verret to Slidell|Modeling non-overtopping levees along the GIWW as well a closures further north<br><br>Modeling a non-overtopping levee following a southern alignment from Larose to Morgan City|


###### Table 2.4 - Overview of measures in LACPR West grid models for Planning Units 3a, 3b, and 4

|Unit<br><br>Model grid|Planning Unit 3a|Planning Unit 3b|Planning Unit 4|
|---|---|---|---|
|Base condition|2007 situation|2007 situation|2007 situation|
|West A|Non-overtopping levee (10 m) along Larose to Golden Meadow alignment|Non-overtopping levee (10 m) along GIWW|Non-overtopping levee (10 m) along GIWW|
|West B|Levee at 100-year elevation along Larose to Golden Meadow alignment with non-overtopping back levee along GIWW|Non-overtopping levee along ridge north of GIWW|Non-overtopping (10 m) ring levee alignment Lake Charles, Vinton, Kaplan, and Gueydan|
|West C|Non-overtopping levee (10 m) along Larose to Golden Meadow alignment (similar to West A)|Non-overtopping levee along ridge north of GIWW (similar to West B)|Non-overtopping (10 m) ring levee alignment Lake Charles in combination with overtopping levee along GIWW alignment|




---PAGE-27---



###### Figure 2.8 – Levee alignments in the East A and East B grids



---PAGE-28---



###### Figure 2.9 – Levee alignments in the East C and East D grids



---PAGE-29---



###### Figure 2.10 – Levee alignments in the West A and West B grids



---PAGE-30---



###### Figure 2.11 – Alignments in the West C grid (upper panel) and Plaquemines 1 grid (lower panel)



---PAGE-31---



###### 2.5 Storm selection

Given time constraints and potentially significant computation requirements, not all 152 storms could be simulated for the numerous hydraulic conditions. Thus, only a subset of the 152 storms was simulated for each condition. The selected subset was created by selecting storms whose tracks and characteristics spanned the range of parameter space defined in the JPM-OS methodology. Additionally, the subset of storms was based on the degree and location of the changed geometry for each condition.

For example, 56 storms were selected for the 2010 baseline conditions based storm characteristics as well as geographic areas they affected and the 2010 geometry that was different than the 2007 geometry.

- Table 2.5 lists the storms simulated for the East grids. The storms are ordered in groups as defined in the JPM-OS White Paper (see Resio et al, 2007). These storms characteristics cover most of the important range of parameter space and thus provide a confident response surface generated from the JPM-OS code. As an example, two storm tracks of this set are shown in


- Figure 2.12. Similarly, the storms for the West grids are listed in Table 2.6.




---PAGE-32---



###### Figure 2.12 - Examples of storm tracks (storms 56 and 87)



---PAGE-33---



###### Table 2.5 - Selected storms for the East grids

| |
|---|




---PAGE-34---



###### Table 2.6 - Selected storms for West grids

| |
|---|




---PAGE-35---



###### 2.6 Point sets

A number of different model output point sets have been developed to present the results from the ADCIRC and STWAVE modeling. Table 2.7 lists the three different point sets that have been used within the LACPR technical evaluation.

Table 2.5 - Overview of point sets used

|Point set|Purpose|
|---|---|
|L 274|To select data for levee height design and overtopping rates for the east grid|
|W 177|To select data for levee height design and overtopping rates for the west grid|
|Q 835|To evaluate potential impacts of alternatives on the Mississippi coastline|


These point sets are visualized in Figure 2.13 (east grid) and Figure 2.14 (west grid) below.

- Figure 2.13 - Point sets (east grid)




---PAGE-36---



###### Figure 2.14 - Point sets (west grid)



---PAGE-37---



###### 3 FREQUENCY ANALYSIS WITH JPM-OS METHOD

This chapter describes the development of the frequency statistics for the surge level and wave characteristics. Inputs for this analysis are the results from the ADCIRC and STWAVE computations (Figure 3.1). The key element in this frequency analysis is the Joint Probability Method with Optimal Sampling (JPM-OS method). The background of this method is briefly summarized in Section 3.1. The JPM-OS method requires a full set of 152 storms to compute the frequency statistics for surge and wave characteristics. However, for all LACPR levee alignments less storms were simulated due to time constraints. To use the method for these levee alignments a fitting procedure was developed for surge levels (Section 3.2) and wave characteristics (Section

- 3.3) so as to create values for all 152 storms. To check the validity of this procedure, a check has been carried out for one specific alternative, see Section 3.4. The frequency statistics are used as input into the determination of the levee heights (Chapter 4) and the overtopping volumes (Chapter


- 5), and they are also used to provide stage frequency results for areas outside of a levee system.


chapter 2

|ADCIRC modelling|
|---|


|STWAVE modelling|
|---|


Water levels

Waves

||Frequency analysis|
|---|
<br><br>chapter 3|
|---|


chapter 5

|Damage analysis exterior areas|
|---|


chapter 4

|Overtopping analysis|
|---|


|Levee design|
|---|


|Cost estimate levees/floodwalls|
|---|


chapter 6

|Interior stages|
|---|


|Damage analysis interior areas|
|---|


###### Figure 3.1 - Flow diagram of hydraulic analysis in LACPR framework (Chapter 3)



---PAGE-38---



###### 3.1 JPM-OS method

In 2006 and 2007, a team from the Corps of Engineers, FEMA, NOAA, private sector, and academia developed a new process for estimating hurricane inundation probabilities, the Joint Probability Method with Optimal Sampling process (JPM-OS). This work was initially begun for the Louisiana Coastal Protection and Restoration technical evaluation (LACPR), but now is being applied to Corps work under the 4th supplemental appropriation, the Interagency Performance Evaluation Team (IPET) risk analysis, and FEMA Base Flood Elevations for production of DFIRMs for coastal Mississippi, Louisiana, and Texas.

For most Joint Probability Methods, several thousand events are evaluated. With the JPM-OS method, optimal sampling allows for a smaller number of events to be used. The JPM-OS method computes the frequency of occurrence of surges at specific geographic points or stations. For each of these points a surge response from each of 152 specific storms is required. The JPM-OS method has been used to derive the still water elevation, wave height, and wave period frequency curves at specific points using output from ADCIRC and STWAVE. JPM-OS takes into account the joint probability of forward speed, size, minimum pressure, angle of approach and geographic distribution of the hurricanes. For more details, the reader is referred to Resio et al. (2007), see Annex B.

The output from the ADCIRC and STWAVE models used in the JPM-OS analysis are the maximum still water elevation and maximum wave characteristics (significant wave height, peak period, and wave direction) at specified points. An example of the model output at two locations is shown in Figure 3.2. The wave characteristics along Lake Pontchartrain are typically windgenerated and depth-limited waves. There is a high correlation between the wave height and the wave period and between the surge level and wave height for this area. In contrast, the results at the MRGO are much more scattered. The relationship between the surge level and the wave height is less evident, and the wave period strongly varies as a function of the wave height. Long wave periods are observed for a few storm conditions. The long wave periods are related to swell waves from the ocean.



---PAGE-39---



| |
|---|
| |


###### Figure 3.2 - Numerical results at Lake Pontchartrain (upper panel) and MRGO (lower panel) from ADCIRC and STWAVE (2007 base condition) Note: The marks (o, x, +) represent 152 storm results.



---PAGE-40---



Surge level frequency curves can be estimated from output from the 152 storms. Along the West Bank, there were instances where there was no output from the 152 storms because these points are dry for a specific storm. In this case, estimates were made of the surge elevation for the missing output so that the frequency analysis continued to be based on 152 values. For the nodes which formed the ADCIRC grids, the topographic elevation was modified for all cases where the surge value for all storms did not produce a surge at that node. After this multiplication, an additional check was made and if the surge was less than 0.0, the surge was set to 2.5 feet.

The original set of 152 storms was selected in such a way that it covered the probabilities in the range of 1/50 – 1/3,500 per year with main emphasis on the range 1/50 – 1/500 year. In the framework of LACPR, the frequency analysis with the JPM-OS method ranges from 1/100 per year to 1/2,000 per year. The 1/2,000 year return period is near the upper end of the original storm set limits and it can be expected that the results for the upper end are more uncertain than the results for the 1/100 – 1/1,000 year range. Nevertheless, we believe that the results can be used after careful checks within the LACPR evaluation because the main purpose is a relative comparison between the various alternatives during these events rather than an exact determination of the hydraulic boundary conditions for these extreme events.

###### 3.2 Fit procedure for surge levels

The LACPR analysis evaluates alternative storm surge risk reduction systems using many levee alignments. ADCIRC grid geometry was created to model the system and provide results from which levee heights can be determined. As described in Section 2.5, a subset of storms was selected from the suite of 152 storms for simulation on the appropriate geometry. For instance, only 48 storms were computed for the 2010 LACPR East A grid.

In order to use the JPM-OS software to create statistical files to compare against the original 152 storms modeled for the 2007 base condition, a surge value was needed for the storms not simulated for that particular geometry. Commonly there is a relationship between the original results from the 2007 base condition and the results for the other conditions (2010 base condition, East A grid, East B grid, etc.). If no variances exist in a specific area, one may expect similar results for the 2007 condition and another condition. If changes to the nearby coastal hydrodynamic features have occurred however (e.g. adding a barrier), one may expect an altered response in the distinctive condition surge levels. To find a relationship between the surge level effect of a specific condition (i.e., East A grid) and the original surge level (2007 base), we examined the results for a few cases (Figure 3.3 and Figure 3.4) in the New Orleans area. Note that the 2010 case includes the barrier at the entrance of GIWW in the New Orleans East area.

Based on inspection of various plots, we have chosen to use the following relationship between the effect on the maximum surge level and the original maximum surge level of 2007:

2

Δζ2010−2007 = a1ζ2007 + a2ζ2007 Equation (1)

where: Δζ : difference in maximum surge level [ft]



---PAGE-41---



ζ2007 : maximum surge level 2007 [ft] a1, a2 : coefficients [-, 1/ft]

The coefficients a1, a2 are fitted using the data of the storms available using a MATLAB routine.

- Figure 3.3 - Correlation between maximum surge levels at Lake Pontchartrain for 2010 base condition and 2007 base condition




---PAGE-42---



- Figure 3.4 - Correlation between maximum surge levels at Lake Pontchartrain for 2010 base condition and 2007 base condition


The final step for the surge levels is to compute the 152 storm results for the new situation (2010, 2010 LACPR East A, 2010 LACPR East B, etc.). For this purpose, the fitted line according to Eq.

(1) has been used for all storms (including the storms that were originally run for the new situation). The 152 results for the new situation are used as input for the probabilistic JPM-OS method to obtain the frequency curves.

For specific cases, the correlation of the fit is relatively low. One example is shown in Figure 3.5. This plot shows the effect on the surge levels for 2010 LACPR East A condition (i.e. full closure of Lake Pontchartrain). As can be observed, the correlation between the surge level of the base case (2007 conditions) and the effect of the surge level between 2010 LACPR East A and 2007 conditions, according to Eq. (1) is not very good. Despite this low correlation, we have produced 152 storm results based on this fit and computed the frequency curve using the JPM-OS method. Note, that points of no-data (-99999) are discarded and not used in the created polynomial curve fit between the datasets.



---PAGE-43---



- Figure 3.5 - Effect of maximum surge level at Lake Pontchartrain (2010 East A grid) with fit for all storms


Due to the low correlation we have investigated whether the various storm tracks could explain this low correlation. In the Figure 3.6 the colored dots indicate the various hurricane tracks: black = track 1, green = track 2, red = track 3, blue = track 4. It can be observed that the relationship between the surge level of 2007 conditions and the effect of the surge level for the data points of track 1 (black points) is very good. The relationships for the other tracks are not as strong. Nonetheless they are considerably better than the fit based on all storms. Because of this, we have produced fits for each storm track separately using Eq. (1) and computed surge levels for the 152 storms applied to the 2010 LACPR East A scenario using the track information of each storm. These results have been used to compute the frequency curves for the surge levels.



---PAGE-44---



- Figure 3.6 - Effect of maximum surge level at Lake Pontchartrain (2010 East A grid) with fit for different storm tracks


A comparison was made between the 1% surge levels based on both methods, viz. the fit with multiple curves based on storm tracks and the results from a single curve with without regard to storm track. Although the data fits appear to be much better for each track separately, it appears that the final 1% surge levels differ less than 0.5ft. Nevertheless, the fitting procedure based on the multiple tracks has been applied throughout the entire LACPR evaluation.

###### 3.3 Fit procedure for wave characteristics

Similarly to the surge levels, the wave characteristics of the various conditions (2010 base, 2010 LACPR East A, 2010 LACPR East B, etc.) are also likely to be related to wave characteristics of the base case (2007 conditions). However, the relationship between the waves from 2007 and the other conditions (2010, 2010 LACPR East A, etc.) appears to be much less strong than for the maximum surge levels. This has to do with the sensitivity of the wave characteristics to small water level changes. Another issue is that the roughness formulation in STWAVE has been changed for the 2010 conditions (and other LACPR alternative conditions). The STWAVE model was executed with no bottom friction formulation for the 2007 conditions. Especially near the levee, the roughness influence is relatively high because of the limited water depth. Therefore, a good fit



---PAGE-45---



between the original 2007 condition wave results and the new 2010 condition wave results cannot be expected.

- To circumvent this problem, we have chosen to make a fit between the surge level and the wave characteristics for each alternative condition. Based on plots we have adopted the following relationships (see also Figure 3.7 and Figure 3.8):

2

1

2

1

b p

b

- s


T a

H a

ζ

ζ

=

=

Equation (2)

where: Hs : significant wave height [ft]

- Tp : peak period [s] ζ : Maximum surge level [ft] a1, b1, b2, a2: coefficients


The coefficients a1, a2, b1 and b2 were fitted using the data of the storms available using a MATLAB routine.

The final step for the wave characteristics was to compute the 152 storm results for the new situation (2010, 2010 East A, East B, etc.). For this purpose, the fitted line according to Eq. (2) has been used for all storms (including the storms that were originally run for the new situation) using the fitted surge levels for that specific grid. Note, similarly to maximum surge levels, point locations with no-data were discarded and not used to create the fit.



---PAGE-46---



###### Figure 3.7 - Wave characteristics at Lake Pontchartrain for 56 storms

###### Figure 3.8 - Wave characteristics at MRGO for 56 storms



---PAGE-47---



Summarizing, frequency statistics are computed for surge, wave heights, and wave periods, for all LACPR alternative conditions. For each LACPR alternative condition, using the curve fitting methodology described in this and the previous section, point files were created for surge, for wave heights, and for wave periods. Each file contains 152 values derived as above. These files are then input to the probabilistic JPM-OS software to obtain the frequency curves for the surge, wave heights, and wave periods. In this manner, 50-year, 100-year, …., 1950-year, 2000-year values are obtained for surges, as well as wave heights, and wave periods. In addition the standard deviation of the surge level as a function of frequency is also obtained.

###### 3.4 Validity of fit procedure

As listed in Table 2.2, a subset of 42 storms was selected for simulation for the East B grid. In order to validate the surge fitting model previously described, the remaining 112 storms of the full suite of 152 storms were simulated for the East B levee configuration. Statistics were computed for all of the point sets using the JPM-OS code to produce the full range of returns from the 50through 2000-year return values. The L274 point group was selected for initial evaluation. A table of differences was computed for the 100 -year surge values between the fitted model results and the full suite of 152 storm results. Figure 3.9 shows the 100-year return values resulting from the analysis of East B using the full 152 storm suite versus the 40 storm suite.

As can be seen in Figure 3.9 the results are almost identical and follow a straight line which indicates they are the same. It appeared that approximately 30% (91 points) of the 100-year surges for the 152 storm set were between 0.1 to 1.3 feet less than the fitted model values. Approximately 24% (67 points) were exactly the same 100-year surge elevations. The remaining 56% were between 0.1 to 1.4 feet above the fitted model values. There were 2 outliers of 7.8 and

- 4.2 feet. These were located away from the coast, towards the upper Pearl River Basin. The larger differences for these 2 points are most likely due to data processing errors. For the 100year surge levels, a standard deviation of 0.63 feet was computed for the absolute difference between the results based on the full storm suite and the 40 storm suite. Also, if the 2 outlier points are disregarded, the standard deviation is 0.34 feet. Thus, the fitted model procedure results agree relatively well with the full 152 storm suite results.




---PAGE-48---



|East B Surges<br><br>0<br><br>5<br><br>10<br><br>15<br><br>20<br><br>25<br><br>0 5 10 15 20 25 1% SWL East B using 152 Storms<br><br>1%SWLEastBusing42Storms<br><br>East B Surges|
|---|


Storms

###### Figure 3.9 - Comparison between the 1% still water levels based on the full storm set of 152 storms and based on the 42 storms using the fit procedure



---PAGE-49---



###### 4 DETERMINATION OF LEVEE HEIGHTS

This chapter gives an overview of the design approach for the levee heights. The frequency results of the various hydraulic variables are the inputs for this analysis (Figure 4.1). The design procedure adopted herein has been developed in the framework of the current 100-year levee and floodwall design effort for the Greater New Orleans Hurricane and Storm Damage Risk Reduction System at the New Orleans District. Several simplifications have been applied to make this procedure applicable for LACPR.

The outline of this chapter is as follows. First, the step-wise approach for the levee design is presented and the simplifications in the LACPR technical evaluation are described (Section 4.1). Next, the general assumptions of the levee design approach are discussed in more detail (Section

- 4.2). Finally, the procedure to account for uncertainties in the levee design procedure is briefly explained (Section 4.3). The final levee heights are input into the determination of the overtopping volumes (Chapter 5) and for producing construction cost estimates. The cost estimates of the levee designs are described in a separate report.


chapter 2

|ADCIRC modelling|
|---|


|STWAVE modelling|
|---|


Water levels

Waves

chapter 5 chapter 3

|Frequency analysis|
|---|


|Damage analysis exterior areas|
|---|


||Levee design|
|---|
<br><br>chapter 4|
|---|


|Overtopping analysis|
|---|


|Cost estimate levees/floodwalls|
|---|


chapter 6

|Interior stages|
|---|


|Damage analysis interior areas|
|---|


###### Figure 4.1 - Flow diagram of hydraulic analysis in LACPR framework (Chapter 4)



---PAGE-50---



###### 4.1 Step-wise design approach

The design procedure below gives a step-wise approach for determining the levee height, within the framework of LACPR, from a hydraulic perspective. The step-wise approach is intended to be used for each section that is more or less uniform in terms of hydraulic boundary conditions (water levels, and wave characteristics) and geometry (levee, floodwall, structure). The procedure has been developed within the framework of the current 100-year levee and floodwall design effort for the Greater New Orleans Storm Damage and Hurricane Risk Reduction System at the New Orleans District.

A levee design was made for three different levels of risk reduction (100-year, 400-year and 1000year). Several simplifications have been applied in the step-wise approach to make the procedure applicable and suitable for LACPR. The step-wise design approach for a given return period has been adopted for LACPR as described in Table 4.1:

Table 4.1 – Step-wise approach

|Step|Description|
|---|---|
|0 – Definition of reaches|For each planning subunit, the surge levels and wave characteristics are examined. Based on the variation in the hydraulic boundary conditions and the orientation, the flood risk reduction system was divided into one or more reaches. For each reach, one or more suitable output locations were selected from the LACPR point set.|
|1 – Water elevation|For each levee reach the surge levels from the frequency analysis were reviewed. Based on the quality of the data a suitable output point was selected. Volume II (Results) discusses in detail the selected output points for all reaches.|
|2 – Wave characteristics|The wave characteristics were extracted from the same output location as the surge levels. The wave height at the toe of the structure is assumed to be reduced as a result of depth-limited breaking according to Hsmax = 0.4 h. The wave period has not been changed.|
|3 – Overtopping rates|The overtopping rate is computed using the Van der Meer formulations (see textbox). For this purpose, a simplified levee design is assumed (Figure 4.2). The steep sloping sections near the crest and near the toe are assumed to be 1:4. In between, a wave berm is present to reduce the amount of overtopping. For all cases, the wave berm factor (γb) is set at 0.7 in the Van der Meer equations and the slope equals 1:4. The other influence factors regarding wave incidence, roughness and vertical wall are all set to 1.0. Hence, we assume a perpendicular wave attack against a grass-sloped levee without a wall on top.|
|4 – Monte Carlo simulations|The final step is a Monte Carlo simulation to compute the overtopping rate from step 3 a large number of times (5,000). Every time, the hydraulic variables and the coefficients of the overtopping equation are changed to account for the uncertainties in these parameters. The approach is explained in detail in the Section 4.3. Based on the 5,000 results, the probability distribution of the overtopping rate is determined. A check is carried out to see if the overtopping rate does not exceed the overtopping criterion of 0.1 cfs per ft with 90% confidence. If yes, the design process is finished and the levee height is set. If not, the levee height is lowered and the calculation repeated until this criterion is reached (see also Annex B).|




---PAGE-51---



|For the purpose of LACPR, the Van der Meer equations have been adopted to compute overtopping rates for levee sections. The overtopping formulations from Van der Meer are (see TAW document):<br><br>⎟<br><br>⎟ ⎠<br><br>⎞ ⎜<br><br>⎜ ⎝<br><br>⎛<br><br>= −<br><br>⎟<br><br>⎟ ⎠<br><br>⎞ ⎜<br><br>⎜ ⎝<br><br>⎛<br><br>= −<br><br>β<br><br>β<br><br>γγ<br><br>ξγγγγ<br><br>γξ α<br><br>m f<br><br>c<br><br>m<br><br>m b f v<br><br>c b<br><br>m<br><br>H<br><br>R gH<br><br>q with imum<br><br>H<br><br>R gH q<br><br>1 max : 0.2exp 2.6<br><br>1 exp 4.75<br><br>tan<br><br>0.067<br><br>0<br><br>3<br><br>0<br><br>0 0<br><br>3 0 0<br><br>(1)<br><br>With: q : overtopping rate [cfs/ft] g : gravitational acceleration [ft/s2] Hm0 : wave height at toe of the structure [ft] ξ0: surf similarity parameter [-] α : slope [-] Rc : freeboard [ft] γ : coefficient for presence of berm (b), friction (f), wave incidence (β), vertical wall (v)<br><br>The coefficients -4.75 and -2.6 in Eq. 1 are the mean values. The standard deviations of these coefficients are equal to 0.5 and 0.35, respectively and these errors are normally distributed (see TAW document).<br><br>Eq. 1 is valid for ξ0 < 5 and slopes steeper than 1:8. For values of ξ0 >7 the following equation is proposed for the overtopping rate:<br><br>( )⎟⎟⎠<br><br>⎞ ⎜<br><br>⎜ ⎝<br><br>⎛<br><br>+<br><br>= − −<br><br>0 0<br><br>0.92 3<br><br>0<br><br>0.33 0.022<br><br>10 exp<br><br>γfγβ m ξ<br><br>c<br><br>m<br><br>H<br><br>R gH q<br><br>(2)<br><br>The overtopping rates for the range 5 < ξ0 < 7 are obtained by linear interpolation of eq. 1 and 2 using the logarithmic value of the overtopping rates. For slopes between 1:8 and 1:15, the solution should be found by iteration. If the slope is less than 1:15, it should be considered as a berm or a foreshore depending on the length of the section compared to the deep water wave length. The coefficients -0.92 is the mean value. The standard deviation of this coefficient is equal to 0.24 and the error is normally distributed (see TAW document).|
|---|




---PAGE-52---



|Still water level<br><br>Wave height, wave period<br><br>1:4 slope<br><br>1:4 slope<br><br>wave berm<br><br>|Parameters settings Van der Meer: Slope α = ¼ (-) Berm factor γb = 0.7 (-) Other influence factors γf = γβ = γv = 1.0 (-) Overtopping criterion qmax = 0.1cft/s per ft (90%-value)|
|---|
|
|---|


- Figure 4.2 - Simplified levee cross section in LACPR evaluation


###### 4.2 Design assumptions

This section briefly discusses the most important choices and assumptions in the design approach. These items are:

- • Full dependency between surge levels and waves
- • Simultaneous occurrence of maxima
- • Breaker parameter
- • Overtopping criteria


Full dependency between surge levels and waves

The step-wise design approach below is (partly) probabilistic in the sense that it makes use of the derived water levels and wave characteristics based on the JPM-OS method (see also Chapter 3). The procedure also includes an uncertainty analysis that accounts for uncertainties in the hydraulic parameters and the overtopping coefficients. However, the approach is not fully probabilistic because the correlation between water elevation and wave characteristics is not taken into account. This assumption is an important restriction to this approach. It is likely that the presented approach is conservative because the correlation between the surge elevation and the wave characteristics is not taken into account. Depending on the situation, the impact of this assumption on the final levee height can be minimal to significant (> 1ft).

Simultaneous occurrence of maxima

Another assumption in the design approach is that the maximum water elevation and the maximum wave height occur simultaneously. Analysis of the ADCIRC and STWAVE results shows that the time lag between the peak of the surge elevation and the wave characteristics at both



---PAGE-53---



sites is small (< 1 hour). It should be noted that there are cases in which the time lag between surge and waves is larger (say 1 – 2 hours). Although this assumption may be conservative for some locations, assuming a coincidence of maximum surge and maximum waves is reasonable for most of the levee and floodwall sections in our design approach.

Breaker parameter

In the design approach we compute the overtopping rates based on empirical formulations. One of the inputs to these formulations is the wave height at the toe of the structure. This value is not known, but is estimated based on the wave results from STWAVE. Because the foreshore is generally very shallow (same order as the wave height), wave breaking will play an important role in the final 600ft before the toe of the structure (floodwall/levee height). Hence, it is not likely that the wave height at 600ft in front of the structure will be equal to the wave height at the toe of the structure, but will be lower.

To account for breaking in front of the levee/floodwall we have reduced the wave height from STWAVE. An estimate of the wave height at the toe of the structure has been made by making use of a breaker parameter. The breaker parameter is the ratio between the significant wave height and the local water depth. In the literature, the breaker parameter is often a constant or it is expressed as a function of bottom slope or incident wave. A typical range for this parameter is between 0.5 – 0.78 for engineering purposes. These values are generally obtained for situations with a mild sloping bed.

However, laboratory experiments and Boussinesq runs suggest that a breaker parameter of 0.4 is a realistic choice for a relatively long shallow foreshore, as is the case around New Orleans. This value has therefore been used in the entire design approach to translate the significant wave heights based on STWAVE to the significant wave height at the toe of the structure. The wave periods from STWAVE have been used without modification.

Overtopping criterion

Hughes (2007) carried out a literature survey to underpin the overtopping criterion value that has been used in the ongoing one-percent design for the Greater New Orleans Storm Damage and Hurricane Risk Reduction System (see USACE, 2007). The survey showed that although various numbers have been proposed, the experimental validation of these numbers is very limited. Typical values are: (see also TAW, 2002):

- • 0.001 cfs/linear ft (cfs/ft) for sandy soil with a poor grass cover;
- • 0.01 cfs/ft for clayey soil with a reasonably good grass cover;
- • 0.1 cfs/ft for a clay covering and a grass cover according to the requirements for the outer slope or for an armored inner slope.


In spring 2007, USACE decided to make use of a maximum overtopping criterion of 0.1 cft/s per ft. This implies that the inner slope of the clay levee/floodwall has a well-maintained grass cover. An assurance criterion of at least 90% was used in accordance with the latest Corps guidelines (April



---PAGE-54---



2007). In the framework of LACPR this criterion has been applied without changes for all design events (100-year, 400-year, 1000-year)3.

###### 4.3 Uncertainty analysis

The design criterion in the framework of LACPR is defined as follows: the overtopping rate should be less than 0.1 cft/s per ft with 90% assurance”. To determine this overtopping rate, a Monte Carlo analysis has been carried out that accounts for uncertainties in water elevations, waves and the coefficients in the overtopping formulations. Notice that we neglect the uncertainties in the geometrical parameters. In other words: we assume that the proposed heights and slopes in this design document are minimum values achieved during construction. The text below gives a brief description of this method. For more information, the reader is referred to USACE (2007).

The probability density distributions of the hydraulic variables and the coefficients in the wave overtopping formulation are inputs into the Monte Carlo Simulation. Frequency results of the surge levels and the waves were used from the JPM-OS method. These values are the so-called “best estimates” (or mean values). An additional analysis has provided the standard deviation in the 1% still water elevation. Standard deviation values of 10% of the average significant wave height and 20% of the peak period were used; these were based on expert judgment (Smith, pers. comm.). The standard deviations of the coefficients in the Van der Meer formulations are described in the textbox in section 4.1. All uncertainties are assumed to normally distributed.

The Monte Carlo Analysis applied herein is executed as follows:

- a) Draw a random number between 0 and 1 to set the exceedance probability p.
- b) Compute the water level from a normal distribution using the expected value 1% surge level and standard deviation as parameters and with an exceedance probability p.
- c) Draw a random number between 0 and 1 to set the exceedance probability p.
- d) Compute the wave height and wave period from a normal distribution using the expected value 1% wave height and 1% wave period and the associated standard deviations and with an exceedance probability p.
- e) Repeat step 3 and 4 for the three overtopping coefficients in the overtopping formula, independently, using estimates of variability (standard deviation) in each coefficient.
- f) Compute the overtopping rate for these hydraulic parameters and overtopping coefficients
- g) Repeat the steps 1 through 5 a large number of times (N = 5,000)
- h) Compute the 50%, 90% and 95% value of the overtopping rate (i.e. q50, q90 and q95)


The procedure is implemented in MATLAB. Several test runs show that 5,000 runs are sufficient to reach statistically stationary results for q50, q90 and q95. The computation time to perform this

- 3 Note that the overtopping criteria have been slightly changed for the 1% design effort in August 2007 after consultation of ASCE review team (USACE, 2007). The overtopping rate should also be less than 0.01 cfs per ft at the 50% confidence limit. Additional analysis shows that this criterion is almost everywhere fulfilled with the original criterion. The LACPR methodology has therefore not been updated with this extra criterion.




---PAGE-55---



analysis is in the order of tens of seconds on a current state of the art personal computer. Thus, the proposed method is straightforward and can be applied in a relatively quick way.

###### Figure 4.3 shows the result of this design process. The probability of non-exceedance is shown as a function of the overtopping rate. The levee design height for this specific section is 24ft. With this height, the 90% overtopping rate is 0.082 cfs per ft which meets the design criterion.

- Figure 4.3 - Result for 100-year design height along MRGO levee (2010 base condition)




---PAGE-56---



###### 5 OVERTOPPING RATES

This chapter describes the determination of the overtopping rates (Figure 5.1). Within the framework of LACPR an estimate of the overtopping rate are needed for a given return period. The temporal variation of the hydraulic boundary conditions to compute the overtopping rate for a given return period is not easily available from ADCIRC and STWAVE. Therefore, the temporal variation of the surge level and the wave characteristics is parameterized (Section 5.1). These three load factors are used as input to the overtopping formulae, in addition to the design heights of the levees to compute the overtopping rates (Section 5.2). The overtopping rates are used as input for the interior stage analysis (Chapter 6).

chapter 2

|ADCIRC modelling|
|---|


|STWAVE modelling|
|---|


Water levels

Waves

||Overtopping analysis|
|---|
<br><br>chapter 5|
|---|


- chapter 3

- chapter 4


|Frequency analysis|
|---|


|Damage analysis exterior areas|
|---|


|Levee design|
|---|


|Cost estimate levees/floodwalls|
|---|


chapter 6

|Interior stages|
|---|


|Damage analysis interior areas|
|---|


- Figure 5.1 - Flow diagram of hydraulic analysis in LACPR framework (Chapter 5)


###### 5.1 Parametrical description of hydrographs

The overtopping discharge, whether due to wave overtopping or free overflow, is determined from the variation in time of the surge level and the wave characteristics. In the framework of LACPR the overtopping rates need to be determined for a given return period. To estimate these rates, a



---PAGE-57---



description is needed of the temporal variation of the hydraulic boundary conditions for that specific return period. However, these variations in time are not directly available from the numerical models ADCIRC and STWAVE. Time series are available for a specific set of storms (with a maximum of 152) for the water level, wave height and wave period. A typical hydrograph at a given point is given in Figure 5.2.

- Figure 5.2 - Example of hydrograph from ADCIRC results


Within the framework of the JPM-OS method, a conditional approach has been adopted (see Resio, 2007). This implies that all parameters can be determined as a function of the surge level (ηmax) for a given return period (1/100 years, 1/500 years, etc). Along similar lines, the shape of a hydrograph is also likely to be correlated to the maximum surge level. One may expect that a correlation can be found between the maximum surge level and the width of a hydrograph, normalized by the maximum surge height. This means that the shape of the hydrograph is more peaked for large surges than for a smaller surge at the same location. Although the maximum surge level of a hydrograph at a given location is much higher, the width of the normalized hydrograph will be less than the width of a normalized hydrograph corresponding to a smaller maximum surge level.

Based on these considerations, a parametric hydrograph has been developed which takes into account the variation of the shape of the hydrograph for the 152 (or less) storms. For this process, we have chosen to assume a Gaussian shape for the hydrograph:

###### ( )

2 max

η t t

t − −

###### ( ) σ

η

e

###### =

2

2 max

η



---PAGE-58---



with: η : surge level [ft] σ : width of hydrograph [hrs]

- tηmax : moment with maximum surge level [hrs]


Because the hydrographs clearly show an asymmetric behavior with time, a distinction has been made between the surge level curve before the peak and after the peak. For both sides, the width of the hydrograph is estimated from the zero-th and second-order moments for the upper 30% of the normalized hydrograph (Note: the subscripts l and r refer to left-hand and right-hand side of the hydrograph):

( )

τη

max

∫

2

t t dt

( )

η σ

(0.7* )

τ η

= ( )

l r

max ,

l r

, max

τη

∫

t dt

( )

η

(0.7* )

τ η

l r

max ,

with: σ : width of hydrograph [hrs] t : time [hrs]

- Figure 5.3 presents one example of the real hydrograph from ADCIRC and the estimated Gaussian shaped hydrograph. Based on visual inspection it can be concluded that the shape of the top of the hydrograph is well represented by the fitted Gaussian formula. A more detailed view of the same comparison is shown in Figure 5.4. This figure presents a comparison between the real and the parameterized hydrograph at one location for one storm. The dots represent the output from ADCIRC in time along the hydrograph. It can be observed that the fit is good (R2 =


- 0.99).




---PAGE-59---



- Figure 5.3 - Real hydrograph from ADCIRC (in red) and parameterized hydrograph (in red)

- Figure 5.4 - Normalized surge from ADCIRC plotted against the normalized parameterized surge


The next step is to establish a relationship between the width of the hydrograph and the maximum surge level. A log-linear fit has been used. Figure 5.5 presents this relationship for one output point in which the crosses represent the storms. Although the scatter is quite large, there is a visible tendency for smaller widths with higher surge levels. Furthermore, it appears that the correlation seems to be better for higher surge levels. This is related to the fact that the upper 70% of the hydrograph of a severe storm scenario has a better defined peak compared with a mild to



---PAGE-60---



moderate storm. Because the scatter in the fits cannot be disregarded, this aspect has been taken into account in the uncertainty analysis of the overtopping discharges. This will be further discussed in Section 5.2.

- Figure 5.5 - Width of the hydrograph plotted against the maximum surge level Note: Crosses indicate the different storms; the lines are the fit through the data points.


Apart from the surge levels, the temporal variation in the wave characteristics may also play a role in the overtopping rates. A similar approach as described above could be used for the wave characteristics as well. It appears, however, from the wave data that the variation in wave height around the peak surge is not considerable. In our approach, we have therefore used the maximum wave height for the entire surge hydrograph. A sensitivity analysis has been executed and the impact on the total overtopping volume appears to be small.

###### 5.2 Overtopping volumes

The overtopping rates have been computed using empirical equations. In contrast with the design approach in Chapter 4, the surge level may be (far) above the crest level for some cases. For instance, a 100-year level of risk reduction in combination with a 1000-year event can easily give



---PAGE-61---



surge levels higher than the crest level. Therefore, two contributions are taken into account for the overtopping rate computation: wave overtopping and free flow overtopping.

To compute the overtopping rates a distinction has been made between two cases:

- • Surge level below the crest level : only wave overtopping
- • Surge level above the crest level : wave overtopping and free flow


For the situation with wave overtopping only, the empirical equations from Van der Meer have been applied (see Chapter 4). If the surge level is above the crest level, both free flow and wave overtopping are taken into account (TAW, 2003):

##### qtot = m (η− zcrest)3/2 +0.13 gHs3 (5.1)

with: qtot : total overtopping rate (cft/s per ft)

⎛

⎞

2 3

2 0.5

⎜ ⎝

m : weir coefficient ⎟ ⎠

= g ≈ 3.1ft / s 3

g : gravitational acceleration (= 32.2 ft/s2) zcrest : crest level [ft] η : water level [ft] Hs : significant wave height [ft]

The first contribution in Eq. 5.1 is due to free flow, the second part is due to wave overtopping.

The overtopping rates have been computed using a Monte Carlo Simulation to account for the various uncertainties. The uncertainty in hydrograph width is initially considered, followed by the uncertainties in wave height, wave period and the coefficients of the overtopping formulation. The following procedure is followed:

- a) Set the confidence level of the overtopping rate (in this case: 10%, 50% or 90%)
- b) Compute the width of the hydrograph associated with this probability from step a) using the expected values and the standard deviation (assuming a normal distribution).
- c) Draw a random number between 0 and 1 to set the exceedance probability p.
- d) Compute the maximum water level from a normal distribution using the expected value 1% surge level and standard deviation as parameters and with an exceedance probability p.
- e) Generate a hydrograph with this maximum water level and the given width of the hydrograph (10%, 50% or 90%)
- f) Compute the wave height and wave period from a normal distribution using the expected value 1% wave height and 1% wave period and the associated standard deviations and with an exceedance probability p.
- g) Repeat step c) and d) for the three overtopping coefficients in the overtopping formula, independently, using estimates of variability (standard deviation) in each coefficient.
- h) Compute the overtopping rate for these hydraulic parameters and overtopping coefficients




---PAGE-62---



- i) Repeat the steps c) through h) a large number of times (N = 5,000)
- j) Select the overtopping rate from the results at i) with the confidence level at step a)


The procedure is implemented in MATLAB to automate this procedure.

The above described approach results in overtopping rates with a 10%, 50% and 90% confidence. As an example, Figure 5.6 presents the overtopping rates as a function of time for one levee design with a 100-year level of risk reduction. Every plot has a unique label at the top:

- • DSX: Design standard with X-year return period (in this case 100-year)
- • RPX: Hydraulic boundary condition with X-year return period (in this case 100/400/1000/2000-year)
- • BSX: Base situation at location X (in this case 0001)
- • BS : Evaluated situation (BS = Base situation, EA = East A, EB = East B, etc)


So, each plot represents a different return period for the hydraulic boundary conditions, viz. 100year, 400-year, 1000-year and 2000-year. Furthermore, each plot gives the 10%, 50% and 90% overtopping rates in different colors.



---PAGE-63---



- Figure 5.6 - Overtopping rates for different return periods (100-year, 400-year, 1000-year and 2000year) at a level with a 1% design elevation A few remarks are made regarding Figure 5.6:


- • The maximum overtopping rate for the 100-year hydraulic situation equals about 0.1 cft/s per ft because this was the design criterion of the levee section. For the higher return periods the overtopping rates increase with several orders of magnitude.
- • The 1000-year and 2000-year return period give free flow over the levee because the maximum surge level is higher than the levee crest.
- • The form of the overtopping curve is not symmetrical but resembles the relatively steep front of the surge.


In total, approximately 6,000 overtopping hydrographs have been produced with the automated script for the LA-East alternatives. This number consists of 7 (Louisiana East alternatives) x 35 (planning subunits) x 2 (two levee sections per subunit on average) x 4 (hydraulic return periods) x 3 (design levels). These overtopping volumes have been used as an input into the interior drainage modeling which is discussed in Chapter 6.



---PAGE-64---



###### 6 INTERIOR DRAINAGE

This chapter discusses the process of converting overtopping into interior drainage areas into stage frequency relationships (Figure 6.1). First the internal drainage areas are defined (section

- 6.1). Next, the basic methodology for considering the interior drainage process is explained (section 6.2). Sections 6.3 to 6.5 describe the dominant processes that occur during a hurricane event which affect internal flooding: rainfall, overtopping and pumping. The interior stage frequency curves developed are used as input into the economic analysis.


chapter 2

|ADCIRC modelling|
|---|


|STWAVE modelling|
|---|


Water levels

Waves

chapter 5 chapter 3

|Frequency analysis|
|---|


|Damage analysis exterior areas|
|---|


chapter 4

|Overtopping analysis|
|---|


|Levee design|
|---|


|Cost estimate levees/floodwalls|
|---|


||Interior stages|
|---|
<br><br>chapter 6|
|---|


|Damage analysis interior areas|
|---|


- Figure 6.1 - Flow diagram of hydraulic analysis in LACPR framework (Chapter 6)


###### 6.1 Storage areas

Within each planning unit the area within the authorized levee systems or for which levees are being planned have been sub-divided into smaller areas, called internal planning subunits. Most of the existing internal planning subunits are located in the vicinity of the city of New Orleans. New planning subunits have been developed for areas such as the north shore of Lake Pontchartrain where there currently is no levee but in one of the alternatives a levee is planned (termed semi-



---PAGE-65---



internal planning subunits). Within the metropolitan areas of New Orleans the internal planning subunits have been defined either by parish boundaries or other defined features (such as raised roads or existing internal levees). For evaluation purposes the planning subunits in Planning Unit 3a, 3b and 4 are grouped into interior drainage areas. See Volume II for maps and further discussion of planning subunits.

###### 6.2 Methodology

Each internal or semi-internal planning subunit has been schematized as a box model for which a stage-storage curve has been established. This information has been extracted from existing rainfall-runoff models or from LIDAR data for these areas. During a hurricane event the water balance is dominated by rainfall, wave or surge water overtopping and pumping (see Figure 6.2). The interior stage frequency has been based on the sum of the overtopping volume together with rainfall in the subunit. The effect of pumping in reducing flood volume has been taken into account if applicable. Where economic sub-basins join, a flow of water has been allowed to occur between areas above defined thresholds.

rainfall

pumping

overtopping

storage area

- Figure 6.2 - Principle water system


The rainfall used in the evaluation was the 10-year rainfall and the development of the rainfall hydrograph is described further in Section 6.3.

For each of the overtopping edges of an internal planning subunit, overtopping hydrographs were established based on the levee design height or the current authorized levee heights, whichever was the higher. These hydrographs are described in more detail in Section 6.4.

An example of an internal planning subunit development is shown in Figure 6.3 below. This shows the extent of an area, the stage storage relationship (in acre-ft) extracted or developed, and the overtopping lengths of the levees adjacent to the internal planning subunit.



---PAGE-66---



||Algiers Storage Curve<br><br>-15<br>-10<br>-5<br><br><br>0<br><br>5<br><br>10<br><br>15<br><br>20<br><br>25<br><br>0 20000 40000 60000 80000 100000 120000 140000 160000 Volume (Acre-ft)<br><br>Stage(ftNAVD88(2004.65))|
|---|
<br><br>Stage(ftNAVD88(2004.65))|
|---|


tage(ftNAVD88(2004.65))

1 mile

- Figure 6.3 – Example internal planning subunit and stage storage relationship


###### 6.3 Rainfall

The LACPR technical evaluation concentrates on the development of flood risk reduction systems (wetlands, levees) that protect against a range of hurricane surge events. Rainfall, however, also contributes to the interior flooding. Although this phenomenon is not the primary focus of this effort, rainfall has been taken into account. Based on earlier work, it appears that the heaviest rainfall have been from storms of less than hurricane intensity (Shoner and Molansky, 1956). In other words, it is not likely that an extreme hurricane event (100-year event, 400-year event, etc.) coincides with a rare rainfall event.

In order to evaluate the large number of LACPR alternatives on a comparable basis, a constant rainfall event was applied across all storm surge events (100-year, 400-year, etc.), confidence bands (10%, 50% and 90%) and for all planning units. Interior drainage is in essence fixed so that interior responses to overtopping over the flood risk reduction system can directly be compared from one plan to another. The rainfall event values were obtained for a range of storm durations from TP-40 documentation. These data were used because the hydrologic work done for the South East Louisiana Urban Flood Control Project (SELA) applied these data.

The basic assumption in the populated areas of New Orleans is that pumping can cope with 1” of rainfall in the first hour, and 0.5” in subsequent hours. Using this assumption, the various 10-year rainfall events (3-hour, 6-hour, 12-hour, 24-hour) were evaluated and the 6 hour duration storm was shown to give the highest rainfall rate over pumping. Since simple stage storage curves do not account for lag times, routing, etc (it is instantaneous), the shorter duration 6 hour 10-yr frequency rainfall intensity was used so that the simple stage storage curve would more closely replicate flooding as predicted with the unsteady flow HEC-RAS analysis performed by IPET.

The total rainfall is 6.5” for a 10-year rainfall event of 6 hours according to TP40 documentation. The rainfall hydrograph was calculated as a sinusoidal distribution over a six hourly period, and values were obtained in steps of 5 minutes. Note that in reality, the temporal development of rainfall events can be quite different from a sinusoidal shape. Figure 6.4 shows the standardized



---PAGE-67---



rainfall hydrograph resulting from this 10 year return period rainfall event. The rates are given in cft/s per square foot and a sinusoidal curve has been assumed. No routing of rainfall has been considered within the volume balance model. All rainfall collecting within a 5 minute time step is assumed to be available for pumping at the same time.

Rainfall

0.016

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


0.014

0.012

Rainfall(ft/sperft2)

0.010

0.008

0.006

0.004

0.002

0.000

0 1 2 3 4 5 6 Time (hrs)

- Figure 6.4 - Standardized rainfall hydrograph


###### 6.4 Overtopping

The levee overtopping rates (10%, 50% and 90% confidence) were computed using the methods described in Chapter 5 for a number of different design standards (100, 400, and 1000-year) and the range of return periods 100, 400, 1000 and 2000 years. Examples for the 100-year design standard and 100- and 400-year storm events for the New Orleans East internal planning subunit are given in Figure 6.5. These show both the rainfall hydrograph and the levee overtopping hydrographs for three different defense lengths. In the same way as with the rainfall no allowance has been made for flood routing between the levees and the pumps.



---PAGE-68---



|Rainfall and overtopping (10% confidence band)<br><br>0<br><br>20000<br><br>40000<br><br>60000<br><br>80000<br><br>100000<br><br>120000<br><br>140000<br><br>160000<br><br>180000<br><br>0 50 100 150 200<br><br>Timestep (5min)<br><br>Rainfallandovertopping(cfts)<br><br>Rainfall<br><br>Hydrograph1<br><br>Hydrograph2<br><br>Hydrograph3<br><br>Hydrograph4<br>|
|---|


|Rainfall and overtopping (10% confidence band)<br><br>0<br><br>20000<br><br>40000<br><br>60000<br><br>80000<br><br>100000<br><br>120000<br><br>140000<br><br>160000<br><br>180000<br><br>0 50 100 150 200<br><br>Timestep (5min)<br><br>Rainfallandovertopping(cfts)<br><br>Rainfall<br><br>Hydrograph1<br><br>Hydrograph2<br><br>Hydrograph3<br><br>Hydrograph4<br>|
|---|


Rainfallandovertopping(cfts)

Rainfallandovertopping(cfts)

|Rainfall and overtopping (50% confidence band)<br><br>0<br><br>20000<br><br>40000<br><br>60000<br><br>80000<br><br>100000<br><br>120000<br><br>140000<br><br>160000<br><br>180000<br><br>0 50 100 150 200<br><br>Timestep (5min)<br><br>Rainfallandovertopping(cfts)<br><br>Rainfall<br><br>Hydrograph 1<br><br>Hydrograph2<br><br>Hydrograph3<br><br>Hydrograph4<br>|
|---|


|Rainfall and overtopping (50% confidence band)<br><br>0<br><br>20000<br><br>40000<br><br>60000<br><br>80000<br><br>100000<br><br>120000<br><br>140000<br><br>160000<br><br>180000<br><br>0 50 100 150 200<br><br>Timestep (5min)<br><br>Rainfallandovertopping(cfts)<br><br>Rainfall<br><br>Hydrograph 1<br><br>Hydrograph2<br><br>Hydrograph3<br><br>Hydrograph4<br>|
|---|


Rainfallandovertopping(cfts)

|Rainfall and overtopping (90% confidence band)<br><br>0<br><br>20000<br><br>40000<br><br>60000<br><br>80000<br><br>100000<br><br>120000<br><br>140000<br><br>160000<br><br>180000<br><br>0 50 100 150 200<br><br>Timestep (5min)<br><br>Rainfallandovertopping(cfts)<br><br>Rainfall<br><br>Hydrograph1<br><br>Hydrograph2<br><br>Hydrograph3<br><br>Hydrograph4<br>|
|---|


|Rainfall and overtopping (90% confidence band)<br><br>0<br><br>20000<br><br>40000<br><br>60000<br><br>80000<br><br>100000<br><br>120000<br><br>140000<br><br>160000<br><br>180000<br><br>0 50 100 150 200<br><br>Timestep (5min)<br><br>Rainfallandovertopping(cfts)<br><br>Rainfall<br><br>Hydrograph1<br><br>Hydrograph2<br><br>Hydrograph3<br><br>Hydrograph4<br>|
|---|


vertopping(cfts)

Rainfallandovertop

- Figure 6.5 - Rainfall hydrograph of New Orleans East (100-year design standard) for a 100-year return period (left) and a 400-year return period (right)


###### 6.5 Pumping

Pumping for each drainage area has been considered as a fixed rate of outflow. The pumping rates were obtained from the Corps for those locations where pumps were thought to exist. The values ranged from around 20,000 cft/s in East Jefferson to around 800 cft/s in St Charles Norco. Once the volume of pumping is exceeded by the inflow into the area in any 5 minute time step then flooding occurs.

New pump capacities were not estimated because of time limitations and the complexity of analyzing a very complex interior drainage system. For instance, the New Orleans area is



---PAGE-69---



composed of numerous interior pumping stations that are fed by a complex system of canals and subsurface drainage systems. The primary stations along the outfall canals are operated in conjunction with the other stations. In order to increase the capacities of the outfall canal pumping stations and make sure that the added capacity is usable, one would have to redesign the complete interior delivery system to insure that flow could reach the outfall canal pump station.

###### 6.6 Flood volumes and stage frequencies

The rate of flooding in each time step is considered by comparing the rate to the pumping rate and then if the difference is positive, recording the difference. These positive rates are then summated and multiplied by 300 to convert per second rates to totals over 5 minutes and then divided by 435,000 to convert from cubic feet to acre-feet. This gives a total volume of flooding for this condition. This is repeated for each confidence band and each design standard.

The flood stage in each internal planning subunit is established by interpolating the total flood volume into the stage storage relationship (as shown in section 6.2). The stage for each return period and design event is then compared with the levee height and the event surge height and the higher stages are capped at the higher of the levee height or surge elevation.

For those interior planning subunits which are internally connected the total flood volumes are used within separate calculations to consider the volumes flowing between adjacent storage areas and then to see whether the combined system fills above the levels of the divides or to the top level of the levees (see Figure 6.66).

sub-unit 1 sub-unit 2

- situation 1
- situation 2
- situation 3


- Figure 6.6 - Water volumes flowing between adjacent subunits




---PAGE-70---



###### 7 REFERENCES

- 1. Plan Formulation Atlas, April 16 2007, http://lacpr.usace.army.mil/default.aspx?p=atlas
- 2. Resio et al., 2007. White paper on estimating Hurricane Inundation Probabilities, USACE, ERDCCHL.
- 3. TAW, 2003. Technische Adviescommissie voor de Waterkeringen, Leidraad kunstwerken (In Dutch), May 2003.
- 4. TAW, 2002: Wave runup and overtopping at Dikes, Technical Report, Delft, 2002. See also: www.tawinfo.nl.
- 5. USACE, 2007. Elevations for design of hurricane protection levees and structures, Lake Pontchartrain, Louisana and vicinity hurricane protection project, west bank and vicinity. Draft report, Final report, Prepared by New Orleans District, 15 October 2007.
- 6. TAW, 2002. Technical Report Wave Run-up and Wave Overtopping at Dikes, Delft, The Netherlands.
- 7. IPET, 2007. Performance Evaluation of the New Orleans and Southeast Louisiana Hurricane Protection System, L.E. Link (editor).
- 8. FEMA, 2007. Flood insurance Study: Southeastern Parishes Louisiana, DRAFT, Intermediate Submission 1: Scoping and Data Review. September 19, 2007. FEMA Region 6 and USACE MVN District.
- 9. R.L. Pfost, 1993. Technical Attachment Rainfall patterns and Hurricane Andrew. A Hydrometeorological Survey, Lower Mississippi River Forecast Center, Slidell, Louisiana
- 10. R.W. Shoner and S. Molansky, 1956. Rainfall associated with Hurricanes. National Hurricane Research Project. Report No. 3. Prepared under P.L.71, 84th Congress, 1st Session.
- 11. Hughes, S.A., 2007: Evaluation of Permissible Wave Overtopping Criteria For Earthen Levees Without Erosion Protection, ERDC-CHL, Vicksburg.
- 12. U.S. Army Corps of Engineers, 2001: Coastal Engineering Manual. Engineer Manual 1110-2-1100, U.S. Army Corps of Engineers, Washington, D.C. (in 6 volumes).


###### =o=o=o=



---PAGE-71---



###### Annex A Sea level rise



---PAGE-72---



Author: Kevin Knuuti, ERDC-CHL

Variations and trends in the relationship between local mean sea level (LMSL) and land elevations are important considerations in the planning and design of structures in areas that are currently tidally influenced or that could become tidally influenced in the future. In areas where the LMSL is rising relative to land elevation, the relative sea-level rise (RSLR) is often divided into a global increase in water mass (eustatic rise), a rise in local water level due to density changes in the water (steric rise), and a drop in local land elevation (subsidence). Throughout the 20th century, the global average SLR due to eustatic and steric effects has been approximately 1.8 mm/year (Meehl, 2007). Examination of tide gauges on geologically stable platforms in the northern Gulf of Mexico indicates a regional average SLR of approximately 1.8-2.0 mm/year during that same time period. Throughout coastal Louisiana, rates of subsidence exceed the rate of SLR by varying amounts. The resulting rates of RSLR throughout coastal Louisiana are significantly higher than the global average and regional average SLR rates.

Though the causes of climate change and future projections of climate change are somewhat controversial, it is well accepted that RSL has been rising across coastal Louisiana and will continue to do so in the future. Because of the difficulty associated with quantifying the rates of SLR that will occur in different areas of Louisiana, a sensitivity analysis is performed to determine how different project designs would respond to a range of SLR rates. For this sensitivity analysis, an extrapolation of the historic rates of RSLR is used as the low level for future sea-level rise and accelerated rates of rise based on National Research Council (NRC, 1987) and Intergovernmental Panel on Climate Change(IPCC) (Meehl, 2007) projections are used for higher rates of rise. Historic rates of RSLR vary across Louisiana and also vary depending on the methods used to estimate those rates. The two most commonly cited methods of estimating historic RSLR rates in Louisiana are radiometric dating of organic deposits (mostly peat) and analysis of long-term tidegauge data. Because the RSLR rates determined from tide gauge data are based on more recent (20th century) data and because these rates are generally greater than the rates determined from radiometric dating, tide gauge RSLR rates are used for the low rate of RSLR in the sensitivity analysis.

Both the National Ocean Service and the U.S. Army Corps of Engineers have maintained longterm water-level gauges that can be used to calculate historic RSLR rates across coastal Louisiana. Because of the distance between these gauges, and the engineering difficulty associated with using numerous historic RSLR rates for analysis, coastal Louisiana was divided into different geomorphic regions for RSLR analysis. Within each geomorphic region, subsidence rates were thought to be relatively uniform due to relatively homogeneous geologic conditions. The geomorphic regions considered were based on the historic shifting of the Mississippi River’s main stem and the associated delta lobes the river created, as shown in figure A.1 and as described by Penland (1990). Based on similarities in historic RSLR rates, alternative screening further grouped the regions into three primary geomorphic regions: the Chenier Plain (region 1 in figure A.1), the Delta Plain (regions 2-6 in figure A.1), and the Pontchartrain Basin (region 7 in figure A.1).



---PAGE-73---



| |
|---|


Figure A.1, from Penland, 1990

Future rates of RSLR were determined by considering both the 1987 NRC global mean SLR projections and the 2007 IPCC global mean SLR projections, along with estimates for local and regional subsidence rates across coastal Louisiana. While the 2007 IPCC projections are considered the most current and rigorous effort to estimate future global mean SLR rates there has been some criticism that these projections do not adequately consider the potential for extreme scenarios such as massive ice loss and melting from Antarctica. The 2007 IPCC mean central value estimate for global mean SLR by 2100 is 0.343 meters and the upper limit value is 0.59 meters. Due to the uncertainties associated with the IPCC estimate methods, a conservative value of 0.5 meters of rise by 2100 is used for rigorous sensitivity analysis, with the acceleration rate being the same as that described in the 1987 NRC report and modified by Knuuti (2002):

eqn A.1

(see Knuuti, 2002, for description of variables and derivation of equation). To account for possible extreme scenarios of global mean SLR and the associated RSLR across Louisiana, the sensitivity analysis also considered the “Curve III” value from the 1987 NRC report, which estimates a global mean SLR of 1.5 meters by 2100. Estimates of local and regional subsidence rates were calculated by subtracting the regional historic SLR rate (2.0 mm/year) from the local and regional RSLR rates described earlier. These subsidence rates were combined with the future projections described in the previous two paragraphs to determine local and regional projections for future rates of RSLR. Table A.1 summarizes the RSLR values developed for the sensitivity analysis scenarios.



---PAGE-74---



Table A.1: Relative Sea-Level Rise Values, 50-year project life

| |Relative Sea-Level Rise Values between 2010 and 2060 (meters)| | |
|---|---|---|---|
|Basis for value|Chenier Plain|Delta Plain|Pontchartrain Basin|
|Historic rate|0.2|0.4|0.2|
|Future scenario 1|0.4|0.6|0.4|
|Future scenario 2|0.8|1.0|0.8|


References:

National Research Council (NRC), 1987. Responding to Changes in Sea Level: Engineering Implications.

Corps of Engineers policy, as described in ER 1105-2-100 (dated 22 April 2000), Knuuti, K. (2002). “Planning for Sea-Level Rise: U.S. Army Corps of Engineers Policy” in Solutions to Coastal Disasters ’02. ASCE, Alexandria, VA. Meehl, G. (Intergovernmental Panel on Climate Change), 2007. The Scientific Basis.



---PAGE-75---



###### Annex B The maximum possible intensity and its use for coastal hazard estimation



---PAGE-76---



###### The Maximum Possible Intensity and Its Use for Coastal Hazard Estimation Don Resio

The Maximum Possible Intensity (MPI) of a hurricane has been recognized as a parameter that critically affects the probabilities of extreme tropical cyclone intensities at least since the late 1970’s) (see for example: World Meteorological Organization, 1976 and Mooley, 1980). Even before that time, theoreticians had recognized the existence of thermodynamic and dynamic constraints on the energy available for tropical cyclone intensification, even when it is unencumbered by the proximity of land (see for example: Riehl, 1954; Miller, 1958; and Malkus and Riehl, 1960). More recently, Emanuel (1986, 1991) and Holland (1997) formulated theoretical models for estimating maximum tropical cyclone intensity. In an evaluation of the performance of these two MPI models, Tonkin et al. (2000) examined storms within 1) the Australian/southwest Pacific region, 2) the northwest Pacific region, and 3) the North Atlantic region. Since our primary interest is focused on the Gulf of Mexico, we will limit our discussion here to results for that region.

Figure 1 shows the geographic area encompassed within the “North Atlantic region” as defined by Tonkin et al. Figure 2 presents the results from Tonkin et al.’s application of the Emanuel Model (black dots joined by a solid line), Holland’s model (dashed line), and observed intensities (open triangles joined by a solid line). This application used a climatological mean Sea Surface Temperature (SST) defined over the period 1950-1979. According to Tonkin et al., Evans (1993) results suggest that there is little gain in predictive skill when actual monthly SST values are used in place of the climatological mean.

As can be seen in Figure 2 and as widely recognized from theoretical considerations, a strong relationship exists between climatological SST values and the lowest central pressures. We see that, in the range of SST values from 26o to 28o (C), the minimum central pressures of the Holland Model, the Emanuel model and the observed intensities are all in approximate agreement. Above 28o (C) the observations continue to show decreasing central pressures with increasing values of SST; whereas, the Emanuel and Holland models do not.

- Figure 3, taken from Schade (2000), shows another approximation for the MPI. In

this paper, Schade suggests that the effect of the SST field on tropical cyclone intensity is twofold. First, the large-scale ambient SST field “sets the stage for the tropical cyclone.” Second, the intensity of a tropical cyclone is highly sensitive to the reduction of the SST in the interior region of the storm due to the response of the ocean to surface winds. Thus, whereas the concept of the MPI is well founded, some of its details are still under development.

- Figure 4 shows the average August-September SST for the Gulf of Mexico for the


period 1940-2006. As can be seen here, the highest average values during this part of the



---PAGE-77---



year (the peak of hurricane season) have varied from as low as 28.17o C in 1984 to as high as 29.49o C in 1962. The dotted vertical line in Figure 3 shows this historical maximum plotted on top of Schade’s results. The heavy solid line along the top of that Figure denotes the MPI value without consideration of any negative feedback of the type discussed by Schade; thus, it is expected to represent a maximum possible threshold for the MPI. From Figures 2, 3, and 4, we can deduce that a value of 880mb represents a very sensible (perhaps slightly conservative) value for the MPI in the Gulf of Mexico.

Once the value of the MPI is established, we can construct a set of storms that represents the envelope of worst conditions for different size storms. Since the present state of the art does not indicate a strong dependence between storm size and the value of the MPI for a given ambient SST field, we will assume here that the MPI is a fixed value, independent of storm size. If we select the storm track which produces the maximum surge values for specified size and intensity, we can make the somewhat conservative assumption that integrates all storms into that class of storm track. In this context, the probability of a storm can be estimated simply from the joint probability of size and intensity along the MPI line, i.e.

###### P (storm) = P(Cp = 880mb)×P(Rp |Cp = 880mb)

If we select values of Rp ranging from small to large, we can estimate the maximum possible surges for any coastal site. This is an important improvement over concepts which attempt to relate storm surge maxima to the Saffir-Simpson scale, which considers only storm intensity.

Figure 5 shows the preliminary results of some runs with a radius to maximum winds of 25 nautical miles along three tracks. For the New Orleans area, the cumulative distribution function (CDF) for hurricane intensity (peripheral pressure minus central pressure) is given by



---PAGE-78---



p c mb R nm

( 880 and 25 )

≤ ≥ = Λ ⋅Λ

p p

1 2

⎪⎧ ⎡Δ − ⎤⎪⎫ Λ = = ⎨− − ⎢ ⎥⎬

P a F a a

[ , ] exp exp (Gumbel Distribution)

0

- 1 0 1

- 1

( ( ) )

- 2 ( )


- 2


a

⎪⎩ ⎣ ⎦⎪⎭

2 2

R P R

Δ − −

p p

1 ( | ) (Conditional Normal Distribution)

P p p

p R c e P

σ

Δ

Λ = =

( ) 2

σ π

Δ

where is the central pressure

c

p

R F

is the scale function for the radius to maximum wind speed

p

( ) is the CDF for the argument is the pressure differential = ( ) where is the peripheral pressure is the conditional mean v

P p c p R

Δ − alue of - given P is the conditional standard deviation of - given P

p

0 0

R

Δ

p

p

σ R

Δ

p

Using values for the Gumbel coefficients which are identical to those described in Resio et al. (2007) and using values for the conditional mean and conditional standard deviations capped to be no smaller than the value at 900 mb, the estimated return period for a storm with a central pressure of 880 is 2905 years. The combination of this central pressure with a size of 25 nm or larger is expected only once every 74,848 years.

- Figure 1. Geographic area considered under heading of “North Atlantic” by Tonkin et al. (2000).




---PAGE-79---



###### Figure 2. Relationship between observed minimum central pressures (maximum intensities) and sea surface temperature in the North Atlantic basin (from: Tonkin et al., 2000)



---PAGE-80---



Upper limit of historical Gulf of Mexico average SST

Location of 880mb on this h t

- Figure 3. Estimated cyclone intensity as a function of the SST under the eye of the storm (from: Schade, 2000). The solid and the dashed lines correspond to ambient relative humidities of 75% and 85%, respectively. The heavy lines mark the maximum possible intensity that is realized neglecting (negative) SST feedback. The thin lines connect points with the same ambient SST.




---PAGE-81---



|Year<br><br>AverageSeaSurfaceTemperature(C)<br><br>1940 1950 1960 1970 1980 1990 2000<br><br>28<br><br>|28.2|
|---|
<br><br>28.4<br><br>28.6<br><br>28.8<br><br>29<br><br><br>29.2<br><br>29.4|
|---|


###### ure(C)

- Figure 4. Variation of average annual (unsmoothed) Gulf of Mexico SST’s from 1940 through 2006.




---PAGE-82---



###### Figure 5. Preliminary results showing contours of the maximum elevation of maximum surges for three tracks (paths shown by sequences of red dots) for a storm with central pressure equal to 880 mb and a radius to maximum wind speed of 25 nautical miles. In these storms, the Holland B term and the pressure and size variations during approach to the coast were treated in the same fashion as the rest of the storms described in the White Paper by Resio et al. (2007).



---PAGE-83---



## Hydraulics and Hydrology Appendix Volume II – Results



---PAGE-84---



###### CONTENTS

###### Page

CONTENTS II

LIST OF FIGURES IV

LIST OF TABLES VII

LIST OF ANNEXES VII

- 1 INTRODUCTION 1

- 1.1 Scope and limitations 1
- 1.2 LACPR alternatives 1
- 1.3 Planning units and subunits 2
- 1.4 Hydraulic evaluation 2


- 2 HYDRODYNAMIC RESULTS 4

- 2.1 Introduction 4
- 2.2 2007 base condition 5
- 2.3 East models 8

- 2.3.1 2010 base condition 8
- 2.3.2 Closure options of Lake Pontchartrain and the Barataria Basin 9
- 2.3.3 Other alternative models considered 12
- 2.3.4 Future degraded landscape 14


- 2.4 West models 26
- 2.5 Statistics of storm surges and wave conditions 29
- 2.6 Discussion on East models 38


- 2.6.1 Comparison of weir with full barrier (East B with East A) 38
- 2.6.2 Comparison of closure with openings and no closure (East C with base) 41
- 2.6.3 Comparison of full block more seaward with weir closure (East D with East B) 43
- 2.6.4 Weir alternative (East B) to 2010 base - Risk reduction in and around Lake Pontchartrain and potential Impacts on Mississippi. 44
- 2.6.5 Barataria Basin 50
- 2.6.6 Conclusion 54
- 2.7 Discussion on West models 54


- 3 COMPUTATION PROCESS FOR STAGE FREQUENCIES 55


- 3.1 Introduction 55
- 3.2 Overview of approach 55


- 3.2.1 Typology of planning subunits based on their relative location 55
- 3.2.2 Hydraulic coding system 56
- 3.3 Future scenarios 61


- 3.3.1 Factors affecting the future conditions 61




---PAGE-85---



- 3.3.2 Effects on levee heights and stages 63


- 4 PLANNING UNIT 1 65

- 4.1 Introduction 65
- 4.2 Levee height 66
- 4.3 Interior and exterior frequency curves 73
- 4.4 Interconnected drainage areas 77

- 4.4.1 St Charles 77
- 4.4.2 New Orleans 77


- 4.5 Hydraulic results to planning alternatives 78
- 4.6 Plaquemines 80


- 5 PLANNING UNIT 2 83

- 5.1 Introduction 83
- 5.2 Levee heights 84
- 5.3 Interior and exterior frequency curves 91


- 6 PLANNING UNIT 3A 92 6.1 Introduction 92 6.2 Levee height 93

- 6.2.1 General 93
- 6.2.2 Ring levee alignment with secondary defense 96
- 6.3 Interior and exterior frequency curves 98
- 6.4 Hydraulic results of planning alternatives 100


- 7 PLANNING UNIT 3B 101

- 7.1 Introduction 101
- 7.2 Levee height 102
- 7.3 Interior and exterior frequency curves 107
- 7.4 Hydraulic results of planning alternatives 109


- 8 PLANNING UNIT 4 110

- 8.1 Introduction 110
- 8.2 Levee height 111


- 8.2.1 General 111
- 8.2.2 12 feet GIWW levee alignment with return 115
- 8.3 Interior and exterior frequency curves 116
- 8.4 Hydraulic results of planning alternatives 119


- 9 CONCLUSIONS AND RECOMMENDATIONS 121 9.1 Summary 121 9.2 Discussion of assumptions and simplifications 121 9.3 Recommendations for refinements to the hydraulic analysis 123
- 10 REFERENCES 124




---PAGE-86---



###### LIST OF FIGURES

- Figure 1.1 - From levee alignments and scenarios to frequency curves for plan evaluation 3
- Figure 2.1 - Maximum surge level for the 2007 base case for all 152 storms (East) 6


- Figure 2.2 - Maximum surge level for the 2007 base case for all 152 storms (West) 6
- Figure 2.3 - Maximum wave height for the 2007 base case for all 152 storms (East STWAVE grid) 7
- Figure 2.4 - Maximum wave height for the 2007 base case for all 152 storms (West STWAVE grid) 8
- Figure 2.5 - Difference in maximum surge level between the 2010 levee configuration and the 2007 base grid for the 2010 storm suite 9
- Figure 2.6 - Difference in maximum surge level between East B grid and the base grid for the East B storm suite 11
- Figure 2.7 - Difference in maximum surge level between East D grid and the base grid for the East D storm suite 12
- Figure 2.8 - Relative water level increases by reach. 13
- Figure 2.9 - Maximum surge elevation for Hurricane Katrina in meters 15
- Figure 2.10 - Maximum surge elevation for Hurricane Rita in meters 15
- Figure 2.11 - Future CLEAR/no action landscape bathymetry changes from the base condition (future condition – base condition) 16
- Figure 2.12 - Marsh analysis profiles 17
- Figure 2.13 - Storm track 17
- Figure 2.14 - Bottom elevation and surge for Storm 011 across Caernarvon 18
- Figure 2.15 - Bottom elevation and surge for Storm 011 across Barataria 18
- Figure 2.16 - Bottom elevation and surge for Storm 011 across Terrebonne 19
- Figure 2.17 - Difference between future and base conditions in bottom elevation and surge for Storm 011 across Caernarvon 20
- Figure 2.18 - Difference between future and base conditions in bottom elevation and surge for Storm 011 across Barataria 20
- Figure 2.19 - Difference between future and base conditions in bottom elevation and surge for Storm 011 across Terrebonne 21
- Figure 2.20 - Bottom elevation and 100-year water surface elevation across Caernarvon 22
- Figure 2.21 - Bottom elevation and 100-year water surface elevation across Barataria 22
- Figure 2.22 - Bottom elevation and 100-year water surface elevation across Terrebonne 23
- Figure 2.23 - Difference between future and base conditions for the 100-, 400-, and 1000-year water surface elevation across Caernarvon 23
- Figure 2.24 - Difference between future and base conditions for the 100-, 400-, and 1000-year water surface elevation across Barataria 24
- Figure 2.25 - Difference between future and base conditions for the 100-, 400-, and 1000-year water surface elevation across Terrebonne 24
- Figure 2.26 - Difference between future and base conditions for the 100-, 400-, and 1000-year water surface elevation across coastal Louisiana 25
- Figure 2.27 - Difference in maximum surge level between West A grid and the 2007 base grid

- for the West A storm suite 26

Figure 2.28 - Difference in maximum surge level between West B grid and the 2007 base grid

- for the West B storm suite 27






---PAGE-87---



- Figure 2.29 - Difference in maximum surge level between West C grid and the 2007 base grid

- for the West C storm suite 28


- Figure 2.30 - Difference in maximum surge level between the CLEAR/no action configuration and the 2007 base case for the no action marsh storm suite 29
- Figure 2.31 - Statistical water surface for the 100-year event, Planning Unit 1 30
- Figure 2.32 - Statistical water surface for the 400-year event, Planning Unit 1 31
- Figure 2.33 - Statistical water surface for the 100-year event, Planning Unit 2 31
- Figure 2.34 - Statistical water surface for the 400-year event, Planning Unit 2 32
- Figure 2.35 - Statistical water surface for the 100-year event, Planning Unit 3a 32
- Figure 2.36 - Statistical water surface for the 400-year event, Planning Unit 3a 33
- Figure 2.37 - Statistical water surface for the 100-year event, Planning Unit 3b 33
- Figure 2.38 - Statistical water surface for the 400-year event, Planning Unit 3b 34
- Figure 2.39 - Statistical water surface for the 100-year event, Planning Unit 4 34
- Figure 2.40 - Statistical water surface for the 400-year event, Planning Unit 4 35
- Figure 2.41 - L 274 point set locations in Planning Units 1 and 2 36
- Figure 2.42 - W 177 point set locations in Planning Units 3a, 3b and 4 37
- Figure 2.43 - Q 835 point set locations for whole coastline 37
- Figure 2.44 - Average differences in surge between East A and East B grids on Mississippi coast 39
- Figure 2.45 - Maximum differences in surge between East A and East B grids on Mississippi coast 39
- Figure 2.46 - Differences in 100-year surge level between East A and East B grids 40
- Figure 2.47 - Differences in 1000-year surge level between East A and East B grids 41
- Figure 2.48 - Difference in 100-year surge level between the East C and 2010 base grids 42
- Figure 2.49 - Difference in 1000-year surge level between the East C and 2010 base grids 42
- Figure 2.50 - Differences in 100-year surge level between the East D and East B grids 43
- Figure 2.51 - Differences in 1000-year surge level between the East D and East B grids 44
- Figure 2.52 - Point locations for stage frequency curves in Lake Pontchartrain 45
- Figure 2.53 - Stage-frequency curves point 294 east end of Lake Pontchartrain 45
- Figure 2.54 - Stage-frequency curves point 555 New Orleans lakefront Lake Pontchartrain 46
- Figure 2.55 - Stage-frequency curves point 570 near Madisonville of Lake Pontchartrain 46
- Figure 2.56 - Stage-frequency curves point 144 west end of Lake Pontchartrain 47
- Figure 2.57 - Difference in 100-year surge level between East B and 2010 base grids 48
- Figure 2.58 - Difference in 400-year surge level between East B and 2010 base grids 49
- Figure 2.59 - Difference in 1000-year surge level between East B and 2010 base grids 50
- Figure 2.60 - Index map showing Locations of Point for stage-frequency curves in Barataria Basin 51
- Figure 2.61 - Stage Frequency for Point 369 Barataria Basin 52
- Figure 2.62 - Stage Frequency for Point 369 Lake Cataouatche 52
- Figure 2.63 - Stage Frequency for Point 78 Lake Salvador 53
- Figure 2.64 - Stage Frequency for Point 99 L 53


- Figure 3.1 - Illustration of categories of planning subunits relative to the levee system 55

- Figure 3.2 Future factors in the framework of LACPR 62
- Figure 4.1 Planning subunits in Planning Unit 1 65


- Figure 4.2 - 2010 base model grid, 100-year design heights in Planning Unit 1 67


- Figure 4.3 - 2010 base model grid, 400-year design heights in Planning Unit 1 68




---PAGE-88---



- Figure 4.5 – East B model grid, 100-year design heights in Planning Unit 1 70
- Figure 4.6 - East B model grid, 400-year design heights in Planning Unit 1 71
- Figure 4.7 - East B model grid, 1000-year design heights in Planning Unit 1 72
- Figure 4.8 – Flow chart showing linkages between New Orleans drainage areas 78
- Figure 4.9 - Plaquemines storage areas and existing levee heights 80


- Figure 5.1 – Planning subunits in Planning Unit 2 83

Figure 5.2 - 2010 base model grid, 100-year design heights in Planning Unit 2 85 Figure 5.3 - 2010 base model grid, 400-year design heights in Planning Unit 2 86 Figure 5.4 - 2010 base model grid, 1000-year design heights in Planning Unit 2 87 Figure 5.5 - East B model grid, 100-year design heights in Planning Unit 2 88 Figure 5.6 - East B model grid, 400-year design heights in Planning Unit 2 89 Figure 5.7 - East B model grid, 1000-year design heights in Planning Unit 2 90 Figure 6.1 - Planning subunits in Planning Unit 3a 92 Figure 6.2 - West A model grid, 100-year design heights in Planning Unit 3a 93

- Figure 6.3 - West A model grid, 400-year design heights in Planning Unit 3a 94

- Figure 6.4 - West A model grid, 1000-year design heights in Planning Unit 3a 94
- Figure 6.5 - West B model grid, 100-year design heights - Morgan City 95
- Figure 6.6 - West B model grid, 400-year design heights - Morgan City 95
- Figure 6.7 - West B model grid, 1000-year design heights - Morgan City 96
- Figure 6.8 - Ring levee alignment with secondary defense, 400-year design heights in

- Planning Unit 3a 97

Figure 6.9 - Ring levee alignment with secondary defense, 1000-year design heights in

- Planning Unit 3a 98




- Figure 7.1 - Planning subunits in Planning Unit 3b 101

- Figure 7.2 - West A model grid, 100-year design heights in Planning Unit 3b 102 Figure 7.3 - West A model grid, 400-year design heights in Planning Unit 3b 103

- Figure 7.4 - West A model grid, 1000-year design heights in Planning Unit 3b 103
- Figure 7.5 - West B model grid, 100-year design heights in Planning Unit 3b 104
- Figure 7.6 - West B model grid, 400-year design heights in Planning Unit 3b 104
- Figure 7.7 - West B model grid, 1000-year design heights in Planning Unit 3b 105
- Figure 7.8 - 2007 base model grid, 100-year design heights in Planning Unit 3b 105
- Figure 7.9 - 2007 base model grid, 400-year design heights in Planning Unit 3b 106
- Figure 7.10 - 2007 base model grid, 1000-year design heights in Planning Unit 3b 106


- Figure 8.1 - Planning subunits in Planning Unit 4 110 Figure 8.2 - West A model grid, 100-year design heights in Planning Unit 4 112


- Figure 8.3 - West A model grid, 400-year design heights in Planning Unit 4 112


- Figure 8.4 - West A model grid, 1000-year design heights in Planning Unit 4 113
- Figure 8.5 - 2007 base model grid, 100-year design heights in Planning Unit 4 113
- Figure 8.6 - 2007 base model grid, 400-year design heights in Planning Unit 4 114
- Figure 8.7- 2007 base model grid, 1000-year design heights in Planning Unit 4 114
- Figure 8.8 - 12 feet GIWW levee alignment with return, 2007 West A model grid, 400-year

- design heights in Planning Unit 4 115

Figure 8.9 - 12 feet GIWW levee alignment with return, 2007 West A model grid, 1000-year

- design heights in Planning Unit 4 116






---PAGE-89---



###### LIST OF TABLES

- Table 3.1 - Hydraulic coding system for the east.................................................................................... 57
- Table 3.2 - Explanation of conditions ‘a’ and ‘b’ used in hydraulic codes (east)..................................... 57
- Table 3.3 - Example of the coding of the stage frequency results per planning subunit per alternative.............................................................................................................................. 59
- Table 3.4 - Hydraulic coding system for the west ................................................................................... 59
- Table 3.5 - Explanation of conditions ‘a,’ ‘b’ and ‘c’ used in hydraulic codes (west)............................... 60
- Table 3.6 - Example of the coding of the stage frequency results per planning subunit per alternative.............................................................................................................................. 61
- Table 3.7 - Sea level rise......................................................................................................................... 62
- Table 3.8 - Effects on levee heights and exterior and interior stages for different future scenarios............................................................................................................................... 63


- Table 4.1 - Interior and semi-interior planning subunits.......................................................................... 73
- Table 4.2 - Planning subunit to hydraulic model grid matrix ................................................................... 74
- Table 4.3 - Planning subunit interior stage frequency alternatives ......................................................... 75
- Table 4.4 - Specific planning subunit comments..................................................................................... 76
- Table 4.5 - Planning subunit to alternative matrix................................................................................... 79
- Table 4.6 - Authorized levee heights....................................................................................................... 81
- Table 4.7 - Stage values in feet for Plaquemines storage areas - based on 50% confidence level results ........................................................................................................................... 81


- Table 5.1 - Interior and semi-interior planning subunits.......................................................................... 91
- Table 6.1 - Input parameters used for design height of the Morganza back levee (stages taken from interior frequency curves).................................................................................... 97

- Table 6.2 - Internal drainage areas ......................................................................................................... 98
- Table 6.3 - Interior drainage area to hydraulic alternative matrix............................................................ 99
- Table 6.4 - Specific planning unit comments........................................................................................... 99
- Table 6.5 - Internal drainage area to alternative sets............................................................................ 100


- Table 7.1 - Drainage areas - relationship to alternative sets and hydrodynamic models ..................... 107

- Table 7.2 - Interior drainage area to hydraulic alternative matrix.......................................................... 108
- Table 7.3 - Specific planning unit comments......................................................................................... 108
- Table 7.4 - Internal drainage area to alternative sets............................................................................ 109


- Table 8.1 - Drainage areas - relationship to alternative sets and hydrodynamic models ..................... 117


- Table 8.2 - Interior drainage area to hydraulic code matrix................................................................... 117
- Table 8.3 - Specific planning unit comments......................................................................................... 119
- Table 8.4 - Internal drainage area to alternative sets matrix................................................................. 120 LIST OF ANNEXES


- ANNEX A Preliminary Hydrodynamic and Sensitivity Analysis Results
- ANNEX B Fact Sheets for Sub Basins




---PAGE-90---



###### 1 INTRODUCTION

Volume II of this appendix presents the results of the hydraulic evaluation of the LACPR alternatives. The methodology that was developed for this evaluation is discussed in Volume I.

Volume II describes the results of the processes carried out for determination of the levee heights and stage frequency curves for the five LACPR planning units. In Chapter 2 the hydrodynamic modeling (surge and waves) is discussed, being the primary input for deriving the levee heights and stage frequencies. Chapter 3 describes the process to come up with stage frequency curves for the planning subunits. Chapters 4 to 8 describe the results for each planning unit, respectively. The report ends with conclusions and recommendations in Chapter 9.

Annex A provides detailed descriptions of preliminary hydrodynamic results used either in the analysis of LACPR alternatives or for sensitivity analyses. Annex B provides maps and information related to levee heights, pumping capacity, stage storage relationships, etc. for 58 individual storage areas, or sub-basins, across South Louisiana.

###### 1.1 Scope and limitations

The work presented in Volume II has been carried out between June and April 2008 as a combined effort of the United States Army Corps of Engineers, New Orleans District, and Haskoning Inc. The methods and results as described in this report are limited to the technical aspects only and do not include the economic evaluation.

The main deliverables of the hydraulic evaluation of the LACPR work are the design levee heights and the stage frequency curves for both interior and exterior areas. These are meant as input for the economic evaluations and the damage studies.

Note that the results described in this volume were developed to enable the relative comparison of various design alternatives. More detailed studies will be needed before doing actual design.

###### 1.2 LACPR alternatives

Within the five LACPR planning units, various alternatives (sets of measures) have been developed and evaluated. An alternative may be the construction of a particular alignment of levees, it may include structures or landscape changes which reduce surge elevations further offshore, it may include nonstructural measures, such as buyout or raising of property. Most often, alternatives are proposed in combination, like the construction of levees together with the raising of property.

Alternatives (proposed sets of levees in terms of alignment and height) are designed to provide risk reduction against flooding events of a certain magnitude. The level of risk reduction provided by an alternative indicates the frequency of the flooding to which the specific alternative is to provide risk reduction, indicated in “once per a certain number of years.” For this report, three particular levels of risk reduction have been considered. These are 100-year, 400-year, and 1000year. The selection of these levels of risk reduction has been based on the request to provide the 100-year level of risk reduction, plus risk reduction for a range of hurricanes up to “Category 5.”

For the evaluation of the alternatives, the designed levee systems have been confronted with a standard set of flooding events. Here, an event is the representation of surge elevation, wave



---PAGE-91---



height, and wave period that might be expected to occur at any location with a defined frequency. The range of return periods used is 10, 100, 400, 1000, and 2000 years. The middle 3 events match with the proposed levels of risk reduction, whilst the 10 gives a lower limit and the 2000 year provides an event which will overtop all levels of risk reduction.

In this way, the amount of overtopping can be computed for each alternative for a certain frequency event. The amount of overtopping results in a water level (stage) in the protected area. Thus, a planning alternative which is designed to provide a 400-year level of risk reduction should not overtop when it is confronted with a 100-year event, but it will overtop in case of a 1000-year event. Details on the LACPR alternatives are given in the main technical report and in the chapters per planning unit in this report.

###### 1.3 Planning units and subunits

Each planning unit is divided into planning subunits. These subunits are aggregates of the census blocks used for economic data collection. Where these planning subunits fall within the authorized levee systems or where levees are being planned, these areas are the subject of calculations to determine flooding with the levees in place. Figures 4.1, 5.1, 6.1, 7.1, and 8.1 illustrate the planning subunits within each of the five LACPR planning units.

Within the existing levee systems of the metropolitan areas of New Orleans and along the West Bank of the Mississippi (planning units 1 and 2), the planning subunits were established as larger groups of census blocks and which were defined either by parish boundaries or other physical features (such as raised roads or existing internal levees). In other areas the census blocks were grouped based on flooding similarity, but limited in size by parish boundaries, proposed levee alignments and physical features.

In the west (planning units 3a, 3b, and 4) the planning subunits are derived purely from the census blocks, which are combined to form the planning subunits. These units have been split along any proposed levee alignment so that groups of planning subunits (called drainage areas) can be used within the calculations.

###### 1.4 Hydraulic evaluation

In the hydraulic evaluation, hydrodynamic results (storm surges and waves) are used to compute the levee heights and the stage frequency curves (see Figure 1.1). The stage frequency curves in their turn are an important input for the economic analysis to estimate the damage in the planning subunits. In addition, the levee heights are required so that the cost of construction and ongoing maintenance can be established.

- Step 1: Determination of the levee heights The levee height is computed for three different levels of risk reduction (100-year, 400-year, 1000year). Given the level of risk reduction, the overtopping volumes are computed for four return periods of the outside surge level and wave characteristics (100-year, 400-year, 1000-year, and 2000-year). The resulting overtopping volumes are used to compute the interior frequency curves in the planning subunits (step 2).




---PAGE-92---



- Step 2: Determination of the stage frequency curves For each planning subunit the frequency curves are extracted from the hydraulic results estimated for different levee alignments and scenarios. A single planning subunit can have either an internal stage frequency, an external stage frequency, or in some cases both an internal and an external stage frequency for a particular hydraulic model condition. A planning subunit has both internal and external stage frequencies in those cases where no levee currently exists in the model, but where a levee is planned in one of the alternatives. The stage frequency curves are used in the economic evaluation to estimate the damages caused by flooding.


planning alternatives

hydraulic results scenarios

- - high level alternative
- - barrier alternative


- - storm surges
- - waves


- - 2010
- - future with:


sea level rise settlement changes to foreshore

|stage frequency curves|
|---|
|- exterior stage frequency curves<br>- interior stage frequency curves<br>|


###### levee heights

- - design height for return period 100, 400, and 1000 years
- - overtopping rates for return period of 100, 400, 1000, and 2000 year


- Figure 1.1 - From levee alignments and scenarios to frequency curves for plan evaluation




---PAGE-93---



###### 2 HYDRODYNAMIC RESULTS 2.1 Introduction

The purpose of the hydrodynamic modeling is to provide engineering based estimates on extreme surge and wave heights for the evaluation of both existing (base) and alternative future conditions to the levee design and stage frequency analysis required for risk assessment and economic evaluation of alternatives within the LACPR technical evaluation.

The JPM-OS statistical code, Resio, was developed for an optimal sampling of storms whose coverage would approximate statistical sampling of surge responses for a domain of about 3.5 degrees longitude of the central Gulf coast. Resio designed the JPM-OS statistical code to accept the maximum ADCIRC surge response at any specified point with-in the domain of coverage. The minimum optimal sampling of storms and tracks that provide the required sampling for the desired probability space combined to include 152 storms. The 152 storm sample produces reliable statistical responses for the coastal region under examination and when viewed as a statistical surface showed no crenulations along the response surface. Too few storms would manifest itself by producing crenulations along a given frequency water surface contour where a smooth response should be expected. Including more storms than the 152 storm suite would result in additional super computer time to run ADCIRC and not appreciably add to the resolution of the response surface. The probability space covered by the chosen suite of 152 storm included storm probabilities with surge responses ranging from about 50 year to about 3500 year in recurrence interval. Details about the JPM-OS can be found in the White Paper contained in the Reference Library attached to this Appendix.

Initially, two separate sets of 152 storms and tracks were used: one for the eastern part of southern Louisiana (primarily Planning Units 1 and 2); and a second set for the west (Planning Units 3a, 3b and 4). In particular Planning Unit 3a (the Morganza area) fell in the overlap area of both of the storm suites and ADCIRC model runs. When reviewing statistical results from the JPM-OS at the western edge of the eastern storm suite, and the eastern edge of the west storm suite, it was apparent that in the overlap areas, Planning Unit 3a produced inconsistent results when considered as separate suites. Rather that attempt a blending of probabilities in Planning Unit 3a, Resio modified the JPM-OS code so that it could analyze the maximum surge responses from all 304 storms from the two separate suites. With the 304 storm suite JPM-OS code, statistical results for Planning Unit 3a would include the effects of possible storms that could affect the area and the statistical surfaces generated with the 304 storm code provided reliable and smooth water surface contouring across all planning units. Statistical surfaces for the existing and other conditions can be found in the Evaluation Results Appendix.

The reader is referred to Volume I for a full description of the applied methodology, the underlying models and assumptions. An important issue regarding the wave results from STWAVE is that only the no friction results has been used ultimately in the framework of LACPR. The results from the independent analysis suggest that compared with the STWAVE results with friction, the no friction STWAVE results provide the more appropriate wave conditions for levee design (see also Annex A). Uncertainty in future location and density of coastal marshes, in part due to local



---PAGE-94---



subsidence and the uncertainty of funding for marsh restoration, provides additional rationale for excluding the effects of friction in the near shore wave results.

In the post processing of the model results the maximum surge values were established by looking at each time step and developing the maximum value at each point within the model over time. This returns the maximum envelope of surge values for a particular storm event. In addition a peak of peaks surface was produced which took the highest value at each point from the range of storms computed. The ensemble of maximum values (from the suite of storms) was used to determine the expected return periods for the surge elevations. A similar process was undertaken from the STWAVE results for wave height and wave period.

The following sections give a brief overview of the hydraulic modeling results. Section 2.2 describes the 2007 base condition modeling. The chapter continues describe the models developed for the east and west part of the State, including changes to the marsh over 50 years. It briefly presents the processes undertaken to turn the model results into event data, before describing the selection of particular model grids for use in the further analysis. More detailed information about the modeling is provided in Annex A.

All figures presented in the following sections represent the maximum of maximum, MOM, ADCIRC response surfaces for all storms simulated, and for the east the results from the southeast STWAVE grid (which covers the east of New Orleans, the Mississippi Delta, Lake Borgne and the barrier islands) have been used to demonstrate the wave effects. It should be noted that the MOM plots are visually informative but care has to be exercised when screening for the maximum change in water level for a particular point since there is the potential for the maximum response to contain momentary instabilities in the ADCIRC run. However, it is apparent that the rather smooth change in surface contouring shown in these plots is unaffected by instabilities and that the MOM surfaces plots are indicative of maximum water levels produced by the 304 suite of storms, 152 in the east and 152 in the west.

###### 2.2 2007 base condition

The 2007 base model has been built to cover the whole of southern Louisiana and represents the situation at the start of the 2007 hurricane season. It includes post Hurricane Katrina and Rita bathymetry together with levee heights and extents which match with the current state of repaired and upgraded levees. A full set of 152 storms was run for each of the east and west parts of the model to determine water levels and corresponding wave heights to use as base conditions for the comparison of future alternatives.

- Figure 2.1 and Figure 2.2 represent the maximum surge level recorded for the 152 storms simulated for each of the east and west grids for Southeastern Louisiana. These plots do not represent a single return period surge event, but are representations of the maximum recorded value at each location from all the 152 storms run through the models. The maximum results show significant surge elevations within the existing Hurricane Storm Damage Risk Reduction System in the east, but this would be expected as the range of storms considered include storms in excess of the 3,500 year return period.




---PAGE-95---



| |
|---|


###### Figure 2.1 - Maximum surge level for the 2007 base case for all 152 storms (East)

| |
|---|


###### Figure 2.2 - Maximum surge level for the 2007 base case for all 152 storms (West)



---PAGE-96---



###### Figure 2.3 and Figure 2.4 show the maximum wave heights predicted from the range of storms run within the model for the southeastern STWAVE grid (with no friction) and the west STWAVE grid. These show the reduction in wave height as the water depth rapidly decreases at the barrier islands and in the east shows maximum heights around the existing levee system of 6 to 8 feet.

- Figure 2.3 - Maximum wave height for the 2007 base case for all 152 storms (East STWAVE grid)




---PAGE-97---



- Figure 2.4 - Maximum wave height for the 2007 base case for all 152 storms (West STWAVE grid)


###### 2.3 East models

- 2.3.1 2010 base condition


The 2010 base condition in the east represents the proposed improvements to the system that are expected to be completed by 2010. These include restoring the levees to their authorized levels and, in and around the metropolitan area of New Orleans, raising the levee heights to provide a 100-year level of risk reduction.

Initially, also included in the 2010 base run was the proposed levee for the Morganza to the Gulf feasibility study. Since the 2007 ADCIRC model runs had already addressed the base no levee condition for the Morganza area it was decided to include this proposed levee system to maximize design output from the ADCIRC runs. The Morganza levee is not expected to be completed by the 2010 date but was included in the ADCIRC runs to expedite reanalysis of the Morganza project which at the time was awaiting authorization for construction by the Congress. Around the Morganza area (to the west of Bayou Lafourche) the model included a non overtopping levee to represent the proposed new levee around the Morganza area. The Morganza project was considered to be sufficiently removed from the Planning Unit 1 and Planning Unit 2 basins so as to not influence surge responses in those basins. Figure 2.5 below in fact shows that the proximity of the proposed Morganza levee has no influence on water levels in Planning Units 1 and 2.



---PAGE-98---



| |
|---|


- Figure 2.5 - Difference in maximum surge level between the 2010 levee configuration and the 2007 base grid for the 2010 storm suite


For this conclusion, the reader should note the large area of no change separating the two response surfaces shown in Figure 2.5. To avoid confusion when looking at the 2010 base in the final analysis for which results are presented in the Evaluation Results Appendix, the 2010 base condition was reanalyzed without the proposed Morganza Levee and all 152 storms in the east were run in ADCIRC. The 304 JPM-OS code was used to compute the frequency analysis for the 2010 base condition.

- Figure 2.5 shows the differences in maximum water level between the existing (2007) model and the 2010 base condition. This shows the dramatic reduction in surge elevations within the levee systems where the improved levees reduce surge elevations. However it also indicates the increase in maximum surge levels outside the levee system (generally 1 to 3 feet, but with localized hot spots). The changes in maximum wave height are much less marked, other than within the levee system where the dramatic reduction in water depths reduces the wave heights to also nil. Plots of the wave height change are included in the Annex A.


- 2.3.2 Closure options of Lake Pontchartrain and the Barataria Basin


Four different model grids have been constructed representing four options for closing the mouth of Lake Pontchartrain (Planning Unit 1), together with three options for closing the Barataria Basin (Planning Unit 2). Note that two of the model grids used the same closure in the Barataria Basin. Of these four models, one was used for the main calculations whilst the remainders were used for screening. All four models are considered below, but more detail is given on the weir closure



---PAGE-99---



option which was used for the main comparison of closure options to non-closure options. All the models used the 2010 base model as the starting point. More details of the model set ups are given in Volume I.

Full Closure along US90 and GIWW (Model grid EA)

For Lake Pontchartrain area this model represents the closure of Lake Pontchartrain along the US90 corridor with a non-overtopping levee. This option prevents any filling of Lake Pontchartrain from Lake Borgne, but it still shows elevated water levels within the Lake as a result of the high wind speeds blowing directly over the lake waters. It also includes moving the primary levee alignment to around the edge of Lake Borgne, closing the Gulf Intracoastal Waterway (GIWW) and the Mississippi River-Gulf Outlet (MRGO). Surge values generated in Lake Pontchartrain would represent the maximum reduction in water levels achievable in the lake since the non-overtopping levee blocks all inflow from Lake Borgne regardless of storm strength and surge heights generated in the Mississippi Sound and Lake Borgne area.

For the Barataria Basin the model includes a non-overtopping levee which follows the line of the GIWW from Belle Chase across to the northern end of the Larose to Golden Meadow levee system. It also includes non-overtopping levees around the Larose to Golden Meadow area.

The results of this model are discussed in the Discussion on the East model grids (see Section 2.6).

Weir Closure along US90 and GIWW (Model grid EB)

For the Lake Pontchartrain closure, this model is the same as model grid EA except that the levee across the mouth of Lake Pontchartrain has been lowered to 12 feet. This blocks the flow of water during small events and act as a weir in extreme events allowing a reduced amount of water into the Lake. Figure 2.6 shows the difference in maximum water levels for all storms between the EB model and the 2007 base case. Reductions of the maximum surges within the Lake are in the order of 2 to 3 feet in the south and 3 to 4 feet in the north. The maximum values do increase on the outside of the weirs, particularly near the closure of the GIWW/MRGO, where the maximum levels go up by 5 to 6 feet. This rather large increase in water levels is due to the fact that the in the EB grid, levee heights are set to not overtop for the reach starting at the GIWW near South Point extending along Lake Borgne where it crosses the MRGO and continuing down around the Chalmette loop back to Carnarvon and south to it lower terminus at the east bank Mississippi River levee across from Belle Chase. Levee heights in the 2007 condition could overtop and hence maximum water levels are moderated and the differences between 2010 and 2007 are accentuated. The potential impact of this weir on the Mississippi coastline is discussed in Section 2.6.



---PAGE-100---



| |
|---|


- Figure 2.6 - Difference in maximum surge level between East B grid and the base grid for the East B storm suite


In the Barataria Basin area the EB model grid replaces the non-overtopping levee in model EA with a 12’ weir. This weir reduces the maximum water levels in the areas north west of the weir further weir, but appears to have little impact on the maximums water levels north east of the weir along the West Bank Hurricane risk reduction levee. Offshore or on the unprotected side of the weir water levels increase by up to 4 feet adjacent to the weir.

Partial closure along US90 and Weir along US90 (Model grid EC)

The EC model uses a non overtopping levee similar to EA across the mouth of the Barataria Basin, but in addition allows for openings through the levees at the Chef Menteur Pass and the Rigolets. These opening allow water to flow between Lake Borgne and Lake Pontchartrain during storm events.

Within the Barataria Basin the EC model adopts a 12’ weir along the alignment of US90, joining the levees around the Sunset Drainage District with a levee running along the east bank of Bayou Lafourche.

The results of this model are discussed in the Discussion on the East model grids (see Section 2.6).



---PAGE-101---



Full Closure through Lake Borgne (Model grid ED)

This alternative considers a non-overtopping levee built across Lake Borgne, connecting the southeastern tip of the St Bernard Parish defenses with Slidell. This alternative results in noticeable increases in maximum water level on the outside of the levee and along the Mississippi coastline, but has a marked reduction in maximum levels within the Lake Pontchartrain and within the areas to the south and east of New Orleans east and St Bernard Parish.

- Figure 2.7 shows the differences in maximum water level between the ED model grid and the 2007 base model.


The model in the Barataria Basin is the same as model grid with the full closure (East A) and is not considered further.

| |
|---|


- Figure 2.7 - Difference in maximum surge level between East D grid and the base grid for the East D storm suite


- 2.3.3 Other alternative models considered


In addition to the four major alignment grids, the following other models have been developed and run to test the impacts of changes to the system:

- - Plaquemines 1 sensitivity analysis - models the introduction of three spillways across the lower Mississippi River within Plaquemines parish;




---PAGE-102---



- - Plaquemines 2 sensitivity analysis - models the removal of all levees along the Mississippi River within the delta which allows the relatively free flow of water across the Mississippi;
- - Barrier Islands sensitivity analysis - five different models were run for a selected storm set which represented the post Katrina conditions and 4 different restored island conditions (see Annex A);
- - Future Landscape Condition for evaluating LACPR alternatives - No action based on the CLEAR model - this evaluation is described in more detail below;
- - Landscape Condition sensitivity analysis - Restored/improved marsh conditions;
- - Sea level rise sensitivity analysis - based on 9 storms using the 2010 model grid and increasing water level by 1’, 2’ and 3’. The 9 storms were selected to represent the 100-year storm event in various locations (Figure 2.8).


- Figure 2.8 - Relative water level increases by reach. The legend provides the sea level rise (1, 2, and 3 ft) and storm number (5, 9, 15, 17, 24, 36, 53, 67, 126). The regions are: SSP


= South shore Lake Pontchartrain, EO = East Orleans, SBN = St Bernard, C = Caernarvon, PE = Plaquemines East, PW = Plaquemines West, SWB = West Bank South, NWB = West Bank North, GM = Golden Meadow, MtG = Morganza to Gulf.

Surge results indicate that the relative increase in water level for a given storm and location decreases as the sea level rise increases. For instance, the response at Caernarvon for storm 24 clearly shows this effect. A sea level rise of 1ft results in a 4.5ft rise, whereas a sea level rise of 3ft results in a 2.5ft rise. The reason is that the amount of surge for a given fetch and wind speed is inversely proportional to the depth. The West Bank and Caernarvon areas showed the largest



---PAGE-103---



variability in response due to the geometric complexity in these regions. Wave results indicate that wave heights generally increase by less than 1 ft. Some areas, however, had 2-3 ft increases in wave height. As with the surge, the rate of wave height increase is less for the larger values of sea level rise.

- 2.3.4 Future degraded landscape


Topography, landscape features, and vegetation have the potential to reduce storm surge elevations and absorb wave energy. Land elevations greater than the storm surge elevation act as a physical barrier and create bathymetric resistance for the surge and waves. Landscape features such as wetlands also have the potential to create frictional resistance and affect storm surge and wave energy even when below the surge elevation. Understanding the interaction between hurricanes and coastal landscapes is important in planning hurricane flood risk reduction for South Louisiana. In the past, the level of risk reduction provided by wetlands has been empirically estimated with simple “rules of thumb” that state surge is attenuated at a rate of X feet per Y miles of marsh. However, the assumption of a constant attenuation rate implies a simple balance between gravity/water surface elevation gradient and friction. The actual situation is much more complex and dependant on many details including storm intensity, track, forward speed, and surrounding local bathymetry and topography.

The application of empirical surge reduction rates can be misleading because they do not account for the transient nature of forcing or the local topographic/bathymetric conditions. In addition, the empirical data on which these “rules of thumb” are based have a high degree of scatter (which is expected because of the complexity of the processes). A close inspection of the data used to establish the often quoted 1ft surge decrease per 2.75 miles of marsh (Corps of Engineers 1963 report), actually shows a range of values from no surge reduction to 1 ft reduction per 1 mile of marsh.

The surge reducing potential of a given wetland, then, is variable and may differ for different storms. An example of this can be seen from by comparing the predicted maximum water elevation across the Caernarvon marsh for Hurricanes Katrina and Rita. Figure 2.9 and Figure 2.10 plot the predicted peak surge elevations for Hurricanes Katrina and Rita, respectively (note that both of these simulations have been validated to high water marks). Figure 2.9 shows a reduction in surge across the Caernarvon marsh for Hurricane Katrina. For Katrina, the water level decreased 1 ft per 4.4 miles of marsh. For Hurricane Rita, however, Figure 2.10 shows an increase in surge elevations. Water levels increase over the marsh at a rate of about 1 ft per 8.7 miles of marsh because Rita blew near steady easterly to southeasterly winds toward the delta for a full day. In this scenario, the bathymetric and frictional resistance of the marsh did not play a dominant role in determining the surge level since the winds blew long enough and strongly enough to push and pile the water against the Mississippi River levees.



---PAGE-104---



| |
|---|


###### Figure 2.9 - Maximum surge elevation for Hurricane Katrina in meters Note: The arrow indicates profile across Caernarvon marsh to illustrate surge attenuation rate.

| |
|---|


###### Figure 2.10 - Maximum surge elevation for Hurricane Rita in meters Note: The arrow indicates profile across Caernarvon marsh to illustrate surge attenuation rate.



---PAGE-105---



The numerical model was applied to assess the potential increase or decrease in surge and waves due to changes in coastal marshes. The landscape conditions included a restored/improved marsh condition and a predicted wetland definition 50 years into the future with no action (primarily a degraded condition). The landscape degradation and restoration is represented in the numerical models by bathymetric and frictional resistance changes. Coastal landscape features can reduce surge potential when land elevations greater than the storm surge elevation act as a physical barrier and create bathymetric resistance for the surge and waves. These features may also reduce surge potential by reducing surface winds due to higher sub-aerial surface roughness and by slowing surge propagation due to bottom friction in shallow flow at the inundation front.

The future no action condition was developed as part of the Coastal Louisiana Ecosystem Assessment and Restoration (CLEAR) Program. The forecasting model developed by CLEAR predicts physical processes, geomorphic features, water quality, and ecological succession. Geomorphic/bathymetric changes are based on the likelihood of discretized regions changing from open water to marsh or marsh to open water. The future condition of Coastal Louisiana predicted by CLEAR predicts degradation across most of Southern Louisiana, but also predicts isolated areas of growth in the Atchafalaya basin and Breton Sound. The CLEAR future condition bathymetry was applied to the model grids and mesh and a series of storm simulations was made.

- Figure 2.11 plots the future (CLEAR/no action) landscape bathymetry changes from the base condition. The marsh areas were reduced in elevation by as much as 3 ft across large areas. The Manning n values were also reduced.


| |
|---|


- Figure 2.11 - Future CLEAR/no action landscape bathymetry changes from the base condition (future condition – base condition)




---PAGE-106---



- To illustrate the impact of marsh degradation, the analysis of changes in water surface elevation across three marsh areas (see Figure 2.12) in southeastern Louisiana will be presented. Storm 011 from the JPM-OS is used for the analysis below. Storm 011 has a central pressure of 960 mb, a radius to maximum winds of 21 nautical miles, and a forward speed of 11 knots. The storm track is plotted in Figure 2.13.
- Figure 2.12 - Marsh analysis profiles

- Figure 2.13 - Storm track




---PAGE-107---



- The variability of the surge response over different marshes for the same storm is illustrated in Figures 2.14 through 2.16, which plot the Storm 011 maximum water surface elevation across the Caernarvon, Barataria, and Terrebonne profiles, respectively. Both the base and future conditions are plotted. As the plots show, the surge for the base condition increases by 5 ft across 39 miles of the Caernarvon marsh, decreases by approximately 4 ft across 39 miles of the Barataria marsh, and decreases approximately 1 ft across 18 miles at Terrebonne. Results are similar for the Caernarvon and Barataria degraded cases, except that we see a greater increase in surge across Caernarvon and a smaller decrease in the surge for the degraded condition across Barataria. For Terrebonne, the degradation of the marsh results in surge nominally increasing across Terrebonne for this storm.
- Figure 2.14 - Bottom elevation and surge for Storm 011 across Caernarvon

- Figure 2.15 - Bottom elevation and surge for Storm 011 across Barataria




---PAGE-108---



- Figure 2.16 - Bottom elevation and surge for Storm 011 across Terrebonne


The difference in surge response between the base and future conditions is further illustrated in Figures 2.17 through 2.19, which plot the difference in both the bathymetry and the Storm 011 peak surge for the two conditions. The first thing to note in Figure 2.17 is that the Caernarvon marsh future condition includes both degradation and land building. The area of improved marsh has little impact on surge elevation. The degraded marsh on the seaward side of the originally emergent marsh, however, results in slightly lower surge seaward of the degradation and an increase in surge landward of the degraded marsh. This occurs because the reduced frictional resistance resulting from the loss of marsh allows the surge to propagate further across the marsh during the storms passage. The marsh degradation occurs over about 8 miles of marsh and the result is about a 1 ft increase in surge. Across Barataria, there are two distinct areas of marsh degradation which both result in increased surge (see Figure 2.18). The first area of degradation is approximately 7 miles and surge increases by less than 1 ft. The second area of degradation is also approximately 7 miles across but the surge increase by nearly 2 ft relative to the base condition. Further inland the surge is increased for the degraded condition relative to the base condition by about 1 ft. For Terrebonne (Figure 2.19), the entire 18 mile profile has been degraded and the surge for the future condition is slightly lower over the seaward half of the marsh and increases relative to the base case on the landward side on the order of 1 ft.



---PAGE-109---



###### Figure 2.17 - Difference between future and base conditions in bottom elevation and surge for Storm 011 across Caernarvon

###### Figure 2.18 - Difference between future and base conditions in bottom elevation and surge for Storm 011 across Barataria



---PAGE-110---



- Figure 2.19 - Difference between future and base conditions in bottom elevation and surge for Storm 011 across Terrebonne


The above analysis illustrates the complexity surge response over marshes wetlands. The response of the surge to the wetland is variable. The complex, transient nature of the forcing, the local topography/bathymetry, and the full dynamics of the governing force balance preclude the application of empirically derived constant attenuation rates. The influence of wetlands on surges was evaluated stochastically by simulating a 304 storm suite for the JPM-OS statistical methodology. Figures 2.20 through 2.22 plot the 100-year water surface elevation for both the base and the future conditions across the Caernarvon, Barataria, and Terrebonne profiles, respectively. In general, the plots indicate that the degradation that is projected to occur over the next 50 years results in relatively small changes in the 100-year water levels. Water levels for the future degraded case are typically lower over and seaward of the degraded marsh and higher landward of the degraded marsh area. These conclusions generally hold for the 400- and 1000year water surface elevations as well. Figures 2.23 through 2.25 plot the difference in the 100-, 400-, and 1000-year maximum water surface elevations for the two conditions across each profile. The increase in water surface elevation for all return periods is generally less than 2 ft. Reductions on the seaward side of marsh degradation are less than 1 ft. The plots show that the wetlands do have surge reduction potential but that it can be variable across the marsh. The degradation of the marsh essentially results in a redistribution of the water and typically more water is allowed to propagate further landward when the wetland is degraded.



---PAGE-111---



###### Figure 2.20 - Bottom elevation and 100-year water surface elevation across Caernarvon

###### Figure 2.21 - Bottom elevation and 100-year water surface elevation across Barataria



---PAGE-112---



###### Figure 2.22 - Bottom elevation and 100-year water surface elevation across Terrebonne

###### Figure 2.23 - Difference between future and base conditions for the 100-, 400-, and 1000-year water surface elevation across Caernarvon



---PAGE-113---



- Figure 2.24 - Difference between future and base conditions for the 100-, 400-, and 1000-year water surface elevation across Barataria

- Figure 2.25 - Difference between future and base conditions for the 100-, 400-, and 1000-year water surface elevation across Terrebonne
- Figure 2.26 plots the difference in peak surge elevations between the future and base conditions across all of coastal Louisiana. The plot is generally consistent with the analysis presented above with water surface elevation changes generally less than 2 ft, with the greatest change being increases landward of degraded marsh. There is essentially no change in Lake Pontchartrain and the greatest change is in the Barataria Basin. Note that in the vicinity of the Atchafalaya River, the future condition is predicted to have lower surge values than the base condition. The reason for




---PAGE-114---



this is that this area is predicted to experience land building, not loss. Reductions in western Louisiana are similar to the east with reduction of less than 2 ft.

|100-year<br><br>400-year<br><br>1000-year|
|---|


- Figure 2.26 - Difference between future and base conditions for the 100-, 400-, and 1000-year water surface elevation across coastal Louisiana


The purpose of this analysis was to apply numerical models to assess the potential of coastal landscape features for reducing storm surge and waves for hurricanes with varying intensity. The impact of landscape features on surge propagation is a relatively new application for surge and wave models and an area of active research that suffers from a lack of quality data. The analysis provides valuable information on trends and relative performance but caution should be exercised



---PAGE-115---



in making definitive quantitative assessments. Results indicate that coastal marsh does have surge reduction potential. The magnitude of the surge reduction potential is variable along the coast, with the maximum magnitude of the change generally being less than 2 ft for the 100-, 400and 1000-year elevations.

###### 2.4 West models

In addition to the 2007 baseline model, for the west three models have been developed to represent three potential levee alignments. These models are described briefly below.

Morganza and GIWW alignment (Grid WA)

This model includes a non-overtopping levee which followed the proposed Morganza alignment to the west of Bayou Lafourche, connecting with the existing levee system around Morgan City and Patterson before following a line to the seawards of the GIWW to Lake Charles, and then tying into high ground just before the Louisiana / Texas border.

- Figure 2.27 shows the differences in maximum water level between the WA model grid and the 2007 base model.


| |
|---|


- Figure 2.27 - Difference in maximum surge level between West A grid and the 2007 base grid for


- the West A storm suite




---PAGE-116---



Morganza and Retired Levee Alignment, plus ring levees (Grid WB)

This model includes an incomplete levee system around Morganza, with two lines of defense, a non-overtopping levee from Morgan City to Abbeville, following a line between the GIWW and the higher ground, with the levee returning to higher ground around the Vermillion River. To the west of the Vermillion the model included small ring levees around a couple of areas of population and a larger ring around Lake Charles.

- Figure 2.28 shows the differences in maximum water level between the WB model grid and the 2007 base model


| |
|---|


- Figure 2.28 - Difference in maximum surge level between West B grid and the 2007 base grid for

- the West B storm suite


Combined Alignments (West C)

This model considers a twin line of defense within Morganza, with a 100-year defense round the outer line and a non-overtopping levee on the inside, a lower level of risk reduction between Houma and Morgan City. Between Patterson and Abbeville the same alignment as West B has been used. From Abbeville to Lake Charles a 100-year levee was modeled along the GIWW alignment, eventually tying into a ring levee around Lake Charles.

- Figure 2.29 shows the differences in maximum water level between the WC model grid and the 2007 base model




---PAGE-117---



| |
|---|


###### Figure 2.29 - Difference in maximum surge level between West C grid and the 2007 base grid for

- the West C storm suite


Future Degraded

In the same way as for the east, a model has been developed based on the projected changes in marsh etc over the next 50 years. This prediction has been made as part of the CLEAR program. The model uses the basic 2007 grid as a starting point.

###### Figure 2.30 shows the differences in maximum water level between the CLEAR/no action model grid and the 2007 base model. The degraded landscape generally results in around a 1 to 2 ft increase in peak surges across western Louisiana with the exception of the Atchafalaya area. This is suggested to equate to possible marsh growth as a result of discharges from the Atchafalaya River.



---PAGE-118---



| |
|---|


- Figure 2.30 - Difference in maximum surge level between the CLEAR/no action configuration and the 2007 base case for the no action marsh storm suite


###### 2.5 Statistics of storm surges and wave conditions

The previous sections of this chapter have described the storm surge and wave models developed for LACPR. The results from these models represent specific storms and only the peak values were extracted from the full suite of storms. For use within the derivation of levee heights and economic damage calculations based on flood depths the results need to be translated into stage frequency relationships. This is done using the JPM-OS methodology described in volume I.

The JPM-OS methodology uses the results from the models and statistically obtains the water level or wave conditions relating to a particular return period of event. This has been done for all models at selected points (discussed further below), and for some model (the base models) for all points. Undertaking the analysis at all points within the model allows for the creation of water level and wave height surfaces for display, which cannot be easily created from the reduced point sets used for the main calculations.

The created surge and wave values do not represent a single storm event with a particular frequency. Rather they represent the water level or wave condition that could occur with that frequency. For example, if the 100-year surge level occurs along the South Shore of Lake Pontchartrain then it is very unlikely that at the same time the 100-year surge level occurs in the Barataria Basin (as the values could be higher or lower depending on the track of the storm).



---PAGE-119---



###### Surfaces of extreme water level have been prepared for some of the models for a range of event frequencies. The following figures show the 100-year and 400-year frequency water levels for the 2010 base model for Planning Units 1 and 2, and the 2007 base model for Planning Units 3a, 3b and 4 are shown here in Figures 2.31 through 2.40. A complete set of statistical surfaces for the various alternatives plans can be found in the Evaluation Results Appendix.

- Figure 2.31 - Statistical water surface for the 100-year event, Planning Unit 1




---PAGE-120---



###### Figure 2.32 - Statistical water surface for the 400-year event, Planning Unit 1

###### Figure 2.33 - Statistical water surface for the 100-year event, Planning Unit 2



---PAGE-121---



###### Figure 2.34 - Statistical water surface for the 400-year event, Planning Unit 2

###### Figure 2.35 - Statistical water surface for the 100-year event, Planning Unit 3a



---PAGE-122---



###### Figure 2.36 - Statistical water surface for the 400-year event, Planning Unit 3a

###### Figure 2.37 - Statistical water surface for the 100-year event, Planning Unit 3b



---PAGE-123---



###### Figure 2.38 - Statistical water surface for the 400-year event, Planning Unit 3b

###### Figure 2.39 - Statistical water surface for the 100-year event, Planning Unit 4



---PAGE-124---



- Figure 2.40 - Statistical water surface for the 400-year event, Planning Unit 4


To establish the stage frequencies for surge levels for use in the economic analysis, a series of points were developed that represented the planning subunits. For these points data was extracted from the models to obtain values for the 100-, 400-, 1000- and 2000-year events. The 10-year surge levels have been obtained from the 2006 FEMA Region 6 study.

In the west some problems occurred with the inland parts of the model where the statistical values of surge decayed faster than expected. The low values were adjusted to ensure that the 100-year or higher events were not lower than the 10-year value. This was achieved by raising the 100-year and higher values to be the same as the 10-year values. In addition, the values were checked to ensure a progression from the 10-year to the 2000-year, and values were adjusted if required. The process of adjustment always took the level at the higher return period and used this for lower return period events - i.e. if the 1000-year level was greater than the 2000-year level then the 1000-year level was reduced to match the 2000-year level.

The wave heights and surge levels have been extracted for a series of point files. The following three sets of points have been used:

L274 - representing a set of points in the East selected for the purposes of levee design in Planning Units 1 and 2;



---PAGE-125---



W177 - representing a set of points in the west selected for the purposes of levee design in Planning Units 3a, 3b and 4; Q835 - covering the whole model areas and used for quality control and comparison of results outside of the key design areas.

###### The spatial extent of these three data sets is given in Figures 2.41 through 2.43.

- Figure 2.41 - L 274 point set locations in Planning Units 1 and 2




---PAGE-126---



###### Figure 2.42 - W 177 point set locations in Planning Units 3a, 3b and 4

###### Figure 2.43 - Q 835 point set locations for whole coastline



---PAGE-127---



###### 2.6 Discussion on East models

There are four basic model grids for the Lake Pontchartrain area that model some form of closure of the Lake Pontchartrain. These four models represent the full (impenetrable) barrier (East A), the approximately 100-year surge level weir (East B), a full barrier with openings at Chef Menteur and the Rigoletes (East C) and a barrier across Lake Borgne (East D).

Below, the four options are compared in order to investigate their relative impacts on surge levels within Lake Pontchartrain, outside Lake Pontchartrain and along the Mississippi coastline. In addition, the East B grid has been compared to the 2010 base grid to investigate particularly the potential impacts on the Mississippi coast.

- 2.6.1 Comparison of weir with full barrier (East B with East A)


The setup and results of the full closure (East A) and weir plan (East B) have been described separately in Section 2.3.2.

Comparison of changes on Mississippi coast The weir plan results in maximum changes on the Mississippi coast of up to 3.2 ft and beyond Bay St. Louis the maximum drops to 0.8ft and to 0.5ft by Gulfport. The average change is a maximum of 2.3 ft adjacent to the Louisiana border, dropping to 0.5 ft beyond Bay St. Louis and 0.2ft at Gulfport. For the full barrier the maximum values are 5.4ft, 1.8ft and 1.3ft at the same points and the averages are 3.6ft, 0.9ft and 0.4ft.

The differences have been made by comparing the results of 36 hurricanes with different tracks and intensities that had been run for the 2010 baseline, East A and East B model grids. The maximum difference values arose from hurricanes of frequency > 400 year (i.e. similar or greater than Hurricane Katrina) with a track passing from south to north and making landfall around the end of the Barataria Bay.

These results are shown in Figure 2.44 and Figure 2.45.



---PAGE-128---



###### Figure 2.44 - Average differences in surge between East A and East B grids on Mississippi coast

###### Figure 2.45 - Maximum differences in surge between East A and East B grids on Mississippi coast



---PAGE-129---



Comparison of changes inside and outside Lake Pontchartrain Full blockage (East A) when compared to a 100-year surge level weir (East B) shows additional reductions in 100-year surge level within the lake of between 3.1 ft close to the weir to 0.1-0.2 ft on the far side of the lake. The differences are shown on Figure 2.46. Outside of the barrier levels are raised by at least 1 ft for an area from St. Bernard Parish across to the Mississippi coast. Differences are greater for the 1000-year storm where the full closure makes a larger impact on levels in the lake, reducing maximum surge levels by up to 7 ft over the weir alternative, shown in

###### Figure 2.47.

- Figure 2.46 - Differences in 100-year surge level between East A and East B grids




---PAGE-130---



- Figure 2.47 - Differences in 1000-year surge level between East A and East B grids


- 2.6.2 Comparison of closure with openings and no closure (East C with base) The results of the base condition 2010 and the partial closure (East C) are described separately in


- Section 2.3.2. Comparison of the two model grids (2010 baseline and East C) shows a limited reduction in surge levels within Lake Pontchartrain. Apart from in the area between New Orleans East and Slidell the reduction in 100-year surge with the closure with openings is less than 1ft, and it induces increases of up to 1 ft on the outside of the closure. For the 1000-year the changes are around the 1 to 1.2 ft range for the main part of the Lake, with increases of 1.5 to 2 ft outside the closure. The differences between East C and baseline are shown in Figure 2.48 and Figure 2.49.




---PAGE-131---



###### Figure 2.48 - Difference in 100-year surge level between the East C and 2010 base grids

###### Figure 2.49 - Difference in 1000-year surge level between the East C and 2010 base grids



---PAGE-132---



- 2.6.3 Comparison of full block more seaward with weir closure (East D with East B)


The East D grid represents a full block of Lake Pontchartrain, similar to East A but at a location further towards the Gulf, on a line across Lake Borgne. For the 100-year surge the differences between East D and East B show increases in surge on the outside of the barrier of around 2 feet, and increased reductions within Lake Pontchartrain of up to 3 feet. It shows very large surge reductions within the Golden Triangle area of up to 13 feet, as this is an area which before was on the outside of the weir, and now is inside.

For the 1000-year surges the differences increase, with increases of up to 3.5 feet on the outside of the barrier. This is most noticeable at the north eastern end of the barrier, adjacent to the Mississippi coast where the surge is some 3.3 feet higher.

- Figure 2.50 and Figure 2.51 show the surge differences between East D and East B for the 100and 1000-year surge levels. The key issue with the East D model would be the constructability of the barrier. To provide the degree of risk reduction given in the model the levee would need to be in excess of 26 feet at 100-year and 37 feet at 1000-year. These figures are those developed for the Golden Triangle alignment along the edge of Lake Borgne. Lake Borgne is the order of 8-10 feet deep along the alignment.


| |
|---|


- Figure 2.50 - Differences in 100-year surge level between the East D and East B grids




---PAGE-133---



| |
|---|


- Figure 2.51 - Differences in 1000-year surge level between the East D and East B grids


- 2.6.4 Weir alternative (East B) to 2010 base - Risk reduction in and around Lake Pontchartrain and potential Impacts on Mississippi.


The Lake Pontchartrain surge reduction weir plan was modeled with the East B weir set at approximately the 100-year surge level thus preventing any surges generated in the Gulf and transmitting via Lake Borgne into Lake Pontchartrain until such time that levels exceed 12 feet at the weir face. Therefore for all events where Lake Borgne stages are blocked from entering Lake Pontchartrain, surges in Lake Pontchartrain are generated only by wind shear blowing across the lake causing the normal water level in the lake to tilt up on the windward side and to depress on the leeward side.

A comparison of water level frequencies for the Lake Pontchartrain 2010 base to water level frequencies for the Lake Pontchartrain surge reduction plan, East B, for the four locations shown on Figure 2.52 follow on Figures 2.53 through 2.56.



---PAGE-134---



###### Figure 2.52 - Point locations for stage frequency curves in Lake Pontchartrain

Stage Frequency Pt 294 East End Lake Pontchartrain

16

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| |Note: The 100-yr HL stage plots at the 310-yr EB stage This example shows that on average for every one dollar at risk in a given year for the HL case thirty-two cents of that dollar would be at risk for the EB case.| | | | |
| | | | | | |
| | | | | | |
| | | | | | |


14

12

10

StageFtNAVD88

8

6

4

2

0

0 500 1000 1500 2000 2500

Frequency

EB HL

###### Figure 2.53 - Stage-frequency curves point 294 east end of Lake Pontchartrain



---PAGE-135---



###### Stage Frequency Pt 555 Lake Pontchartrain at New Orleans Lakefront

16

14

12

10

StageinFtNAVD88

EB HL

8

6

Note: The 100-yr HL stage plots at the 475-yr EB stage This example shows that on average for every one dollar at risk in a given year for the HL case only twenty-one cents of that dollar would be at risk for the EB case.

4

2

0

0 500 1000 1500 2000 2500

Frequency

###### Figure 2.54 - Stage-frequency curves point 555 New Orleans lakefront Lake Pontchartrain

Stage Frequency Point 570 North Central Lake Pontchartrain Near Madisonville, LA

14

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| |Note: The 100-yr HL stage plots at the 1150-yr EB stage This example shows in theory that on average for every one dollar at risk in a given year for the HL case only nine cents of that dollar would be at risk for the EB case.| | | | |
| | | | | | |
| | | | | | |


12

10

StageNAVD88

8

EB HL

6

4

2

0

0 500 1000 1500 2000 2500

Frequency

###### Figure 2.55 - Stage-frequency curves point 570 near Madisonville of Lake Pontchartrain



---PAGE-136---



###### Stage Frequency Pt 144 West End Lake Pontchartrain

18

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| |Note: The 100-yr HL stage plots at the 275-yr EB stage Theoretically this example shows that on average for every one dollar at risk in a given year for the HL case only thirty-six cents of that dollar would be at risk for the EB case due to the frequency| | | | |
| | | | | | |
| | | | | | |
| | | | | | |


16

14

12

StageNAVD88

10

EB HL

8

6

shift

4

2

0

0 500 1000 1500 2000 2500

Frequency

- Figure 2.56 - Stage-frequency curves point 144 west end of Lake Pontchartrain


It is interesting to note that for the point locations at the eastern and western ends of the lake the 100-year 2010 base stage (Labelled HL for High Level) corresponds to about 275 to 310 year stage. The two series are labelled EB and HL in the frequency plots. For the points located on the north and south shore of Lake Pontchartrain the shift is more pronounced. The 100-year 2010 base stage corresponds to about the 475-year EB elevation on the south shore and for the North Shore point location, the frequency shift is even greater with the 100-year 2010 base stage plotting at about the 1150-year EB frequency.

The definition of risk as applied in this discussion is as follows: Annualized risk is equal to the probability of an event occurring times the dollar value of what is at risk. A purely theoretical example of a hypothetical risk that one can use to gain some insight into just what reduction in risk could occur is discussed briefly in the note placed on each plot. The risk hypothesized, assumes that if there is a $1 risk of loss associated with the 100-year 2010 base stage at each of the points shown on the map, then based purely on the shift in annual probability of occurrence, that same 100-year stage with the EB stage frequency reduces that $1 risk to about 9 cents to 36 cents depending upon the point’s location within the lake. This example should not be interpreted to mean that the EB plan provides 100-year level of risk reduction to the areas around the Lake Pontchartrain since these points are actually in the lake and development around the lake perimeter varies in elevation and certainly some development would likely remain at risk with the 100-year water level associated with the EB plan.



---PAGE-137---



The conclusion that one can draw from the above comparisons is that the Lake Pontchartrain surge reduction plan does afford considerable risk reduction to riparian interests around the lake’s perimeter as well as to interests located within those leveed areas adjacent to the lake.

There is a potential that any changes to the hurricane risk reduction system may have an impact on the surrounding areas. Of particular interest for LACPR is the potential impact that partially closing Lake Pontchartrain may have on the adjacent Mississippi coastline. Specific work has been carried out to look at the differences between the surge frequency surfaces for the 2010 base conditions and the 12-foot weir across Lake Pontchartrain.

Figures 2.57 through 2.59 show the difference in the 100-, 400- and 1000-year still water levels outside of the barrier system.

- Figure 2.57 - Difference in 100-year surge level between East B and 2010 base grids




---PAGE-138---



###### Figure 2.58 - Difference in 400-year surge level between East B and 2010 base grids



---PAGE-139---



- Figure 2.59 - Difference in 1000-year surge level between East B and 2010 base grids


- 2.6.5 Barataria Basin


A similar comparison showing stage-frequency shifts with an accompanying risk reduction can be made in Planning Unit 2 for the Weir Surge Reduction Plan. Figure 2.60 shows point locations selected for the comparative stage frequency plots. For the Barataria Basin analysis, we again use the same nomenclature as used in the stage frequency plots for the Lake Pontchartrain analysis discussed above, i.e. HL stands for a high level levee plan (No weir, the levee alignment is shown as a red line in Figure 2.60) and EB stands for East Barrier (with-weir, the weir alignment is shown as a green line in Figure 2.60). Note that with the weir levee plan, it is assumed the “red line levee” will be in place and constructed to the 2010, 100-yr protection grade.



---PAGE-140---



- Figure 2.60 - Index map showing Locations of Point for stage-frequency curves in Barataria Basin


Comparative stage-frequency plots for the points shown in Figure 2.60 follow in Figures 2.61 through 2.64. Note that in general the amount of risk reduction associated with the EB plan is greatest in the area south of Des Allemands to the protected side of weir levee. As can be seen for point 99 north of Des Allemands EB and HL curves are essentially the same curves with the EB curve being only slightly lower in elevation. Even for the HL plan, the area north of Des Allemands appears to have a much less exposure to risk from storm surges as compared to the area south of Des Allemands.

The EB plan for Planning Unit 2 provides substantial risk reduction to the areas located behind the weir. However, as with the Lake Pontchartrain Surge Reduction Plan, the blocking or confinement of the surge to the south of the EB weir in Planning Unit 2 does create higher water levels to those areas located outside the line of protection. Therefore, the application of a weir plan must also address the inducements in areas not protected by the plan. For the weir plan, the induced flooding in those areas has been taken into account by the application of both structural and nonstructural plans in the areas where additional flooding is predicted to occur. Structural measures involve adding additional heights to existing levee systems impacted by the weir plan and the application of non-structural measures where no protection exists.



---PAGE-141---



###### Stage Frequency Pt 369 Barataria Basin

- 0
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| |Note: The 100-yr HL stage plots at the 250-yr EB stage| | | | |
| | | | | | |
| | | | | | |
| | | | | | |


StageFtNAVD88

EB HL

0 500 1000 1500 2000 2500

Frequency

###### Figure 2.61 - Stage Frequency for Point 369 Barataria Basin

Stage Frequency Pt 328 Barataria Basin Lake Cataouatche

12

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| |Note: The 100-yr HL stage plots well beyond the 2000-yr EB stage| | | | |
| | | | | | |
| | | | | | |


10

8

StageNAVD88

EB HL

6

4

2

0

0 500 1000 1500 2000 2500

Frequency

###### Figure 2.62 - Stage Frequency for Point 369 Lake Cataouatche



---PAGE-142---



###### Stage Frequency Point 78 Barataria Basin Lake Salvador

12.0

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| |Note: The 50-yr HL stage plots at the 1500-yr EB stage and the 100-yr HL stage would plot well beyond the upper limit of the EB frequency plot.| | | | |
| | | | | | |
| | | | | | |


10.0

8.0

StageNAVD88

EB HL

6.0

4.0

2.0

0.0

0 500 1000 1500 2000 2500

Frequency

###### Figure 2.63 - Stage Frequency for Point 78 Lake Salvador

Stage Frequency Pt 99 Barataria Basin Lac des Allemand

7.0

6.0

5.0

StageinFtNAVD88

4.0

EB HL

3.0

2.0

Note: The 100-yr HL stage plots very near or close to the EB stage in this area of Barataria Basin.

1.0

0.0

0 500 1000 1500 2000 2500

Frequency

###### Figure 2.64 - Stage Frequency for Point 99 L



---PAGE-143---



- 2.6.6 Conclusion

In conclusion, only the East B grid has been taken forward as an alternative to the baseline model in the analysis of differing structural alignments. This is because the impacts of the full closure on both the Mississippi coast and on constriction heights and the limited beneficial effects of the ungated openings suggest that neither of these alternatives will provide a more sustainable and cost effective alternative in hydraulic terms.

Because of the potential adverse impacts associated with LACPR plans on adjacent areas along the Mississippi coast, a comprehensive review of the system wide affects of the Louisiana plans was undertaken to ensure that those plans such as the weir barrier plan were sufficiently analyzed to determine the potential impacts on water level frequencies elsewhere in the system. Details are presented in the System Analysis Section of the main report.

- 2.7 Discussion on West models


There are four primary model grids for the west:

- - Base condition
- - West A - Continuous, non-overtopping levee from the Larose to Golden Meadow Hurricane Protection Project to west of Vinton (near the Texas border); follows the authorized Morganza alignment with a ring levee around Berwick/Patterson, then follows the GIWW west to Vinton.
- - West B - Series of regional, non-overtopping levees. Includes the authorized Morganza alignment with secondary alignment along the GIWW south of Houma; continuous levee from west of Patterson to Abbeville plus ring levees in Planning Unit 4
- - West C - Series of regional, non-overtopping levees plus 100-year levee along the GIWW from Abbeville to Vinton. Includes the authorized Morganza alignment with secondary alignment along the GIWW south of Houma; continuous levee from west of Patterson to Abbeville; 100-year levee from Abbeville to south of Lake Charles with ring levee around Lake Charles and Vinton.


Whereas in the east the model grids were developed to test a number of possible alternatives so that the most appropriate one could be identified, in the west the grids were developed to specifically model significantly different levee alignments. As such the base condition, the West A and West B grids were required to represent most of the planning alternatives proposed.

The West C grid, was proposed to investigate the twin lines of defense, and also the potential increase in general risk reduction that could be achieved by introducing a 100-year levee along the GIWW. The levee was taken at a nominal 12 feet to approximate a 100-year levee. As the modeling did not account for wave overtopping, and as the number of storms that created flooding within the levees was small, the internal stages derived from the statistics were not taken as being appropriate to use in the alternative with the 12-foot levee along the GIWW and the normal interior stage frequency calculations were carried out instead.



---PAGE-144---



###### 3 COMPUTATION PROCESS FOR STAGE FREQUENCIES

###### 3.1 Introduction

This chapter describes the general process applied to the hydrodynamic model results in order for them to be translated into the data required for hydraulic evaluation in the framework of LACPR. Section 3.2 describes the general process for the entire planning area. On some aspects the approach as applied to the planning units in the West (3a, 3b, and 4) differs from that applied in the East (Planning Units 1 and 2). Therefore, first the common approach is described, with specific attention for the deviations in East and West where applicable. In Section 3.3 the approach and values used to establish hydraulic values for the future scenarios (2060) are outlined.

###### 3.2 Overview of approach

- 3.2.1 Typology of planning subunits based on their relative location


The planning subunits that make up the planning units are the level on which the evaluation of the various planning alternatives has taken place. Based on their relative location with respect to the levee system, planning subunits can be identified in three categories (Figure 3.1):

- A external - the area is always outside of the levee system;
- B internal - the area is within a current levee system and will remain inside a levee system;
- C semi-internal - the area is currently outside of the levee system, but may become inside the levee system in the future.


- Figure 3.1 - Illustration of categories of planning subunits relative to the levee system




---PAGE-145---



The determination of the stage frequency curves for the planning subunits in these categories is discussed below:

- A A stage frequency relationship has been established representing the effects outside the levee systems for differing hydraulic models, as the levee alignments within the model can have an impact on conditions outside of the levees. The outside surge levels for different frequencies originate from the statistical analysis of the hydrodynamic model results. For more information about these models and the statistical method, the reader is referred to Chapter 3 and 4 in Volume

I.

- B The stage frequency curve has been determined representing the effects of wave/surge overtopping, rainfall and pumping. In these calculations the wave/surge overtopping volumes have been determined using the exterior waves and surge levels, and the levee characteristics. Rainfall and pumping have been included to compute the total water volume in either one or a connected series of planning subunits. The stage has been established using this volume and a single stagestorage relationship. For more information about this procedure, the reader is referred to Chapter 6 in Volume I.
- C Per planning subunit, both a stage frequency for the exterior and stage frequencies from interior drainage have been developed. This category combines Category A and B.


The stage frequency curves for the planning subunits have been developed based on the evaluation of the 10-year, 100-year, 400-year, 1000-year and 2000-year hydraulic event. They have been computed for the hydraulic model alternatives (e.g. Base, EB etc), and for areas with new levees this procedure is repeated for the different levels of risk reduction (100-, 400-, and 1000-year).

East Since in the East a levee system already exists, all three categories as described above are present in Planning Units 1 and 2. In addition, a number of special cases result in another set of internal stage frequencies. Examples of these are the introduction of the Golden Triangle alignment along the edge of Lake Borgne, or the closure of the Algiers and Harvey Canals.

West In the West there is no current levee system. Thus, no internal areas exist in these Planning Units, and all planning subunits (and drainage areas) are external (Category A) or semi-internal (Category B).

- 3.2.2 Hydraulic coding system


Various planning alternatives have been assessed using the results from the modeling efforts (see Chapter 2). These planning alternatives consider new levees, different levee alignments, and a range of flood risk reduction standards. The modeling grids that were evaluated with the surge and wave models do not always match exactly with the planning alternatives in terms of levee



---PAGE-146---



alignments. Hence, combinations of various modeling grids have often been applied to specify the conditions for a specific planning subunit in a specific planning alternative.

To ensure consistency in the approach, a coding system has been developed to specify which modeling results apply to the planning subunit for each planning alternative. As the models that have been used for the planning units in the East and the West differ, the hydraulic coding systems differ accordingly. These coding systems are described below:

East The model grids that were used in the East were:

- - 2010 base model grid (BS), used for:

- Planning Unit 1: the “High Level” alternatives (HL);
- Planning Unit 2: the West Bank Improvements and Ridge alignments;


- - East B model grid (EB), used for:


- PU1: the Lake Pontchartrain Barrier alternatives (LP);
- PU2: the GIWW weir alternatives.


Results from the models were used to develop results for stage frequencies as indicated in Table

###### 3.1.

- Table 3.1 - Hydraulic coding system for the east

|Hydraulic Code|Model Grid|Description|
|---|---|---|
|BS-ext|Baseline|Stage frequency developed from ADCIRC for areas outside of levees|
|EB-ext|East B|Stage frequency developed from ADCIRC for areas outside of levees|
|BS-xxxxa|Baseline|Stage frequency developed from internal drainage for areas inside levees protected to the xxxx level of risk reduction - condition ‘a’|
|BS-xxxxb|Baseline|Stage frequency developed from internal drainage for areas inside levees protected to the xxxx level of risk reduction - condition ‘b’|
|EB-xxxxa|East B|Stage frequency developed from internal drainage for areas inside levees protected to the xxxx level of risk reduction - condition ‘a’|
|EB-xxxxb|East B|Stage frequency developed from internal drainage for areas inside levees protected to the xxxx level of risk reduction - condition ‘b’|


- Table 3.2 explains what the various conditions represent in Planning Units 1 and 2.


- Table 3.2 - Explanation of conditions ‘a’ and ‘b’ used in hydraulic codes (east)


|Condition|Planning Unit 1|Planning Unit 2|
|---|---|---|
|a|The inner alignment around Lake Borgne (closure from B. Biennenue to Michoud Canal)|Represents the closure of the Harvey and Algiers Canals|
|b|The outer alignment around Lake Borgne (closure along Lake Borgne Shoreline)|Represents the Harvey and Algiers Canals being open|




---PAGE-147---



The planning alternatives have been coded for straightforward identification. This coding is made up of five elements:

PU1-HL-a-100-1 1 2 3 4 5

Each element for Planning Units 1 and 2 is described below.

- Element 1 PU1 Planning Unit 1 PU2 Planning Unit 2
- Element 2 HL High Level Plan Alternative (PU1) LP Lake Pontchartrain Surge reduction barrier Alternative (PU1) WBI West Bank Levee Alternative (PU2) G GIWW Weir alternatives (PU2) R Ridge alternatives (PU2)
- Element 3 a the inner alignment around Lake Borgne (closure from B. Bienvenue to Michoud Canal)

b The outer alignment around Lake Borgne (closure along Lake Borgne Shoreline) <blank> All PU2 alternatives

- Element 4 100 Alternative provides a 100-year level of risk reduction 400 Alternative provides a 400-year level of risk reduction 1000 Alternative provides a 1000-year level of risk reduction
- Element 5 Planning Unit 1 1 Existing defenses including Oakville extension 2 As 1 plus Laplace and all of the North Shore 3 As 1 plus Laplace and Slidell only Planning Unit 2


- 1 Existing defenses - plus closure of Harvey and Algiers canals and Larose to Golden Meadow
- 2 As 1 plus levees to Luling and Highway 90
- 3 As 2 plus levees to Sunset Drainage District
- 4 As 3 plus levees along Bayou Lafourche (Lockport)


Descriptions and maps of each of the LACPR alternatives are located in the Evaluation Results Appendix.

An example of the system for linking the hydraulic codes to the alternatives for the East is shown in Table 3.3 below for some of the planning subunits in Planning Unit 1:



---PAGE-148---



###### Table 3.3 - Example of the coding of the stage frequency results per planning subunit per alternative

|Planning subunit|Planning Alternative| | | | |
|---|---|---|---|---|---|
| |PU1-HL-a-400-1|PU1-HL-b-400-1|PU1-LP-a-400-1|PU1-LP-b-400-1|…|
|St Bernard Wet|BS-0400a|BS-0400b|EB-0400a|EB-0400b|…|
|St Bernard Dev|BS-0400a|BS-0400b|EB-0400a|EB-0400b|…|
|STBE_17a|BS-ext|BS-0400b|EB-ext|EB-0400b|…|
|ORLE_16b|BS-ext|BS-0400b|EB-ext|EB-0400b|…|
|STBE_14a|BS-ext|BS-ext|EB-ext|EB-ext|…|
|…|…|…|…|…|…|


West The model grids that were used in the West were:

- - Baseline model grid, referred to as WT;
- - West Model Grid A (WA), used for: Planning Units 3a, 3b, and 4; - West Model Grid B (WB), used for:


Planning Units 3a and 3b.

At the onset of the modeling the planning alternatives in the west were less well defined. This resulted in the levee alignments within the model grids not matching single planning alternatives. Therefore some combining of results from different models has been required in order to represent the planning alternatives.

Results from the models were used to develop results for stage frequencies as indicated in Table 3.4.

###### Table 3.4 - Hydraulic coding system for the west

|Hydraulic Code|Model Grid|Description|
|---|---|---|
|WT-ext|Baseline|Stage frequency developed from ADCIRC for all areas|
|WA-ext|West A|Stage frequency developed from ADCIRC for areas outside of levees included in model|
|WB-ext|West B|Stage frequency developed from ADCIRC for areas outside of levees included in model|
|WT-xxxx|Baseline|Stage Frequency developed from internal drainage for areas inside levees protected to the xxxx level of risk reduction|
|WA-xxxxa|West A|Stage Frequency developed from internal drainage for areas inside levees protected to the xxxx level of risk reduction – condition ‘a’|
|WA-xxxxb|West A|Stage Frequency developed from internal drainage for areas inside levees protected to the xxxx level of risk reduction - condition ‘b’|
|WA-xxxxc|West A|Stage Frequency developed from internal drainage for areas inside levees protected to the xxxx level of risk reduction - condition ‘c’|
|WB-xxxx|West B|Stage Frequency developed from internal drainage for areas inside levees protected to the xxxx level of risk reduction|




---PAGE-149---



- Table 3.5 explains what the various conditions represent in Planning Units 3a, 3b, and 4.


- Table 3.5 - Explanation of conditions ‘a,’ ‘b’ and ‘c’ used in hydraulic codes (west)


|Condition|Planning Unit 3a|Planning Unit 3b|Planning Unit 4|
|---|---|---|---|
|a|Continuous levee from Larose to Morgan City|Not Used|Full levee along GIWW alignment - connecting into Planning Unit 3b|
|b|Levee from Larose, returning to high ground to the west of Houma, plus Morgan City ring|Not Used|12-foot levee along GIWW together with localized ring levees|
|c|As ‘a’ but with a 100-year defense around Morganza and a secondary defense line|Not Used|Levee along GIWW, returning to high ground to the west of the Vermilion River|


The planning alternatives have been coded for straightforward identification. This coding is made up of four elements:

PU3a-M-0100-1 1 2 3 4

Each element for Planning Units 3a, 3b and 4 is described below.

- Element 1 PU3a Planning Unit 3a PU3b Planning Unit 3b PU4 Planning Unit 4
- Element 2 M Morganza Levee - from Larose to Morgan City (PU3a) RL Ring Levees - used in PU3b and 4 G GIWW alignment - used in 3a for the secondary alignment alternatives and

for the alignment along the GIWW in PU3b and 4 F Franklin alignment - used in PU3b for alignment which extends between the GIWW and the areas of risk.

- Element 3 100 Alternative designed to provide a 100-year level of risk reduction 400 Alternative designed to provide a 400-year level of risk reduction 1000 Alternative designed to provide a 1000-year level of risk reduction
- Element 4 1 PU3a Continuous levee from Larose to Morgan City PU3b All alternatives PU4 Continuous GIWW levee from PU3b to the west of Lake Charles (G) and ring levees (RL)


- 2 PU3a Levee from Larose which returns to the west of Houma to higher ground


- PU3b Not used
- PU4 GIWW levee which returns to the west of the Vermillion River




---PAGE-150---



- 3 PU3a Not Used


- PU3b Not Used
- PU4 GIWW levee at 12’ with a return and isolated ring levees


Descriptions and maps of each of the LACPR alternatives are located in the Evaluation Results Appendix.

An example of the system for linking the hydraulic codes to the planning alternatives for the West is shown in Table 3.6 below for some of the planning subunits in Planning Unit 4:

- Table 3.6 - Example of the coding of the stage frequency results per planning subunit per alternative


|Planning Subunit|Planning Alternative| | |
|---|---|---|---|
| |Base2007|PU4-G-0100-1|…|
|CALC_ 11i|WT-ext|WT-0100|…|
|CALC_ 5e|WT-ext|WT-0100|…|
|VMLN_ 10f|WT-ext|WA-0100a|…|
|VMLN_ 12d|WT-ext|WA-0100a|…|
|CALC_ 10g|WT-ext|WT-0100|…|
|CALC_ 10h|WT-ext|WT-0100|…|
|…|…|…|…|


###### 3.3 Future conditions

- 3.3.1 Factors affecting the future conditions


Part of the hydraulic evaluation of the planning alternatives is to consider the performance in the future (2060). A number of factors affect the hydraulic performance in the future. The following factors have been taken into account:

- 1. Sea level rise;
- 2. Subsidence;
- 3. Changes to the foreshore (marshes). These factors are visualized schematically in Figure 3.2.




---PAGE-151---



|0. Present situation 1. Sea level rise<br><br>2. Sea level rise with subsidence<br><br>3. Sea level rise with changes to foreshore<br><br>|
|---|


- Figure 3.2 Future factors in the framework of LACPR


These factors potentially result in higher surges and wave heights, and also affect the levee heights that are required to provide a specific level of risk reduction. In the framework of LACPR the following approach has been chosen to account for these future factors:

Ad. 1,2) Sea level rise and subsidence has been allowed for in a combined value added to the surge levels. Three scenarios have been evaluated for the relative sea level rise (sea level rise + subsidence): no sea level rise, a mid range sea level rise value and a high sea level rise value. The values used for these scenarios are given in Table 3.7.

- Table 3.7 – Relative sea level rise


|Planning Unit|No sea level rise (for sensitivity analysis only)|Mid Range|High Range|
|---|---|---|---|
|1 - Pontchartrain Basin|+ 0 ft|+ 1.3 ft|+ 2.6 ft|
|2 - Barataria Basin|+ 0 ft|+ 1.9 ft|+ 3.2 ft|
|3a – Terrebonne|+ 0 ft|+ 1.9 ft|+ 3.2 ft|
|3b - Teche/Vermilion|+ 0 ft|+ 1.9 ft|+ 3.2 ft|
|4 - Mermentau|+ 0 ft|+ 1.3 ft|+ 2.6 ft|


Ad. 3) Two future developments of the foreshore conditions have been evaluated. The first is the “maintain coast” condition which has been represented by the existing (2010) bathymetry assuming that the coastline will be maintained. In fact, the surge levels and the waves do not change in this foreshore condition. The second is the “degraded coastal features” condition which has been represented by the bathymetry computed by the CLEAR model. The degraded coastal features model has only been run for the 2010



---PAGE-152---



base condition but with a changed bathymetry. Based on these runs, the effect of a degraded foreshore on the surge levels and the waves has been quantified.

Considering the three values for sea level rise and two future coastlines, this gives six possible alternatives for the future with a range of results.

- 3.3.2 Effects on levee heights and stages


The table below summarizes how the future scenarios have been incorporated in the levee heights, and the exterior and interior stages. These effects are discussed below:

- Table 3.8 - Effects on levee heights and exterior and interior stages for different future scenarios


|Future coastline scenarios|Future sea level rise scenarios<br><br>|Levee heights|Exterior Stages|Interior stages| |
|---|---|---|---|---|---|
| | | | |No action|Maintain levee heights|
|Maintain coastline|Sea Level rise 0|Present situation + effect of sea level rise scenario|Present situation + effect of sea level rise scenario|Based on present heights with increased overtopping due to sea level rise scenario|No change with present situation|
| |Sea Level rise 1| | | | |
| |Sea Level rise 2| | | | |
|Degraded coastline|Sea Level rise 0|Present situation + effect sea level rise scenario + effect degraded coastline|Present situation + effect sea level rise scenario + effect degraded coastline|Based on present heights with increased overtopping due to sea level rise scenario + effect degraded coastline<br><br>|No change with present situation|
| |Sea Level rise 1| | | | |
| |Sea Level rise 2| | | | |


The levee heights for 2060 were established as described below (see also Table 3.8):

Maintain coastal features. For the maintained coast alternatives, the design heights were taken from the Base case which represents the current situation. These heights were increased based on the sea level rise values given in Table 3.7. for all Planning Units to determine the 2060 levee heights.

East - degraded coastal features For the degraded coastal features the future degraded model results were used to compute design heights for the ‘without barrier’ alignments. For the ‘with barrier’ option the difference in levee height between the without and with barrier alternatives was computed. This value was then added to the levee heights calculated for the future degraded model to give a ‘with barrier’ levee height for the 2060 situation. In all cases sea level rise was applied by adding the values from Table 3.7.



---PAGE-153---



West - degraded coastal features For the degraded coastal features the model results were used to compute design heights for the same levee alignments as the baseline model. For the other modeled alternatives the change in levee height from the baseline model results to alternative model results was applied to the levee heights calculated for the degraded coastal features model. In all cases sea level rise was applied by adding the values from Table 3.7 to the levee heights.

The stages for 2060 have been computed as follows (see also Table 3.8):

Exterior – Maintained coast Exterior stage frequency values for the “maintained coast” were obtained by adding the sea level rise values to the external stage frequencies established for the current conditions.

Exterior – Degraded coast For the degraded coastal features, the exterior stage frequencies have been developed from the degraded coastal model results and then increased by sea level rise. This could only be done directly for the baseline situations, because the degraded coastal features only have been evaluated for this situation. Therefore, the various alternative geometries (e.g. barrier alignment in the East or different levee alignments in the West) are treated differently. For these alternatives, the difference between the current geometry and the alternative geometry results have been applied to the degraded coastal features exterior stage frequencies of the baseline situation, and these are then adjusted for sea level rise.

Interior (East only) For interior stage frequencies, two options have been considered: “No Action” (this is used as a baseline for the economic evaluation) and with any alternative in place. In the “No Action” plan, the levee heights are kept at a constant elevation and new overtopping rates are calculated using the degraded coastal features model, and calculating the effects on overtopping of the three sea level rise alternatives. These overtopping rates are then used to develop new stage frequency tables for those planning subunits. For the alternatives, the overtopping rate is assumed to be constant as the degree of risk reduction by the levees is maintained over time, and therefore the stage frequencies did not change.



---PAGE-154---



###### 4 PLANNING UNIT 1 4.1 Introduction

This chapter presents the results of the calculations of the levee heights and the stage frequency curves for the planning subunits of Planning Unit 1 (see Figure 4.1).

- Section 4.2 describes the results of the levee heights being computed for the levee system in 2010 for the two different situations. The first is a levee system with a barrier at MRGO (called the High Level Plan, modeled in the 2010 base model grid); the second a levee system with closure of Lake Pontchartrain along US90, full closure of IHNC/GIWW along west shore of Lake Borgne, and a weir closure West Bank from Belle Chasse to Larose along GIWW (called the Barrier Plan, modeled in the East Model Grid B).


- In section 4.3 the stage frequency curves for Planning Unit 1 are determined. For the economic evaluation both the High Level plan and the Barrier plan have been evaluated in more detail. For each, four return periods have been considered for the outside surge level and wave characteristics (100-year, 400-year, 1000-year, and 2000-year). In addition, there are a number of special cases that result in additional internal stage frequencies. These are dealt with by determining a second set of internal stage frequency curves.


- Figure 4.1 Planning subunits in Planning Unit 1




---PAGE-155---



###### 4.2 Levee height

The levee height design followed the methodologies described in Volume I of this appendix. Levee heights were computed for both the High Level Plan and the Barrier Plan for three design standards (100-year, 400-year, and 1000-year) for all levees included in the modeling. Using both the waves developed from the no bed friction model and waves from the with bed friction model has resulted in two sets of levee heights. Below, only the results of the no friction wave model are presented, thus giving the more conservative design heights.

- Figure 4.2 to Figure 4.7 show the 100-year, 400-year, and 1000-year design heights in feet for the levees in Planning Unit 1 for the High Level Plan and the Barrier Plan. The design height values have been adjusted to include any adjustments made to increase the levee heights to match the authorized levee heights. In some instances the heights were also adjusted because the results from the hydrodynamic models were not considered to be representative of the locations. A detailed overview of the design height is given in the fact sheets in Annex B.


The resulting height values have been used as input for costing design options and for establishing overtopping rates.



---PAGE-156---



###### Figure 4.2 - 2010 base model grid, 100-year design heights in Planning Unit 1



---PAGE-157---



| |
|---|


###### Figure 4.3 - 2010 base model grid, 400-year design heights in Planning Unit 1



---PAGE-158---



| |
|---|


F

- Figure 4.4 - 2010 base model grid, 1000-year design heights in Planning Unit 1




---PAGE-159---



| |
|---|


###### Figure 4.5 – East B model grid, 100-year design heights in Planning Unit 1



---PAGE-160---



| |
|---|


###### Figure 4.6 - East B model grid, 400-year design heights in Planning Unit 1



---PAGE-161---



| |
|---|


###### Figure 4.7 - East B model grid, 1000-year design heights in Planning Unit 1



---PAGE-162---



###### 4.3 Interior and exterior frequency curves

Given the above described levee heights, the overtopping volumes were computed for four return periods of the outside surge level and wave characteristics (100-year, 400-year, 1000-year, and 2000-year). The overtopping volumes are an important input for determination of the interior stage frequency curves per planning subunit.

Of the 100 planning subunits in Planning Unit 1, 9 are protected by levees and it is proposed that these continue to be protected in the future. Another 36 are semi-interior, which means they are currently being outside the levee system, but may fall within a levee in one of the future alternatives. The interior and semi-interior planning subunits are listed in Table 4.1.

- Table 4.1 - Interior and semi-interior planning subunits


|Name|Type|
|---|---|
|New Orleans East|Interior|
|New Orleans - Metropolitan|Interior|
|East Jefferson|Interior|
|St Charles - Norco|Interior|
|St Charles - remainder|Interior|
|St Bernard - wetland|Interior|
|St Bernard - Developed|Interior|
|PLAQ_14s|Semi-interior (Plaquemines - Scarsdale) (requires improved levee for interior)|
|PLAQ_15s|Semi-interior (Plaquemines - Scarsdale) (requires improved levee for interior)|
|PLAQ_16s|Semi-interior (Plaquemines - Scarsdale) (requires improved levee for interior)|
|PLAQ_17s|Semi-interior (Plaquemines - Scarsdale) (requires improved levee for interior)|
|Laplace 1|Interior (no flooding when exterior)|
|Laplace 2|Interior (no flooding when exterior)|
|Madisonville_1|Semi-interior (North Shore) new levee|
|Madisonville_2|Semi-interior (North Shore) new levee|
|Madi_to_Mande|Semi-interior (North Shore) new levee|
|Mandeville_1|Semi-interior (North Shore) new levee|
|Mandeville_2|Semi-interior (North Shore) new levee|
|West_Lacombe_1|Semi-interior (North Shore) new levee|
|West_Lacombe_2|Semi-interior (North Shore) new levee|
|West_Lacombe_3|Semi-interior (North Shore) new levee|
|East_Lacombe_1|Semi-interior (North Shore) new levee|
|East_Lacombe_2|Semi-interior (North Shore) new levee|
|Slidell_1|Semi-interior (North Shore) new levee|
|Slidell_2|Semi-interior (North Shore) new levee|
|Slidell_3|Semi-interior (North Shore) new levee|
|Slidell_4|Semi-interior (North Shore) new levee|
|Slidell_5|Semi-interior (North Shore) new levee|
|Oak_Harbour|Semi-interior (North Shore) new levee|
|STTA_10e|Semi-interior (North Shore) new levee|
|STTA_11d|Semi-interior (North Shore) new levee|
|STTA_10i|Semi-interior (North Shore) new levee|




---PAGE-163---



|Name|Type|
|---|---|
|STTA_12b|Semi-interior (North Shore) new levee|
|STTA_12c|Semi-interior (North Shore) new levee|
|ORLE_15a|Semi-interior (Golden Triangle) only interior with new levee alignment|
|ORLE_16b|Semi-interior (Golden Triangle) only interior with new levee alignment|
|ORLE_17b|Semi-interior (Golden Triangle) only interior with new levee alignment|
|STBE_16a|Semi-interior (Golden Triangle) only interior with new levee alignment|
|STBE_17a|Semi-interior (Golden Triangle) only interior with new levee alignment|


For each planning subunit, Table 4.2 lists the model grids that have been used, as well as the application of the special cases. The special cases are described following the table. For those cases where several planning subunits are located within a single drainage area the name of the drainage area is listed.

- Table 4.2 - Planning subunit to hydraulic model grid matrix


| |Hydraulic Code| | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Planning Subunit|BS-ext|BS-0100a|BS-0100b|BS-0400a|BS-0400b|BS-1000a|BS-1000b|EB-ext|EB-0100a|EB-0100b|EB-0400a|EB-0400b|EB-1000a|EB-1000b|
|Laplace|x|x| |x| |x| |x|x| |x| |x| |
|St Charles Norco| |x| |x| |x| | |x| |x| |x| |
|St Charles - rest| |x| |x| |x| | |x| |x| |x| |
|East Jefferson| |x|x|x|x|x|x| |x|x|x|x|x|x|
|New Orleans Metro| |x|x|x|x|x|x| |x|x|x|x|x|x|
|New Orleans East| |x|x|x|x|x|x| |x|x|x|x|x|x|
|St Bernard Wetland| |x|x|x|x|x|x| |x|x|x|x|x|x|
|St Bernard developed| |x|x|x|x|x|x| |x|x|x|x|x|x|
|Plaquemines - Scarsdale|x|x| |x| |x| |x|x| |x| |x| |
|Golden Triangle|x| |x| |x| |x|x| |x| |x| |x|
|Madisonville|x|x| |x| |x| |x|x| |x| |x| |
|Madisonville to Mandeville|x|x| |x| |x| |x|x| |x| |x| |
|South Covington|x|x| |x| |x| |x|x| |x| |x| |
|Mandeville|x|x| |x| |x| |x|x| |x| |x| |
|West Lacombe|x|x| |x| |x| |x|x| |x| |x| |
|East Lacombe|x|x| |x| |x| |x|x| |x| |x| |
|Slidell|x|x| |x| |x| |x|x| |x| |x| |
|Other External areas|x| | | | | | |x| | | | | | |
| |x = stage frequency calculated| | | | | | | | | | | | | |


The hydraulic model grid codes at the top of the table columns relate to the various layout alternatives and corresponding sources of information; below these are listed for the 100-year design options:



---PAGE-164---



BS-ext - exterior stage frequency results from the ADCIRC modeling for grid BS; EB-ext - exterior stage frequency results from the ADCIRC modeling for grid EB;

- BS-0100a - interior stage frequency results developed for a 100-year design option -

- alternative a (see Table 4.3 below) based on the BS model grid;

BS-0100b - interior stage frequency results developed for a 100-year design option -

- alternative b (see Table 4.3 below) based on the BS model grid;




- EB-0100a - interior stage frequency results developed for a 100-year design option -

- alternative a (see Table 4.3 below) based on the BS model grid;

EB-0100b - interior stage frequency results developed for a 100-year design option -

- alternative b (see Table 4.3 below) based on the BS model grid.




The 0400 and 1000 codes refer to the 400-year and 1000-year design options.

- Table 4.3 - Planning subunit interior stage frequency alternatives


|Planning Subunit|Condition ‘a’|Condition ‘b’|
|---|---|---|
|Laplace|with levee|N/A|
|St Charles Norco|baseline|N/A|
|St Charles – rest|baseline|N/A|
|East Jefferson|baseline|effects of Golden Triangle alignment|
|New Orleans Metro|baseline|effects of Golden Triangle alignment|
|New Orleans East|baseline|effects of Golden Triangle alignment|
|St Bernard Wetland|baseline|effects of Golden Triangle alignment|
|St Bernard developed|baseline|effects of Golden Triangle alignment|
|Plaquemines - Scarsdale|with levee|N/A|
|Golden Triangle|N/A|with levee along Lake Borgne|
|Madisonville|with levee|N/A|
|Madisonville to Mandeville|with levee|N/A|
|South Covington|With levee|N/A|
|Mandeville|with levee|N/A|
|West Lacombe|with levee|N/A|
|East Lacombe|with levee|N/A|
|Slidell|with levee|N/A|
|Other External areas|N/A|N/A|


Comments on the specific planning subunits are given in Table 4.4. Additional area specific information is given in Annex B.



---PAGE-165---



###### Table 4.4 - Specific planning subunit comments

|Planning Subunit|Comment|
|---|---|
|Laplace|This is considered as initially without a levee system and therefore exterior. Several of the options (both without and with the Lake Pontchartrain barrier) consider the construction of a levee and so the effect on stage frequency has been calculated with a range of different design standards of a levee protecting Laplace.|
|St Charles - east bank|The two planning subunits within St Charles Parish on the east bank are within an existing levee system and have been considered as interconnected above a flood level of 4.5’.|
|East Jefferson New Orleans Metro New Orleans East St Bernard Wetland St Bernard Developed|The central area of New Orleans has been considered as an interconnected system. The following assumptions have been made in developing the stage frequency results in this area. St Bernard wetland and St Bernard Developed are inter-linked at 10.5’. For flood levels greater than 12.5’ water flows from St Bernard into New Orleans Metro. Similarly if flooding in New Orleans East exceeds 12.5’ then water flows into New Orleans Metro. Water flows between New Orleans Metro and East Jefferson at flood levels greater than 5’. A maximum level of 16’ has generally been used within the central New Orleans area. In addition, the effects of creating a levee along the edge of Lake Borgne (the Golden Triangle alignment) were considered by increasing the storage in St Bernard wetland and reducing the overtopping lengths to New Orleans East. Also the design height of this levee, together with overtopping rates, was evaluated. The evaluation of this option resulted in the ‘b’ alternatives in the matrix above.|
|Golden triangle|There are a number of areas that have an interior stage frequency when the Golden Triangle alignment is implemented. These areas have the same stage frequency as St Bernard Wetland and are presented in the ‘b’ alternatives.|
|Plaquemines Scarsdale|There are a number of areas within the existing low levee system south of St Bernard Parish that have been included using exterior stage frequency values for the baseline case, and have then been analyzed with improved levee systems at a range of design standards to provide interior stage frequency results.|
|Slidell|This area covers the Slidell part of the North Shore. Some parts of the existing levee system have been modeled and the results from the hydrodynamic modeling have been used and the impacts have been considered for low frequency events. The ‘a’ alternatives consider the creation of a new levee around the areas which then links up with a further levee to the west (see below).|
|Madisonville, Madisonville to Mandeville, Mandeville, South Covington, West and East Lacombe|These areas cover the North Shore to the west of Slidell and use the exterior stage frequency results from the hydrodynamic modeling for the current no levee situation. Interior stage frequencies have been developed as ‘a’ alternatives using both the BS and EB grids and with a range of design standards.|




---PAGE-166---



###### 4.4 Interconnected drainage areas

Two groups of planning subunits have been considered as interconnected during severe flood events. Details on how these areas have been linked are given below.

- 4.4.1 St Charles


The planning subunits St Charles Norco and St Charles-rest are considered as connected, with the link being at 4.5 feet. If both areas have a stage of less than 4.5 feet, then the stages are used from the system. If one is greater than 4.5 feet, then the excess flood volume is added to the other and a new stage is computed. If both stages then reach a level higher than 4.5 feet, the total volume is used with the total stage storage to give a single value of stage. This value is then limited to the higher of the authorized height (13 feet), the design height (32) or the surge (32).

- 4.4.2 New Orleans


There are five areas that are considered to be linked within the New Orleans area. These are two in St Bernard, New Orleans East, New Orleans Metro, and East Jefferson. A flow chart of this linkage is shown in Figure 4.8.



---PAGE-167---



- Figure 4.8 – Flow chart showing linkages between New Orleans drainage areas


The key points for this system are that there is no connection between New Orleans East and St Bernard until the New Orleans Metro/East Jefferson areas have filled to 12.5 feet as well.

###### 4.5 Hydraulic results to planning alternatives

At the initial planning stage, a large number of planning alternatives have been considered. These cover the two basic alternatives:

- • High Level plan: raising and extending the existing levee system;
- • Barrier plan: construction of a barrier of some sort across the entrance to Lake Pontchartrain together with levee improvements.




---PAGE-168---



In addition, three design standards have been considered (100-year, 400-year, and 1000-year) as well as a range of variations in alignments and areas. All of these alternatives are used for the determination of the interior and exterior stage frequencies, thus providing results that are the input for the economic evaluation. Following the screening process carried out by the LACPR planning team, eight alternatives and the baseline situation have been considered in more detail.

The relationship between the planning subunits, selected alternatives, and hydraulic codes (as discussed in section 4.2) is given in Table 4.5.

- Table 4.5 - Planning subunit to alternative matrix


|Planning Subunit|2010_base|HL-a-100-3|HL-b-400-3|LP-a-100-1|LP-a-100-3|LP-b-400-1|LP-b-400-3|LP-b-1000-1|LP-b-1000-2|
|---|---|---|---|---|---|---|---|---|---|
|Laplace|BS-ext|BS-0100a|BS-0400a|EB-ext|EB-0100a|EB-ext|EB-0400a|EB-ext|EB-1000a|
|St Charles Norco|BS-0100a|BS-0100a|BS-0400a|EB-0100a|EB-0100a|EB-0400a|EB-0400a|EB-1000a|EB-1000a|
|St Charles – rest|BS-0100a|BS-0100a|BS-0400a|EB-0100a|EB-0100a|EB-0400a|EB-0400a|EB-1000a|EB-1000a|
|East Jefferson|BS-0100a|BS-0100a|BS-0400b|EB-0100a|EB-0100a|EB-0400b|EB-0400b|EB-1000b|EB-1000b|
|New Orleans Metro|BS-0100a|BS-0100a|BS-0400b|EB-0100a|EB-0100a|EB-0400b|EB-0400b|EB-1000b|EB-1000b|
|New Orleans East|BS-0100a|BS-0100a|BS-0400b|EB-0100a|EB-0100a|EB-0400b|EB-0400b|EB-1000b|EB-1000b|
|St Bernard Wetland|BS-0100a|BS-0100a|BS-0400b|EB-0100a|EB-0100a|EB-0400b|EB-0400b|EB-1000b|EB-1000b|
|St Bernard developed|BS-0100a|BS-0100a|BS-0400b|EB-0100a|EB-0100a|EB-0400b|EB-0400b|EB-1000b|EB-1000b|
|Plaquemines - Scarsdale|BS-ext|BS-0100a|BS-0400a|EB-ext|EB-0100a|EB-ext|EB-0400a|EB-ext|EB-1000a|
|Golden Triangle|BS-ext|BS-ext|BS-0400b|EB-ext|EB-ext|EB-0400b|EB-0400b|EB-1000b|EB-1000b|
|Madisonville|BS-ext|BS-0100a|BS-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-1000a|
|Madisonville to Mandeville|BS-ext|BS-0100b|BS-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-1000a|
|South Covington|BS-ext|BS-0100a|BS-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-1000a|
|Mandeville|BS-ext|BS-0100a|BS-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-1000a|
|Madisonville|BS-ext|BS-0100a|BS-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-1000a|
|West Lacombe|BS-ext|BS-0100a|BS-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-1000a|
|East Lacombe|BS-ext|BS-0100a|BS-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-1000a|
|Slidell|BS-ext|BS-0100a|BS-400a|EB-ext|EB-0100a|EB-ext|EB-0400a|EB-ext|EB-1000a|
|Other External areas|BS-ext|BS-ext|BS-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-ext|EB-ext|


The alignments and levee heights for each of the alternatives are shown on the summary maps in the Evaluation Results Appendix. These maps all go along with an accompanying table showing stage frequency comparisons (baseline to alternative) for a selection of planning subunits.



---PAGE-169---



###### 4.6 Plaquemines

This section of the report is primarily focused on the determination of interior stages for the existing/authorized Plaquemines levees. The existing levees from Oakville to Venice (the Plaquemines area) were originally not included in the levee improvements. However since the potential alternatives may affect the standard of risk reduction afforded to this area, the heights of the levees and stage frequencies needed to be established.

An overview of the levees and storage areas is shown in Figure 4.9 below. The existing levee heights (authorized as well as non-federal) as shown in the map and in Table 4.6 were obtained from the USACE design memorandum for each of the reach of the Mississippi River and Tributaries Project and/or the New Orleans to Venice Hurricane Protection Project.

- Figure 4.9 - Plaquemines storage areas and existing levee heights




---PAGE-170---



###### Table 4.6 - Authorized levee heights

|Location|Height in feet|Notes|
|---|---|---|
|Belair|11.5|Non-federal|
|Ollie|8|Non-federal|
|Myrtle Grove|5|Non-federal|
|Bellevue|17|Authorized - Reach C|
|Point ala Hache|17|Authorized - Reach C|
|Diamond - upper|12.8|Authorized - Reach A|
|Diamond - lower|13|Authorized - Reach A|
|Diamond - Mississippi|17|Authorized|
|Gainard Woods - west|13.5 – 14.5|Authorized - Reach A|
|Gainard Woods - Mississippi|17|Authorized|
|Sunrise - west|15|Authorized - Reach B1|
|Sunrise - Mississippi|17|Authorized|
|Grand Liard - west|15|Authorized - Reach B1 and B2|
|Grand Liard - Mississippi|17 – 16|Authorized|


To obtain overtopping rates the levees were linked to model output points. The 2010 base model was used, here.

For each storage area the stage storage values have been obtained from the previous modeling of the area. Rainfall was taken as the standard 6.5 inch in 6 hours, as used for the main internal storage areas.

Using the overtopping rates calculated for the points together with the rainfall, flood volumes for the 10-year, 50-year, and 100-year flood events have been calculated. These have then been converted to flood levels using the stage storage volumes. The range of events considered (10, 50 and 100) is different from the normal set (10,100,400,1000,2000) as it was considered that over the 100-year event the storage areas would be totally overwhelmed, but that having the 50-year value may enable some conclusions to be drawn as to the vulnerability of the area.

For the 100-year event the majority of the areas were flooded to significant depths. The stage values (for the 50% confidence level) are listed in Table 4.7 below:

###### Table 4.7 - Stage values in feet for Plaquemines storage areas - based on 50% confidence level results

|Area|10-year event (ft)|50-year event (ft)|100-year event (ft)|
|---|---|---|---|
|Bellevue|1.0|1.9|Full to levee|
|Pointe ala Hache|1.6|2.6|Full to levee|
|Diamond|0.1|0.1|Full to levee|
|Gainard Woods|-1.1|-1.1|9.4|
|Sunrise|-2.3|-1.9|9.7|
|Grand Liard|-4.7|-4.6|1.9|
|Ollie|1.4|1.4|Full to levee|




---PAGE-171---



The values for 400-, 1000-, and 2000-year events have been taken from the adjacent exterior stage frequency curves as it was assumed that the levees have only a minor effect on flood levels at these frequencies. For the ‘with barrier’ option changes in exterior stage frequency were applied for the higher return period events using the east model B results.

To take into account the impacts of implementing the barrier across Lake Pontchartrain and the Barataria Basin, the increase in surge levels along the Plaquemines was investigated.

The differences in surge heights along the levees was obtained for the without and with barrier options across Lake Pontchartrain and along the GIWW in the Barataria Basin (in Planning Unit 2) by comparing the surge levels from the High Level Plan and east model B results. The differences in surge level were taken as the changes required to increase the levee height to maintain the same standard of risk reduction.

The analysis suggested the following changes to levee heights:

- - Ollie - increase levee heights by 2.6 feet to accommodate the maximum change in surge seen at 100-year;
- - Bellevue - increase levee heights by 0.6 feet to accommodate the increase in surge level;
- - Pointe a la Hache - increase levee heights by 0.3 feet to accommodate the increase in surge level;
- - Diamond - Mississippi Levee - increase levee heights by 0.3 feet to accommodate the increase in surge level;
- - Gainard Woods - Mississippi Levee - increase levee heights by 0.2 feet to accommodate the increase in surge level;
- - Belair - at Belair the increase is around 2 feet, but the non-federal levee is overtopped at less than once in 50 years (1.8 feet still water over levee at 1 in 50 year event). Because of this low defense standard, no allowance was made for increases in this levee.
- - Myrtle Grove - no allowances have been investigated for Myrtle Grove as the levee height has been taken as around 5 feet and assumed to be overtopped regularly.


No changes were made to the interior stage frequency values for storage areas in Plaquemines for future conditions as the changes were deemed to affect only a relatively small area and would only have a minor impact on the final results of the overall evaluation of alternatives developed for the planning unit. Since the storage areas behind the existing levees are already mostly totally overwhelmed for the 2010 Base condition, it was viewed that calculating new stage frequency values for future H&H conditions would result in little change under future conditions since the only change would be to the interior stages in the storage areas that were not overwhelmed under the 2010 Base conditions (a relatively small area). Developing new interior stage frequency values for these remaining areas would have been a very tedious effort for only minor impacts on the final



---PAGE-172---



results. Therefore no changes were made. For exterior stage frequencies, which were also used in damage calculations for the areas in the Plaquemines where the interior storage areas were previously determined to be overwhelmed for the 2010 base conditions, the relative sea level rise values were added to the 2010 base stages for future conditions.

###### 5 PLANNING UNIT 2 5.1 Introduction

Following the same structure as the previous chapter on Planning Unit 1, this chapter presents the levee heights and the stage frequency curves resulting from the calculations for the planning subunits of Planning Unit 2 (see Figure 5.1).

- Section 5.2 describes the results of the levee heights being computed for both the 2010 base model grid and the east hydro model grid B, for three design standards (100-year, 400-year, and 1000-year), over all levees included in the modeling.


- In section 5.3 the stage frequency curves for Planning Unit 2 are determined.


- Figure 5.1 – Planning subunits in Planning Unit 2




---PAGE-173---



###### 5.2 Levee heights

The levee height design was carried out using the methodologies described in Volume I of this report. Levee heights were computed for both the 2010 base model grid and the east model B, for three separate design standards (100-year, 400-year, and 1000-year) for all levees included within the modeling.

Figures 5.2 through 5.7 show the 100-year, 400-year, and 1000-year design heights in feet for the levees within Planning Unit 2 for the 2010 base grid and the east hydro model B grid. These values have been adjusted to include any changes made for authorized heights or because of issues with specific modeling results. A detailed overview of the design heights is given in the fact sheets in Annex B.

The heights are again used for the purposes of costing design options and for establishing overtopping rates.



---PAGE-174---



###### Figure 5.2 - 2010 base model grid, 100-year design heights in Planning Unit 2



---PAGE-175---



###### Figure 5.3 - 2010 base model grid, 400-year design heights in Planning Unit 2



---PAGE-176---



###### Figure 5.4 - 2010 base model grid, 1000-year design heights in Planning Unit 2



---PAGE-177---



###### Figure 5.5 - East B model grid, 100-year design heights in Planning Unit 2



---PAGE-178---



###### Figure 5.6 - East B model grid, 400-year design heights in Planning Unit 2



---PAGE-179---



###### Figure 5.7 - East B model grid, 1000-year design heights in Planning Unit 2



---PAGE-180---



###### 5.3 Interior and exterior frequency curves

Given the above described levee heights, the overtopping volumes were computed for four return periods of the outside surge level and wave characteristics (100-year, 400-year, 1000-year, and 2000-year). The overtopping volumes are an important input for determination of the interior stage frequency curves per planning subunit.

Planning Unit 2 consists of over 100 planning subunits. Of these, 9 are protected by levees and it is proposed that they continue to be protected in the future, and 21 fall in the category of currently being outside the levee system, but may fall within a levee in one of the future alternatives (semiinterior). A list of these is given in Table 5.1.

- Table 5.1 - Interior and semi-interior planning subunits


|Name|Type|
|---|---|
|Algiers|Interior|
|English Turn|Interior|
|West Jefferson - East of Harvey|Interior|
|West Jefferson - Harvey Estelle|Interior|
|West Jefferson - Ames|Interior|
|West Jefferson - Segnette|Interior|
|St Charles - Davis Pond|Interior|
|St Charles - Luling Boutte|Semi-interior - new levee|
|STCH_3c|Semi-interior (Luling) - new levee|
|STCH_5a|Semi-interior (Luling) - new levee|
|STCH_6a|Semi-interior (Luling) - new levee|
|St Charles - Sunset|Semi-interior - non federal levee|
|STCH_1c|Semi-interior (Sunset) - non federal levee|
|STCH_1d|Semi-interior (Sunset) - non federal levee|
|STCH_2c|Semi-interior (Sunset) - non federal levee|
|Larose to Golden Meadow|Interior|
|Plaquemines - Belle Chase|Interior|
|LAFO_2c|Semi-interior (Lockport) - new levee|
|LAFO_3b|Semi-interior (Lockport) - new levee|
|LAFO_3c|Semi-interior (Lockport) - new levee|
|LAFO_4c|Semi-interior (Lockport) - new levee|
|LAFO_5d|Semi-interior (Lockport) - new levee|
|LAFO_6b|Semi-interior (Lockport) - new levee|
|LAFO_6c|Semi-interior (Lockport) - new levee|
|LAFO_7e|Semi-interior (Lockport) - new levee|
|LAFO_8e|Semi-interior (Lockport) - new levee|
|LAFO_9a|Semi-interior (Lockport) - new levee|


The stage storage relationships for these planning subunits are based on the results from two of the hydraulic modeling grids: the 2010 East base model (BS) and the East hydro model grid B (EB). Refer to Annex B for more details on individual sub-basins.



---PAGE-181---



###### 6 PLANNING UNIT 3A 6.1 Introduction

This chapter presents the results of the calculations of the levee heights and stage frequency

- curves for Planning Unit 3a. It addresses the development of the 100-year, 400-year, and 1000year design heights in feet for the potential levee alignments within Planning Unit 3a for the 2007 base West, West A and the West B model grids.


- In section 6.2 computation of the levee heights is described for the different alternatives in Planning Unit 3a in 2007.


As for the other planning units, the resulting heights are used for the purposes of costing design options and for establishing overtopping rates. The combination of the heights to given planning alternatives is coupled with the stage frequency analysis as is described in section 6.3.

- Figure 6.1 shows the planning subunits in Planning Unit 3a.


| |
|---|


- Figure 6.1 - Planning subunits in Planning Unit 3a




---PAGE-182---



###### 6.2 Levee height

- 6.2.1 General


The levee height design has been carried out using the methodologies described in Volume I of this appendix. Levee heights have been computed for the West A (WA) and the West B (WB) model grids, for three separate design standards (100-year, 400-year, and 1000-year) for all levees included in the alternatives. The design elevations are based on the wave heights and periods obtained from the no bed friction STWAVE models for the west.

Figures 6.2 through 6.9 show the levees designed for Planning Unit 3a using the WA and WB model grids for the 100-year, 400-year, and 1000-year levels of risk reduction. As the WB grid was only used only for the area of Morgan City, only the results for that area are shown with the WB grid.

The levee heights north of Morgan City run along the edge of the Atchafalaya Basin. This is an area where the effects of the extreme conditions are lesser than on the southern side of Morgan City, as the surge has to propogate through the narrowing’s around Patterson (to the west of Morgan City). As the levels within the basin, and more significantly the wave heights, are not well modeled, particularly in the hydrodynamic models with high levees, the levee heights within the basin have been derived by using the levee heights outside the basin but reducing their height by the apparent reduction in surge level obtained from the 2007 base grid, for which base values were available within the model results. A detailed overview of the design heights is also given in the fact sheets in Annex B.

- Figure 6.2 - West A model grid, 100-year design heights in Planning Unit 3a




---PAGE-183---



###### Figure 6.3 - West A model grid, 400-year design heights in Planning Unit 3a

###### Figure 6.4 - West A model grid, 1000-year design heights in Planning Unit 3a



---PAGE-184---



###### Figure 6.5 - West B model grid, 100-year design heights - Morgan City

###### Figure 6.6 - West B model grid, 400-year design heights - Morgan City



---PAGE-185---



- Figure 6.7 - West B model grid, 1000-year design heights - Morgan City


- 6.2.2 Ring levee alignment with secondary defense


This alternative in Planning Unit 3a protects the main Morganza area with a levee based on the 100-year design, while the higher grounds more inland of Morganza are protected by a secondary levee (only 400- and 1000-year design), thus providing it a 400- or 1000-year level of risk reduction. The 100-year design height of the levee at the perimeter of Morganza uses the same design heights derived from the WA grid for the 100-year design. The levee design height of the back levee is based on the interior stages in the Morganza area instead of the surge elevation of the 400- and 100-year conditions in front of this levee. The stage values were obtained by considering the overtopping of the outer levee line for the 400- and 1000-year events to provide a starting water level within the inner area.

Given the 100-year design height at the outer rim of Morganza in combination with a storm event with a return period of 400 years, an interior stage of 6.6 feet results for the Morganza polder (90% confidence level). To determine the wave height and period, first the return period of a 6.6 feet stage is derived for a point in the data set that is close to the levee alignment. The wave height and period have then been set, matching with the found figures. This results in a new set of input parameters based on which the levee height is calculated. For the 1000-year design height a similar procedure has been followed (see Table 6.1).



---PAGE-186---



- Table 6.1 - Input parameters used for design height of the Morganza back levee (stages taken from interior frequency curves)


|Design standard|Stage (ft) (90%)|Significant wave height (ft)|Peak wave period (s)|Levee Height (ft)|
|---|---|---|---|---|
|400-year|6.6|2|4.51|9.5|
|1000-year|15|4.1|7.48|24|


- Figure 6.8 - Ring levee alignment with secondary defense, 400-year design heights in Planning Unit 3a




---PAGE-187---



- Figure 6.9 - Ring levee alignment with secondary defense, 1000-year design heights in Planning Unit 3a


###### 6.3 Interior and exterior frequency curves

Over 200 planning subunits are defined in Planning Unit 3a. These fall into 2 groups, those which are always outside of the levees and those which fall inside the levees in one of the proposed alignments.

The planning subunits are grouped together to form areas considered for interior drainage. This grouping is based on the level of risk reduction being provided to the area by a particular levee alignment. Thus, the planning subunits are grouped into six internal drainage areas. These are listed in Table 6.2 below.

- Table 6.2 - Internal drainage areas


|Name|Used in|Model|
|---|---|---|
|Morgan_City|Ring alternatives|WB|
|Morganza_with_ret_ring|Ring alternatives|WA|
|East_of_Morgan_City_ring|Morganza alternative|WA|
|Morganza_no_ret_ring|Morganza alternative|WA|
|Morganza_with_ret_ring_m_only|Ring Alternative (100-year levee)|WA|
|Morganza_back_levee|Ring Alternative (100-year levee)|Hand calculation|




---PAGE-188---



Given the levee height as described above in section 6.2, the overtopping volumes were calculated for four return periods of the outside surge level and wave characteristics (100-year, 400-year, 1000-year, and 2000-year).

- The grids that are used for each of the drainage areas are listed in Table 6.3 below, followed by a description of the specific variations. The hydraulic codes at the top line of the table relate to the various layout alternatives and corresponding sources of information; as listed in Chapter 3.


- Table 6.3 - Interior drainage area to hydraulic alternative matrix

|Interior Drainage Area|WT_ext|WA-ext|WA-0100a|WA-0400a|WA-1000a|WA-0100b|WA-0400b|WA-1000b|WA-0100c|WA-0400c|WA-1000c|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Morgan_City|x| | | | |x|x|x| | | |
|Morganza_with_ret_ring|x| | | | |x|x|x| | | |
|East_of_Morgan_City_ring|x|x|x|x|x| | | | | | |
|Morganza_no_ret_ring|x| |x|x|x| | | | | | |
|Morganza_with_ret_ring_m_only|x| | | | | | | |x|x|x|
|Morganza_back_levee|x| | | | | | | |x|x|x|
|Other External Areas|x|x| | | | | | | | | |


WT_ext

WA-ext

WA-0100a

WA-0400a

WA-1000a

WA-0100b

WA-0400b

WA-1000b

WA-0100c

WA-0400c

WA-1000c

Note - as there are no levees in the Base model, all interior drainage areas also have a WT-ext value.

Whereas in Planning Units 1 and 2 the interior drainage areas are separate (i.e. they don’t

- overlap) in Planning Unit 3a the interior drainage areas may nest or intersect, depending on the respective planning alternatives.


Specific comments with respect to the internal drainage areas in Planning Unit 3a are given in

- Table 6.4. Additional area specific information is given in Annex B.


- Table 6.4 - Specific planning unit comments


|Polder Ring|Polder(s)|Comment|
|---|---|---|
|Morganza_with_ret_ring_m_only|Morganza|For the alternative “Ring levee alignment with secondary defense,” stages in Morganza are only analyzed given the 100-year design and the 100-, 400-, 1000- and 2000-year return periods.|
|Morganza_back_levee|North_of_Houma Houma West_of_Houma|For the alternative “Ring levee alignment with secondary defense,” stages behind the secondary defense are calculated based upon overtopping from the flooded polder Morganza. An exception is made for the 2000-year event where stages are equal to the base surge conditions.|




---PAGE-189---



###### 6.4 Hydraulic results of planning alternatives

A number of planning alternatives have been considered. They cover a range of design standards (100-year, 400-year, and 1000-year) together with a range of variations in alignment. All of these alternatives are used for the determination of interior and exterior stage frequencies, thus providing results that are used as the input for the economic evaluation. For the West, all the alternatives and the baseline have been considered in more detail.

The key alternatives are as follows:

- - Morganza plan
- - Morganza/ring levee plan
- - GIWW/Morganza/Ring levee plan


These three basic alternatives use levee height designs and interior drainage results from different model runs, and different internal drainage areas (because of the nesting/intersecting of drainage areas). Table 6.5 shows the linkage between the six interior drainage areas and the planning alternatives. The codes are explained in Chapter 3.

- Table 6.5 - Internal drainage area to alternative sets


| | |Planning Alternative Set| | | |
|---|---|---|---|---|---|
| | |Baseline|Morganza plan|Morganza/ring levee plan|GIWW/Morganza/Ring levee plan|
|InternalDrainageArea|Morgan_City| | |WA-xxxxb|WA-xxxxb|
| |Morganza_with_ret_ring| | |WA-xxxxb| |
| |East_of_Morgan_City_ring| |WA-xxxxa| | |
| |Morganza_no_ret_ring| |WA-xxxxa| | |
| |Morganza_with_ret_ring_m_only| | | |WA-0100c|
| |Morganza_back_levee| | | |WA-xxxxc|
| |Other External Areas|WT-ext|WA-ext|WA-ext|WA-ext|


The alignments and levee heights for each of the alternatives are shown on the summary maps in the Evaluation Results Appendix. These maps all go along with an accompanying table showing stage frequency comparisons (baseline to alternative) for a selection of planning subunits.



---PAGE-190---



###### 7 PLANNING UNIT 3B 7.1 Introduction

This chapter presents the details of the calculations of the levee heights and stage frequency

- curves for Planning Unit 3b.


- Section 7.2 addresses the development of the 100-year, 400-year, and 1000-year design heights in feet for the potential levee alignments in Planning Unit 3b for the 2007 base West, West A, and the West B model grids.


The heights computed during the process are used for costing design options and for establishing overtopping rates. The combination of the heights to given planning alternatives is coupled with the stage frequency analysis as described in section 7.3. Figure 7.1 shows the planning subunits in Planning Unit 3b.

| |
|---|


- Figure 7.1 - Planning subunits in Planning Unit 3b




---PAGE-191---



###### 7.2 Levee height

The levee height design has been carried out using the methodologies described in Volume I of this report.

Levee heights have been computed using three models, for three separate design standards (100year, 400-year, and 1000-year) for all levees included within the alternatives. The design elevations are based on the wave heights and periods obtained from the no bed friction STWAVE models for the west.

The 2007 base West (WT) model grid (containing no levees) has been used for designing a series of localized ring levees. The West A (WA) model grid has been used to design levee heights along the GIWW alignment, while the West B (WB) model grid has been used to design levee heights along a defense line between the GIWW and the higher ground, extending from Franklin to Abbeville.

The results of levee height designs from these three models for the 100-, 400-, and 1000-year levels of risk reduction are given in the figures below (Figure 7.2 – 7.10). A detailed overview of the design heights is given in the fact sheets in Annex B.

- Figure 7.2 - West A model grid, 100-year design heights in Planning Unit 3b




---PAGE-192---



###### Figure 7.3 - West A model grid, 400-year design heights in Planning Unit 3b

###### Figure 7.4 - West A model grid, 1000-year design heights in Planning Unit 3b



---PAGE-193---



###### Figure 7.5 - West B model grid, 100-year design heights in Planning Unit 3b

###### Figure 7.6 - West B model grid, 400-year design heights in Planning Unit 3b



---PAGE-194---



###### Figure 7.7 - West B model grid, 1000-year design heights in Planning Unit 3b

###### Figure 7.8 - 2007 base model grid, 100-year design heights in Planning Unit 3b



---PAGE-195---



###### Figure 7.9 - 2007 base model grid, 400-year design heights in Planning Unit 3b

###### Figure 7.10 - 2007 base model grid, 1000-year design heights in Planning Unit 3b



---PAGE-196---



###### 7.3 Interior and exterior frequency curves

Over 200 planning subunits are identified in Planning Unit 3b. These fall into two categories: those being always outside of the levees, and those falling inside the levees in one of the proposed alignments.

The planning subunits have been grouped together to form areas considered for interior drainage. This grouping was based on the risk reduction being provided to the area by a particular levee alignment. A list of the drainage areas is given in Table 7.1.

- Table 7.1 - Drainage areas - relationship to alternative sets and hydrodynamic models


|Name|Used in|Model|
|---|---|---|
|Abbeville|Ring levee alignment|WT|
|Abbeville_to_Delcambre_ring|Franklin to Abbeville Alignment|WB|
|Baldwin|Ring levee alignment|WB|
|Charenton_ring|Franklin to Abbeville Alignment|WB|
|Delcambre|Ring levee alignment|WT|
|Erath|Ring levee alignment|WT|
|Franklin|Ring levee alignment|WB|
|New_Iberia|Ring levee alignment|WT|
|New_Iberia_ring|Franklin to Abbeville Alignment|WT|
|Patterson|GIWW alternative|WA|
|South_of_Franklin_ring|GIWW alternative|WA|
|GIWW_PU3b_ring|GIWW alternative|WA|


Given the levee height described above in section 7.2, the overtopping volumes have been computed for four return periods of the outside surge level and wave characteristics (100-year, 400-year, 1000-year, and 2000-year). The overtopping volumes are used as input to establish the interior stage frequency curve for the planning subunits.

- The grids that are used for each of the drainage areas are listed in Table 7.2 below, followed by a description of the specific variations. In those cases where several planning subunits are located within a single interior drainage area, the name of the drainage area is given. The hydraulic codes at the top line of the table relate to the various layout alternatives and corresponding sources of information; as listed in Chapter 3.




---PAGE-197---



###### Table 7.2 - Interior drainage area to hydraulic alternative matrix

|Interior Drainage Area|WT_ext|WA-ext|WT-0100|WT-0400|WT-01000|WB-0100|WB-0400|WB-1000|WA-0100|WA-0400|WA-1000|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Abbeville|x| |x|x|x| | | | | | |
|Abbeville_to_Delcambre_ring|x| | | | |x|x|x| | | |
|Baldwin|x| | | | |x|x|x| | | |
|Charenton_ring|x| | | | |x|x|x| | | |
|Delcambre|x| |x|x|x| | | | | | |
|Erath|x| |x|x|x| | | | | | |
|Franklin|x| | | | |x|x|x| | | |
|New_Iberia|x| |x|x|x| | | | | | |
|New_Iberia_ring|x| | | | |x|x|x| | | |
|Patterson|x| | | | | | | |X|x|x|
|South_of_Franklin_ring|x| | | | | | | |X|x|x|
|GIWW_PU3b_ring|x| | | | | | | |X|x|x|
|Other External Areas|x|x| | | | | | | | | |


WT-01000

WB-0100

WB-0400

WB-1000

WA-0100

WA-0400

WA-1000

WT-0100

WT-0400

WT_ext

WA-ext

Note - as there are no levees in the Base model, all interior drainagae areas also have a WT-ext value.

Whereas in Planning Units 1 and 2 the interior drainage areas are separate (i.e. they don’t overlap) in Planning Unit 3b the interior drainage areas may nest or intersect.

- Specific comments with respect to the polders in Planning Unit 3b are given in Table 7.3. Additional area specific information is given in Annex B.


###### Table 7.3 - Specific planning unit comments

|Polder Ring|Polder(s)|Comment|
|---|---|---|
|Patterson|Patterson|For the WA model the back levees at Patterson are 3 feet lower than the levee at the front/sea side. For the WB model the difference is slightly larger (4.5 to 5’), but the levels were adopted at the lower levels for consistency.The overtopping calculations are based upon the assumption that overtopping takes place only from the front/sea side.|
|GIWW alignment|GIWW_PU3b|The discharge of the river Vermillion is not included in the stored volume, pumps have been assumed to be installed to handle this additional volume.|




---PAGE-198---



###### 7.4 Hydraulic results of planning alternatives

A number of planning alternatives have been considered for Planning Unit 3b. They consider a range of design standards (100-year, 400-year, and 1000-year) together with a range of variations in alignment and in the areas included within the protected areas. All of these alternatives are considered for interior stage frequency and results have been developed to be used as input for the economic evaluation. For the West, all the alternatives and the baseline have been considered in more detail.

The key alternatives are as follows:

- - GIWW plan
- - Franklin to Abbeville Alignment plan
- - Ring levee plan


These alternatives use a different combination of levee height designs and interior drainage results. Table 7.4 shows the linkage of the interior drainage areas to the planning alternatives, codes are explained in Chapter 3:

- Table 7.4 - Internal drainage area to alternative sets


| |Baseline|GIWW Plan|Franklin to Abbeville Alignment|Ring levee Plan|
|---|---|---|---|---|
|Abbeville| | | |WT-xxxx|
|Abbeville_to_Delcambre_ring| | |WB-xxxx| |
|Baldwin| | | |WT-xxxx|
|Charenton_ring| | |WB-xxxx| |
|Delcambre| | | |WT-xxxx|
|Erath| | | |WT-xxxx|
|Franklin| | | |WT-xxxx|
|New_Iberia| | | |WT-xxxx|
|New_Iberia_ring| | |WB-xxxx| |
|Patterson| |WA-xxxx|WA-xxxx|WT-xxxx|
|South_of_Franklin_ring| |WA-xxxx| | |
|GIWW_PU3b_ring| |WA-xxxx| | |
|Other External Areas|WT-ext|WA-ext|WB-ext|WT-ext|


The alignments and levee heights for each of the alternatives are shown on the summary maps in the Evaluation Results Appendix. These maps all go along with an accompanying table showing stage frequency comparisons (baseline to alternative) for a selection of planning subunits.



---PAGE-199---



###### 8 PLANNING UNIT 4

###### 8.1 Introduction

This chapter presents the results of the calculations of the levee heights and stage frequency curves for Planning Unit 4.

- Section 8.2 describes the development of the 100-year, 400-year, and 1000-year design heights in feet for the potential levee alignments in Planning Unit 4. These have been developed for the 2007 base West (WT), West A (WA) and the West B (WB) model grids.


The heights computed during the process are used as input for costing design options and for establishing overtopping rates. The combination of the heights to given planning alternatives is coupled with the stage frequency analysis as is described in section 8.3. Figure 8.1 gives the planning subunits of Planning Unit 4. For evaluation purposes the planning subunits are grouped into drainage areas.

| |
|---|


- Figure 8.1 - Planning subunits in Planning Unit 4




---PAGE-200---



###### 8.2 Levee height

8.2.1 General The levee height design has been carried out using the methodologies described in Volume I of this report. Levee heights were computed for the 2007 base West (WT) and West A (WA) model grids, for three separate design standards (100-year, 400-year, and 1000-year) for all levees included in the alternatives. The design elevations are based on the wave heights and periods obtained from the no bed friction STWAVE models for the west.

The 2007 base West (containing no levees) model grid has been used for designing a series of localized ring levees, while the West A model grid has been used to design levee heights along the GIWW alignment.

The results of levee height designs from these two models for the 100-, 400- and 1000-year levels of risk reduction are given in the following figures (Figures 8.2 – 8.9). In addition levees were designed considering a low (12-foot high) levee along the GIWW together with ring levees further inland. Heights for these levees were based on hand calculations using the interior stages based on overtopping of the levees using the West A model.

The Calcasieu River flows through Lake Charles on its way to the sea. Within the town there are a number of lower spots which may be at risk of flooding in extreme hurricane events. The heights of the proposed levees located along the Calcasieu River are based upon the modeled sea water elevations and a 3-foot wave height. A moderate wave of 3 feet is chosen as the levees do not face the sea.

A detailed overview of the design heights is given in the fact sheets in Annex B.



---PAGE-201---



- Figure 8.2 - West A model grid, 100-year design heights in Planning Unit 4
- Figure 8.3 - West A model grid, 400-year design heights in Planning Unit 4




---PAGE-202---



###### Figure 8.4 - West A model grid, 1000-year design heights in Planning Unit 4

###### Figure 8.5 - 2007 base model grid, 100-year design heights in Planning Unit 4



---PAGE-203---



###### Figure 8.6 - 2007 base model grid, 400-year design heights in Planning Unit 4

###### Figure 8.7- 2007 base model grid, 1000-year design heights in Planning Unit 4



---PAGE-204---



- 8.2.2 12 feet GIWW levee alignment with return


The concept of the 12-foot levee alternative was to look at whether a lower level defense relatively close to the sea could improve the level of risk reduction for a large proportion of the population at risk without the need to introduce extreme levees near the populace.

The 12-foot GIWW levee alignment alternative consists of a 12-foot levee along the GIWW. Behind this alignment there are three areas of significant population which may still be at risk of flooding in extreme events. Therefore three levees have been proposed which can provide either a 400-year or 1000-year level of risk reduction to these areas. The areas are Kaplan, Gueydan and East Lake Charles.

Levee height design for the 400- and 1000-year level of risk reduction is based on interior stages behind the 12-foot levee. Original (WT) designs for the ring levees are reduced in height equal to the decrease in water level in front of the levee that occurs as a consequence of the presence of the 12-foot levee. In these cases interior stages are used instead of surge levels, except those cases where the surge level exceeds levee height and stage level.

For the levees bordering the Calcasieu River, a similar approach has been used. Levee design heights are given in the two figures below.

- Figure 8.8 - 12 feet GIWW levee alignment with return, 2007 West A model grid, 400-year design heights in Planning Unit 4




---PAGE-205---



- Figure 8.9 - 12 feet GIWW levee alignment with return, 2007 West A model grid, 1000-year design heights in Planning Unit 4


###### 8.3 Interior and exterior frequency curves

There are over 200 planning subunits defined in Planning Unit 4. These fall into 2 groups, those being always outside of the levees and those falling inside the levees in one of the proposed alignments.

Similar to Planning Unit 3a and 3b, the planning subunits are grouped together to form areas considered for interior drainage. This grouping is based on the risk reduction being afforded to the area from a particular levee alignment.

The planning subunits are grouped into twelve internal drainage areas. These are listed in Table

- 8.1 below, while, details of the areas are given in the Evaluation Results Appendix.




---PAGE-206---



###### Table 8.1 - Drainage areas - relationship to alternative sets and hydrodynamic models

|Name|Used in|Model|
|---|---|---|
|West_Lake_Charles|GIWW levee alignment 12 feet GIWW levee alignment Ring levee alternative|WT|
|East_Lake_Charles|12 feet GIWW levee alignment Ring levee alternative|WT|
|Gueydan|12 feet GIWW levee alignment Ring levee alternative|WT|
|Kaplan|12 feet GIWW levee alignment Ring levee alternative|WT|
|South_of_Lake_Charles_ring|GIWW levee alignment (with return)|WA|
|Central_PU4_ring|GIWW levee alignment (with return)|WA|
|GIWW_to_Veterans_ring|GIWW levee alignment (with return)|WA|
|South_of_Lake_Charles_ring_12|12 feet GIWW levee alignment|WA|
|Central_PU4_ring_large_12|12 feet GIWW levee alignment|WA|
|GIWW_to_Veterans_ring_large_12|12 feet GIWW levee alignment|WA|
|Prien|GIWW levee alignment 12 feet GIWW levee alignment Ring levee alternative|WT|
|Inner_Lake_Charles|GIWW levee alignment 12 feet GIWW levee alignment Ring levee alternative|WT|


Given the levee height (see section 8.2) the overtopping volumes are computed for four return periods of the outside surge level and wave characteristics (100-year, 400-year, 1000-year, and 2000-year).

The grids that are used for each of the drainage areas are listed in Table 8.2 below, followed by a description of the specific variations. In those cases where several planning subunits are located within a single drainage area, the name of the drainage area is given. The hydraulic codes at the top line of the table relate to the various layout alternatives and corresponding sources of information; as listed in Chapter 3.

###### Table 8.2 - Interior drainage area to hydraulic code matrix



---PAGE-207---



|Interior Drainage Area|WT_ext|WA-ext|WT-0100|WT-0400|WT-01000|WA-0100a|WA-0400a|WA-1000a|WA-0100c|WA-0400c|WA-1000c|WA-0100b|WA-0400b|WA-01000b|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|West_Lake_Charles|x| |x|x|x| | | | | | | | | |
|East_Lake_Charles|x| |x|x|x| | | | | | | |x|x|
|Gueydan|x| |x|x|x| | | | | | | |x|x|
|Kaplan|x| |x|x|x| | | | | | | |x|x|
|South_of_Lake_Charles_ring|x|x| | | |x|x|x| | | | | | |
|Central_PU4_ring|x|x| | | |x|x|x| | | | | | |
|GIWW_to_Veterans_ring|x|x| | | |x|x|x| | | | | | |
|GIWW_to_Veterans_inc_ret_ring|x|x| | | | | | |x|x|x| | | |
|GIWW_PU3b_ring (PU4-ext)|x|x| | | |x|x|x| | | | | | |
|South_of_Lake_Charles_ring_12|x| | | | | | | | | | |x| | |
|Central_PU4_ring_large_12|x| | | | | | | | | | |x| | |
|GIWW_to_Veterans_ring_large_12|x| | | | | | | | | | |x| | |
|Prien|x| |x|x|x| | | | | | | | | |
|Inner_Lake_Charles|x| |x|x|x| | | | | | | | | |
|Other External Areas|x|x| | | | | | | | | | | | |


WA-01000b

WA-0100b

WA-0400b

WA-0100a

WA-0400a

WA-1000a

WA-0100c

WA-0400c

WA-1000c

WT-01000

WT-0100

WT-0400

WT_ext

WA-ext

Note - as there are no levees in the Base model, all interior drainage areas also have a WT-ext value.

Whereas in Planning Units 1 and 2 the interior drainage areas are separate (i.e. they don’t overlap) in Planning Unit 3b the interior drainage areas may nest or intersect.

Because of the large areas of potential flooding and that these areas may be reaching the maximum potential length of coastline affected by a single hurricane approaching the GIWW levee, the area behind the GIWW levee has been split into three drainage areas even though they might act together. To evaluate the flooding in these areas they have been modelled as both independent, and as linked. When linked, the overtopping has been considered as coming from just one of the three sections (representing an extreme hurricane), but the volume has been distributed between all three areas.

For the GIWW as a primary defence, where it was required to ensure that the potential highest residual flood levels were recorded, the drainage areas are considered as acting independently, while when the levee was set at 12’ and a more conservative approach could be considered, the areas were considered interlinked. These alternatives are described as the “large” internal drainage areas.

- Specific comments with respect to the polders in Planning Unit 4 are given in Table 8.3. Additional area specific information is given in Annex B.


- Table 8.3 - Specific planning unit comments


|Polder Ring|Drainage area(s)|Comment|
|---|---|---|




---PAGE-208---



|Polder Ring|Drainage area(s)|Comment|
|---|---|---|
|GIWW alignment|North of Veterans|The discharge of the river Mermentau is not included in the stored volume, pumps will handle this additional volume.|
|12 feet GIWW alignment|North of Veterans and Central PU4 ring|For the 12 feet alignment the stages within the polders are calculated based upon large Polder Rings.|
|12 feet GIWW alignment|South of Lake Charles|The stages for South of Lake Charles are based on overtopping of the levee protecting the Polder South of Lake Charles or based on flooding spreading form the Central PU4 polder. Due to higher grounds between Central PU4 and the South of Lake Charles polder (higher ridge at 8 feet) stages are set to a minimum of 8 feet when overtopping occurs from the South of Lake Charles side. Otherwise, stages within South of Lake Charles follow the stages caused by the flooding of Central PU4 if these stages exceed the threshold of 8 feet.|


###### 8.4 Hydraulic results of planning alternatives

A number of planning alternatives have been considered. They considered a range of design standards (100-year, 400-year, and 1000-year) together with a range of variations in alignment and in the areas included within the protected areas. All of these alternatives are considered for interior stage frequency and results developed for inclusion in the economic evaluation. For the West all the alternatives, plus the baseline were taken forward for more detailed consideration.

The key alternatives are as follows:

- - GIWW plan;
- - 12 feet GIWW plan;
- - Ring levee plan.


These alternatives use different combinations of levee height designs and interior drainage results to produce sets of stage frequency results. Table 8.4 shows the linkage of the interior drainage areas to the planning alternatives:



---PAGE-209---



- Table 8.4 - Internal drainage area to alternative sets matrix


| |Alternative Sets| | | |
|---|---|---|---|---|
|Internal Drainage Area|Baseline|GIWW Plan|12’ GIWW Plan|Ring levee Plan|
|West_Lake_Charles| |WA-xxxxa| |WT-xxxx|
|East_Lake_Charles| | |WA-xxxxb|WT-xxxx|
|Gueydan| | |WA-xxxxb|WT-xxxx|
|Kaplan| | |WA-xxxxb|WT-xxxx|
|South_of_Lake_Charles_ring| |WA-xxxxa| | |
|Central_PU4_ring| |WA-xxxxa| | |
|GIWW_to_Veterans_ring| |WA-xxxxa| | |
|GIWW_to_Veterans_inc_ret_ring| | | | |
|South_of_Lake_Charles_ring_12| | |WA-0100b| |
|Central_PU4_ring_large_12| | |WA-0100b| |
|GIWW_to_Veterans_ring_large_12| | |WA-0100b| |
|Prien| |WA-xxxxa| |WT-xxxx|
|Inner_Lake_Charles| |WA-xxxxa| |WT-xxxx|
|Other External Areas|WT-ext| | | |


###### The alignments and levee heights for each of the alternatives are shown on the summary maps in the Evaluation Results Appendix. These maps all go along with an accompanying table showing stage frequency comparisons (baseline to alternative) for a selection of planning subunits.



---PAGE-210---



###### 9 CONCLUSIONS AND RECOMMENDATIONS

###### 9.1 Summary

The hydraulic analysis for each LACPR alternative consisted of the following consecutive steps:

- 1. numerical computations of surge levels and wave characteristics using ADCIRC, WAM, and STWAVE;
- 2. frequency analysis using the JPM-OS method and determination of exterior stage frequency;
- 3. determination of the levee heights and overtopping volumes;
- 4. determination of the interior stages including rainfall.


To provide a range of alternatives for evaluation and to enable the economic evaluation, each levee alignment alternative was evaluated for different risk reduction levels and event frequencies. A levee design has been made for three levels of risk reduction (100-year, 400-year, 1000-year). Given the level of risk reduction, the overtopping volumes have been computed for four return periods of the outside surge level and wave characteristics (100-year, 400-year, 1000-year, and 2000-year). For all alternatives, the 10-year rainfall was added to the overtopping volume to establish the interior stage frequency curve, while also pumping has been taken into account.

The ADCIRC model results and the “without friction” STWAVE results in combination with the JPM-OS method have been used for determination of levee design and overtopping quantities. This dataset has also been used for the calculation of interior and exterior stages. The method was adopted as being a robust approach for the purpose of comparison for the selection of the levee alignment plans presented in this report.

###### 9.2 Discussion of assumptions and simplifications

From the onset of LACPR the scale of the work, both in terms of geographic area and the range of alternatives to be considered, has dictated the selection of methods and procedures used to determine results. The main assumptions and simplifications are described below.

Hydraulic Modeling and Frequency Analysis

- • Model alignments - what has been modeled does not necessarily represent the final alternatives; this would have required an iterative process to review the results and then modify the models to optimize the levee layouts.
- • Range of storms - for some models the suite of storms has been reduced so that the models could be completed within a practical time frame. The selection of the storms may have skewed the statistical results for the higher extremes.
- • Result presentation - only for selected points results have been prepared for all models rather than for all model points, which would have enabled a more accurate view of the spatial variation in variables and the identification of problem areas within the model grids.
- • Wave computations with and without friction - at present all calculations have been made using wave heights derived from a without-friction model. The with-friction models have been




---PAGE-211---



developed, but the results have not been used in the analysis to date. Validation of the wave models is also required.

Levee Design

- • Use of a single point to define a long length of levee - some of the variations in surge elevation and wave height have not been considered as the levee height design has been based on a single result point - in some cases extending some tens of miles.
- • Fixed design criteria - the design process has only considered earthen embankments, and all levees have been designed to the same design criteria. No consideration has been made to other forms of construction, to the area at risk, or to the consequences of failure.


Stage Frequency Calculations

- • Simple stage storage approach - no allowance has been made in the stage frequency analysis for the flow of water within areas and the time taken for areas to fill and empty.
- • Large storage areas - the size of the storage areas has generally been large and the areas have been considered to act primarily in isolation. Only in critical areas interconnection has been considered and then only in a very simple “overflowing bucket” process.
- • No breaching of defenses - the levees have been assumed to withstand all ranges of overtopping without breaching. This may potentially lead to higher flood depths inside a levee as the water can “pump up” due to the influences of waves.
- • Simplified pumping - pumping has been included at the existing capacity where known. In other areas a simple relationship of 0.5 cfs/acre has been adopted without any consideration of any potential storage areas, the time for the water to reach the pumps or the distances over which pumping needed to take place. In some areas the area used for computing the pumping capacity has been fixed as there was no upper limit because of normal catchment drainage.
- • Pre-event storage. No allowance has been made for water trapped inside areas once flood defenses have been shut prior to a hurricane.
- • Rainfall - the rainfall rates have been taken as a synthetic distribution based on a fixed 10 year rainfall event. This has been used for all events, whereas in reality the rates of rainfall are likely to change for different return periods of event, and the distribution is unlikely to follow the uniform distribution assumed for this evaluation.
- • Joint probability of high river levels and high surges - no consideration has been given to the potential for increased levels at the interface between tidal and fluvial flows. River flows and levels have been taken as nominal.


Many of the above issues can easily be dealt with for small areas or if sufficient time and resources are available. Within the constraints of LACPR, they have been adopted as a pragmatic approach.

However, as the range of alternatives decreases then some of these issues should be reviewed and changes to the methodology made. It is not easy to quantify the effect that addressing these issues will have on the final results, but as alternatives progress towards more detailed design then addressing the issues will improve confidence on the absolute values obtained.



---PAGE-212---



In addition it will be difficult to improve all of the issues to the same degree for all of the planning units. As such, care should be taken in improving issues if the approach cannot be applied to all planning units as this may make comparing alternatives difficult, whereas at present the consistent approach adopted across all units makes alternatives comparable not only within a planning unit but also across planning units.

###### 9.3 Recommendations for refinements to the hydraulic analysis

As the options presented in the LACPR technical report are implemented, there will be a number of opportunities to refine the work carried out to date. The types of refinements required will be defined by each specific project or study. In general, suggested key refinements of the hydraulic analysis used for future projects or studies are as follows:

- • Model in ADCIRC and STWAVE the actual proposed levee alignments at their proposed heights and for the full suite of storms. Extract data for locations required for design and overtopping purposes for the proposed alignments. Ensure that a larger range of values are available for checking of the results.
- • Validate the STWAVE results for the actual areas with a field measurement program of wave propagation over marshes so that the issue of no friction or with friction wave modeling can be resolved. It is without doubt that more insight and more predictive capabilities in this regard could save huge amounts of money considering the differences in design heights when waves with and without friction are applied.
- • Undertake levee design specific to more localized areas and consider walls as well as embankments if necessary.
- • Compute wave overtopping over shorter lengths to give variable inflow into flood areas.
- • Use 2D modeling of flood flow to establish residual flood areas and depths and use the results of this modeling to site and design pump stations. 2D models should consider their interaction with adjacent areas so sequential flooding of drainage areas can be undertaken.
- • In the 2D modeling consider varying rainfall and establishing relationships between rainfall and hurricane events so that the shape of the rainfall hydrograph more closely matches that which would be expected within an extreme event.
- • Carry out further research to look at the parameters for defense breaching and determine if in extreme events levees should be assumed to breach. Investigate the impact of breaching on peak water levels within drainage areas.




---PAGE-213---



###### 10 REFERENCES

- 1. Plan Formulation Atlas, April 16 2007, http://lacpr.usace.army.mil/default.aspx?p=atlas
- 2. Resio et al., 2007. White paper on estimating Hurricane Inundation Probabilities, USACE, ERDCCHL.
- 3. TAW, 2003. Technische Adviescommissie voor de Waterkeringen, Leidraad kunstwerken (In Dutch), May 2003.
- 4. TAW, 2002: Wave runup and overtopping at Dikes, Technical Report, Delft, 2002. See also: www.tawinfo.nl.
- 5. USACE, 2007. Elevations for design of hurricane protection levees and structures, Lake Pontchartrain, Louisiana and vicinity hurricane protection project, west bank and vicinity. Draft report, Final report, Prepared by New Orleans District, 15 October 2007.
- 6. TAW, 2002. Technical Report Wave Run-up and Wave Overtopping at Dikes, Delft, The Netherlands.
- 7. IPET, 2007. Performance Evaluation of the New Orleans and Southeast Louisiana Hurricane Protection System, L.E. Link (editor).
- 8. FEMA, 2007. Flood insurance Study: Southeastern Parishes Louisiana, DRAFT, Intermediate Submission 1: Scoping and Data Review. September 19, 2007. FEMA Region 6 and USACE MVN District.
- 9. R.L. Pfost, 1993. Technical Attachment Rainfall patterns and Hurricane Andrew. A Hydrometeorological Survey, Lower Mississippi River Forecast Center, Slidell, Louisiana
- 10. R.W. Shoner and S. Molansky, 1956. Rainfall associated with Hurricanes. National Hurricane Research Project. Report No. 3. Prepared under P.L.71, 84th Congress, 1st Session.
- 11. Hughes, S.A., 2007: Evaluation of Permissible Wave Overtopping Criteria For Earthen Levees Without Erosion Protection, ERDC-CHL, Vicksburg.
- 12. U.S. Army Corps of Engineers, 2001: Coastal Engineering Manual. Engineer Manual 1110-2-1100, U.S. Army Corps of Engineers, Washington, D.C. (in 6 volumes).


###### =o=o=o=



---PAGE-214---



###### Annex A Preliminary Hydrodynamic and Sensitivity Analysis Results



---PAGE-215---



## Summary

Hydrodynamic modeling information presented in Annex A includes storm surge results from ADCIRC runs along with STWAVE results. In order to obtain estimates for computing storm surge frequency, each node in the ADCIRC domain is monitored for its water level response as a storm progresses along it track during a simulation. The maximum surge and wave value obtained for each point for each storm simulation is used in the JPM-OS analysis to develop a stage frequency at that point. Stage frequency relationships were computed in this manner for all ADCIRC nodes in the LACPR planning units. Statistical analysis and surfaces are not presented in this annex. Statistical analysis and surfaces are discussed in Volume II of the H&H Appendix and surfaces are included in the Evaluation Results Appendix.

In general, in Annex A only the maximum of maximum (MOM) surge results and wave results are presented when making plan comparisons. The MOM plots were obtained from maximum ADCIRC surge responses at each ADCIRC node using the entire suite of storms. For a given plan, the maximum surge elevation at each point in the ADCIRC domain was compiled into a single surface to represent the highest stages and waves that can be produced in the ADCIRC domain for the entire suite of 152 storms. The MOM water level and wave plots for a plan are not indicative of a specific water surface or wave frequency but rather represent the maximum water level and wave height obtainable from a plan with the suites of storms used to generate the surge estimates.

Plan comparisons of MOM plots to the 2007 base MOM plot are presented in Annex A. The reader needs to be aware that for most of the plans analyzed in the LACPR modeling effort, levee heights in the model were set to not overtop for even the highest storm surge generated by the 152 storm suite. This was done so that water levels on the flood side of the levee system would not be moderated by overtopping and therefore levee design heights for a specified frequency could be obtained from the surge values generated at the face of the various levee reaches in a proposed plan. Levee design elevations in the LACPR analysis were developed for the 100-, 400- and 1000year frequency water levels. This non-overtopping levee scenario is true for all plans unless otherwise noted. The one notable exception to the non-overtopping levees is the 2007 case where levee elevations in the model were set to the existing levee elevation at the start of the June 2007 hurricane season. Therefore, when comparing the 2010 base MOM condition to the 2007 MOM case, for the 2010 MOM one sees very large increases in water levels on the outside of levee systems and very large decreases in water levels on the protected side of the levee.

Future conditions for a projected 50-year future coast landscape are also discussed in Annex A. Landscape projections were obtained from the CLEAR modeling group who modified the ADCIRC grid to reflect the projected coastal change in near shore bathymetry. MOM plots of the future surge and wave heights are compared to the 2007 base MOM plots. Statistical analysis of future degraded no-action water surfaces are not presented in Annex A. Statistical surfaces are discussed in Volume II of the H&H Appendix and Maps are shown in the Evaluation Results Appendix.

Annex A also presents a sensitivity analysis for sea level rise in which water levels in the model were increased by 1, 2 and 3 feet above the base water level. The analysis was done to support ongoing restoration work for Corps offices involved in restoring levees damaged by Hurricane Katrina in response to the Congressional Directive to rebuild the damaged levee systems to their design grades or to the 100-year design level, whichever of the two levels is the higher. Using the 1, 2 and 3 foot increases in base water levels, the inundated marsh areas covered by these increased water levels were converted to water bottoms and the appropriate friction values were applied to simulate change in resistance to flow. Twenty-seven storms from the 152 storm suite were chosen for the sensitivity analysis. These storms were selected since their surge generating characteristics closely approximated the 100-year surge value in the area of on-going restoration work. The results from the sensitivity analysis were used to estimate future conditions for the restoration work in the New Orleans area but were not used in LACPR.



---PAGE-216---



## ANNEX A. PRELIMINARY HYDRODYNAMIC AND SENSITIVITY ANALYSIS RESULTS

#### A.1 Introduction

The purpose of the hydrodynamic modeling was to estimate the surge and wave conditions for the base conditions and various alternatives for storms in the JPM-OS suite for the calculation of stagefrequency curves. This involved an examination of the entire spatial domain every time step (1 sec) to determine if water levels exceeded the previous time steps maximum water level at any point in the domain. The result of this analysis is a maximum envelope of water level for a given simulation. From the ensemble of results, the expected return periods for those surge and wave conditions is calculated to assist in the quantification of risk. Example output generated from the ADCIRC model results are provided in the figures and discussion below. The results provided in this section are maximum surge elevations for each alternative or base condition for all storms simulated. The results are for illustrative purposes and as presented here do not provide information on levels of protection, which is discussed in subsequent chapters of this report. As discussed in Volume I of this report, five STWAVE grids were utilized. Results from only the southeast grid are presented here as an example of those results.

For each alternative presented herein, results for the suite of storms simulated for each alternative were scanned for peak elevations at each node, from which a “peak of peaks” data file and plot were produced (hereafter referred to as “peak” or “maximum” values/plots). The peak values for the same storm suite run on the 2007 base grid were then subtracted from the alternative maximum surge values to produce difference files and plots. Each figure title indicates the alternatives being compared to the 2007 base. Because the 2007 peak values are always subtracted from the alternative, a positive number indicates that peak surge values for the alternative are higher than the 2007 peaks, while a negative number indicates that peak surge values for the alternative are lower than the 2007 peaks. For surge results, the upper range of the legend ends at +12 feet (except for the Barrier Island cases), the maximum difference observed in any of the comparisons. Areas colored mauve indicate regions that were wet for at least one storm in the alternative simulations but were dry during all storms in the 2007 simulations. The lower range of the legend ends at -12 feet for the Marsh, and Plaquemines alternatives, the lowest observed difference for those scenarios. For the EA-ED levee system options, as well as the 2010 configuration, the lower range of the legend ends at -22 feet, the maximum observed difference for those scenarios. Areas colored dark green indicate regions that were dry during the entire storm suite in the alternative simulations but were wet for at least one storm in the 2007 base case. For these graphs, the range -12 to -22 feet was colored pale green; this color indicates regions that have a small depth of water present for at least one storm for that alternative (e.g., a marsh-like area), and they had a large peak surge value for at least one storm in the 2007 base case. The Barrier Island surge results legend had an upper and lower end of +/- 6 feet, respectively. For the STWAVE results, a legend with an upper range of +6 feet and a lower range of -6 feet was used for all alternatives, except the Barrier Islands, which used +8 feet at the upper end and -8 feet at the lower.

#### A.2 2007 Base Condition - East

The 2007 Base condition was created to represent South Louisiana as it was projected to exist at the start of the 2007 hurricane season. Post Hurricane Katrina and Rita topographic and bathymetric conditions were combined with levee definitions to reflect the system repairs and upgrades that were implemented as part of the USACE Task Force Guardian and by the USACE HPO and MVN.



---PAGE-217---



Simulations were completed for the 152 storms for eastern Louisiana in order to define water levels and corresponding wave conditions. This information serves as a base condition to which alternative levee systems, barrier island variations, marsh improvements and/or degradation, and sea level rise can be compared. Section 2.4 of Volume 1 of this report (and section A.4 of this Annex) describes the motivation for study and changes to the physical system for each alternative inspected.

- Figure A.2-1 represents the maximum surge level recorded for the East 152 storms simulated for Southeastern Louisiana. It is important to note that the displayed water levels are not stochastic representations of the 100-year or other return period water elevations, but rather are the maximum surge levels for all 152 specific storms simulated for the JPM-OS method. The highest surge levels occurred in three locations: along the east side of the Plaquemines Parish levee system from Belle Chasse to Port Sulphur; along the Mississippi coast near Biloxi and Gulfport; and northwest of Terrebonne Bay near Houma.


- Figure A.2-1. Maximum surge level (ft) for the 2007 base case for all East 152 storms.


East of the Mississippi River, peak surge levels along the Plaquemines Parish levees all the way to the Mississippi Coast are on the order of 25 ft. These high surges develop as water is blown by easterly and then southerly winds onto the shallow Mississippi-Alabama shelf and is then stopped by the Mississippi River delta and levees and the coast of the state of Mississippi. The New Orleans metropolitan region is significantly flooded as the levees of St. Bernard Parish and New Orleans East are overtopped. Mean water levels also rise in Lake Pontchartrain as water flows via the Rigolets, Chef Menteur Pass and over the Pontchartrain land bridge, especially in easterly winds. In addition, strong localized set up occurs in this large shallow lake. Maximum surge elevations on the north and south shores of Lake Pontchartrain are approximately 15 to 18 ft. A substantial populace is located in areas directly affected by the water levels in the lake. For this reason, primary alternative levee systems inspected are various closure options for Lake Pontchartrain. Maximum surge values northwest of Terrebonne Bay in the Houma area are over 20 ft due in large part to surge being locally trapped both as it propagates north but also east and west by local levees and



---PAGE-218---



roads. Maximum surge elevations along the West Bank levees are more modest reaching about 12 ft. Much like the regions adjacent to Lake Pontchartrain, a high populace resides in this portion of the state. Maximum 2007 wave heights outside of the east New Orleans levee system, as predicted by STWAVE simulations (Figure A.2-2), are on the order of 6 to 8 feet near Caernarvon, on the order of 6 to 8 feet near the MRGO/GIWW, and on the order of 8 to 10 ft near the Pontchartrain land bridge.

- Figure A.2-2. Maximum wave height (ft) for the 2007 base case for all 152 storms.


#### A.3 2010 Base Condition

The 2010 condition represents the levee configuration that would exist if the proposed hurricane protection system was built to currently-authorized levels and also includes a levee that runs along the proposed Morganza to the Gulf alignment raised so that it does not overtop. The 2010 system also raises levee heights around the existing system in and around metropolitan New Orleans on both the east and west banks (with the exception of the Belle Chase) to approximate 100 year levels. In addition, the system includes a levee to close the MRGO/GIWW east of Paris Road to stop the propagation of surge into the heart of New Orleans. Figure A.3-1 shows the difference in the envelope of maximum water level between the 2010 and 2007 configurations. Initially, also included in the 2010 base run was the proposed levee for the Morganza to the Gulf project. Since the 2007 ADCIRC model runs had already addressed the base no levee condition for the Morganza area it was decided to include this proposed levee system to maximize design output from the ADCIRC runs. The Morganza levee is not expected to be completed by the 2010 date but was included in the ADCIRC runs to expedite reanalysis of the Morganza project which at the time was awaiting authorization for construction by the Congress. Around the Morganza area (to the west of Bayou Lafourche) the model included a non overtopping levee to represent the proposed new levee



---PAGE-219---



around the Morganza area. The Morganza project was considered to be sufficiently removed from the PU-1 and PU-2 basins so as to not influence surge responses in those basins. Figure 2.5 below in fact shows that the proximity of the proposed Morganza levee has no influence on water levels in PU-1 and PU-2. For this conclusion, the reader should note the large area of no change separating the two response surfaces shown in Figure 2.5. To avoid confusion when looking at the 2010 base In the final Analysis for which results are presented in the Evaluation Results Appendix the 2010 Base condition was reanalyzed without the proposed Morganza Levee and all 152 storms in the east were run in ADCIRC. The 304 JPM-OS code was used to compute the frequency analysis for the 2010 Base condition.

The inclusion of a non-overtopping barrier around Golden Meadows and from Morganza to the Gulf blocks the incoming surge, raising the peak water levels south of the levees by up to 12 feet near Cut Off and up to 3 feet near Morgan City. Behind the barrier, the peak water levels in most areas are either reduced by 10 to 22 feet (dark blue and pale green areas), or they remain completely dry for all simulated storms, whereas in the 2007 configuration, the area had peaks up to 22 feet. Similar effects are seen in the New Orleans area, i.e., the fortified 2010 system either reduces the peaks by 10 to 22 feet (dark blue and pale green areas), or eliminates the surge entirely (dark green areas). Outside of the fortified New Orleans system, the peak surge increases in most areas about 1 to 3 feet. However, near the MRGO/GIWW closure, the peak surge increases 4 to 5 feet, while the peak surge near the English turn in the Mississippi increases by about 7 to 8 feet, relative to peak 2007 conditions. Maximum surge also increases up to 6 ft in the poorly protected Belle Chase region with effective focusing of surge in this concavity in the system. There was very little change in the maximum wave heights outside the hurricane protection system (Figure A.3-2).

- Figure A.3-1. Difference in maximum surge level between the 2010 levee configuration and the 2007 base case for the 2010 storm suite.




---PAGE-220---



- Figure A.3-2. Difference in maximum wave height (ft) between the 2010 levee configuration and the 2007 base case for the 2010 storm suite for the southeast STWAVE grid.


#### A.4 Closure options of Lake Pontchartrain

Various levee system alternatives were developed to understand the performance and implications of a variety of levee system improvements. A more detailed description and the suite of storms simulated for each alternative is provided in Volume I of this report, Background and Methodology. Four east levee configurations included closure options of Lake Pontchartrain. This section documents results for east alternatives A through D as they relate to the proposed closures of Lake Pontchartrain.

###### A.4.1 Full closure along US90 (Alternative EA)

- Alternative EA involves complete closure of Lake Ponchartrain through a 30-mile non-overtopping levee extending from the junction of US11 and US90 to a point just north of Slidell near I-59. The levee generally follows the US90 corridor, extending along the west bank of Lake Borgne, the west boundary of Lake Saint Catherine, and crossing through the Chef Menteur and Rigolets Passes. Both the passes would be entirely closed during storms with gates. At the intersection of US90 and US190, the levee stretches northwestward, ultimately terminating at a point approximately one mile north of the I-10/I-12/I-59 interchange near Slidell, LA. Another feature of the alternative EA configuration is a non-overtopping levee extending along the west shore of Lake Borgne, providing full closure at the funnel for the Inner Harbor Navigation Channel and the Gulf Intracoastal Waterway.




---PAGE-221---



- Figure A.4-1 depicts the difference in maximum water level between the alternative EA and 2007 base case. Non-overtopping levees and channel closures prevent the filling of Lake Pontchartrain from Lake Borgne and the Mississippi Sound and thus prevent the increase in mean lake levels. Local winds still drive a localized set up in the wind direction causing high water levels along the shores of the lake. A 2 to 3 ft decrease is predicted for lakefront areas at the city of New Orleans, with maximum surge levels in the neighborhood of 10 to 12 ft. Along the north shore of Lake Pontchartrain, areas such as Mandeville and Lacombe are expected to experience a maximum surge decrease ranging between 2 and 7 ft. Maximum surge levels along the north shore of Pontchartrain are predicted to be between 9 and 14 ft. At the western shore of Lake Pontchartrain, surge reductions are predicted to be between 3 and 4 ft. In addition, the entire south levee of New Orleans East, about half the north levee of St. Bernard and the southern reach of the IHNC experience vast reductions in surge levels and/or see little or no surge against them as a result of the closure on the west shore of Lake Borgne.


Areas seaward of the levee experience water level increases. As inland surge propagation accumulates along the seaward side of the non-overtopping levee, maximum levels within Lake St. Catherine are predicted to increase by as much as 8 ft in comparison with the 2007 base levels, with a maximum predicted level of approximately as much as 30 ft. Increases in maximum surge levels are expected to be around 4 ft along the mouth of the Pearl River, and 7 ft near Bayou Savage National Wildlife Refuge within Lake Borgne. At the non-overtopping levee that encloses the funnel, surge levels are expected to increase by between 6 and 8 ft from the base 2007 levels. The effects of alternative EA may be felt as far east as Long Beach, MS, with a surge increase of 1 ft, and maximum levels between 22 and 24 ft.

In Figure A.4-2, the difference in maximum wave heights between alternative EA and the base case are presented. Wave heights increase seaward of the full-closure funnel levee between 0.5 and 1 feet. Wave heights increase seaward of the non-overtopping US90 Pontchartrain levee by up to 3 ft.

- Figure A.4-1. Difference in maximum surge level between alternative EA and the base case for the


- EA storm suite.




---PAGE-222---



- Figure A.4-2. Difference in maximum wave height (ft) between alternative EA and the base case

- for the EA storm suite for the southeast STWAVE grid.


A.4.2 Weir closure along US90 (Alternative EB)

Alternative EB is identical to EA with the exception that the levee across the Pontchartrain landbridge from Chef Menteur to the Rigolets was lowered from a height not to be overtopped to 12 ft.

- Figure A.4-3 is the difference in the envelope of maximum water level between alternative EB and the 2007 base case. The weir levee stops the propagation of the surge into Lake Pontchartrain until its elevation exceeds 12 ft, resulting in lower peak surges in Lake Pontchartrain relative to the base case. However, for large storms on select tracks there will still be considerable infilling of Lake Pontchartrain from Lake Borgne and the Mississippi Sound. The surge on the south shore of Pontchartrain is reduced 2 to 3 ft relative to the 2007 base case and reductions of up to 3 to 4 ft are predicted on the north shore. The maximum surges on the south shore with alternative EB in place range from about 9 to 13 ft, increasing as you move from west to east. On the north shore, the peak surges for alternative EB are greater than 12 ft from about Madisonville to the east. The inclusion of the weir levee across the Pontchartrain land bridge increases water level seaward of the weir 3 to 4 ft and near Slidell 2 to 4 ft. The peak surge at the proposed levee that closes the funnel is increased


- 5 to 6 ft. In comparison to alternative EA, the surge reductions in Lake Pontchartrain due weir closure are less, however they are not significantly different on the south shore. The surge seaward of the structure is also less, with a maximum increase of 8 ft for alternative EA, compared to an increase of 4 ft for alternative EB. Figure A.4-4 depicts the maximum wave height differences for alternative EB. Wave height differences for areas seaward of the full-closure funnel levee range between 4 and 5 feet. Wave heights are predicted to increase inland of the US90 Pontchartrain weir by up to about 2 ft.




---PAGE-223---



- Figure A.4-3. Difference in maximum surge level between alternative EB and the base case for the


- EB storm suite.




---PAGE-224---



- Figure A.4-4. Difference in maximum wave height (ft) between alternative EB and the base case

for the EB storm suite for the southeast STWAVE grid.

A.4.3 Partial closure along US90 (Alternative EC)

The levee configuration for alternative EC involves a non-overtopping levee following the same path as alternative EA. Alternative EC differs from alternative EA in that it includes openings at Chef Menteur Pass and the Rigolets. These openings allow water to flow through these deep conveyance channels between Lake Pontchartrain and Lake Borgne. Alternative EC maintains the closure at the funnel through a non-overtopping levee placed along the west bank of Lake Borgne.

- Figure A.4-5 illustrates the difference between the maximum water level for alternative EC and Base


2007. Alternative EC’s partial closure configuration results in a maximum increase within Lake Pontchartrain of less than 3 ft. Areas along Pontchartrain’s north shore are predicted to experience a surge reduction of less than 2 ft, with similar reductions in the vicinity of New Orleans. Maximum water levels within Lake Pontchartrain range from 11 to 15 ft along the northern shore from Mandeville, LA to Lacombe, LA. Water levels as high as 18 ft are predicted for areas between Kenner, LA and Frenier, LA. Seaward of the levee, an accumulation of surge forms, resulting in an increase of alternative EC water levels in comparison with the Base 2007 levels. The greatest surge increase due to the EC configuration is 6 ft, occurring within Lake Saint Catherine. Maximum surge level increases range between 5 and 6 ft at points along the seaward side of the levee that provides closure to the funnel. The effects of the levees in alternative EC are confined to areas west of Waveland, MS, where surge increases due to the modified levees are predicted to be less than 1 ft. In comparison with alternatives EA and EB, alternative EC provides less reduction in surge levels within Lake Pontchartrain. For example, Lacombe, LA is predicted to experience only a 1 ft surge reduction due to alternative EC compared to 7 and 3 ft for alternatives EA and EB, respectively. Maximum wave height differences for alternative EC are presented in Figure A.4-5. Wave heights seaward of the full-closure funnel levee are not predicted to increase. Wave heights are predicted to increase at the partial closure US90 Pontchartrain levee by up to 1 ft.



---PAGE-225---



- Figure A.4-5. Difference in maximum surge level between alternative EC and the base case for the


- EC storm suite.




---PAGE-226---



- Figure A.4-6. Difference in maximum wave height (ft) between alternative EC and the base case


- for the EC storm suite for the southeast STWAVE grid.


###### A.4.4 Full closure through Lake Borgne (Alternative ED)

In alternative ED, a non-overtopping levee isolates Lake Pontchartrain from Lake Borgne. This levee extends from Verret, LA, northward through Lake Borgne along a straight line to a point along the Gulf Intracoastal Waterway just south of Little Lake. At this point, the levee extends northwestward along the Pearl River corridor, crossing I-10, and terminating at a point approximately one mile north of the I-10/I-12/I-59 interchange. This approximately 35 mile levee provides full closure to Lake Pontchartrain, Lake Saint Catherine, the Chef Menteur Pass, the Rigolets, the funnel, and portions of southeastern Lake Borgne. The non-overtopping levee in alternative ED results in an inland surge decrease accompanied by seaward accumulation of water. Figure A.4-7 illustrates the difference between the maximum water level for alternative ED and Base 2007. Maximum surge decreases inland of the non-overtopping levee are predicted to be over 12 ft at areas within Lake Borgne and Lake Saint Catherine. From Mandeville, LA to Lacombe, LA, predicted maximum surge decreases range from 3 to 6 ft along Pontchartrain’s north shore. Areas along the southern shore show a 2 to 3 ft decrease from the Base 2007 levels. Maximum water levels within Lake Pontchartrain range from 3 to 15 feet, with the highest levels occurring along Pontchartrain’s southwestern shore, between Kenner, LA and Frenier, LA. Maximum levels along Lake Pontchartrain at New Orleans were between 9 and 12 ft. Simulation of the alternative ED configuration depicts the maximum water level occurring seaward of the non-overtopping levees. For areas seaward of the non-overtopping levee within Lake Borgne, maximum water levels are approximately 30 ft. The effects of the alternative ED levee are predicted to be felt as far east as Gulfport, MS, where surge levels increase less than one foot due to levee implementation. In regards to surge reductions within Lake Pontchartrain, alternative ED is comparable to alternative



---PAGE-227---



###### EA. Alternative ED is unique in that it provides dramatic reductions within Lake Saint Catherine and portions of Lake Borgne, whereas alternative EA increases levels in these areas. Figure A.4-8 depicts maximum wave height differences for alternative ED. Wave heights seaward of the full closure levee dividing Lake Pontchartrain and Lake Borgne are predicted to increase up to approximately 2 ft. Wave heights in the Caernarvon area are expected to increase by less than 1 ft.

- Figure A.4-7. Difference in maximum surge level between alternative ED and the base case for the


- ED storm suite.




---PAGE-228---



- Figure A.4-8. Difference in maximum wave height (ft) between alternative ED and the base case


- for the ED storm suite for the southeast STWAVE grid.


#### A.5 Plaquemines

This section documents the results of the study that explored the influences of the lower Plaquemines Parish levee system on storm surge. The height of the levee system range from 16 to 18 ft, the natural floodplains of the Mississippi range from 3 to 8 ft. From Jesuit Bend, the levee system has a length of 24 mi on the eastside and 57 mi on the west side of the river. The total length of the delta is 81 mi from Jesuit Bend to the birds-foot. A suite of 18 hypothetical storms were simulated in order to evaluate three different configurations of the levee system: One represents the 2007 base case and serves as the reference case; the second, Plaquemines 1, introduces three spillways across the levee system with a total length of 9.5 mi; and the last one, Plaquemines 2, represents the situation of having no levees along the delta, 57 mi of levees has been removed.

###### A.5.1 Plaquemines 1

The purpose of the spillways is to provide a hydrodynamic connection between the west- and eastside of the delta, which should result in reduced surge levels on the upwind side of the delta.

- Figure A.5-1 shows the difference in peak values between Plaquemines 1 and the 2007 base case. The spillways reduce the maximum water levels 1 to 2 ft on the northeastern part of the delta, around the first spillway. At Pointe a la Hache, at the second spillway, the maximum reduction in peak water levels is about 2 ft. On the west side of the delta, around Barataria, maximum surge levels are increased 1 to 2 ft. Changes in maximum water levels due to the spillways only occur




---PAGE-229---



###### along the delta. Surge that propagates upriver spills out through the northern spillway, reducing the surge that propagates to New Orleans. Figure A.5-2 shows the difference in maximum wave heights between Plaquemines 1 and the 2007 base case. Waves are predicted to locally increase by less than 3 ft at the spillways while there are some small decreases in waves east of the spillways.

- Figure A.5-1. Difference in maximum surge level between Plaquemines 1 and the base case for the Plaquemines storm suite.




---PAGE-230---



- Figure A.5-2. Difference in maximum wave height (ft) between Plaquemines 1 and the base case for the Plaquemines storm suite for the southeast STWAVE grid.


###### A.5.2 Plaquemines 2

The configuration without having levees along the delta provides an upper limit in creating a hydrodynamic connection between the west- and eastside of the delta and represents a more natural system as well. Figure A.4-3 plots the difference in peak values between Plaquemines 2 and the 2007 base case. Completely removing levees reduces the maximum flood levels 3-8 ft along the levees of St. Bernard and Plaquemines Parish. The flood levels increase less than 1 ft at Barataria, on the westside of the delta, less than in the case with spillways. Surge that propagates upriver towards New Orleans is reduced due to the surge that propagates across the delta; and because the surge moving up the river spills out before reaching Jesuit Bend. Figure A.5-4 shows the difference in maximum wave heights between Plaquemines 2 and the 2007 base case. Waves are predicted to decrease 2 to 3 ft along the levees of St. Bernard and Plaquemines Parish as well as in the Caernarvon and Biloxi Marsh areas. Waves on the east bank of the river are predicted to decrease up to 6 ft.



---PAGE-231---



###### Figure A.5-3. Difference in maximum surge level between Plaquemines 2 and the 2007 base case for the Plaquemines storm suite.



---PAGE-232---



- Figure A.5-4. Difference in maximum wave height (ft) between Plaquemines 2 and the base case for the Plaquemines storm suite for the southeast STWAVE grid.


#### A.6 Closure options for Barataria Basin

Various levee system alternatives were developed to understand the performance and implications of a variety of levee system improvements. A more detailed description and the suite of storms simulated for each alternative is provided in Volume I of this report, Background and Methodology. Two east levee configurations included closure options for the Barataria Basin. This section documents results for east alternatives EA and EB as they relate to the proposed closure of Barataria Basin.

###### A.6.1 Full closure (Alternative EA)

In this region, alternative EA includes the non over-topping Morganza to the Gulf levee as in the 2010 system and adds a non-overtopping levee from the west bank of the Mississippi River from Belle Chasse to Larose along the alignment of the GIWW. On the east, the closure ties into the Mississippi river levee and on the west, the closure ties into the Larose and Golden Meadow flood protection structure. The difference in the envelope of maximum water level between alternative EA and the 2007 base case is given in Figure A.4-1. The non over-topping levee effectively eliminates the propagation of the surge into the Barataria Basin where water levels in the protected region behind the levee are shown to be reduced by as much as 10 ft in some areas, including along the West Bank. However, the inclusion of the non over-topping levee across the opening of the Barataria Basin does increase water levels seaward of the structure by up to 12 ft because the hurricane wind and waves force the water to pile up against the levee structure. Water surface elevations to the west of Golden Meadow are essentially the same as in the 2010 configuration.



---PAGE-233---



###### A.6.2 Weir closure (Alternative EB)

Alternative EB includes a lower 20 ft overtopping Morganza to the Gulf levee and in addition lowers the closure across Barataria Basin from a height not to be overtopped to 12 ft. The difference in the envelope of maximum water level between alternative EB and the 2007 base case is given in Figure A.4-3. While the weir reduces the flooding from smaller storms, it is over-topped by larger storm events. The Barataria levee does slow surge propagation northward, but the additional defenses along the west bank increase the surge in this area. Consequently, maximum surge values north of the Barataria closure are not changed much relative to the base case. However, the inclusion of the weir across the opening of Barataria Basin still stops or reduced northerly flows and therefore does increase peak water levels seaward of the weir by up to 4 ft. Surge is also amplified in this region by raising of the Mississippi river levees (see 2010 Base condition) which prevents water from escaping from west bank to the Mississippi River. Without this relief, the water piles up higher against the seaward side of the Barataria Basin levee. Since the weir in this configuration will allow overtopping, some regions immediately landward from the structure show increases in maximum surge levels as a result of the water which piles up on the landward side of the structure. The increases within the protected region are very localized. A benefit that is not revealed by the maximum plots is that many smaller storms will generate significantly less surge behind the weir compared with the base case, for instance a reduction in the 100-yr water level is expected and this is the intent of such a weir structure. Water surface elevations to the west of Golden Meadow are similar to the 2010 configuration although more flow propagates northward behind the lowered system.

A comparison of difference in the envelope of maximum water surface elevations between alternatives EA and EB reveals that Barataria Basin is significantly better protected against large events by the non-overtopping levee. Reducing the crest elevation of the levee to permit overtopping in EB results in minimal protection from large storm events, but does provide protection for storms near and below the 100-year level. On the seaward side of the levee, the higher levee of EA induces a much greater increase in maximum surge along the structure. Conversely, the lower EB weir allows relief during the larger storms that can overtop it, thus its impact seaward of the structure is not as pronounced. In summary, the EA structure is more effective at reducing surge in Barataria Basin but causes greater increase in surge on the seaward side, while the EB structure reduces surge in Barataria Basin from smaller storms.

#### A.7 West Alignments

Various levee system alternatives were also developed for the western part of the state. A description and the suite of storms simulated for the west and each alternative is provided in Volume I of this report, Background and Methodology. Three west levee configurations were simulated and this section documents results for west alternatives A through C.

###### 2.7.1 2007 Base Condition

The 2007 Base condition was created to represent South Louisiana as it was projected to exist at the start of the 2007 hurricane season. Post Hurricane Katrina and Rita topographic and bathymetric conditions were used. Simulations were completed for the 152 storms for western Louisiana in order to define water levels and corresponding wave conditions. This information serves as a base condition to which alternative levee systems, marsh improvements and/or degradation, and sea level rise can be compared. Section 2.4 of Volume 1 of this report (and section A.4 of this Annex)



---PAGE-234---



describes the motivation for study and changes to the physical system for each alternative inspected.

- Figure A.7-1 represents the maximum surge level recorded for the West 152 storms simulated for Southeastern Louisiana. It is important to note that the displayed water levels are not stochastic representations of the 100-year or other return period water elevations, but rather are the maximum surge levels for all 152 specific storms simulated for the JPM-OS method. The highest surge levels in Louisiana occurred along the coast of Cameron Parish. Peak surge levels along the Cameron Parish levees are on the order of 24 ft. South of Lafayette, LA, peak surge levels reach approximately 21 ft. Maximum 2007 wave heights, as predicted by STWAVE simulations (Figure


- A.7-2), are on the order of 18 feet near the coast but break there and are greatly reduced inland.


- Figure A.7-1. Maximum surge level (ft) for the LAWEST 2007 base case for all West 152 storms.




---PAGE-235---



- Figure A.7-2. Maximum wave height (ft) for the LAWEST 2007 base case for all 152 storms.


###### A.7.2 Alternative WA

- Alternative WA includes a non-ovetopping levee that runs along the GIWW across all of western Louisiana from the Atchafalaya River to Vinton. West of Vinton, the levee turns north and runs to higher ground. The difference in the envelope of maximum water level between alternative WA and the 2007 base case is given in Figure A.7-3. The non over-topping levee eliminates the propagation of the surge north of the levee where water levels in the protected region behind the levee are shown to be reduced by greater than 10 ft in some areas. However, the inclusion of the non overtopping levee does increase water levels seaward of the structure by up to 6 ft because the hurricane wind and waves force the water to pile up against the levee structure. Maximum wave heights (Figure A.7-4) are reduced by 1 to 3 ft in some areas north of the proposed levee. Less than a 1 ft increase in wave height is predicted seaward of the levee.




---PAGE-236---



- Figure A.7-3. Difference in maximum surge level between alternative WA and the LAWEST base

- case for the WA storm suite.


- Figure A.7-4. Difference in maximum wave height (ft) between alternative WA and the LAWEST


- base case for the WA storm suite for the west STWAVE grid.




---PAGE-237---



###### A.7.3 Alternative WB

- Alternative WB includes a non-ovetopping levee that runs from the Atchafalaya River to Abbeyville, north of the GIWW. At Abbeyville, the levee turns north and runs west of Lafayette to higher ground. This alternative also includes small ring levees around Gueydan and Kaplan. Further to the west, a large ring levee extends from east of Lake Charles to west of Vinton protecting these areas. The difference in the envelope of maximum water level between alternative WB and the 2007 base case is given in Figure A.7-5. The non over-topping levees eliminate the propagation of the surge north of the levee where water levels in the protected region behind the levee are shown to be reduced by up to 10 ft in some areas and flooding is eliminated in many areas. The inclusion of the non overtopping levees does increase water levels seaward of the structures. Maximum wave heights (Figure A.7-6) are changed by less than 1 ft.


- Figure A.7-5. Difference in maximum surge level between alternative WB and the LAWEST base


- case for the WB storm suite.




---PAGE-238---



- Figure A.7-6. Difference in maximum wave height (ft) between alternative WB and the LAWEST


- base case for the WB storm suite for the west STWAVE grid.


###### A.7.4 Alternative WC

- Alternative WC is similar to WB except that a 100-year protection levee extends along the GIWW from Vermillion Bay to Calcasieu Lake and there are no ring levees around Gueydan and Kaplan. The difference in the envelope of maximum water level between alternative WC and the 2007 base case is given in Figure A.7-7. The results are similar to the other alternatives. The non over-topping levees eliminate the propagation of the surge north of the levee where water levels in the protected region behind the levee are shown to be reduced by up to 10 ft in some areas and flooding is eliminated in many areas. The 100-year protection levee also greatly reduces surges, with decreases from 1 to 10 ft across the protected area. The inclusion of the levees does increase water levels seaward of the structures. Maximum wave heights (Figure A.7-8) are generally changed by less than 1 ft with 1 to 2 ft reductions in some areas behind the proposed levees.




---PAGE-239---



- Figure A.7-7. Difference in maximum surge level between alternative WC and the LAWEST base

- case for the WC storm suite.


- Figure A.7-8. Difference in maximum wave height (ft) between alternative WC and the LAWEST


- base case for the WC storm suite for the west STWAVE grid.




---PAGE-240---



#### A.8 Future Conditions

A sensitivity analysis was performed to assess the impact of sea level rise and bathymetric and frictional resistance changes on ADCIRC-simulated peak surge elevations and STWAVE-simulated waves. Topography, landscape features, and vegetation have the potential to reduce storm surge elevations and absorb wave energy. Land elevations greater than the storm surge elevation act as a physical barrier and create bathymetric resistance for the surge and waves. Landscape features such as barrier islands also have the potential to create frictional resistance and affect storm surge and wave energy even when below the surge elevation. The influence of these features is reduced if they are lost or inundated due to sea level rise. This section is used to assess the impact of barrier island and marsh features on storm surge and wave energy at the mainland coast and to evaluate the impact of sea level rise.

###### A.8.1 Barrier Islands

The barrier island configurations modeled were: 1) the existing 2007 base Post-Katrina degraded condition; 2) no barrier islands with open water Manning's n value = 0.02 (BI-1); and 3) a restored barrier island configuration of 12 ft (NAVD88 2004.65) for Cat Island, Ship Island, Horn Island, Petit Bois Island, and Dauphin Island and 6 ft (NAVD88 2004.65) for the Chandeleur Islands (BI-2), 4) the existing Post-Katrina degraded condition with a forest Manning's n = 0.15 (BI-3), and 5) a restored barrier island configuration with a forest Manning's n = 0.15 (BI-4). The BI-4 configuration is identical to the restored BI-2 configuration except a Manning’s n=0.15 friction has been applied to the islands to represent the increased frictional resistance associated with a forest. Results from the extreme cases, BI-1 and BI-4, are presented here.

The difference in the envelope of maximum water level between the BI-1 configuration and the 2007 base case can been seen in Figure A.8-1. The largest increase in surge seen by the removal of the barrier islands is approximately 1.7 ft in Chandeleur Sound. Outside of Chandeleur Sound, the surge increases less than a foot nearly everywhere when compared to the 2007 base case. Lake Borgne demonstrates a rise in surge of approximately 0.7 ft. The removal of the barrier islands also increases surge by as much as 1.5 ft in the Bay St. Louis, MS area. The maximum wave height differences predicted for the BI-1 configuration can be seen in Figure A.8-2. Maximum wave heights are expected to increase outside of the east New Orleans levee system up to 2 feet near Caernarvon and the IHNC/MRGO funnel. Maximum wave heights are predicted to increase by as much as 3 ft in the Bay St. Louis, MS area. The largest increase in maximum wave heights (greater than 8 ft) is observed immediately landward of the barrier islands.



---PAGE-241---



Figure

- A.8-1. Difference in maximum surge level (ft) between the BI-1 configuration and the base case for the Barrier Islands storm suite.




---PAGE-242---



- Figure A.8-2. Difference in maximum wave height (ft) between BI-1 and the base case for the Barrier Islands storm suite for the southeast STWAVE grid.


Figure A.8-3 is the difference in the envelope of maximum water level between the BI-4 configuration and the 2007 base case. The figure demonstrates the potential effects of the restored barrier islands configuration with reductions in maximum surge generally 2 ft or less at the levees when compared to the 2007 base case. There is less than 1 ft decrease in surge in Lake Pontchartrain. The restored barrier islands also decrease surge by approximately 2 ft in the Bay St. Louis, MS area. The surge in Chandeleur Sound just behind the island is reduced by as much as 6 ft with for this restoration scenario, but the reduction is less than one foot at the Plaquemines and St. Bernard levees. Figure A.8-4 shows the maximum wave height differences for the BI-4 configuration. Maximum wave heights are expected to decrease outside of the east New Orleans levee system, as predicted by STWAVE simulations, up to 2 feet near Caernarvon and 1 ft near the IHNC/MRGO funnel. Maximum wave heights are predicted to decrease by as much as 1.5 ft in the Bay St. Louis, MS area. The largest decrease in maximum wave heights (greater than 6 ft) is observed immediately landward of the barrier islands. Wave energy dissipates as a result of the restored islands and reduces the landward maximum wave heights when compared to the BI-1 and base configurations.



---PAGE-243---



###### Figure A.8-3. Difference in maximum surge level (ft) between the BI-4 configuration and the base case for the Barrier Islands storm suite.



---PAGE-244---



- Figure A.8-4. Difference in maximum wave height (ft) between BI-4 and the base case for the Barrier Islands storm suite for the southeast STWAVE grid.


The model results indicate that the barrier islands provide some level of protection as a first line of defense. In general, raising the barrier islands caused a decrease in peak water level and wave energy landward of the barrier islands when compared to the peak water level and wave energy for the baseline 2007 Post-Katrina configuration. Degradation of the barrier islands caused a minimal increase in maximum surge level landward of Chandeleur Sound and increased waves at the hurricane protection system. With less obstruction in the Chandeleur Sound, the modeled wave heights increase, thus heightening the potential for overtopping of levees and inundation of protection areas.

###### A.8.2 Marsh Alternatives

The marsh alternatives included a predicted wetland definition 50 years into the future with no increased action (NIA) taken and a restored/improved marsh condition. The NIA condition was developed as part of the Coastal Louisiana Ecosystem Assessment and Restoration (CLEAR) Program. The forecasting model developed by CLEAR predicts physical processes, geomorphic features, water quality, and ecological succession. Geomorphic/bathymetric changes are based on the likelihood of discretized regions changing from open water to marsh or marsh to open water. The future condition of Coastal Louisiana predicted by CLEAR, referred to as the degraded condition, in fact does predict degradation in Southern Louisiana, but also predicts growth in the Atchafalaya basin and Breton Sound. The CLEAR future condition bathymetry was applied to the model grids and mesh and a series of storm simulations was made. Figure A.8-5 identifies the CLEAR/NIA landscape changes. Figure A.8-6 is the difference in the envelope of maximum water level between the CLEAR marsh configuration and the 2007 base case for areas to the west and the 2010 base case for the West Bank and areas east of the river. Comparison to two grids is required to isolate the impact of the wetland degradation. The degraded wetlands were incorporated into the



---PAGE-245---



2010 base grid with the Morganza to the Gulf levee removed. For this reason, areas to the west were compared to 2007 which also did not incorporate the Morganza to the Gulf levee. White areas experienced less than 1 ft of increase or decrease. There is a widespread increase in surge up to 6 ft across most of the degraded areas shown in Figure A.8-6a. The surge is increased by 1-3 ft in the Lake Maurepas region, 1-6 ft in St. John/St. Charles Parishes, and 1-3 ft east of Morgan City. Less than 1 ft change in surge occurs east of the MS River and surges are increased at the West Bank 1-2 ft. Figure A.8-7 shows the maximum wave heights differences for the restored configuration. Seaward of the east New Orleans levee system, waves are expected to increase by as much as 2 ft. Maximum wave heights are also expected to increase by up to 2 ft in the Crown Point vicinity. Note that the wave height differences west of the MRGO in St. Bernard Parish are consistent with the differences observed for the 2010 vs 2007 configurations, i.e. the CLEAR/NIA bathymetry is based on the 2010 grid so the predicted differences are due to the increased 2010 levee heights and not a result of the degraded marsh conditions.

- Figure A.8-5. Outline of CLEAR/NIA landscape changes.




---PAGE-246---



||a<br><br>Maurepas, Houma, and Atchafalaya|
|---|
<br><br>|b<br><br>West Bank and east of river|
|---|
<br><br>Degraded – 2007 Base Degraded – 2010 Base<br><br>|
|---|


- Figure A.8-6. Difference in maximum surge level (ft) between the CLEAR/NIA configuration and the 2007 and 2010 base cases for the NIA marsh storm suite.




---PAGE-247---



- Figure A.8-7. Difference in maximum wave height (ft) between the CLEAR/NIA configuration and the base case for the NIA marsh storm suite for the southeast STWAVE grid.


The restored condition was developed by ERDC-CHL under the direction of the New Orleans District’s improved action plan. The District provided CHL with marsh creation locations and type (i.e. freshwater, cypress swamp, saline, etc), freshwater diversion locations, and the volume of sediment diverted. CHL implemented these restoration features into a marsh creation program and modifications were made to the bathymetry, Manning’s n values, and directional roughness lengths. These changes were applied to the model grids, mesh, and frictional files and a series of storm simulations was made. Figure A.8-8 shows an outline of the marsh restoration features for eastern Louisiana. Figure A.8-9 is the difference in the envelope of maximum water level between the restored marsh configuration and the 2007 base case and the 2010 base case. As with the degraded case, comparison to two grids is required to isolate the impact of the wetland restoration. There is a reduction in surge west of the MS River bounded by Golden Meadow on the east and mid-Terrebonne Parish on the west ranging from 1-3 ft with the largest reduction (greater than 2 ft) east of the Houma Navigation Canal and south of Route 24. This region of attenuated surge corresponds with an area that has many restoration features. There is also an area of 1-3 ft surge reduction on the West Bank east of the GIWW. Less than 1 ft change in maximum surge occurs east of the MS River. Figure A.8-10 shows the maximum wave height differences for the restored configuration. Seaward of the east New Orleans levee system, the waves are not expected to change. Note that the wave height differences west of the MRGO in St. Bernard Parish are generally consistent with the differences observed for the 2010 vs 2007 configurations, i.e. the restored bathymetry is based on the 2010 grid so the predicted differences are likely due to the increased 2010 levee heights and not a result of the restored marsh conditions.



---PAGE-248---



###### Figure A.8-8. Outline of marsh restoration features. Marsh types are outlined as follows: 1 = saline, 2 = intermediate, 3 = brackish, 4 = fresh, 5 = cypress, white lines = ridges, purple = shrub/scrub for barrier islands.



---PAGE-249---



||West Bank and east of river|
|---|
<br><br>|Maurepas, Houma, and Atchafalaya|
|---|
<br><br>Restored – 2007 Base Restored – 2010 Base|
|---|


- Figure A.8-9. Difference in maximum surge level (ft) between the restored marsh configuration and the 2007 and 2010 base cases for the restored marsh storm suite.




---PAGE-250---



###### Figure A.8-10. Difference in maximum wave height (ft) between the restored marsh configuration and the base case for the restored marsh storm suite for the southeast STWAVE grid.



---PAGE-251---



###### A.8.2.1 Marsh Alternatives for LAWEST

The improved marsh scenario for western Louisiana changed maximum surge levels and wave heights by less than 1 ft. See Figures A.8-11 and A.8-12.

- Figure A.8-11. Difference in maximum surge level (ft) between the restored marsh configuration and the LAWEST base cases for the LAWEST restored marsh storm suite.




---PAGE-252---



- Figure A.8-12. Difference in maximum wave height (ft) between the restored marsh configuration and the LAWEST base case for the LAWEST restored marsh storm suite for the west STWAVE grid.


The impact of the future degraded landscape on peak surge levels and wave heights are given in Figures A.8-13 and A.8-14. The degraded landscape generally results in 1 to 2 ft increases in peak surges across western Louisiana with the exception of the Atchafalaya area. The future condition in this area is an improved landscape due to land building from the Atchafalaya River. Decreases in surges in this area are 1 to 3 ft. Maximum wave heights are also generally increased across west Louisiana. Some areas are greater experience greater than 1 ft change while others are less than a foot. In the Atchafalaya area, maximum wave height decreases are as much as 6 ft.



---PAGE-253---



###### Figure A.8-13. Difference in maximum surge level (ft) between the CLEAR/NIA configuration and the LAWEST base case for the LAWEST NIA marsh storm suite.

###### Figure A.8-14. Difference in maximum wave height (ft) between the CLEAR/NIA configuration and the LAWEST base case for the LAWEST NIA marsh storm suite for the west STWAVE grid.



---PAGE-254---



###### A.8.3 Sea Level Rise

Sea level rise and subsidence are significant issues in the design of flood protection for southeast Louisiana. Flood walls, in particular, can not be easily raised, so future sea level rise must be considered in the initial design. The purpose of this analysis is to estimate the impact of sea level rise on surge and waves for the design of the flood defenses.

The sea level rise analysis consisted of 27 storm simulations. Nine storms were selected from the 2010 simulations and each was run with 1 ft, 2 ft, and 3 ft increase in water level. No other changes to input were made (same offshore waves, same land cover specification, same model parameters, etc.). The storms were chosen to target 100-year water levels in various areas. To summarize the results, eleven reaches are defined: South Shore of Lake Pontchartrain (SSP), East Orleans (EO), St. Bernard North (SBN), St. Bernard South (SBS), Caernarvon (C), Plaquemines East (PE), Plaquemines West (PW), South West Bank (SWB), North West Bank (NWB), Golden Meadow (GM), and Morganza to the Gulf (MtG). These areas are illustrated in Figure A.8-9.

The selection of only nine storms that give approximate 100-yr water levels provides estimates of the impact of sea level rise, but is not a rigorous analysis. For example, land cover classifications were not changed in the analysis. Vegetation types would change as water level increases, but if the increase is slow enough and sediment is available, the marsh elevation may also adjust to the change in water level. Manning-n values were not adjusted in this analysis because of the uncertainty in the values for higher sea level and so the results at each water level could be directly compared. Sea level was increased over the entire domain, which means that local impacts of subsidence are probably over estimated. The impacts of increasing

sea level are two fold, the surge wave (which propagates at a speed, c = gd , were g is acceleration of gravity and d is water depth) propagates faster, and the depth-limited wave height increases (also increasing wave setup). In general, it is expected that sea level rise increases water levels more than linearly (water level increase > sea level rise), but the complex, shallow geometry and bathymetry of Southeast Louisiana alters this trend depending on the relative speed of the storm and the surge propagation (and the relative phasing of the two).

The surge increases are calculated as the difference between the maximum water level at each grid point for the sea level rise run and the maximum water level for the base 2007 run. Similarly, the wave increases are calculated as the difference between the maximum wave height at each grid point for the sea level rise run and the maximum wave height for the base 2007 run. Surge increases were normalized by the sea level rise and are presented as multipliers below.

South Shore of Lake Pontchartrain. The SSP reach has the most consistent response to sea level rise. The multiplier is 1.0 to 1.5 (1 would be a linear response, 1 ft sea level rise = 1 ft increase is water level) with an average value of 1.3 for the target storms. The increased depth decreases the friction, allowing more water to pile up on the shore. The SSP reach has fairly consistent increase in wave height for sea level rise: 0.6 ft for 1 ft sea level rise, 1.0 ft for 2 ft sea level rise, and 1.5 ft for 3 ft sea level rise. The ratio of wave height increase to water level increase for the target storms varies from 0.23 to 0.60, with an average value of 0.43. The values are relatively high because an increase in surge results in a direct increase in depthlimited wave height in most areas.



---PAGE-255---



South Shore Pontchartrain

East Orleans St. Bernard North

North West Bank South West Bank

St. Bernard South Caenarvon

Plaquemines East

Plaquemines West

Golden Meadow Morganza to the Gulf

Figure A.8-9. Reach Definitions.

Back Levees of East Orleans and St. Bernard North. The response in EO and SBN has slightly more variation than SSP, with a multiplier of 1.1 to 1.6. This area forms a small pocket in the funnel area, but the reach is not as complex or shallow as areas to the south and west. The multipliers for the storms near the 100-yr water level are 1.1 to 1.6 in EO and 1.2 to 1.6 in SBN, with average values of 1.2 and 1.3, respectively. The EO and SBN behave relatively consistently with increases in wave height of 0.1 to 1.2 ft for EO and 0.1 to 1.0 ft for SBN. The ratios of wave height increase to water level increase are all less than 0.4, with average values for the target storms of 0.13 (range of 0.06 to 0.31) for EO and 0.17 (range of 0.04 to 0.38) for SBN.

St. Bernard South and Caernarvon. This reach is complex and shallow, and the results are highly variable with multipliers of 0.7 to 4.5. The large responses correspond to the storms with some of the smallest maximum surges, which have tracks that cross through Breton Sound, east of this area. As the storms pass, the larger water depth allows the surge to move in faster, as well as decreasing the frictional resistance. The “catchers mitt” of Caernarvon amplifies the surge for these storms. Storms that produce the largest surge in these areas (20-25 ft) have a sea level rise multiplier of 0.6 to 1.3 for St. Bernard South and 0.6 to 2.0 for Caernarvon. Storms that produce the 100-yr water levels have multipliers of 0.7 to 2.3 for SBS and 0.7 to 4.5 for C with average values of 1.4 and 2.1, respectively. The wave height results are highly variable with increases of 0.1 to 2.1 ft for SBS and 0.5 to 3.0 ft for C. The large responses correspond to the storms with the smallest maximum surges with tracks that cross through Breton Sound, east of this area. As the storms pass, the larger water depth allows large waves to propagate into



---PAGE-256---



the area, as well as decreases the frictional resistance. The average ratio of wave height increase to water level increase is relatively large in this area, 0.45 (range of 0.4 to 0.5) for SBS

- and 0.50 (range of 0.42 to 0.63) for C. Plaquemines East and West. These reaches are large with a lot of spatial variability, but the multipliers are less variable than the adjoining reaches. The multipliers for the target storms are 1.3 to 2.0 for Plaquemines East. For the Plaquemines West reach, the range of multipliers for the target storms is 1.4 to 3, with average values of 1.5 and 1.9, respectively. The wave height increases in these areas are similar to St. Bernard South and Caernarvon. The wave height increases are 0.4 to 2.8 ft for PE and 0.4 to 2.9 ft for PW. The maximum increases in wave height in the Plaquemines East reach were typically at the north end of this reach, between Phoenix and Davant. The average ratio of wave height increase to water level increase is 0.58 (range 0.38 to 0.78) for the target storms for PE. For the Plaquemines West reach, the maximum increases in wave height were typically between Empire and Buras or near Myrtle Grove. The average ratio of wave height increase to water level increase is 0.41 (range 0.23 to 0.69) for the target storms for PE. West Bank. This reach is also complex and shallow. The multipliers range from 1.0 to 3.6. Storms near the 100-yr level for the West Bank have multipliers ranging from 1.3 to 3.6 for SWB

- and 1.0 to 2.9 for NWB. The largest numbers tend to be hot spots (small areas) and not large areas of high multipliers. The average multipliers for the target storms are 2.5 for SWB and 2.1 for NWB. The wave height increases are 0.1 to 1.0 ft. The ratio of wave height increase to water level increase is 0.03 to 0.3 for the target storms with average values of 0.11 for SWB and 0.15 for NWB.


Golden Meadow and Morganza to the Gulf. Multipliers in this reach are similar to the West Bank, but not as variable. Multipliers range from 1.0 to 2.5. The surges tend to be most amplified on the northeast corner of Golden Meadow and in the pocket regions. The multipliers for the storms near the 100-yr water level are 1.4 to 2.3 for Golden Meadow and 1.5 to 2.0 for Morganza to the Gulf, with average values of 1.8 and 1.7, respectively. These reaches include complex levee geometries (pockets) and bathymetry, but are more exposed than the west bank. The wave height increases are up to 2.0 ft along Golden Meadow and up to 3.0 ft along Morganza to the Gulf. The average ratio of wave height increase over surge increase for the target storms is 0.27 (range 0.14 to 0.42) for Golden Meadow and 0.37 (range 0.23 to 0.5) for Morganza to the Gulf.



---PAGE-257---



###### Annex B Fact sheets for sub basins



---PAGE-258---



###### LIST OF FIGURES

- Figure B.1–Sub-basin and levees Laplace (High Level and Barrier Plan)..................................................................1
- Figure B.2 – Stage storage relationship Laplace........................................................................................................2
- Figure B.3 – Sub-basin and levees St Charles Norco (High Level and Barrier Plan) .................................................4
- Figure B.4 – Stage storage relationship St Charles Norco .........................................................................................5
- Figure B.5 – Sub-basin and levees St. Charles Remainder (High Level and Barrier Plan) ........................................6
- Figure B.6 – Stage storage relationship St Charles Remainder .................................................................................7
- Figure B.7 – Sub-basin and levees East Jefferson (High Level and Barrier Plan)......................................................8
- Figure B.8 – Stage storage relationship East Jefferson .............................................................................................9
- Figure B.9 – Sub-basin and levees New Orleans Metro (High Level and Barrier Plan)............................................10
- Figure B.10 – Stage storage relationship New Orleans Metro..................................................................................11
- Figure B.11 – Sub-basin and levees New Orleans East (High Level and Barrier Plan)............................................12
- Figure B.12 – Stage storage relationship New Orleans East....................................................................................13
- Figure B.13 – Sub-basin and levees St Bernard Wetland (High Level and Barrier Plan) .........................................14
- Figure B.14 – Stage storage relationship St Bernard Wetland .................................................................................15
- Figure B.15 – Sub-basin and levees St Bernard Developed (High Level and Barrier Plan) .....................................16
- Figure B.16 – Stage storage relationship St Bernard Developed .............................................................................17
- Figure B.17 – Sub-basin and levees Plaquemines - Scarsdale (High Level and Barrier Plan).................................18
- Figure B.18 – Stage storage relationship Plaquemines - Scarsdale.........................................................................19
- Figure B.19 – Sub-basin and levees Madisonville (High Level and Barrier Plan).....................................................21
- Figure B.20 – Stage storage relationship Madisonville.............................................................................................22
- Figure B.21 – Sub-basin and levees South Covington (High Level and Barrier Plan)..............................................24
- Figure B.22 – Stage storage relationship South Covington......................................................................................25
- Figure B.23 – Sub-basin and levees Madisonville to Mandeville (High Level and Barrier Plan)...............................28
- Figure B.24 – Stage storage relationship Madisonville to Mandeville.......................................................................29
- Figure B.25 – Sub-basin and levees Mandeville (High Level and Barrier Plan) .......................................................31
- Figure B.26 – Stage storage relationship Mandeville ...............................................................................................32
- Figure B.27 – Sub-basin and levees West Lacombe (High Level and Barrier Plan).................................................34
- Figure B.28 – Stage storage relationship West Lacombe.........................................................................................35
- Figure B.29 – Sub-basin and levees East Lacombe (High Level and Barrier Plan)..................................................37
- Figure B.30 – Stage storage relationship East Lacombe..........................................................................................38
- Figure B.31 – Sub-basin and levees Slidell (High Level and Barrier Plan)...............................................................40
- Figure B.32 – Stage storage relationship Slidell.......................................................................................................41
- Figure B.33 – Sub-basin and levees Algiers (High Level and Barrier Plan)..............................................................44
- Figure B.34 – Stage storage relationship Algiers .....................................................................................................45
- Figure B.35– Sub-basin and levees English Turn (High Level and Barrier Plan) .....................................................46
- Figure B.36 – Stage storage relationship English Turn ............................................................................................47
- Figure B.37 – Sub-basin and levees Plaquemaines Belle Chase (High Level and Barrier Plan)..............................48
- Figure B.38 – Stage storage relationship Plaquemaines Belle Chase .....................................................................49
- Figure B.39 – Sub-basin and levees West Jefferson – East of Harvey (High Level and Barrier Plan) .....................50
- Figure B.40 – Stage storage relationship West Jefferson – East of Harvey .............................................................51
- Figure B.41 – Sub-basin and levees West Jefferson – Harvey (High Level and Barrier Plan) .................................52
- Figure B.42 – Stage storage relationship West Jefferson – Harvey .........................................................................53
- Figure B.43 – Sub-basin and levees West Jefferson – Ames (High Level and Barrier Plan)....................................54
- Figure B.44 – Stage storage relationship West Jefferson – Ames ...........................................................................55
- Figure B.45– Sub-basin and levees West Jefferson – Segnette (High Level and Barrier Plan) ...............................56
- Figure B.46 – Stage storage relationship West Jefferson – Segnette ......................................................................57
- Figure B.47 – Sub-basin and levees St Charles – Davis Pond (High Level and Barrier Plan)..................................58
- Figure B.48 – Stage storage relationship St Charles – Davis Pond .........................................................................59




---PAGE-259---



- Figure B.49 – Sub-basin and levees St Charles - Lulling (High Level and Barrier Plan) ..........................................60
- Figure B.50 – Stage storage relationship St Charles - Lulling ..................................................................................61
- Figure B.51 – Sub-basin and levees St Charles - Sunset (High Level and Barrier Plan) .........................................62
- Figure B.52 – Stage storage relationship St Charles - Sunset .................................................................................63
- Figure B.53 – Sub-basin and levees Lockport (High Level and Barrier Plan)...........................................................64
- Figure B.54 – Stage storage relationship Lockport...................................................................................................65
- Figure B.55 – Sub-basin and levees Larose to Golden Meadow (High Level and Barrier Plan)...............................66
- Figure B.56 – Stage storage relationship Larose to Golden Meadow ......................................................................67
- Figure B.57 – Sub-basin and levees Morganza_no_ret_ring....................................................................................69
- Figure B.58 – Stage storage relationship for Morganza no ret ring ..........................................................................70
- Figure B.59 – Sub-basin and levees East_of_Morgan_City_ring .............................................................................71
- Figure B.60 – Stage storage relationship for East_of_Morgan_City_ring.................................................................72
- Figure B.61 – Sub-basin and levees Morganza_with_ret_ring .................................................................................73
- Figure B.62 – Stage storage relationship for Morganza with ret ring........................................................................74
- Figure B.63 – Sub-basin and levees Morganza_with_ret_ring_m_only....................................................................75
- Figure B.64 – Stage storage relationship for Morganza_with_ret_ring_m_only .......................................................76
- Figure B.65 – Sub-basin and levees Morganza_back_levee....................................................................................77
- Figure B.66 – Stage storage relationship for Morganza_back_levee .......................................................................78
- Figure B.67 – Sub-basin and levees Morgan_City_ring ...........................................................................................79
- Figure B.68 – Stage storage relationship for Morgan City........................................................................................80
- Figure B.69 – Sub-basin and levees South_of_Franklin_ring...................................................................................81
- Figure B.70 – Stage storage relationship for South_of_Franklin_ring ......................................................................82
- Figure B.71 – Sub-basin and levees GIWW_PU3b_ring ..........................................................................................83
- Figure B.72 – Stage storage relationship for GIWW_PU3b_ring..............................................................................84
- Figure B.73 – Sub-basin and levees Patterson ........................................................................................................85
- Figure B.74 – Stage storage relationship for Patterson............................................................................................86
- Figure B.75 – Sub-basin and levees Abbeville_to_Delcambre_ring.........................................................................87
- Figure B.76 – Stage storage relationship for Abeville_to_Delcambre_ring...............................................................88
- Figure B.77 – Sub-basin and levees New_Iberia_ring .............................................................................................89
- Figure B.78 – Stage storage relationship for New_Iberia_ring .................................................................................90
- Figure B.79 – Sub-basin and levees Charenton_ring...............................................................................................91
- Figure B.80 – Stage storage relationship for Charenton_ring...................................................................................92
- Figure B.81 – Sub-basin and levees Abbeville.........................................................................................................93
- Figure B.82 – Stage storage relationship for Abbeville.............................................................................................94
- Figure B.83 –Sub-basin and levees Erath................................................................................................................95
- Figure B.84 – Stage storage relationship for Erath...................................................................................................96
- Figure B.85 – Sub-basin and levees Delcambre ......................................................................................................97
- Figure B.86 – Stage storage relationship for Delcambre..........................................................................................98
- Figure B.87 – Sub-basin and levees New_Iberia .....................................................................................................99
- Figure B.88 – Stage storage relationship for New_Iberia .......................................................................................100
- Figure B.89 – Sub-basin and levees Baldwin.........................................................................................................101
- Figure B.90 – Stage storage relationship for Baldwin.............................................................................................102
- Figure B.91 – Sub-basin and levees Franklin.........................................................................................................103
- Figure B.92 – Stage storage relationship for Franklin ............................................................................................104
- Figure B.93 – Sub-basin and levees Central_PU4_ring.........................................................................................105
- Figure B.94 – Stage storage relationship for Central_PU4_ring.............................................................................106
- Figure B.95 – Sub-basin and levees GIWW_to_Veterans_ring..............................................................................107
- Figure B.96 – Stage storage relationship for GIWW_to_Veterans_ring .................................................................108
- Figure B.97 – Sub-basin and levees South_of_Lake_Charles_ring .......................................................................109
- Figure B.98 – Stage storage relationship for South_of_Lake_Charles_ring...........................................................110




---PAGE-260---



- Figure B.99 – Sub-basin and levees West_Lake_Charles .....................................................................................111
- Figure B.100 – Stage storage relationship for West_Lake_Charles.......................................................................112
- Figure B.101 – Sub-basin and levees Prien ...........................................................................................................113
- Figure B.102 – Stage storage relationship for Prien...............................................................................................114
- Figure B.103 – Sub-basin and levees Inner_Lake_Charles ...................................................................................115
- Figure B.104 – Stage storage relationship for Inner_Lake_Charles.......................................................................116
- Figure B.105 – Sub-basin and levees South_of_Lake_Charles_ring_12 ...............................................................117
- Figure B.106 – Stage storage relationship for South_of_Lake_Charles_ring_12...................................................118
- Figure B.107 – Sub-basin and levees Central_PU4_ring_large_12 .......................................................................119
- Figure B.108 – Stage storage relationship for Central_PU4_ring_large_12...........................................................120
- Figure B.109 – Sub-basin and levees GIWW_to_Veterans_ring_large_12............................................................121
- Figure B.110 – Stage storage relationship for GIWW_to_Vetterans_ring_large_12...............................................122
- Figure B.111 – Sub-basin and levees East_Lake_Charles ....................................................................................123
- Figure B.112 – Stage storage relationship for East_Lake_Charles........................................................................124
- Figure B.113 – Sub-basin and levees Gueydan.....................................................................................................125
- Figure B.114 – Stage storage relationship for Gueydan.........................................................................................126
- Figure B.115 – Sub-basin and levees Kaplan ........................................................................................................127
- Figure B.116 – Stage storage relationship for Kaplan............................................................................................128 LIST OF TABLES


- Table B-1 – Levee characteristics Laplace.................................................................................................................2
- Table B-2 – Levee characteristics St Charles Norco..................................................................................................5
- Table B-3 – Levee characteristics St. Charles Remainder .........................................................................................7
- Table B-4 – Levee characteristics East Jefferson ......................................................................................................9
- Table B-5 – Levee characteristics New Orleans Metro.............................................................................................11
- Table B-6 – Levee characteristics New Orleans East ..............................................................................................13
- Table B-7 – Levee characteristics St Bernard Wetland............................................................................................15
- Table B-8 – Levee characteristics St Bernard Developed ........................................................................................17
- Table B-9 – Levee characteristics Plaquemines - Scarsdale....................................................................................19
- Table B-10 – Levee characteristics Madisonville......................................................................................................22
- Table B-11 – Levee characteristics South Covington...............................................................................................25
- Table B-12 – Levee characteristics Madisonville to Mandeville................................................................................29
- Table B-13 – Levee characteristics Mandeville ........................................................................................................32
- Table B-14 – Levee characteristics West Lacombe .................................................................................................35
- Table B-15 – Levee characteristics East Lacombe ..................................................................................................38
- Table B-16 – Levee characteristics Slidell................................................................................................................41
- Table B-17 – Levee characteristics Algiers ..............................................................................................................44
- Table B-18 – Levee characteristics English Turn .....................................................................................................46
- Table B-19 – Levee characteristics Plaquemaines Belle Chase ..............................................................................49
- Table B-20 – Levee characteristics West Jefferson – East of Harvey......................................................................51
- Table B-21 – Levee characteristics West Jefferson - Harvey...................................................................................53
- Table B-22 – Levee characteristics West Jefferson – Ames ....................................................................................55
- Table B-23 – Levee characteristics West Jefferson – Segnette ...............................................................................57
- Table B-24 – Levee characteristics St Charles – Davis Pond ..................................................................................59
- Table B-25 – Levee characteristics St Charles – Lulling ..........................................................................................61
- Table B-26 – Levee characteristics St Charles – Sunset..........................................................................................63
- Table B-27 – Levee characteristics Lockport............................................................................................................65
- Table B-28 – Levee characteristics Larose to Golden Meadow ...............................................................................67
- Table B-29 – Levee characteristics Morganza_no_ret_ring .....................................................................................69




---PAGE-261---



- Table B-30 – Levee characteristics East of Morgan_City_ring.................................................................................71
- Table B-31 – Levee characteristics Morganza_with_ret_ring...................................................................................73
- Table B-32 – Levee characteristics Morganza_with_ret_ring_m_only .....................................................................75
- Table B-33 – Levee characteristics Morganza_back_levee .....................................................................................77
- Table B-34 – Levee characteristics Morgan_City_ring.............................................................................................79
- Table B-35 – Levee characteristics South_of_Franklin_ring ....................................................................................81
- Table B-36 – Levee characteristics GIWW_PU3b_ring............................................................................................83
- Table B-37 – Levee characteristics Patterson..........................................................................................................85
- Table B-38 – Levee characteristics Abbeville_to_Delcambre_ring...........................................................................87
- Table B-39 – Levee characteristics New_Iberia_rign ...............................................................................................89
- Table B-40 – Levee characteristics Chareton_ring...................................................................................................91
- Table B-41 – Levee characteristics Abbeville...........................................................................................................93
- Table B-42 – Levee characteristics Erath.................................................................................................................95
- Table B-43 – Levee characteristics Delcambre........................................................................................................97
- Table B-44 – Levee characteristics New_Iberia .......................................................................................................99
- Table B-45 – Levee characteristics Baldwin...........................................................................................................101
- Table B-46 – Levee characteristics Franklin...........................................................................................................103
- Table B-47 – Levee characteristics Central_PU4_ring...........................................................................................105
- Table B-48 – Levee characteristics GIWW_to_Veterans_ring................................................................................107
- Table B-49 – Levee characteristics South_of_Lake_Charles_ring.........................................................................109
- Table B-50 – Levee characteristics West_Lake_Charles .......................................................................................111
- Table B-51 – Levee characteristics Prien...............................................................................................................113
- Table B-52 – Levee characteristics Inner_Lake_Charles .......................................................................................115
- Table B-53 – Levee characteristics South_of_Lake_Charles_ring_12...................................................................117
- Table B-54 – Levee characteristics Central_PU4_ring_large_12...........................................................................119
- Table B-55 – Levee characteristics GIWW_to_Veterans_ring_large_12................................................................121
- Table B-56 – Levee characteristics East_Lake_Charles ........................................................................................123
- Table B-57 – Levee characteristics Gueydan.........................................................................................................125
- Table B-58 – Levee characteristics Kaplan ............................................................................................................127




---PAGE-262---



###### Planning Unit 1

Laplace

- Figure B.1–Sub-basin and levees Laplace (High Level and Barrier Plan)




---PAGE-263---



- Table B-1 – Levee characteristics Laplace


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0176|27.3|n.a.|13.5|18.5|21|12.5|17|19|
|-|-|-|-|-|-|-|-|-|
|-|-|-|-|-|-|-|-|-|


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0176|27.3|n.a.|9|14.5|18|8|13|16|
|-|-|-|-|-|-|-|-|-|
|-|-|-|-|-|-|-|-|-|


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|0|10,000|Based on 0.5cfs/acre|


|Storage Area|Type|Notes|
|---|---|---|
|Laplace|Single area|Max stage is higher of surge (176) or design height (176)|


Stage-storage relationship

20

| |
|---|
| |
| |
|50000 100000 150000 200000 250000|
| |


15

10

5

Stage[ft]

0

0 300000

-5

- -15
- -10


Storage [acre ft]

- Figure B.2 – Stage storage relationship Laplace




---PAGE-264---



Additional Notes

Pumping needs to be included based on the basis of 0.5cfs/acreas as development is close behind the proposed levee line. Area taken as 21000 acres and therefore assumed 10,000cfs.

A new alignment for the levee in Laplace has been suggested from a different study. At present for consistency - the original alignment is being maintained, but reference will be made in the final documentation to the new alignments. Pump sizing has also been undertaken for both the existing and new alignments by the other project. For the existing alignment a value of 3500cfs has been developed against the 10,000cfs suggested in above. For consistency the 10,000cfs value has been used.

Initial economic runs suggested that significantly more people were affected with a levee than without. This appears to be a result of the planning sub units finishing short of the actual flood extents, therefore suggesting in the without case that some property is outside the flood extent whereas they are below the extreme surge elevations (for the higher events). To solve this exterior stage frequency values were taken from the existing planning sub units and applied to the interior units in this area. The relationships were:

- Laplace 1 - exterior values from SJJO_8c
- Laplace 2 - exterior values from STCH_11b




---PAGE-265---



St. Charles Norco

- Figure B.3 – Sub-basin and levees St Charles Norco (High Level and Barrier Plan)




---PAGE-266---



- Table B-2 – Levee characteristics St Charles Norco


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0032|4.3|13|16|21|23.5|14.5|19.5|21.5|
|-|-|-|-|-|-|-|-|-|


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0032|4.3|13|16(1)|18.5|21.5|16(1)|17|19.5|
|-|-|-|-|-|-|-|-|-|


Note (1) Height fixed equal to High Level Plan 100 year as this should have been implemented.

| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|800|800| |


|Storage Area|Type|Notes|
|---|---|---|
|St Charles - Norco|Linked area (St Charles)|Connects to St Charles - rest (4.5’). See description of linked system in chapter 4.|


Stage-storage relationship

20

| |
|---|
| |
| |
|5000 10000 15000 20000 25000|
| |


15

10

5

Storage [acre ft] Stage[ft]

0

0

-5

- -15
- -10


###### Figure B.4 – Stage storage relationship St Charles Norco



---PAGE-267---



###### St Charles Remainder

- Figure B.5 – Sub-basin and levees St. Charles Remainder (High Level and Barrier Plan)




---PAGE-268---



- Table B-3 – Levee characteristics St. Charles Remainder


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0032|4.2|13|16|21|23.5|14.5|19.5|21.5|
|-|-|-|-|-|-|-|-|-|


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0032|4.2|13|16(1)|18.5|21.5|16(1)|17|19.5|
|-|-|-|-|-|-|-|-|-|


Note (1) Height fixed equal to High Level Plan 100 year as this should have been implemented.

| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|0|0| |


|Storage Area|Type|Notes|
|---|---|---|
|St Charles - Rest|Linked area (St Charles)|Connects to St Charles - Norco (4.5’). See description of linked system in chapter 4.|


Stage-storage relationship

20

| |
|---|
| |
| |
| |
|20000 40000 60000 80000 100000 120000 140000 160000|
| |


15

10

5

Storage [acre ft] Stage[ft]

0

0 180000

-5

- -15
- -10


###### Figure B.6 – Stage storage relationship St Charles Remainder



---PAGE-269---



East Jefferson

- Figure B.7 – Sub-basin and levees East Jefferson (High Level and Barrier Plan)




---PAGE-270---



- Table B-4 – Levee characteristics East Jefferson


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0032|4.0|13|16|21|23.5|14.5|19.5|21.5|
|BS-0092|10.0|16.5|16.5|19.5|21.5|16.5|19.5|21.5|


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0032|4.0|13|16(1)|18.5|21.5|16(1)|17|19.5|
|EB-0092|10.0|16.5|16.5|16.5|18.5|16.5|16.5|18.5|


Note (1) Height fixed equal to High Level Plan 100 year as this should have been implemented.

| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|20,590|20,590| |


|Storage Area|Type|Notes|
|---|---|---|
|East Jefferson|Linked area (New Orleans)|Connects to NO Metro with a weir at 5’. If stage < 5’ then likely only floods to this level. See description of linked system in chapter 4|


Stage-storage relationship

20

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


15

10

5

Storage [acre ft] Stage[ft]

0

0 100000 200000 300000 400000 500000 600000

-5

- -15
- -10


- Figure B.8 – Stage storage relationship East Jefferson




---PAGE-271---



- New Orleans Metro
- Figure B.9 – Sub-basin and levees New Orleans Metro (High Level and Barrier Plan)




---PAGE-272---



- Table B-5 – Levee characteristics New Orleans Metro


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0026|6.1|18.5|18.5|20|23.5|18.5|20|23.5|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0026|6.1|18.5|18.5|18.5|18.5|18.5|18.5|18.5|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|26,160|26,160| |


|Storage Area|Type|Notes|
|---|---|---|
|NO Metro|Linked area (New Orleans)|Connects to East Jefferson (5’), St Bernard (12.5’) and NOE (12.5’). See description of linked system in chapter 4|


Stage-storage relationship

20

15

10

5

Storage [acre ft] Stage[ft]

0

0 100000 200000 300000 400000 500000 600000

-5

- -15
- -10


- Figure B.10 – Stage storage relationship New Orleans Metro




---PAGE-273---



- New Orleans East
- Figure B.11 – Sub-basin and levees New Orleans East (High Level and Barrier Plan)




---PAGE-274---



- Table B-6 – Levee characteristics New Orleans East


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0040|8.4|15|18|23.5|26|17.5|23|26|
|BS-0048|4.4|18|28.5|35|38|24|30|32|
|BS-0058|6.1|15|15|18|21|15|18|21|
|BS-0093|6.2|18|18|19|21.5|18|19|21.5|


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0058|6.3|15|15|15|15|15|15|15|
|EB-0093|6.2|18|18|18|18|18|18|18|
|EB-0129|4.4|18|28.5(1)|33.5|37|26.5|33.5|37|
|EB-0147|8.4|15|18(1)|16.5|20.5|17.5(1)|16.5|20|


Note (1) Height fixed equal to High Level Plan 100 year as this should have been implemented.

| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|6,310|6,310| |


|Storage Area|Type|Notes|
|---|---|---|
|NOE|Linked area (New Orleans)|Connects to NO Metro with a weir at 12.5’. If stage <12.5’ then likely floods to this level. See description of linked system in chapter 4|


Stage-storage relationship

20

15

10

5

Stage[ft]

0

0 100000 200000 300000 400000 500000 600000 700000 800000

-5

- -15
- -10


Storage [acre ft]

###### Figure B.12 – Stage storage relationship New Orleans East



---PAGE-275---



St Bernard Wetland

- Figure B.13 – Sub-basin and levees St Bernard Wetland (High Level and Barrier Plan)




---PAGE-276---



- Table B-7 – Levee characteristics St Bernard Wetland


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0005|11.8|18|26.5|32.5|35.5|24|29.5|32|
|BS-0007|2.0|17|26|34|38|21.5|28|31.5|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0007|2.0|17|28|37.5|40.5|23|30.5|35|
|EB-0129|11.8|18|26.5|33.5|37|26.5|33.5|37|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|0|0| |


|Storage Area|Type|Notes|
|---|---|---|
|St Bernard Wetland|Linked area (New Orleans)|Connects to St Bernard Developed at 10.5’. If stage <10.5’ then likely only floods to this level. See description of linked system in chapter 4|


Stage-storage relationship

20

| |
|---|
| |
| |
|100000 200000 300000 400000 500000|
| |
| |


15

10

5

Stage[ft]

0

0 600000

-5

- -15
- -10


Storage [acre ft]

###### Figure B.14 – Stage storage relationship St Bernard Wetland



---PAGE-277---



St Bernard Developed

- Figure B.15 – Sub-basin and levees St Bernard Developed (High Level and Barrier Plan)




---PAGE-278---



- Table B-8 – Levee characteristics St Bernard Developed


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0007|8.8|17|26|34|38|21.5|28|31.5|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0007|8.8|17|28|37.5|40.5|23|30.5|35|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|8,190|8,190|Pumps assumed to pump out of system rather than into St Bernard Wetland|


|Storage Area|Type|Notes|
|---|---|---|
|St Bernard Developed|Linked area (New Orleans)|Connects to St Bernard Wetland (10.5’) and NO Metro (12.5’). See description of linked system in chapter 4.|


Stage-storage relationship

20

| |
|---|
| |
| |
|50000 100000 150000 200000 250000 300000 350000|
| |
| |


15

10

5

Storage [acre ft] Stage[ft]

0

0

-5

- -15
- -10


- Figure B.16 – Stage storage relationship St Bernard Developed




---PAGE-279---



- Plaquemines - Scarsdale
- Figure B.17 – Sub-basin and levees Plaquemines - Scarsdale (High Level and Barrier Plan)




---PAGE-280---



- Table B-9 – Levee characteristics Plaquemines - Scarsdale


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0009|12.0|n.a.|29|38.5|42.5|24|31|35|
| | | | | | | | | |
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0009|12.3|n.a.|33|42.5|45.5|25.5|34.5|40|
| | | | | | | | | |
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|1,780|1,780| |


|Storage Area|Type|Notes|
|---|---|---|
|Plaquemines Scarsdale|Single area|Max height is higher of surge (9) or design height (9) - upper level is also capped at 18’ as the outflow level into the Mississippi River|


Stage-storage relationship

20

15

10

5

Stage[ft]

0

0 20000 40000 60000 80000 100000 120000 140000 160000

-5

- -15
- -10


Storage [acre ft]

- Figure B.18 – Stage storage relationship Plaquemines - Scarsdale




---PAGE-281---



Additional Notes

Limit of flood depth will be based on the MRT levees rather than the hurricane protection - taken as 18’ as an upper limit.



---PAGE-282---



Madisonville

- Figure B.19 – Sub-basin and levees Madisonville (High Level and Barrier Plan)




---PAGE-283---



- Table B-10 – Levee characteristics Madisonville


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0136|6.6|n.a.|16|20|22|16|20|22|


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0136|6.6|n.a.|11|15.5|17.5|11|15.5|17.5|


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|0|5,000|Based on 1cfs/acre|


|Storage Area|Type|Notes|
|---|---|---|
|Madisonville|Single area|Max stage is higher of surge (136) or design height (136).|


Stage-storage relationship

30

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


25

20

Stage[ft]

15

10

5

0

0 5000 10000 15000 20000 25000 30000 35000 40000 45000 50000

Storage [acre ft]

- Figure B.20 – Stage storage relationship Madisonville




---PAGE-284---



Additional Notes

The Lidar levels on the North Shore show very low levels and the storage curves would extend to well below 0 datum. It has been decided to assume that there is no storage available below 3’ in all areas on the North shore when levees are to be constructed. The stage storage relationships used in the calculations have been amended to this for both the high level and barrier plans and this is the curve shown in the graph above.

The location of the levee has resulted in only a small area of storage adjacent to the proposed levees, and as such the degree of pumping has been increased to compensate for this, compared with the levels of pumping assumed in the central New Orleans area where the drainage channels and roads absorb much more of the initial flooding. For the North Shore a rate of 1cfs/acre has been adopted.

The areas for calculating rainfall volumes have been derived by looking at the natural topography and estimating the drainage area. No allowance has been made for man-made drainage routes which may affect the total volumes within a particular area.

Much of the proposed levee system is not likely to be subject to wave action as it extends along the banks of the major tributaries draining into Lake Pontchartrain. Only the levees facing the Lake have been used within the overtopping calculations. The overtopping lengths are indicated on the plans at the start of the section and the lengths are indicated here:

| |High Level Plan| | | |Barrier Plan| | | |
|---|---|---|---|---|---|---|---|---|
| |BS-0136 (miles)| | | |EB-0136 (miles)| | | |
|Overtopping|4.1| | | |4.1| | | |
|Non-overtopping|2.5| | | |2.5| | | |




---PAGE-285---



South Covington

- Figure B.21 – Sub-basin and levees South Covington (High Level and Barrier Plan)




---PAGE-286---



- Table B-11 – Levee characteristics South Covington


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0136|3.0|n.a.|13.6|16|17.4|16|20|22|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0136|3.0|n.a.|11|15.5|17.5|11|15.5|17.5|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|0|1,600|Based on 1cfs/acre|


|Storage Area|Type|Notes|
|---|---|---|
|South Covington|Single area|Max height is higher of surge (136) or design height (136)|


Stage-storage relationship

30

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


25

20

Storage [acre ft] Stage[ft]

15

10

5

0

0 2000 4000 6000 8000 10000 12000 14000 16000 18000 20000

- Figure B.22 – Stage storage relationship South Covington




---PAGE-287---



Additional Notes

The Lidar levels on the North Shore show very low levels and the storage curves would extend to well below 0 datum. It has been decided to assume that there is no storage available below 3’ in all areas on the North shore when levees are to be constructed. The stage storage relationships used in the calculations have been amended to this for both the high level and barrier plans and this is the curve shown in the graph above.

The location of the levee has resulted in only a small area of storage adjacent to the proposed levees, and as such the degree of pumping has been increased to compensate for this, compared with the levels of pumping assumed in the central New Orleans area where the drainage channels and roads absorb much more of the initial flooding. For the North Shore a rate of 1cfs/acre has been adopted.

The areas for calculating rainfall volumes have been derived by looking at the natural topography and estimating the drainage area. No allowance has been made for man-made drainage routes which may affect the total volumes within a particular area.

None of the proposed levee system is likely to be subject to wave action as it is inland and protected from wave action buy other levees. Levee heights and internal flooding has therefore been developed by using a simple weiring process. The process and the results are given below.

It was decided to use the 90% surge level plus 3’ as the design basis rather than using the levee height from the lakefront.

High Level (BS)

This results in the following levee heights

100 year 13.6’ (10.6’ surge +3’) 400 year 16’ (13’ surge + 3’) 1000 year 17.4’ (14.4’ surge + 3’)

The highest water level (2000yr 90%) is 15.2’. Therefore there is no significant overtopping of the 400 or 1000 year defenses and therefore only rainfall contributes to flooding.

At 100 year the 1000yr/90% and 2000yr/90% exceed the levee level and would cause additional flooding.

- The peak overflow height would be 0.8’ for the 1000/90 and 1.6’ for the 2000/90


Overflow rates are the order of 2.4cfs/ft for 1000/90 and 6.7cfs/ft for 2000/90. This is a peak value and would only apply for a short time.

The time of overtopping has been established by developing a surge hydrograph and cutting the hydrograph at the levee height. Overtopping has been taken as occurring linearly from zero to peak and back again and an approximate volume of overtopping can be established using this assumption.



---PAGE-288---



Time for 1000/90 above 13.6’ is 240 mins. Therefore volume of overtopping is approx. 3151 acreft which equates to a flood level of 12.75’ (nearly full to levee level)

Time for 2000/90 above 13.6’ is 340 mins. This equates to a volume of approx. 25000 acre ft - this is full to surge level of 15.2’

Barrier Plan (EB)

This results in the following levee heights

100 year 10.3’ (7.3’ surge +3’) 400 year 12.8’ (9.8’ surge + 3’) 1000 year 14.1’ (11.1’ surge + 3’)

The highest water level (2000yr 90%) is 12.0’. Therefore there is no significant overtopping of the 400 or 1000 year defenses and therefore only rainfall contributes to flooding.

At 100 year the 1000yr/90% and 2000yr/90% exceed the levee level and would cause additional flooding.

- The peak overflow height would be 0.8’ for the 1000/90 and 1.7’ for the 2000/90


The time of overtopping has been established by developing a surge hydrograph and cutting the hydrograph at the levee height. Overtopping has been taken as occurring linearly from zero to peak and back again and an approximate volume of overtopping can be established using this assumption.

Time for 1000/90 above 10.3’ is 150 mins. Therefore volume of overtopping is approx. 3938 acre ft - this is full to surge level of 11.1’ Time for 2000/90 above 13.6’ is 220 mins. This equates to a volume of approx. 17900 acre ft - this is full to surge level of 12.0’



---PAGE-289---



Madisonville to Mandeville

- Figure B.23 – Sub-basin and levees Madisonville to Mandeville (High Level and Barrier Plan)




---PAGE-290---



- Table B-12 – Levee characteristics Madisonville to Mandeville


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0136|11.5|n.a.|16|20|22|16|20|22|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0136|11.5|n.a.|11|15.5|17.5|11|15.5|17.5|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|0|5,600|Based on 1cfs/acre|


|Storage Area|Type|Notes|
|---|---|---|
|Madisonville to Mandeville|Single area|Max stage is higher of surge (136) or design height (136)|


Stage-storage relationship

30

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


25

20

Storage [acre ft] Stage[ft]

15

10

5

0

0 10000 20000 30000 40000 50000 60000 70000 80000

- Figure B.24 – Stage storage relationship Madisonville to Mandeville




---PAGE-291---



Additional Notes

The Lidar levels on the North Shore show very low levels and the storage curves would extend to well below 0 datum. It has been decided to assume that there is no storage available below 3’ in all areas on the North shore when levees are to be constructed. The stage storage relationships used in the calculations have been amended to this for both the high level and barrier plans and this is the curve shown in the graph above.

The location of the levee has resulted in only a small area of storage adjacent to the proposed levees, and as such the degree of pumping has been increased to compensate for this, compared with the levels of pumping assumed in the central New Orleans area where the drainage channels and roads absorb much more of the initial flooding. For the North Shore a rate of 1cfs/acre has been adopted.

The areas for calculating rainfall volumes have been derived by looking at the natural topography and estimating the drainage area. No allowance has been made for man-made drainage routes which may affect the total volumes within a particular area.

Much of the proposed levee system is not likely to be subject to wave action as it extends along the banks of the major tributaries draining into Lake Pontchartrain. Only the levees facing the Lake have been used within the overtopping calculations. The overtopping lengths are indicated on the plans at the start of the section and the lengths are indicated here:

| |High Level Plan| | | |Barrier Plan| | | |
|---|---|---|---|---|---|---|---|---|
| |BS-0136 (miles)| | | |EB-0136 (miles)| | | |
|Overtopping|4.1| | | |4.1| | | |
|Non-overtopping|7.4| | | |7.4| | | |




---PAGE-292---



Mandeville

- Figure B.25 – Sub-basin and levees Mandeville (High Level and Barrier Plan)




---PAGE-293---



- Table B-13 – Levee characteristics Mandeville


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0137|9.2|n.a.|15|19|21.5|15|19|21.5|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0137|9.2|n.a.|9.5|13.5|16|9.5|13.5|16|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|0|5,200|Based on 1cfs/acre|


|Storage Area|Type|Notes|
|---|---|---|
|Mandeville|Single area|Max stage is higher of surge (137) or design height (137)|


Stage-storage relationship

30

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


25

20

Stage[ft]

15

10

5

0

0 10000 20000 30000 40000 50000 60000 70000

Storage [acre ft]

- Figure B.26 – Stage storage relationship Mandeville




---PAGE-294---



Additional Notes

The Lidar levels on the North Shore show very low levels and the storage curves would extend to well below 0 datum. It has been decided to assume that there is no storage available below 3’ in all areas on the North shore when levees are to be constructed. The stage storage relationships used in the calculations have been amended to this for both the high level and barrier plans and this is the curve shown in the graph above.

The location of the levee has resulted in only a small area of storage adjacent to the proposed levees, and as such the degree of pumping has been increased to compensate for this, compared with the levels of pumping assumed in the central New Orleans area where the drainage channels and roads absorb much more of the initial flooding. For the North Shore a rate of 1cfs/acre has been adopted.

The areas for calculating rainfall volumes have been derived by looking at the natural topography and estimating the drainage area. No allowance has been made for man-made drainage routes which may affect the total volumes within a particular area.

Much of the proposed levee system is not likely to be subject to wave action as it extends along the banks of the major tributaries draining into Lake Pontchartrain. Only the levees facing the Lake have been used within the overtopping calculations. The overtopping lengths are indicated on the plans at the start of the section and the lengths are indicated here:

| |High Level Plan| | | |Barrier Plan| | | |
|---|---|---|---|---|---|---|---|---|
| |BS-0137 (miles)| | | |EB-0137 (miles)| | | |
|Overtopping|5.5| | | |5.5| | | |
|Non-overtopping|3.7| | | |3.7| | | |




---PAGE-295---



West Lacombe

- Figure B.27 – Sub-basin and levees West Lacombe (High Level and Barrier Plan)




---PAGE-296---



- Table B-14 – Levee characteristics West Lacombe


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0138|8.2|n.a.|15|20|22.5|15|20|22.5|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0138|8.2|n.a.|9.5|14.5|17.5|9.5|14.5|17.5|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|0|2,400|Based on 1cfs/acre|


|Storage Area|Type|Notes|
|---|---|---|
|West Lacombe|Single area|Max stage is higher of surge (138) or design height (138)|


Stage-storage relationship

30

| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |


25

20

Stage[ft]

15

10

5

0

0 5000 10000 15000 20000 25000 30000 35000 40000 45000 50000

Storage [acre ft]

- Figure B.28 – Stage storage relationship West Lacombe




---PAGE-297---



Additional Notes

The Lidar levels on the North Shore show very low levels and the storage curves would extend to well below 0 datum. It has been decided to assume that there is no storage available below 3’ in all areas on the North shore when levees are to be constructed. The stage storage relationships used in the calculations have been amended to this for both the high level and barrier plans and this is the curve shown in the graph above.

The location of the levee has resulted in only a small area of storage adjacent to the proposed levees, and as such the degree of pumping has been increased to compensate for this, compared with the levels of pumping assumed in the central New Orleans area where the drainage channels and roads absorb much more of the initial flooding. For the North Shore a rate of 1cfs/acre has been adopted.

The areas for calculating rainfall volumes have been derived by looking at the natural topography and estimating the drainage area. No allowance has been made for man-made drainage routes which may affect the total volumes within a particular area.

Much of the proposed levee system is not likely to be subject to wave action as it extends along the banks of the major tributaries draining into Lake Pontchartrain. Only the levees facing the Lake have been used within the overtopping calculations. The overtopping lengths are indicated on the plans at the start of the section and the lengths are indicated here:

| |High Level Plan| | | |Barrier Plan| | | |
|---|---|---|---|---|---|---|---|---|
| |BS-0138 (miles)| | | |EB-0138 (miles)| | | |
|Overtopping|5.3| | | |5.3| | | |
|Non-overtopping|2.9| | | |2.9| | | |




---PAGE-298---



East Lacombe

- Figure B.29 – Sub-basin and levees East Lacombe (High Level and Barrier Plan)




---PAGE-299---



- Table B-15 – Levee characteristics East Lacombe


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0138|5.6|n.a.|15|20|22.5|15|20|22.5|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0138|5.6|n.a.|9.5|14.5|17.5|9.5|14.5|17.5|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|0|5,000|Based on 1cfs/acre|


|Storage Area|Type|Notes|
|---|---|---|
|East Lacombe|Single area|Max stage is higher of surge (138) or design height (138)|


Stage-storage relationship

30

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


25

20

Storage [acre ft] Stage[ft]

15

10

5

0

0 10000 20000 30000 40000 50000 60000

- Figure B.30 – Stage storage relationship East Lacombe




---PAGE-300---



Additional Notes

The Lidar levels on the North Shore show very low levels and the storage curves would extend to well below 0 datum. It has been decided to assume that there is no storage available below 3’ in all areas on the North shore when levees are to be constructed. The stage storage relationships used in the calculations have been amended to this for both the high level and barrier plans and this is the curve shown in the graph above.

The location of the levee has resulted in only a small area of storage adjacent to the proposed levees, and as such the degree of pumping has been increased to compensate for this, compared with the levels of pumping assumed in the central New Orleans area where the drainage channels and roads absorb much more of the initial flooding. For the North Shore a rate of 1cfs/acre has been adopted.

The areas for calculating rainfall volumes have been derived by looking at the natural topography and estimating the drainage area. No allowance has been made for man-made drainage routes which may affect the total volumes within a particular area.

Much of the proposed levee system is not likely to be subject to wave action as it extends along the banks of the major tributaries draining into Lake Pontchartrain. Only the levees facing the Lake have been used within the overtopping calculations. The overtopping lengths are indicated on the plans at the start of the section and the lengths are indicated here:

| |High Level Plan| | | |Barrier Plan| | | |
|---|---|---|---|---|---|---|---|---|
| |BS-0138 (miles)| | | |EB-0138 (miles)| | | |
|Overtopping|3.9| | | |3.9| | | |
|Non-overtopping|1.7| | | |1.7| | | |




---PAGE-301---



Slidell

- Figure B.31 – Sub-basin and levees Slidell (High Level and Barrier Plan)




---PAGE-302---



###### Table B-16 – Levee characteristics Slidell

|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0139|10.0|n.a.|16|21.5|24|16|21.5|24|
|BS-0094|4.6|n.a.|16.5|23|26|16.5|23|16|
|BS-0175|7.3|n.a.|22.5|30.5|24.5|19|25.5|29|
|BS-0177|7.1|n.a.|20|28|32|17.5|23.5|26.5|


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0139|10.0|n.a.|11|17.5|21|11|17.5|21|
|EB-0094|4.6|n.a.|13|21|24.5|12.5|20.5|24.5|
|EB-0175|7.3|n.a.| | | | | | |
|EB-0177|7.1|n.a.|26|35|39|20.5|27|30|


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|0|54,000|Based on 1cfs/acre|


|Storage Area|Type|Notes|
|---|---|---|
|Slidell|Single area|Max stage is higher of surge (94) or design height (94) - see note|


Stage-storage relationship

30

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


25

20

Stage[ft]

15

10

5

0

0 100000 200000 300000 400000 500000 600000 700000

Storage [acre ft]

###### Figure B.32 – Stage storage relationship Slidell



---PAGE-303---



Additional Notes

The Lidar levels on the North Shore show very low levels and the storage curves would extend to well below 0 datum. It has been decided to assume that there is no storage available below 3’ in all areas on the North shore when levees are to be constructed. The stage storage relationships used in the calculations have been amended to this for both the high level and barrier plans and this is the curve shown in the graph above.

The location of the levee has resulted in only a small area of storage adjacent to the proposed levees, and as such the degree of pumping has been increased to compensate for this, compared with the levels of pumping assumed in the central New Orleans area where the drainage channels and roads absorb much more of the initial flooding. For the North Shore a rate of 1cfs/acre has been adopted.

The areas for calculating rainfall volumes have been derived by looking at the natural topography and estimating the drainage area. No allowance has been made for man-made drainage routes which may affect the total volumes within a particular area.

Much of the proposed levee system is not likely to be subject to wave action as it extends along the banks of the major tributaries draining into Lake Pontchartrain. Only the levees facing the Lake have been used within the overtopping calculations. The overtopping lengths are indicated on the plans at the start of the section and the lengths are indicated here:

| |High Level Plan| | | |Barrier Plan| | | |
|---|---|---|---|---|---|---|---|---|
| |BS-0139 (miles)|BS-0094 (miles)|BS-0175 (miles)|BS-0177 (miles)|EB-0139 (miles)|EB-0094 (miles)|EB-0175 (miles)|EB-0177 (miles)|
|Overtopping|10.0|4.6|7.3|4.5|10.0|4.6|7.3|4.5|
|Non-overtopping|0.0|0.0|0.0|2.6|0.0|0.0|0.0|2.6|


In addition there are three areas within the proposed new levee system which already have nonfederal levees which will affect the flood levels. These areas have been called Oak Harbor, Slidell 4 and Slidell 5. They are shown on the figure below. For this assessment the levees have been taken as having a crest elevation of 11’.

Using stage storage curves for these areas the 10 year rainfall without pumping results in the following flood levels.

Oak Harbor 3.8ft

- Slidell_4 6.2ft
- Slidell_5 4.8ft


This will not cause excessive flooding so additional pumping within theses areas has not been included. These values have been used for the inside of these areas apart from when the interior stage for the rest of the area exceeds 11' (the nominal levee height) when they were assumed to fill to the same level as outside the levees.



---PAGE-304---



|OakHarbor<br><br>Slidell_4<br><br>Slidell_5<br><br>94<br><br>1<br><br>7<br><br>5<br><br>139|
|---|




---PAGE-305---



###### Planning unit 2 – Barataria Basin

Algiers

- Figure B.33 – Sub-basin and levees Algiers (High Level and Barrier Plan)


- Table B-17 – Levee characteristics Algiers


|High Level Plan/ Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0158|2.0|10|10|15|17.5|10|15|17.5|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|4,650|4,650| |


|Storage Area|Type|Notes|
|---|---|---|
|Algiers|Single area|Max stage is higher of surge (158) or authorized (10’) or design height<br><br>(158)|




---PAGE-306---



| |
|---|
| |
| |
|20000 40000 60000 80000 100000 120000|
| |


15

10

5

Stage[ft]

0

0 140000

-5

- -15
- -10


Storage [acre ft]

- Figure B.34 – Stage storage relationship Algiers




---PAGE-307---



- English Turn
- Figure B.35– Sub-basin and levees English Turn (High Level and Barrier Plan)


- Table B-18 – Levee characteristics English Turn


|High Level Plan/ Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0158|0.9|10|10|15|17.5|10|15|17.5|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|1,670|1,670| |


|Storage Area|Type|Notes|
|---|---|---|
|English Turn|Single area|Max stage is higher of surge (158) or authorized (10’) or design height<br><br>(158)|




---PAGE-308---



| |
|---|
| |
| |
|10000 20000 30000 40000 50000 60000 70000|
| |
| |


15

10

5

Stage[ft]

0

0 80000

-5

- -15
- -10


Storage [acre ft]

- Figure B.36 – Stage storage relationship English Turn




---PAGE-309---



- Plaquemaines Belle Chase
- Figure B.37 – Sub-basin and levees Plaquemaines Belle Chase (High Level and Barrier Plan)




---PAGE-310---



- Table B-19 – Levee characteristics Plaquemaines Belle Chase


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0130|4.8|11|11|17|20|11|15|17|
|BS-0158|7.4|10|10|15|17.5|10|15|17.5|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0101|2.9|11|11|11|11|11|11|11|
|EB-0130|1.0|11|16|22|25|14|19|22|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|4,650|4,650| |


|Storage Area|Type|Notes|
|---|---|---|
|Plaquemines Belle Chase|Single area|Max height is higher of authorized (11’), surge (130) or design height<br><br>(130)|


Stage-storage relationship

20

15

10

5

Stage[ft]

0

0 50000 100000 150000 200000 250000 300000

-5

- -15
- -10


Storage [acre ft]

- Figure B.38 – Stage storage relationship Plaquemaines Belle Chase




---PAGE-311---



- West Jefferson – East of Harvey
- Figure B.39 – Sub-basin and levees West Jefferson – East of Harvey (High Level and Barrier Plan)




---PAGE-312---



- Table B-20 – Levee characteristics West Jefferson – East of Harvey


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0130|0.3|11|11|17|20|11|15|17|
|BS-0157|3.8|10|10|14|16.5|10|14|16|
|BS-0158|6.5|10|10|15|17.5|10|15|17.5|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0101|0.8|11|11|11|11|11|11|11|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|10,430|10,430| |


|Storage Area|Type|Notes|
|---|---|---|
|West Jeff - East of Harvey|Linked area (West Jeff)|Connects to Harvey (5’). See description of linked system in chapter 5|


Stage-storage relationship

20

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
|500|00 100|000 150|000 2000|00 2500|00|
| | | | | | |


15

10

5

Stage[ft]

0

0

-5

- -15
- -10


Storage [acre ft]

- Figure B.40 – Stage storage relationship West Jefferson – East of Harvey




---PAGE-313---



- West Jefferson – Harvey
- Figure B.41 – Sub-basin and levees West Jefferson – Harvey (High Level and Barrier Plan)




---PAGE-314---



- Table B-21 – Levee characteristics West Jefferson - Harvey


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0037|4.4|11|11|14|18|11|12.5|16|
|BS-0130|3.5|11|11|17|20|11|15|17|
|BS-0157|3.3|10|10|14|16.5|10|14|16|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0101|7.9|11|11|11|11|11|11|11|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|7,930|7,930| |


|Storage Area|Type|Notes|
|---|---|---|
|West Jeff - Harvey|Linked area (West Jeff)|Connects to EoH (5’) and Ames (5’). See description of linked system in chapter 5.|


Stage-storage relationship

20

| |
|---|
| |
| |
|20000 40000 60000 80000 100000 120000 140000 160000 180000|
| |


15

10

5

Stage[ft]

0

0 200000

-5

- -15
- -10


Storage [acre ft]

- Figure B.42 – Stage storage relationship West Jefferson – Harvey




---PAGE-315---



- West Jefferson – Ames
- Figure B.43 – Sub-basin and levees West Jefferson – Ames (High Level and Barrier Plan)




---PAGE-316---



- Table B-22 – Levee characteristics West Jefferson – Ames


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0037|7.5|11|11|14|18|11|12.5|16|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0101|7.5|11|11|11|11|11|11|11|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|4,760|4,760| |


|Storage Area|Type|Notes|
|---|---|---|
|West Jeff - Ames|Linked area (West Jeff)|Connects to Segnette (5’) and fed from Harvey (5’). See description of linked system in chapter 5|


Stage-storage relationship

20

| |
|---|
| |
| |
|10000 20000 30000 40000 50000 60000 70000|
| |
| |


15

10

5

Storage [acre ft] Stage[ft]

0

0 80000

-5

- -15
- -10


- Figure B.44 – Stage storage relationship West Jefferson – Ames




---PAGE-317---



- West Jefferson – Segnette
- Figure B.45– Sub-basin and levees West Jefferson – Segnette (High Level and Barrier Plan)




---PAGE-318---



- Table B-23 – Levee characteristics West Jefferson – Segnette


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0101|9.6|11|11|14|16|11|14|16|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0101|9.6|11|11|11|11|11|11|11|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|2,000|2,000| |


|Storage Area|Type|Notes|
|---|---|---|
|West Jeff - Segnette|Linked area (West Jeff)|Connects to Ames (5’). See description of linked system in chapter 5.|


Stage-storage relationship

20

| |
|---|
| |
| |
|50000 100000 150000 200000 250000 300000 350000|
| |


15

10

5

Storage [acre ft] Stage[ft]

0

0 400000

-5

- -15
- -10


- Figure B.46 – Stage storage relationship West Jefferson – Segnette




---PAGE-319---



- St Charles – Davis Pond
- Figure B.47 – Sub-basin and levees St Charles – Davis Pond (High Level and Barrier Plan)




---PAGE-320---



- Table B-24 – Levee characteristics St Charles – Davis Pond


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0101|4.0|11|11|14|16|11|14|16|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0101|4.0|11|11|11|11|11|11|11|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|0|0| |


|Storage Area|Type|Notes|
|---|---|---|
|St Charles - Davis pond|Single area|Max stage is higher of surge (101) or authorized (11’) or design height<br><br>(101)|


Stage-storage relationship

20

| |
|---|
| |
| |
| |


15

10

5

Storage [acre ft] Stage[ft]

0

0 20000 40000 60000 80000 100000 120000

-5

- -15
- -10


- Figure B.48 – Stage storage relationship St Charles – Davis Pond




---PAGE-321---



- St Charles – Lulling
- Figure B.49 – Sub-basin and levees St Charles - Lulling (High Level and Barrier Plan)




---PAGE-322---



- Table B-25 – Levee characteristics St Charles – Lulling


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0112|13.8|n.a.|8.5|12|13.5|8|11|13|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0112|13.8|n.a.|6.5|9|10.5|6|9|10|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|3,150|3,150| |


|Storage Area|Type|Notes|
|---|---|---|
|St Charles - Luling|Single area|Max stage is higher of surge (112) or design height (112)|


Stage-storage relationship

20

| |
|---|
| |
| |
| |
|100000 200000 300000 400000 500000 600000 700000 800000|
| |
| |


15

10

5

Stage[ft]

0

0 900000

-5

- -15
- -10


Storage [acre ft]

- Figure B.50 – Stage storage relationship St Charles - Lulling




---PAGE-323---



- St Charles – Sunset
- Figure B.51 – Sub-basin and levees St Charles - Sunset (High Level and Barrier Plan)




---PAGE-324---



- Table B-26 – Levee characteristics St Charles – Sunset


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0111|9.3|n.a.|8|11.5|13|8|11.5|13|
|BS-0112|8.9|n.a.|8.5|12|13.5|8|11|13|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0112|18.2|n.a.|6.5|9|10.5|6|9|10|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|800|800| |


|Storage Area|Type|Notes|
|---|---|---|
|St Charles - Sunset|Single area|Max stage is higher of surge (112) or design height (112)|


Stage-storage relationship

20

15

10

5

Storage [acre ft] Stage[ft]

0

0 20000 40000 60000 80000 100000 120000 140000 160000 180000

-5

- -15
- -10


- Figure B.52 – Stage storage relationship St Charles - Sunset




---PAGE-325---



- Lockport
- Figure B.53 – Sub-basin and levees Lockport (High Level and Barrier Plan)




---PAGE-326---



- Table B-27 – Levee characteristics Lockport


|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0112|30.4|n.a.|8.5|12|13.5|8|11|13|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0500|30.4|n.a.|6|8.5|10|6|8|10|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|0|0| |


|Storage Area|Type|Notes|
|---|---|---|
|Lockport|Single area|Max stage is higher of surge (110BS or 101EB) or design height (110BS or 101EB)|


Stage-storage relationship

20

15

10

5

Storage [acre ft] Stage[ft]

0

0 100000 200000 300000 400000 500000 600000

-5

- -15
- -10


- Figure B.54 – Stage storage relationship Lockport




---PAGE-327---



- Larose to Golden Meadow
- Figure B.55 – Sub-basin and levees Larose to Golden Meadow (High Level and Barrier Plan)




---PAGE-328---



###### Table B-28 – Levee characteristics Larose to Golden Meadow

|High Level Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|BS-0074|19.2|12|18|25|28.5|15.5|21.5|25|
|BS-0075|19.6|12|17|21.5|23.5|16|20.5|22.5|
|BS-0205|9.2|12|12|14|16.5|11|14|16.5|
| | | | | | | | | |


|Barrier Plan| | |Design Height (waves modeled without friction)| | |Design Height (waves modeled with friction)| | |
|---|---|---|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|100 year|400 year|1000 year|
|[-]|[miles]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|[ft]|
|EB-0074|19.8|12|18.5|26.5|30.5|15.5|22|25.5|
|EB-0075|26.1|12|17.5|23|26|16.5|22|24.5|
|EB-0236|2.7|12|17.5|23|26|16.5|22|24.5|
| | | | | | | | | |


| |Existing|Proposed|Notes|
|---|---|---|---|
|Pump Capacity (cfs)|0|0| |


|Storage Area|Type|Notes|
|---|---|---|
|Larose|Single area|This is a ring levee system with a varying level of levee because of a rapidly changing elevation of surge. Max surge is the higher of surge<br><br>(75), authorized (13.5’) or design height (75), but capped at 15’ as the damages don’t increase beyond this point. (see additional note below)|


Stage-storage relationship

20

| |
|---|
| |
| |
| |


15

10

5

Stage[ft]

0

0 100000 200000 300000 400000 500000 600000 700000 800000 900000

-5

- -15
- -10


Storage [acre ft]

###### Figure B.56 – Stage storage relationship Larose to Golden Meadow



---PAGE-329---



Additional Notes

Two authorized heights have been used, 13.5’ for the southern end of the ring and 10’ for the northern end. A review of the stage damage curves has suggested that damages tail off dramatically at 15’.

The Larose to Golden Meadow area is considered as a single interior stage storage area with the potential for overtopping from both the east and west. The western side falls within Planning Unit 3a, which has not been fully investigated yet. If the results from the EB model grid are used for the west it results in higher design heights than with the base case. This is because of the effects of the closure across the Morganza region in the EB model. As the alternatives for this area have yet to be evaluated it has been decided to use the values from the base grid for both the without and with GIWW weir alternatives so the rates of overtopping are constant into the Larose areas from the west. (i.e. BS-0074 is to be used for all alternatives in Planning Unit 2.

As there will be no 100 year level of protection levee system in place before 2010 the base case internal stage frequency should be based on the existing authorized heights rather than the 100 year design heights. For this study three sections are used, BS-0074, BS-0075 and BS-0205. Using the original study reports the authorized heights vary from 13.5’ in the south to 10’ in the north. For analysis the 13.5’ levels have been used for points BS-0074 and BS-0075 whilst 10’ has been used for BS-0205.



---PAGE-330---



- Planning Unit 3a Polder Ring: Morganza_no_ret_ring


- Figure B.57 – Sub-basin and levees Morganza_no_ret_ring


- Table B-29 – Levee characteristics Morganza_no_ret_ring


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WA-W0050|17395|n.a.|12|19.5|23.5|
|WA-W0045|63223|n.a.|15|24|29|
|WA-W0035|83975|n.a.|23|31|35.5|
|WA-W0026|110857|n.a.|28|36.5|41|
|WA-W0025|57759|n.a.|22|30.5|35.5|


|Storage Area|pumping rate [cfs]|Type|Notes|
|---|---|---|---|
|Morganza_no_ret_ring|36581|Single area| |




---PAGE-331---



###### Figure B.58 – Stage storage relationship for Morganza no ret ring



---PAGE-332---



Polder Ring: East_of_Morgan_City_ring

- Figure B.59 – Sub-basin and levees East_of_Morgan_City_ring


- Table B-30 – Levee characteristics East of Morgan_City_ring


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WA-W0056|86276|n.a.|16.5|23|27|
|WA-W0050|78062|n.a.|12|19.5|23.5|
|WT-WPATT| |n.a.|13.5|20|24|
| | | | | | |
| | | | | | |


|Storage Area|pumping rate [cfs]|Type|Notes|
|---|---|---|---|
|East_of_Morgan_City_ring|400|Single area| |




---PAGE-333---



###### Figure B.60 – Stage storage relationship for East_of_Morgan_City_ring



---PAGE-334---



Polder Ring: Morganza_with_ret_ring

- Figure B.61 – Sub-basin and levees Morganza_with_ret_ring


- Table B-31 – Levee characteristics Morganza_with_ret_ring


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WA-W0050|43663|n.a.|12|19.5|23.5|
|WA-W0050|21006|n.a.|12|19.5|23.5|
|WA-W0045|63223|n.a.|15|24|29|
|WA-W0035|83975|n.a.|23|31|35.5|
|WA-W0026|110857|n.a.|28|36.5|41|
|WA-W0025|57759|n.a.|22|30.5|35.5|


|Storage Area|Pumping rate [cfs]|Type|Notes|
|---|---|---|---|
|Morganza_with_ret_ring|55151|Single area| |




---PAGE-335---



###### Figure B.62 – Stage storage relationship for Morganza with ret ring



---PAGE-336---



Polder Ring: Morganza_with_ret_ring_m_only

- Figure B.63 – Sub-basin and levees Morganza_with_ret_ring_m_only


- Table B-32 – Levee characteristics Morganza_with_ret_ring_m_only


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WA-W0045|63223|n.a.|15|24|29|
|WA-W0035|83975|n.a.|23|31|35.5|
|WA-W0026|110857|n.a.|28|36.5|41|
|WA-W0025|57759|n.a.|22|30.5|35.5|
| | | | | | |
| | | | | | |


|Storage Area|Pumping rate [cfs]|Type|Notes|
|---|---|---|---|
|Morganza_with_ret_ring_m_only|2042|Single area| |




---PAGE-337---



###### Figure B.64 – Stage storage relationship for Morganza_with_ret_ring_m_only



---PAGE-338---



Polder Ring: Morganza_back_levee

- Figure B.65 – Sub-basin and levees Morganza_back_levee


- Table B-33 – Levee characteristics Morganza_back_levee


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WA-W0050|43663|n.a.|12|19.5|23.5|
|WA-W0050|21006|n.a.|12|19.5|23.5|
|WC-W0169|154153|n.a.|-|9.5|24|
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping rate [cfs]|Type|Notes|
|---|---|---|---|
|Morganza_back_levee|53109|Single area|Stages behind the secondary defense (Morganza back levee) are calculated based upon overtopping from the flooded polder Morganza. An exception is made for the 2000 year event where stages are equal to the base surge conditions|




---PAGE-339---



###### Figure B.66 – Stage storage relationship for Morganza_back_levee



---PAGE-340---



Morgan_City

- Figure B.67 – Sub-basin and levees Morgan_City_ring


- Table B-34 – Levee characteristics Morgan_City_ring


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WB-W0056|33243|n.a.|18|25|28.5|
|WT-WPATT| |n.a.|13.5|20|24|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Morgan_City_ring|400|Single area|For small ring levees overtopping is assumed only to occur from the sea side levee. In this case that is levee 56|




---PAGE-341---



###### Figure B.68 – Stage storage relationship for Morgan City



---PAGE-342---



- Planning Unit 3b Polder Ring: South_of_Franklin_ring


- Figure B.69 – Sub-basin and levees South_of_Franklin_ring


- Table B-35 – Levee characteristics South_of_Franklin_ring


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WA-W0079|151872|n.a.|20.5|28|32.5|
|WT-WPATT| |n.a.|13.5|20|24|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|South_of_Franklin_ring|311|Single area| |




---PAGE-343---



###### Figure B.70 – Stage storage relationship for South_of_Franklin_ring



---PAGE-344---



Polder Ring: GIWW_PU3b_ring

- Figure B.71 – Sub-basin and levees GIWW_PU3b_ring


- Table B-36 – Levee characteristics GIWW_PU3b_ring


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WA-W0103|48316|n.a.|21.5|28|31.5|
|WA-W0063|131984|n.a.|20|27.5|32.5|
|WA-W0079|12102|n.a.|20.5|28|32.5|
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|GIWW_PU3b_ring|19046|Single area| |




---PAGE-345---



###### Figure B.72 – Stage storage relationship for GIWW_PU3b_ring



---PAGE-346---



Polder Ring: Patterson

- Figure B.73 – Sub-basin and levees Patterson


- Table B-37 – Levee characteristics Patterson


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WB-W0056|77285|n.a.|18|25|28.5|
|WT-WPATT| |n.a.|13.5|20|24|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Patterson|29853|Single area|For the Patterson ring levee overtopping is assumed to only occur over the levee facing the sea.|




---PAGE-347---



###### Figure B.74 – Stage storage relationship for Patterson



---PAGE-348---



Polder Ring: Abbeville_to_Delcambre_ring

- Figure B.75 – Sub-basin and levees Abbeville_to_Delcambre_ring


- Table B-38 – Levee characteristics Abbeville_to_Delcambre_ring


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WB-W0090|42402|n.a.|18|24.5|28.5|
|WB-W0075|48469|n.a.|20|27|31|
|WB-W0085|22333|n.a.|17|26|31.5|
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Abbeville_to_Delcambre_ring|27617|Single area| |




---PAGE-349---



###### Figure B.76 – Stage storage relationship for Abeville_to_Delcambre_ring



---PAGE-350---



Polder Ring: New_Iberia_ring

- Figure B.77 – Sub-basin and levees New_Iberia_ring


- Table B-39 – Levee characteristics New_Iberia_rign


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WB-W0085|106523|n.a.|17|26|31.5|
|WB-W0089|13927|n.a.|19|26.5|30.5|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|New_Iberia_ring|0|Single area|For large storage areas pumping capacities are set to zero as it is assumed that enough “natural storage” is available inside these drainage basins.|




---PAGE-351---



###### Figure B.78 – Stage storage relationship for New_Iberia_ring



---PAGE-352---



Polder Ring: Charenton_ring

- Figure B.79 – Sub-basin and levees Charenton_ring


- Table B-40 – Levee characteristics Chareton_ring


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WB-W0089|31581|n.a.|19|26.5|30.5|
|WB-W0094|11259|n.a.|16.5|25|30|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Charenton_ring|10472|Single area| |




---PAGE-353---



###### Figure B.80 – Stage storage relationship for Charenton_ring



---PAGE-354---



Polder Ring: Abbeville

- Figure B.81 – Sub-basin and levees Abbeville


- Table B-41 – Levee characteristics Abbeville


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WT-W0110|33797|n.a.|12.5|20.5|25|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Abbeville|1836|Single area| |




---PAGE-355---



###### Figure B.82 – Stage storage relationship for Abbeville



---PAGE-356---



Polder Ring: Erath

- Figure B.83 –Sub-basin and levees Erath


- Table B-42 – Levee characteristics Erath


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WT-W0111|19667|n.a.|17.5|25|29|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Erath|553|Single area|Erath is amongst the ring levees for which overtopping is only included for the seaward side of the levee|




---PAGE-357---



###### Figure B.84 – Stage storage relationship for Erath



---PAGE-358---



Polder Ring: Delcambre

- Figure B.85 – Sub-basin and levees Delcambre


- Table B-43 – Levee characteristics Delcambre


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WT-W0111|21979|n.a.|17.5|25|29|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Delcambre|555|Single area| |




---PAGE-359---



###### Figure B.86 – Stage storage relationship for Delcambre



---PAGE-360---



Polder Ring: New_Iberia

- Figure B.87 – Sub-basin and levees New_Iberia


- Table B-44 – Levee characteristics New_Iberia


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WT-W0104|66021|n.a.|14.5|22|26.5|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|New_Iberia|0|Single area| |




---PAGE-361---



###### Figure B.88 – Stage storage relationship for New_Iberia



---PAGE-362---



Polder Ring: Baldwin

- Figure B.89 – Sub-basin and levees Baldwin


- Table B-45 – Levee characteristics Baldwin


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WB-W0094|17831|n.a.|16.5|25|30|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Baldwin|554|Single area| |




---PAGE-363---



###### Figure B.90 – Stage storage relationship for Baldwin



---PAGE-364---



Polder Ring: Franklin

- Figure B.91 – Sub-basin and levees Franklin


- Table B-46 – Levee characteristics Franklin


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WB-W0094|78444|n.a.|16.5|25|30|
|WB-W0060|42760|n.a.|16.5|23.5|27.5|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Franklin|17125|Single area| |




---PAGE-365---



###### Figure B.92 – Stage storage relationship for Franklin



---PAGE-366---



###### Planning Unit 4

Polder Ring: Central_PU4_ring

- Figure B.93 – Sub-basin and levees Central_PU4_ring


- Table B-47 – Levee characteristics Central_PU4_ring


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WA-W0119|38332|n.a.|13.5|21.5|26|
|WA-W0073|62206|n.a.|16|24|28.5|
|WA-W0082|57523|n.a.|14|20.5|24.5|
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Central_PU4_ring|0|Single area| |




---PAGE-367---



###### Figure B.94 – Stage storage relationship for Central_PU4_ring



---PAGE-368---



Polder Ring: GIWW_to_Veterans_ring

- Figure B.95 – Sub-basin and levees GIWW_to_Veterans_ring


- Table B-48 – Levee characteristics GIWW_to_Veterans_ring


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WA-W0124|132503|n.a.|12|19.5|24|
|WA-W0103|33981|n.a.|21.5|28|31.5|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|GIWW_to_Veterans_ring|366|Single area| |




---PAGE-369---



###### Figure B.96 – Stage storage relationship for GIWW_to_Veterans_ring



---PAGE-370---



Polder Ring: South_of_Lake_Charles_ring

- Figure B.97 – Sub-basin and levees South_of_Lake_Charles_ring


- Table B-49 – Levee characteristics South_of_Lake_Charles_ring


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WA-W0119|62456|n.a.|13.5|21.5|26|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|South_of_Lake_Charles_ring|29761|Single area| |




---PAGE-371---



###### Figure B.98 – Stage storage relationship for South_of_Lake_Charles_ring



---PAGE-372---



Polder Ring: West_Lake_Charles

- Figure B.99 – Sub-basin and levees West_Lake_Charles


- Table B-50 – Levee characteristics West_Lake_Charles


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WT-W0127|77095|n.a.|11|15.5|17.5|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|West_Lake_Charles|29761|Single area| |




---PAGE-373---



###### Figure B.100 – Stage storage relationship for West_Lake_Charles



---PAGE-374---



Polder Ring: Prien

- Figure B.101 – Sub-basin and levees Prien


- Table B-51 – Levee characteristics Prien


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WT-W0999|1918|n.a.|13.5|17|19.5|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Prien|13927|Single area|The Prien area is more prone to flooding from the river side instead of the sea side while sea surge penetrate up the river. Due to lack of wave data a 3ft wave is applied to come to overtopping rates for this levee.|




---PAGE-375---



###### Figure B.102 – Stage storage relationship for Prien



---PAGE-376---



Polder Ring: Inner_Lake_Charles

- Figure B.103 – Sub-basin and levees Inner_Lake_Charles


- Table B-52 – Levee characteristics Inner_Lake_Charles


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WT-W0999|2103|n.a.|13.5|17|19.5|
|WT-W0999|15698|n.a.|13.5|17|19.5|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Inner_Lake_Charles|13927|Single area|Equally to the Prien area this area is more prone to flooding from the river side instead of the sea side while sea surge penetrates up the river. Due to lack of wave data a 3ft wave is applied to come to overtopping rates for this levee.|




---PAGE-377---



###### Figure B.104 – Stage storage relationship for Inner_Lake_Charles



---PAGE-378---



Polder Ring: South_of_Lake_Charles_ring_12

- Figure B.105 – Sub-basin and levees South_of_Lake_Charles_ring_12


- Table B-53 – Levee characteristics South_of_Lake_Charles_ring_12


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WA-W0119|62456|n.a.|12|12|12|
|WT-W0127|44374|n.a.|-|10.7|12.3|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|South_of_Lake_Charles_ring_12|311|Single area| |




---PAGE-379---



###### Figure B.106 – Stage storage relationship for South_of_Lake_Charles_ring_12



---PAGE-380---



Polder Ring: Central_PU4_ring_large_12

- Figure B.107 – Sub-basin and levees Central_PU4_ring_large_12


- Table B-54 – Levee characteristics Central_PU4_ring_large_12


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WA-W0119|38332|n.a.|12|12|12|
|WA-W0073|62206|n.a.|12|12|12|
|WA-W0082|57523|n.a.|12|12|12|
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Central_PU4_ring_large_12|29761|multiple areas|For the 12’ levee design to be effective areas are combined to let the flooding to spread out over several areas.|




---PAGE-381---



###### Figure B.108 – Stage storage relationship for Central_PU4_ring_large_12



---PAGE-382---



Polder Ring: GIWW_to_Veterans_ring_large_12

- Figure B.109 – Sub-basin and levees GIWW_to_Veterans_ring_large_12


- Table B-55 – Levee characteristics GIWW_to_Veterans_ring_large_12


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WA-W0124|132503|n.a.|12|12|12|
|WA-W0103|33981|n.a.|12|12|12|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|GIWW_to_Veterans_ring_large_12|366|multiple areas|For the 12’ levee design to be effective areas are combined to let the flooding to spread out over several areas.|




---PAGE-383---



###### Figure B.110 – Stage storage relationship for GIWW_to_Vetterans_ring_large_12



---PAGE-384---



Polder Ring: East_Lake_Charles

- Figure B.111 – Sub-basin and levees East_Lake_Charles


- Table B-56 – Levee characteristics East_Lake_Charles


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WT-W0127|77095|n.a.|11|15.5|17.5|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|East_Lake_Charles|5396|single area| |




---PAGE-385---



###### Figure B.112 – Stage storage relationship for East_Lake_Charles



---PAGE-386---



Polder Ring: Gueydan

- Figure B.113 – Sub-basin and levees Gueydan


- Table B-57 – Levee characteristics Gueydan


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WT-W0153|21674|n.a.|9|15.5|18.5|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Gueydan|366|single area|Equally to other smaller ring levees Gueydan is only overtopped from the seawards side|




---PAGE-387---



###### Figure B.114 – Stage storage relationship for Gueydan



---PAGE-388---



Polder Ring: Kaplan

- Figure B.115 – Sub-basin and levees Kaplan


- Table B-58 – Levee characteristics Kaplan


| | | |Design Height (waves modeled without friction)| | |
|---|---|---|---|---|---|
|Reach ID|Length|Authorized Height|100 year|400 year|1000 year|
|[-]|[ft]|[ft]|[ft]|[ft]|[ft]|
|WT-W0135|16630|n.a.|9|15.5|18.5|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


|Storage Area|Pumping Rate [cfs]|Type|Notes|
|---|---|---|---|
|Kaplan|5496|single area|Equally to other smaller ring levees Kaplan is only overtopped from the seawards side|




---PAGE-389---



###### Figure B.116 – Stage storage relationship for Kaplan

