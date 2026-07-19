Title: Regional Wave Analysis in the East China Sea Based on the SWAN Model

URL Source: https://www.mdpi.com/2077-1312/13/6/1196

Published Time: 2025-06-19

Markdown Content:
Logical Operator Operator

Search Text

Search Type

_add\_circle\_outline_

_remove\_circle\_outline_

[![Image 1: jmse-logo](https://pub.mdpi-res.com/img/journals/jmse-logo.png?c64da767266cbc39)](https://www.mdpi.com/journal/jmse)

## Article Menu

Font Type:

_Arial_ _Georgia_ _Verdana_

Font Size:

Aa Aa Aa

Line Spacing:

__ __ __

Column Width:

__ __ __

Background:

Open Access Article

by 
Songnan Ma

 1,2[](mailto:2131614@tongji.edu.cn), 
Fuwu Ji

 1,2,*[](mailto:jifuwu@tongji.edu.cn), 
Qunhui Yang

 1,2,3,*[](mailto:yangqh@tongji.edu.cn)[![Image 2: ORCID](https://pub.mdpi-res.com/img/design/orcid.png?0465bc3812adeb52?1783907519)](https://orcid.org/0000-0003-2423-5085), 
Zhinan Mi

 4[](mailto:znm21cn@tongji.edu.cn) and 
Wenhui Cao

 1,2[](mailto:henry_cao@tongji.edu.cn)[![Image 3: ORCID](https://pub.mdpi-res.com/img/design/orcid.png?0465bc3812adeb52?1783907519)](https://orcid.org/0000-0002-6803-582X)

1

State Key Laboratory of Marine Geology, Tongji University, Shanghai 200092, China

2

Project Management Office of China National Scientific Seafloor Observatory, Tongji University, Shanghai 200092, China

3

Laoshan Laboratory, Qingdao 266237, China

4

School of Mechanical Engineering, Tongji University, Shanghai 200092, China

*

Authors to whom correspondence should be addressed.

Submission received: 24 April 2025 / Revised: 12 June 2025 / Accepted: 16 June 2025 / Published: 19 June 2025

## Abstract

High-precision wave data serve as a foundation for investigating the wave characteristics of the East China Sea (ECS) and wave energy development. Based on the simulating waves nearshore (SWAN) model, this study uses the ERA5 (ECMWF Reanalysis v5) reanalysis wind field data and ETOPO1 bathymetric data to perform high-precision simulations at a resolution of 0.05° × 0.05° for the waves in the area of 25–35° N and 120–130° E in the ECS from 2009 to 2023. The simulation results indicate that the application of the whitecapping dissipation parameter Komen and the bottom friction parameter Collins yields an average RMSE of 0.374 m and 0.369 m when compared to satellite-measured data, demonstrating its superior suitability for wave simulation in shallow waters such as the ESC over the other whitecapping dissipation parameter, Westhuysen, and the other two bottom friction parameters, Jonswap and Madsen, in the SWAN model. The monthly average significant wave height (SWH) ranges from 0 to 3 m, exhibiting a trend that it is more important in autumn and winter than in spring and summer and gradually increases from the northwest to the southeast. Due to the influence of the Kuroshio current, topography, and events such as typhoons, areas with significant wave heights are found in the northwest of the Ryukyu Islands and north of the Taiwan Strait. The wave energy flux density in most areas of the ECS is >2 kW/m, particularly in the north of the Ryukyu Islands, where the annual average value remains above 8 kW/m. Because of the influence of climate events such as El Niño and extreme heatwaves, the wave energy flux density decreased significantly in some years (a 21% decrease in 2015). The coefficient of variation of wave energy in the East China Sea exhibits pronounced regional heterogeneity, which can be categorized into four distinct patterns: high mean wave energy with high variation coefficient, high mean wave energy with low variation coefficient, low mean wave energy with high variation coefficient, and low mean wave energy with low variation coefficient. This classification fundamentally reflects the intrinsic differences in dynamic environments across various maritime regions. These high-precision numerical simulation results provide methodological and theoretical support for exploring the spatiotemporal variation laws of waves in the ECS region, the development and utilization of wave resources, and marine engineering construction.

## 1. Introduction

Waves are an essential dynamic factor in the marine environment and play a crucial role in the exchange of momentum and energy between the atmosphere and the ocean boundary layer [[1](https://www.mdpi.com/2077-1312/13/6/1196#B1-jmse-13-01196),[2](https://www.mdpi.com/2077-1312/13/6/1196#B2-jmse-13-01196)]. The continental shelf of the East China Sea (ECS) is one of the broadest continental shelves in the world, and the Yangtze River Delta economic belt, which is highly economically developed, is located along its coast [[3](https://www.mdpi.com/2077-1312/13/6/1196#B3-jmse-13-01196)]. Therefore, an in-depth study of the spatiotemporal variation characteristics of waves in the ECS region and accurate numerical wave simulation is of great significance for enhancing the safety of marine engineering, strengthening the capacity for marine environmental protection and disaster prevention and mitigation, and promoting regional economic development [[4](https://www.mdpi.com/2077-1312/13/6/1196#B4-jmse-13-01196),[5](https://www.mdpi.com/2077-1312/13/6/1196#B5-jmse-13-01196)].

Wave information has been primarily obtained through real-time observations using buoys, ships, and satellites [[6](https://www.mdpi.com/2077-1312/13/6/1196#B6-jmse-13-01196)]. However, real-time observations are costly and limited by spatiotemporal resolution and coverage, making it difficult to provide long-term, large-scale, and high-precision wave parameters [[7](https://www.mdpi.com/2077-1312/13/6/1196#B7-jmse-13-01196)]. In addition, severe weather further increases the difficulty of measuring wave data [[8](https://www.mdpi.com/2077-1312/13/6/1196#B8-jmse-13-01196)]. Researchers have developed various wave spectrum models based on wave observation data to address these issues.

The wave model WAM [[9](https://www.mdpi.com/2077-1312/13/6/1196#B9-jmse-13-01196)], WAVEWATCH III [[10](https://www.mdpi.com/2077-1312/13/6/1196#B10-jmse-13-01196)], and simulating waves nearshore (SWAN) [[11](https://www.mdpi.com/2077-1312/13/6/1196#B11-jmse-13-01196)], developed based on the principle of energy conservation, are mainstream third-generation wave models internationally. WAM and WAVEWATCH III are primarily used for large-scale wave calculations in open oceans [[12](https://www.mdpi.com/2077-1312/13/6/1196#B12-jmse-13-01196),[13](https://www.mdpi.com/2077-1312/13/6/1196#B13-jmse-13-01196),[14](https://www.mdpi.com/2077-1312/13/6/1196#B14-jmse-13-01196)].

However, SWAN uses an implicit propagation scheme and is more stable in shallow waters, making it more suitable for simulating nearshore waves than the other two wave models [[15](https://www.mdpi.com/2077-1312/13/6/1196#B15-jmse-13-01196)]. For example, Umesh et al. compared the simulation capabilities of the WAVEWATCH III and SWAN models for wave fields along the shallow-water coasts of northwestern and northeastern India [[13](https://www.mdpi.com/2077-1312/13/6/1196#B13-jmse-13-01196)], further validating these simulation results. Ponce de León used models such as WAM, WAVEWATCH III, and SWAN to simulate the wave field in the North Sea (water depth < 150 m) in the northwestern Atlantic Ocean and found that WAM and WAVEWATCH III underestimated high-frequency wave energies under specific wind directions [[16](https://www.mdpi.com/2077-1312/13/6/1196#B16-jmse-13-01196)]. In contrast, the SWAN model effectively solves the above problems.

The continental shelf of the ECS is broad, and the water depth in most areas is relatively shallow, with an average water depth of 370 m [[17](https://www.mdpi.com/2077-1312/13/6/1196#B17-jmse-13-01196)]. The wave observation data are limited. There is an urgent need to perform numerical wave simulations. Research on applying the SWAN model to wave simulations in the ECS is still in its infancy. Xie et al. simulated the ECS (26° N–32° N, 120° E–126° E) based on cross-calibrated, multi-platform (CCMP) wind field data and earth topography (ETOPO) terrain data. They improved the accuracy of the SWAN model for simulating waves in the ECS by investigating the adaptability of the triangular grid [[18](https://www.mdpi.com/2077-1312/13/6/1196#B18-jmse-13-01196)]. However, the period of the study was relatively short, only analyzing the data of 2011, and the time resolution of the wind field data was 6 h, which had certain limitations for inversely calculating the daily wave changes. Liu et al. simulated the wave height distribution in the ECS region using the SWAN model based on National Energy and Climate Plans (NECP, [https://www.emc.ncep.noaa.gov/emc.php](https://www.emc.ncep.noaa.gov/emc.php) accessed on 10 December 2024) data [[19](https://www.mdpi.com/2077-1312/13/6/1196#B19-jmse-13-01196)]. They obtained the seasonal distribution pattern of the waves; however, the calculation grid had a low precision (0.5° × 0.5°). Overall, the current analysis of wave elements in the ECS using the SWAN model is limited to any wave height, energy, or period, and multiple wave elements cannot be analyzed comprehensively. There is a lack of large-scale, long-time-series, high-precision wave simulations that integrate multiple wave elements.

It is noteworthy that the default parameter settings of the SWAN model lack universality and cannot accurately reproduce wave processes in all maritime regions. Previous studies have demonstrated that targeted selection and adjustment of model parameters for specific study areas can significantly enhance the reliability and accuracy of simulation results [[4](https://www.mdpi.com/2077-1312/13/6/1196#B4-jmse-13-01196),[20](https://www.mdpi.com/2077-1312/13/6/1196#B20-jmse-13-01196),[21](https://www.mdpi.com/2077-1312/13/6/1196#B21-jmse-13-01196)]. Among these parameters, bottom friction and whitecapping dissipation, as key physical processes governing wave energy dissipation, directly influence simulated outputs such as significant wave height and have thus garnered widespread attention. For instance, Kutupoğlu et al., in their wave simulation study of the Marmara Sea, Turkey, compared results with Silivri buoy observations and found that adopting the Komen whitecapping dissipation scheme effectively reduced simulation errors, significantly outperforming the Westhuysen parameterization [[20](https://www.mdpi.com/2077-1312/13/6/1196#B20-jmse-13-01196)]. Similarly, Samiksha et al. investigated the impact of three bottom friction parameterizations (Jonswap, Collins, and Madsen) on significant wave height simulations along the southwestern coast of India. Their results indicated that the Jonswap scheme yielded the smallest bias and the lowest root mean square error [[21](https://www.mdpi.com/2077-1312/13/6/1196#B21-jmse-13-01196)]. In applications of the SWAN model to the East China Sea, studies have also attempted to adjust whitecapping dissipation and bottom friction parameters to optimize wave simulations under forcing conditions such as typhoons [[4](https://www.mdpi.com/2077-1312/13/6/1196#B4-jmse-13-01196)]. However, most existing research has focused on short-term simulations (e.g., individual typhoon events) and parameter sensitivity analyses, with parameter settings often relying on localized empirical knowledge or calibration against single observational datasets. A systematic optimization strategy tailored to regional characteristics remains lacking. Particularly under the combined influence of varying wind fields, bathymetric changes, and complex topography, current parameter configurations exhibit insufficient spatial adaptability, struggling to meet the requirements for universal applicability across different dynamic conditions. Therefore, establishing a regionally adaptive parameter selection framework is crucial for improving the SWAN model’s simulation capability in the East China Sea and similar maritime regions.

In this study, the SWAN model is used. High-precision ERA5 (ECMWF Reanalysis v5, [https://www.ecmwf.int/](https://www.ecmwf.int/) accessed on 10 December 2024) reanalysis wind field data and ETOPO1 ([https://www.ncei.noaa.gov/products/etopo-global-relief-model](https://www.ncei.noaa.gov/products/etopo-global-relief-model) accessed on 10 December 2024) bathymetric data are used to perform high-precision simulations with a calculation grid of 0.05° × 0.05° for the waves in the area of 25–35° N and 120–130° E in the ECS from 2009 to 2023. The spatiotemporal distribution characteristics of wave parameters, such as significant wave height and wave direction, were analyzed, and the long-term variations of wave energy resources and their responses to climatic events were also evaluated in this study, which can improve our knowledge of the characteristics of the waves in the East China Sea.

## 2. Model Parameterization and Data Sources

The study area is located in the continental shelf area of the ECS and has latitude and longitude ranges of 25–35° N and 120–130° E, respectively. The specific location is shown in [Figure 1](https://www.mdpi.com/2077-1312/13/6/1196#fig_body_display_jmse-13-01196-f001). Note that the default parameter settings of the SWAN model do not apply to all sea areas, and the bottom friction coefficient significantly influences the accuracy of the simulation results in shallow sea areas [[22](https://www.mdpi.com/2077-1312/13/6/1196#B22-jmse-13-01196)]. Based on previous experience in applying the SWAN model for wave simulations in shallow seas, this study optimized model parameters and data sources, with particular attention to evaluating and selecting bottom friction coefficients and whitecapping parameters according to the characteristics of the East China Sea. The simulation period was set from 2009 to 2023, which not only covers interannual fluctuations, extreme events, and intense typhoon processes but also ensures the quality and continuity of wind field and observational data [[23](https://www.mdpi.com/2077-1312/13/6/1196#B23-jmse-13-01196),[24](https://www.mdpi.com/2077-1312/13/6/1196#B24-jmse-13-01196)].

**Figure 1.** Marine topography of the study area (based on ETOPO1 data).

### 2.1. SWAN Model

The SWAN model was developed by the Delft University of Technology in the Netherlands [[11](https://www.mdpi.com/2077-1312/13/6/1196#B11-jmse-13-01196)]. The dynamic spectral density is conserved in the flow field, whereas the energy spectral density is not. The dynamic spectral density N(σ, θ) is the ratio of the energy spectral density E(σ, θ) to the relative frequency σ.

$$
N \left(\sigma , \theta\right) = \frac{S \left(\sigma , \theta\right)}{\sigma} ,
$$

(1)

where N(σ, θ) denotes the dynamic spectral density; S donates the non-conservative source and sink term that represents all physical processes that generate, dissipate, or redistribute wave energy at a point; σ denotes the relative frequency of ocean waves; θ denotes the wave direction perpendicular to the wave crest line in the spectral component [[25](https://www.mdpi.com/2077-1312/13/6/1196#B25-jmse-13-01196)].

Therefore, the SWAN model uses an implicit scheme to discretize the control equations and represents random waves through two-dimensional dynamic spectral densities rather than two-dimensional energy spectral densities [[26](https://www.mdpi.com/2077-1312/13/6/1196#B26-jmse-13-01196)].

In the Cartesian coordinate system, the dynamic spectral balance equation can be expressed as follows:

$$
\frac{\partial}{\partial t} N + \frac{\partial}{\partial X} C_{x} N + \frac{\partial}{\partial y} C_{y} N + \frac{\partial}{\partial \sigma} C_{\sigma} N + \frac{\partial}{\partial \theta} C_{\theta} N = \frac{S}{\sigma} ,
$$

(2)

$$
S = S_{i n} + S_{n l 3} + S_{n l 4} + S_{d s , w} + S_{d s , b} + S_{d s , b r} ,
$$

(3)

where S in denotes wind energy input; S nl3 denotes triad wave–wave interactions, representing the redistribution of energy due to the transfer from the spectral peak to higher harmonics; S nl4 denotes quadruplet wave–wave interactions, representing the redistribution of energy first from the spectral peak to the low-frequency region and then to the high-frequency region; S ds,w denotes whitecapping dissipation, which is energy dissipation caused by wave breaking; S ds,b and S ds,br denote energy dissipation due to friction and depth-induced breaking, respectively.

Among these, S nl3, S ds,b, and S ds,br primarily act in shallow water and are collectively called shallow-water processes [[11](https://www.mdpi.com/2077-1312/13/6/1196#B11-jmse-13-01196),[27](https://www.mdpi.com/2077-1312/13/6/1196#B27-jmse-13-01196)]. These shallow-water processes significantly improve the ability of the SWAN model to simulate waves in shallow sea areas

### 2.2. Key Model Parameter Selection

When applying the SWAN model for wave simulation, key parameters mainly include nonlinear interactions (DIA, discrete interaction approximation), wave breaking, whitecapping dissipation, and bottom friction. Based on previous research findings in global marine regions and the ESC [[28](https://www.mdpi.com/2077-1312/13/6/1196#B28-jmse-13-01196),[29](https://www.mdpi.com/2077-1312/13/6/1196#B29-jmse-13-01196),[30](https://www.mdpi.com/2077-1312/13/6/1196#B30-jmse-13-01196)], the settings for nonlinear interactions and wave-breaking parameters can typically adopt the default parameters of the SWAN model directly, as the errors between simulation results and actual observations are relatively small. However, whitecapping dissipation and bottom friction parameters require customized selection depending on regional hydrodynamic conditions (such as wind-wave characteristics) and seabed topography in marine areas [[31](https://www.mdpi.com/2077-1312/13/6/1196#B31-jmse-13-01196),[32](https://www.mdpi.com/2077-1312/13/6/1196#B32-jmse-13-01196)]. In this study, when applying the SWAN model for wave simulation in the ESC, particular emphasis was placed on selecting whitecapping dissipation and bottom friction parameters based on the wave characteristics of the ESC while retaining default settings for all other parameters.

#### 2.2.1. Whitecapping Dissipation Parameter Selection

Wave-breaking-induced energy dissipation plays a significant role in air–sea interactions [[32](https://www.mdpi.com/2077-1312/13/6/1196#B32-jmse-13-01196)]. The white foam formed on the ocean surface after wave breaking is referred to as “whitecaps.” Whitecapping dissipation is the energy dissipation process caused by wave breaking [[32](https://www.mdpi.com/2077-1312/13/6/1196#B32-jmse-13-01196)]. In the SWAN model, the primary whitecapping dissipation parameter options are the Westhuysen and Komen formulations [[33](https://www.mdpi.com/2077-1312/13/6/1196#B33-jmse-13-01196)]. To improve the accuracy of the SWAN model in simulating the wave field in the ECS, this study systematically evaluated the applicability of different whitecapping dissipation parameters within the model. Specifically, the Komen and Westhuysen whitecapping dissipation parameters were incorporated into the SWAN model, and the resulting simulation outcomes were compared and verified with existing observation data. The verification and comparison data were based on the SWIM (Surface Waves Investigation and Monitoring) dataset from January 2010 to October 2019, obtained from the AVISO (Archiving, Validation, and Interpretation of Satellite Oceanographic, [https://www.aviso.altimetry.fr/en/home.html](https://www.aviso.altimetry.fr/en/home.html) accessed on 10 December 2024) website. This dataset has a spatial resolution of 0.5° × 0.5°. Finally, an error analysis of the model was conducted using the mean absolute error (MAE) and root mean square error (RMSE).

#### 2.2.2. Bottom Friction Parameter Selection

The bottom friction parameter is a key parameter characterizing energy dissipation at the interface between waves and the seabed, and its value directly affects the simulation accuracy of the wave energy attenuation rate, wave height, and propagation characteristics [[22](https://www.mdpi.com/2077-1312/13/6/1196#B22-jmse-13-01196)]. The influence of bottom friction on wave evolution is highly significant, particularly in sea areas with broad and shallow shelves and complex seabed sediment types. Currently, the SWAN model’s primary selectable bottom friction parameters are Jonswap (the default scheme), Collins, and Madsen, and they primarily differ in terms of the different assumptions about seabed roughness and the interaction between the wave boundary layer [[34](https://www.mdpi.com/2077-1312/13/6/1196#B34-jmse-13-01196)]. To improve the accuracy of the SWAN model for simulating the wave field in the ECS, this study evaluated the applicability of different bottom friction parameters in the model. Specifically, the bottom friction parameters Jonswap, Collins, and Madsen were substituted into the SWAN model, and the obtained simulation results were compared and verified with existing observation data. The data sources utilized for verifying the aforementioned whitecapping dissipation parameters are consistent across all cases. Meanwhile, MAE and RMSE are employed to perform a comprehensive error analysis of the model.

### 2.3. Data Sources of Model

The water depth conditions of the ocean and the complex and variable seabed topography constitute the key factors affecting the propagation and dissipation of wave energy. To improve the spatial resolution of the topographic data, this study adopted the ETOPO1 global topographic dataset released by the National Oceanic and Atmospheric Administration (NOAA) of the United States. This dataset integrates topographic data from multiple sources, is updated regularly, and has a spatial resolution of 0.016 × 0.016°. However, limited by the errors in satellite altimetry and the differences between different data sources, specific accuracy errors exist in the topographic data. In particular, at the land-sea boundary, due to the complex and variable topography and the significant difficulty of measurement, these errors may be more significant, manifested as an increase in numerical deviation and an unclear land–water boundary [[35](https://www.mdpi.com/2077-1312/13/6/1196#B35-jmse-13-01196),[36](https://www.mdpi.com/2077-1312/13/6/1196#B36-jmse-13-01196)]. To overcome these challenges, this study used global information system (GIS) software ArcGIS 10.7 to fine-process the ETOPO1 dataset. Based on the spatial analysis and data correction techniques of GIS, the numerical deviation at the land-sea boundary was effectively reduced, making the land-sea boundary more precise and definite.

The wind field is the primary driving force behind ocean wave development and propagation. This study selected the latest data released by ERA5, a new atmospheric reanalysis tool developed by the European Centre for Medium-Range Weather Forecasts (ECMWF). The spatial resolution is 0.25° × 0.25°, and the time-frequency is 1 h. Compared with the previous generation of wind field data, these data are more accurate and are thus widely used [[28](https://www.mdpi.com/2077-1312/13/6/1196#B28-jmse-13-01196),[37](https://www.mdpi.com/2077-1312/13/6/1196#B37-jmse-13-01196)].

### 2.4. Model Control Conditions

The study simulation area is relatively wide (25–35° N, 120–130° E), and the period is long (from 2009 to 2023). The waves in the area are stable over a long time scale. The second-order upwind (SORDUP) differencing scheme, which incorporates second-order diffusion and is well suited for stable, long-term simulations, was selected for wave computation to accommodate large-scale computations under steady conditions [[38](https://www.mdpi.com/2077-1312/13/6/1196#B38-jmse-13-01196)]. This calculation method primarily considers spatial integration, does not consider time variables, and uses an iterative procedure. The second and third terms of Equation (2), representing x- and y-derivatives, respectively, are replaced by (4) and (5).

$$
\left(\frac{1.5 \left(c_{x} N\right)_{i x} - 2 \left(c_{x} N\right)_{i x - 1} + 0.5 \left(c_{x} N\right)_{i x - 2}}{\Delta x}\right)_{i y , i \sigma , i \theta}^{i t , n} ,
$$

(4)

$$
\left(\frac{1.5 \left(c_{y} N\right)_{i y} - 2 \left(c_{y} N\right)_{i y - 1} + 0.5 \left(c_{y} N\right)_{i y - 2}}{\Delta y}\right)_{i x , i \sigma , i \theta}^{i t , n} ,
$$

(5)

where it denotes the time layer identifier, n represents the number of iterations at each time layer, ix, iy, iσ, and iθ denote the labels in the x, y, σ, and θ directions, respectively, and Δx and Δy denote the spatial step sizes in the x and y directions [[38](https://www.mdpi.com/2077-1312/13/6/1196#B38-jmse-13-01196)].

In this study, the wave energy flux density was calculated using the TRANSP output from the SWAN model, with the final results including the directional components P x and P y representing energy transport per unit length in both directions [[38](https://www.mdpi.com/2077-1312/13/6/1196#B38-jmse-13-01196)].

$$
P_{w} = \sqrt{P_{x}^{2} + P_{y}^{2}}
$$

(6)

$$
P_{x} = \rho g \iint c_{x} S \left(f , \theta\right) d \theta d f
$$

(7)

$$
P_{y} = \rho g \iint c_{y} S \left(f , \theta\right) d \theta d f
$$

(8)

where $\rho$ represents the water density in kg/m 3, g denotes the acceleration due to gravity in m/s 2, c x and c y represent the x and y components of the group velocity of waves in m/s.

To enhance computational efficiency, this study employed a 0.05° resolution orthogonal grid as the computational grid for the SWAN model. The simulations assumed that waves were entirely wind generated within the study area, utilizing a hot-start approach where each year’s simulation was initialized using the previous year’s results, with a time step set to 1 h.

## 3. Results and Discussion

### 3.1. Model Validity Test

#### 3.1.1. Model Validity Testing Based on Whitecapping Dissipation Parameters

The SWH values derived from simulation calculations using two whitecapping dissipation parameters, namely Komen and Westhuysen, within the SWAN model were compared against the satellite-measured data obtained from the SWIM dataset. The comparative results are summarized in [Table 1](https://www.mdpi.com/2077-1312/13/6/1196#table_body_display_jmse-13-01196-t001). According to most existing studies, an RMSE value within the range of 0.1 m < RMSE < 0.5 m indicates a high degree of consistency between simulated and observed data [[21](https://www.mdpi.com/2077-1312/13/6/1196#B21-jmse-13-01196),[39](https://www.mdpi.com/2077-1312/13/6/1196#B39-jmse-13-01196),[40](https://www.mdpi.com/2077-1312/13/6/1196#B40-jmse-13-01196)]. As illustrated in [Table 1](https://www.mdpi.com/2077-1312/13/6/1196#table_body_display_jmse-13-01196-t001), the accuracy of simulations utilizing the Komen parameters surpasses that achieved with the Westhuysen parameter.

**Table 1.** Comparison of simulated significant wave height data with satellite-measured effective wave height data for the two whitecapping conditions of Komen and Westhuysen over the period 2010 to 2019.

The discrepancies in simulation results arising from applying different whitecapping dissipation parameters can be attributed to the computational principles underlying these parameters. The Westhuysen parameter, grounded in the “saturation-based approach” theory, is predominantly utilized for simulating mixed sea states in open ocean environments [[33](https://www.mdpi.com/2077-1312/13/6/1196#B33-jmse-13-01196)]. However, this parameter inadequately addresses boundary layer instability and the “directional spreading” effect in wave simulations, resulting in insufficient low-frequency energy and consequently impacting the precision of simulation results [[41](https://www.mdpi.com/2077-1312/13/6/1196#B41-jmse-13-01196)]. Conversely, the Komen parameter employs an empirical method based on wave steepness, modulating dissipation intensity through the dependence of spectral energy on frequency. This parameter exhibits robust performance across diverse marine environments, particularly excelling in fully developed sea states [[33](https://www.mdpi.com/2077-1312/13/6/1196#B33-jmse-13-01196)].

The ECS area is frequently impacted by typhoons, leading to frequent changes in the wind field. Prior research has demonstrated that employing the Komen parameter for wave simulations in the ESC can stably output reasonable wave heights and periods, even under complex typhoon paths and abrupt wind field variations [[42](https://www.mdpi.com/2077-1312/13/6/1196#B42-jmse-13-01196)]. This finding aligns with the conclusions of Li et al. [[4](https://www.mdpi.com/2077-1312/13/6/1196#B4-jmse-13-01196)] and Lin et al. [[43](https://www.mdpi.com/2077-1312/13/6/1196#B43-jmse-13-01196)]. This present study further substantiates the efficacy of the Komen parameter in wave modeling within the East China Sea, as evidenced by its reduced bias in significant wave height and enhanced simulation accuracy.

#### 3.1.2. Model Validity Testing Based on Bottom Friction Parameters

The SWH obtained from the simulation calculations using the three bottom friction parameters Jonswap (the default scheme), Collins, and Madsen in the SWAN model were compared with the satellite-measured data from the SWIM dataset. As shown in [Table 2](https://www.mdpi.com/2077-1312/13/6/1196#table_body_display_jmse-13-01196-t002), the accuracy of the simulation results obtained using the three bottom friction parameters, ranked from highest to lowest, is as follows: Collins > Jonswap > Madsen.

**Table 2.** Comparison of simulated significant wave height data with satellite-measured effective wave height data for the three bottom friction parameter conditions of Collins, Jonswap, and Madsen for the period 2010 to 2019.

The discrepancies in simulation results caused by applying different bottom friction parameters are primarily linked to the computational principles of these parameters. For instance, when calculating bottom friction coefficients, two critical parameters are involved: C b (bottom friction coefficient related to near-bed orbital motion) and U rms (root-mean-square velocity dependent on wave-induced near-bed water particle motion) [[43](https://www.mdpi.com/2077-1312/13/6/1196#B43-jmse-13-01196)]. For the Collins parameter, C b = C fw·gU rms, this formulation explicitly accounts for the influence of seabed topography on wave velocity, enabling accurate representation of realistic bottom boundary conditions [[34](https://www.mdpi.com/2077-1312/13/6/1196#B34-jmse-13-01196)]. For the Jonswap parameter, C b is fixed at 0.038 m 2/s 3. It was indicated that Jonswap may significantly underestimate energy dissipation in shallow, friction-dominated regions (water depth < 20 m) [[44](https://www.mdpi.com/2077-1312/13/6/1196#B44-jmse-13-01196)]. Based on linear wave theory, the Madsen parameter performs well for low-intensity, small-amplitude waves. However, in shallow-water environments where waves exhibit strong nonlinearity (e.g., wave steepening, flattening of troughs, wave–wave interactions), Madsen often fails to accurately capture nonlinear effects on bottom friction, leading to more significant errors in simulating highly nonlinear waves [[21](https://www.mdpi.com/2077-1312/13/6/1196#B21-jmse-13-01196)].

The study area (25–35° N, 120–130° E) encompasses complex topography, significant monsoonal and tidal influences, and dramatic depth variations (ranging from <10 m to >2000 m), with most regions <200 m depth. The Collins parameter was selected for its ability to adjust C b dynamically based on actual wave velocities and seabed topography, thereby improving energy dissipation accuracy. Li et al. also noted that Collins yielded optimal wave simulation results in the ESC using the SWAN model [[4](https://www.mdpi.com/2077-1312/13/6/1196#B4-jmse-13-01196)]. Notably, the MAE (mean absolute error) in this study is approximately twice that reported by Li et al. This discrepancy may stem from differences in wind field data: ERA5 data were used here, whereas Li et al. employed CCMP data. Wind field variations propagate through wave generation processes into bottom friction dissipation simulations [[45](https://www.mdpi.com/2077-1312/13/6/1196#B45-jmse-13-01196)], directly affecting the accuracy of the results.

#### 3.1.3. SWAN Model Parameter Settings

These results demonstrate that implementing the Komen whitecapping dissipation parameter and the Collins bottom friction parameter can substantially enhance the accuracy of the SWAN model in simulating the waves in the ECS. Furthermore, the simulated wave data can serve as a valuable supplement to the existing wave observation data. Therefore, the specific parameter settings of the SWAN model used in this study are listed in [Table 3](https://www.mdpi.com/2077-1312/13/6/1196#table_body_display_jmse-13-01196-t003).

**Table 3.** SWAN model parameter settings.

The simulated significant wave heights were compared with satellite observations in a scatter plot ([Figure 2](https://www.mdpi.com/2077-1312/13/6/1196#fig_body_display_jmse-13-01196-f002)), showing good agreement between model results and measurements. Based on 365 matched data points, the correlation coefficient reached 0.87. Consequently, this modeling scheme was adopted to simulate the spatiotemporal fields of significant wave height in the East China Sea during 2009–2023.

**Figure 2.** Comparison of significant wave height data simulated by SWAN and satellite observation data.

### 3.2. Numerical Simulation Results of Wave Parameters

#### 3.2.1. Characteristics of Wave Parameter Variations

According to the regulations of the internationally recognized Douglas Sea State Table ([https://www.douglashistory.co.uk/history/ships/sea_scale.htm](https://www.douglashistory.co.uk/history/ships/sea_scale.htm) accessed on 1 April 2025), when the SWH is in the range of 0.10–0.50 m, the waves are microwaves; when the SWH is in the range of 1.25–2.50 m, the waves are moderate; when the SWH is in the range of 2.50–4.00 m, the waves are significant [[47](https://www.mdpi.com/2077-1312/13/6/1196#B47-jmse-13-01196)].

The monthly average distribution and variation characteristics of the SWH and wave direction of the waves in the study area are shown in [Figure 3](https://www.mdpi.com/2077-1312/13/6/1196#fig_body_display_jmse-13-01196-f003). The monthly average SWH ranges from 0 to 3 m, with maximum values in autumn and winter and minimum values in spring and summer. Except for the months significantly affected by the winter (January) and summer (July) monsoons, in most months, the SWH exhibits a gradually increasing trend from the northwest to the southeast, reaches a peak near the Ryukyu Islands, and then decreases again in the open sea area.

**Figure 3.** Monthly significant wave height and direction distribution in the ESC, 2009–2023.

During winter (December to February of the following year), which is affected by the strong northwest monsoon, the wave activity significantly increases and generally exhibits an SWH. The SWH in 73.52% of the sea area exceeds 1.25 m. In December, the maximum value of the monthly average wave height throughout the year (2.5 m) was observed in the southwestern region of the study area near the Taiwan Strait, which is consistent with the buoy observation data of Xu et al. in the Taiwan Strait in 2017 [[48](https://www.mdpi.com/2077-1312/13/6/1196#B48-jmse-13-01196)]. In terms of wave direction, the wave directions in the ECS’s northern and central sea areas are primarily concentrated in the north and northwest directions. In contrast, the wave direction in the southern region of the ECS is mainly in the west and southwest directions.

The SWH generally decreases after entering spring (March–May), which is affected by the transition from winter to summer monsoons. Although the influence of the winter monsoon has not completely subsided in March, its contribution to the SWH is less than that during winter. Although some local sea areas (such as the northern sea area of the Ryukyu Islands) can maintain a relatively high SWH (2 m), overall, the wave height exhibits a downward trend. By May, the SWH in the fully developed sea area decreases to its lowest level throughout the year, generally lower than 1.25 m. During this period, the northward waves in the northern area of the ECS decrease and transform into northwestward waves; the average wave directions in the central and southern regions of the ECS change to the west direction.

In summer (June to August), the southeast monsoon prevails in the ECS [[49](https://www.mdpi.com/2077-1312/13/6/1196#B49-jmse-13-01196)]. The SWH in only 57.39% of the sea area is higher than 1.25 m, and the variation range of the wave height in the overall sea area is small; the wave directions over the entire sea area of the ECS change to the north and northwest directions.

In autumn (September to November), which is affected by the transition from the summer to the winter monsoon, particularly in October and November, the SWH in some sea areas reaches up to 2.5 m or higher. This is because the ECS region is typically affected by the combined effects of tropical cyclones and cold air, increasing the wind speed on the sea surface and promoting wave formation and energy accumulation [[50](https://www.mdpi.com/2077-1312/13/6/1196#B50-jmse-13-01196),[51](https://www.mdpi.com/2077-1312/13/6/1196#B51-jmse-13-01196)]. In addition, the average wave directions in the northern part of the ECS are west and northwest, the average wave direction in the central part of the ECS is west, and the average wave direction in the southern part of the ECS is west and southwest.

#### 3.2.2. Key Factors Influencing Wave Parameters Variability

Regions with low SWH in the study area primarily occur near the continental coast and islands, mainly due to strong energy dissipation caused by complex shoreline morphology and shallow water depths [[52](https://www.mdpi.com/2077-1312/13/6/1196#B52-jmse-13-01196)] and island sheltering effects [[53](https://www.mdpi.com/2077-1312/13/6/1196#B53-jmse-13-01196)]. In the Yangtze River Estuary and Hangzhou Bay, SWH remains low throughout the year, with monthly averages generally below 0.5 m. Similarly, significant SWH attenuation is observed near the Ryukyu Islands and the western coast of Kyushu Island, where island sheltering effects obstruct wave propagation paths and reduce wave intensity [[54](https://www.mdpi.com/2077-1312/13/6/1196#B54-jmse-13-01196),[55](https://www.mdpi.com/2077-1312/13/6/1196#B55-jmse-13-01196)]. This results in notably lower SWH values in the northwestern and southeastern Ryukyu Islands and the western coastal waters of Kyushu compared to other regions at the same latitude, unaffected by island sheltering [[53](https://www.mdpi.com/2077-1312/13/6/1196#B53-jmse-13-01196),[56](https://www.mdpi.com/2077-1312/13/6/1196#B56-jmse-13-01196)].

In contrast, high SWH values are predominantly observed in the northwestern Ryukyu Islands (approximately 28–31° N, 126–130° E), consistent with previous findings from SOM and EOF simulations [[50](https://www.mdpi.com/2077-1312/13/6/1196#B50-jmse-13-01196)]. This high-value zone arises because the northwestern Ryukyu Islands lie within the Okinawa Trough, where water depths exceed 2300 m [[57](https://www.mdpi.com/2077-1312/13/6/1196#B57-jmse-13-01196)]. Waves in this region experience minimal propagation resistance and rare breaking events, leading to low energy dissipation [[58](https://www.mdpi.com/2077-1312/13/6/1196#B58-jmse-13-01196)]. Additionally, the Kuroshio Current flows through this area, and its superposition with waves further amplifies wave energy, increasing SWH [[59](https://www.mdpi.com/2077-1312/13/6/1196#B59-jmse-13-01196)].

Notably, in the northern Taiwan Strait (approximately 25–26° N, 120–124° E), SWH is relatively low from April to August (0.5–1.5 m). However, a high-value SWH center (1.5–2.5 m) emerges from October to December due to frequent northeastern monsoon winds and autumn typhoon activity [[45](https://www.mdpi.com/2077-1312/13/6/1196#B45-jmse-13-01196)]. These results align with buoy-measured wave data in the northern strait [[30](https://www.mdpi.com/2077-1312/13/6/1196#B30-jmse-13-01196),[48](https://www.mdpi.com/2077-1312/13/6/1196#B48-jmse-13-01196)]. However, discrepancies exist between this study and previous reanalysis based on TOPEX/Poseidon (TP) satellite altimetry data. Earlier studies reported SWH peaks exceeding 3 m in January and October [[56](https://www.mdpi.com/2077-1312/13/6/1196#B56-jmse-13-01196)], higher than the values obtained here, though results for April and July show good agreement (SWH < 1.5 m). These differences may stem from spatiotemporal resolution variations in input data. TP satellite altimetry data, with a 10-day revisit cycle and 2.5° × 2.5° spatial resolution, were used for monthly SWH averaging in prior work [[56](https://www.mdpi.com/2077-1312/13/6/1196#B56-jmse-13-01196)]. In contrast, this study employed hourly wind field input data at 0.25° × 0.25° resolution. The higher temporal and spatial resolution likely enhances the accuracy of SWH representation.

### 3.3. Wave Energy Simulation Results and Discussion

#### 3.3.1. Characteristics of Wave Energy Variability

The spatial distribution and variation characteristics of the wave energy in the study area are shown in [Figure 4](https://www.mdpi.com/2077-1312/13/6/1196#fig_body_display_jmse-13-01196-f004). The wave energy flux density ranges from 0 to 12 kW/m and exhibits a gradually increasing trend from the northwest to the southeast sea area. The wave energy flux density is primarily affected by the wave height and period; thus, its distribution trend is consistent with the wave height [[59](https://www.mdpi.com/2077-1312/13/6/1196#B59-jmse-13-01196)], exhibiting low values near the shore and high values in the open sea. The wave energy flux density near the beach is relatively low, primarily due to the influence of intense energy dissipation caused by the complex shoreline and shallowing of the seabed topography [[60](https://www.mdpi.com/2077-1312/13/6/1196#B60-jmse-13-01196),[61](https://www.mdpi.com/2077-1312/13/6/1196#B61-jmse-13-01196)]. In open sea areas, due to the complete development of waves and the influence of wave input from the Pacific Ocean, the wave energy flux density is relatively high [[62](https://www.mdpi.com/2077-1312/13/6/1196#B62-jmse-13-01196)].

**Figure 4.** Regional wave energy flux density distribution in ECS.

Regarding interannual changes, the annual average wave energy flux density in the entire sea area of the ECS fluctuates significantly ([Figure 5](https://www.mdpi.com/2077-1312/13/6/1196#fig_body_display_jmse-13-01196-f005)). From 2009 to 2014, excluding 2013, the annual average wave energy flux density increased year by year, from 4.89 kW/m in 2009 to 6.22 kW/m in 2014; it decreased to approximately 4.9 kW/m in 2015 and 2016, then increased year by year to 5.83 kW/m (in 2018) and decreased to 5.04 kW/m in 2019; from 2020 to 2022, the fluctuation range of the annual average wave energy flux density was significantly smaller, with an average value of 5.37 ± 0.01 kW/m, which was relatively stable; it decreased to 5.22 kW/m in 2023.

**Figure 5.** Average annual wave energy flux density in the ECS from 2009 to 2023.

The wave energy flux density is critical in evaluating wave energy resources. An area with a wave energy flux density greater than 2 kW/m is assumed to be available [[63](https://www.mdpi.com/2077-1312/13/6/1196#B63-jmse-13-01196)]. The results show that the annual average energy flux density in most sea areas of the ECS exceeds 2 kW/m. In particular, in the northern part of the Ryukyu Islands, the annual average energy flux density remains above 8 kW/m, and the high values in most years are greater than 10 kW/m, reaching the highest value of 12 kW/m in 2014, indicating good development potential.

#### 3.3.2. Key Factors Influencing Wave Energy Variability

The high-value areas of wave energy flux density are primarily located in the western and northwestern regions of the Ryukyu Islands, as well as in the northern waters of Taiwan. Except for 2009, 2013, and 2022, which exhibited dual high-value centers of wave energy flux density, the high-value zones in other years were mainly concentrated in the western and northwestern parts of the Ryukyu Islands. This is attributed to the dramatic topographic variations around the Ryukyu Islands and the influence of Pacific waves and the Kuroshio Current [[64](https://www.mdpi.com/2077-1312/13/6/1196#B64-jmse-13-01196)], resulting in perennial high-value centers. In contrast, the northern Taiwan Strait forms high-value centers under the influence of frequent strong wind events such as typhoons [[48](https://www.mdpi.com/2077-1312/13/6/1196#B48-jmse-13-01196),[64](https://www.mdpi.com/2077-1312/13/6/1196#B64-jmse-13-01196)]. The enhanced sea surface wind speeds caused by typhoons are the direct reason for the higher wave energy flux density in the northern Taiwan Strait [[65](https://www.mdpi.com/2077-1312/13/6/1196#B65-jmse-13-01196)]. Studies have shown that the annual average wind speeds in the Taiwan Strait in 2009 and 2022 were significantly higher than in other years [[66](https://www.mdpi.com/2077-1312/13/6/1196#B66-jmse-13-01196)]. In 2013, the Taiwan Strait region experienced more than five typhoons, with gale days (10 min average wind speed ≥ 13.9 m/s) reaching as many as 15 [[67](https://www.mdpi.com/2077-1312/13/6/1196#B67-jmse-13-01196)].

Through 15 years (2009–2023) of high-resolution simulations, this study found that the interannual variability of wave energy flux density in the ESC exhibited anomalous decreases in certain years. For example, the annual average wave energy flux density in 2013, 2015, 2019, and 2023 showed abnormal reductions. Specifically, 2013 saw an 8.8% decrease compared to the previous year, while 2015 and 2019 experienced 21% and 14% declines, respectively. Comparing these findings with global climate change data, it was observed that super El Niño events occurred globally in 2015, 2019, and 2023 [[68](https://www.mdpi.com/2077-1312/13/6/1196#B68-jmse-13-01196),[69](https://www.mdpi.com/2077-1312/13/6/1196#B69-jmse-13-01196)]. Previous studies suggest that El Niño events caused abnormal ocean currents and significantly reduced tropical cyclone activity in the ESC, decreasing wave energy flux density [[60](https://www.mdpi.com/2077-1312/13/6/1196#B60-jmse-13-01196),[70](https://www.mdpi.com/2077-1312/13/6/1196#B70-jmse-13-01196)]. Additionally, the extreme heatwave event in eastern China in 2013 [[71](https://www.mdpi.com/2077-1312/13/6/1196#B71-jmse-13-01196)] has been linked to anomalous atmospheric circulation patterns during the heatwave, which may have caused local wind directions to oppose the dominant wave directions, creating a significant wave-wind cancellation effect [[72](https://www.mdpi.com/2077-1312/13/6/1196#B72-jmse-13-01196)]. This likely contributed to the decline in wave energy flux density in the ESC in 2013.

### 3.4. Stability Analysis of Wave Energy Results and Discussion

#### 3.4.1. Stability Analysis of Wave Energy

The analysis of wave energy variability in the East China Sea provides a crucial reference for assessing its renewable energy potential [[73](https://www.mdpi.com/2077-1312/13/6/1196#B73-jmse-13-01196)]. A stable energy source ensures normal operation and conversion efficiency of energy systems, making stability analysis essential.

The coefficient of variation (COV) was calculated annually for wave energy flux density, where lower COV values indicate higher energy stability [[74](https://www.mdpi.com/2077-1312/13/6/1196#B74-jmse-13-01196)]. The COV index can be expressed by the following equation [[75](https://www.mdpi.com/2077-1312/13/6/1196#B75-jmse-13-01196)]:

$$
C O V = \frac{\sigma}{\mu}
$$

where σ is the standard deviation, and μ is the mean value of the resource.

The spatial distribution of the coefficient of variation (COV) for wave energy in the East China Sea exhibits distinct regional characteristics. High COV values (>1.6) predominantly occur in three areas: east of the Ryukyu Islands, along the shelf break transition zone, and in the northeastern East China Sea, indicating significant wave energy variability ([Figure 6](https://www.mdpi.com/2077-1312/13/6/1196#fig_body_display_jmse-13-01196-f006)). In contrast, low COV zones (≤0.6) are concentrated in nearshore shallow waters, particularly from the Yangtze River estuary to the Fujian coast, where shorter fetch distances and topographic damping contribute to more stable wave conditions.

**Figure 6.** COV of wave energy flux density.

A notable spatial correlation exists between wave energy flux density (0–12 kW/m) and COV values. The wave energy flux density shows a gradual northwest-to-southeast increasing trend, which corresponds spatially with the COV distribution pattern. In the southeastern offshore regions, especially near the Ryukyu Islands, both wave energy flux density (reaching up to 12 kW/m) and COV values (generally > 1.6) are significantly elevated. Conversely, in coastal areas along mainland China (e.g., Yangtze Estuary to Fujian coast), lower wave energy flux density coincides with COV values typically below 0.6, reflecting relatively stable wave conditions.

Distinct regional patterns emerge in wave energy characteristics: the northern East China Sea demonstrates low wave energy flux density (<4 kW/m) coupled with high COV values (>1.6), while the north of Taiwan Strait exhibits high wave energy flux density (8–10 kW/m) with low COV values (<0.6). These contrasting regimes highlight the complex interplay between energy potential and stability across different marine environments of the East China Sea.

#### 3.4.2. Factors Affecting the Stability of Wave Energy Variation

The spatial distribution of the wave energy coefficient of variation (COV) in the East China Sea exhibits significant regional heterogeneity. According to the spatial patterns of COV and wave energy flux density, the area can be divided into four typical categories: high mean-high COV, high mean-low COV, low mean-low COV, and low mean-high COV.

The high mean-high COV region primarily encompasses the eastern waters of the Ryukyu Islands and the continental shelf break transition zone of East China Sea, with COV values generally exceeding 1.5. In the east of the Ryukyu Islands area, wave energy flux density is mainly controlled by the Kuroshio mainstream, where strong velocity shear interacting with island arc topography induces significant wave field variations, creating this region’s high variability characteristics [[57](https://www.mdpi.com/2077-1312/13/6/1196#B57-jmse-13-01196),[58](https://www.mdpi.com/2077-1312/13/6/1196#B58-jmse-13-01196),[59](https://www.mdpi.com/2077-1312/13/6/1196#B59-jmse-13-01196)]. The continental shelf break transition zone exhibits relatively high wave energy flux density due to fully developed waves and influences from Pacific wave inputs [[60](https://www.mdpi.com/2077-1312/13/6/1196#B60-jmse-13-01196)]. This region’s significant exposure to Pacific-originating waves makes it particularly susceptible to ENSO (El Niño–Southern Oscillation) effects, resulting in elevated COV values.

The high mean-low COV area is mainly located north of Taiwan, where annual energy input remains stable. The island’s sheltering effect reduces oceanic influences on wave variability, leading to lower COV values in this region [[74](https://www.mdpi.com/2077-1312/13/6/1196#B74-jmse-13-01196)].

The low mean-high COV zone predominantly covers the northeastern East China Sea at the northern edge of monsoon systems where air-sea coupling effects are pronounced. Winter cold surges generate short-period waves under limited fetch conditions, while summer typhoons produce extreme but spatiotemporally uneven energy inputs due to their variable tracks. This area lies within the oceanic frontal zone where the Yellow Sea Cold Water Mass meets the Tsushima Warm Current, causing wave field distortions through wave–current interactions [[75](https://www.mdpi.com/2077-1312/13/6/1196#B75-jmse-13-01196)]. These combined factors yield high variability but low wave energy density.

The low mean-low COV region concentrates along China’s coastal waters, where shorter fetch and topographic damping maintain stable yet low-energy wave conditions [[61](https://www.mdpi.com/2077-1312/13/6/1196#B61-jmse-13-01196),[62](https://www.mdpi.com/2077-1312/13/6/1196#B62-jmse-13-01196)].

## 4. Conclusions

Based on the third-generation wave model SWAN, this study used the ERA5 reanalysis wind field data from ECMWF and the ETOPO1 bathymetric data from NOAA to perform high-resolution simulations of the wave field in the ECS region from January 2009 to December 2023. The results are summarized as follows:

(1)
The simulated SWH is consistent with the satellite-measured data. In the ECS with a broad continental shelf and shallow water, the simulation results based on the Collins bottom friction parameter have higher accuracy than those based on the Jonswap and Madsen bottom friction parameters. The simulation results demonstrate that applying the whitecapping dissipation parameter Komen and the bottom friction parameter Collins produces an average RMSE of 0.374 m and 0.369 m, respectively, compared to satellite-measured data.

(2)
The ECS’s significant wave height (SWH) exhibits significant seasonal variation characteristics. It is higher in autumn and winter (from September to February of the following year) than in spring and summer. It exhibits a trend of gradually increasing from the northwest to the southeast. There is a long-term high-SWH in the northwest of the Ryukyu Islands, which may be due to the influence of the interaction among the Kuroshio current, waves from the Pacific Ocean, and topography. The high SWH in the northern part of the Taiwan Strait primarily appears during seasons with frequent, intense wind events, such as typhoons.

(3)
The annual average wave energy flux densities in most ECS sea areas exceed 2 kW/m, and the wave energy flux density is more significant in the open sea than in the nearshore area. In particular, in the northwestern sea area of the Ryukyu Islands, the high annual average energy flux density is generally greater than 10 kW/m, which can be regarded as a key sea area for wave energy development. The interannual variation of the wave energy flux density in the ECS is significantly affected by climate events such as El Niño and extreme heatwaves, which significantly decrease the wave energy flux density in some years. For example, the wave energy flux density 2015 decreased by 21% compared to 2014.

(4)
The spatial distribution of wave energy coefficient of variation (COV) in the East China Sea exhibits distinct regional differentiation, manifesting four characteristic combination patterns: high wave energy mean-high COV, high wave energy mean-low COV, low wave energy mean-high COV, and low wave energy mean-low COV. Notably, the eastern Ryukyu Islands and continental shelf break transition zone constitute a high wave energy mean-high COV region, where wave energy density exceeds 8 kW/m, and COV values generally surpass 1.5 due to the combined effects of Kuroshio’s strong shear flow and abrupt topographic changes. The northern Taiwan Strait demonstrates high wave energy mean-low COV characteristics, resulting from stable energy input by monsoon–Kuroshio interactions and topographic shielding effects. In contrast, the northeastern East China Sea exhibits low wave energy mean but high variability under the combined influences of cold surges, typhoon track fluctuations, and convergence of cold/warm water masses. Coastal areas along mainland China maintain both low wave energy mean and COV values owing to limited wind energy input and significant topographic dissipation.

## Author Contributions

Conceptualization, F.J., Z.M. and Q.Y.; investigation, S.M., Z.M. and W.C.; resources, Q.Y., F.J. and Z.M.; data curation, S.M.; writing—original draft preparation, S.M., F.J., Z.M. and Q.Y.; writing—review and editing, S.M., Q.Y., W.C., F.J. and Z.M.; visualization, S.M. and W.C.; supervision, F.J., Z.M. and Q.Y.; project administration, F.J. and Q.Y.; funding acquisition, Q.Y. All authors have read and agreed to the published version of the manuscript.

## Funding

This research was sponsored by the China National Scientific Seafloor Observatory (2017-000030-73-01-002437), the National Natural Science Foundation of China (40976025), the National Key Research and Development Program (2018YFC1405803), and the Ocean Negative Carbon Emissions (ONCE) Program.

## Data Availability Statement

## Acknowledgments

We thank all those who helped write this article and the editors and reviewers of this paper for their constructive feedback.

## Conflicts of Interest

The authors declare no conflicts of interest.

## References

1.   Babanin, A.V. Ocean Waves in Large-Scale Air-Sea Weather and Climate Systems. J. Geophys. Res.-Ocean.**2023**, 128, e2023JC019633. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Ocean+Waves+in+Large-Scale+Air-Sea+Weather+and+Climate+Systems&author=Babanin,+A.V.&publication_year=2023&journal=J.+Geophys.+Res.-Ocean.&volume=128&pages=e2023JC019633&doi=10.1029/2023JC019633)] [[CrossRef](https://doi.org/10.1029/2023JC019633)]
2.   Casas-Prat, M.; Hemer, M.A.; Dodet, G.; Morim, J.; Wang, X.L.; Mori, N.; Young, I.R.; Erikson, L.; Kamranzad, B.; Kumar, P.; et al. Wind-wave climate changes and their impacts. Nat. Rev. Earth Environ.**2024**, 5, 23–42. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Wind-wave+climate+changes+and+their+impacts&author=Casas-Prat,+M.&author=Hemer,+M.A.&author=Dodet,+G.&author=Morim,+J.&author=Wang,+X.L.&author=Mori,+N.&author=Young,+I.R.&author=Erikson,+L.&author=Kamranzad,+B.&author=Kumar,+P.&author=et+al.&publication_year=2024&journal=Nat.+Rev.+Earth+Environ.&volume=5&pages=23%E2%80%9342&doi=10.1038/s43017-023-00502-0)] [[CrossRef](https://doi.org/10.1038/s43017-023-00502-0)]
3.   Zhang, J.; Zhu, X.; Zhang, R.; Ren, J.; Wu, Y.; Liu, S.; Huang, D. Dissolved Fe in the East China Sea Under the Influences of Land Sources and the Boundary Current with Implications for Global Marginal Seas. Glob. Biogeochem. Cycle**2022**, 36, e2021GB006946. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Dissolved+Fe+in+the+East+China+Sea+Under+the+Influences+of+Land+Sources+and+the+Boundary+Current+with+Implications+for+Global+Marginal+Seas&author=Zhang,+J.&author=Zhu,+X.&author=Zhang,+R.&author=Ren,+J.&author=Wu,+Y.&author=Liu,+S.&author=Huang,+D.&publication_year=2022&journal=Glob.+Biogeochem.+Cycle&volume=36&pages=e2021GB006946&doi=10.1029/2021GB006946)] [[CrossRef](https://doi.org/10.1029/2021GB006946)]
4.   Li, G.; Zhang, H.; Lyu, T.; Zhang, H. Regional significant wave height forecast in the East China Sea based on the Self-Attention ConvLSTM with SWAN model. Ocean Eng.**2024**, 312, 119064. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Regional+significant+wave+height+forecast+in+the+East+China+Sea+based+on+the+Self-Attention+ConvLSTM+with+SWAN+model&author=Li,+G.&author=Zhang,+H.&author=Lyu,+T.&author=Zhang,+H.&publication_year=2024&journal=Ocean+Eng.&volume=312&pages=119064&doi=10.1016/j.oceaneng.2024.119064)] [[CrossRef](https://doi.org/10.1016/j.oceaneng.2024.119064)]
5.   Yang, H.; Li, Y.; Wang, J.; Ma, Y.; Xu, Z. Numerical modeling of an offshore shellfish farm exposed to extreme wave conditions. Front. Mar. Sci.**2024**, 11, 1452919. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Numerical+modeling+of+an+offshore+shellfish+farm+exposed+to+extreme+wave+conditions&author=Yang,+H.&author=Li,+Y.&author=Wang,+J.&author=Ma,+Y.&author=Xu,+Z.&publication_year=2024&journal=Front.+Mar.+Sci.&volume=11&pages=1452919&doi=10.3389/fmars.2024.1452919)] [[CrossRef](https://doi.org/10.3389/fmars.2024.1452919)]
6.   Sun, F.; Yang, J.; Cui, W. Accuracy Evaluation of Ocean Wave Spectra from Sentinel-1 SAR Based on Buoy Observations and ERA5 Data. Remote Sens.**2024**, 16, 987. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Accuracy+Evaluation+of+Ocean+Wave+Spectra+from+Sentinel-1+SAR+Based+on+Buoy+Observations+and+ERA5+Data&author=Sun,+F.&author=Yang,+J.&author=Cui,+W.&publication_year=2024&journal=Remote+Sens.&volume=16&pages=987&doi=10.3390/rs16060987)] [[CrossRef](https://doi.org/10.3390/rs16060987)]
7.   Beckman, J.N.; Long, J.W. Quantifying errors in wind and wave measurements from a compact, low-cost wave buoy. Front. Mar. Sci.**2022**, 9, 966855. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Quantifying+errors+in+wind+and+wave+measurements+from+a+compact,+low-cost+wave+buoy&author=Beckman,+J.N.&author=Long,+J.W.&publication_year=2022&journal=Front.+Mar.+Sci.&volume=9&pages=966855&doi=10.3389/fmars.2022.966855)] [[CrossRef](https://doi.org/10.3389/fmars.2022.966855)]
8.   Dzwonkowski, B.; Coogan, J.; Fournier, S.; Lockridge, G.; Park, K.; Lee, T. Compounding impact of severe weather events fuels marine heatwave in the coastal ocean. Nat. Commun.**2020**, 11, 4623. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Compounding+impact+of+severe+weather+events+fuels+marine+heatwave+in+the+coastal+ocean&author=Dzwonkowski,+B.&author=Coogan,+J.&author=Fournier,+S.&author=Lockridge,+G.&author=Park,+K.&author=Lee,+T.&publication_year=2020&journal=Nat.+Commun.&volume=11&pages=4623&doi=10.1038/s41467-020-18339-2)] [[CrossRef](https://doi.org/10.1038/s41467-020-18339-2)]
9.   Group, T.W. The WAM Model—A Third Generation Ocean Wave Prediction Model. J. Phys. Oceanogr.**1988**, 18, 1775–1810. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=The+WAM+Model%E2%80%94A+Third+Generation+Ocean+Wave+Prediction+Model&author=Group,+T.W.&publication_year=1988&journal=J.+Phys.+Oceanogr.&volume=18&pages=1775%E2%80%931810&doi=10.1175/1520-0485(1988)018%3C1775:TWMTGO%3E2.0.CO;2)] [[CrossRef](https://doi.org/10.1175/1520-0485(1988)018%3C1775:TWMTGO%3E2.0.CO;2)]
10.   Tolman, H.L. A Third-Generation Model for Wind Waves on Slowly Varying, Unsteady, and Inhomogeneous Depths and Currents. J. Phys. Oceanogr.**1991**, 21, 782–797. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=A+Third-Generation+Model+for+Wind+Waves+on+Slowly+Varying,+Unsteady,+and+Inhomogeneous+Depths+and+Currents&author=Tolman,+H.L.&publication_year=1991&journal=J.+Phys.+Oceanogr.&volume=21&pages=782%E2%80%93797&doi=10.1175/1520-0485(1991)021%3C0782:ATGMFW%3E2.0.CO;2)] [[CrossRef](https://doi.org/10.1175/1520-0485(1991)021%3C0782:ATGMFW%3E2.0.CO;2)]
11.   Booij, N.; Ris, R.C.; Holthuijsen, L.H. A third-generation wave model for coastal regions: 1. Model description and validation. J. Geophys. Res.-Ocean.**1999**, 104, 7649–7666. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=A+third-generation+wave+model+for+coastal+regions:+1.+Model+description+and+validation&author=Booij,+N.&author=Ris,+R.C.&author=Holthuijsen,+L.H.&publication_year=1999&journal=J.+Geophys.+Res.-Ocean.&volume=104&pages=7649%E2%80%937666&doi=10.1029/98JC02622)] [[CrossRef](https://doi.org/10.1029/98JC02622)]
12.   Björkqvist, J.V.; Vähä-Piikkiö, O.; Alari, V.; Kuznetsova, A.; Tuomi, L. WAM, SWAN and WAVEWATCH III in the Finnish archipelago—The effect of spectral performance on bulk wave parameters. J. Oper. Oceanogr.**2020**, 13, 55–70. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=WAM,+SWAN+and+WAVEWATCH+III+in+the+Finnish+archipelago%E2%80%94The+effect+of+spectral+performance+on+bulk+wave+parameters&author=Bj%C3%B6rkqvist,+J.V.&author=V%C3%A4h%C3%A4-Piikki%C3%B6,+O.&author=Alari,+V.&author=Kuznetsova,+A.&author=Tuomi,+L.&publication_year=2020&journal=J.+Oper.+Oceanogr.&volume=13&pages=55%E2%80%9370&doi=10.1080/1755876X.2019.1633236)] [[CrossRef](https://doi.org/10.1080/1755876X.2019.1633236)]
13.   Umesh, P.A.; Swain, J.; Balchand, A.N. Inter-comparison of WAM and WAVEWATCH-III in the North Indian Ocean using ERA-40 and QuikSCAT/NCEP blended winds. Ocean Eng.**2018**, 164, 298–321. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Inter-comparison+of+WAM+and+WAVEWATCH-III+in+the+North+Indian+Ocean+using+ERA-40+and+QuikSCAT/NCEP+blended+winds&author=Umesh,+P.A.&author=Swain,+J.&author=Balchand,+A.N.&publication_year=2018&journal=Ocean+Eng.&volume=164&pages=298%E2%80%93321&doi=10.1016/j.oceaneng.2018.06.053)] [[CrossRef](https://doi.org/10.1016/j.oceaneng.2018.06.053)]
14.   Shao, W.; Yu, W.; Jiang, X.; Shi, J.; Wei, Y.; Ji, Q. Analysis of Wave Distributions Using the WAVEWATCH-III Model in the Arctic Ocean. J. Ocean Univ.**2022**, 21, 15–27. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Analysis+of+Wave+Distributions+Using+the+WAVEWATCH-III+Model+in+the+Arctic+Ocean&author=Shao,+W.&author=Yu,+W.&author=Jiang,+X.&author=Shi,+J.&author=Wei,+Y.&author=Ji,+Q.&publication_year=2022&journal=J.+Ocean+Univ.&volume=21&pages=15%E2%80%9327&doi=10.1007/s11802-022-4811-y)] [[CrossRef](https://doi.org/10.1007/s11802-022-4811-y)]
15.   Wu, W.; Li, P.; Zhai, F.; Gu, Y.; Liu, Z. Evaluation of different wind resources in simulating wave height for the Bohai, Yellow, and East China Seas (BYES) with SWAN model. Cont. Shelf Res.**2020**, 207, 104217. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Evaluation+of+different+wind+resources+in+simulating+wave+height+for+the+Bohai,+Yellow,+and+East+China+Seas+(BYES)+with+SWAN+model&author=Wu,+W.&author=Li,+P.&author=Zhai,+F.&author=Gu,+Y.&author=Liu,+Z.&publication_year=2020&journal=Cont.+Shelf+Res.&volume=207&pages=104217&doi=10.1016/j.csr.2020.104217)] [[CrossRef](https://doi.org/10.1016/j.csr.2020.104217)]
16.   Ponce de León, S.; Bettencourt, J.; Van Vledder, G.; Doohan, P.; Higgins, C.; Guedes Soares, C.; Dias, F. Performance of WAVEWATCH-III and SWAN Models in the North Sea. In Proceedings of the International Conference on Ocean, Offshore and Arctic Engineering, Madrid, Spain, 17–22 June 2018. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Performance+of+WAVEWATCH-III+and+SWAN+Models+in+the+North+Sea&conference=Proceedings+of+the+International+Conference+on+Ocean,+Offshore+and+Arctic+Engineering&author=Ponce+de+Le%C3%B3n,+S.&author=Bettencourt,+J.&author=Van+Vledder,+G.&author=Doohan,+P.&author=Higgins,+C.&author=Guedes+Soares,+C.&author=Dias,+F.&publication_year=2018)]
17.   Cong, J.; Zhang, Y.; Hu, G.; Mi, B.; Kong, X.; Xue, B.; Ning, Z.; Yuan, Z. Textures, provenances, and transport patterns of sediment on the inner shelf of the East China Sea. Cont. Shelf Res.**2022**, 232, 104624. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Textures,+provenances,+and+transport+patterns+of+sediment+on+the+inner+shelf+of+the+East+China+Sea&author=Cong,+J.&author=Zhang,+Y.&author=Hu,+G.&author=Mi,+B.&author=Kong,+X.&author=Xue,+B.&author=Ning,+Z.&author=Yuan,+Z.&publication_year=2022&journal=Cont.+Shelf+Res.&volume=232&pages=104624&doi=10.1016/j.csr.2021.104624)] [[CrossRef](https://doi.org/10.1016/j.csr.2021.104624)]
18.   Xie, Y.; Guo, J.; Zhu, J.; Liu, X.; Li, G. Simulative Analysis on the Significant Wave Height over the East China Sea by SWAN Model with Jason-2 Satellite Altimetric Crossover Points. J. Ocean Technol.**2017**, 36, 24–30. (In Chinese) [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Simulative+Analysis+on+the+Significant+Wave+Height+over+the+East+China+Sea+by+SWAN+Model+with+Jason-2+Satellite+Altimetric+Crossover+Points&author=Xie,+Y.&author=Guo,+J.&author=Zhu,+J.&author=Liu,+X.&author=Li,+G.&publication_year=2017&journal=J.+Ocean+Technol.&volume=36&pages=24%E2%80%9330)]
19.   Liu, C.; Zheng, C.; Li, R.; Jia, Y. Statistics analysis of big wave frequency and extreme wave height in the East China Sea. Mar. Forecast.**2014**, 31, 8–13. (In Chinese) [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Statistics+analysis+of+big+wave+frequency+and+extreme+wave+height+in+the+East+China+Sea&author=Liu,+C.&author=Zheng,+C.&author=Li,+R.&author=Jia,+Y.&publication_year=2014&journal=Mar.+Forecast.&volume=31&pages=8%E2%80%9313)]
20.   Kutupoğlu, V.; Çakmak, R.E.; Akpınar, A.; van Vledder, G.P. Setup and evaluation of a SWAN wind wave model for the Sea of Marmara. Ocean Eng.**2018**, 165, 450–464. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Setup+and+evaluation+of+a+SWAN+wind+wave+model+for+the+Sea+of+Marmara&author=Kutupo%C4%9Flu,+V.&author=%C3%87akmak,+R.E.&author=Akp%C4%B1nar,+A.&author=van+Vledder,+G.P.&publication_year=2018&journal=Ocean+Eng.&volume=165&pages=450%E2%80%93464&doi=10.1016/j.oceaneng.2018.07.053)] [[CrossRef](https://doi.org/10.1016/j.oceaneng.2018.07.053)]
21.   Samiksha, S.V.; Jancy, L.; Sudheesh, K.; Kumar, V.S.; Shanas, P.R. Evaluation of wave growth and bottom friction parameterization schemes in the SWAN based on wave modelling for the central west coast of India. Ocean Eng.**2021**, 235, 109356. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Evaluation+of+wave+growth+and+bottom+friction+parameterization+schemes+in+the+SWAN+based+on+wave+modelling+for+the+central+west+coast+of+India&author=Samiksha,+S.V.&author=Jancy,+L.&author=Sudheesh,+K.&author=Kumar,+V.S.&author=Shanas,+P.R.&publication_year=2021&journal=Ocean+Eng.&volume=235&pages=109356&doi=10.1016/j.oceaneng.2021.109356)] [[CrossRef](https://doi.org/10.1016/j.oceaneng.2021.109356)]
22.   Nielsen, P. Coastal Bottom Boundary Layers and Sediment Transport; World Scientific: Singapore, 1992; Volume 4, p. 340. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Coastal+Bottom+Boundary+Layers+and+Sediment+Transport&author=Nielsen,+P.&publication_year=1992)]
23.   Wu, H.; Yan, P.; Hou, W.; Zhao, J.; Feng, G. Detection of Decadal Phase Transition and Early Warning Signals of PDO in Recent and Next 100 Years. Chin. J. Atmos. Sci.**2022**, 46, 225–236. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Detection+of+Decadal+Phase+Transition+and+Early+Warning+Signals+of+PDO+in+Recent+and+Next+100+Years&author=Wu,+H.&author=Yan,+P.&author=Hou,+W.&author=Zhao,+J.&author=Feng,+G.&publication_year=2022&journal=Chin.+J.+Atmos.+Sci.&volume=46&pages=225%E2%80%93236&doi=10.3878/j.issn.1006-9895.2108.20127)] [[CrossRef](https://doi.org/10.3878/j.issn.1006-9895.2108.20127)]
24.   Lu, Z.; Yuan, N.; Yang, Q.; Ma, Z.; Kurths, J. Early Warning of the Pacific Decadal Oscillation Phase Transition Using Complex Network Analysis. Geophys. Res. Lett.**2021**, 48, e2020GL091674. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Early+Warning+of+the+Pacific+Decadal+Oscillation+Phase+Transition+Using+Complex+Network+Analysis&author=Lu,+Z.&author=Yuan,+N.&author=Yang,+Q.&author=Ma,+Z.&author=Kurths,+J.&publication_year=2021&journal=Geophys.+Res.+Lett.&volume=48&pages=e2020GL091674&doi=10.1029/2020GL091674)] [[CrossRef](https://doi.org/10.1029/2020GL091674)]
25.   Ris, R.C.; Holthuijsen, L.H.; Booij, N. A third-generation wave model for coastal regions: 2. Verification. J. Geophys. Res.-Ocean.**1999**, 104, 7667–7681. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=A+third-generation+wave+model+for+coastal+regions:+2.+Verification&author=Ris,+R.C.&author=Holthuijsen,+L.H.&author=Booij,+N.&publication_year=1999&journal=J.+Geophys.+Res.-Ocean.&volume=104&pages=7667%E2%80%937681&doi=10.1029/1998JC900123)] [[CrossRef](https://doi.org/10.1029/1998JC900123)]
26.   Du, J.; Bolaños, R.; Guo Larsén, X. The use of a wave boundary layer model in SWAN. J. Geophys. Res.-Ocean.**2017**, 122, 42–62. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=The+use+of+a+wave+boundary+layer+model+in+SWAN&author=Du,+J.&author=Bola%C3%B1os,+R.&author=Guo+Lars%C3%A9n,+X.&publication_year=2017&journal=J.+Geophys.+Res.-Ocean.&volume=122&pages=42%E2%80%9362&doi=10.1002/2016JC012104)] [[CrossRef](https://doi.org/10.1002/2016JC012104)]
27.   Hasselmann, K.F.; Barnett, T.P.; Bouws, E.; Carlson, H.C.; Cartwright, D.E.; Enke, K.; Ewing, J.A.; Gienapp, H.; Hasselmann, D.E.; Kruseman, P.; et al. Measurements of wind-wave growth and swell decay during the Joint North Sea Wave Project (JONSWAP). Deut. Hydrogr. Z.**1973**, 8, 1–95. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Measurements+of+wind-wave+growth+and+swell+decay+during+the+Joint+North+Sea+Wave+Project+(JONSWAP)&author=Hasselmann,+K.F.&author=Barnett,+T.P.&author=Bouws,+E.&author=Carlson,+H.C.&author=Cartwright,+D.E.&author=Enke,+K.&author=Ewing,+J.A.&author=Gienapp,+H.&author=Hasselmann,+D.E.&author=Kruseman,+P.&author=et+al.&publication_year=1973&journal=Deut.+Hydrogr.+Z.&volume=8&pages=1%E2%80%9395)]
28.   Amarouche, K.; Akpınar, A.; Rybalko, A.; Myslenkov, S. Assessment of SWAN and WAVEWATCH-III models regarding the directional wave spectra estimates based on Eastern Black Sea measurements. Ocean Eng.**2023**, 272, 113944. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Assessment+of+SWAN+and+WAVEWATCH-III+models+regarding+the+directional+wave+spectra+estimates+based+on+Eastern+Black+Sea+measurements&author=Amarouche,+K.&author=Akp%C4%B1nar,+A.&author=Rybalko,+A.&author=Myslenkov,+S.&publication_year=2023&journal=Ocean+Eng.&volume=272&pages=113944&doi=10.1016/j.oceaneng.2023.113944)] [[CrossRef](https://doi.org/10.1016/j.oceaneng.2023.113944)]
29.   Lee, H. Evaluation of WAVEWATCH III performance with wind input and dissipation source terms using wave buoy measurements for October 2006 along the east Korean coast in the East Sea. Ocean Eng.**2015**, 100, 67–82. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Evaluation+of+WAVEWATCH+III+performance+with+wind+input+and+dissipation+source+terms+using+wave+buoy+measurements+for+October+2006+along+the+east+Korean+coast+in+the+East+Sea&author=Lee,+H.&publication_year=2015&journal=Ocean+Eng.&volume=100&pages=67%E2%80%9382&doi=10.1016/j.oceaneng.2015.03.009)] [[CrossRef](https://doi.org/10.1016/j.oceaneng.2015.03.009)]
30.   Zheng, K.; Osinowo, A.A.; Sun, J.; Hu, W. Long-Term Characterization of Sea Conditions in the East China Sea Using Significant Wave Height and Wind Speed. J. Ocean Univ.**2018**, 17, 733–743. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Long-Term+Characterization+of+Sea+Conditions+in+the+East+China+Sea+Using+Significant+Wave+Height+and+Wind+Speed&author=Zheng,+K.&author=Osinowo,+A.A.&author=Sun,+J.&author=Hu,+W.&publication_year=2018&journal=J.+Ocean+Univ.&volume=17&pages=733%E2%80%93743&doi=10.1007/s11802-018-3484-z)] [[CrossRef](https://doi.org/10.1007/s11802-018-3484-z)]
31.   Sun, W.; Liang, B.; Shao, Z.; Wang, Z. Analysis of Komen scheme in the SWAN model for the whitecapping dissipation during the tropical cyclone. Ocean Eng.**2022**, 266, 113060. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Analysis+of+Komen+scheme+in+the+SWAN+model+for+the+whitecapping+dissipation+during+the+tropical+cyclone&author=Sun,+W.&author=Liang,+B.&author=Shao,+Z.&author=Wang,+Z.&publication_year=2022&journal=Ocean+Eng.&volume=266&pages=113060&doi=10.1016/j.oceaneng.2022.113060)] [[CrossRef](https://doi.org/10.1016/j.oceaneng.2022.113060)]
32.   Wang, H.; Yang, Y.; Sun, B.; Shi, Y. Improvements to the statistical theoretical model for wave breaking based on the ratio of breaking wave kinetic and potential energy. Sci. China-Earth Sci.**2017**, 60, 180–187. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Improvements+to+the+statistical+theoretical+model+for+wave+breaking+based+on+the+ratio+of+breaking+wave+kinetic+and+potential+energy&author=Wang,+H.&author=Yang,+Y.&author=Sun,+B.&author=Shi,+Y.&publication_year=2017&journal=Sci.+China-Earth+Sci.&volume=60&pages=180%E2%80%93187&doi=10.1007/s11430-016-0053-3)] [[CrossRef](https://doi.org/10.1007/s11430-016-0053-3)]
33.   Allahdadi, M.N.; He, R.; Neary, V.S. Predicting ocean waves along the US east coast during energetic winter storms: Sensitivity to whitecapping parameterizations. Ocean Sci.**2019**, 15, 691–715. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Predicting+ocean+waves+along+the+US+east+coast+during+energetic+winter+storms:+Sensitivity+to+whitecapping+parameterizations&author=Allahdadi,+M.N.&author=He,+R.&author=Neary,+V.S.&publication_year=2019&journal=Ocean+Sci.&volume=15&pages=691%E2%80%93715&doi=10.5194/os-15-691-2019)] [[CrossRef](https://doi.org/10.5194/os-15-691-2019)]
34.   Collins, J.I. Prediction of shallow-water spectra. J. Geophys. Res.**1972**, 77, 2693–2707. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Prediction+of+shallow-water+spectra&author=Collins,+J.I.&publication_year=1972&journal=J.+Geophys.+Res.&volume=77&pages=2693%E2%80%932707&doi=10.1029/JC077i015p02693)] [[CrossRef](https://doi.org/10.1029/JC077i015p02693)]
35.   Shum, C.K.; Ries, J.C.; Tapley, B.D. The accuracy and applications of satellite altimetry. Geophys. J. Int.**1995**, 121, 321–336. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=The+accuracy+and+applications+of+satellite+altimetry&author=Shum,+C.K.&author=Ries,+J.C.&author=Tapley,+B.D.&publication_year=1995&journal=Geophys.+J.+Int.&volume=121&pages=321%E2%80%93336&doi=10.1111/j.1365-246X.1995.tb05714.x)] [[CrossRef](https://doi.org/10.1111/j.1365-246X.1995.tb05714.x)]
36.   Bašić, T. Introductory Chapter: Satellite Altimetry—Overview. In Satellite Altimetry; Bašić, T., Ed.; IntechOpen: Rijeka, Croatia, 2023; pp. 1–131. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Introductory+Chapter:+Satellite+Altimetry%E2%80%94Overview&author=Ba%C5%A1i%C4%87,+T.&publication_year=2023&pages=1%E2%80%93131)]
37.   van Eeden, F.; Klonaris, G.; Verbeurgt, J.; Troch, P.; De Wulf, A. Sensitivities in Wind Driven Spectral Wave Modelling for the Belgian Coast. J. Mar. Sci. Eng.**2022**, 10, 1138. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Sensitivities+in+Wind+Driven+Spectral+Wave+Modelling+for+the+Belgian+Coast&author=van+Eeden,+F.&author=Klonaris,+G.&author=Verbeurgt,+J.&author=Troch,+P.&author=De+Wulf,+A.&publication_year=2022&journal=J.+Mar.+Sci.+Eng.&volume=10&pages=1138&doi=10.3390/jmse10081138)] [[CrossRef](https://doi.org/10.3390/jmse10081138)]
38.   Team, T.S. SWAN Cycle III version 41.51. SWAN Tech. Doc.**2024**, 1–149. Available online: [https://swanmodel.sourceforge.io/download/zip/swanuse.pdf](https://swanmodel.sourceforge.io/download/zip/swanuse.pdf) (accessed on 10 December 2024).
39.   Zhang, W.; Zhao, H.; Chen, G.; Yang, J. Assessing the performance of SWAN model for wave simulations in the Bay of Bengal. Ocean Eng.**2023**, 285, 115295. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Assessing+the+performance+of+SWAN+model+for+wave+simulations+in+the+Bay+of+Bengal&author=Zhang,+W.&author=Zhao,+H.&author=Chen,+G.&author=Yang,+J.&publication_year=2023&journal=Ocean+Eng.&volume=285&pages=115295&doi=10.1016/j.oceaneng.2023.115295)] [[CrossRef](https://doi.org/10.1016/j.oceaneng.2023.115295)]
40.   Tian, Z.; Zhang, Y. Numerical estimation of the typhoon-induced wind and wave fields in Taiwan Strait. Ocean Eng.**2021**, 239, 109803. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Numerical+estimation+of+the+typhoon-induced+wind+and+wave+fields+in+Taiwan+Strait&author=Tian,+Z.&author=Zhang,+Y.&publication_year=2021&journal=Ocean+Eng.&volume=239&pages=109803&doi=10.1016/j.oceaneng.2021.109803)] [[CrossRef](https://doi.org/10.1016/j.oceaneng.2021.109803)]
41.   Christakos, K.; Björkqvist, J.; Tuomi, L.; Furevik, B.R.; Breivik, Ø. Modelling wave growth in narrow fetch geometries: The white-capping and wind input formulations. Ocean. Model.**2021**, 157, 101730. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Modelling+wave+growth+in+narrow+fetch+geometries:+The+white-capping+and+wind+input+formulations&author=Christakos,+K.&author=Bj%C3%B6rkqvist,+J.&author=Tuomi,+L.&author=Furevik,+B.R.&author=Breivik,+%C3%98.&publication_year=2021&journal=Ocean.+Model.&volume=157&pages=101730&doi=10.1016/j.ocemod.2020.101730)] [[CrossRef](https://doi.org/10.1016/j.ocemod.2020.101730)]
42.   Ji, Y.; Zhu, Y.; Li, L.; He, Z.; Shen, H.; Li, X. Study on the parameters adaptability of typhoon wave model in Zhejiang coastal area. Mar. Forecast.**2023**, 40, 22–31. (In Chinese) [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Study+on+the+parameters+adaptability+of+typhoon+wave+model+in+Zhejiang+coastal+area&author=Ji,+Y.&author=Zhu,+Y.&author=Li,+L.&author=He,+Z.&author=Shen,+H.&author=Li,+X.&publication_year=2023&journal=Mar.+Forecast.&volume=40&pages=22%E2%80%9331&doi=10.11737/j.issn.1003-0239.2023.02.003)] [[CrossRef](https://doi.org/10.11737/j.issn.1003-0239.2023.02.003)]
43.   Lin, Y.; Liu, Y.; Wang, X.; Lu, P.; Yang, Z.; Dong, S. Study on the calibration of wave field simulation in the China adjacent sea based on SWAN model. Trans. Oceanol. Limnol.**2024**, 46, 1–10. (In Chinese) [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Study+on+the+calibration+of+wave+field+simulation+in+the+China+adjacent+sea+based+on+SWAN+model&author=Lin,+Y.&author=Liu,+Y.&author=Wang,+X.&author=Lu,+P.&author=Yang,+Z.&author=Dong,+S.&publication_year=2024&journal=Trans.+Oceanol.+Limnol.&volume=46&pages=1%E2%80%9310&doi=10.13984/j.cnki.cn37-1141.2024.04.001)] [[CrossRef](https://doi.org/10.13984/j.cnki.cn37-1141.2024.04.001)]
44.   Zijlema, M.; van Vledder, G.P.; Holthuijsen, L.H. Bottom friction and wind drag for wave models. Coast. Eng.**2012**, 65, 19–26. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Bottom+friction+and+wind+drag+for+wave+models&author=Zijlema,+M.&author=van+Vledder,+G.P.&author=Holthuijsen,+L.H.&publication_year=2012&journal=Coast.+Eng.&volume=65&pages=19%E2%80%9326&doi=10.1016/j.coastaleng.2012.03.002)] [[CrossRef](https://doi.org/10.1016/j.coastaleng.2012.03.002)]
45.   Chen, X.; Ni, Y.; Shen, Y.; Ying, Y.; Wang, J. The research on the applicability of different typhoon wind fields in the simulation of typhoon waves in China’s coastal waters. Front. Mar. Sci.**2024**, 11, 1492521. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=The+research+on+the+applicability+of+different+typhoon+wind+fields+in+the+simulation+of+typhoon+waves+in+China%E2%80%99s+coastal+waters&author=Chen,+X.&author=Ni,+Y.&author=Shen,+Y.&author=Ying,+Y.&author=Wang,+J.&publication_year=2024&journal=Front.+Mar.+Sci.&volume=11&pages=1492521&doi=10.3389/fmars.2024.1492521)] [[CrossRef](https://doi.org/10.3389/fmars.2024.1492521)]
46.   Komen, G.; Hasselmann, K. On the Existence of a Fully Developed Wind-Sea Spectrum. J. Phys. Oceanogr.**1984**, 14, 1271–1285. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=On+the+Existence+of+a+Fully+Developed+Wind-Sea+Spectrum&author=Komen,+G.&author=Hasselmann,+K.&publication_year=1984&journal=J.+Phys.+Oceanogr.&volume=14&pages=1271%E2%80%931285&doi=10.1175/1520-0485(1984)014%3C1271:OTEOAF%3E2.0.CO;2)] [[CrossRef](https://doi.org/10.1175/1520-0485(1984)014%3C1271:OTEOAF%3E2.0.CO;2)]
47.   Morrisey, D.J.; Inglis, G.J.; Tait, L.W.; Woods, C.M.C.; Lewis, J.F.; Georgiades, E.T. Procedures for Evaluating in-Water Systems to Remove or Treat Vessel Biofouling; Ministry for Primary Industries: Manatū Ahu Matua, New Zealand, 2015; pp. 1–104. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Procedures+for+Evaluating+in-Water+Systems+to+Remove+or+Treat+Vessel+Biofouling&author=Morrisey,+D.J.&author=Inglis,+G.J.&author=Tait,+L.W.&author=Woods,+C.M.C.&author=Lewis,+J.F.&author=Georgiades,+E.T.&publication_year=2015)] [[CrossRef](https://doi.org/10.13140/RG.2.1.4025.8648)]
48.   Xu, X.; Tao, A.; Li, X.; Zheng, X.; Lin, Y. Analysis of Wave Characteristics in the Central Taiwan Strait Based on Measured Data. J. Trop. Oceanogr.**2021**, 40, 12–20. (In Chinese) [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Analysis+of+Wave+Characteristics+in+the+Central+Taiwan+Strait+Based+on+Measured+Data&author=Xu,+X.&author=Tao,+A.&author=Li,+X.&author=Zheng,+X.&author=Lin,+Y.&publication_year=2021&journal=J.+Trop.+Oceanogr.&volume=40&pages=12%E2%80%9320&doi=10.11978/2020035)] [[CrossRef](https://doi.org/10.11978/2020035)]
49.   Qian, J.; Lu, M.; Sui, C. Evolution of South China Sea and East Asian monsoon from spring to summer by the progression of daily weather types. Int. J. Climatol.**2022**, 42, 3633–3647. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Evolution+of+South+China+Sea+and+East+Asian+monsoon+from+spring+to+summer+by+the+progression+of+daily+weather+types&author=Qian,+J.&author=Lu,+M.&author=Sui,+C.&publication_year=2022&journal=Int.+J.+Climatol.&volume=42&pages=3633%E2%80%933647&doi=10.1002/joc.7436)] [[CrossRef](https://doi.org/10.1002/joc.7436)]
50.   Hisaki, Y. Swell and wind-wave height variability in the East China Sea. Ocean Dyn.**2023**, 73, 493–515. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Swell+and+wind-wave+height+variability+in+the+East+China+Sea&author=Hisaki,+Y.&publication_year=2023&journal=Ocean+Dyn.&volume=73&pages=493%E2%80%93515&doi=10.1007/s10236-023-01552-0)] [[CrossRef](https://doi.org/10.1007/s10236-023-01552-0)]
51.   Yamaguchi, M.; Maeda, S. Increase in the Number of Tropical Cyclones Approaching Tokyo since 1980. J. Meteorol. Soc. Jpn.**2020**, 98, 775–786. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Increase+in+the+Number+of+Tropical+Cyclones+Approaching+Tokyo+since+1980&author=Yamaguchi,+M.&author=Maeda,+S.&publication_year=2020&journal=J.+Meteorol.+Soc.+Jpn.&volume=98&pages=775%E2%80%93786&doi=10.2151/jmsj.2020-039)] [[CrossRef](https://doi.org/10.2151/jmsj.2020-039)]
52.   Zhang, S.; Zhang, Z.; Hong, q.; Guo, H. Correlation between complexity of coastal geomorphology and the dissipation of tidal energy- A case study of Zhoushan Islands in Hangzhou Bay. Authorea**2023**. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Correlation+between+complexity+of+coastal+geomorphology+and+the+dissipation+of+tidal+energy-+A+case+study+of+Zhoushan+Islands+in+Hangzhou+Bay&author=Zhang,+S.&author=Zhang,+Z.&author=Hong,+q.&author=Guo,+H.&publication_year=2023&journal=Authorea&doi=10.22541/au.169142771.15368683/v1)] [[CrossRef](https://doi.org/10.22541/au.169142771.15368683/v1)]
53.   Shi, Y.; Yang, D.; Yin, B. The effect of background flow shear on the topographic Rossby wave. J. Oceanogr.**2020**, 76, 307–315. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=The+effect+of+background+flow+shear+on+the+topographic+Rossby+wave&author=Shi,+Y.&author=Yang,+D.&author=Yin,+B.&publication_year=2020&journal=J.+Oceanogr.&volume=76&pages=307%E2%80%93315&doi=10.1007/s10872-020-00546-6)] [[CrossRef](https://doi.org/10.1007/s10872-020-00546-6)]
54.   Ponce de León, S.; Guedes Soares, C. On the sheltering effect of islands in ocean wave models. J. Geophys. Res.-Ocean.**2005**, 110. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=On+the+sheltering+effect+of+islands+in+ocean+wave+models&author=Ponce+de+Le%C3%B3n,+S.&author=Guedes+Soares,+C.&publication_year=2005&journal=J.+Geophys.+Res.-Ocean.&volume=110&doi=10.1029/2004JC002682)] [[CrossRef](https://doi.org/10.1029/2004JC002682)]
55.   Pacaldo, J.C.; Bilgera, P.H.T.; Abundo, M.L.S. Nearshore Wave Energy Resource Assessment for Off-Grid Islands: A Case Study in Cuyo Island, Palawan, Philippines. Energies**2022**, 15, 8637. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Nearshore+Wave+Energy+Resource+Assessment+for+Off-Grid+Islands:+A+Case+Study+in+Cuyo+Island,+Palawan,+Philippines&author=Pacaldo,+J.C.&author=Bilgera,+P.H.T.&author=Abundo,+M.L.S.&publication_year=2022&journal=Energies&volume=15&pages=8637&doi=10.3390/en15228637)] [[CrossRef](https://doi.org/10.3390/en15228637)]
56.   He, H.; Song, J.; Bai, Y.; Xu, Y.; Wang, J.; Bi, F. Climate and extrema of ocean waves in the East China Sea. Sci. China-Earth Sci.**2018**, 61, 980–994. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Climate+and+extrema+of+ocean+waves+in+the+East+China+Sea&author=He,+H.&author=Song,+J.&author=Bai,+Y.&author=Xu,+Y.&author=Wang,+J.&author=Bi,+F.&publication_year=2018&journal=Sci.+China-Earth+Sci.&volume=61&pages=980%E2%80%93994&doi=10.1007/s11430-017-9156-7)] [[CrossRef](https://doi.org/10.1007/s11430-017-9156-7)]
57.   Chen, S.; Lin, J.; Su, C.; Doo, W. Introduction to the special issue on tectonic environment and seabed resources of the southern Okinawa Trough. Terr. Atmos. Ocean Sci.**2019**, 30, 605–611. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Introduction+to+the+special+issue+on+tectonic+environment+and+seabed+resources+of+the+southern+Okinawa+Trough&author=Chen,+S.&author=Lin,+J.&author=Su,+C.&author=Doo,+W.&publication_year=2019&journal=Terr.+Atmos.+Ocean+Sci.&volume=30&pages=605%E2%80%93611&doi=10.3319/TAO.2019.08.27.01)] [[CrossRef](https://doi.org/10.3319/TAO.2019.08.27.01)]
58.   Webb, P. Introduction to Oceanography; Rebus Community: Minneapolis, MN, USA, 2020. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Introduction+to+Oceanography&author=Webb,+P.&publication_year=2020)]
59.   Zhu, X.; Park, J.; Wimbush, M.; Yang, C. Comment on “Current system east of the Ryukyu Islands” by A. Nagano et al. J. Geophys. Res.-Ocean.**2008**, 113. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Comment+on+%E2%80%9CCurrent+system+east+of+the+Ryukyu+Islands%E2%80%9D+by+A.+Nagano+et+al&author=Zhu,+X.&author=Park,+J.&author=Wimbush,+M.&author=Yang,+C.&publication_year=2008&journal=J.+Geophys.+Res.-Ocean.&volume=113&doi=10.1029/2007JC004458)] [[CrossRef](https://doi.org/10.1029/2007JC004458)]
60.   Zheng, C.; Li, C. Variation of the wave energy and significant wave height in the China Sea and adjacent waters. Renew. Sust. Energ. Rev.**2015**, 43, 381–387. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Variation+of+the+wave+energy+and+significant+wave+height+in+the+China+Sea+and+adjacent+waters&author=Zheng,+C.&author=Li,+C.&publication_year=2015&journal=Renew.+Sust.+Energ.+Rev.&volume=43&pages=381%E2%80%93387&doi=10.1016/j.rser.2014.11.001)] [[CrossRef](https://doi.org/10.1016/j.rser.2014.11.001)]
61.   Navarro, W.; Orfila, A.; Orejarena-Rondón, A.; Velez, J.C.; Lonin, S. Wave Energy Dissipation in a Shallow Coral Reef Lagoon Using Marine X-Band Radar Data. J. Geophys. Res.-Ocean.**2021**, 126, e2020JC017094. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Wave+Energy+Dissipation+in+a+Shallow+Coral+Reef+Lagoon+Using+Marine+X-Band+Radar+Data&author=Navarro,+W.&author=Orfila,+A.&author=Orejarena-Rond%C3%B3n,+A.&author=Velez,+J.C.&author=Lonin,+S.&publication_year=2021&journal=J.+Geophys.+Res.-Ocean.&volume=126&pages=e2020JC017094&doi=10.1029/2020JC017094)] [[CrossRef](https://doi.org/10.1029/2020JC017094)]
62.   Chen, J.; Ralston, D.K.; Geyer, W.R.; Sommerfield, C.K.; Chant, R.J. Wave Generation, Dissipation, and Disequilibrium in an Embayment with Complex Bathymetry. J. Geophys. Res.-Ocean.**2018**, 123, 7856–7876. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Wave+Generation,+Dissipation,+and+Disequilibrium+in+an+Embayment+with+Complex+Bathymetry&author=Chen,+J.&author=Ralston,+D.K.&author=Geyer,+W.R.&author=Sommerfield,+C.K.&author=Chant,+R.J.&publication_year=2018&journal=J.+Geophys.+Res.-Ocean.&volume=123&pages=7856%E2%80%937876&doi=10.1029/2018JC014381)] [[CrossRef](https://doi.org/10.1029/2018JC014381)]
63.   Chu, T. Exploitation and Utilization of Ocean Energy; Chemical Industry Press: Beijing, China, 2005. (In Chinese) [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Exploitation+and+Utilization+of+Ocean+Energy&author=Chu,+T.&publication_year=2005)]
64.   Shi, H.; Zhang, X.; Du, W.; Li, Q.; Qu, H.; You, Z. Assessment of Wave Energy Resources in China. J. Mar. Sci. Eng.**2022**, 10, 1771. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Assessment+of+Wave+Energy+Resources+in+China&author=Shi,+H.&author=Zhang,+X.&author=Du,+W.&author=Li,+Q.&author=Qu,+H.&author=You,+Z.&publication_year=2022&journal=J.+Mar.+Sci.+Eng.&volume=10&pages=1771&doi=10.3390/jmse10111771)] [[CrossRef](https://doi.org/10.3390/jmse10111771)]
65.   Chen, C.; Peng, C.; Xiao, H.; Wei, M.; Wang, T. Typhoon field construction and wind-induced wave model optimization based on topographic parameters. Terr. Atmos. Ocean Sci.**2023**, 34, 2. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Typhoon+field+construction+and+wind-induced+wave+model+optimization+based+on+topographic+parameters&author=Chen,+C.&author=Peng,+C.&author=Xiao,+H.&author=Wei,+M.&author=Wang,+T.&publication_year=2023&journal=Terr.+Atmos.+Ocean+Sci.&volume=34&pages=2&doi=10.1007/s44195-023-00034-6)] [[CrossRef](https://doi.org/10.1007/s44195-023-00034-6)]
66.   Wen, C.; Wang, Z.; Zou, J. Analysis of temporal and spatial characteristics of sea surface wind field in Taiwan Strait based on CCMP. Haiyang Xuebao**2024**, 46, 65–78. (In Chinese) [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Analysis+of+temporal+and+spatial+characteristics+of+sea+surface+wind+field+in+Taiwan+Strait+based+on+CCMP&author=Wen,+C.&author=Wang,+Z.&author=Zou,+J.&publication_year=2024&journal=Haiyang+Xuebao&volume=46&pages=65%E2%80%9378&doi=10.12284/hyxb2024023)] [[CrossRef](https://doi.org/10.12284/hyxb2024023)]
67.   Lin, X.; Wu, X.; Chen, M.; Li, Y.; Liu, J.; Chen, B. Characteristics of strong typhoon wind and typical cases of extreme wind on the west coast of the Taiwan Strait, China. J. Meteorol. Environ.**2019**, 35, 93–100. (In Chinese) [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Characteristics+of+strong+typhoon+wind+and+typical+cases+of+extreme+wind+on+the+west+coast+of+the+Taiwan+Strait,+China&author=Lin,+X.&author=Wu,+X.&author=Chen,+M.&author=Li,+Y.&author=Liu,+J.&author=Chen,+B.&publication_year=2019&journal=J.+Meteorol.+Environ.&volume=35&pages=93%E2%80%93100)]
68.   Tan, W.; Hu, Z.; McPhaden, M.J.; Zhu, C.; Li, X.; Liu, Y. On the Divergent Evolution of ENSO After the Coastal El Niños in 2017 and 2023. Geophys. Res. Lett.**2024**, 51, e2024GL108198. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=On+the+Divergent+Evolution+of+ENSO+After+the+Coastal+El+Ni%C3%B1os+in+2017+and+2023&author=Tan,+W.&author=Hu,+Z.&author=McPhaden,+M.J.&author=Zhu,+C.&author=Li,+X.&author=Liu,+Y.&publication_year=2024&journal=Geophys.+Res.+Lett.&volume=51&pages=e2024GL108198&doi=10.1029/2024GL108198)] [[CrossRef](https://doi.org/10.1029/2024GL108198)]
69.   Chen, L.; Li, T.; Wang, B.; Wang, L. Formation Mechanism for 2015/16 Super El Niño. Sci. Rep.**2017**, 7, 2975. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Formation+Mechanism+for+2015/16+Super+El+Ni%C3%B1o&author=Chen,+L.&author=Li,+T.&author=Wang,+B.&author=Wang,+L.&publication_year=2017&journal=Sci.+Rep.&volume=7&pages=2975&doi=10.1038/s41598-017-02926-3&pmid=28592846)] [[CrossRef](https://doi.org/10.1038/s41598-017-02926-3)] [[PubMed](https://www.ncbi.nlm.nih.gov/pubmed/28592846)]
70.   Zhang, S.; Wang, H.; Jiang, H.; Song, C.; Du, L. Sea surface temperature variations of the Yellow Sea and East China Sea influenced by both ENSO and typhoons in July. Haiyang Xuebao**2017**, 39, 32–41. (In Chinese) [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Sea+surface+temperature+variations+of+the+Yellow+Sea+and+East+China+Sea+influenced+by+both+ENSO+and+typhoons+in+July&author=Zhang,+S.&author=Wang,+H.&author=Jiang,+H.&author=Song,+C.&author=Du,+L.&publication_year=2017&journal=Haiyang+Xuebao&volume=39&pages=32%E2%80%9341&doi=10.3969/j.issn.0253-4193.2017.12.004)] [[CrossRef](https://doi.org/10.3969/j.issn.0253-4193.2017.12.004)]
71.   Xia, J.; Tu, K.; Yan, Z.; Qi, Y. The super-heat wave in eastern China during July–August 2013: A perspective of climate change. Int. J. Climatol.**2016**, 36, 1291–1298. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=The+super-heat+wave+in+eastern+China+during+July%E2%80%93August+2013:+A+perspective+of+climate+change&author=Xia,+J.&author=Tu,+K.&author=Yan,+Z.&author=Qi,+Y.&publication_year=2016&journal=Int.+J.+Climatol.&volume=36&pages=1291%E2%80%931298&doi=10.1002/joc.4424)] [[CrossRef](https://doi.org/10.1002/joc.4424)]
72.   Barriopedro, D.; García-Herrera, R.; Ordóñez, C.; Miralles, D.G.; Salcedo-Sanz, S. Heat Waves: Physical Understanding and Scientific Challenges. Rev. Geophys.**2023**, 61, e2022RG000780. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Heat+Waves:+Physical+Understanding+and+Scientific+Challenges&author=Barriopedro,+D.&author=Garc%C3%ADa-Herrera,+R.&author=Ord%C3%B3%C3%B1ez,+C.&author=Miralles,+D.G.&author=Salcedo-Sanz,+S.&publication_year=2023&journal=Rev.+Geophys.&volume=61&pages=e2022RG000780&doi=10.1029/2022RG000780)] [[CrossRef](https://doi.org/10.1029/2022RG000780)]
73.   Reguero, B.G.; Losada, I.J.; Méndez, F.J. A global wave power resource and its seasonal, interannual and long-term variability. Appl. Energy**2015**, 148, 366–380. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=A+global+wave+power+resource+and+its+seasonal,+interannual+and+long-term+variability&author=Reguero,+B.G.&author=Losada,+I.J.&author=M%C3%A9ndez,+F.J.&publication_year=2015&journal=Appl.+Energy&volume=148&pages=366%E2%80%93380&doi=10.1016/j.apenergy.2015.03.114)] [[CrossRef](https://doi.org/10.1016/j.apenergy.2015.03.114)]
74.   Su, W.; Chen, H.; Chen, W.; Chang, C.; Lin, L.; Jang, J.; Yu, Y. Numerical investigation of wave energy resources and hotspots in the surrounding waters of Taiwan. Renew. Energy**2018**, 118, 814–824. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Numerical+investigation+of+wave+energy+resources+and+hotspots+in+the+surrounding+waters+of+Taiwan&author=Su,+W.&author=Chen,+H.&author=Chen,+W.&author=Chang,+C.&author=Lin,+L.&author=Jang,+J.&author=Yu,+Y.&publication_year=2018&journal=Renew.+Energy&volume=118&pages=814%E2%80%93824&doi=10.1016/j.renene.2017.11.080)] [[CrossRef](https://doi.org/10.1016/j.renene.2017.11.080)]
75.   Dai, D.; Qiao, F.; Xia, C.; Jung, K.T. A numerical study on dynamic mechanisms of seasonal temperature variability in the Yellow Sea. J. Geophys. Res.-Ocean.**2006**, 111. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=A+numerical+study+on+dynamic+mechanisms+of+seasonal+temperature+variability+in+the+Yellow+Sea&author=Dai,+D.&author=Qiao,+F.&author=Xia,+C.&author=Jung,+K.T.&publication_year=2006&journal=J.+Geophys.+Res.-Ocean.&volume=111&doi=10.1029/2005JC003253)] [[CrossRef](https://doi.org/10.1029/2005JC003253)]

**Figure 1.** Marine topography of the study area (based on ETOPO1 data).

[![Image 4: Jmse 13 01196 g001](https://www.mdpi.com/jmse/jmse-13-01196/article_deploy/html/images/jmse-13-01196-g001.png)](https://www.mdpi.com/jmse/jmse-13-01196/article_deploy/html/images/jmse-13-01196-g001.png)

**Figure 2.** Comparison of significant wave height data simulated by SWAN and satellite observation data.

[![Image 5: Jmse 13 01196 g002](https://www.mdpi.com/jmse/jmse-13-01196/article_deploy/html/images/jmse-13-01196-g002.png)](https://www.mdpi.com/jmse/jmse-13-01196/article_deploy/html/images/jmse-13-01196-g002.png)

**Figure 3.** Monthly significant wave height and direction distribution in the ESC, 2009–2023.

[![Image 6: Jmse 13 01196 g003](https://www.mdpi.com/jmse/jmse-13-01196/article_deploy/html/images/jmse-13-01196-g003.png)](https://www.mdpi.com/jmse/jmse-13-01196/article_deploy/html/images/jmse-13-01196-g003.png)

**Figure 4.** Regional wave energy flux density distribution in ECS.

[![Image 7: Jmse 13 01196 g004](https://www.mdpi.com/jmse/jmse-13-01196/article_deploy/html/images/jmse-13-01196-g004.png)](https://www.mdpi.com/jmse/jmse-13-01196/article_deploy/html/images/jmse-13-01196-g004.png)

**Figure 5.** Average annual wave energy flux density in the ECS from 2009 to 2023.

[![Image 8: Jmse 13 01196 g005](https://www.mdpi.com/jmse/jmse-13-01196/article_deploy/html/images/jmse-13-01196-g005.png)](https://www.mdpi.com/jmse/jmse-13-01196/article_deploy/html/images/jmse-13-01196-g005.png)

**Figure 6.** COV of wave energy flux density.

[![Image 9: Jmse 13 01196 g006](https://www.mdpi.com/jmse/jmse-13-01196/article_deploy/html/images/jmse-13-01196-g006.png)](https://www.mdpi.com/jmse/jmse-13-01196/article_deploy/html/images/jmse-13-01196-g006.png)

**Table 1.** Comparison of simulated significant wave height data with satellite-measured effective wave height data for the two whitecapping conditions of Komen and Westhuysen over the period 2010 to 2019.

| Year | Komen (MAE/m) | Komen (RMSE/m) | Westhuysen (MAE/m) | Westhuysen (RMSE/m) |
| --- | --- | --- | --- | --- |
| 2010 | 0.240 | 0.335 | 0.240 | 0.444 |
| 2011 | 0.244 | 0.357 | 0.244 | 0.455 |
| 2012 | 0.235 | 0.338 | 0.237 | 0.472 |
| 2013 | 0.270 | 0.399 | 0.270 | 0.497 |
| 2014 | 0.257 | 0.371 | 0.256 | 0.469 |
| 2015 | 0.262 | 0.405 | 0.262 | 0.456 |
| 2016 | 0.265 | 0.370 | 0.264 | 0.370 |
| 2017 | 0.279 | 0.452 | 0.319 | 0.502 |
| 2018 | 0.248 | 0.345 | 0.248 | 0.468 |
| 2019 | 0.234 | 0.366 | 0.216 | 0.434 |
| Total | 2.532 | 3.738 | 2.556 | 4.567 |
| Average | 0.253 | 0.374 | 0.256 | 0.457 |
| % Difference a | - | - | 1.1% | 22% |

$a : D i f f e r e n c e s = \frac{A - B}{B} \times 100 \%$. Here, A denotes simulation results based on the Westhuysen parameters for comparative analysis, while B represents results derived from the Komen parameter.

**Table 2.** Comparison of simulated significant wave height data with satellite-measured effective wave height data for the three bottom friction parameter conditions of Collins, Jonswap, and Madsen for the period 2010 to 2019.

| Year | Collins (MAE/m) | Collins (RMSE/m) | Jonswap (MAE/m) | Jonswap (RMSE/m) | Madsen (MAE/m) | Madsen (RMSE/m) |
| --- | --- | --- | --- | --- | --- | --- |
| 2010 | 0.244 | 0.325 | 0.240 | 0.335 | 0.239 | 0.334 |
| 2011 | 0.241 | 0.335 | 0.244 | 0.357 | 0.243 | 0.356 |
| 2012 | 0.233 | 0.350 | 0.235 | 0.338 | 0.234 | 0.372 |
| 2013 | 0.267 | 0.395 | 0.270 | 0.399 | 0.270 | 0.398 |
| 2014 | 0.254 | 0.367 | 0.257 | 0.371 | 0.256 | 0.369 |
| 2015 | 0.254 | 0.395 | 0.262 | 0.405 | 0.261 | 0.405 |
| 2016 | 0.264 | 0.371 | 0.265 | 0.370 | 0.264 | 0.369 |
| 2017 | 0.275 | 0.441 | 0.279 | 0.452 | 0.279 | 0.450 |
| 2018 | 0.250 | 0.348 | 0.248 | 0.345 | 0.247 | 0.344 |
| 2019 | 0.233 | 0.366 | 0.234 | 0.366 | 0.233 | 0.365 |
| Total | 2.515 | 3.694 | 2.532 | 3.738 | 2.525 | 3.762 |
| Average | 0.252 | 0.369 | 0.253 | 0.374 | 0.253 | 0.376 |
| % Difference b | - | - | 0.3% | 1.3% | 0.3% | 1.8% |

$b : D i f f e r e n c e s = \frac{A - B}{B} \times 100 \%$. Here, A denotes simulation results based on the Jonswap or Madsen parameters for comparative analysis, while B represents results derived from the Collins parameter.

**Table 3.** SWAN model parameter settings.

|  | Parameter |
| --- | --- |
| SWAN Version | Versions 41.45 |
| Model simulation area | 25–35° N,120–130° E |
| Model spatial resolution | 0.05° |
| Model temporal resolution | 1 h |
| Wave propagation governing equations | Second-order SORDUP differential |
| Whitecap dissipation | $S_{w c} \left(\sigma , \theta\right) = - \Gamma \overset{\sim}{\sigma} \frac{k}{\overset{\sim}{k}} E \left(\sigma , \theta\right)$ [[46](https://www.mdpi.com/2077-1312/13/6/1196#B46-jmse-13-01196)] |
| Bottom friction dissipation | $S d s , b = - C_{b o t t o m} \frac{\sigma^{2}}{g^{2} \left(s i n h\right)^{2} \left(k d\right)} E \left(\sigma , \theta\right) d \sigma d \theta$ [[34](https://www.mdpi.com/2077-1312/13/6/1196#B34-jmse-13-01196)] |
| Simulation time | January 2009 to December 2023 |
| Directional discretization | 10° |

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.

© 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license ([https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)).

## [](https://www.mdpi.com/2077-1312/13/6/1196)Share and Cite

**MDPI and ACS Style**

Ma, S.; Ji, F.; Yang, Q.; Mi, Z.; Cao, W. Regional Wave Analysis in the East China Sea Based on the SWAN Model. _J. Mar. Sci. Eng._**2025**, _13_, 1196. https://doi.org/10.3390/jmse13061196

**AMA Style**

Ma S, Ji F, Yang Q, Mi Z, Cao W. Regional Wave Analysis in the East China Sea Based on the SWAN Model. _Journal of Marine Science and Engineering_. 2025; 13(6):1196. https://doi.org/10.3390/jmse13061196

**Chicago/Turabian Style**

Ma, Songnan, Fuwu Ji, Qunhui Yang, Zhinan Mi, and Wenhui Cao. 2025. "Regional Wave Analysis in the East China Sea Based on the SWAN Model" _Journal of Marine Science and Engineering_ 13, no. 6: 1196. https://doi.org/10.3390/jmse13061196

**APA Style**

Ma, S., Ji, F., Yang, Q., Mi, Z., & Cao, W. (2025). Regional Wave Analysis in the East China Sea Based on the SWAN Model. _Journal of Marine Science and Engineering_, _13_(6), 1196. https://doi.org/10.3390/jmse13061196

Note that from the first issue of 2016, this journal uses article numbers instead of page numbers. See further details [here](https://www.mdpi.com/about/announcements/784).

## [](https://www.mdpi.com/2077-1312/13/6/1196)Article Metrics

### Citations

Crossref

Scopus

Web of Science

Google Scholar

### Article Access Statistics

For more information on the journal statistics, click [here](https://www.mdpi.com/journal/jmse/stats).

Multiple requests from the same IP address are counted as one view.
