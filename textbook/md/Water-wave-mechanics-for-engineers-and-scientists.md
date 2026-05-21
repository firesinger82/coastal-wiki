

---PAGE-1---





---PAGE-2---





---PAGE-3---



###### WATERWAVE MECHANICS FOR

ENGINEERS AND SCIENTISTS



---PAGE-4---



###### ADVANCED SERIES ON OCEAN ENGINEERING

Series Editor-in-Chief

###### Philip L-F Liu Cornell University, USA

- Vol. 1 The Applied Dynamics of Ocean Surface Waves by Chiang C Mei (MIT, USA)
- Vol. 2 Water Wave Mechanics for Engineers and Scientists by Robert G Dean (Univ. Florida, USA) and Robert A Dalrymple (Univ. Delaware. USA)
- Vol. 3 Mechanics of Coastal Sediment Transport by hrgen Fredsue and Rolf Deigaard (Tech. Univ. Denmark, Denmark)
- Vol. 4 Coastal Bottom Boundary Layers and Sediment Transport by Peter Nielsen (Univ. Queensland, Australia)


Forlhcorning titles: Water Waves Propagation Over Uneven Bottoms by Maarten W Dingemans (Delft Hydraulics, The Netherlands) Ocean Outfall Design by /an R Wood (Univ. Canterbury, New Zealand) Tsunami Run-up by Philip L - F Liu (Cornell Univ.), Cosras Synolakis (Univ. Southern California), Harry Yeh (Univ. Washington) and Nobu Shuto (Tohoku Univ.) Physical Modules and Laboratory Techniques in Coastal Engineering by Steven A. Hughes (Coastal Engineering Research Center, USA)



---PAGE-5---



Advanced Series on Ocean Engineering -Volume 2

###### Robert G. Dean

University of Florida

###### Robert A. Dalrymple

Universityof Delaware

###### World Scientific

ingapore.New Jersey. London. HongKong



---PAGE-6---



Published by World Scientific PublishingCo. Re. ttd. P 0Box 128,FarrerRoad, Singapore912805 USA oftice: Suite IS, 1060Main Street, River Edge,NJ 07561 UK ofice: 57 Shelton Street,Covent Garden,London WC2H 9HE

###### Library of Congress Cataloging-in-Publica~ianData Dean, Robert G. (Robert George), 1930-

Water wave mechanics for engineersand scientistsI Robea G. I and Robert A. Dalryrnple.

p. cm. Includes bibliographical referencesand index.

ISBN 9810204205. --ISBN 9810204213 (pbk.)

1. Water waves. 2. Fluid mechanics. I. Dalrymple,Robert A,,

1945- II. Title TC172.D4 1991 627'.042--dc20 90-27331

CIP

First published in 1984by Prentice Hall, Inc

CopyrightQ 1991by World Scientific PublishingCo. Re. Ltd. Reprinted in 19Y2, 1993, 1994, 1995,1998. 20M).

All rights reserved. Thishook, orparts thereal; may fiotbe reproduced in m yform orbym ymeans,electrunirormet.hcmica1,includingphotocopying,recording ornny in$Jrviiition storuge and relrievd system now known or m be invented, withour wrirtenpermi.csbnfrr,rn rhe Publisher.

For photocopying of materia! in this volume, please pay a copying fee through the Copyrighl ClearanceCenter, Inc., 222 Rosewood Drive. Uanvers, MA01921, USA.

Printed in Singapore.



---PAGE-7---





---PAGE-8---





---PAGE-9---



###### xi

###### PREFACE

###### 1

INTRODUCTION TO WAVE MECHANlCS

- 1.1 Introduction,2
- 1.2 Characteristics of Waves, 2
- 1.3 Historical and Present Literature, 4


###### A REVIEW OF HYDRODYNAMICS AND VECTOR ANALYSIS 6

- 2.1 introduction, 7
- 2.2 Reviewof Hydrodynamics,7
- 2.3 Review of Vector Analysis, 79
- 2.4 Cylindrical Coordinates,32 References,36 Problems, 37


###### SMALL-AMPLITUDE WATER WAVE THEORY FORMULATION AND SOLUTION 41

- 3.1 introduction, 42
- 3.2 Boundary Value Problems, 42


vii



---PAGE-10---



viii Contents

3.3 3.4 3.5

Summary of the Two-Dimensional Periodic Water Wave Boundary Value Problem,52 Solution to LinearizedWater Wave Boundary Value Problem for a Horizontal Bottom, 53 Appendix: Approximate Solutions to the Dispersion Equation, 77 References,73 Problems, 73

###### 4

ENGINEERINGWAVE PROPERTIES

###### 78

- 4.1 Introduction, 79
- 4.2
- 4.3
- 4.4
- 4.5
- 4.6 Partial StandingWaves, 90
- 4.7
- 4.8
- 4.9 Wave Diffraction, 176
- 4.10 Combined Refraction-Diffraction, 723 References, 124 Problems, 126


Water Particle Kinematics for ProgressiveWaves, 79 Pressure Field Under a ProgressiveWave, 83 Water Particle Kinematics for Standing Waves, 86 Pressure Field Under a StandingWave, 89

Energy and Energy Propagation in ProgressiveWaves, 93 Transformationof Waves Entering Shallow Water, 700

###### 5

LONG WAVES

131

5.1 5.2 5.3 5.4 5.5 5.6 5.7 5.8 5.9 5.10 5.11

Introduction, 132 Asymptotic Long Waves, 732 Long Wave Theory, 133 One-Dimensional Tides in IdealizedChannels, 738 Reflection and Transmission Past an Abrupt Transition, 147 Long Waves with Bottom Friction, 146 Geostrophic Effects on Long Waves, 154 Long Waves in Irregular-Shaped Basins or Bays, 157 Storm Surge, 157 Long Waves Forced by a Moving Atmospheric Pressure Disturbance, 163 Long Waves Forced by a Translating Bottom Displacement, 766 References, 167 Problems, 767



---PAGE-11---



ix

Contents

170

###### WAVEMAKER THEORY

- 6.1 Introduction, 770
- 6.2
- 6.3
- 6.4 CylindricalWavemakers, 780
- 6.5 Plunger Wavemakers, 784


Simplified Theory for Plane Wavemakers in Shallow Water, 777 Complete Wavemaker Theory for Plane Waves Produced by a Paddle, 772

References, 785 Problems, 785

###### 7

###### 187

###### WAVE STATISTICS AND SPECTRA

- 7.1 Introduction, 787
- 7.2 Wave Height Distributions, 788
- 7.3 The Wave Spectrum, 793
- 7.4 The DirectionalWave Spectrum,202
- 7.5 Time-Series Simulation,207
- 7.6 Examples of Use of Spectral Methods to Determine Momentum Flux, 208 References,209 Problems,270


###### 21 2

###### WAVE FORCES

- 8.1 Introduction,272
- 8.2 Potential Flow Approach, 273
- 8.3
- 8.4
- 8.5


Forces Due to Real Fluids, 227 Inertia Force Predominant Case, 237 Spectral Approach to Wave Force Prediction,254 References,255 Problems,257

###### WAVES OVER REAL SEABEDS 261

- 9.1 Introduction,261
- 9.2
- 9.3


Waves Over Smooth, Rigid, Impermeable Bottoms, 262 Water Waves Over a Viscous Mud Bottom, 277



---PAGE-12---



###### X Contents

9.4 Waves Over Rigid, Porous Bottoms, 277 References, 282 Problems, 282

###### 10

NONLINEAR PROPERTIES DERIVABLE FROM SMALL-AMPLITUDE WAVES

284

- 10.1 introduction, 285
- 10.2 Mass Transport and Momentum Flux,285
- 10.3 Mean Water Level, 287
- 10.4 Mean Pressure, 288
- 10.5 Momentum Flux,289
- 10.6 Summary, 293 References, 293 Problems, 294


###### 11

295

###### NONLINEAR WAVES

- 11.1 Introduction, 296
- 11.2 Perturbation Approach of Stokes, 296
- 11.3 The Stream FunctionWave Theory, 305
- 11.4 Finite-AmplitudeWaves in Shallow Water, 309
- 11.5 The Validity of Nonlinear Wave Theories, 322 References,324 Problems, 325


###### A SERIES OF EXPERIMENTS FOR A LABORATORY COURSE COMPONENT IN WATER WAVES

326

- 12.1 Introduction,326
- 12.2 Required Equipment, 326
- 12.3 Experiments,330 References, 345


347

SUBJECT INDEX

351

AUTHOR INDEX



---PAGE-13---



###### C

The initial substantiveinterest in andcontributionsto water wave mechanics date from more than a century ago, beginning with the analysis of linear wave theory by Airy in 1845and continuing with higher order theories by Stokes in 1847,long wave theories by Boussinesq in 1872,and limiting wave heights by Michell in 1893and McCowan in 1894.

Following that half-century of pioneering developments, research continued at a relatively slow pace until the amphibious landings in the Second World War emphasized the need for a much better understanding of wave initiation and growth due to winds, the conservative anddissipative transformation mechanisms occurring from the source area to the shoaling, and the breaking processes at the shore. The largely unsuccessful attempt to utilize portable and floating breakwaters in the surprise amphibious landing at Normandy, France, stimulated interest in wave interaction with fixed and floating objects.

After the Second World War, the activity in water wave research probably would have subsided without the rather explosive growth in oceanrelated engineering in scientific, industrial, and military activities. From the 1950sto the 1980s,offshore drilling and production of petroleum resources progressed from water depths of approximately 10meters to over 300meters, platforms for the latter being designed for wave heights on the order of 25 meters and costing in excess of $700,000,000(U.S.).The financial incentives of well-planned and comprehensive studies of water wave phenomena became much greater. Laboratory studies as well as much more expensive field programs were required to validate design methodology and to provide a better basis for describing the complex and nonlinear directional seas. A second and substantial impetus to nearshore research on water waves has been the interest in coastal erosion, an area still only poorly understood. For example, although the momentum flux concepts were systematized by Longuet-Higginsand Stewart and applied to a number ofrelevant problems

xi



---PAGE-14---



xii Preface

in the 1960s,the usual (spilling wave) assumption of the wave height inside the surf zone being proportional to the water depth avoids the important matter of the distribution of the applied longshore stress across the surf zone. This can only be reconciled through careful laboratory and field measurements of wave breaking. Wave energy provides another example. In the last two decades remote sensing has indicated the potential of defining synoptic measures of wave intensity over very wide areas,with the associated benefits to shipping efficiency. Simple calculations of the magnitudes of the “standing crop” of wave energyhave stimulated many scientistsand engineerstodevise ingenious mechanisms to harvest this energy. Still, these mechanisms must operate in a harsh environment known for its long-term corrosive and fouling effects and the high-intensity forces during severe storms.

The problem of quantifying the wave climate, understanding the interaction of waves with structures and/or sediment, and predicting the associated responses of interest underlies almost every problem in coastal and ocean engineering. It is toward this goal that this book is directed. Although the book is intended for use primarily asa text at the advanced undergraduate orfirst-year graduate level, it is hoped that it will serve also asa reference and will assist one to learn the field through self-study.Toward these objectives, each chapter concludes with a number of problems developed to illustrate by application the material presented. The references included should aid the student and the practicing engineer to extend their knowledge further.

The book is comprised of twelve chapters. Chapter 1 presents a number of common examples illustrating the wide range of water wave phenomena, many of which can be commonly observed. Chapter 2 offers a review of potential flow hydrodynamics and vector analysis.This material is presented forthe sake of completeness, even though it will be familiar to many readers. Chapter 3formulates the linear water wave theory and develops the simplest two-dimensional solution for standing and progressive waves. Chapter 4 extends the solutions developed in Chapter 3to many features of engineering relevance, including kinematics, pressure fields, energy, shoaling, refraction, and diffraction. Chapter 5 investigates long wave phenomena, such as kinematics, seiching, standing and progressive waves with friction, and long waves including geostrophic forces and storm surges. Chapter 6 explores various wavemaker problems, which are relevant to problems of wave tank and wave basin design and to problems of damping of floating bodies. The utility of spectral analysis to combine many elemental solutions is explored in Chapter 7. In this manner a complex sea comprising a spectrum of frequencies and, at each frequency, a continuum of directions can be represented. Chapter 8examines the problem of wave forces on structures.A slight modification of the problem of two-dimensional idealized flow about a cylinder yields the well-known Morison equation. Both drag- and inertiadominant systems are discussed, including methods for data analysis, and somefield data are presented.Thischapter concludeswith a brief description of the Green’s function representation for calculating the forces on large



---PAGE-15---



Preface xiii

bodies. Chapter 9 considers the effects of waves propagating over seabeds which may be porous, viscous, and/or compressible and at which frictional effects may occur in the bottom boundary layer. Chapter 10 develops a number of nonlinear (to second order in wave height) results that, somewhat surprisingly, may be obtained from linear wave theory.These results, many of which are of engineering concern, include mass transport, momentum flux, set-down and set-up of the mean water level, mean pressure under a progressive wave, and the “microseisms,” in-phase pressure fluctuations that occur under two-dimensional standing waves. Chaper 11 introduces the perturbation method to develop and solve various nonlinear wave theories, including the Stokes second order theory, and the solitary and cnoidal wave theories. The procedure for developing numerical wave theories to high order is described, as are the analytical and physical validities of theories. Finally, Chapter 12 presents a number of water wave experiments (requiring only simple instrumentation) that the authors have found useful for demonstrating the theory and introducing the student to wave experimentation, specifically methodology, instrumentation, and frustrations.

Each chapter is dedicated to a scientist who contributed importantly to this field. Brief biographies were gleaned from such sources as TheDictionary of National Biography (United Kindom scientists; Cambridge University Press), Dictionary of Scientific Biography (Charles Scribner’s Sons, New York),Neue Deutsche Biogruphie (Helmholtz; Duncker and Humblot, Berlin) and TheLondon Times (Havelock). These productive and influential individuals are but a few of those who have laid the foundations of our present-day knowledge; however, the biographies illustrate the level of effort and intensity of those people and their eras, through which great scientific strideswere made.

The authors wish to acknowledge the stimulating discussions and inspiration provided by many of their colleagues and former professors. In particular, Professors R. 0. Reid, B. W. Wilson, A. T. Ippen, and C. L. Bretschneider were central in introducing the authors to the field. Numerous focused discussions with M. I? O’Brien have crystallized understanding of water wave phenomena and their effects on sediment transport. Drs.Todd L. Walton and IbA. Svendsen provided valuable reviews of the manuscript, as have a number of studentswho have taken the WaterWave Mechanics course at the University of Delaware. Mrs. SueThompson deserves great praise for her cheerful disposition and faultless typing of numerous drafts of the manuscript, as does Mrs. ConnieWeber, who managed final revision.

Finally the general support and encouragement provided by the University of Delaware is appreciated.

###### Robert G.Dean Robert A. Dalrymple



---PAGE-16---





---PAGE-17---



###### V

###### Dedication SIR HORACE LAMB

Sir Horace Lamb(1849-1934) is best knownfor his extremely thorough and well-written book, Hydrodynamics, which first appeared in 1879 and has beenreprinted numeroustimes. It still serves as a compendium of useful information as well as the source for a great numberof papers and books. If this present book has but a small fraction of the appeal of Hydrodynamics, the authors would be well satisfied.

Sir Horace Lamb was born in Stockport, England in 1849, educated at Owens College, Manchester, and then Trinity College, Cambridge University, where he studied with professors such as J. Clerk Maxwell and G. G. Stokes. After his graduation, he lectured at Trinity (1822-1825) and then movedto Adelaide, Australia, to become Professor of Mathematics.

After ten years, he returned to Owens College (part of Victoria University of Manchester) as Professor of Pure Mathematics; he remaineduntil 1920.

Professor Lambwas noted for his excellent teaching and writing abilities. Inresponseto a student tribute on the occasionof his eightieth birthday, he replied: “Idid try to makethings clear, first to myself.. .and then to my students, and somehow makethese dry bones live.”

His research areas encompassed tides, waves, and earthquake properties as well as mathematics.

1



---PAGE-18---



2 Introductionto Wave Mechanics Chap. 1

###### 1.IINTRODUCTION

Rarely can one find a body of water open to the atmosphere that does not have waveson its surface.Thesewavesarea manifestation offorcesactingon the fluid tending to deform it against the action of gravity and surface tension,which together act to maintain a levelfluid surface.Thus it requires a force of some kind, such as would be caused by a gust of wind or a falling stone impacting on the water, to create waves. Once these are created, gravitationaland surface tension forces are activated that allow the waves to propagate, in the same manner as tension on a string causes the string to vibrate, much to our listening enjoyment.

Waves occur in all sizes and forms, depending on the magnitude of the forces acting on the water. A simple illustration is that a small stone and a large rock create different-size waves after impacting on water. Further, different speeds of impact create different-size waves, which indicates that the pressure forces acting on the fluid surface are important, as well as the magnitude of the displaced fluid. The gravitational attraction of the moon, sun, and other astronomical bodies creates the longest known water waves, the tides. These waves circle halfway around the earth from end to end and travel with tremendous speeds. The shortest waves can be less than a centimeter in length. The length of the wave gives one an idea of the magnitude of the forces acting on the waves. For example, the longer the wave, the more important gravity (comprised of the contributions from the earth, the moon, and the sun) is in relation to surface tension.

The importance of waves cannot be overestimated. Anything that is near or in a body of water is subject to wave action. At the coast, this can result in the movement of sand alongthe shore, causing erosion or damageto structures during storms. In the water, offshore oil platforms must be able to withstand severe storms without destruction. At present drilling depths exceeding 300m, this requires enormous and expensive structures. On the water, all ships are subjected to wave attack, and countless ships have foundered due to waves which have been observed to be as large as 34 m in height. Further, any ship moving through water creates a pressure field and, hence, waves. These waves create a significant portion of the resistance to motion enountered by the ships.

###### 1.2 CHARACTERISTICSOF WAVES

The important parameters to describewaves are their length and height, and the water depth over which they are propagating.All other parameters, such as wave-induced water velocities and accelerations, can be determined theoretically from these quantities. In Figure 1.1,a two-dimensional schematic of a wave propagatingin the x direction is shown.The length of the wave,



---PAGE-19---



- Sec. 1.2 Characteristicsof Waves 3


###### .

I Trough

h

Figure 1.1 Wave characteristics.

L, is the horizontal distance between two successivewave crests, or the high points on a wave, or alternatively the distance between two wave troughs. The wave length will be shown later to be related to the water depth h and wave period T,whichisthe time required for two successivecrests or troughs to pass a particular point.As the wave, then, must move a distanceL in time T,the speed of the wave, called the celerity, C, is defined as C =L/T.While the wave form travelswith celerity C, the waterthat comprises the wave does not translate in the direction of the wave.

The coordinate axis that will be used to describe wave motion will be located at the still water line, z =0.The bottom of the water body will be at

z = -h.

Waves in nature rarely appear to look exactly the same from wave to wave, nor do they always propagate in the same direction. If a device to measurethe water surface elevation, 9, as a function of time was placed on a platform in the middle of the ocean, it might obtain a record such as that shown in Figure 1:2. This sea can be seen to be a superposition of a large number of sinusoidsgoing in different directions. For example, consider the two sine waves shown in Figure 1.3 and their sum. It is this superpositionof sinusoidsthat permits the use of Fourier analysisand spectral techniques to be used in describing the sea. Unfortunately, there is a great amount of randomness in the sea, and statistical techniques need to be brought to bear. Fortunately, very large waves or, alternatively,waves in shallowwater appear

Figure 1.2 Exampleofapossible recordedwave form.



---PAGE-20---



4 Introductionto Wave Mechanics Chap. 1

Figure 1.3 Complex wave form resultingas the sum oftwosinusoids.

to be more regular than smaller waves or those in deeper water, and not so random. Therefore, in thesecases,eachwaveismore readily describedby one sinusoid, which repeats itself periodically. Realistically,due to shallow water nonlinearities, more than one sinusoid, all of the same phase, are necessary; however, using one sinusoid has been shown to be reasonably accurate for some purposes.It is this surprisingaccuracy and easeofapplicationthat have maintained the popularity and the widespread usage of so-called linear, or small-amplitude, wave theory. The advantages are that it is easy to use, as opposedto more complicated nonlinear theories, and lends itselfto superposition and other complicated manipulations. Moreover, linear wave theory is an effective stepping-stoneto some nonlinear theories. For this reason, this book is directed primarily to linear theory.

###### 1.3 HISTORICALAND PRESENT LITERATURE

The fieldofwater wave theory isover 150yearsold and,ofcourse, during this period of time numerous books and articles have been written about the subject. Perhaps the most outstanding is the seminal work of Sir Horace Lamb. His Hydrodynamics has served as a source book since its original publication in 1879.

Other notable books with which the reader should become acquainted are R. L. Wiegel's Oceanographical Engineering and A. T. Ippen's Estuary



---PAGE-21---



- Sec. 1.3 Historical and Present Literature 5


and Coastline Hydrodynamics. These two books, appearing in the 1960s, provided the education of many ofthe practicing coastaland ocean engineers of today.

The authors also recommend for further studies on waves the book by G. B. Witham entitledLinear and Nonlinear Waves,from which a portion of Chapter 11is derived, and the article “§Surface Waves,” by J.V.Wehausenand E.V. Laitone, in the Handbuch der Physik.

In terms of articles, there area number ofjournals and proceedingsthat will provide the reader with more up-to-date material on waves and wave theory and its applications. These include the American Society of Civil Engineers’ Journal of Waterway, Port, Coastal and Ocean Division, the Journal of Fluid Mechanics, the Proceedings of the International Coastal Engineering Conferences, the Journal of Geophysical Research, Coastal Engineering, Applied Ocean Research, and the Proceedings of the Offshore Technology Conference.



---PAGE-22---



###### Dedication LEONHARDEULER

LeonhardEuler(1707-1783), bornin Basel, Switzerland,was oneof the earliest practitioners of applied mathematics, developing with others the theory of ordinary and partial differential equations and applying them to the physical world. The most frequent use of his work here is the use of the Euler equations of motion, which describe the flow of an inviscid fluid.

In1722he graduated from the University of Basel with a degree in Arts. During this time, however, he attended the lectures of Johan I. Bernoulli (Daniel Bernoulli’s father), and turned to the study of mathematics. In 1723 he received a master’s level degree in philosophy and began to teach in the philosophy department. In 1727 he movedto St. Petersburg, Russia, and to the St. Petersburg Academy of Science, where heworked inphysiology and mathematics and succeededDaniel Bernoullias Professor of Physicsin 1731.

In 1741 he was invited to work in the Berlin Society of Sciences (foundedby Leibniz).Someof his work there was appliedasopposedto theoretical. He worked on the hydraulic works of Frederick the Great’s summer residence as well as in ballistics, which was of national interest. InBerlinhe published 380 works relatedto mathematical physicsin such areas as geometry, optics, electricity, and magnetism. In 1761 he published his monograph, “Principia motus fluidorum,” which put forth the now-familiar Euler and continuity equations.

He returned to St. Petersburg in 1766 after a falling-out with

###### 6



---PAGE-23---



###### Sec. 2.2 Reviewof Hydrodynamics 7

Frederickthe Great and began to dependoncoauthorsfor anumber of hisworks, as he was going blind.He died therein1783.

Inmathematics, Euler was responsiblefor introducingnumerous

notations:for example,i = fi,efor baseof the natural log, andthe

finite differenceb.

###### 2.1 INTRODUCTION

In order to investigate water waves most effectively, a reasonably good background in fluid dynamics and mathematics is helpful. Although it is anticipated that the reader has this background, a review of the essential derivations and equations is offered here as a refresher and to acquaint the reader with the notation to be used throughout the book.

A mathematical tool that will be used often is the Taylor series. Mathematically, it can be shown that if a continuous functionfix, y) of two independent variablesx and y is known at, say,x equal to XOt, hen it can be approximatedat another location on the x axis,xo+Ax,bytheTaylor series.

+... +~"JTXO~Y)(~)"+ . . .

dx" n!

where the derivatives offix, y) are all taken at x =xo,the location for which the function is known. For very small values of Ax, the terms involving (Ax)",where n > 1, are very much smaller than the first two terms on the right-hand side of the equation and often in practice can be neglected. If Ax,y)varies linearly withx,for example,Ax,y) = y2+mx+b,truncating the Taylor series to two terms involves no error, for all values of Ax.' Through the use of the Taylor series, it is possible to develop relationships between fluid properties at two closely spaced locations.

###### 2.2 REVIEW OF HYDRODYNAMICS

2.2.1 Conservationof Mass

In a real fluid, mass must be conserved; it cannot be created or destroyed. To develop a mathematical equation to express this concept, consider a very small cube located with its center at x, y , z in a Cartesian coordinatesystemasshown in Figure2.1. For the cube with sidesAx, Ay,and

'In fact, for any nth-order function, the expression (2.1)is exact as longas (n + 1) terms in the series are obtained.



---PAGE-24---



###### 8 A Review of Hydrodynamicsand Vector Analysis Chap. 2

W

Velocity

components

Figure2.1 Referencecubeinafluid.

Az, the rate at which fluid mass flows into the cube across the various faces must equal the sum of the rate of mass accumulation in the cubeand the mass fluxes out of the faces.

Takingfirst thexfaceatx - Ax/2,the rate at which the fluid mass flows in is equal to the velocity component in thex direction times the area through which it is crossing, all multiplied times the densityofthe fluid,p. Therefore, the mass inflow rate atx -Ax/2, or sideACEG, is

where the terms in parentheses denote the coordinate location. truncated Taylor series, keeping in mind the smallnessof the cube,

This mass flow rate can be related to that at the centerof the cubeby the

Ax Ax

P(x --7 Y , Z ) W --7 Y , z)AY A.2 (2.3)

2 2

For convenience, the coordinates ofpand u at the center of the cube will not be shown hereafter. The mass flow rate out of the other x face, at x +Ax/2, face BDFH, can also be represented by theTaylor series,

###### [pu +d@u)s+ax 2 . . ) y A z

By subtracting the mass flow rate out from the mass flow rate in, the net flux of mass into the cube in the x direction is obtained, that is, the rate of mass accumulation in the x direction:

where the term O(AX)~denotes terms of higher order, or power, than (Ax)’



---PAGE-25---



Sec. 2.2 Review of Hydrodynamics 9

and is stated as "order of AX)^.'' This term is a result of neglected higherorder terms in the Taylor series and implicitly assumes that Ax, Ay, and Az are the same order of magnitude. If the procedure is followed for the y and z directions, their contributions will also be obtained. The net rate of mass accumulation inside the control volume due to flux across all six faces is

Let us now consider this accumulation ofmass to occur for a time increment At and evaluate the increase in mass within the volume. The mass of the volume at time t isp(t)Ax Ay Az and at time (t+ Al) isf i t +At)Ax Ay Az. The increase in mass is therefore

Lt I

Lp(t+ At)-At)]Ax Ay Az = 9At +O(At)2 Ax Ay Az (2.7)

where O(At)* represents the higher-order terms in the Taylor series. Since mass must be conserved, this increase in mass must be due to the net inflow rate [Eq. (2.6)] occurring over a time increment At, that is,

(2.8). ,

ax ay -1az

a@u)+a@v)+a@w' Ax Ay Az At +O(AX)~At

Dividing both sides by Ax Ay Az At and allowing the time increment and size of the volume to approach zero, the followingexact equation results:

ap apu apv apw at ax ay az

-+-+-+-=

(2.9)

By expanding the product terms, a different form of the continuity equation can be derived.

Recalling the definition for the total derivative from the calculus, the term within brackets can be seen to be the total derivative* of p(x, y, z, t ) with respect to time, Dp/Dt or dpldt, given u = dx/dt, v =dy/dt, and w = dz/dt. The first term is then (l/p)(dp/dt)and is related to the change in pressure through the bulk modulus E of the fluid, where

###### E = pdP-

(2.11)

###### dP

'This is discussed laterin the chapter.



---PAGE-26---



10 A Reviewof Hydrodynamicsand Vector Analysis Chap. 2

where dp is the incremental change in pressure, causing the compression of the fluid.Thus

###### I dp 1 dp p dt E dt

--=-- (2.12)

For water, E = 2.07 x 109Nm-2, a very large number. For example, a 1 x lo6Nm-2 increase in pressure results in a 0.05% change in density of water. Therefore,it will be assumed henceforth that water is incompressible.

From Eq. (2.10), the conservation of mass equation for an incompresszble fluid can be stated simply as

I I

(2.13)

I I

which must be true at every location in the fluid. This equation is also referred to as the continuity equation, and the flow field satisfling Eq. (2.13) is termed a “nondivergent flow.” Referringback to the cubein Figure 2.1, this equation requires that if there isa change in the flow in a particular direction across the cube, there must be a corresponding flow change in another direction, to ensure no fluid accumulation in the cube.

- Example 2.1


An example of an incompressible flow is accelerating flow into a corner in two dimensions, as shown in Figure 2.2 The velocity components are u = -Axt and

- w =Azt. To determine if it is an incompiessible flow, substitute the velocity components into the continuity equation, -At + A t =0.Therefore, it is incompressible.


2.2.2 Surface Stresses on a Particle

The motion of a fluid particle is induced by the forces that act on the particle. These forces are of two types, as can be seen if we again refer to the fluid cube that was utilized in the preceding section. Surface forces include pressure and shear stresses which act on the surface of the volume. Body forces,on the other hand, act throughout the volume of the cube.Theseforces

Z

+ Figure2.2 Fluidflow in a corner.

Flow is tangent to solid lines.

0



---PAGE-27---



Sec. 2.2 Review of Hydrodynamics 11

include gravity, magnetic, and other forces that act directly on each individual particle in the volume under consideration.

All of these forces which act on the cubeof fluid will causeit to move as predictedby Newton’s secondlaw,F = ma,for a volume ofconstant massm. This law, which relates the resultant forceson a body to its resultant acceleration a, is a vector equation, being made up of forces and accelerationsin the

- x, y, and z coordinate directions, and therefore all forces for convenience must be resolved into their components.


Hydrostatic pressure. By definition, a fluid is a substance distinguished from solids by the fact that it deforms continuously under the action of shear stresses. This deformation occurs by the fluid‘s flowing. Therefore, for a still fluid, there are no shear stressesand the normal stresses or forces must balance each other, F =0. Normal (perpendicular) stresses must be present because we know that a fluid column has a weight and this weight must be supported by a pressure times the area of the column. Using this static forcebalance, we will show first that the pressure is the same in all directions (i.e., a scalar) and then derive the hydrostatic pressure relationship.

For a container of fluid,asillustrated in Figure 2.3a, the only forcesthat act are gravity and hydrostatic pressure. If we first isolate a stationary prism

offluid with dimensionsA x , Az, A1 [=J(Ax)* +(Az)’], we can examine the force balance on it. We will only consider the x and z directions for now; the forcesin the y direction do not contribute to the x direction.

On the left side of the prism, there is a pressure force acting in the positivex direction,pxAz Ay. On the diagonalface, there must be a balanc-

###### +z +z

t S F ,

###### Figure2.3 Hydrostatic pressureson (a)aprismand(b)acube.



---PAGE-28---



12 A Reviewof Hydrodynamics and Vector Analysis Chap. 2

ingcomponentofp,, which yields the followingform of Newton's secondlaw:

pxAz Ay = p nsin 8 A1 Ay (2.14) In the vertical direction,the force balance yields

pzAx Ay =pn cos8A1 Ay +&g Az Ax Ay (2.15)

where the secondterm on the right-hand side corresponds to the weight of the prism, which also must be supported by the vertical pressure force. From the geometry of the prism, sin 8 =Az/Al and cos 8=Ax/Al, and after substitution we have

P x =P n ~z =Pn +iPg

Ifwe let the prism shrink to zero, then

P x =Pz =Pn

which indicates that the pressures in the x-zplane are the same at a point irrespective of the orientation of the prism's diagonal face, since the final equations do not involve the angle 8.This result would still be valid, of course,if the prism were oriented along they axis, and thus we concludeat a point,

P x =P y =Pz (2.16)

or, the pressure at a point is independent of direction.An important point to notice is that the pressure is not a vector; it is a scalar and thus has no directionassociated with it.Any surface immersed in a fluid will have a force exerted on it by the hydrostatic pressure,and the forceacts in the direction of the normal, or perpendicular to the surface; that is, the direction of the force depends on the orientation of the face considered.

Now, to be consistent with the conservation of mass derivation, let us examine a small cube of sizeAx,Ay, Az (see Figure2.3b). However,this time we will not shrink the cube to a point. On the left-hand face atx -Ax/2 there is a pressure acting on the face with a surface area of Ay Az. The total force tending to accelerate the cube in the +xdirection is

aP Ax

Ay AZ=P(X, y, Z ) Ay AZ---Ay AZ+* . . (2.17)

ax 2

wherethe truncatedTaylorseriesis used, assuminga small cube. On the other

- x face, there must be an equal and opposite force; otherwise, the cube would have to accelerate in this direction. The force in the minus x direction is exerted on the face located atx +Ax/2.


###### aP Ax (2.18)

###### Ay AZ= p Ay AZ+-- Ay AZ

ax 2



---PAGE-29---



Sec. 2.2 Review of Hydrodynamics 13

Equating the two forces yields

-=ap 0

(2.19) For the y direction, a similar result is obtained,

ax

In the vertical, z,direction the force acting upward is

which must be equal to the pressure forceacting downward,and the weight of the cube,pg AX Ay Az, whereg is the accelerationof gravity.

Summing these forces yields

or dividing by the volume of the small cube, we have

###### -aP = -pg

(2.22)

az

Integrating the three partial differential equations for the pressure results in the hydrostatic pressure equation

p =-pgz 4- c (2.23)

Evaluating the constant C at the free surface, z = 0, where p = 0 (gage pressure),

P = -P@ (2.24) The pressure increases linearly with increasingdepth into the fluid.3

The buoyancy force is just a result of the hydrostatic pressure acting over the surface of a body. In a container of fluid, imagine a small sphere of fluid that could be denoted by some means such as dye. The spherical boundaries of this fluid would be acted upon by the hydrostatic pressure, which would be greaterat the bottom of the sphere,as it is deeper there, than at the top of the sphere. The sphere does not move because the pressure difference supports the weight of the sphere. Now, if we could remove the fluid sphere and replace it with a sphere of lesser density, the same pressure forces would existat itssurface,yet the weight would be lessand therefore the hydrostatic force would push the object upward. Intuitively, we would say

'Note that z is negative into the fluid and therefore Eq. (2.24) does yield positive pressure underwater.



---PAGE-30---



14 A Reviewof Hydrodynamicsand Vector Analysis Chap. 2

that the buoyancy force due to the fluid pressureisequal to the weight of the fluid displaced by the object. To examine this, let us look again at the force balance in the z direction, Eq. (2.21):

###### --a ’ Az Ax Ay =pg Ax Ay Az=pg AV =dF, (2.25)

az

which states that the net force in the z direction for the incremental area Ax Ay equals the weight of the incremental volume of fluid delimited by that area. There is no restriction on the size of the cubedue to the linear variation of hydrostatic pressure.

If we now integrate the pressure force over the surfaceof the object, we obtain

Fbuoyancy =PgV (2.26)

The buoyancy force is equalto the weightofthe fluid displaced by the object, as discovered by Archimedes in about 250 B.C., and is in the positive z (vertical) direction (and it acts through the center of gravity of the displaced fluid).

Shear stresses. Shear stresses also act on the surface; however, they differ from the pressure in that they are not isotropic. Shear stresses are caused by forces acting tangentially to a surface; they are always present in a real flowing fluid and, as pressures, have the units of force per unit area.

If we again examine our small volume (see Figure 2.4),we can see that there are three possible stressesfor each of the six faces of the cube; two shear stresses and a normal stress, perpendicular to the face.Any other arbitrarily oriented stress can alwaysbe expressed in terms of these three. On the x face atx +Ax/2 which willbe designated the positivex face, the stresses area,,

T~,,,and rXz.The notation convention for stresses is that the first subscript

Figure 2.4 Shear and normal stresses X on a fluid cube.



---PAGE-31---



- Sec. 2.2 Review of Hydrodynamics 16


refers to the axis to which the face is perpendicular and the second to the direction of the stress. Far a positive face, the stressespoint in the positive axes directions. For the negativex face atx -&/2, the stressesare againom,

7xy, and 7=, but they point in the direction of negative x, y, and z, re~pectively.~Although these stresses have the same designation as those in the positive x face, in general they will differ in magnitude. In fact, it is the difference in magnitude that leads to a net force on the cube and a correspondingacceleration.

There are nine stressesthat are exertedon the cube faces.Three of these stressesinclude the pressure,as the normal stresses are wriften as

IY,=-p+7,

aw=-p +,rw

###### (2.27)

ozz = -P + 722

where

forboth still and flowing fluids. It is possible, however, to show that some of the shear stresses are identical. To do this we use Newton's second law as adapted to moments and angular momentum. If we examine the moments about the z axis, we have

M2=zzo2 (2.28)

where M, is the sum of the moments about the z axis, Z2 is the moment of inertia, and hzis the z component of the angular acceleration of the body. The moments about an axis through the center of the cube, parallel to the z axis, can be readily identified if a slice is taken through the fluid cube perpendicularly to the z axis. This is shown in Figure 2.5. Considering moments about the center of the element and positive in the clockwise direction,Eq. (2.28)is written, in terms of the stresses existingat the centerof

Y

Figure2.5 Shear stresses contributing to moments about the z-axis. Note that rw, r,, are functionsofx andy. X

4Canyou identify the missing stresseson the -Ayy/2)face and orient them correctly?



---PAGE-32---



16 A Review of Hydrodynamics and Vector Analysis Chap. 2

the cube,

###### (2.29)

Reducing the equation leaves

###### z AX Ay AZ-T,, Ax Ay AZ =&p[AX Ay AZ(Ax2+Ay2)]Oz (2.30)

For a nonzero difference, on the left-hand side, as the cube is taken to be smallerand smaller,the accelerationhZmust becomegreater, as the moment of inertia involves terms of length to the fifth power, whereas the stresses involve only the length to the third power. Therefore, in order that the angular acceleration of the fluid particle not unrealistically be infinite as the cube reduces in size, we conclude that,,z =,,z (i.e., the two shear stresses must be equal). Further, similar logic will show that T, = zZx, T,, = .,T Therefore,there are onlysix unknown stresses(axx,T,,, ,,,z T,, a,,, and azz)on the element. These stresses depend on parameters such as fluid viscosityand fluid turbulence and will be discussed later.

2.2.3 The Translational Equations of Motion

For thex direction,Newton’s second law is, again,CF, = ma,, wherea, is the particle acceleration in thexdirection. By definition a, =du/dt,where u is the velocity in the x direction. This velocity, however, is a function of spaceand time, u = u(x,y, z, t);therefore,its total derivative is

du du dudx dudy dudz

-=-+--+--+-- (2.31)

dt at ax dt ay dt az at

or, sincedx/dt is u,and so forth,

du au au au au dt at ax ay az

###### -=- +u-+v-+w- (2.32)

This is the total acceleration and will be denoted asDu/Dt. The derivative is composed of two types of terms, the local acceleration,du/dt, which is the change of u observed at a point with time, and the convective acceleration terms

au au au ax ay az

###### u-+v-+w-

which are the changes of u that result due to the motion of the particle. For



---PAGE-33---



- Sec. 2.2 Review of Hydrodynamics 17


I..

Figure2.6 Accelerationof flowthrough a convergent section.

example, if we follow a water particle in a steady flow (i.e., a flow which is independent of time so that &/at = 0) into a transition section as shown in Figure 2.6, it is clear that the fluid accelerates.The important terms applica-

au au

ble to the figure are the u -and the w -terms.

ax az

The equation of motion in the xdirection can now be formulated:

Du

###### CF..=m-

Dt

From Figure 2.4, the surface forces can be obtained on the six faces via the truncatedTaylor series

###### (0, +%$)AyAz-(0, ---

ax 2

AxAz+(7zx+2$)AxAy (2.33)

The capitalX denotes any body force per unit mass acting in the x direction. Combiningterms and dividing by the volume of the cube yields

DU a0, aTyx aTzx

p- =-+-+-+p x (2.34)

Dt ax ay az

###### or

(2.35) and, by exactly similar developments, the equations of motion are obtained



---PAGE-34---



- 18 A Review of Hydrodynamics and Vector Analysis Chap. 2 for they and z directions:


DV I ap I ar,, az,

p ay p(ax ay a T z y )az

+--+-+- + Y Dt

- -=---
- -=---


- (2.36)
- (2.37)


To apply the equations of motion for a fluid particle, it is necessary to know something about stresses in a fluid. The most convenient assumption, one that is reasonably valid for most problems in water wave mechanics, is that the shear stressesare zero, which resultsin the Euler equations. Expressing the body forceper unit mass as-g in the z direction and zero in thex and

- y directions,we have


_-- --- (2.38a)

DU l a p

Dt pax

the Euler equations (2.38b)

(2.38~)

In many real flow cases, the flow isturbulent and shearstressesareinfluenced by the turbulence and thus the previous stress terms must be retained. If the flow is laminar, that is there is no turbulence in the fluid, the stresses are governed by the Newtonian shear stress relationship and the accelerations are governed by

(2.39a)

+ Y (2.39b)

(2.39~)

andp is the dynamic (molecular)viscosity of the fluid. Oftenp/p is replaced by v,defined as the kinematic viscosity.

For turbulent flows, where the velocities and pressure fluctuate about mean values due to the presence of eddies, these equations are modified to describe the mean and the fluctuating quantities separately, in order to



---PAGE-35---



Sec. 2.3 Review of Vector Analysis 19

facilitate their use.We will not, however,be using these turbulent forms ofthe equations directly.

###### 2.3 REVIEW OF VECTOR ANALYSIS

Throughout the book, vector algebra will be used to facilitate proofs and minimize required algebra;therefore, the use of vectorsand vector analysis is reviewed briefly below.

In a three-dimensional Cartesian coordinate system, a reference system (x,y, z) as has been used before can be drawn (see Figure 2.7). For each coordinate direction, there is a unit vector, that is, a line segment of unit length oriented such that it is directed in the corresponding coordinate direction. These unit vectors are defined as (i, j, k) in the (x,y , z )directions. Thc boldface type denotes vector quantities.Any vector with orientation and a length can be expressed in terms of unit vectors. For example, the vector a can be represented as

a=a,i +ayj+a,k (2.40) where a,, up,and a, are the projections of a on the x,y , and z axes.

2.3.1 The Dot Product

The dot (or inner or scalar) product is defined as

a * b =la! \bl cos8 (2.41)

where the absolute value sign refers to the magnitude or length of the vectors and 8 refers to the angle between them. For the unit vectors, the following identitiesreadily follow:

- i . i = I
- i . j = O

- i * k = O
- j . j = I
- j . k = O


- k * k = l


(2.42)

Z

k



---PAGE-36---



20 A Review of Hydrodynamics and Vector Analysis Chap.2

P

###### A-Figure2.8 Projectionsofvectora.

These rules are commutative, also, so that reversing the order of the operation does not alter the results. For instance,

i..j.=j.i (2.43)

ora b =b a. Consider taking a dot product of the vector with itself.

###### a. a=(axi+ayj+a,k)-(axi+ayj+a,k) (2.44)

=a; +a; +af

Agraphicalinterpretationofa-acanbeobtainedfromFigure2.8,wherethe magnitudeofvectoraisthelengthm.FromthePythagoreantheorem,m2

=OQ'+m.But isjusta,andm2=af+a;.Therefore,m2=a:+a;+a:.

Therefore, the magnitude of vector a can be written as

la1=D=Ja.a (2.45) Thequantitya-basshownbeforeisascalarquantity;thatis,ithasa

magnitude, but no direction (therefore, it is not a vector). Another way to

expressa.bis

a . b = la1 Ibl cos8=a.xbx+a$y+azbz (2.46)

Note that if a b is zero, but neither a or b is the zero vector, defined as (Oi+Oj +Ok),then cos 8must bezero; the vectors are perpendicular to one another.

An important use of the dot product is in determining the projection of a vector ontoanother vector. For example, the projection of vectoraonto the x axis isa. i. In general, the projection ofaonto the bvector direction would bea-b/IbI.

2.3.2 The Cross Product

The cross product (or outer, or vector product) is a vector qualztity which is defined as a x b= 1aI IbI sin 8,but with a direction perpendicular to the plane of a and b accordingto the right-hand rule. For the unit vectors,

###### i x i = j x j = k x k = O ; i x j = k , j x k = i , k x i = j (2.47)



---PAGE-37---



Sec. 2.3 Review of Vector Analysis 21

but this rule is not commutative. So, for example,j x i =-k. A convenient method for evaluating the cross product of two vectors is to use a determinant form:

i j k (2.48) a, ay a, =(a$, -a,by)i+(a,b, -axbz)j+(axby-a$,)k b, by b,

a x b =

2.3.3 The Vector Differential Operator and the

Gradient

Consider a scalar field in space;for example,this might be the temperature T(x,y, z ) in a room. Because of uneven heating, it is logical to expect that the temperature will vary both with height and horizontal distance into

the room. If the te>xb n*Ant . H ? ?

truncated three-dimensionalTaylor series can be used to estimate the temperature at a small distancedr(=dxi+dyj+dzk)away.

T(x+ Ax,y + Ay, z +Az) (2.49)

The last three terms in this expression may be written as the dot product of two vectors:

###### ($i+5j+ k)-(Axi+Ayj+Azk) (2.50)

The first term is defined as the gradient of the temperature and the second is the differential vectorAr.

Thegradient or gradient vectorisoften written asgrad TorVT,andcan be further broken down to

(2.51)

where the first term on the right-hand side is defined as the vector differential operator V, and the second,of course, isjust the scalar temperature.

The gradient always indicates the direction of maximum change of a scalar field' and can be used to indicate perpendicular, or normal,vectors to

'The totaldifferentialdT=VT.dr= IVTI IdrIcos&Themaximumvalueoccurswhendrisin

thedirectionof IVT I.



---PAGE-38---



22 A Review of Hydrodynamics and VectorAnalysis Chap.2

a surface. For example, if the temperature in a room was stably stratified, the temperature would be solely a function of elevation in the room, or T(x,y, z) = T(z). If we move horizontally acrossthe room to a new point, the change in temperature would be zero, as we have moved along a surface of constant temperature. Therefore,

- (2.52)
- (2.53)
- (2.54)


where

-=-=aT aT

0, Ar =dxi+dyj+Ok

ax ay

###### or

VT*Ar=O

which means, using the definition ofthe dot product, that V T isperpendicular to the surface of constant temperature. The unit normal vector will be defined here as the vector n, having a magnitude of 1and directed perpendicular to the surface. For this example,

(2.55)

###### or

###### n =Oi +Oj+lk =k

2.3.4 The Divergence

If the vector differential operator is applied to a vector using a dot product rather than to a scalar, as in the gradient, we have the divergence

(2.56)

###### -_- +-+-

da, day aa,

ax ay a2

We have already seen this operator in the continuity equation, Eq. (2.10), which can be rewritten as

(2.57)

whereu is the velocity vector,u =iu +j v +kw,

v . u = - + - + -du av aw

(2.58)

ax ay az



---PAGE-39---



Sec. 2.3 Reviewof Vector Analysis 23

For an incompressible fluid, for which (l/p) (Dp/Dt)is equal to zero, the divergenceof the velocity is also zero, and therefore the fluid is divergenceless. Another useful result may be obtained by taking the divergence of a gradient,

###### V . V T =

=-+-+-d2T a2T d2T

(2.59)

ax2 ay2 az2

= V2T

Del squared(V2)is known as the Laplacian operator, named after the famous French mathematician Laplace (1749-1827).6

2.3.5 The Curl

If the vector differential operator is applied to a vector using the cross product, then the cud of the vector results.

###### x (a$ +ayj+a,k) (2.60)

Carrying out the cross product, which can be done by evaluating the following determinant, yields

(2.61)

As we will see later, the curl of a velocity vector is a measureof the rotation in the velocity field.

As an exampleof the curl operator, let us determine the divergenceof the curl of a.

%3apter3 is dedicatedto Laplace.



---PAGE-40---



24 A Review of Hydrodynamics and Vector Analysis Chap. 2

Figure 2.9 Integration paths between 0 + two points.

This is an identity for any vector that has continuous first and second derivatives.

2.3.6 Line Integrals

In Figure2.9, two points are shown in the (x-y)plane,Poand PI.Over this plane the vector a(x,y )exists. Consider the integral from Poto PIof the projection of the vector a on the contour line C1.We will denote this integral asF

(2.62)

It is anticipated that should we have chosen contour C2,a different value of the integral would have resulted. The question is whether constraints can be prescribed on the nature of a such that it makes no difference whether we go from POto P,on contour C,or C2.

If Eq. (2.62)were rewritten as

###### F = $?dF

wheredFis the exactdifferentialofF,then F would be equaltoF(Pl)-F(P0); that is, it is only a function of the end points o fthe integration. Therefore, if we can require that a dl be of the form dF, independence of path should ensue. Now,

a. dl =a, dx +a, dz for two dimensions, as dl =dxi +dzk and the total differentialofF is

dF=-dX +-dz=VF-dl

aF aF

(2.63)

ax az

Byequatinga.dlwithdF,we seethatindependenceofpathrequires,intwo

dimensions,

aF aF

(2.64)

a,=- and a,=- or a = V F

ax az



---PAGE-41---



Sec. 2.3 Reviewof Vector Analysis 25

If this is true for axand a,, it followsthat

###### aa, aa, az ax

###### __--- 0 (2.65) as

----a2F a2F - 0 azax axaz

Therefore, in summary, independence of path of the line integral requires that Eq. (2.65) be satisfied. For three dimensions it can be shown that this condition requires that the curl of amust be zero.

- Example 2.2 What is the value of


Pindicatesacompletecircuitaroundtheclosedcontour

if V x a =0 and where the composed of C,and C2?Do this by parts.

Solution.

F=$"a-dl+ a-dl=F(PI)-F(Po)+F(Po)-F(P,)=0

###### PO

Alternatively, note that by Stokes's theorem, the integral can be cast into another form:

F= a-dl=s s(Vxa).nds

whereds is a surface element contained within the perimeter of C,+ CZ,and nis an outward unit normal to ds.Therefore, if V x a is zero, F = 0.

2.3.7 Velocity Potential

Instead of discussingthe vector a, let us consider u,the vector velocity,

givenby

u(x,y , z, t )= ui + vj + wk

(2.66)

Now, letus define the value of the line integralofu as-4:

- + = $ ; u . d l = $ ( u d x + v d y + w dz ) (2.67) The quantity u sdl is a measure of the fluid velocity in the direction of the



---PAGE-42---



26 A Review of Hydrodynamicsand Vector Analysis Chap. 2

contour at each point. Therefore, -4 is related to the product of the velocity and length along the path between the two points PoandPI.The minus signis a matter of definitional convenience; quite often in the literature it is not present.

For the value of 4 to be independent of path, that is, for the flow rate between Poand PIto be the same no matter how the integration is carried out, the terms in the integral must be an exact differential d4,and therefore

- (2.68a)
- (2.68b)


###### (2.68~)

To ensure that this scalar function 4 exists, the curl of the velocity vector must be zero:

The curl of the velocity vector is referred to asthe vorticity a.

The velocity vector u can therefore be conveniently represented as

u =-u$ (2.70)

That is,we can express the vector quantity by the gradient of a scalar function 4 for a flow with no vorticity. Further u flows “downhill,” that is, in the direction of decreasing 4.’If 4 (x,y , z,t )is known over all space, then u,v, and wcan be determined. Note that 4has the units oflength squared divided by time.

Let us examine more closely the line integral of the velocity component along the contour. If we consider the closed path from Poto P,and then back again, we know, from before, that the integral is zero.

###### I

###### u.dl=O (2.71)

which means that if, for example, the path taken from PotoPIand back again were circular, no fluid would travel this circular path.Therefore, we expect no rotation of the fluid in circles if the curl of the velocity vector is zero.

To examine this irrotationality concept more fully, consider the average rate of rotation of a pair of orthogonal axes drawn on the small water mass

’This is the reasonforthe minus sign in the defintion of4.



---PAGE-43---



Sec. 2.3 Reviewof Vector Analysis

27

###### f 1

Az

I

Figure 2.10

shown in Figure 2.10. Denoting the positive rotation in the counterclockwise direction, the average rate of rotation of the axes will be given by Eq. (2.72).

(2.72)

Now if u and w are known at (XO,ZO),the coordinatesof the centerof the fluid mass, then at the edges of the mass the velocities are approximated as

and

Now the angular velocity of the z axis can be expressed as 4 , =-~ (xo,zo+62/21-~(xoZO), - au

6212 az and similarlyfor 8b:

The averagerate of rotation is therefore

(2.73)

Therefore, thej component of the curl of the velocity vector is equalto twice the rate of rotation of the fluid particles, or V x u = 28 = o,where o is the fluid vorticity.

A mechanical analog to irrotational and rotational flows can be depicted by considering a carnival Ferns wheel. Under normal operating



---PAGE-44---



28 A Reviewof Hydrodynamicsand Vector Analysis Chap.2

Figure 2.11 (a) Irrotational motion of chairs on a Ferris wheel; (b) rotationalmotion of the chairs.

conditions the chairs do not rotate; they always have the same orientation with respect to the earth (see Figure 2.11a). As far as the occupants are concerned, this is irrotational motion. If, on the other hand, the cars were fixed rigidly to the Ferris wheel, we would have, first, rotational motion (Figure 2.11b) and then perhaps a castastrophe.

For an inviscid andincompressible fluid,where the Euler equations are valid, there are only normal stresses (pressures) acting on the surface of a fluid particle; since the shear stressesare zero, there are no stresses to impart a rotation on a fluid particle. Therefore, in an inviscid fluid, a nonrotating particle remains nonrotating. However, if an initial vorticity exists in the fluid, the vorticity remains constant.Tosee this, we write the Euler equations in vector form:

###### Du 1

_----vp -gk (2.74)

Dt P

Taking the curl of this equation and substituting V x u = o and V x V p = 0 (identically),we have

###### DO-=o

(2.75)

Dt

Therefore, there can be no change in the vorticity or the rotation of the fluid with time.This theory is due to Lord Kelvin (1869).8

2.3.8 Stream Function

For the velocity potential, we defined 4 as (minus) the line integral of the velocity vector projected onto the line element; let us now define the line integral composed of the velocity component perpendicular to the line

###### *Chapter5 is dedicatedto Lord Kelvin.



---PAGE-45---



Sec. 2.3 Review of Vector Analysis 29

element in two dimensions.

v =$“ti.Po ndl (2.76)

wheredl = IdlI.Consideration of the integrand above will demonstrate that ty represents the amount of fluid crossing the line CIbetween points Poand PI.The unit vector nis perpendicular to the path of integration CI.

To determine the unit normal vector n,it is necessary to find a normal vector N such that

###### N * d l = O

or N, dx +N, dz =0 This is always true if

###### N, =-dz and N, = dx

It would have been equally valid to takeN, =dz and N, =-dx; however,this would have resulted in N directed to the right along the path of integration instead of the left.

To find the unit normal n,it remains only to normalize N.

N -dzi+dxk -dzi+dxk

###### n=--

IN1-&Z-z?= dl

The integral can thus be written as

###### v/ = (-u dz + w dx) (2.77)

For independence of path, so that the flow between Po and PI will be measured the same way no matter which way we connect the points, the integrand must be an exact differential, dty.This requires that

###### w = a x ’av. u=--av

- (2.78)
- (2.79)


az

and thus the condition for independence of path [Eq. (2.65)]is

###### aw au

- + - = O

az ax

which is the two-dimensionalform of the continuity equation. Therefore, for two-dimensional incompressible flow, a stream function exists and if we know its functional form, we know the velocity vector.

In general,there can be no stream function forthree-dimensionalflows, with the exception of axisymmetric flows. However, the velocity potential exists in any three-dimensional flow that is irrotational.



---PAGE-46---



30 A Review of Hydrodynamicsand Vector Analysis Chap.2

Note that the flow rate (per unit width) between points Po and PIis measured by the difference between and y/(Po).If an arbitrary constant is added to both values of the stream function, the flow rate is not affected.

2.3.9 Streamline

velocityvector,or,onastreamline,u-n=0,wherenisthenormaltothe

A streamline is defined as a line that is everywhere tangent to the

streamline. From the earlier section,

dx - dz u w

dz w dx u

_ --_ (2.80)

u - n =-u dz+ wdx = 0 or

or

along a streamline. These are the equations for a streamline in two dimensions. Streamlines are a physical concept and therefore must also exist in all three-dimensional flows and all compressible flows.

From the definition of the stream function in two-dimensional flows, ay//dl= 0on a streamline,and therefore the stream function,when it exists, is a constant along a streamline. This leads to the result Vy/ dl =0 along a streamline, and therefore the gradient ofv/ is perpendicular to the streamlines and in the direction normal to the velocity vector.

2.3.10 Relationshipbetween Velocity Potential and Stream Function

For a three-dimensional flow, the velocity field may be determined from a velocity potential if the fluid is irrotational. For some threedimensional flows and all two-dimensional flows for which the fluid is incompressible,a stream function v/ exists. Each is a measure of the flow rate between two points: in either the normal or transverse direction. For twodimensional incompressible fluid flow, which is irrotational, both the stream function and the velocity potential exist and must be related through the velocity components.

The streamline, or line of constant stream function, and the lines of constant velocity potential are perpendicular, as can be seen from the fact that their gradients are perpendicular:

n $ . V y / = O

as

(a,ia4 +z k )a4 (Ei +$k)=

###### (-ui - wk) (+wi - uk) = (2.81)

-uw + uw =0



---PAGE-47---



Sec. 2.3 Review of Vector Analysis 31

The primary advantage of either the stream function or the velocity potential is that they are scalar quantities from which the velocity vector field can be obtained.As one can easily imagine, it is far easier to work with scalar rather than with vector functions.

Often, the stream function or the velocity potential is known and the other is desired.To obtain one from the other, it is necessary to relate the two. Recalling the definition of the velocity components

u =--=-dVa4 -

ax az

a4 a+ w = - - = -az ax

we have

- (2.82a)
- (2.82b)


These relationships are called the Cauchy-Riemann conditions and enable the hydrodynamicist to utilize the powerful techoiques of complex variable analysis. See for example, Milne-Thomson (1949).

- Example 2.3 For the following velocity potential, determine the corresponding stream function.


2nt

4(x, z, 2 ) = (-3x + 5z) cos -

T

Thisvelocity potential represents a to-and-fro motion of the fluid with the streamlines slanted with respect to the origin as shown in Figure 2.12. The velocity components are

Solution. From the Cauchy-Riemann conditions

or, integrating,

2nt T

Y(X, Z, t )=-3z cos-+C,(X,t )



---PAGE-48---



###### 32 A Reviewof Hydrodynamics andVector Analysis Chap. 2

7

: Figure 2.12

Note that because we integrated a partial differential, the unknown quantity that resultsisa function of both x and t. For the vertical velocity,

-ary 2nt ax =-5 cos -T

###### or

2nt

Y(X, Z, t )=- 5 cos~ -+ G ~ ( z ,t )

T

Comparing these two equations, which must be the same stream function, it is apparent that

###### 2nt

W(X, Z, t)=- ( 5 ~+3Z)cos-+ G(t)

T

The quantity G(t)isa constant with regard to the space variablesx and z and can, in fact, vary with time.This time dependency,due to G(t),has nobearing whatsoeveron the flow field; hence G(t)can be set equal to zero without affecting the flow field.

###### 2.4 CYLINDRICAL COORDINATES

The most appropriate coordinate system to describe a particular problem usually is that for which constant values of a coordinate most nearly conform to the boundaries or response variables in the problem. Therefore, for the caseofcircular waves, which might be generatedwhen a stone is dropped into a pond, it is not convenient to use Cartesian coordinates to describe the problem, but cylindrical coordinates. These coordinates are (r,8,z), which are shown in Figure 2.13. The transformation between coordinates depends on these equations,x = r cos 0,y = r sin 8,and z = z. For a velocity potential defined in terms of (r,8,z),the velocity components are

- (2.83a)
- (2.83b)




---PAGE-49---



Sec. 2.4 Cylindrical Coordinates 33

i

Figure 2.13 Relationshipbetween Cartesianand cylindricalcoordinate systems r and 8lie in the x-y plane.

(2.83~)

As noted previously, the stream function exists only for those threedimensional flows which are axisymmetric. The stream function for an axisymmetric flow in cylindrical coordinates is called the “Stokes” stream function. The derivation of this stream function is presented in numerous references, however this form is not used extensively in wave mechanicsand therefore will not be discussed further here.

###### 2.5 THE BERNOULLI EQ

The Bernoulliequation is simplyan integrated form of Euler equations of motion and provides a relationship between the pressure field and kinematics, and will be useful later. Retaining our assumptions of irrotational motion and an incompressible fluid, the governing equations of motion in the fluid for the x-z plane are the Euler equations, Eqs. (2.38).

- (2.84a)
- (2.84b)


###### Substituting in the two-dimensional irrotationality condition [Eq. (2.69)],

au aw az ax

###### -

- (2.85)
- (2.86)
- (2.87)


###### the equations can be rewritten as

au + a(u2/2)+ a(w2/2) I ap

- ~ --

at ax ax P ax

aw + a(u2/2)+ a(w2/2) 1 ap at az az P az

- ~ --



---PAGE-50---



34 A Review of Hydrodynamics and Vector Analysis Chap.2

Now, since a velocity potential exists for the fluid, we have

u = - - a4. w =--a4

- (2.88)

Therefore, ifwe substitute these definitions into Eqs. (2.86)and(2.87),we get

- (2.89a)


ax' az

(2.89b)

where it has been assumed that the density is uniform throughout the fluid. Integrating the x equation yields

-_a4+A(u2+w2)+P-=C(Z, t )

(2.90)

at 2 P

where, asindicated, the constant of integration C'(z, t )varies only with z and t. Integrating the z equation yields

--a4+-1 (u2+w2)+P-=-gz +C(X,t)

(2.91)

at 2 P

Examining these two equations, which have the same quantity on the lefthand sides, shows clearly that

C(z,t )=-gz +C(X,t )

Thus C cannot be a function of x, as neither C' nor (gz) depend on x. Therefore, C'(z,t )=-gz +C(t).The resulting equation is

###### 1-Tt+L(u22 +w2)+P-P +gz =C(t)

(2.92)

The steady-state form of this equation, the integrated form of the equations of motion, is called the Bernoulli equation, which is valid throughout the fluid. In this book we will refer to Eq. (2.92) as the unsteady form of the Bernoulli equation or, for brevity, as simply the Bernoulli equation. The function C(t)is referred to as the Bernoulli term and is a constant for steady flows.

--a4+P-+-[(>'1 a4 +(31+gz=C(t)

The Bernoulli equation can also be written as

###### (2.93)

at p 2 ax



---PAGE-51---



See. 2.4 CylindricalCoordinates 35

which interrelates the fluid pressure, particle elevation, and velocity potential. Between any two points in the fluid of known elevation and velocity potential, pressure differences can be obtained by this equation; for example, for pointsA and B at elevations zAand z ~the, pressure atA is

(2.94)

Notice that the Bernoulli constant is the same at both locations and thus dropped out of the last equation. [Another method to eliminate the constant is to absorb it into the velocity potential. Starting with Eq. (2.93) for the Bernoulli equation, we can define a functionJt) such that

Therefore, the Bernoulli equation can be written as

###### - +- (2.95)

at P Now, if we define&(x,z, t)=$(x,z, t )+ At),'

(2.96)

Often we will use the & form of the velocity potential, or, equivalently, we will take the Bernoulli constant as zero.] For three-dimensional flows, Eq. (2.96) would be modified only by the addition of (1/2>(d$/~3y)~on the lefthand side.

In the following paragraphs a form of the Bernoulli equation will be derived for two-dimensional steady flow in which the density is uniform and the shear stresses are zero; however, in contrast to the previous case, the results apply to rotational flow fields (i.e., the velocity potential does not exist).In Figure2.14the velocity vector at a point on a streamline is shown, as is a coordinate system, s and n, in the streamline tangential and normal directions.

By definition of a streamline, at A a tangential velocity exists, us,but there is no normal velocity to the streamline un.Referring to Eq. (2.84), the steady-state form of the equation of motion for a particle at A would be

9The kinematics associated with @ (x,z, t ) are exactly the same as $(x, z, t ) , as can be shown easilyby the reader.



---PAGE-52---



###### 36 A Review of Hydrodynamics and Vector Analysis Chap. 2

2

I -g sin OL = forcelunit mass in s direction

Figure 2.14 Definition sketch for derivation of steady-state two-dimensional Bernoulli equation for rotational flows.

written as

au, I ap . as p as

us- = ----g sin a (2.97)

where sin a accounts for the fact that the streamline coordinate system is inclined with respect to the horizontal plane. From the figure, sin a = dz/ds, and therefore the equation of motion is

###### .(.:as -+-+gz2 p 1= o

where again we have assumed the density p to be a constant along the streamline. Integrating along the streamline, we have

-uf +P-+gz =C(y)

(2.98)

2 P

This is nearly the familiar form of the Bernoulli equation, except that the time-dependent term resulting from the local accelerationis not present due to the assumption of steadyflowandalso, the Bernoulli constant isa function of the streamline on which we integrated the equation. In contrast to the Bernoulli equation for an ideal flow, in this case we cannot apply the Bernoulli equation everywhere, only at points along the same streamline.

###### REFERENCES

MILNE-THOMSON,L. M., Theoretical Hydrodynamics, 4th ed., The Macmillan Co.,

###### N.Y., 1960.



---PAGE-53---



###### 37

Chap. 2 Problems

###### PROBLEMS

- 2.1 Consider the followingtransition section:

+lorn&

6m -- i - t - - - +--+3’m

L L ’

- (a) The flow from left to right is constant at Q = 12n m3/s. What is the total accelerationof a water particle in the x direction at x = 5 m?Assume that the water is incompressible and that the x component of velocity is uniformacrosseach cross section.
- (b) The flow of water from right to left isgiven by Q(t>= nt2


Calculate the total acceleration at x = 5 m for t = 2.0 s. Make the same assumptions asin part (a).

- 2.2 Consider the followingtransition section:


y-sjA/--I -----,

- (a) If the flow of water from left to right is constant at Q =.1m’/s, what is the total acceleration of a water particleat x =0.5 m? Assumethat the water is incompressible and that the x component of velocity is uniform across each cross section.
- (b) The flow of water from right to leftis expressedby Q<t>= t2/100


Calculate the total accelerationat x =0.5 m fort =4.48 s. Make the same assumptions as in part (a).



---PAGE-54---



38 A Review of Hydrodynamics andVector Analysis Chap.2

- 2.3 The velocity potential for a particular two-dimensional flow field in which the density is uniform is

2n T

(b =(-3x + 5z)cos-t

where the z axis is oriented vertically upward.

- (a) Isthe flow irrotational?
- (b) Is the flow nondivergent? If so,derive the stream function and sketch any


- 2.4 If the water (assumed inviscid) in the U-tube is displaced from its equilibrium position, it will oscillate about this position with its natural period. Assume that the displacement of the surface is

two streamlines fort = T/8.

where the amplitudeA is 10 cm and the natural period Tis 8 s.What will be the pressure at a distance 20 cm below the instantaneous water surface for tj =+lo, 0,and -10 cm?Assume that g =980cm/s2andp= 1g/cm’.

- 2.5 Suppose that we measure the mass density p at function of time and observe the following:


fixed point (x,y, z) a

From this information alone, is it possible to determine whether the flow is nondivergent?



---PAGE-55---



###### Chap. 2 Problems 39

- 2.6 Derive the following equation for an inviscid fluid and a nondivergent steady flow:

1 ap a(uw)+ a(vw)+ a(w2) p a z ax ay az

-g---=- ~ -

- 2.7 Expand the following expression so that gradients of products of scalar functions do not appear in the result:

v (+wf)

where4, ty,andfare scalar functions.

- 2.8 The velocity components in a two-dimensional flow of an inviscid fluid are

Kx x2+z2

u=-

Kz x2+z2

w = -

- (a) Is the flow nondivergent?
- (b) Is the flow irrotational?
- (c) Sketch the two streamlines passing through points A and R, where the coordinates of these points are:


- Point A: x = 1 , z = 1
- Point B: x = 1,.z = 2


- 2.9 For a particular fluid flow, the velocity components u, v,and w in the .x,y, and z directions, respectively, are

- u = X +8y +6fz+t4
- v = 8~ - l y + 6~ 2at

T

- w = 1 2 +~6y + 1 2 ~cos-- +1’


- (a) Are there any times for which the flow is nondivergent? If so, when?
- (b) Are there any times for which the flow is irrotational? If so,when?
- (c) Develop the expression for the pressure gradient in the vertical (z)direction as a function of space and time.


- 2.10 The stream function for an inviscid fluid flow is w =AX2Zt

where x, z, t 3 0.

- (a) Sketch the streamlines w =0and II/=6A fort = 3s.
- (b) Fort = 5 s,what are thecoordinates ofthepoint where the streamlineslope dz/dx is -5 for the particular streamline w=IOOA?
- (c) What is the pressure gradient at x = 2, z = 5 and at time t = 3 s? A = 1.0, p = 1.0.


- 2.11 Develop expressions for sinh x and cosh x for small values of x . using the Taylor series expansion.




---PAGE-56---



40 A Reviewof Hydrodynamics and Vector Analysis Chap. 2

- 2.12 The pressures pd(f) and pB(t)act on the massless pistons containing the inviscid, incompressiblefluid in the horizontal tube shown below. Develop an expression for the velocity of the fluid as a function of time p = I gm/cm3.

-p 100cm 7-

Note:

p&) = CAsin at P&) =CBsin(at+a)

where a = 0.5 rad/s

c d = C, = 10dyn/cm3

- 2.13 An early experimenter of waves and other two-dimensional fluid motions closely approximating irrotational flows noted that at an impermeable horizontal boundary, the gradient of horizontal velocity in the vertical direction is always zero. Isthis finding in accordancewith hydrodynamic fundamentals?If so,prove your answer.


t

###### X



---PAGE-57---



###### Small-Amplitude Water

###### Wave

Dedication

###### PIERRE SIMON LAPLACE

Pierre Simon Laplace(1749-1827) is well known for the equation that bears his name. The Laplace equation is one of the most ubiquitous equations of mathematical physics (the Helmholtz, the diffusion, and the wave equation being others); it appears in electrostatics, hydrodynamics,groundwaterflow, thermostatics, andother fields.

As had Euler, Laplaceworked in agreat variety of areas, applying his knowledge of mathematics to physical problems. He has been calledthe Newtonof France.

He was born in Beaumont-en-Auge, Normandy, France, and educated at Capn (1765-1767). In 1768he becameProfessor of Mathematics at the Ecole Militaire in Paris. Later he moved to the Ecole Normale,also in Paris.

Napoleon appointed him Minister of the Interior in 1799, and he became a Count in 1806 and a Marquis in 1807, the same year that he assumedthe presidency of the FrenchAcademy of Sciences.

A large portion of Laplace’sresearchwas devoted to astronomy. He wrote on the orbital motion of the planets and celestial mechanics andonthe stability of the solar system. He alsodeveloped the hypothesis that the solar system coalesced out of a gaseous nebula.

Inother areas of physics, he developedthe theory of tides which bears his name, worked with Lavoisier on specific heat of solids, studied capillary action, surface tension, and electric theory, and with Legendre, introduced partial differential equations into the study of probability. He also developed and applied numerous solutions (potential functions)of the Laplace equation.

41



---PAGE-58---



42 Small-Amplitude Water Wave Theory Formulationand Solution Chap. 3

###### 3.1 INTRODUCTION

Real water waves propagate in a viscous fluid over an irregular bottom of varying permeability. A remarkable fact, however, is that in most cases the main body of the fluid motion is nearly irrotational. This is because the viscous effects are usually concentrated in thin “boundary” layers near the surface and the bottom. Since water can also be considered reasonably incompressible, a velocity potential and a stream function should exist for waves. To simplify the mathematical analysis, numerous other assumptions must and will be made as the development of the theory proceeds.

###### 3.2 BOUNDARY VALUE PROBLEMS

In formulating the small-amplitude water wave problem, it is useful to review, in very general terms, the structure of boundary value problems, of which the present problem of interest is an example. Numerous classical

Boundary conditions (B.C.) specified

###### t I

t5B’c‘Regioncanofbeinterestanyshape)(ingeneral,

###### X

\

B.C. specified (a)

Kinematic free surface boundary condition

Dynamic free surface

boundary condition Lateral

(LBO

I Velocitycomponents II

Bottom boundary condition (kinematic requirement)

(b)

###### Figure 3.1 (a) General structureof two-dimensional boundary value problems. (Note:The number of boundary conditions required depends on the orderof the differential equation.) (b) Two-dimensional water waves specified as a boundary value problem.



---PAGE-59---



Sec. 3.2 Boundary Value Problems 43

problems of physics and most analytical problems in engineering may be posed as boundary value problems; however, in some developments, this may not be apparent.

The formulation of a boundary value problem is simply the expression in mathematical terms of the physical situation such that a unique solution exists. This generally consists of first establishing a region of interest and specifyinga differential equation that must be satisfied within the region (see Figure 3.la). Often, there are an infinite number of solutionsto the differential equation and the remaining task is selecting the one or more solutions that are relevant to the physical problem under investigation. This selection is effected through the boundary conditions, that is,rejecting those solutions that are not compatible with these conditions.

In addition to the spatial (orgeometric)boundary conditions, there are temporal boundary conditions which specify the state of the variable of interest at some point in time. This temporal condition is termed an “initial condition.” If we are interested in water waves, which are periodic in space, then we might specify, for example, that the waves are propagating in the positive x direction and that at t =0, the wave crest is located at x = 0.

In the following development of linear water wave theory, it will be helpful to relate each major step to the general structure of boundary value problems discussed previously. Figure 3.lb presents the region of interest, the governing differential equations, and indicates in a general manner the important boundary conditions.

3.2.1 The Governing DifferentialEquation

With the assumption of irrotational motion and an incompressible fluid, a velocity potential exists which should satisfy the continuity equation

###### o . u = o (3.la) or

O*Vi$=O (3.lb)

- As was shown in Chapter 2, the divergence of a gradient leads to the Laplace equation, which must hold throughout the fluid.


The Laplace equation occurs frequently in many fields of physics and engineering and numerous solutions to this equation exist (see,e.g., the book by Bland, 1961), and therefore it is necessary to select only those which are applicable to the particular water wave motion of interest.

In addition, for flows that are nondivergent and irrotational, the Laplace equation also applies to the stream function. The incompressibility



---PAGE-60---



44 Small-Amplitude Water Wave Theory Formulationand Solution Chap. 3

or, equivalently,the nondivergent condition for two dimensions guarantees the existence of a stream function, from which the velocities under the wave can be determined. Substituting these velocities into the irrotationality condition again yields the Laplace equation, except for the stream function this time,

- (3.3a)
- (3.3b)


or

This equation must hold throughout the fluid. If the motion had been rotational, yet fiictionless, the governing equation would be

V2y/ = 0 (3.4)

where ois the vorticity.

A few comments on the velocity potential and the stream function may help in obtaining a better understanding for later applications. First, as mentioned earlier, the velocity potential can be defined for both two and three dimensions, whereas the definition of the stream function is suchthat it can only be defined for three dimensions if the flow is symmetric about an axis (in this case although the flow occurs in three dimensions, it is mathematically two-dimensional). It therefore followsthat the stream function is of greatest use in cases where the wave motion occurs in one plane. Second, the Laplace equation is linear; that is, it involves no products and thus has the interesting and valuable property of superposition; that is, if

- 4,and 42 each satisfy the Laplace equation, then 43=A 4 , +B42 also will solve the equation, whereA and B are arbitrary constants. Therefore,we can add and subtract solutions to build up solutions applicable for different problems of interest.


3.2.2 Boundary Conditions

Kinematictrorrndat-y c a n d i t h A t w e t h e r it is fixed, such as the bottom, or free, such as the water surface,which is freeto deform under the influence of forces,certain physical conditions must be satisfiedby the fluid velocities. These conditions on the water particle kinematics are called kinematic boundary conditions. At any surface or fluid interface, it is clear that there must be no flow across the interface; otherwise, there would be no interface.This is most obvious in the case of an impermeable fixed surfacesuch as a sheet pile seawall.

The mathematical expression for the kinematic boundary condition may be derived from the equation which describes the surface that constitutes the boundary.Any fixed or moving surfacecan be expressed in terms of



---PAGE-61---



Sec. 3.2 BoundaryValue Problems 45

a mathematical expression of the form F(x,y, z, t )=0. For example, for a stationary sphere of fixed radius a,F(x,y, z,t )=x2+y2+z2-a2=0.If the surface vanes with time, as would the water surface, then the total derivative of the surface with respect to time would be zero on the surface. In other words, if we move with the surface, it does not change.

at ax av a F laZ onF(x.y,r,f)=~

W x ,Y ,z, 0 aF aF dF

= o = - + u - + v - + w - (3.5a)

Dt

###### or

###### ---aF

- u . V F = u .nlVFI (3.5b)

at

where the unit vector normal to the surface has been introduced as n = VF/IVFI.

Rearranging the kinematic boundary condition results:

where

This condition requires that the component of the fluid velocity normal to the surfacebe related to the local velocity of the surface.If the surface does

notchangewithtime,thenu-n=0;thatis,thevelocitycomponentnormal

to the surfaceiszero.

Example 3.1

Fluid in a U-tube has been forced to oscillate sinusoidally due to an oscillating pressure on one leg of the tube (see Figure 3.2). Develop the kinematic boundary condition for the free surface in legA .

Solution. The still water level in the U-tube is located at z = O.The motion of the free surfacecan be describedby z = q(t)=a cost ,wherea is the amplitude ofthevanation of q.

If we examine closely the motion of a fluid particle at the surface (Figure 3.2b), as the surface drops, with velocity w,it follows that the particle has to move with the speed of the surfaceor else the particle leavesthe surface.The same is true for a rising surface.Therefore, we would postulate on physical grounds that



---PAGE-62---



###### 46 Small-Amplitude Water Wave Theory Formulation and Solution Chap. 3

###### Oscillating pressure

z = o

(a)

Figure 3.2 (a)Oscillatingflow in a U-tube;(b)detailsoffree surface.

where dqfdt = the rate of rise or fall of the surface. To ensure that this is formally correct, we followthe equation for the kinematic boundary condition, Eq.(3.6), where F(z,t) =z -qt)=0.Therefore,

where n =Oi +Oj +1k, directed vertically upward and u =ui +v j +wk,and carrying out the scalar product, we find that

w = -arl

at

which is the same as obtained previously, when we realize that dqfdt =aqfat,as q is only a function of time.

TheBottom Boundary Condition (BBC). In general,the lowerboundary of our region of interest is described as z = -h(x) for a two-dimensional case where the origin is located at the still water level and h represents the depth.Ifthebottomisimpermeable,we expectthatu-n=0,asthebottom does not move with time. (For some cases, such as earthquake motions, obviouslythe time dependencyof the bottom must be included.)

The surface equation for the bottom is F(x,z) =z +h(x)=0.Therefore,

u . n = O (3.7)

where

dh

- i + l k V F dx

###### (3.8)



---PAGE-63---



Sec. 3.2 Boundary Value Problems 47

Carrying out the dot product and multiplying through by the square root, we have

dh dx

u -+ w =0 on z =-h(x) (3.9a)

###### or

dh w =-u -dx

on z = -h(x)

(3.9b)

For a horizontal bottom, then, w =0 on z =-h. For a sloping bottom, we have

w dh u dx

-=-- (3.10)

Referring to Figure 3.3, it isclear that the kinematic condition states that the flow at the bottom is tangent to the bottom. In fact,we could treat the bottom

- as a streamline, as the flow is everywhere tangential to it. The bottom boundary condition, Eq. (3.7), also applies directly to flows in three dimensions in which h is h(x,y).


Kinematic Free Surface Boundary Condition (KFSBC). The free surface of a wave can be described as F(x,y, z, t ) = z - q(x,y, t )=0, where q(x,y, t )is the displacement of the free surface about the horizontal plane, z = 0.The kinematic boundary condition at the free surface is

u.n= alllat on z = q(x,y, t ) (3.112

J(W W2+(WW2+ 1

i

Figure3.3 Illustration of bottom boundary condition for the two-dimensional case.



---PAGE-64---



48

Small-Amplitude Water Wave Theory Formulation and Solution Chap.3

where

- (3.1lb)
- (3.1lc)


Carrying out the dot product yields

This condition, the KFSBC, is a more complicated expression than that obtained for (l),the U-tube, where the flow was normal to the surface and (2) the bottom, where the flow was tangential. In fact, inspectionofEq.(3.11~)

will verify that the KFSBC is a combination of the other two conditions, which arejust special cases of this more general type of condition.’

The boundary conditions for fixed surfaces arexelatively easy to prescribe, as shown in the preceding section, and they apply on the known surface. A distinguishing feature of fixed (in space) surfaces is that they can support pressure variations. However, surfaces that are “free,” such as the air-water interface, cannot support variations in pressure2 across the interface and hence must respond in order to maintain the pressure as uniform. A second boundary condition, termed a dynamic boundary condition, is thus required on any free surfaceor interface, to prescribe the pressure distribution pressures on this boundary.An interesting effect of the displacement of the free surface is that the position of the upper boundary is not known a priori in the water wave problem. This aspect causes considerable difficulty in the attempt to obtain accurate solutions that apply for large wave heights (Chapter 11).

Dynamic Free Surface Boundary Condition.

As the dynamic free surface boundary condition is a requirement that the pressure on the free surface be uniform along the wave form, the Bernoulli equation [Eq. (2.92)] with p q = constant is applied on the free surface,z = q(x,t),

-_ +1(u2+w’) +P3+gz=C(t)

(3.12)

at 2 P

wherep qis a constant and usually taken as gage pressure,ptl=0.

As noted previously,an additional condition must be imposed on those boundaries that can respond to spatial or temporal variations in pressure. In the case of wind blowingacross

Conditionsat “Responsive”Boundaries.

’Thereader is urged to develop the general kinematic free surface boundary condition for a wave propagatingin the x direction alone. ‘Neglecting surface tension.



---PAGE-65---



Sec. 3.2 Boundary Value Problems 49

a water surface and generating waves, if the pressure relationship were known, the Bernoulli equation would serve to couplethat wind fieldwith the kinematics of the wave. The wave and wind field would be interdependent and the wave motion would be termed “coupled.”If the wave were driven by, but did not affect the applied surface pressure distribution, this would be a case of “forced wave motion and again the Bernoulli equation would serve to express the boundary condition. For the simpler case that is explored in some detail in this chapter,the pressure will be consideredto be uniform and hence a case of “free” wave motion exists. Figure 3.4 depicts various degrees of coupling between the wind and wave fields.

Surface pressure distribution affected by interaction of __Jt Wind wind and waves

###### X

Translating pressure field

p = atmospheric everywhere

###### Figure 3.4 Various degrees of air-water boundary interaction and coupling to atmospheric pressure field: (a) coupled wind and waves; (b) forced waves due to moving pressure field; (c) free waves-not affected by pressure variations at airwater interface.



---PAGE-66---



50 Small-Amplitude Water Wave Theory Formulation and Solution Chap.3

The boundary condition for free waves is termed the “dynamic free surface boundary condition” (DFSBC), which the Bernoulli equation expresses as Eq. (3.13)with a uniform surface pressurep,:

- +5+I[(37+($I2]+gz=C(t), z=~(x,t ) (3.13)

at p 2 ax

where p,,is a constant and usually taken as gage pressure,p,,= 0,

If the wave lengths are very short (on the order of several centimeters), the surface is no longer “free.” Although the pressure is uniform above the water surface, as a result of the surface curvature, a nonuniform pressure will occur within the water immediately below the surface film. Denoting the coefficient of surface tension as o’,the tension per unit length T is simply

###### T = 0‘ (3.14)

Consider now a surface for which a curvature existsasshown in Figure 3.5. Denoting p as the pressure under the free surface, a free-body force analysis in the vertical direction yields

T [-sin aJ,+sin C Y ~ ~ + ~ X+] (p-pa) Ax +terms of orderAx2=0

in which the approximation dq/dx =sin a will be made. Expanding by Taylor’s series and allowing the size of the element to shrink to zero yields

(3.15)

Thus for cases in which surface tension forces are important, the dynamic free surface boundary condition is modified to

-dq5-+p2__(+’d2q-+- 1[(*I2+(?I2]+gz=C(t), z=~(x,t ) (3.16)

at p p ax2 2 ax

which will be of use in our later examination ofcapillary water waves.

Lateral Boundary Conditions. At this stage boundary conditions have been discussed for the bottom and upper surfaces.In order to complete specification of the boundary value problem, conditions must also be speci-

x + Ax Figure3.5 Definition sketch for

surface element.



---PAGE-67---



Sec. 3.2 Boundary Value Problems 51

fied on the remaining lateral boundaries. There are several situations that must be considered.

If the waves are propagating in one direction (say the x direction), conditionsaretwo-dimensionaland then “no-flow” conditionsareappropriate for the velocities in the y direction. The boundary conditions to be applied in thex direction depend on the problem under consideration. If the wave motion results from a prescribed disturbanceof, say, an object atx =0, which is the classical wavemaker problem, then at the object, the usual kinematic boundary condition is expressedby Figure 3.6a.

Consider a vertical paddle acting as a wavemaker in a wave tank. If the displacement of the paddle may be described as x =S(z,t), the kinematic boundary condition is

where

li--kas

-

z

t Outgoingwavesonly

(b)

###### Figure 3.6 (a) Schematic of wavemaker in a wave tank;(b) radiation condition for wavemaker problem for region unboundedin x direction.



---PAGE-68---



52 Small-Amplitude Water Wave Theory Formulation and Solution Chap. 3

or, carrying out the dot product,

(3.17)

which, of course, requires that the fluid particles at the moving wall follow the wall.

Two different conditions occur at the other possible lateral boundaries:

- at a fixed beach as shown at the right side of Figure 3.6a, where a kinematic condition would be applied, or as in Figure 3.6b, where a “radiation” boundary condition is applied which requires that only outgoingwavesoccur at infinity. This precludes incoming waves which would not be physically meaningful in a wavemaker problem.


For waves that are periodic in space and time, the boundary condition is expressed as a periodicity condition,

+(x, 0 =+(x +L,t ) +<x,0 =+(x, t + r)

(3.18a) (3.18b)

where L is the wave length and Tis the wave period.

###### 3.3 SUMMARY OF THE TWO-DIMENSIONAL PERIODIC WATER WAVE BOUNDARY VALUE PROBLEM

The governing second-order differential equation for the fluid motion under a periodic two-dimensional water wave is the Laplace equation, which holds throughout the fluid domain consisting of one wave, shown in Figure 3.7.

###### v2$J= 0, 0 <x <L, - h < z < V (3.19)

I V Z $ = V Z * = O I , - [ Periodiclateralboundary

###### PLBC 1

###### . .._>:.:^.. In7DO,

[ condition (PLBC)

Figure 3.7 Boundary value problem specificationforperiodicwater waves.



---PAGE-69---



Sec. 3.4 Solution to Linearized Water Wave Boundary Value Problems 53

- At the bottom, which isassumed to be horizontal, a no-flow condition applies (BBC):


w = O onz=-h (3.20a)

###### or

a4 - 0 onz=-h

(3.20b) At the free surface, two conditions must be satisfied. The KFSBC,Eq. (3.11c),

az

(3.1lc) The DFSBC, Eq. (3.13), withp, = 0,

-!!$+1[(gy+($71+gq=C(t) onz=rt(x,t ) (3.13)

at 2

Finally, the periodic lateral boundary conditions apply in both time and space, Eqs. (3.18).

(3.1Sa) (3.18b)

- 3.4 SOLUTION TO LINEARIZED WATER WAVE BOUNDARY VALUE PROBLEM FOR A HORIZONTAL BOTTOM


In this section a solution is developed for the boundary value problem representing waves that are periodic in space and time propagating over a horizontal bottom. This requires solution of the Laplace equation with the boundary conditions as expressed by Eqs. (3.19), (3.20b), (3.11c), (3.13), and (3.18).

3.4.1 Separation of Variables

A convenient method for solving some linear partial differential equations is called separation of variables. The assumption behind its use is that the solution can be expressed as a product of terms, each of which is a function of only one of the independent variables. For our case,

$(x, z, t ) = X(X).Z(Z).T(t) (3.21)

where X(x)is some function that depends only on x, the horizontal coordinate, Z(z)depends only on z, and T(t)varies only with time. Since we know



---PAGE-70---



54 Small-AmplitudeWater Wave Theory Formulationand Solution Chap.3

that $ I must be periodic in time by the lateral boundary conditions, we can specifyT(t)= sin at.Tofind a,the angular frequencyof the wave, we utilize the periodic boundary condition, Eq. (3.18b).

sinat =sinoft + T)

###### or

sinat =sin at cosaT +cosat sinaT

which is true foraT =2aor a=2njT. Equally as likely, we could have chosen

cosat or some combination of the two: A cos at +B sin at. Since the

equations to be solvedwill be linear and superposition is valid, we can defer generalizing the solution in time until after the solution components have been obtained and discussed.The velocity potential now takes the form

&x, z, t)= X(x).Z(z).sin at (3.22) Substitutinginto the Laplace equation, we have

-.d2x(x)z(z).sinat +~ ( x-.d2Z(z)) sin at =0

dx2 dz2

Dividing through by4givesus

(3.23)

Clearly, the first term of this equation depends on x alone, while the second term dependsonly on z. If we considera variation in z in Eq. (3.23) holdingx constant, the second term could conceivably vary, whereas the first term could not.This would give a nonzero sum in Eq. (3.23) and thus the equation would not be satisfied.The only way that the equation would hold is if each term is equal to the same constant except for a sign difference, that is,

d2X(xj)d x2=-k2

- (3.24a)
- (3.24b)


###### X(X)

d2Z(z)/dz2

= +k2

Z (Z)

The fact that we have assigned a minus constant to the x term is not of importance, aswe will permit the separation constant k to have an imaginary value in this problem and in general the separation constant can be complex.

Equations (3.24) are now ordinary differential equations and may be solved separately.Three possible cases may now be examined depending on the nature of k;these are for k real, k =0, and k a pure imaginary number. Table 3.1 lists the separatecases. (Note that ifk consistedofboth a real and an imaginary part, this could imply a change of wave height with distance, which may be valid for cases of waves propagating with damping or wave growth by wind.)



---PAGE-71---



Sec. 3.4 Solution to LinearizedWater Wave BoundaryValue Problems 55

TABLE 3.1 Possible Solutions to the Laplace Equation, Based on Separation ofVariables

Character of k, the Ordinary Differential

Separation Constant Equations Solutions

###### e+k2X=0

X(x)=A coskx +Bsin kx

Real

dx2

###### Z(z)=Cek' +De-'"

_ _ k2Z=0 dz2

k2> 0

k=O -=

X(X)=AX+B Z(Z)=CZ+D

0

dx2

-=od2Z

dz2

IkI=magnitudeofk e+lkI2Z=0 Z(z)=CcosIklz+Dsinlklz

dz2

3.4.2 Application of Boundary Conditions

The boundary conditions serve to select, from the trial solutions in Table 3.1, those which are applicable to the physical situation of interest. In addition,the use of the boundary conditions allowsdeterminationof someof the unknown constants (e.g.,A , B, C,and D).

Lateral periodicity condition. All solutions in Table 3.1 satisfy the Laplace equation; however, some of them are not periodic in x;in fact, the solution is spatially periodic only ifk is real3and nonzero. Therefore,we have as a solution to the Laplace equation the following velocity potential:

$(x,z, t )=(A cos kx +B sin kx)(Cekz+D&) sin ot (3.25)

To satisfy the periodicity requirement (3.18a)explicitly,

A coskx +B sin kx =A cos k(x +L)+B sin k(x +L )

=A(cos kx cos kL - sin kx sin kL)

+B(sin kx cos kL +cos kx sin kL)

which is satisfied for coskL =1and sin kL = 0;which means that kL = 27cor k (called the wave number) =27c/L.

Using the superposition principle, we can divide $ into several parts. Let us keep, for present purposes, only$=A coskx(Cekz+ sinat.Lest

'Fork =0,A is zero.This ultimately yields c$ = B sin ct.



---PAGE-72---



58 Small-Amplitude Water Wave Theory Formulation and Solution Chap. 3

this be thought of as sleight of hand, the B sin kx term will be added back in later by superposition.

Bottom boundary conditionfor horizontalbottom. Substituting in the bottom boundary condition yields

###### a+

w = --= -A cos kx(kCek"- kDe-&')sin at =0 on z =-h (3.26)

az

###### or

###### -Ak cos kx(Ce-kh-Dekh)sin at = 0

For this equation to be true for any x and t,the terms within the parentheses must be identically zero, which yields

###### C = DeZkh

The velocity potential now reads

c$ =A coskX(DeZkhe" +De-k')sin at or, factoring out Dekh,

+=~ ~cos &(ek(h+4~ k +he-k(h+z))sin at

###### or

+=Gcoskxcoshk(h+z )sinat (3.27)

where G = 2ADekh,a new constant.

Dynamic free surface boundary condition. As stated previously, the Bernoulli equation can be used to specify a constant pressure on the surface of the water.Yet the Bernoulli equation must be satisfied on z = q(x,t),which is a priori unknown. A convenient method used to evaluate the condition, then, is to evaluate it on z = q(x,t )by expanding the value of the condition at z =0 (a known location) by the truncated Taylor series.

(Bernoulli equation),,, = (Bernoulli equation),,o

###### (3.28)

+q -d (Bernoulli equation),,o +. . .

az

or

gz--+-a+ u2+w2

at

wherep=Oonz=q.



---PAGE-73---



Sec. 3.4 Solutionto Linearized Water Wave BoundaryValue Problems 57

Now for infinitesimally small waves, r] is small, and therefore it is assumed that velocities and pressures are small; thus any products of these variables are very small: r] << 1, but q2<< r], or ur]<< r]. If we neglect these small terms, the Bernoulli equation is written as

This process is called linearization. We have retained only the terms that are linear in our variable^.^ The resulting linear dynamic free surface boundary condition relates the instantaneous displacement of the free surface to the time rate of change of the velocity potential,

- (3.29)
- (3.30)


If we substitute the velocity potential, as given by Eq. (3.27),

1coskxcosot+-C(t)

- [Gocosh kh L g l g

Since by our definition r] will have a zero spatial and temporal mean, C(t)= 0.5Theterms within the brackets are constant; therefore, r] is given as a constant times periodic terms in space and time plus a function of time. We can rewrite r] as

###### H

coskx cos ot (3.31)

r] =-2

The last substitution came about by comparing the analytical representation of r] to the physical model, as shown in Figure 3.7. G can now be obtained from

###### f&

G = The velocity potential is now

2a cosh kh

(3.32)

The velocity potential is now prescribed in terms ofH,o,h, and k. The

4Linearin the sense that variablesare only raisedto the first power. 'Had we not usedp(q)=0, how would C(t)be changed?



---PAGE-74---



58 Small-Amplitude Water Wave Theory Formulation and Solution Chap. 3

first three of these would be available from the data or alternatively the wave length might be known and ounknown.

Kinematic free surface boundary condition. The remaining free surface boundary condition will be utilized to establishthe relationship between nand k. Using theTaylor series expansion torelate the boundary condition at the unknown elevation,z = q(x,t )to z =0, we have

Again retaining only the terms that are linear in our small parameters, q, u, and w,and recallingthat qis not a function ofz, the linearized kinematic free surface boundary condition results:

- (3.33a)
- (3.33b)


###### or

Substitutingfor4and qgives us

###### H gk sinh k(h+z)

coskx sin at Iz=o

2 o cosh kh

=- H ocoskx sinot

###### 2

or

(3.34)

Rewriting this equation as dh/gkh =tanh kh and plotting each term versus kh for a particular value of d h / g yields Figure 3.8. The solution is determined by the intersection ofthe two curves. Therefore, the equation has only one solution or equivalently one value of k for given values of oand h.

Noting that by definition a propagating wave will travel a distance of one wave length L, in one wave period T, and recalling that a = 2z/T and k = 2n/L,it is clear that the speed of wave propagation C can be expressed from Eq. (3.34)as

(FY=g2tanhkh

###### L



---PAGE-75---



###### Sec. 3.4 Solutionto Linearized Water WaveBoundary ValueProblems 59

## 1.or r

2.0

1.o

-0

###### 0 1.o

1.o 2.0 3.0

0

kh

Figure 3.8 Illustrating single root to dispersion equation.

or

C2 =-=-tanhkhL2 g T2 k

(3.35)

A similar algebraicmanipulation of Eq. (3.34) will yield a relationship forthe wave length,

g 2nh

L =-T2 tanh -

(3.36)

2n L

In deep water, kh is large and tanh 2nhlL = 1.0;therefore, L = Lo =gT2/2n, where the zero subscriptisused to denote deep water values. In general, then,

L =Lotanh kh (3.37)

Thus the wave length continually decreases with decreasing depth €or a constant wave period.

Equations (3.34), (3.35),and (3.37), which are really the same equation expressed in slightly different variables, are referred to as the “dispersion” equation, because they describe the manner in which a field of propagating wavesconsistingof many frequencieswould separate or “disperse”duetothe different celeritiesof the various frequency components.

The wave speed, or celerity, C, has been defined as C =LIT.Therefore, L O (3.38a)

C =-tanh kh

T



---PAGE-76---





---PAGE-77---



Sec. 3.4 Solution to LinearizedWater Wave Boundary Value Problems 61

or

C = Cotanh kh (3.38b)

since, as will be shown later, the wave period does not change with depth. Waves of constant period slow down as they enter shallow water. Figure 3.9 presents, as a function of h/Lo,the ratio C/Co(=L/Lo= ko/k)and a number of other variables commonly occuringin water wave calculations.Thisfigure provides a convenient graphical means to determine intermediate and shallow water values of these variables.

3.4.3 Summary of StandingWaves

One solution of the boundary value problem for small-amplitude waves has been found to be

###### c p - -H g cash k(h +z) cos kx sin

2 a cosh kh

= cos kx cos at g at r=O 2

(3.39) whered =gk tanh kh.

The wave form is shown in Figure 3.10. At at = n/2, the wave form is zero for all x, at at =0, it has a cosine shape and at other times, the same cosine shape with different magnitudes. This wave form is obviously a “standing wave,” as it does not propagate in any direction. At positions kx = n/2, and 3n/2, and so on, nodes exist; that is, there is no motion of the free surface at these points. Standing waves often occur when incoming waves are completely reflected by vertical walls. At which phase position would the wall be located? See Figure 4.6 for a hint.

Figure 3.10 Water surface displacementassociatedwith astandingwater wave.



---PAGE-78---



62 Small-Amplitude Water Wave Theory Formulationand Solution Chap. 3

3.4.4 ProgressiveWaves

Consider another standing wave,

###### (3.40)

This velocity potential is also a solution to the Laplace equation and all the boundary conditions, as may be verified readily. It is, in fact, one of the solutions that we discarded. It differs from the previous solution in that thex and t terms are 90"out of phase.The associated water surface displacement is

g7at z=o 2

q(x,t)=-- =-- sin k~ sin at

(3.41)

as determined from the linearized DFSBC. Remembering that the Laplace equation is linear and superposition is valid, we can add or subtract solutions to the linearized boundary value problem to generate new solutions. If we subtract the present velocity potential in Eq. (3.40) from the previous solution we had, Eq. (3.32),we obtain

- (3.42)
- (3.43)


This new velocity potential has a water surface elevation, given as H

=-cos (kx-at) g at z=o 2

Had we just subtracted the two q(x,t) corresponding to the two velocity potentials, we would have had

###### H H . H

q(x,t )=-cos kx cos at +-sin kx sin at =-cos(kx-at)

2 2 2

which is the same result. This should not have been a surprise, as the total boundary value problem has been linearized and superposition is valid for all variables in the problem.

Examiningthe equation for the water surface profile, it is clear that this wave form moves with time. To determine the direction of movement, let us examine the same point on the wave form at two different time values, tland t2.The x location of the point also changes with lime. In Figure 3.11, the locations of the point at time tI and tZare shown.The speed at which the



---PAGE-79---



###### Sec. 3.4 Solutionto Linearized Water Wave Boundary Value Problems 63

X

Figure 3.11 Characteristicsofa propagating wave form.

wave propagated from one point to the other is C,given as

###### C=-x2 -XI t2 -tl

We further point out that the samepoint on the wavecrest impliesthat we are examining the wave at the same phase, that is, at constant values of the argument of the trigonometric function ofx and t.Therefore, we expect that

or, in fact,

###### or

###### -=--a 2nfT -C=-=-X I -x2 x2-xI k 2nfL tl - t 2 t 2 - tl

as before.Therefore, if t2 > t l ,x2 >x i,the wave form propagates from left to

right. Had the argument ofthe trigonometric function been (kx+at),the

waves would propagate from right to left (i.e., in the negative x direction).

Simplificationsfor shallowand deep water. The hyperbolic functions have convenient shallowanddeep water asymptotes, and often it is helpful to use them to obtain simplified forms of the equations describing wave motion. For example, the function cosh kh,which appearsin the denominator for the velocity potential, isdefined as

ekh + e-kh

cash kh = 2

For a small argument, the exponential function e"can be expanded to z =kh in aTaylor seriesabout zero as



---PAGE-80---



64 Small-Amplitude Water Wave Theory Formulation and Solution Chap.3

or

###### e k h = l + k h + -(kh)*+. . *

2 Of course, ckhwould then equal

###### . .

Therefore, for small kh,

For large kh, cosh kh = ekh/2as e-khbecomes quite small. Table 3.2 presents the asymptotes.

TABLE 3.2 Asymptotic Formsof HyperbolicFunctions

Function Large kh Small kh

cosh kh sinh kh tanh kh

$ h / 2 1

PI2 kh 1 kh

It is worthwhile to distinguish the regions within which these asymptotic approximations become valid. Figure 3.12 is a plot of hyperbolic functions together with the asymptotes,& = kh,fi = 1.O,f3 = ekh/2.The percentage values presented in Figure 3.12 represent, for particular ranges of kh, the errors incurred by using the asymptotes rather than the actual value of the function. The largest error is %o. The lower scale on the figure is the relative depth. Note that dueto this dimensionless representation a 200-m-long wave in 1000 m of water has the same relative depth as a 0.2-m wave in 1 m of water. Limits for three regions are denoted in the figure: kh < n/10, n/10 < kh < n,and kh > n. These regions are defined as the shallow water, intermediate depth, and the deep water regions, respectively. It may be justified to modify the limits of these regions for particular applications.

The disperd=gk tanh kh =gk’h

The dispersion relationship in shallow and deep water.

sion relationship for shallow water reduces in the following manner:



---PAGE-81---



- sinh kh

A h

tanh kh

0 T/lO 1 2

3 7 r

kh

Intermediate depth (long waves) (short waves)

Shallow water waves waves Deep water waves

###### Figure 3.12 Relative depth and asymptotes to hyperbolic functions.

65



---PAGE-82---



66 Small-Amplitude Water WaveTheory Formulationand Solution Chap. 3

###### or

###### and

###### C=@ (3.44)

The wave speed in shallow water is determined solely by the water depth. Recall that the definition of shallowwater is based on the relative depth. For theocean,wherehmightbe-1km,awavewithalengthof20kmisin shallow water. For example, tsunamis, which are waves caused by earthquake motions of the ocean boundaries, have lengths much longer than this. The speed in the ocean basins for long waves would be about 100m/s (225 mph).

For deep water,kh > n, d =gk tanh kh =gk L=Lo

where

5.12T2(English system of units, ft) 1.56T2(SI units, meters)

###### L~=.E~ 2 =

###### 2 R

and

(3.45)

5.12T (English system of units, ft/s) 1.56T(SI units, m/s)

Co=-T=g 2n

3.4.5 Waves with Uniform Current UO

As an example of the procedure just followed for the solution for progressive and standing waves, it is instructive to repeat the process for a differentcase: water waves propagatingon a current. For example, for waves in rivers or on ocean currents, a first approximation to the waves and currents is to assume that the current is uniform over depth and horizontal distanceand flowingin the same direction as the waves.

An assumed form of the velocity potential will be chosen to represent the uniform current Uoand a progressive wave, which satisfies the Laplace equation.

4=-UG +A CoShk(h +Z ) cos(kx-at) (3.46)

The form of this solution guarantees periodicity of the wave in space and time and satisfies the no-flow bottom boundary condition. It remains neces-



---PAGE-83---



Sec. 3.4 Solutionto LinearizedWater Wave Boundary Value Problems 67

sary to satisfy the linearized form of the KFSBC and the DFSBC. Yet we cannot just apply the forms that we arrived at earlier, as errors would be incurred because the velocity Uois no longer necessarily small; we must rederive the linear boundary conditions.

The dynamic free surface boundary condition. Again, we will expand the Bernoulli equation about the free surface on which a zerogage pressure is prescribed.

(3.47)

azai‘2 ::Izd

+ q - -(u’+w2)+gz-- + * . . =C(t)

Now the horizontal velocity is

u=--”=u +Ak cosh k(h+z) sin(kx-at)

###### ax

Therefore, the u2term is

u2= Ui+U k U ocosh k(h +z) sin (kx-at) +A2k2cosh2k(h+z)sin’ (la-at)

For infinitesimal waves, it is expected that the wave-induced horizontal velocity component would be small (i.e., Ak small), and therefore (Ak)’ would be much smaller. We will then neglect the last term in the equation above.

The linearized Bernoulli equation [i.e., dropping all terms of order (Ak)’],evaluated on z = 0, is now

+[v2, +UkUocosh kh sin (kx-at)] -A a cosh kh sin (kx- at)+gq = C(t)

###### or

cosh kh sin(kx-at)+C(t)

(3.48)

2g g

To determine the Bernoulli term C(t),we average both sides of Eq. (3.48) over space. Sincethe spaceaverageof q(x,t) is taken to be zero, it is clearthat C(t)= constant = G/2g. Also, if we define a water surface displacement, q(x,t ) =H/2 sin (kx-at),then

A = gH (3.49)

20(1 - Uo/C)cash kh



---PAGE-84---



68 Small-Amplitude Water Wave Theory Formulation and Solution Chap. 3

The kinematic free surface boundary condition. The remaining boundary condition to be satisfied is the linearized form of the KFSBC.

###### all a4arl a47 z=rl at ax ax az

Expanding about the still water level, we have

or, retaining only the linear terms,

###### (3.50)

Substituting forqand4yieldsthe followingdispersion equation for the case of a uniform current Uo:

d =gk tanh kh

- (3.51)
- (3.52)


(1 - uo/c)2

or, another form can be developed by using the relationship Q = kC:

02d(1(1---(/Okj2?)'=gktanhkh=gktanhkh

###### a / -

or

Q=Uok+Jm

The second term on the right-hand side is the angular frequency formula obtained without a current.

In terms of the celerity, the dispersion relationship can be written as (C- U0)*=g-tanh kh (3.53)

k

It is worthwhile noting that it is possible to solve the preceding problem of a uniform current simply by adopting a reference frame which moves with the current Uo.With reference to our new coordinate system, there is no current and the methods, equations, and solutions obtained are therefore identical to those obtained originally for the case of no current.

When relating this moving frame solution for a stationary reference system, it is simply necessary to recognize that (1) the wavelength is the same in both systems;(2) the period T relative to a stationary reference system is related to the period T'relative to the reference system moving with the



---PAGE-85---



Sec. 3.4 Solutionto Linearized Water Wave Boundary Value Problems 69

current Uoby

(3.54)

where C' is the speed relative to the moving observer; and (3) the total water particle velocity is Uo+ u,, where u, is the wave-induced component. It is noted that in the case of arbitrary depth, when T and h are given, it is necessary to solve for the wave length from Eq. (3.54) by iteration.6

For shallow water, we have, from Eq. (3.53),

###### L

c=-=T uo+&% (3.55) That is, since the celerity of the wave is independent of wave length, it is simply increased by the advecting current Uo. For deep water, the corresponding result is determined by solving Eq. (3.53) for C using the quadratic solution and replacing k with o/C,that is,

(3.56) For small currents with respect to C (i.e., Uo<g/a),

c1:g-+2u0

0

Capillary waves. As indicated in Eq. (3.16), the surface tension at the water surface causes a modification to the dynamic free surface boundary condition. To explore the effects of surface tension, we proceed as before by choosing a velocity potential of the form

6=A cosh k(h +z)sin (kx-ol) (3.57)

which is appropriate for a progressive water wave, satisfies the Laplace equation, and all boundary conditions except those at the upper surface.The surface displacement associated with Eq. (3.57) will be of the form

###### H

q =-cos(kx-a)

(3.58)

2

Substituting Eqs. (3.57) and (3.58) into the linearized form of Eq. (3.16), and employing the linearized form of the kinematic free surface boundary condition, Eq. (3.33a), the dispersion equation is found to be

(3.59)

6Thistechniquehas been appliedto nearly breaking wavesby Dalrympleand Dean(1975).



---PAGE-86---



70 Small-Amplitude Water Wave Theory Formulation and Solution Chap.3

and it can be seen that the effect of surface tension is to increase the celerity for all wave frequencies.The effect of surface tension can be examined most readily by considering the case of deep water waves.

###### (3.60)

That is, the contributions due to the speed of short waves (large wave numbers) is small due to the effect of gravity and large due to the effect of surfacetension.Thereis a minimum speed C, at which waves can propagate, found in the usual way:

###### _-ac-0

- (3.61)
- (3.62)
- (3.63)


###### ak

k,=v$

which leadsto

That is, the contributions from gravity and surface tension to Ci are equal. For a reasonable valueof surface tension, a’=7.4x lo-*N/m, C, N 23.2cm/s, which occurs at a wave period of approximately0.074 s.Figure 3.13 presents

2

###### ty contribution

0 1 2 3 4

-k

km

Figure 3.13 Capillary and gravitational components ofthe squareofwave celerity in deep water.



---PAGE-87---



Sec. 3.5 Appendix: ApproximateSolutions to the Dispersion Equation 71

the relationship

(3.64)

3.4.6 The Stream Function for Small-Amplitude

Waves

For convenience, the velocity potential has been used to develop the small-amplitude wave theory, yet often it is convenient to use the stream function representation. Therefore, we can use the Cauchy-Riemann equations, Eqs. (2.82),to develop them from the velocity potentials.

Progressivewaves.

- (3.65)
- (3.66)


H g sinh k(h +z) 2 a cosh kh

cos(kx-ot)

v/(x,2, t )= ---

It is often convenient for a progressive wave that propagates without changeof form to translate the coordinate system horizontallywith the speed of the wave, that is, with the celerity C, as this then gives a steady flow condition.

H gsinh k(h +z)coskx 2 o cosh kh

v / = c z - - -

- (3.67)
- (3.68)
- (3.69)


###### Standing waves. From before,

H g sinh k(h +z) v / = - - - 2 a cosh kh

sin kx sin at

The streamlines and velocity potential for both cases are shown in Figure 3.14.The streamlines and potential lines are lines of constant v/ and 4.

3.5 APPENDIX: APPROXIMATE SOLUTIONS TO THE

DISPERSION EQUATION

The solution to the dispersion relationship, Eq. (3.34),fork is not difficult to obtain for given aand h. However, since the relationship is a transcendental



---PAGE-88---



###### 72 Small-Amplitude Water Wave Theory Formulation and Solution Chap. 3

_ _ _ _ Streamlines

Velocity potential

Progressive wave, Progressive wave, Standing wave, stationary reference reference frame moving stationary reference frame with speed of wave frame

Figure 3.14 Approximate streamlines and lines of constant velocity potential for varioustypes ofwave systems and reference frames.

equation, in that it is not algebraic, graphical (see Figure 3.8) and iterative techniques are used (see Problem 3.15).

Eckart (1951) developed an approximate wave theory with a corresponding dispersion relationship,

This can be solved directly for k and generally is in error by only a few percent. This equation therefore can be used as a first approximation to k for an iterative technique orcan be used to determine k directlyif accuracyis not a paramount consideration.

Recently, Hunt (1979) proposed an approximate solution that can be solved directly for kh:

###### (kh)2=y2+ Y

###### 1+ Cdnyn

n=l

where y =d h / g=kohanddl=0.666...,d2=0.355...,dj=0.1608465608,d4 =0.0632098765,ds=0.0217540484,and d6 =0.0065407983.The last digitsin dland d2 are repeated seven more times. This formula can be conveniently used on a programmablecalculator.

The wave celeritywas also obtained

###### C2

-=[y +(1 +0.6522~+0.4622~~+0.0864~~+0.0675~~)-~]-'

###### gh

which is accurateto 0.1%for 0 <y < co.



---PAGE-89---



Chap.3 Problems 73

REFERENCES BLAND,D. R., Solutions of LaplaceS Equation, Routledge & Kegan Paul, London,

1961.

DALRYMPLE,R. A., and R. G. DEAN,“Waves of Maximum Height on Uniform

Currents,” J. Waterways,Harbors Coastal Eng. Div., ASCE, Vol. 101, No. WW3, ECKART,C., “SurfaceWavesonWater ofvariable Depth,” SIO51-12, ScrippsInstitute HUNT,J. N., “Direct Solution of Wave Dispersion Equation,” J. Waterways,Ports,

pp. 259-268,1975. of Oceanography,Aug. 1951. Coastal OceanDiv.,ASCE,Vol. 105, No. WW4, pp. 457-459,1979.

###### PROBLEMS

- 3.1 The linearization of the kinematic and dynamic free surface boundary conditions involved neglecting nonlinear terms. Show, for both the conditions, that this linearization implies that

q..1

L

- 3.2 Near the bow of a moving submarine, the hull can be represented as a moving parabola,

D(z -A)’ = -(x - Ut)

where U is the speed of the submarine, A represents the depth of the centerline of the submarine below the free surface,and D is a constant.

- (a) Plot the hull shape at t = 0and t = 1 s if the submarine is moving at 2 m/s.
- (b) Determine the kinematic boundary condition at the hull.


- 3.3 The equation for the stationary boundary c(x) of an incompressible fluid is ((x) =Ae-K”


2

###### t

The horizontal velocity component may be regarded to be approximately uniform in the z direction. If u(x=O) = 40cm/s, A = 30cm, and K = 0.02 cm-’, calculate w at the upper boundary forx = 50 cm.



---PAGE-90---



74 Small-Amplitude Water Wave Theory Formulationand Solution Chap. 3

- 3.4 The equation for the upper moving boundary L(x,t) of an incompressible fluid is

c,,(x, t ) = The lower boundary Cr is expressed by

Cdx, t )=0 A =30cm k =0.02 cm-'

M =0.1 s-'

- (a) Sketch the boundaries for t =0.
- (b) Discussthe motional characteristics of the upper boundary (i.e., speed and
- (c) The horizontal velocity component (u) may be regarded to be approxi-


direction). mately uniform in the z direction. If

u(x = 0, t = 10s) = 40 cm/s

calculate w at the upper boundary for x = 50cm and t = 10s.

- 3.5 Using separation of variables, solve in cylindrical coordinates the problem of steady flow past a cylinder. Given Laplace's equation

4rr+-r1+r +-r214- =0

in which the subscripts denote partial differentiation with respect to the subscripted variable. The boundary conditions are

in two dimensions

4 = Ur cos8 at r large and

4,Ir-a =O

- 3.6 A two-dimensional horizontal flow is described by

&x, Y)=w2-Y2)

Find the point ofmaximum pressure ifp =0at (x,y ) =(1, 1).

A wave field is observed by satellite. The wave lengths are determined to be 312 m in deep water and 200 m over the continental shelf. What is the shelf depth?

Formulate the boundary value problem for the situation below, which represents a model to study the effects of waves on a harbor with a narrow entrance. The strokeSofthe wavemaker is considered to be small compared to the depth h.

- 3.7
- 3.8




---PAGE-91---



###### Chap. 3 Problems 75

f h 3

Flaptype wavemaker (simple harmonic motion)

Elevation view

3.9 Set up,but donot solve, the complete two-dimensional(x,z, t )boundary value problem as illustrated, which was designedto simulate earthquake motions of the continental shelf. The slopingbottom oscillates with a period T and has an amplitudea. State all assumptions.

\-

###### Neglect corner effects



---PAGE-92---



76 Small-AmplitudeWater Wave Theory Formulationand Solution Chap. 3

- 3.10 A horizontal cylindrical wavemaker is oscillating verticallyin the free surface. Examiningthe two-dimensional problem shownbelow, develop the kinematic boundary condition for the fluid at the cylinder wall. Discussthe results.

t = O

I=-T

4

t = -3T

4

where Tis period of oscillation.

- 3.11 The stream function for a progressive small-amplitude wave is

w = - - -H2 gusinhcoshk(hkh+z )cos(h-at)

Draw the streamlines for t =0, when T = 5 s, h = 10 m, and H = 2.0 m.

- 3.12 You are on a ship (100m in length) on the deep ocean traveling north. The (regular)waves are propagating north also and you note two items of information: (1) when the shipbow is positioned at a crest, the stern is at a trough, and

(2) a different crest is positioned at the bow every 20 s. (a) Doyou have enough information to determine the ship speed? (b) Ifthe answer to part (a) is “no,” what additional item(s) ofinformation are

(c) If the answer to part (a)is “yes,” what is the ship speed?

- 3.13 A tsunami is detected at 12:OO h on the edge of the continental shelf by a warning system. At what time can the tsunami be expected to reach the shoreline?


required?

Warning system sensor --



---PAGE-93---



Chap. 3 Problems 77

- 3.14 A rigid sinusoidal form is located as shown in the sketch. The form is forced to move in the +x direction at speed V.

- (a) Derive an expression for the velocity potential for the water motion induced by the moving form.
- (b) Evaluatepc-p ,for the following cases:

- (1) V2<g tanh kh k
- (2) V2=g tanh kh k
- (3) V2> tanh kh k


where pcand p , denote the pressure just below the form at the crest and trough, respectively.

- (c) Discuss the special significance of b(2).


l h

- 3.15 Develop an iterative technique to solve the dispersion relationship for k given u and h. Note: It is somewhat easier to first solve for kh. (Hint:A NewtonRaphson technique could be used.)
- 3.16 Determine the celerity of a deep water wave on a current equal to 50 cm/s and T = 5 s. What is the wave period seenby an observer moving with the current?
- 3.17 Develop the boundary value problem for small-amplitude waves in terms of the pressure, assuming that Euler's equations are valid and the flow is incompressible.




---PAGE-94---



###### ve

###### ertie

Dedication

###### SIR GEORGE BIDDELL AIRY

Sir George Biddell Airy (1801-1892) was an astronomer who worked in a variety of areas of science, as did his contemporary and personal acquaintance, Laplace. His major work with respect to this book is his development of small-amplitude water wave theory published in an article inthe EncyclopediaMetropolitan.

Airy ‘was born in Alnwich, Northumberland, England, and attendedTrinity College, Cambridge, from 1819to 1823. In 1826 hewas appointed the Lucasian Chairof Mathematicsat Cambridge(once held by IsaacNewton). Atthat time he worked inoptics and drew a great deal of attention to the problem of astigmatism, a vision deficiency from which he suffered.

In 1828 he was named the Plumian Professor of Astronomy and Director of the Cambridge Observatory, He became the Astronomer Royal in 1835, a position he held for 46 years. During that time, he and the observatory staff reduced all measurementsmade by the observatory between1750and 1830.

His research (over 377 papers) encompassed magnetism, tides, geography, gravitation,partialdifferential equations,and sound. In1867 his paper on suspension bridges received the Telford Medal of the Institutionof CivilEngineers.

HisNumerical Theory of Tides was published in 1886 despite the presence of severalinexplicable errors. He attempted (unsuccessfully) to resolvethese until 1888.He died in 1892.

78



---PAGE-95---



Sec.4.2 Water Particle Kinematics for Progressive Waves 79

###### 4.1 INTRODUCTION

The solutions developed in Chapter 3 for standing and progressive smallamplitude water waves provide the basis for applications to numerous problems of engineering interest. For example, the water particle kinematics and the pressure field within the waves are directly related to the calculation of forces on bodies. The transformation of waves as they propagate toward shore is also important, as in many cases coastal engineeringdesign involves the forecasting of offshore wave climates or the use of offshore data, for example, those obtained from ships. It is obviously necessary to be able to determine any modifications that occur to these waves as they encounter shallower water and approach the shore.

###### 4.2 WATER PARTICLE KINEMATICS FOR PROGRESSIVE WAVES

Consider a progressive wave with water surface displacement given by

The associatedvelocity potential is

By introducing the dispersion relationship, d =gk tanh kh, this can be written as

4.2.1 Particle Velocity Components

The horizontal velocity under the wave is given by definition, Eq. (2.68),as

- (4.3a)
- (4.3b)


or



---PAGE-96---



80 EngineeringWave Properties Chap. 4

The local horizontal accelerationis then

du H cosh k(h +z)

-=- sin (kx-at) at 2 sinh kh

- (4.4)
- (4.5)


and the vertical velocity and local acceleration are

w =- ---a4_ -H asinh k(h+z) sin(kx-at)

dz 2 sinh kh dw H sinh k(h+z) at 2 sinh kh _---- cos (kx- at)

Examining the horizontal and vertical velocity components as a function of position, it is clearthat they are 90"out of phase; the extreme valuesof the horizontal velocity appear at the phase positions (kx-at)=0, n,. . . (under the crest and trough positions), while the extreme vertical velocities appear at 7r/2,3n/2,...(where the water surface displacement is zero).

The vertical variation of the velocity components is best viewed by

starting at the bottom wherek(h +z)=0.Here the hyperbolicterms involv-

ingz in both the u and w velocitiesare at their minima, 1 and 0,respectively. As we progress upward in the fluid, the magnitudes of the velocity components increase. In Figure 4.1,the velocity components are plotted for four phase positions. The accelerations are such that the maximum vertical accelerations occur as the horizontal velocities are extremes and the same is true for the vertical velocitiesand the horizontal accelerations.

4.2.2 Particle Displacements

A water particle with a mean position of, say,(xi,zI)will be displaced by the wave-induced pressures and the instantaneous water particle position

willbedenotedas(xl+c,zI+5),asshowninFigure4.2.Thedisplacement components (C,5) of the water particle can be found by integrating the velocity with respect to time.

Inkeepingwith our small-amplitude wave considerations, Cand willbe smallquantitiesandthereforewe canreplaceu(xI+C,z1+r>withU(XI,ZI).'

au

###### 'This involves neglecting terms such as - ,T, as can be seen from a Taylor series expansion.

ax



---PAGE-97---



Sec. 4.2 Water Particle Kinematics for ProgressiveWaves 81

z

###### t

###### Direction of progressive wave propagation

X

Figure 4.1 Water particlevelocities in a progressivewave.

Integratingthe equations above then yields

###### c=---H gk cashk(h+z I ) sin(kxl-at)

(4.9)

2 OZ cosh kh

or

###### c=--H cashk(h+21)

sin (kxl- at)

2 sinh kh

using the dispersion relationship. The vertical displacement is determined similarly:

H sinh k(h +21) 2 sinh kh

cos (kx1-at)

<=- (4.10)

Figure 4.2 Elliptical form ofwater particletrajectory.



---PAGE-98---



82 EngineeringWave Properties

Chap. 4

The displacementsI;and can be rewritten as

###### C(xl,zI,t) = -A sin (kxl- at) {(XI, 21,t )= B cos(kx1-at)

- (4.11)
- (4.12)
- (4.13)


Squaring and adding yields the water particle trajectory as

which is the equation of an ellipse with semiaxesA and B in the x-z direction, respectively (Figure 4.2).We should note also that A is always greater than or equal to B. In fact, at the locations of the mean water level, the water particles with mean elevation z = 0, follow a closed trajectory with vertical displacement H/2; that is, these particles comprise the surface. There are no water particles with mean locations higher than z = 0.

Inshallow wuter (h/L < 1/20),using the shallow water approximations, the major semiaxis reduces to

###### H cash k(h +z I ) H 1

###### A =- - HL - H T g (4.14)

2 sinh kh 2 kh 4nh 4n

wherethe equality for shallowwater,L =CT= &T,hasbeenintroduced.

The minor semiaxisB can be determined similarly.

B=-Hsinhk(h+zI)="(1):+

(4.15)

###### 2 sinh kh 2

Note thatA is not a function of elevation.Thehorizontal excursionof a water particle is a constant distance for all particles under the wave. The total vertical excursion increases linearly with elevation, being zero, of course, at the bottom and beingH at the mean water surface,z = 0.

For deep water waves (h/L3 t) it can be shown that the semiaxes simpIifLto

(4.16)

###### B =!!ekz!=A (4.17)

2

The trajectoriesarecircleswhich decayexponentially with depth. For a depth of z = -L/2, the values of A and B have been reduced by the amount e-",or the radii of the circlesare only4% of the surface values,essentially negligible. Figure 4.3 displays the shapes of the water particle trajectories for different relative depths.



---PAGE-99---



-

Sec. 4.3 Pressure Field Under a Progressive Wave 83

###### 0

0

0

kh <

kh >x

10

(-h <--)l

(--20I <-hL <-)l2

h 1

(-L >-)2

L 20

Figure 4.3 Water particle trajectories in progressive water waves of different relativedepths.

###### 4.3 PRESSURE FIELD UNDER A PROGRESSIVEWAVE

The pressure field associated with a progressive wave isdetermined from the unsteady Bernoulli equation developed for an ideal fluid and the velocity potential appropriate to this case, Eq. (2.92):

a+

i! +gz +t (2.42 +w2)--=C(t) (4.18)

P at

Equating the relationship above at any depth z, and at the free surface q, where the pressure is taken as zero, and linearizingyields

- (4.19)
- (4.20)
- (4.21)


Recallingfrom Chapter 3that the linearized DFSBC reduces to

###### q = - -

it is seen that the pressure can be expressed as

L - g z + -a+

P at

where the small velocity squared terms have been neglected. we have

For a progressive wave described by the velocity potential in Eq. (4.1),

- (4.22)

or

- (4.23)




---PAGE-100---



84

EngineeringWave Properties Chap. 4

where

cosh k(h +z) cosh kh

K A 4 = (4.24)

The first term on the right-hand side of the pressure equation (4.23) is, of course, the hydrostatic term, which would exist without the presence of the waves. The second term is called the dynamic pressure. The term K,(z) is referred to as the “pressure response factor” and below the mean water surface is always less than unity.

The dynamicpressure isa result oftwo contributions; the first and most obvious contributor is the surcharge of pressure due to the presence of the free surface displacement. If the pressure response factor were unity, the pressure contribution from the free surface displacement would be purely hydrostatic. However, associated with the wave motion is the vertical acceleration, which is 180”out of phase with the free surface displacement. This contribution modifies the pressure from the purely hydrostatic case. The reader may wish to verify that Eq. (4.22)can be obtained by integrating the linearized verticalequation of motion, Eq. (2.38c),from any depth z up to the free surface q.In Figure 4.4, the effect of the dynamic pressure in modifying the hydrostatic pressure is shown.

The pressure response factor has a maximum of unity at t= 0, and a minimum of l/cosh kh at the bottom. To determine the pressure above the mean water level we again must use the Taylor series for a small positive distancezI(0< z1< q):

(4.25)

to the first order

=pgq -pgzl

=Pg(q - 21) (4.26) Thus to this approximation the pressure is hydrostatic under the wave crest

z

___I)

X

Figure 4.4 Hydrostatic and dynamic pressure components at various phase positions in a progressivewater wave.



---PAGE-101---



Sec. 4.3 Pressure Field Under a Progressive Wave 85

down to z = 0. Below that depth, however, it deviates from the hydrostatic law. Note also that Eq. (4.26)predicts a zero pressure at the instantaneous free surface, zI= q. Figure 4.5 shows the isolines of pressure under a wave for

###### h/L =0.2.

One method of measuring waves in either the laboratory or field is by sensing the pressure fluctuations and then calculating the associated water surface displacements by Eq. (4.23). From Eq. (4.23), a bottom-mounted pressure gage would record a steady hydrostatic pressure plus the oscillating dynamic pressure, which for a particular wave period is proportional to the free surface displacement q, the variable of interest. If the dynamic pressure

- p Dis isolated by subtracting out the mean hydrostatic pressure, then q is


1

###### v =

P D

and Kp(-h) =~

(4.27)

PgKA-h) cosh kh

where Kp(-h) is a function of the angular frequency of the waves. Thus the dispersion relationship must be used to determine kh from the frequency of the observed waves. If a mean current is present, the wave number must be computed via Eq. (3.52);otherwise, significant errors can occur.

Even though we have derived the pressure response factor for only one frequency component, it is interesting to note that for cases in which the linear assumption is reasonably valid, Eq. (4.27)can be used to determine the composite wave system containing many (or an infinite) number of components from a measured pressure time series.

Because of the dependency of the pressure response factor on the wave frequency,short-period waves have a very small Kp(at the bottom), while for long-period waves Kpapproaches unity. In other words, very short period waves may not even be recorded by the pressure gage.The reader may wish to

###### .c

###### Z

###### t

Figure 4.5 Isolines ofpD/[y(H/2)]for progressive wave of h/L =0.20.



---PAGE-102---



86 EngineeringWave Properties Chap. 4

show that the shallow and deep water asymptotes for the pressure response factor are unity and ekz,respectively.

###### 4.4 WATER PARTICLE KINEMATICS FOR STANDING WAVES

The originalvelocity potential we derived represented a pure standing wave,

- (4.28)
- (4.29)
- (4.30)


with

###### HS

cos kx cos at d=gk tanh kh

?I=-2

where H, denotes the height of the standing wave and is twice the height of each of the two progressive waves forming the standing wave.

The velocity potential for a standing wave can be rederivedby subtracting the velocity potential for two progressive waves of the same period with heightsHppropagating in opposite directions.

###### 4 =-HpE ‘0s’ k(h +Z ) sin (k-at)

2 a cosh kh

(4.31) Sin (kxk at)can be rewritten as sin kx cos at f cos kx sin at, (from

trigonometry) and thus the velocity potential is rewritten as

(4.32)

Comparing the two velocity potentials, it is clearthatHp=HJ2.Therefore,a standing wave of height H,iscomposed of two progressive waves propagating in opposite directions, each with height equal to one-half that of the standingwave.

4.4.1 Velocity Components

The velocities under a standing wave are readily found to be

(4.33)



---PAGE-103---



Sec.4.4 Water Particle Kinematics for Standing Waves 87

where for convenience the subscripts has been dropped. Usingthe dispersion relationship,

u = - aH cash k(h +z)sin h sin at w = - -Ha sinh k(h +z)cos h sin at

- (4.35a)
- (4.35b)


2 sinh kh

2 sinh kh

As with the velocities under a progressive wave, these velocities increase with elevation above the bottom. The extreme values of u and w in space occur under the nodes and antinodes of the water surface profile as shown in Figure 4.6,where u and w are zero under the antinodes and nodes, respectively. It is of interest that the horizontal and vertical components of velocity under a standing wave are in phase; that is, the time-varying term “sin at”modifies both velocity components and, at certain times, the velocity iszero everywhere in the standingwave system.It is therefore evident that at some times all the energy is potential and, by reference to Eqs. (4.33, at other times all the energy is kinetic.

If a progressivewave were normally incident on a verticalwall, it would be reflected backward without a changein height, thusgivinga standingwave in front of the wall. The lateral boundary condition at the vertical wall would be oneof no flowthrough the wall, oru =-a+/& =0atx =xWall,wherexwallis the Iocation of the wall. Inspectionofthe equation forthe horizontalvelocity, Eq.(4.33),showsthat atlocationskx = na(wheren isan integer),the no-flow boundary condition is satisfied. Therefore, a standing wave could exist within a basin with two walls situated at two antinodes of a standing wave. This is, in fact, the simplest model of uniform depth lakes, estuaries, and harbors where standing waves, called seiches, can be generated by winds, earthquakes, or other Dhenomena. We examine these Chapter 5.

waves further in

The local accelerations under a standing wave are au H cosh k(h +z) at - 2 sinh kh

sin kx cos at

###### (4.36)

Antinode

Figure4.6 Distribution ofwater particle velocities in a standing water wave.



---PAGE-104---



dw H sinh k(h +z) dt 2 sinh kh

cos kx cos at

-=-- (9 (4.37)

Under the wave antinodes, the vertical accelerations are maxima, while the horizontal accelerations are zero, and under the nodes, the opposite is true.

4.4.2 Particle Displacements

The displacements of awaterparticle (c, 5) from its meanposition

(XI, ZI) under a standing wave are defined in a linearized fashion as before. c= J u ( x ~+[,Z I +5)dt m JU(X~21), dt (4.38) <=Jw(x~+c,Z I +5>dt G Jw(xI, z I ) dt (4.39)

###### or

###### c=--Hcash k(h +z ! ) .

sin kxl cos at =-A cos at

(4.40)

2 sinh kh sinh k(h + 'I) cos kxl cos at =B cos at (4.41)

'=, sinhkh

The displacement vector isr =Q+&;its magnitude IrI is

Irl = J X T i P cos ut (4.42)

or

H cos at 2 sinh kh

cosh2k(h +zI)sin'kxl +sinh2k(h +zl) cos2kx1(4.43)

IrWl. - = J

For infinitesimally small motions, the displacement vector is a straight line,' the amplitude and inclination being dependent on position (xI,zl). The water particle under the standing wave moves back and forth along the line with time. Substituting the trigonometric identities,

Cosh2k(h +z,) = [cash 2k(h +zI) + 11 sin2kxl=t (1-cos2kxl) sinh2k(h+zI)=$ [cosh 2k(h +zI)- 11 COS' kxl= i(1 +cos2 k ~ l ) yields from Eq. (4.43),

###### 'From Equations (4.40) and (4.41), we obtain 6 = -(B/A)l which may be compared with Eq. (4.13), the equation for the trajectories of a progressive wave.



---PAGE-105---



Sec. 4.5 Pressure FieldUndera StandingWave 89

Note that at the bottom under the antinodes IrIis zero.The maximum value of (r1 occurs under the nodes, where cos 2kxl = -1.

The motion of the water particles under a standing wave can thus be described as a simpleharmonic motion alonga straight line.The slopeof the displacement vector 6' is given by

(4.44)

which is not a function of time. Clearly, at the bottom, the trajectories are horizontal (6' =0), as is to be expected by the bottom boundary condition. Figure 4.6 portrays the water particle trajectories at several phase positions under a standing wave.

###### 4.5 PRESSURE FIELD UNDER A STANDING WAVE

To find the pressure at any depth under a standing wave, the unsteady Bernoulli equation is used as in the case for progressive waves.

###### p u 2 + w 2

-+--- a4+ PZ=C(t) (4.45)

P 2 at

0-

Linearizing and evaluating as before between depth (z )in the fluid, the gage pressure is

the free surface and at some

###### a4

p = -pgz + p -

at

or

###### H

where the pressure response factor Kp (z)is the same as determined for progressive waves. Note that under the nodes, the pressure is solely hydrostatic. Again, the dynamic pressure is in phase with the water surface elevation, and as before it is a combined result of the local water surface displacement and the vertical accelerations of the overlying water particles.

The force exerted on a wall at an antinode can be calculated by integrating the pressure over depth per unit width ofwall

from Eqs. (4.26) and (4.46) and where qw= (H/2)cos at, the water surface



---PAGE-106---



displacement at the wall. It should be stressed that this formulation is not entirely consistent, as the second integral on the right-hand side representing the forcecontribution ofthe wave crest region is of second order;yet secondorder terms in the form of the square of the velocity components have already been dropped from the first tern of the right-hand side. Integrating, we get

- (4.47)
- (4.48)


To first order,

F=p-++gh----sh2

tanh kh

###### 2 kh

UlW

The force on the wall consists of the hydrostatic contribution, plus an oscillatory term due to the dynamic pressure. The maximum force occurs when qW=H/2,

###### (4h2+(H)2)

+ pgh H--tanh kh

###### Fmax=pg (4.49)

8 2 kh

###### 4.6 PARTIAL STANDING WAVES

For the case just consideredof pure standing waves, two waves of the same period and height, but propagating in opposite directions, were superimposed, as one expects from the perfect reflection of an incident wave from a vertical wall. Quite often in nature, however, when waves are reflected from obstacles, not all of the wave energy is reflected; some is absorbed by the obstacle and some is transmitted past the obstacle. For example, waves are reflected from breakwaters and beaches; in each case wave energy is not perfectlyreflected.Toexamine this case, let us assume that the incident wave has a height Hi, but that the reflected wave has a smaller height H , and different phase than the incident wave.The wave periods of the incident and reflected waves will be the same. The total wave profile seaward of the obstacle is then

###### H

qr =!5 cos(kx-o*)+-1:cos(kx4- ot+E ) (4.50a)

2 2

whereEisthe phase lag inducedby the reflection process. If the water surface displacementsare plotted, they appear as in Figure4.7.Due to the imperfect reflection,there are no true nodes in the wave profile.

Quite often in measuringwave heights in a wave tank, reflections occur and it is necessary to be able to separate out the incident and reflected wave



---PAGE-107---



Sec.4.6 PartialStanding Waves 91

heights.To do this, we rewrite q,,using trigonometric identities.

- q, = -H , (cos kx cos at +sin kx sin at) 2


+z(cos ( k+~€1cosat -sin ( k+~€1sin at)

###### 2

Grouping similar time terms,

1

###### H

cos kx +-2 cos(kx+E ) cosat

2

###### H . I

sin kx -2sin (kx+E) sin ot or,for convenience, denoting the bracketed terms by Z(x) and F(x),

2

###### ql =Z(x)cosat +F(x)sin at (4.50b)

Thus ql isa sum of standing waves.To find the extreme values of qrfor any x, that is, the envelope of the wave heights, denoted by the dotted lines in the figure, it is necessary to find the maximas and minimas of ql with respect to time. Proceeding as usual by taking the first derivative and setting it equal to zero to find the extremes yields

--"r --~(x)asin at +~(x)acos at =o (4.51)

at

or

Upper envelope

,ar = 0" /

'Lower envelope

###### Figure 4.7 Instantaneous water surface displacements and envelope in a partial standing wave system.



---PAGE-108---



EI ( x ) F(x),andI(x).

###### 92 EngineeringWave Properties Chap. 4

ftw'

F(x)

(Ut)," Figure 4.8 Relationships among (at),,

Therefore, to find the maxima and minima of ql,( ~ tis)substituted~ into Eq. (4.50a). Examining Figure 4.8, it is clear that

###### F(x) JZ"x) +P ( X )

###### sin ( ~ t= ) ~

Substituting into Equation (4.50b),3 we have

(4.52)

Substituting for Z(x) and F(x) from Eq. (4.50b), it is seen readily that the extreme values of ql for any location x are

[ q t ( x ) ] m = -f(Hi>'- +(".)*- +- cos(2kx+E) (4.53)

2 2 2 [qI(x)lmobviously varies periodically with x. At the phase positions (2kxl+E) =2nn (n =0,1,...),[qI(x)lmbecomes a maximum of the envelope

(ql)max =;(Hi +Hr), the quasi-antinodes (4.54)

whereas at the phase positions, (2kx2+E ) =(2n+ 1)n(n=0,1,. ..),the value of [ql(x)lmbecomes a minimum ofthe envelope:

(ql)min =i(H,-Hr), the quasi-nodes (4.55)

The distance between the quasi-antinode and node can be found by subtracting the phases

(2kx2+E) -(2kxl+E) =(2n + 1)n-2nn

or

###### 2k(x2 -XI) = n

L

###### x2-xI =-4

'This exercise shows simply that the maximum and minimum of (A sin at + B cos at) are

k J A V .



---PAGE-109---



Sec. 4.7 Energy And Energy Propagation in ProgressiveWaves 93

For a laboratory experiment, where reflection from a beach or an obstacle is present, if the amplitude of the quasi-antinodes and nodes are measured by slowly moving a wave gage along the wave tank, the incident and reflected wave heights are found simply from Eqs. (4.54)and (4.55)as

Hi = (Vr)rnax + (VOrnin (4.56) Hr =(Vtlrnax -(VOrnin (4.57)

The reflection coefficient of the obstacle is defined as

H ,

###### Kr = - (4.58)

###### Hi

Figure 4.9presents such data for the caseof extremely small waves and nearly perfect reflection.To find the phaseE , it is necessary to find the distance from origin to the nearest maximum or minimum xI,and to solve one of the following equations:

2nn, n =o, 1,2)... for the maximum (2n + l)n, n =0, 1, 2,.. . for the minimum

###### 2kX1+€=

The reader should verify that the dynamic and hydrostatic pressure under a partial standing wave system can be expressed as

P(X,=, 0 =-Pgz +pgK,(z)Zl

where ~(x,t )and Kp(z)are given by Eqs. (4.50a) and (4.24),respectively.

###### 4.7 ENERGY AND ENERGY PROPAGATION IN PROGRESSIVEWAVES

The total energy contained in a wave consists of two kinds: the potential energy, resulting from the displacement of the free surface and the kinetic energy, due to the fact that the water particles throughout the fluid are moving. This total energy and its transmission are of importance in determining how waves change in propagating toward shore, the power required to generate waves, and the available power for wave energy extraction devices, for example.

P1 + 92.x <0

Positionof wave gage for x <0 x = -6‘ -7’ -8’ -9’ -10’ -1 1’ -12’

Figure 4.9 Water surface displacement as measured from a slowly moving carriage for the caseofnearly perfect reflection. (From Dean and Ursell,1959.)



---PAGE-110---



94 EngineeringWave Properties Chap. 4

4.7.1 PotentialEnergy

Potential energy as it occurs in water waves is the result of displacinga mass from a position of equilibrium againsta gravitational field.When water is at rest with a uniform free surface elevation, it can be shown readily that the potential energy is a minimum. However, a displacement of an assemblage of particles resultingin the displacement of the free surfacewill require that work be done on the systemand results in an increase in potential energy.

We will derive the potential energyassociatedwith a sinusoidalwave by two different methods. First consider the wave shown in Figure 4.10;we will determine the average potential energy per unit surface area associatedwith the wave asthe differencebetween the potential energy with and without the wave present.The potential energy of a small column of fluidshown in Figure 4.10with mass dm relative to the bottom is

d(PE)= dmgZ (4.59) in whichz is the height to the center of gravityof the mass, and can be written

as

-z=- h + q

(4.60)

2

and the differential mass per unit width is

###### dm =p (h+q)dx

The potential energy averagedover onewave length fora progressive waveof heightH is then

=@Sr+L['(h2+2qh+$)I dx

(4.62)

L x 2

Figure4.10 Definition sketchfordeterminationofpotentialenergy.



---PAGE-111---





---PAGE-112---



96 EngineeringWave Properties Chap. 4

water formerly in the trough to the crest location through a vertical distance 2.zcg,where zcgis shown in Figure4.11.Note that this area isH L / ~ Rand the vertical distance from the mean waterline to the centers of gravity is lrH/16.

4.7.2 Kinetic Energy

The kinetic energy is due to the moving water particles; the kinetic energy associated with a small parcel of fluid with mass dm is

###### d(KE)=dm u2+w2-- p d x u2d +z w2y (4.70)

###### L L

To find the average kinetic energy per unit surface area, d(KE)must be integrated over depth and averaged over a wave length.

(4.71)

From the known solution for the velocities under a progressive wave, Eqs. (4.3a) and (4.5),the integral can be written as

+sinh’ k(h +z)sin2(kx-at)]dz dx

Using trigonometric identities Cjust as was done for the trajectories under a

Figure4.11 Potential energy determined as the result of raising water mass in trough area to crest area.



---PAGE-113---



Sec.4.7 EnergyAnd Energy Propagationin Progressive Waves 97

standing wave), this can be recast as

J-;=o ;

(4.73)

-[cash2k(h +Z ) +cos 2(kx -at)]dz dx

Carryingout the integration and simplifyingyields

###### KE= pgH2 (4.74)

This is equal to the magnitude of the potential energy, which is characteristic of conservative (nondissipative) systems in general.Thetotal averageenergy per unit surface area of the wave is then the sum of the potential and kinetic energy. Denoting E as the total average energy per unit surface area

E =-KE +-PE =$pgH2 (4.75) The total energy per wave per unit width is then simply

###### EL=ApgH2L (4.76)

It is worthwhile emphasizing that neither the average (over a wave length) potential nor kinetic energy per unit area depends on water depth or wave length, but each is simply proportional to the squareofthe wave height.

4.7.3 Energy Flux

Small-amplitude water waves do not transmit mass as they propagate acrossa fluid, as the trajectories of the water particles are c10sed.~However, water waves do transmit energy. For example, consider the waves generated by a stone impacting on an initially quiescent water surface.A portion of the kinetic energy of the stone is transformed into wave energy.As these waves travel to and perhaps break on the shoreline, it is clear that there has been a transferof energy away from the generation area.Therate at which the energy is transferred is called the energyJlux3,and for linear theory it is the rate at which work is being done by the fluid on one side of a vertical section on the fluid on the other side. For the vertical sectionAA’,shown in Figure 4.10, the instantaneous rate at which work is being done by the dynamic pressure IpD=(p+pgz)]per unit width in the direction of wave propagation is

###### (4.77)

4Forfinite-amplitude waves, thereis a mass flux;see Chapter 10.



---PAGE-114---



98 Engineering Wave Properties Chap. 4

Theaverageenergy flux is obtained asbeforeby averaging over a wave period (4.78)

from Eqs. (4.22)and (4.3b) forp and u,or

using the dispersion relationship. to integrate up to the mean free surface.

To retain terms to the second order in wave height, it is only necessary

(4.80)

- pgo H 2(2kh+sinh2kh) 3=-(-) sinh 2kh

4k 2

-

3 =ECn (4.81)

where Cn is the speed at which the energy is transmitted; this velocity is called the group velocity C,, for reasons to be explained shortly.

C, = nC (4.82a) or

(4.82b)

The factor n has as deep and shallow water asymptotes the values of and 1, respectively. Therefore, in deep water, the energy is transmitted at only half the speed of the wave profile, and in shallow water, the profile and energy travel at the same speed.

Originof the term "group velocity." We have just derived the group velocity in terms of the rate at which energy is being transferred by a train of propagating waves.A more descriptive explanation of the term group velocity results from examining the propagation of a group of waves.

If there are two trains of waves of the same height propagating in the same direction with slightly different frequencies and wave numbers, they



---PAGE-115---



Sec. 4.7 Energy And Energy Propagation in Progressive Waves 99

Figure 4.12 Characteristicsofa “group” of waves.

are superimposed as

- (4.83)
- (4.84)
- (4.85)


q = q l + q 2

H H

-cos(k,x-all)+-cos(k2X -ad) where’

= 2 2

###### Aa Ak 2 2

4=o+-, k2 =k +-

Using trigonometric identities, the profiles can be combined in the following manner:

###### +k2)x-(at+a2)t]]cos[i [ (k,-k2)x-(al-a$]1

=Hcos(kx-at)cos[:-Ak(x--::t11 (4.86)

The resulting profile, consisting of wave forms moving with velocity C = a/k,is modulated by an “envelope” that propagates with speed Aa/Ak, which is referred to as the group velocity C,. The superimposed profile is shown in Figure 4.12. If we recall that the wave energy is proportional to the wave height, it isclear that no energy can propagate past a node as the wave height (and therefore dynamic pressure) is zero there. Therefore, the energy must travel with the speed of the group of waves. This velocity is seen to be, from Eq. (4.86),

Aa

###### C,=- (4.87)

Ak

’This derivationis strictly true for small Ak and Aa, in order that the relationships givenin Eq. (4.85)satisfy the dispersionrelation.



---PAGE-116---



100 EngineeringWave Properties Chap. 4

InthelimitasAk-.0,we obtainagroupvelocityforawavegroupofinfinite length L, (hence, a wave train of constant height), C, =da/dk. This derivative can be evaluated from the dispersion relationship

?C =gk tanh kh (4.88)

###### do

20-=g tanh kh +gkh sech' kh

dk

da (gtanh kh +gkh sech' kh)a g-dk 2 gk tanh kh

c --=

###### ="(2 1+

- (4.89)
- (4.90)


sinh 2kh

Therefore, C, =nC,where again

4.8 TRANSFORMATION OF WAVES ENTERING SHALLOW

WATER

Several changes occur as a train of waves propagates into shallow water. One of the most obviousis the change in height asthe wave shoals. If energy losses (or additions) are negligible, from observation, it is evident that the waves near the point of breaking at a beach are somewhat higher than those farther offshore. Other changes, such as the previously discussed decrease in wave length with shallower depths and the changes in wave direction (Figure4.13), are not readily apparent from the beach, but often are clearly observable from the air.

4.8.1 The Conservation of Waves Equation

In all previous derivations it has been assumed that the waves are propagating in the x direction; yet if we are discussing a coastline, it is often convenient to locate the coordinate system such that the x direction is in the onshore direction and the y direction is in the longshore direction. It is rare that waves propagate solely in the x direction once the coordinate system is prescribed.

In general, a wave crest corresponds to a line of constant wave phase. For example, if a wave train is represented as q =H/2 cos R, where R corresponds to the scalar phase function [recall that forwaves propagating in the x direction, R =(kx-at)].Therefore, crests occur for R =2nn, where n is defined here as an integer. From vector analysis, the normal unit vector n



---PAGE-117---



Sec. 4.8 Transformationof Waves Entering Shallow Water 101

Figure 4.13 Refraction of waves around a small Caribbean island. (Photo courtesy of the L.S.U.Coastal Studies Institute.)

to a scalar function is related to the normal vector N,which is found by taking the gradient ofthe function, Eq. (2.55),

N=VQ (4.91) where

N = nlVQ1 (4.92)

and where, for purposes here, the gradient operator is only the horizontal operator

(4.93)

as R is not a function of elevation z.The vector N points in the direction of the greatest change of Q, which is the wave propagation direction.6

We will define the wave number k as

(4.94)

###### 6 V=~(H/2)sin vVv;thus Vq isin the same direction asVy.Vqisthe wave direction.



---PAGE-118---



102 EngineeringWave Properties Chap.4

Figure 4.14 Resolution of wave

~ number k into orthogonal components.

Note that for waves in the x direction that

k =ki +Oj (4.95a) and

lkl = k (4.95b)

wherek is the previously defined wave number. It becomes clearnow that the wave number vector is nothing more than the wave number oriented in the wave direction. For waves propagating in an arbitrary direction in x-y space, we have

k =k,i +kyj (4.96)

and

Ikl =k = -4 (4.97)

If an angle of incidence 8 is defined as the angle made between the beach normal (thex direction) and the wave direction, then

k, = ]klcos 8 k, = Ikl sin 6 (4.98)

The phase function’ is, therefore, Q(x,y , t) = kx cos 8 + ky sin 8 - ot = k.x-ot.Iftheangleofincidenceiszero,itisobviousthatQrevertsbackto the simple form [Eq. (4.95a)l.

The horizontal line along which waves travel is called a wave ray. It is defined (in a manner similar to a streamline) as a line along which the wave number vector is always tangent. As energy travels in the direction of the

7Thisf ormofthe phasefunctioncanbeobtained in an alternativemanner.Forwaves oflengthL propagating at an angleto thex axis, the projectionof the waveon thex axis has a wave lengthof L,. From geometry,L, =L/cos 0 and thereforek,x =(2n/L,)x= k cos Ox.The y contribution followssimilarly.



---PAGE-119---



Sec. 4.8 Transformationof Waves Entering Shallow Water 103

wave, the wave energy associated with the wave travels along the wave ray also.

The angle made by the wave ray to the x axis can be obtained in the same manner as the local wave direction [see Figure 4.141:

8=tan-' -kY k,

The wave frequency can be determined from the phase function as

aa

a=--

- (4.99)
- (4.100)
- (4.101)


at

It is readily seen that the following expression is identically zero:

###### +VQ)a +v(-$)=0

at

which using Eqs. (4.94)and (4.99)can be written as

dk

- + V a = O

at

This equation states that any temporal variation in the wave number vector must be balanced by spatial changes in the wave angular frequency. If the wave field is constant in time, then V a = 0, or-the wave period does not change with space. It is constant even as the water depth changes. If the waves encounter a steady current, it was shown in Chapter 3 that a=k . U + d m ,where U =mean current vector. Even for this casea+Ax,y), that is, only changes in k occur to compensate for the variable current.

To examine the conservation of waves relationship further, it is best to rederive it in a more intuitive manner. For a small length dx in the direction of wave travel, shown in Figure 4.15,we will relate the number of waves entering and leaving the block of fluid to the accumulation of waves within it. The rate at which waves enter the column is 1/Tor 0/2n.The rate at which waves are leaving the column a distance dx away is found by using the firstorderTaylor series.Thedifferencein inflow andefflux ofwaves must be equal

Figure4.15 Considerationofconservation ofwaves.



---PAGE-120---



104 EngineeringWave Properties Chap. 4

to the accumulation of waves within the region with time, that is, the time rate of change of the number N of waves within the column,

- (4.102)
- (4.103)


Equating, we have

###### b - ( ? + - ! - a b d x ) = +--dx ak 2R 2~ 2nax 2~ at

or

###### ak ao at ax

-+-=o

which agrees with Eq. (4.101) when applied in the direction of the waves.

4.8.2 Refraction

Referringback to Eq. (4.94), the wave number vectoristhe gradient of a

scalar.If we take the curl of k, we find that

V x k = O (4.104) by the identitythat the curl of agradient is zero.This irrotationality condition

onkindicatesthatthelineintegralJk-dlisindependentofpath(Chapter2). Rewritingtheintegral,we haveJVQ .dl =JdQ.Therefore,theirrotationality impliesthat Q(x, y, t) is uniquely determined at each point (for fixed t).

Substituting the components of k yields

###### d(k sin 6)-d(kcos 6)

= o (4.105)

###### ax dY

For a shoreline where the alongshore variations in the y direction of all variables are zero, that is, there are straight and parallel offshore contours, this equation reduces to

d(k sin 6)

(4.106) or

= O

dx

k sin 6= constant (4.107) Therefore, the longshoreprojection of the wave number is a constant.

Dividingby (Tin the steady-statecase,

--sin 6-constant

C (4.108)



---PAGE-121---



Sec. 4.8 Transformation of Waves Entering Shallow Water 105

The constant is most readily evaluated in deep water, yielding Snell's law:

##### 1 c=c,sin8 sin8, 1

(4.109)

This equation, originally found in geometric optics, relates the change in direction of a wave to the change in wave celerity.Yet from before we know that waves slow down in shallower water; therefore, Snell's law indicatesthat for coastlines with straight and parallel contours, the wave direction 8 decreases as the wave shoals, tending to make the waves approach shore normally.

In general, however, offshore contours are irregular and vary along a coast, so that the full equation must be used.

a k sin 8 d k cos8

###### - = O

- (4.110)
- (4.111j


###### ax aY

or

a0 a0 ak ak k cos 8 - +k sin 8 - =cos 8- -sin 8-

ax JY dY ax

This first-order nonlinear partial differential equation for 8must be solved by computer techniques for a general coastline (see Noda et al.,1974)to give the wave directions for various locations and water depths.

Historically,ray-tracing techniques were developed to solve this equation followingthe path of the waves. We can transform Eq. (4.111) into one valid for a coordinate system (s,n) such that sis in the wave direction and n normal to it (see Figure 4.16), defined as

- x = s cos 8- n sin 8 (4.112a)
- y = s sin 8+n cos8


Using the chain rule the derivative operators in the sand n directions can be

11

Y

Figure4.16 Coordinate system(5, n) definedby directionof wave number vectork.

X



---PAGE-122---



106

EngineeringWave Properties Chap. 4

established,

a d x a dya (4.112b)

-=--as ds ax +--ds ay

###### a a

=cos8-+sin 8-

ax aY

and correspondingly,

a a a (4.112~)

-=-sin 8-+cos8-

an ax aY

It is clear that the equation governing the wave angle can be rewritten as

a8 1ak 1 ac

-=--=--- (4.113)

as k a n C a n

with k =a/C. This equation relates the curvature of the wave ray to the logarithmic derivative of the wave number normal to the wave direction.

Ray tracing is often done by hand calculation,* as well as by computer programs. The procedure involves using Snell’s law locally at each contour line of the offshore bathymetry that must be known. First a “smoothing” procedure is used to remove sharp changes of direction of the contour lines. The proper amount of smoothing is unfortunately a matter of judgment. Then the deep water wave period and angle of incidence must be known. Drawing the deep water wave crest on the bathymetry chart offshore of the (h/Lo= 0.5) contour provides the starting point for each of the rays, which are spaced at equal intervals. These intervals are chosen to give sufficient detail in the nearshore zone. For each of the contours representing a known depth, the wave celerity is determined. A ray is then drawn from the deep water crest location to the first intersection of a contour for which the wave feels bottom. At this point, a locally straight contour line is assumed and constructed by making a line segment tangent to the point of intersection. The normal to this line provides a means to calculate the angle of incidence with respect to the contour. Using Snell’s law [Eq.(4.109)],the angle to which the wave is refracted is computed. The ray is then extended to the next contour and the process repeated. This can be tedious and several aids have been constructed to aid in this process (see the Shore Protection Munuul).

4.8.3 Conservation of Energy

For conservation of energy, in a steady-state case, where there are not any energy losses or inputs, equationsaredevelopedreadily relating the wave

‘See,forexample, theShore Protection Manual (1977).



---PAGE-123---



Sec. 4.8 Transformation of Waves Entering Shallow Water 107

heights at two points of interes't, especiallyfor the case of straightand parallel bottom contours as in Figure 4.17. Recognizing that there is no energy flux acrossthe wave rays, the energy flux5across boisthe same as across bland bz.Due to the convergence or divergence of the wave rays, resulting from either refraction or actual physical boundaries, and due to changes in depth, the energy per unit area changes between bl and bz.Assuming no wave reflection, the conservation of energy, Eq. (4.81), requires

(EnC),bl= (EnC)zbz (4.114) or, using our definition forE as

E =QpgH2 (4.115) we can solve for the wave heightHz:

(4.116)

If it is recognized that waves do not change period with depth (ie., the wave period is a constant), then we have between deep and intermediate or shallow

Depth contours

###### Figure4.17 Characteristicsofwave raysduring refractionover idealized bathymetry.



---PAGE-124---



108

Engineering WaveProperties Chap. 4

depth water

(4.117)

###### =H o K K

where K, is the shoaling coefficient and K, the shoaling coefficient is plotted in Figure 3.9.

refraction coefficient.The

In-water with straight and parallel offshore contours, it is possible to determine the refraction coefficient, (b0/b2)”*,directly. In Figure 4.17 two rays are shown propagating to shore. Intuitively, since each wave refracts at the same rate alongthe beach, it should be expectedthat ray 2 is merely ray 1 displaced a constant distance loin the longshore direction.This is, in fact, the interpretation of the constancy of longshore wave number given by Snell’s law, kosin 8,=k sin 8.From the diagram it can be seen that bo=locos 8,and

Figure 4.18 Changes in wave direction and height due to refraction on slopes with straight, parallel depth contours. (From U.S. Army Coastal Engineering Research Center, 1977.)



---PAGE-125---



Sec.4.8 Transformationof Waves Entering Shallow Water 109

b2=locos 02.Therefore, the refraction coefficientK, is

K,=($ ) ' I 2 =(cos ">'I2 =( I -sin2e,,>"4 (4.118)

cos 82 1-sin' e2

which is always less than unity. The perpendicular spacing between the rays alwaysbecomes greater as the wave shoals. Figure 4.18 presents a convenient means to determine K, and wave directions from deep water characteristics. SinceK,depends on h/gT2and O0andK, depends only on h/gT2,it ispossible to present the product K,K, as a function of h/gT2and eo,as shown in Figure 4.19.

Example 4.1

A wave of 2 m height in deep water approaches shore with straight and parallel contours at a 30" angle and has a wave period of 15s. In water of 8 m, what is the direction ofthe wave, and what is its wave height?

Solution. Using Figure 4.18, h/gT2=0.0036 and therefore 6 2: 10.5"and K, = 0.94. The value of K,, using the C,/Co curve of Figure 3.9, is computed to be 1.2. H = 2(0.94)(1.2)= 2.26 m. This result can also be obtained directly from Figure 4.19 [i.e., K,K, = 1.13and H = 2(1.13)= 2.26 m].

In ray-tracing procedures, the separation distance b can be found analytically (Munk and Arthur, 1952). From Figure 4.20 it can be seen, for waves traveling with celerity C in the s direction, that the velocity components are-

Ccos 8, -=csin (4.119)

-ds =C, dx dY dt -dt = dt

+ i v m - sSeIweA43provide-' along the ray

path.

At A , d8 =(dO/dn)band, also db =dBds,which is the first-order change in arc length &e toXeZ$e incrmmt rf8.SubZE-rn8in these two

--equations yields

--=-1ab ae

?.. V=fq

-I

###### b -

or, definingp =b/bo,where bois an initial reference spacing of the wave ray, we obtain

I ap ae

--=- (4.120b)

pas an

This equation, which relates the change in spacing along the ray to the change in 8 in the normal direction, is similar in form to Eq. (4.113),which also involves 8.



---PAGE-126---





---PAGE-127---



Sec. 4.8 Transformationof Waves Entering Shallow Water 111

###### 4Y

Figure 4.20 Schematic diagram showing adjacent rays.

An ordinary differential equation can be obtained forp bycomputing

the mixed derivatives

###### a ae a ae

an as asan

Using the defnitions for the alan, d/as operators [Eqs. (4.112b) and (4.112c)], we obtain

an as asan

###### =-(->’+-(c21 ac 1 ap)2

###### an p2 as

after substituting from Eqs. (4.113) and (4.120b). Note that the right-hand side isnonzero;this is due to the fact that the derivative operators are functions of

8.

If we cross-differentiate Eqs. (4.113) and (4.120b)directly for the mixed derivative expressions, the following results:

again, a nonzero right-hand side. If we now equate the two right-hand sides, we have

a2p 1 d 2 c

+-7 p=0 (4.121a)

-as2 c a n

This equation can be used to obtainp;however, it involves knowledgeofthe wave fronts in order to determine derivatives in the n direction. If we



---PAGE-128---



112 EngineeringWave Properties Chap. 4

evaluate the second term, we have

azc aZc

- (sin2 eax2-2sin 8cos8- +cos28- ---

a2cay2 acae)as an

Canz C ax ay

but aO/an =(l/p) (ap/as) from Eq. (4.120b).

Therefore, finallyp is given by

g + p -+dP qp=o

(4.121b ) where

ds2 ds

- p(s)=--cosc8__dCdx -~sinc8-aCay

and

sin28a2c sin 8cos8 a2c cos28a2c

c ax2 c axay c ay2

- q(s)=---2 +--


Equations (4.121b) and (4.1 19) provide four ordinary differential equations which can be solved simultaneously to provide locations along the ray and the spacing between the rays over a given bathymetry for which C(x,y) is available (through the dispersion relationship). Numerous ray-tracing programs have been written (see, e.g., Wilson, 1966)and a recent example from Noda (1974) is presented in Figure 4.21.

Wave heights along a ray are related to P, as shown in the preceding section. Similarly to Eq. (4.117), we have

4.8.4 Waves Breakingin Shallow Water

The shoaling coefficient indicates that the wave height will approach infinity in very shallow water, which clearly is unrealistic. At some depth, a wave of given characteristics will become unstable and break, dissipating energy in the form of turbulence and work against bottom friction. When designing a structure which at times may be inside the surf zone it becomes necessary to be able to predict the location of the breaker line.

The means by which waves break depends on the nature of the bottom and the characteristics of the wave. See Figure 4.22. For very mildly sloping beaches,typically the waves are spilling breakers and numerous waves occur within the surf zone (defined as that region where the waves are breaking, extending from the dry beach to the seaward limit of the breaking). Plunging breakers occur on steeper beaches and are characterized by the crest of the



---PAGE-129---



###### Sec. 4.8 Transformationof Waves Entering Shallow Water 113

-101 I I I I I I I I I I

0 20 40 60 80 100 120 140 160 180 200

X (meters)

Figure 4.21 Ray lines for oblique wave incidence on a beach in the periodicrip channels.(From Noda, 1974.)

wave curlingoverforward and impingingonto part of the wave trough. These waves can be spectacular when air, trapped inside the “tube” formed by the wave crest, escapesby bursting through the back of the wave or by blowing out at a nonbreaking section of wave crest. Surging breakers occur on very steep beaches and are characterized by narrow or nonexistent surf zonesand high reflection. Galvin (1968)has identified coffupsingas a fourth classification, which is a combination of plunging and surging.

The earliest breaker criterion was that of McCowan (1894),who determined that waves break when their height becomes equal to a fraction of the water depth

Hb =Khb (4.122a)

where K = 0.78 and the subscript b denotes the value at breaking. Weggel (1972) reinterpreted many laboratory results, showing a dependency of breaker height onbeach slope m.His results were

(4.122b)



---PAGE-130---



###### SWI19

SmallFmThreeofbeaches.wavebreakingondenotedifferent4.22figurestypes

345

###### 21I6543n

###### ofstagestheofI.Svendsen.)brealringprocess.(FigurecourtesyA.

breakerPlunging

breakerSurging

breakerSpilling



---PAGE-131---



Sec. 4.8 Transformation of Waves EnteringShallow Water 115

where

- a(m)= 43.8(1.0 - e-'9m)
- b(rn)= 1.56(1.0+e-'g.Sm)-l


which approaches K =0.78 as the beach slope rn approaches zero.gSee Figure

*-+ 1

###### IL.1 .

As a first approximation, the depth of wave breaking can be determined by the shoaling and refraction formulas for straight and parallel contours if the offshore wave characteristics are known.

H=Ho(&)'I* (-)cos8,

- (4.123)
- (4.124)


cos 8 For shallow water, this is approximately equal to

if it is assumed that the breaking angle is small. Using McCowan's breaking criterion, we have

- (4.125)
- (4.126)


and solving for hb yields

or for a plane beach where h =rnx and rn =tan /?,the beach slope,the distance to the breaker line from shore is

- (4.127)
- (4.128)


Finally, the breaking wave height is estimated to be

Komar and Gaughan (1972), using the conservation ofwave energy flux in the manner of Munk (1949) for solitary waves, developed an equation similar to Eq. (4.128) for normally incident waves (8= 0").Dalrymple et al. (1977)included the deep water wave angle asdeveloped above. By comparing to a number of laboratory data sets, it appears that Eq. (4.128)underpredicts the breaking wave height by approximately 12% (with K = 0.8). See Figure

9Thea(m)parameter originally defined by Weggel was dimensional and required use of the English system ofunits. The parametersa(m)andb(m)presented here are dimensionless.



---PAGE-132---



###### 116 Engineering Wave Properties Chap. 4

_..

lo-’ 2 3 4 5 6 7 8 9 1 0 - 2 2 3 4 5 6 7 8 9 1 0 ’ 2 3 4 5 6 7 8 9 ~ 1 0 ”

Figure 4.23 Surf zone width xb and breaking wave height Hb versus deep water wave height Ho in dimensionless form and as a function of Oo, the deep water incident angleK =0.8.

4.23for a dimensionless representation of Eq. (4.128).Wave breaking, with its complexities of turbulence and wave nonlinearities, is still an area of active research. The reader who must deal with design in the surf zone is referred to the literature for the most accurate prediction of surf zone width, breaking wave height, and other surf zone parameters. As an example, see Svendsen and Buhr Hansen (1976).

###### 4.9 WAVE DIFFRACTION

Wave diffraction is the process by which energy spreads laterally perpendicular to the dominant direction of wave propagation. A simple illustration is presented in Figure 4.24,in which a wave propagates normal to a breakwater of finite length and diffraction occurs on the sheltered side of the breakwater such that a wave disturbance is transmitted into the “geometric shadow zone.” It is clear that a quantitative understanding of the effects of wave diffraction is relevant to the planning and evaluation of various harbor layouts, including the extent and location of various wave-absorbing features on the perimeter. Diffraction is also important in the case of wave propagation across long distances, in which classical wave refraction effects considered alone would indicate zones of wave convergences and extremely high concentrations of wave energy. As the energy tends to be concentrated



---PAGE-133---



Sec. 4.9 Wave Diffraction 117

Geometricilluminated +

Y

Geometric shadow zone

Diffracted wave

:Incidentwave

X

Figure 4.24 Diffraction of wave energy into geometric shadow zone behind a structure.

between a pair of converging wave orthogonals, some of this energy will “leak” across the rays toward regions of less wave energy density. Most present methodologies for computing wave energy distribution along a shoreline due to wave propagation across a shelf do not account for diffraction and may result in greatly exaggerateddistributions ofwaveenergy.In the followingsections, the main contributionscontained in the classicalpaper by Penney and Price (1952) which relate to diffraction around breakwater-like structures will be reviewed.

4.9.1 Diffraction Due to Wave-Structure

Interaction

The three-dimensional linearized boundary value problem formulation for this situation is similar to that presented before [Eqs. (3.19), (3.20), (3.29), and (3.30)] for two dimensions with the exception of the no-flow condition on the structure boundary and will not be presented here. Considering water of uniform depth, the vertical dependencyZ(z)satisfyingthe noflow bottom boundary condition is

Z(Z)=cash k(h + Z) (4.129) and the velocity potential is represented by

&x, Y ,z, 0 = Z(z)F(x,Y )eluf (4.130)

whereF(x,y )isacomplexfunctionandi=J-1.SubstitutingEq.(4.130)into

the Laplace equation yields the Helmholtz equation in F(x,y): a2F a2F

~ +__ +k2F(x,y )=0

(4.131)

ax2 ay2



---PAGE-134---



118 Engineering Wave Properties Chap.4

The kinematic and dynamic free surfaceboundary conditions yield the usual dispersion equation

###### c? =gk tanh kh

and an equation for the water surface displacement q given by

ia

q =-F(x,y) cosh kh eluf (4.132) The solutions to this equation will be examined for several important cases.

###### g

Normalwave incidenceon a semi4nfinite breakwater. An ideal (perfectlyreflecting)breakwater alignedon thex axisand extending fromx =0to x = +awill require the boundary condition

-=o,dF o<x<+co, y = o

(4.133)

dY

For the boundary condition for x < 0, we require that the waves be

purely progressive in the positive y direction, that is,

~ ( xy,)=Ae+, x + -a,all y (4.134)

which, when combined with Eq. (4.132),yields the desired result.

The solution of the governing equations was developedby Sommerfeld

(1896)and is expressedas

wherep,j?',and r are defined by

and the signs ofp and j?' to betaken depend on the quadrant in which the solution is being applied (see Figure 4.25).With considerablealgebra, it can be verified that F(x,y) as given by Eq. (4.135) satisfies both the Helmholtz equation and the boundary condition given by Eq. (4.133).The solution for F(x,y) may be evaluated in terms of Fresnel integrals

L'cos 1nu2du and 1"sint nu2du (4.137)

which are tabluated in Abramowitz and Stegen(1965).

As F(x,y) is complex, it contains both wave amplitude and phase information.As expected, at largex and y <0a standing wave is formed, at largex andy the waves approach zero, and forx -,-a,and ally ,the wave is unaffected by the presence of the breakwater. Figure 4.26 represents wave



---PAGE-135---



Sec. 4.9 Wave Diffraction 119

Figure4.25 Signcriterion for(J,p). 1

fronts and isolines of relative wave height for y > 0;the horizontal scales are rendered dimensionless in terms of wave lengths.

Although the solution for F(x,y )is algebraicallycomplicated, there are several simple features that are ofengineering relevance. First for largey,the relative wave height approaches one-half on a line separating the geometric shadow and illuminated regions (x =0) (see Figure 4.27). Second, for y/L > 2, isolines of wave height behind a breakwater may be determined in

10

8

###### 6

4

###### 2

-8 -6 -4 -2 0 2 4 6 8

-X

L

Figure4.26 Wavefrontsandcontour linesofmaximum wave heights in the lee of a rigid breakwater, and waves being incident normally. -( )exact solution, (-- - --)approximatesolution based on Eq. (4.138) and Figure 4.27. (After Penney and Price, 1952.)



---PAGE-136---



120 EngineeringWave Properties Chap. 4

Figure4.27 Relativediffractedwave height R versusdistanceparameterW. (From Penney and Price, 1952.)

accordance with the following parabolic equation:

x = v m

###### (4.138)

###### L 16 2 L

in whichPRis the abscissa value obtained from Figure 4.27 for any value of relative wave height, R = H/HI. The dashed lines in Figure 4.26 compare several isolines obtained from Eq. (4.138)and Figure 4.27with those from the complete solution.

Obliquely incident waves on a semi-infinite breakwater. For this case, there will also be three regions or zones corresponding to (1) the geometric shadow zone, (2) the geometric illuminated zone outside the region of direct reflection from the breakwater, and (3) the up-wave region within which direct reflection from the breakwater occurs.An example of a diffraction diagram showing isolines of relative wave height is presented in

- Figure 4.28 for 0, = 30". Plots for other directions are presented in the Shore Protection Manual (1977). The diffracted wave fronts in the geometric shadow zone are approximated well by circles with their centers at the breakwater tip. As before, the relative wave height along a line separating the geometric sheltered and illuminated zones is approximately one-half.

Wave diffraction behind an offshore breakwater of finite length. For an offshorebreakwater of finite length, an approximate diffraction diagram can be developedby consideringthe maximum wave height to be the sum of the two waves diffractingaround each of the two ends of the breakwater.The resulting diffraction coefficients would therefore represent an upper limit, since only in very special locations would the waves reinforce completely.

- Figure 4.29 presents approximate isolines of diffraction coefficients for an offshore breakwater which is 10wave lengths long.




---PAGE-137---



###### O0

4.28Wavediffractionbyasemi-infiniteimpermeablebreakwater,waveapproachFigure

30".1962.)direction(AfterWiegel,=

Radiusiwavelength

ofwaveDirection



---PAGE-138---



###### 122 Engineering Wave Properties Chap. 4

###### 0.40

Figure4.29 Isolines of approximate diffraction coefficients for normal wave incidence behind a breakwater that is 10 wavelengths long. (From Penney and Price, 1952.)

Waves of wavelength L

Wave diffraction due to waves of normal incidence propagating through a breakwater gap. For a gap width that is in excess of one wave length, it can be shown that the diffracted wave solution is very nearly given by the superposition of terms in the diffraction solution selected to approximately satisfy the boundary conditions on the two breakwater segments.

- Figure 4.30 presents an example for a gap that is 2.5 wave lengths long.


Waves propagating througha breakwater gap narrower than one wave length. For this case, the waves in the lee of the breakwater propagate as if from a point source and in accordance with energy conservation relationships; the wave heights decrease as r-”’ with distance from the center of the gap. The expression for relative wave height as a function of r for locations not too near a gap ofwidth b is

(4.139)

in which yis the Euler constant (=0.577.. .).



---PAGE-139---



Sac.4.10 Combined Refraction-Diffraction 123

Figure4.30 Isolines of approximate diffraction coefficients for normal wave incidence and a breakwater gap width of 2.5 wavelengths. (From Penney and Price, 1952.)

###### 4.10 COMBINED REFRACTION-DIFFRACTION

Refraction, which involves wave direction and height changes due to depth variations, and diffraction, caused by discontinuities in the wave field resulting from the wave’s interaction with structures, often occur simultaneously. For example, at the tip of a breakwater, diffraction is of utmost importance, yet if a large scour hole exists there or if a beach is nearby, refraction is important aswell. It therefore is necessary to be ableto treat both phenomena simultaneously.

Theoretically, the problem is difficult, demanding the solution of the Laplace equation in an irregularly varying domain. Therefore, approximations must be made to simplify the problem. The crudest approach, most often used in practice, is to assume that diffraction predominates within several wave lengths of the structure and farther away, only refraction. In the last decade, however, a newer approach has evolved through the use of a model equation. Berkhoff (1972), seeking an equation governing the propagating wave mode [which has a coshk(h +z )dependency over the depth], multiplied the Laplace equation by cosh k(h+z) and integrated over the



---PAGE-140---



124 Engineering Wave Properties Chap. 4

depth.This reduces the equation to the two horizontal dimensions and yields (4.140)

where vh is the horizontal gradient operator and C and Cgare the wave and group velocity,respectively.TheFis a complex function which represents the wave amplitude and phase. The total velocity potential then is

cosh k(h+z)

&x, Y ,4=F- (4.141)

cosh kh

In deriving this equation it was assumed that the bottom slopesaremild.This model equation, while approximate in intermediate depth, is exact in both deep and shallow water. In deep water it reduces to Eq. (4.131), while in shallow water it is

gvh * (hVhJ;?+dF=0 (4.142)

which is a two-dimensional equivalent of Eq. (5.37),valid for long waves, as discussed in Chapter 5.

Analytical solutions to the model equation are few;Jonsson and BrinkKjaer (1973) and Smith and Sprinks (1975) present the case of waves encountering a circular island, and for Smith and Sprinks, the case for edge waves and waves propagating over a step are also treated. Kirby et al. (1981) used the model equation to study edge waves on irregular beach profiles. Numerical finite element techniques have been used by Berkhoff to treat arbitrary boundary problems such as harbors and islands.

A second approach, developed by Radder (1979) and Lozano and Liu (1980), utilizes a parabolic approximation to the elliptic Laplace equation, which makes the solution more easily obtainable as only initial condition must be specified as opposed to all the lateral boundary conditions. These methods are computationally quicker than Berkhoff’s.

###### REFERENCES

ABRAMOWITZ,M., and I. A, STEGUN,Handbook of Mathematical Functions, Dover,

NewYork, 1965.

BERKHOFF,J. C.W., “Computation of Combined Refraction-Diffraction,” Proc. 13th Con5 CoastalEng., ASCE,Vancouver, 1972.

DALRYMPLE,R. A., R. A. EUBANKS,and W. A. BIRKEMEIER,“Wave-Induced Circulation in Shallow Basins,” J. Waterways, Ports, Coastal Ocean Div.,ASCE,Vol. 103, Feb. 1977.

DEAN,R. G. and E URSELL,“Interation of a Fixed Circular Cylinder with a Train of Surface Waves,” MIT Hydrodynamics Laboratory Rept. T.R. No. 37, Sept. 1959.



---PAGE-141---



Chap. 4 References 125

GALVIN,C. J., “Breaker type classifications of three laboratory beaches,” J. Geophys.

Res., Vol. 73, No. 12, 1968.

JONSSONI,. G., and 0.BRINK-KJAER,“A Comparison between Two Reduced Wave Equations for Gradually Varying Depth,” ISVA Prog. Rep. 31, Tech. Univ., Denmark, 1973.

KIRBY,J . T., R. A. DALRYMPLE,and l? L.-E LIU,“Modification of Edge Waves by

Barred Beach Topography,” CoastalEng.,Vol. 5,1981.

KOMAR,F? D., and M. K. GAUGHAN,“Airy Wave Theory and Breaker Wave Height

Prediction,” Proc. 13th Con$ Coastal Eng., ASCE,Vancouver, 1972.

LOZANO,C. J., and I? L.-E LIU,“Refraction-Diffraction Model for Linear Surface

Water Waves,” J. Fluid Mech.,Vol. 101, 1980. MCCOWANJ,. , “On the Highest Wave of Permanent Type,” Philos. Mag. J. Sci., Vol.

38, 1894. MUNK,W. H., “The Solitary Wave Theory and Its Applications to Surf Problems,”

Ann. N. 2: Acad. Sci., Vol. 51, 1949.

MUNK,W. H., and R. S.ARTHUR,“Wave Intensity along a Refracted Ray in Gravity

Waves,” Natl. Bur. Stand. Circ. 521, Washington, D. C., 1952. NODA,E. K., “Wave-Induced Nearshore Circulation,” J. Geophys. Rex, Vol. 79, No. 27, 1974, pp. 4097-4106. NODA,E. K., C. J. SONU,V. C. RUPERT,and J. I. COLLINS,“Nearshore Circulation

under Sea Breeze Conditions and Wave-Current Interaction in the Surf Zone,” Rep. TETRA T-P-72-149-4, Tetra Tech, Inc., Pasadena, Calif, 1974.

PENNEY,W. G., andA.T.PRICE“, The DiffractionTheory of Sea Waves and the Shelter Afforded by Breakwaters,” Philos. Trans. Roy. SOC.A,Vol. 244 (882), pp. 236-253, 1952.

RADDER,A. C., “On the Parabolic Equation Method for Water-Wave Propagation,” J. Fluid Mech.,Vol. 95, 1979. SMITH,R., andT. SPRINKS“, Scattering of SurfaceWaves by a Conical Island,” J. Fluid

Mech.,Vol. 72, 1975. SOMMERFELD,A., “Mathematische Theorie der Diffraction,” Math. Ann.,Vol. 47, pp. SVENDSEN,I. A. and J. BUHR HANSON“, Deformation Up to Breaking of Periodic US. ARMY,Coastal Engineering Research Center, Shore Protection Manual, Vol. I, WEGGEL,J. R., “Maximum Breaker Height,” J. Waterways, Harbors Coastal Eng. WIEGEL,R. L., “Transmission of Waves Past a Rigid Vertical Thin Barrier,” J. WIEGEL,R. L., “Diffraction of Waves by a Semi-infinite Breakwater,” J. Hydraulics WILSON,W. S., “A Method for Calculating and Plotting Surface Wave Rays,” Tech.

317-374,1896. Waves on a Beach,” Proc. 15th Conf: CoastalEng., ASCE, Honolulu, 1976. U.S. Government Printing Office, Washington, D.C., 1977. Div., ASCE,Vol. 98, No. WW4, Nov. 1972. Waterways Harbors Div.,ASCE,Vol. 86, No. WW1, Mar. 1960. Div., ASCE,Vol. 88,No. HY1, pp. 27-44, Jan. 1962. Memo 17,U.S.Army, Coastal Engineering Research Center, 1966.



---PAGE-142---



126 EngineeringWave Properties Chap. 4

###### PROBLEMS

- 4.1 (a) A wave train is propagating normally toward the coastline over bottom topography with straight and parallel contours. The deep water wave length and height are 300 m and 2 m, respectively. What are the wave length, height, and group velocity at a depth of 30 m?

- (b) What isthe average energy per unit surface area at the site of interest?
- (c) Work part (a) for the case of the same deep water characteristics, but with Derive the relationship for the average potential energy per unit interface area associated with the interface displacement: (Note: Neglect capillary effects.)


deep water crests oriented at 60"to the bottom contours.

- 4.2

H

r) 2

= - cos (kx - of)

h'

/\

/ 11

h" p" >p'

- 4.3 The harbor entrance shown below is designed for the following deep water wave conditions:


H0=5m

###### T = 1 8 ~

###### b- 6000m-4

###### Ocean b, Harbor

Statibn B

It isdesired to design the width at station B such that the wave height at station B resulting from the design wave is 2 m. What must be the slope of the side



---PAGE-143---



###### Chap. 4 Problems 127

walls between A and B for this criterion to be satisfied? Use the following information:

bA= 100m

###### hA= 15m hB= 10m

and assume that the wave height is uniform acrossthe harbor width at station B and that the spacing between orthogonals at station A is one-half that in deep water.

- 4.4 Observations of the water particle motions in a small-amplitude wave system have resulted in the following data for a total water depth of 1 m.

major semiaxis =0.1 m minor semiaxis = 0.05 m

These observations apply for a particle whose mean position is at middepth. What are the wave height, period, and wave length?

- 4.5 As a first approximation, the decrease in wave amplitude due to viscous effects can be considered to occur exponentially. For example, for a progressive wave v,


###### H,

###### q =-e-w cos (kx- at)

2

- (a) Develop an expression corresponding to that above for the wave system resulting from a wave ofheight Hgenerated at the wave maker, propagating (and sufferinga loss in wave height due to viscosity)to the barrier which is at x = C, reflecting back (reflection coefficient = 1.0) and propagating back to the wavemaker. Do not consider secondary reflections from the wavemaker.
- (b) Outline a laboratory procedure for determining the wave system amplitude envelope Iq I.
- (c) Showthat


H

###### I vI =-2 e-@J2 [cos2k(x- C) +cosh 2p(x- t)]

- n - - -

/ - - w - -

x = o X"



---PAGE-144---



128 Engineering Wave Properties Chap. 4

- 4.6 Awave of 10speriod is propagating toward the rubble mound breakwater. The recording determined by the traversing pressure sensor is shown below. Calculate the rate (per meter of width) of energy dissipation by the breakwater. At what separation distance do the pressure maxima occur?

Pressure 4700 N/m2

0

Pressure record from traversing sensor

- 4.7 An important problem in beach erosion control is the scour in front of vertical walls due to reflected waves. Assuming perfect reflection from a wall and shallow water conditions, determine the resulting water depth under the node nearest the wall if the wave height and period are known at the wall. Assume that the equilibrium scour depth h is one for which the maximum horizontal velocity at the bottom is less than or equal to 3 m/s.
- 4.8 For a group of waves in deep water, determine the time for each individual wave to pass through the group and the distance traveled by the group during that time if the spacing between the nodes of the group is LI and the wave period of the constituent wave is T.There are n waves in the group.
- 4.9 Two pressure sensorsare located as shown in the sketch. For an 8-sprogressive wave, the dynamic pressure amplitudes at sensors 1and 2 are 2.07 x lo4N/m2 and 2.56 x lo4N/m2,respectively. What are the water depth, wave height, and wave length?


Sensor 2

Sensor 1

1.62 m



---PAGE-145---



Chap. 4 Problems 129

The z axis is oriented vertically upward, that is, in a direction opposed to the gravity vector. The following values may be used:

g = 9.81 m/s2 p = 992 kg/m’

- 4.10 An experiment is being conducted on the wave reflection-transmission by the step-barrier combination shown in the drawing that follows. The characteristics of the two wave envelopes are shown.

- (a) What is the height A of the step?
- (b) Is enough information given to determine whether or not energy is conserved at the step-barrier?
- (c) Ifthe answer to part (b)is “no,” what additional information is required?If the answer to part (b) is “yes,” determine whether energy lossesoccur at the step-bamer.


Step

- 4.11 An axially symmetric wavemaker is oscillating vertically in the free surface, generating circular waves propagating radially outward. At some distance (say Ro)from the wavemaker, the crestsare nearly straight over a short distance and the results derived for plane waves may be regarded as valid for the wave kinematics and dynamics at any point. The wave height at R, isH(R0).Derive an expression forH(r),where r > Ro.(The depth is uniform.)
- 4.12 A wave with the following deep water characteristics is propagating toward the coast:


Ho= 1 m

###### T = 1 5 ~

At a particular nearshore site (depth = 5 m) a refraction diagram indicates that the spacing between orthogonals is one-half the deep water spacing.

- (a) Find the wave height and wave length at the nearshore site.
- (b) Assuming no wave refraction, but the same deep water information as in part (a), and that the wave will break when the ratio H/h reaches 0.8, in what depth does the wave break?




---PAGE-146---



130 Engineering Wave Properties Chap. 4

- 4.13 A wave with the following deep water characteristics is propagating toward the shore in an area where the bottom contours are all straight and parallel to the coastline:

H o = 3 m

T =10s

The bottom is composed of a sand of 0.1 mm diameter. If a water particle velocity of 30 cm/s is required to initiate sediment motion, what is the greatest depth in which sediment motion can occur?

- 4.14 For the wave system formed by the two progressive wave components

H,

2

q,=-cos(kx- ot+E , )

H,

2

q,=-cos(kx+of -E,)

derive the expression for the average rate of energy propagation in the +x direction.

- 4.15 Develop an experimental method for determining the phase shift E incurred by a wave partially reflecting from a bamer.
- 4.16 Develop an equation for the transmitted wave height behind a vertical wall extending a depth d into the water ofdepth h based on the concept that the wall allows all the wave power below depth d to propagate past (Wiegel, 1960). Qualitatively, do you believe that your equation for the transmitted wave height would underestimate or overestimate the actual value? Discuss your reasons.
- 4.17 What is thephysical reason that the pressure is hydrostatic under the nodes ofa standingwave (to first order in wave height)?
- 4.18 Consider an intuitive treatment for the sum of an incident wave of height H, and reflected wave of height H, and show that the same envelope results are determined as obtained in the text. Represent the incident wave as two components: one of height H,and the second asH,-H,. Now the combination of the first incident component with the reflected yields a pure standing wave and the second incident component is a pure progressive wave. Simply add the envelopes for the pure standingand progressive wave systems.
- 4.19 Develop the pressure response factor by integrating the linearized equation of motion from some arbitrary elevation z up to the free surface z = r].
- 4.20 Using asa breaking criterion that the horizontalwater particle at the wave crest exceeds the wave celerity, determine breaking criteria for deep and shallow water. Why does the latter one differ from that of McCowan?




---PAGE-147---



###### Long Waves

Dedication

###### LORD KELVIN

Sir William Thompson (Lord Kelvin) (1824-1907), born in Belfast, contributed significantly to the field of hydrodynamics, from its theoretical basis to the solution of numerous wave problems. Here he is cited for his work in long waves with Coriolis and gravitational forcing, but he addressed a variety of problems,as isevidencedby his661 papers and 56 patents. (See Mathematical and PhysicalPapers, Cambridge,1882.)

When he was 11 years old, he entered the University of Glasgow, leavingin1841to enter Peterhouse, CambridgeUniversity,to further his education. During this time he made a trip to Paris University to meet Biot, Liouville, Sturm, and Foucault. In 1846 he became Professor of Natural Philosophy at Glasgow,a post he held for 53 years.

A contemporary of Joule (whom he had met at Oxford)as well as Carnot, Rankine, and Helmholtz, Kelvin pursued a variety of research areas, including heat and heat conduction. Between 1851 and 1854, he fully elucidated the first two laws of thermodynamics, and suggested the concept of refrigeration by the expansion of compressed cold air.

Kelvin contributed actively to the early developmentof submarine cables. He interacted with cable companies and developed means of testing the purity of copper inthe cables after he showed that the purity affected its conductivity. He was knighted in 1866 for his cable work. Before the Institution of Civil Engineers in 1883, Kelvin remarked, “There cannot be a greater mistake than that of looking superciliously upon practical applications of sciences.” This philosophy led him to invent numerous electrical devices such as a galvanometer and an ampere gauge, and to set up an electrical company, Kelvin and White, Limited.

He became the first Baron Kelvinof Largsin1892. He died in1907 and was buried inWestminsterAbbey.

131



---PAGE-148---



132 LongWaves Chap. 5

###### 5.1 INTRODUCTION

Waves propagating in shallow water,kh <n/lO, areoften called long waves or shallow water waves.Tidal waves, tsunamis (erroneouslycalled tidal waves), and other waves with extremely long periods and wave lengths are shallow water waves, even in the deep ocean.

The studyof long waves is of importance to the engineer in the designof harbors and in studying estuaries and lagoons. Because long wave energy is effectively reflected by structures or even by beaches of mild slope, harbors, which have waves propagating into them, can be excited into resonance by long waves of the proper period, obviously not a desirable state. Tidal propagation in estuaries is affected greatly by the geometry of the estuary; resonance, as in a harbor, can also occur, yielding large tides(50+ft at the Bay of Fundy).

In this chapter selected long wave topics are presented, after the equations governing them are derived.

###### 5.2 ASYMPTOTIC LONG WAVES

Previously, the velocity potential and the corresponding velocities and free surface profile for small amplitude waves were derived. The velocities and the surface profile for a progressive wave are described by these equations:

###### H

q =-cos (kx-at)

2

Using the shallowwater asymptotic forms of the hyperbolic functions,we can arrive at equations for the water particle velocitiesof long waves,kh << n/10,

us g H k rlc

=-cos (kx-at)=-

2a h (5.2)

where the shallow water wave celerity C = &%was introduced and the subscript s denotes shallow water. Interestingly, us is not a function of elevation; the horizontal velocity is uniform over depth. For the vertical water particle velocity,

w, =g H k-[k(h +z)]sin (kx-at)

20

--_ sin(kx-at) (5.3)

= -C

###### 2 h



---PAGE-149---



Sec. 5.3 Long Wave Theory 133

The vertical velocity varies linearly with depth from zero at the bottom to a maximum at the surface and is much smaller in magnitude than us. The ratio of their maximum values is

where kh issmall.The pressure under these long waves is found by Eq.(4.22):

cosh k(h +z ) P = -P@ +Pgrl cosh kh

###### or

The pressure under these long waves is thus hydrostatic, as might be expected since the vertical accelerations can be shown to be small.

###### 5.3 LONG WAVE THEORY

In Chapter 3 the equations and boundary conditions necessary to solve for two-dimensional water waves were presented. If we assume that the pressure under long waves is hydrostatic at the outset, we can integrate the governing equations over the water depth to get the long wave equations directly rather than asymptotically. Integrating over depth should not be a surprising technique here, particularly when we know that the horizontal velocity is not a function of depth. As a further generalization of the results, the flow will be allowed to be three-dimensional.

5.3.1 Continuity Equation

The three-dimensional conservation of mass equation for an incompressible fluid is

a u a v aw

###### -+-+-=o

(5.6)

ax ay az

This is true everywhere in the fluid. Integrating over depth, we have

(5.7)

The Leibniz rule of integration is used to integrate terms such as the



---PAGE-150---



134 LongWaves Chap. 5

first two on the right-hand side of this expression. In general, it is stated as

Note that if the limits of the integral are constants relative to the variable of integration, the differential operator can be moved into or out of the integral without generating additional terms.

Therefore, the integrated continuity equation is rewritten as

###### d arl ah

dz - u(x,Y , rl) -- u(x,Y ,-h) -+ w(x, Y , V ) - w(x, Y , -h)

ax ax ax

###### + l:v dz-v(x,y,q)--v(x,y,-h)-=0 (5.9)

arl ah

aY aY aY

If we define

###### U=-lhudz1 q and V=-J‘vdz1

h + v h + q -h

through the use of the mathematical definition of an average (thereby incorporating any possible vertical variation in horizontal velocity), or if we just assumethat u and v areconstantsover the depth, Uand V,the continuity equation can be written as

(5.10)

Further simplification will result through the use of boundary conditions. The kinematic free surface boundary condition is, in three dimensions,

- (5.11)
- (5.12)


The bottom boundary condition for a fixed (with time) surface is

Substitutingthese conditions into the vertically integrated continuity equation yields the final form of the continuity equation

a[U(h+701+a[V(h+rl)l =-d’l (5.13)

###### ax aY at



---PAGE-151---



Sec.5.3 LongWave Theory 135

This equation can also be derived by considering a column of water of area dxdy andheight(h+v).Thecontinuity equation statesthat the sumofall the net fluid flows into the column must be balancedby an increaseof fluid in the column, which, since it is an incompressible fluid, is manifested by a change in height (volume) of the column (see Figure 5.1). This exercise is recommended to the reader.

5.3.2 Equationsof Motion

The equation of motion in the x direction for a fluid is [Eq.(2.35)]

at ax ay az pax p(ax ay az

- + u - + v - + w - = - - - + -au au au au 1 ap 1 -+-+-ar, az,, (5.14)

Using the equation for pressure under a long wave [Eq. (5.5)],p =pg(q- z), which states that the pressure is hydrostatic, the first term on the right-hand side becomes

(5.15)

which is constant over depth. After adding the continuity equation, and vertically integrating using Leibniz’s rule, as well as using the kinematic boundary conditions at the surface and the bottom, the horizontal momentum equation becomes

(5.16)

Control volume for conservationof mass.The qx,qvdenote U(h+ r])

Figure 5.1 and V(h+r]), respectively.



---PAGE-152---



136

LongWaves Chap. 5

where

Equation (5.16) is based on the assumption that,z and,,z do not depend on z.The parameters are momentum correction factors,P, is slightly greater than unity, and they are used in hydraulics in order to permit the substitution of the squared mean velocity for the mean of the velocity squared.

They equation becomes

(5.17)

Quite often in practice the momentum correction factor is considered to be unity, and, employing the continuity equation, the equations may be simplified to

- (5.18)
- (5.19)


The governing equations, continuity and the equations of motion, are nonlinear.To linearize them to facilitate analytical solutions, we again argue that U , V,and qare small; therefore, their products are also small.The linear equations become, in the absence of shear stresses:

Linearized continuity equation-

(5.20)



---PAGE-153---



Sec. 5.3 Long Wave Theory 137

Linearized frictionless long wave equations of motion-

###### au aq

_-- -g - (5.21)

at ax

_-av--g -aq

(5.22)

at aY

If the bottom is horizontal, the equations can be cross-differentiated to eliminate U and V,yielding

(5.23)

where C= @.This is known as the “wave equation,” which occurs quite often in other fields; it governs, for example, membrane vibrations and planar sound waves. To compare with the previous asymptotic results, a solution of the wave equation will be sought for only the x direction. The solution to this equation for a progressive long wave is

H 2

q =-cos (kx- at)

(5.24)

Substituting into the x equation of motion [Eq. (5.21)]yields H

###### =g -k sin (kx- at)

- (5.25)
- (5.26)


at 2

or

U =g -H k cos (kx-at)=-VC

20 h

the same as found by asymptotic means before. form of the dispersion relationship as derived in Chapter 3.

Substituting into the continuity equation yields C2=gh, the long wave

5.3.3 The Energy and Energy Flux in a Long

Wave

For a progressive long wave, the total average energy may be obtained asbefore asthe contributions from the kinetic (KE)and potential energy(PE) components. Because the vertical velocity component is much smaller than the horizontal velocity component, it is not necessary to account for the vertical velocity (for the same order of accuracy).The appropriate expressions are

(5.27)



---PAGE-154---



138

Long Waves Chap. 5

and

Substituting Eqs. (5.24) and (5.26) for U and q, respectively, and integrating, it is found that

###### KE = PE = kpgH2

and, as before, the total energy per unit surface area is

###### E =KE +PE=ipgH2 (5.29)

The average energy flux can be shown to be

-

3= EnC = E,@

which again shows that the wave energy travels with the phase speed of the shallow water wave. If we examine the change in wave height due to changes in water depth and channel width via conservation of energy flux, we find that

which is the shallow water approximation to Eq. (4.116). For the special case of bl = b2,this relationship is called Green’s law.

5.4 ONE-DIMENSIONAL TIDES IN IDEALIZED CHANNELS

5.4.1 Co-oscillating Tide

As a simple example of tidal wave propagation into a channel, consider a long wave propagating from the deep ocean intoachannel of constant depth which has a reflectingwall at one end.This configuration isdepicted in Figure 5.2. The wall requires that there be an antinode of a standing wave system there.

Adding two long waves (remember, the equations are linear and superposition is still valid), we have

H H

###### q =q,+ qr=-cos (kx-at)+-cos(kx +at)

2 2

###### = H cos at cos kx (5.30)

a pure standing wave system as before. Note that the total water surface elevation has a range twice that of the incident tidal height and a = 2n/T, where T is the tidal period. For a semidiurnal tide, two highs and two lows



---PAGE-155---



Sec. 5.4 One-DimensionalTides in Idealized Channels 139

X = I

Figure 5.2 Co-oscillating tide in a channel of length1.

during a lunar day, the tidal period is 12.4 h. The distance to the node isfound by equating the spatial phase function of qr to a/2, that is, finding the phase position for which q equals zero.

- (5.3la)
- (5.3lb)


###### or

The rangeof the tide at the entrance to the channel is

###### 2(q(f)1=2HI coskfl-

- (5.32)
- (5.33)


Relating q(2)to q(O), the amplitude of the tide at the wall, we have

1

For channels for which f approaches (2n - 1)(L/4)and n = 1,2,...,the ratio Iq(O)/q(f)I approaches infinity (i.e., this represents a resonant condition).

5.4.2 Channels with Variable Cross Sections

In deriving the equations of motion and continuity, had we not taken a unit width in the derivation, but considered a channel of width b, the linearized one-dimensional equations valid along the channel centerline would have been

- (5.34a)
- (5.34b)


These can be verified by integrating Eqs. (5.6)and (5.14)with respect to y prior to the integration over depth. Differentiating the first equation (5.34a)



---PAGE-156---



tongWaves Chap.5

140

with respect to time,

- (5.35)
- (5.36)


Substituting the second equation (5.34b) yields

which reduces to the wave equation ifband h areconstant.As in the previous case for the constant depth basin, assume that q(x,t) can be written as q(x,t) = q(x)cos at.The equation then becomes

(5.37)

Several examples of the application ofthis equation to estuaries with linearly varying widths, depths, or both are provided by Lamb (1945) in Article 186. Onecase is discussedbelow. In all these examples, the resultingwave height is different from that predicted by Green's law, as Eq. (5.37) allows for the reflection of waves by the topographic changes, while Green's law assumes that the bathymetric changes are sogradual as to not cause reflection.

- Example 5.1


Consideran estuary of uniform depth whose width increases linearly (from zero) with distance toward the mouth at x = I. Determine the tidal surface elevations within the estuary, due to the co-oscillating tide.

Solution. Let b = ax, where a is equal to b//Iand b/is the width of the bay at the mouth. Substituting into Eq. (5.37) the following equation results directly:

###### (5.38)

where k2= d/C2=$/gh. This equation is a Bessel equation of order zero which is solved in terms of Bessel functions. The general solution is

q(x,t)= [CIJO(kx)+C,Yo(kx)]cos at (5.39a)

where CIand C2are constants to be determined. At x = 0, the end of the channel, Yo(0),is infinite, which would be unrealistic for ~ ( 0t);, therefore, C2 = 0. To evaluate C,,the tide atx = I , the mouth, is taken tobe (Hj2)cosgf,where, again, H i sthe local tide range.

H

ll(L t ) = CIJO(kl)cos at = -cos at or

2



---PAGE-157---



Sec. 5.5 Reflectionand Transmission Past an Abrupt Transition 141

Figure5.3 Standing waves in a pie-shaped estuary of uniform depth.

Finally, the solution is

(5.39b)

As shown in Figure 5.3 the zeroth-order Bessel function calls for a large increase in tidal height into the estuary or bay, with a correspondingwave length decrease in the near field (about 25% over the first half wave length). If the estuary length 1 corresponds to a zero of the Bessel function, then again the possibility for resonance occurs.

###### 5.5 REFLECTION AND TRANSMISSION PAST AN ABRUPT TRANSITION

A more dramatic example oflong wave reflection (and transmission) occurs when there is an abrupt change in depth or channel width. Also in this case, Green's law does not apply due to the presence of a reflected wave. Figure 5.4 showsthe geometry ofthe transition region. The fluid domain is divided into regions 1 and 2 as shown.The incoming wave qiwill be assumed to propagate in the positive x direction with height Hi.At the step, it is expected that a portion ofthe wave will be reflected and someof ittransmitted.Therefore, in

Figure5.4 Elevation and plan views of an abruptchannel transition.



---PAGE-158---



142 Long Waves Chap.5

each region, the total wave forms are assumed as follows:

Hi H

2 2 ql= qj +q r =-cos(klx-at)+2cos(klx+at +E,) q 2 =qf=-cos(k2X -at +€0

Hf (5.40)

2

where the subscripts i, r, and t signify incident, reflected, and transmitted, respectively.The differencein sign modifyingat in the phase function for the reflected wave means that this wave is propagating in the negativex direction. In each region the angular frequenciesare the same; however, the wave numbers are different due to the change in water depths. The two phase angles, E, and Ef,are included to allow for the possible phase differences caused by the reflectionprocess.

At the step there are two boundary considerations that must be met by the wave forms ql and q 2 . First (at x = kb, where 6is infinitesimally small), the water levels on each side of the step should be the same, as, from the long wave equations of motion, any finite water level change over an infinitely small distance 26 would give rise to infinite accelerations of the fluid particles. Second, from continuity considerations, the mass flow rate from region 1must equal that into region 2. For a homogeneous fluid, this merely reducesto matching volumetric flow rates between regions.Applying the first condition gives us

qi+qr=qf atx =0 (5.41) or, through a trigonometricexpansion after substitution,

2 2

- (5.42)

As this condition must be valid for all time t, two independent condi-

- (5.43a)


tions result by equating each bracketed term separatelyto zero:

###### H;iH , cos E, =HZ cos E/

H, sin E , = -H, sin El (5.43b)

The continuityof flowcondition can be written in terms of the horizontal water particle velocity of the wave multiplied by the cross-sectional area for each region [fromthe width-integrated continuity equation, Eq. (5.34a)l.

( U l ~ h ) ~= ( U l ~ h ) ~at x = 0 (5.44)



---PAGE-159---



Sec. 5.5 Reflection and Transmission Past an Abrupt Transition 143

or, recalling that fora long wave,

in the direction of the wave,we can write

biCi(V1- Vr) = b2C2~r (5.45)

Again we have two conditions, after trigonometric expansion and

equating the terms modifying the cosine and sine, respectively:

blClHi - biCIH,cos E~ = b2C2HI cos€1 blCIH,sin E , = b2C2Hfsin (5.47)

###### (5.46)

Denoting the reflection and transmission coefficients by K , (=H,/Hi) and K, (=Hf/Hi),respectively, the four equations (5.43a, 5.46, 5.43b,and 5.47)in terms of the four unknowns (K,, K,, E,, and el)are

1+ K , cosE, =K, cosE, (5.48) 1 - K, cos E , = K( -b2C2cos E,

###### (5.49) K~sin E~ = -K, sin.€, (5.50)

biCi

- (5.51)
- (5.52)


Subtraction of the last two equations yields

which requires that E, be +_nnfor non-trivial values of xf.Multiplying Eq. (5.50) by b2CzlbICI and adding to Eq. (5.51)also indicates that E , = knn for nontrivial solutions. The four governing equations can therefore be condensed to the following two:

###### 1 k K , = kKf (5.53) (5.54)

in which the plus and minus signs follow from the requirements on E, and E,. It is only known that the signs on the right-hand side of each equation are the same and those on the left-hand side are in opposition.The correct signs will be determined later from physical reasoning. Adding Eqs. (5.53)and (5.54),



---PAGE-160---



144 Long Waves Chap. 5

we find that

###### (5.55)

and here it is clear that the +sign is to be taken because forb2C2 =blCI,that is, the case of a uniform channel, the transmission coefficient is obviously unity. Multiplying Eq. (5.53) by b2C2/bICIand subtracting from Eq. (5.54) gives us

###### (5.56)

and here the minus sign is tobe taken since for the limiting caseofa vanishing channel, b2CZ/blCI= 0, the reflection coefficient should be +I, that is,

###### (5.57)

Several interesting cases can be examined for bl=bZ.If the long wave assumptions are still valid, yet hi >> h2,then K~-.2 and K, -,1. This case corresponds to a pure standing wave in region 1 and transmitted wave of the same height as the standing wave. But if the situation is reversed, that is, if long waves in very shallow water propagate to a region of greater depth, h2>> hI,then rc, -.0and rc, -.-1. (Anegative reflection coefficientmeans only that the phase of the wave E,, which we had taken as zero degrees, is shifted to 180".) It is thus very difficult for waves to propagate from shallow to deeper water.This in fact is true for shortwaves also. [Hilaly(1969)shows interesting experiments for waves unable to propagate over steps.] Figure 5.5 presents the variations of Kr and rcfwith the parameter ( b 2 / b I ) m .

Dean (1964),using this approach and Eq. (5.37), has examined numerous cases of cross-sectional channel changes and obtained the transmission and reflection coefficients.

5.5.1 Seiching

In previous sections, the oscillations of the water in a basin were forced by the tide at a frequency corresponding to the tidal frequency. However, any natural basin, closed or open to a larger body of water, will oscillate at its natural frequency if it is excited in some fashion, such as by earthquake motion, impulsive winds,or other effects.

To predict these oscillations,the equation developed previously can be used.As an example, the seichingin a long rectangular lake with essentiallya constant depth will be examined first. A solution to Eq. (5.23)for standing



---PAGE-161---



Sec. 5.5 Reflection and Transmission Past an Abrupt Transition 145

I I I I I I I I I I I 1

I\JKr ----------------

Y "

### - IO l 1? T2 S3 z 4E d5

U

m

Y'

Figure 5.5 Reflection and transmission coefficients for long waves propagating past an abrupt transition.

waves in this basin is, as before,

###### H

?l=-cos kx cos at. (5.58)

2

exceptthat aand k areboth unknown.At the endsofthe basin, the horizontal velocities must be zero.This requirement can be satisfied using Eq. (5.21) or using the knowledge that the antinodes must be situated at the walls,x = 0,l. This requirement yields sin kx = 0forx =0,l.Therefore,kl = nn,where n is the number of oscillations of the wave within the basin (equivalently the number of nodes). Substitutingfork givesus

L = -21 (5.59)

###### n

For three values of n,the wave lengthsare shown for the basin in Figure 5.6. Each possible typeofoscillation is called a mode, and the mode that occurs in

n = l n = 2 n = 3

Standing waves in a simple rectangular basin. The first three modes are

Figure 5.6

shown.



---PAGE-162---



146 LongWaves Chap. 5

seiching is determined by the cause (forces)that induces seiching. In reality, however, the lower modes are most prevalent since the energy in the higher modes is dissipated more rapidly.

To determine the period of seiching, the dispersion relationship for shallow water waves is used, with Eq. (5.59):

###### or

(5.60)

This formula is known asthe Merian formula. Proudman (1953)gives several examples for actual lakes. For Lake Baikal in Siberia, the length is 664 km and the average depth is 680 m. The Merian formula predicts T = 4.52 h, compared to a measured period of 4.64h.

For more complex one-dimensional basins, a modified Merian formula can be used. Wilson (1966) has summarized the results for a number of geometries and these are presented in Table 5.1. More icCcntly,Wilson (1972) has developed more analytical seiching models and also reviews the literature.

###### 5.6 LONG WAVES WITH BOTTOM FRICTION

The bottom shear stress756retarding the motion of the fluid in unidirectional open channel flow can be expressed in terms of a quadratic friction law:

(5.61)

wherefis the Darcy-Weisbach friction factor and U is the fluid velocity. This equation has been developed through dimensional analysisand experimental data have been used to develop values off. Further discussion of bottom friction appears in Chapter 9.

For an oscillatory flow, it is clear that as the fluid reverses direction, so also must the bottom friction. Therefore, an absolute value sign is introduced.

(5.62)

For wave motions, the bottom friction is a nonlinear function and due to the absolute value sign becomes difficult to work with directly. A common procedure is to linearize the friction term.



---PAGE-163---



Sec. 5.6 LongWaves withBottomFriction 147

Consider U as a periodic function in time, U = Umcos at,where Urnis the maximum magnitude of U.Ifweexpand the shear stressterm in a Fourier cosine' series,we have

m

UlUl =ao+ 2a,cosnat

- (5.63)
- (5.64)


,=I

where

a. =-

and

a,=-2v',lTcosatlcosatIcosnotdt (5.65)

###### T

Evaluating severalof these integralsyields

a0 = 0

###### a2=0

8Gl

###### a3 =15n

All of the even harmonics arezero while the odd harmonics arenonzero. It is interesting that the quadratic friction law has introduced higher harmonics (which is expected as friction is a nonlinear process). Keeping only the first term in the Fourier expansion (recognizing, however, that the next term in the series expansion is only one-fifth of the leadingterm),

(5.66)

This linearization was first developed by Lorentz (1926) utilizing a dissipation argument and is sometimes referred to as the Lorentz concept. For uniform depth the vertically integrated equation of motion in thex direction can now be written with rb = r,(-h), from Eq. (5.18), as

(5.67)

where A =flm/3nh,typically a small number, much less than unity. The continuity equation, Eq. (5.13), remains unchanged, of course. Crossdifferentiating the two equations assumingA is locally constant and substi-

'A cosine series is chosen as U and 76 are even functions of time.



---PAGE-164---



###### I

###### m\o

OQ

0 0

s

-?

0

###### I

###### I

0

09-

I

###### -

###### z%

###### .- -

C

L

4

n a

.-a

M

###### .C

C

ol

.-a

U

cc"

148



---PAGE-165---



oo oo

00

###### 2

00

###### 2

8

.r r-

2

###### 2

~

0 90

0

09-

h!-

Nd

fi

149



---PAGE-166---



150 LongWaves Chap.5

tuting, the wave equation can be derived, including friction:

###### a2q aq a2q at2 at ax

-+A -=gh 7

- (5.68)
- (5.69)


5.6.1 StandingWaves with FrictionalDamping

If a solution is assumed of the form

where k remains fixed, such as would occur with a standing wave in a basin with fixed length, andf(olt) is some unknown function of time, then the equation is

dtf+A -df+ghky=0

(5.70) The total solution is then found to be

###### dt2 dt

q=5e(-A/2)1cos (5.71)

2

where 0,=krCI (the subscript I refers to undamped conditions), C,= ,@ and HIis the initial wave height (at t =0),or

where

###### A

and ar=al

Q. = -

I - 2

The horizontal velocity can be found using the continuity equation

or u=--HI d me-"('sin(a,t +E ) sinkIx (5.72)

2kIh where

ai

E = tan-' -

or

The parameters a,and a,areplotted in Figure 5.7 versus the ratioA/a,. Asardecreases with friction, the period of oscillation increases; friction slows



---PAGE-167---



###### Sec. 5.6 Long Waves with BottomFriction 151

2.0 I I I I 1 I

I

###### I

I

n.

0 1.o 2.0

###### * A/02 *

Decreasing friction Increasing friction

Figure 5.7 Wave number and phase angle fora damped standing wave.

the wave motion. It is clear that the damping ratioA/a,in the expression for a, must be less than 2; otherwise, excessive damping occurs and there is no wave-like motion (such as might occur with a basin full of molasses).

The relative reduction in amplitude over one wave period isa constant value and isexpressed as

###### (5.73)

which decreases rapidly with increasing cri or A. For example, for A/oI as small as 0.05, this ratio is 0.85, or a 15% reduction in height within one wave period.

- Example 5.2


Shiau and Rumer (1974) carried out a series of experiments to examine the decay of shallow water standingwaves (seiches)in a basin. The experiments were conducted in very shallow water (0.15 < h < 8.5cm). Assuming that the motion is laminar, a friction factor can be chosen to compare the above model with their experimental results. Stokes's (1851) second problem, that of an oscillating (with frequency a)flat plate beneath a still fluid, yields a shear stress on the plate with a magnitude

###### =b- = P f i urn (5.74)

where v is the kinematic viscosity of the fluid and U,,, is the magnitude of the oscillating velocity. This problem is directly analogous to the case under considera-



---PAGE-168---



###### 152

a

-9 10-1

###### 1

~

0 3' X 15' (basin size)

2

B

###### A 6' X IS' V 8' X IS'

10-2

I,, L I 1 1 1 1 1 , 8 1 1 1 1 1 I 1 1 1 1 1 1 , , I 1 1 1 1 1 I I ,

Proudman number,P = 2-

gk2Ri

Figure 5.8 Decay modulus versus Proudman number for an assumed laminar friction factor. [From Shiau and Rumer (1974). Equation (21) in figure refers to their solution.]

tion; the only change is that of the reference frame, which is taken as one that is fixed to the oscillating plate.

Since Eq. (5.74) for the.shear stress is linear and the preceding treatment represents a linearized form of the shear stress, the laminar flow problem can be treated directly. Comparison of Eqs. (5.74), (5.67), and (5.18) shows that

(5.75)

The Shiau and Rumer study determined the decay modulusa,which can be obtained from Eq. (5.73) as

- (5.76)
- (5.77)


or from Eq. (5.75)can be expressed as

whereP isthe Proudman number,P = 3/gk2h5.Figure5.8showsthe theoretical value ofacompared with the experimental data.As can be seen, the agreement isexcellent for this case with laminar conditions. For deeper relative water depth, when the flow conditions become turbulent, the friction factor becomes more like that for turbulent open channel flow.

5.6.2 ProgressiveWaves with Frictional

Damping

For a periodic progressivewave, the free surfaceis assumed ofa similar form as before, except for a spatial amplitude dependence,

v =-H I2 e-k,x cos (k,x-ot)

(5.78)



---PAGE-169---



###### Sec. 5.6 Long Waves with Bottom Friction 153

###### 2.0

1.O

###### 0 2 4 6 8 10

-A

0

Figure 5.9 Wave number and phase angle for a damped progressive long wave.

The k,and kiare determined from the differential equation, Eq. (5.68):

1 - +l]"' Nk,[1+'(">I (5.79)

8 0

k,=-Jz[ v q-l]"*N!!!A_2a forsmallA/a (5.80)

where the second expression is valid for smallA/a and kI=a/&%.

Thesewave numbers are plotted in Figure 5.9 as a function ofA/a. As can be seen, k,increases with A/a;therefore, friction decreases the wave length of the wave, thus slowingit.

The change in wave amplitude over one wave length of travel can be readily found to be

dx+L,--e-k,L =e-2~(k,/k,) e-R(A/a) (5.81)

###### rt(x)

which decreases rapidly with increasingA/a. For example, with A/a = 0.05, this ratio is0.85, or a 15%reduction in wave height.The horizontal velocity is then found by the same means as before.

###### HIae-k8x

###### 2h,/m

U = cos(k,x -at -E ) (5.82)



---PAGE-170---



154

where

E =tan-’-ki

###### k,

###### 5.7 GEOSTROPHIC EFFECTS ON LONG WAVES

The earth’s rotation plays an important role in long wave motion when the Coriolis acceleration becomes significant, or equivalently when the wave frequency o is the same order as f c , the Coriolis parameter defined as 2 0 sin $,where $is the earth’s latitude measured positiveand negativein the northern and southern hemispheres, respectively,and o is the rotation rate of the earth, o = 7.27 x lo-’ rad/s-’. Typically, the Coriolis acceleration can produce significant effects in tidal waves.

The frictionless equations of motion for long waves on a rotating surface are modified by the introduction of two terms as follows:

- -+au u-+au v---v=-g-au az7

at ax ay ax

- -+u--+av av v-+feu=-g-av arl


- (5.83a)
- (5.83b)


at ax ay aY where shear stresseshave been neglected.The continuity equation is the same as before:

-arl+ +49+a w +rl)=O (5.84)

at ax aY

To illustrate the effectsof the Coriolis acceleration, consider the propagation of longprogressive wavesin an infinitely longstraightcanal in thex direction with a flat bottom. The transverse velocity V is considered negligible. The equation of motion in the x direction, therefore, is not affected by the presence of the Coriolis force.In the y direction the equation reduces to

feu=-g-arl

(5.85)

dY

which statesthat the Coriolisforce is balancedby a cross-channel hydrostatic force in the form of a water surfaceslope, which varies in magnitude and sign with the longitudinalvelocities in the channel.

If we linearize the equation of motion in the x direction (5.83a), a solution can be assumed as

q = $(y)cos (kx- ot) u=-C q(y)- cos(kx-ot)

h



---PAGE-171---



Sec. 5.7 Geostrophic Effectson LongWaves 155

They equation of motion is now

(5.86)

whereC=m.Thetotalwatersurfaceprofileandhorizontalwaterprofile

motions are now

###### tl =-e-LYlc cos (kx - at)

- (5.87)
- (5.88)


2

&lJ=--e - f Y l c cos(kx-at)

2 h

At the wave crest, the wave amplitude and velocity decrease across the channel (y increasing) while at the wave trough (when the velocities are reversed) the amplitude increases. (Recall that we are dealing with a righthanded coordinate system.) The wave is called a Kelvin wave after Lord Kelvin (SirW.Thomson),who derived an expression for it in 1879.The speed of propagation of the Kelvin wave is found by the continuity equation and it is the same as any other long wave, C = @.

The deviation in tidal ranges between the French and English coasts of the English channel can be largely explained by a northward-propagating Kelvin wave, which causes the French tides to be roughly twice as large (Proudman, 1953).

5.7.1 AmphidromicWaves in Canals

Consider the superposition of two Kelvin waves, traveling in opposite directions but with the same height:

The resulting water surface elevation is always zero at the origin, (x, y )= 0; however, the wave amplitudes reinforce across the channel. The wave propagating in the positive x direction has a surface slope increasing in the negativey direction, while the wave propagating in the negative x direction has a positive surface slope in the positive y direction. Lines of maximum water surface elevation may be found by maximizingq(x,t)as a function of time,

###### - = oarl

at



---PAGE-172---



156 LongWaves Chap. 5

or, after some rearranging,

tanhLY-=-cot at tan kx

- (5.90)
- (5.91)


C Near the origin the equation for the tidal maxima is given by

fey =-kx cot at

C

###### or

Ckx

y =--fc cotat

which is a straight line varying with time.A plot of the lines of high tide as a function of time is shown in Figure 5.10. These lines are called cotidal lines. The origin is called an amphidromic point and the tides are seen to apparently rotate around the origin. However, there is no transverse V velocity and the motion is purely in the X direction. Amphidromic tides of this nature are frequently seen in semienclosed bodies of water; Proudman (1953) cites the Adriatic Sea and Taylor (1920) discusses the Irish Sea. The mechanism for opposite traveling Kelvinwaves requires a narrow channel in order that the motion be rectilinear and either two connected seas or a reflecting end to the channel. Taylor (1920) discusses the problem of the reflection of Kelvin waves and also seiching in a rectangular basin with the influence of Coriolis forces. For a further discussion of long waves with Coriolis effects, see Platzman (1971).

ut = 90".

kx

ut = 120°,300" ut = 150°, 330"

###### Figure 5.10 Cotidallines.



---PAGE-173---



Sec. 5.9 StormSurge 157

###### 5.8 LONGWAVES IN IRREGULAR-SHAPED BASINS OR BAYS

Quite often,astudyof long waves or tides in a basin, lagoon, or near the coast requires the use of a computer, due to the complicated bathymetry, basin shape, and forcing due to winds or tide. To study these problems adequately, recourse must be made to computer techniques.Numerous studies have been made of tidal propagation by computer-too numerous to mention, in fact; however, many are referenced in two papers by Hinwood and Wallis (1975a,b).

###### 5.9 STORM SURGE

The long wave equations can be used to describe the change in water level induced by wind blowing over bodies of water such as a continental shelf (Freeman et al., 1957)or a 1ake.Althoughthe wind shear stressis usually very small, its effect, when integrated over a large body of water, can be catastrophic. Hurricanes, blowing over the shallow continental shelf of the Gulf of Mexico, have caused rises in water levels (storm surges, but not tidal waves!) in excess of 6 m at the coast.

The wind shear stress acting on the water surfacet,, is represented as

###### t, =pkW IwI (5.92)

wherep is the mass density of water, W the wind speed vector at a reference elevation of 10 m, and k a friction factor of order Numerous studies have been made fork (seeWu, 1969)andone of the more widely used setsof results is that of Van Dorn (1953),

where W,= 5.6 m/s.

If we adopt a coordinate system normal to a coastline, and the wind blows at an angle 8to the coast normal (Figure 5.11), then the onshore wind shear stress is ,z = It, I cos 8. The linearized equation of motion in this direction is [from Eq. (5.18), neglectinglateral shear stresses]

(5.94)

After a long time, the flow U in the x direction must be zero, due to the presence of the coast, and therefore the steady-state equations show that the wind shear stress is balanced by the bottom shear stress as well as a hydrostatic pressure gradient. As we can no longer define the bottom fiction in



---PAGE-174---



LongWaves Chap. 5

###### 158

-

9

Coast

terms of the mean (zero)flow U,it is convenient to define a factorn suchthat

nrzx(49 = Tzx(49 - L4-h)

###### or

n = 1 -~Tzx(-h) (5.95)

###### L(49

This factor, which lumps the effect of the bottom friction in with the wind shear stress, is greater than 1, as the bottom shear stress in our convention (Figure2.4)is negative. Typical values are n = 1.15to 1.30(ShoreProtection

Manual, 1977).

The equation is now

(5.96)

- Example 5.3


Calculate the wind setup due to a constant and uniform wind (t, is not a function ofx) blowingover a continental shelf of width 1.Assume (a) that the depth is a constant, ho; and (b) that h is linearly varying, h = ho(1 -x/l).

Solution. Tobegin, the governing equation can be written as

(a) Sincehoisnot a function of x,



---PAGE-175---



Sec.5.9 Storm Surge 159

Solving givesus

###### 2nrWxx Pg

(ho+q)’ =~ +c

To evaluate the constant of integration, we require the setup to be zero at x = 0.This condition arises from the fact that where h is very large, there is no surface gradient (why?)and thus no setup in deep water. After substitution for C,we have

or

- (5.97a)
- (5.97b) whereA =nr,,l/pgh;, a ratio of shear to hydrostatic forces.


In dimensionless form, q is

(b)Fora slopingbottom, the governing equation, Eq. (5.96), can be rewritten as d(h + 49 dh n r ,

(h+q)-- -(h+q)-=-

- (5.98)

or, in dimensionless form,

- (5.99b)


dx dx. Pg

where dhldx =-ho/l, a constant. Separation of variables leads to

###### -

with A again defined as nr,J/pgh;. Solvingyields

###### x+C=l[(1-~hh+oq) - A Cn(y -A)]

Evaluating Cas before, we have

\ 1 - A

. ..

These two solutions [Eqs. (5.99b) and (5.97b)lare plotted in Figure 5.12 to show the effect ofthe bottom slopeon the storm surge. Clearly, the sloping



---PAGE-176---



0 0.2 0.4 0.6 0.8 1.o x11

Figure 5.12 Dimensionless storm surge versus dimensionlessdistanceofa continental shelffortwo casesofdimensionless wind shear stress.

bottom causes an increasein the storm surge height; this can be explainedby referring to Eq. (5.96), which indicates that for a given wind stress, the water surface slope depends on the local water depth in such a way that the shallower the depth, the greater the slope. In Figure 5.13, the storm surge at the coast(x/l= 1)is shownfora sloping shelf as a function of the dimensionless onshore shear stress. The solution for x/l is usually obtained for given values of (h +q)/ho.However, to obtain (h +q)/hodirectly for a given x/l value, then it is usually more convenient to solve the equation iteratively for (h +q)/ho.The Newton-Raphson technique works wellhere.

The solution of Eqs. (5.99) isgenerallynot computed forx shorewardof the shoreline (x/Z = 1); however, it is often useful to determine backshore inundation (i.e., when h is negative).This can be done with this equation up to the point where

At this point the water surface slope is equal to the bottom slope [from Eq. (5.98)] and a uniform steady surge is reached, analogous to steady open



---PAGE-177---



###### Sec. 5.9 StormSurge 161

- 1.o 7

5

4

3

- 2

0.10

7

5

4

- 3


h+q

h0

- 2

0.010

7

5

4

- 3 2


0.001 2 3 4 5 6 7 0 . 0 1 0 2 3 4 5 6 7 0 . 1 0 2 3 4 5 6 7 1.0

nr,,, C O S O I

A = ____

Pgk;

Figure5.13 Storm tide forx// = 1.0for a slopingshelf.For the caseof no Coriolis force, the ordinateisequal to q/ho,the storm surge at the coast, ash =0atx// = 1.

channel flow, in the sensethat the downstream component of fluid weight is supported by the surface and bottom shear stresses. In a practical problem, the backshore region terminates in a wall or else significant flooding can occur.

5.9.1 BathystrophicStormTide

For large-scale systems the influence of the Coriolis forces cannot be neglected. If the wind blows at an angle 8to the coast, such that a longshore current is generated, then if the current is moving in such a direction that the coastline is to the right (in the northern hemisphere), the Coriolis force requires a balancing hydrostatic gradient, as in the Kelvin wave. This gradient addstothe surface gradient inducedby the wind. If the wind were blowing in the opposite direction, of course, the Coriolis forces would reduce the



---PAGE-178---



surge; however, large storms, such as hurricanes (due to their circular wind patterns), will induce longshore flows in both directions.

The analytical solution will be developed for a wind that begins abruptly at t = 0, with a magnitude W and a direction 8. To simplify the problem, we will assume that (a) the onshore flow and the return flows are continually in balance, sothat U =0 for all times, and (b) the wind system is uniform, so that there is no variability in the y direction. Assumption (a) is not always true, asa certain amount of water must flow into the shelf region to generate the surge. For these conditions the equations of motion in the x andy directions are

(5.100)

###### y: --d V - 7 w , - Ly(-h)- ZW”

fv’ (5.101)

at P(h + rl) P(h + 7) 8(h+ tl)

where a Darcy-Weisbach friction factorfis introduced for the bottom shear stress in the y direction. If we now consider q <<h, we can solve the last equation:

where k is defined in Eqs. (5.92) and (5.93). The longshore velocity increases from V =0at t = 0 to the steady-state value of

v s =vF (5.103)

8k sin 8

for t = co.Effectively, the time to steady state is determined by setting the V argument of the hyperbolic tangent to n (tanh 7c=0.996) or

- (5.104)
- (5.105)


Solving for t, we get

###### nh

t =

The time to steady state varies with the depth, with the shallowerdepths reaching the terminal velocity more rapidly than the offshore regions.As an example, forh = 10m and W = 20 m/s, about 8 h is necessary for steady state to be reached. At this time, Eq. (5.103) shows that V,is about 3%of the wind speed.



---PAGE-179---



Sec. 5.10 Long Waves Forcedby a Moving Atmospheric PressureDisturbance 163

If V is now introduced into the x-momentum equation,

(h+q)[~d(h+ q )--dh-f-cVstanht/

(5.106) where

###### dx dx g

-I*--(1--hi:) - A * hTi1--A*]A* (5.107)

Again solving by separation of variables yields

h + V

where

and

- (5.108a)
- (5.108b) for large t.


or

This solution in dimensionless form is exactly the same as the solution for a surge over a sloping beach without the Coriolis terms except that I is replaced by I*, and we see that the Coriolis force simply serves to “modify” the bottom slope.

The effect of wind angle becomes important in this problem as 7w,is important for the direct wind stress component of the surge, while T~~ is important for the Coriolis force contribution. Figure 5.14 shows the effect of wind angle for the setup at the shoreline at x= I.

###### 5.10 LONG WAVES FORCED BY A MOVING ATMOSPHERIC PRESSURE DISTURBANCE

Consider the case of an atmospheric pressure disturbance po moving with speed U in the positive xdirection:

po =flu-x) (5.109)



---PAGE-180---



###### 164 LongWaves Chap. 5

0.10

###### 0.09

0.08 0.07

-h +q

ho 0.05

0.04

0.03

0.02

0.01

I I I I I I I I \ 0 10" 20" 30" 40" 50" 60" 70" 80" 90"

Figure5.14 Maximum storm surge at x = I from the bathystrophic storm tide.

where the parentheses indicate a functional relationship. The governing equations include the momentum and continuity equations. The linearized momentum equation is

(5.110)

The continuity equation will be developed by selectinga coordinate system moving with the wave that renders the system stationary with a horizontal velocity component u - U. Realizing that the discharge Q past any given point is invariant and that the wave-induced particle velocityisproportional to the water surface displacement,

or

- (5.111)
- (5.112)
- (5.113)


which has been linearized. Assumingr,~ofthe form

v = G ( U t - x )

it is clear that

###### !!I=-,-a?

at ax



---PAGE-181---



Sec. 5.10 Long Waves Forcedby a Moving Atmospheric Pressure Disturbance 165

and combiningEqs. (5.109), (5.110), (5.112), and (5.113), we get

which is an exaCt differential and can be integrated from a location from where both r] andPOare nonexistent to

-=-tt PolP

(5.1 14)

###### h U 2 - g h

FromEq.(5.114),it is seen that for a static condition,q,= -po/pg, whereas for cases in which the speed of translation approaches that of a long free wave (C= @)there is an amplification which becomes unbounded due to the lack of any damping teFms. Moreover, when U < C,the pressure and displacement are exactly o h of phase, whereas for U > C,the two are in phase. For values of U >> C,the response approaches zero as the time interval over which the forceis appliedisnot sufficient forthe liquid to respond.The solid line in Figure 5.15 presents the amplification factor 1r,~I/IrlSI for no damping

1 2 3 4 5

UIC

###### Figure 5.15 Dynamic response of translating pressure disturbance, with and without friction.



---PAGE-182---



166 LongWaves Chap. 5

in which qsis the static water displacement for a pressure anomaly,

;Pol

(5.115)

l r l s l =-

Pg

It is noted that the effect of friction is to reduce the maximum amplification dueto a finite value as shown by the dashed line in Figure 5.14; see also Problem 5.19.

Finally, it is noted that the “forcing function” present in Eq. (5.109) could have been generalizedto include the surface shear stress.

5.11 LONG WAVES FORCED BY A TRANSLATING

BOTTOM DISPLACEMENT

A displacement of the bottom qo,which translates at speed U,will cause an associated surface displacement, much as in the case for a moving pressure displacement discussed in the preceding section. In this case, the linearized momentum equation is simply

(5.116)

where qIand qopertain to the air-water and bottom interface displacements, respectively, given by the forms

rlo=fo (Ut-x) r l l =fi (Ut -x)

(5.1 17a)

- (5.117b)

The continuity equation can be determined in the same manner as before:

- (5.118)


U(?I -v o )

Wrll - rlo) h + (111 - rlo)

U = ?=

h

CombiningEqs.(5.116), (5.117),and (5.118), the followingexact differen-

tial results:

- (5.119)
- (5.120)


or

###### U2

r l l = rlo-

U2-gh which, as in the previous case, increases without bound as U approaches the speed, C (= @)of a long free wave. For U =0, of course, there is no upper surface displacement and for large U, the upper surface displacement r l ~ approaches the lower surface displacementVO.The latter can be interpreted as due to the bottom motions occurring so rapidly that the upper surface does



---PAGE-183---



Chap.5 Problems 167

###### not have time to respond laterally (i.e., for the liquid to be mobilized in the horizontaldirection).

REFERENCES DEAN,R. G., “LongWave Modificationby LinearTransitions,”J.WaterwaysHarbors FREEMAN,J. C., L. BAER,and G. H. JUNG,“ The Bathystrophic StormTide,” J. Mar: HILALY,N., “Water Waves over a Rectangular Channel through aReef,” J. Waterways HINWOOD,J. B., and I. G. WALLIS,“Classification of Models of Tidal Waters,” .J. HINWOOD,J. B., and I. G.WALLIS,“Review of Models ofTidalWaters,” J.Hydraulics LAMB,H., Hydrodynamics, 6th ed., Dover, NewYork, 1945. LORENTZ,H. A., “Verslag Staatscommissie Zuiderzee 1918- 1926,” Staatsdrukkerij,

Div., ASCE,Vol. 90, No. WW1, pp. 1-29,1964. Res., Vol. 16, No. 1,1957. Harbors Div., ASCE,Vol. 95, No.WW1, pp. 77-94, Feb. 1969. HydraulicsDiv., ASCE,Vol. 101, No. HYlO, pp. 1315-1331, Oct. 1975a. Div., ASCE,Vol. 101, No. HYll, pp. 1405-1421, Nov. 1975b.

The Hague, The Netherlands, 1926.

PLATZMAN,G.W., “Ocean Tides and Related Waves,” in Lectures in Applied Mathematics, Vol. 14, Pt. 2, W. H. Reid, ed., American Mathematical Society, Providence, R.I., 1971.

PROUDMAN,J., Dynamical Oceanography, Wiley, NewYork, 1953,p. 239. SHIAU,J., and R. R. RUMER,Jr., “Decay of Mass Oscillations in Rectangular Basins,” STOKES,G. G., “On the Effects of the Internal Friction of Fluids on the Motion of TAYLORS,i r G., 11,Proc. Lond. Math. Soc. (2),Vol. 20, p. 148 (1920). THOMSON,W. (Lord Kelvin), “On Gravitational Oscillations of RotatingWater,” Proc. U.S. Army, Coastal Engineering Research Center, Shore Protection Manual, U.S. VAN DORN,W. C., “Wind Stress on an Artificial Pond,” J. Mar:Rex, Vol. 12, 1953. WILSON,B. S., in Encyclopedia of Oceanography, R. W. Fairbridge, ed., Academic WILSON,B. S., “Seiches,” in Advances in Hydroscience, Ven Te Chow, ed., Vol. 8, WU,J., “Wind Stress and Surface Roughness at Sea Interface,” J. Geophys. Res., Vol.

J.Hydraulics Div., ASCE,Vol. 100,No. HY1, Jan. 1974. Pendulums,” Trans. Camb. Philos. Soc.,Vol. 9,No. 8, 1851.

Roy. SOC.Edin.,Vol. 10,1879, p. 92. Government Printing Office, Washington, D.C., 1977.

Press, NewYork, 1966. Academic Press, NewYork, 1972. 74, pp. 444-453,1969.

###### PROBLEMS

5.1 Compare the fundamental periods of seiching for a long narrow basin with length 1 km and maximum depth of 10m, if its bottom is flat or sloped. Explain the differences.



---PAGE-184---



168 LongWaves Chap.5

- 5.2
- 5.3
- 5.4
- 5.5
- 5.6
- 5.7
- 5.8
- 5.9

Making reasonable assumptions, calculate the time necessary for the seiching in Problem 5.1 to reduce to 10%of the original value.

Determine the water surface elevation of a long standing wave in an estuary with linearly increasing depth and constant width. What assumptions have been made?h =ho at x = I, the mouth of the estuary.

Show that a linearized equation for seiching in two dimensions would be

With this equation, determine the seiching periods in a rectangular basin of length I and width b with constant depth h. Verify that long wave reflection from an abrupt step conserves the flux of wave energy. An edge wave is a progressive wave that propagates parallel to a coast. For a sloping beach given by h = mx, show that

t l = Ae-*&L, (21,~)cos (Any- of)

is a solution where L, (21,~)is the Laguerre polynomial oforder n and A, and o are related by 2 =gA, (2n + 1)m.

A large dock extends from above the free surface down to a depth d.Assuming long waves and that the dock is rigid, calculate the reflection and transmission coefficients for the dock, which has a width of 1.

Determine the Kelvin wave in a long narrow canal with bottom friction.

Develop the condition for the constant of integration C for the case of a storm surge in a closed basin of constant depth ho. A numerical solution will be necessary.

- 5.10 Calculate an equation for the “blow-down’’ on a sloping continental shelf of width I due to a strong directly offshore wind. Determine the location of the mean water line.
- 5.11 Show from the continuity equation, Eq. (5.6), that the vertical velocity W(z) under a long wave varies linearly with depth and can be expressed as

W(z)=-+(q-z)Dtl Dt

if U and Vare assumed to be independent of depth.

- 5.12 Determine the seiching period of a circular tank of radius a. Use the wave equation in cylindrical form and find only the first mode, which has a cos 0 dependency (Lamb, 1945).Compare your results to reality by shaking a coffee cup.
- 5.13 Compare the transmission coefficient determined in the abrupt step problem to the one calculated by Green’s law. Account for the differences.
- 5.14 Develop an equation for the ratio R of kinetic energy in the horizontal component of water particle velocity to the total ‘kineticenergy. Solve for the shallow and deep water asymptotes. Plot this ratio versus h/&.




---PAGE-185---



Chap. 5 Problems 169

- 5.15 For a bay of uniform depth and pie-shaped plan form as discussed in Example 5.1, develop an expression for the ratio R,

as determined by Green’s law and the complete solution, Eq. (5.39b). Plot and discuss the ratio R for the case of I/L = 10 and I/L = 2.

- 5.16 Which continental shelf configuration allows the greatest storm surges at the coast: (a)shelf width lo; maximum depth ho;(b) shelf width II (> lo), same maximum depth ho;or (c) shelf width II (> lo), maximum depth hl (> ho)but with bottom slope (ho/lo)?Verify your answer for hl = 5ho,I I = 510,and A (for case a) = 0.05.
- 5.17 Show that the storm surge for a continental shelf modeled as h =ho [1 - (x/l)]’ can be approximated by

(Note:There is another possible solution to the linearized problem; however, it gives infinite surge heights at x = 1.)

- 5.18 Show that the governing linearized momentum equation for long waves forced by an atmospheric pressure anomaly with linear friction present is


and that the solution depends on the wave number (k)of the forcing disturbance and that the solution in terms of the ratio of the modulus of the dynamic to static water surface displacements is

###### I Idyn = 1 IFda)Istat J(U2/gh- 1)’ +(AU/khgh)’

[Note:There are at least two ways of approaching this problem. One is to represent the traveling pressure and water surface displacements aq

p =PR cos (at-kx) v =NRcos(at -kx -a)

and tosubstitutethese in the governing equation above and solveforN Rand a. The second (equivalent) method is to represent p and v as Fourier integrals

tl(x,t )=~ s“F,, da

-m

in which Fp(a)and Fq(a)are complex amplitude spectra (i.e., they contain phases). The latter approach is the simpler of the two, algebraically.]



---PAGE-186---



###### Wavemaker Theory

Dedication

###### SIR THOMAS HENRY HAVELOCK

Sir Thomas Henry Havelock (1877-1968) pursued a variety of water wave areas, including ship wave problemsandthe generationof waves by wavemakers, the subject of this chapter.

Havelock was born in Newscastle upon Tyne. He obtained his education at Armstrong College, University of Durham, and St. Johns College, University of Cambridge. Returning to Durham, he became a lecturer and then professorof mathematics. He received knighthoodfor his scientific works in 1957 and accepted honorary doctorates from Universityof Durham and Universityof Hamburg. He received the first William Froude Gold Medal in 1956 for his work in naval architecture.

Havelockwas a Fellowof the Royal Society anda corresponding memberof theAcademy of Science, Paris.

###### 6.1 INTRODUCTION

To date most laboratory testingoffloatingor bottom-mounted structuresand studies of beach profiles and other related phenomena have utilized wave tanks, which are usually characterized as long, narrow enclosures with a wavemaker of some kind at one end; however, circular beaches have been proposed for littoral drift studies and a spiral wavemaker has been used (Dalrymple and Dean, 1972). For all of these tests, the wavemaker is very important. The wave motion that it induces and its power requirements can be determined reasonably well from linear wave theory.

Wavemakers are, in fact, more ubiquitous than one would expect. Earthquake excitation of the seafloor or human-made structures causes

170



---PAGE-187---



- Sec. 6.2 SimplifiedTheory for Plane Wavemakers in Shallow Water 171


waves which can be estimated by wavemaker theory; in fact, the loading on the structures can be determined (see Chapter 8).Any moving body in a fluid with a free surfacewill produce waves: ducks, boats, and soon.

- 6.2 SlMPLlFlED THEORY FOR PLANE WAVEMAKERS IN SHALLOW WATER


In shallow water, a simpletheory for the generation of waves by wavemakers was proposed by Galvin (1964),who reasoned that the water displaced by the wavemaker should be equal to the crest volume of the propagating wave form. For example, consider a piston wavemaker with a stroke S which is constant over a depth h.The volume ofwater displaced over a whole stroke is

###### LL’*

Sh (see Figure6.1).The volume of water in a wave crest is (H/2)sinkxdx

=H/k. Equating the two volumes,

k ,(,I22271

###### S h = - = - - -

in which the 2/71 factor represents the ratio of the shaded area to the area of the enclosing rectangle (i.e., an area factor). This equation can also be expressed

where H/S is the height-to-stroke ratio. This relationship is valid in the shallow water region, kh <71/10. For a flapwavemaker, hinged at the bottom, the volume of water displacedby the wavemaker would be less by a factor of 2.

These two relationships are shown as the straight dashed lines in Figure 6.2.

Figure6.1 Simplifiedshallow water piston-type wavemaker theory ofGalvin.



---PAGE-188---



###### -S

H

###### Flap type -

0 1 2 3 4 5 6

kPh

Figure 6.2 Plane wavemaker theory.Wave height to stroke ratios versus relative depths. Pistonand flaptype wavemaker motions.

Another type of wavemaker is the plunger wavemaker.This couldbe, as an example, a horizontal cylinder moving vertically about the mean water level. If the cylinder has a radiusR and a strokeR, then the cylinder position ranges from fully emerged to half submerged at full stroke. If waves are generated in each direction normal to the cylinder axis, then for shallow water conditions the wave height-to-strokeratio can be easily shown to be

###### 6.3 COMPLETEWAVEMAKER THEORY FOR PLANE WAVES PRODUCEDBY A PADDLE

The boundary value problem for the wavemaker in a wave tank follows directly from the boundary value problem for two-dimensional waves propagating in an incompressible, irrotational fluid, as in Chapter 3. For the geometry depicted in Figure 6.1, the governing equation for the velocity potential isthe Laplace equation,

-+-=()a2+ a2+

ax2 az2



---PAGE-189---



- Sec. 6.3 Complete Wavemaker Theory for Plane Waves Producedby a Paddle 173


The linearized forms of the dynamic and kinematic free surface boundary conditions are the same as before.

The bottom boundary condition is the usual no-flow condition

###### a4-0, z=-h

az

The only conditions that changeare the lateral boundary conditions. In the positive x direction, as x becomes large, we require that the waves be outwardly propagating, imposing the radiation boundary condition (Sommerfeld, 1964). At x =0, a kinematic condition must be satisfied on the wavemaker. If S(z) is the stroke of the wavemaker, its horizontal displacement is described as

x=- sin at

###### 2

where ais the wavemaker frequency. The function that describes the surfaceof the wavemaker is

F(x, z, t) =x --S(z)sin at =0

2

The general kinematic boundary condition is Eq. (3.6).

(6.10)

whereu=ui +wk andn =VF/IV FI.Substituting forF(x,z, t) yields

w dS(z) . 2 dz 2

###### u

sin at =-acos at on F(x,z, t) = 0 (6.11)

For small displacements S(z) and small velocities, we can linearize this equation by neglecting the second term on the left-hand side.

As at the free surface, it is convenient to express the condition at the moving lateral boundary in terms of its mean position,x =0.To do this we expand the condition in a truncated Taylor series.

(6.12)



---PAGE-190---



Clearly,only the first term in the expansionis linear in u and S(z);the others aredropped, as they areassumed to be very small. Therefore, the final lateral boundary condition is

u(0,2, t )=32acosrst (6.13)

2

Now that the boundary value problem is specified, all the possible solutions to the Laplace equation are examined as possible solutions to determine those that satisfy the boundary conditions. Referring back to Table 3.1, the following general velocity potential, which satisfies the bottom boundary condition, is presented.

&x, z,t )= Apcosh kp(h+z)sin(k+ -at)+(Ax+B) (6.14) +CfkJcosk,(h +z)cosrst

The subscripts on k indicate that that portion of q4 is associated with a progressiveor a standingwave. For the wavemaker problem,A must be zero, as there is no uniform flow possible through the wavemaker and B can be set to zero without affectingthe velocity field. The remaining terms must satisfy the two linearized free surface boundary conditions. It is often useful to employ the combined linear free surface boundary condition, made up of both conditions.This condition is

(6.15)

which can be obtained by eliminating the free surface q from Eqs. (6.5) and (6.6). Substitutingour assumed solution into this condition yields

tf =gk, tanh kJz (6.16) and

d=-gks tan k,h (6.17)

The first equation is the dispersion relationship for progressive waves, as obtained in Chapter 3, while the second relationship, which relates k, to the frequency of the wavemaker, determines the wave numbers for standing waves with amplitudes that decrease exponentially with distance from the wavemaker. Rewriting the last equation as

###### d h

###### -=-tan k,h gksh

###### (6.18)

the solutions to this equationcan be shown in graphical form (seeFigure6.3).

Thereareclearly an infinite numberof solutions to this equation and all are possible. Each solution will be denoted asks(n),where n is an integer.The



---PAGE-191---



###### Sec. 6.3 Complete Wavemaker Theoryfor Plane Waves Producedbya Paddle 175

-0.5

Figure 6.3 Graphical representationof the dispersion relationshipfor the standing wave modes, showingthreeofthe infinite numbersofroots,ks(n).Here,dh/g

=1.0.

final form for the boundary value problem is proposed as

###### 4 =A, cosh k, (h +z) sin ( k g-at) (6.19) Cne-ks(n'cos[k,(n)(h+z)] cosat

m

###### +

n-1

Again, the first term represents a progressivewave, made by the wavemaker, while the second series of waves are standing waves which decay away from the wavemaker. To determine how rapidly the exponential standing waves decrease in the x direction, let us examine the first term in the series, which decays the least rapidly. The quantityk,(l)h,from Figure 6.3, must be greater than n/2,but for conservative reasons, say k,(l)h= n/2, therefore, the decay of standing wave height is greater than e-(d2Xx/h).For x = 2h, e-("'2xx/h)=0-04 , for x = 3h, it is equal to 0.009. Therefore, the first term in the series is virtually negligible two to three water depths away from the wavemaker.

For a complete solution,A, and the Cn'sneed to be determined. These are evaluatedby the lateral boundary condition at the wavemaker.

u(0,z, t ) =-S(Z) a4

0 cos at =--(0, z, t ) 2 ax

=-A&, cash k,(h +Z ) cosat

+cC,k,(n)cos[k,(n)(h+z)] cosat

- m
- n-1


or



---PAGE-192---



176 Wavemaker Theory Chap. 6

Now we have a function of z equal to a series of trigonometric functions of z on the right-hand side, similar to the situation for the Fourier series. In fact, the set of functions, (cosh k,(h +z), cos [k,(n)(h+z)],n = 1, co) form a complete harmonic series of orthogonal functions and thus any continuous function can be expanded in terms of them.' Therefore, to find A,, the equation above is multiplied bycosh k,(h +z )and integrated from -h to 0. Due to the orthogonality property of these functions there is no contribution from the seriesterms and therefore

-1: acoshk,(h+z )dz

kp1;cosh'kp(h+z)dz

A, = -

(6.21)

MultiplyingEq.(6.20)bycos{k,(rn)(h+z)}and integrating over depth yields

:lF acos[k,(rn)(h+z)]dz

c,= r o (6.22)

###### k,(rn)J cos' [k,(m)(h+z)]dz

###### -h

Depending on the functional form of S(z), the coefficients are readily obtained. For the simple cases of piston and flap wavemakers, the S(z)are specified as

+El, flapmotion

piston motion

(6.23)

c

The wave height for the progressive wave is determined by evaluating q far from the wavemaker.

q=-- =-5acoshk,h cos( k-~at)

g at z=o g

= cos (k+ -at) x>>h

(6.24)

2

'This follows from the Sturm-Liouville theory. Proof of the orthogonality can be obtained by showingthat the integralsbelow are zero, that is,

JIcoshk,(h+z)cos[ks(n)(h+z)]dz=0 cos[k,(m)(h+z)]cos[k,(n)(h+z)]dz=0

form +n using the dispersion relation andEq. (6.17), Problem6.8.



---PAGE-193---



Sec. 6.3 Complete Wavemaker Theory for Plane Waves Producedbya Paddle 177

Substituting for A,, we can find the ratio of wave height to stroke as

H sinh kph kphsinh k,h -cosh k,h + 1, flapmotion (6.25)

###### -=4(S kph ) sinh2kph+2kph

H--- 2 (cash 2k,h - 1) S sinh 2kph+2k,h’

###### (6.26)

piston motion

In Figure 6.2, the wave height-to-stroke ratio is plotted for both flap and piston wavemaker motions for different water depths. This graph enables the rapid prediction of wave height given the stroke of the wavemaker. The reader is referred to Ursell et al. (1960)for further details.

The power required to generate these waves can be easily obtained by determining the energy flux away from the wavemaker.

###### P = ECn (6.27)

where E is proportional to the propagating wave height, as obtained from the preceding equation.The power necessary to generate waves in various water depths is shown in Figure 6.4. By examining Figures 6.2 and 6.4, it can be seen that togenerate a wave of the same height, in shallow water, itiseasier to generate it with a piston wavemaker motion, as the piston motion more closely resembles the water particle trajectories under the waves, while in deeper water, the flap generator is more efficient.

0.7t -I

###### 0 1 2 3 4 5

kPh

Figure 6.4 Dimensionless mean power as a function of water depth for piston and flap wavemakers.



---PAGE-194---



178 Wavemaker Theory Chap. 6

The wavemaker theory has been developed assuming both smallamplitude motions of the paddle and small wave heights. There are singificant nonlinear effects that occur when thc wavemaker moves with large displacements; in fact, the waves that result are of different size and shape at different locations away from the wavemaker (see, e.g., Madsen, 1971, and Flick and Guza, 1980).

6.3.1 PlanarWave Energy Absorbers

Energy may be removed from waves by moving paddles as well as added, as in the preceding section. One means to extract wave energy from waves under various conditions has been discussed by Milgram (1970).

The principle behind the wave absorber is that incident waves onto the paddle are absorbedby the paddle moving in a manner soas to be invisible to the waves. In other words, while in the wavemaking problem, the paddle is pushed forward to make a wave crest, in this case the paddle will move backward asa wave crest impinges onit (thusmaking waves on the other side of the paddle, if there is water), making it appear that the waves have passed through.

The most efficient absorption of the waves, of course, is dependent on moving the paddle in just the “right” motions, which can be determined theoretically. The mathematical formulation involves examining the waves on the opposite side of the paddle from the previous analysis. The velocity potential remains the same,except for thexdependency ofthestanding wave terms.

###### - Hg ‘Osh kP(h +’) ,.,in (kdc - at) incident - 20 cosh kph

(6.28)

(6. .

###### + 2 Cfle+k~(“bcos [k,(n)(h+z)]cosat

W

forx=sO dent wave.

fl=l

The value of wave absorber strokeS must be found for a given inc To do this we use the boundary condition at x =0.

cos at a(6

S(Z)O at x=O

(6.29)

u(2)= =--

2 ax

Following the same procedure as before, the same relationship and (6.26)] results for H/S.Therefore, for a given incident wavc stroke necessary to absorb the waves can be determined. There stiliare, of course, the standing waves that are set up to account for the fact that the paddle velocities do not exactly match those of the incident wave. In addition. the velocitv of the wavemaker motion must have exactlvthe same

Eqs. (6.25) height. the

I ,~ ~ . ~ ~.. _._._.___. _ _ _ _ .-._.__.._.- -..____.2 ---- ------

... .~ . ~ ~ . ~ ~ - - ~ -

phase as that of the horizontal velocity of the incoming wave.



---PAGE-195---



Sec. 6.3 Complete Wavemaker Theory for Plane Waves Producedby a Paddle 179

6.3.2 Three-Dimensional Wavemakers

The "snake" wavemaker. By using an articulated long wavemaker in a wave basin, it is possible to make waves propagating in different directions depending on the motion of the wavemaker. To study this case, consider a wavemaker located on the y axis, making waves that propagate in the x-y plane. For simplicity the wavemaker will be assumed to be infinitely long. The motion of the wavemaker at x = 0generatesvelocities in thexdirection, u(y,z; t), which in the simplest case may be written

u(y,z;t )= U(z)cos (Ay- at) on x= 0

###### (6.30)

This represents a horizontal velocity at the wavemaker which consists of periodic motion, propagating in the +y direction.

I-h<z<O

The boundary value problem which must be solved is

o<x<oo

a2+ a2+ a2+

-+-+-=O in - m < y < c o (6.31)

ax2 ay2 aZ2

At the horizontal bottom of the basin, the bottom boundary condition must be met. At the surface, the linearized kinematic and dynamic conditions apply, as before.

Using separation of variables a solution is assumed which satisfies the bottom boundary condition.

+=A, coshkp(h+z)sin( d v x-+Ay-at) (6.32) +5Cncos[k,(n)(h+z)]exp[ - J k m X]cos(Ay-at)

n=l

###### whered=gk, tanh k,h; d=-gk,(n) tan k,(n)h.

It can be shown, by examining all other possible solutions, that only this form provides for a propagating wave in the x direction with the usual cosh kp(h+z) depth dependency. Further, this imposes a restriction that kp3 A.

Invoking the wavemaker boundary condition atx =0, V(z)cos (Ay - at)= --

::Ix=o

(6.33)

=-A, Jv-coshk,(h+z)cos(Ay-at)

###### +5CnJWcos(k,(n)(h+z)Icos(Ay-at)

n=l



---PAGE-196---



180 Wavemaker Theory Chap. 6

/A

x

Figure6.5 Definitionfor 0.

Examining only the propagating mode (in the x direction), and utilizing the

4k,soU(z)coshkp(h+z)dz

orthogonal properties of (cosh k,(h + 2); cos [k,(n)(h + z)], n = 1 ,

2,. . . , 00, we have

###### A, = - -h (6.34)

###### ,/P(sinh2k,h +2k&)

which is nearly the same as before.

If we introduce a directional angle8made by the wave orthogonal to the x axis as in Figure 6.5, where A is the wave number in the y direction and

4- is the wavenumber in thex direction, we seethat k, represents the wavenumberinthepropagationdirection.Further, 4- =k,cos8andA = k, sin 8. This latter expression requires that the wavelength A of the wavemaker displacement be related to the desired wave angle. Substituting, the velocity potential of the propagating wave can be written

&(x, y , z;t )=A, cosh k,(h +z)cos((k,cos 8)x+(kpsin8)y-at) (6.35) where A, is given by Eq. 6.34and is related to the planar value [Eq.(6.21)]by (cos8)-'.To make waves in the opposite -8 direction, the wave displacement must propagate in the opposite direction

u(z,y ;t ) a cos (Ay+ at)

In order to generate a realistic sea state in a wave basin, numerous wavemakermotions can be superimposed due to the linearity of the problem.

###### 6.4 CYLINDRICAL WAVEMAKERS

Although not in common use, the wavemaker theory for water waves generated by moving vertical cylinders follows directly from plane wavemaker theory, the only exception being that the problem is worked in polar coordinates (see Chapter 2).

The fluid motion can be described by a velocity potential which is governed by the Laplace equation with the usual linearized free surface and bottom boundary conditions.

###### (6.36)



---PAGE-197---



Sec.6.4 Cylindrical Wavemakers 181

where r and 8are the polar coordinates of the horizontal plane.

###### (6.37)

Additionally, a radiation boundary condition is imposed at large r to ensure outgoing waves and a kinematic condition must be applied to the moving wall of the cylinder.

Thereareseveral possibilities for cylindrical wavemakers, which will be denoted by different types. Type I will be a vertical cylinder (located at r =0, with radius a)moving in piston orflap motion in a fixed vertical plane, taken as8= 0 or n.Applyinga kinematic condition that the fluid at the cylinder wall follows the cylinder’s motion, we have in linearized form

where Re( ) denotes real part,2m is an integer equal to unity and S(z)is the vertical variation of the displacement of the cylinder.TheType I1wavemaker is a pulsating cylinder, which expands and contracts radially with no 8 dependency.The corresponding linear kinematic condition is

with m =0. Finally, the Type I11 wavemaker is a spiral wavemaker discussed by Dalrymple and Dean (1972), who advocate its use in littoral drift studies. In a circular basin the spiral wavemaker generates waves which impinge on a circular beach everywhere at the same angle, thus resulting in an “infinite” beach ideal for sediment transport studies. [In some cases, the spiral wave shoals in a manner differently than plane waves (Mei, 1973).]The cylinder motion can be visualized by placing a pencil point down on a table and rotating the top in a small circular path. The linearized kinematic boundary condition becomes

where rn =1for the case of the rotating pencil, but could be greater than unity for a lobe-shaped cylinder.

###### *Seepage 190.



---PAGE-198---



182 Wavernaker Theory Chap. 6

The solution for the velocity potential is obtained by separation of variables, in the same manner asbefore (see Problem 6.9).The solutions that satisfy all the boundary conditions with the exception of the kinematic condition on the cylinder are

whereH$(k,r) is the Hankel function of the first kind, defined as H$(k,r) = J,(kpr)+ iY,(k,r), a complex number formed by the Bessel functions, and Krn(ks(n)r)is the modified Bessel function of the second kind.Associatedwith these solutionsarethe dispersion relationships relating the angular frequency to the wave number(s),

d =gk, tanh k,h and

###### 2 =-gks(n) tan k,(n)h, n = 1, 2,...,co (6.42)

The unknown coefficients in the series for the velocity potential are obtained by satisfying the remaining boundary condition at the cylindrical wall usingthe orthogonalityof the depth-dependent functions,with the result that

###### I:SOacoshk,(h+z)dz

2

A, = - m

- (6.43)
- (6.44)


###### k,[Hijtl(k4)]’J - cosh’ k,(h +z)dz

###### -h

and

c,=- m

The [.1’denotes the derivative with respect to the argument of the function. The coefficients A, and C, are. the same for all three types of cylinder wavemaker and are similar to the coefficients for the planar wavemaker, differing due to the presence of the derivative of a Bessel function in the denominator. These terms in the velocity potential account for the radial decay of the waves away from the wavemaker.



---PAGE-199---



Sec. 6.4 CylindricalWavemakers 183

Far from the wavemaker, the water surface displacement q may be determined from the linear dynamic free surfaceboundary condition andthe Hankel function term as the others become negligible several water depths from the wavemaker. Using the asymptotic form for the Hankel function,we

q(r,8,t)=ReI-iaA, coshk&

have I

###### (6.45)

I

###### I

###### 4

###### 4

ling the relations-ipbetween strokesS(z)andA, and the last equation, the wave height-to-strokeratio can be determined.This isshownin Figure6.6for

I

kPh

Figure 6.6 Dimensionless progressive wave amplitude evaluated at the cylinder for piston or circular motion of the wavemaker. rn = I. (From Dalrymple and Dean, 1972.)



---PAGE-200---



###### 184 Wavemaker Theory Chap. 6

I I I

I

Locus of cylinder axis

2.2

2.0

1.8

1.6

###### I .4

###### ;H 1.2 I.o

0.8

0.6

0.4

0.2

0 1.o 2.0 3.0 4.0 5.0

kPh

Figure 6.7 Dimensionless progressive wave amplitude evaluated at cylinder, sway motion. rn = 1. (From Dalrymple and Dean, 1972.)

the case of piston motion and Figure 6.7 for sway motion for Type I and I11 wavemakers(rn = 1).

Power requirements to generate these radial waves, energy flux,and the direction (for spiral waves) can be determined fairly simply; the reader is referred to the original paper by Dalrymple and Dean (1972) for details.

###### 6.5 PLUNGER WAVEMAKERS

Plunger wavemakers with a wedge-shaped cross section are often used in laboratories instead of piston or flap-type paddles. These wavemakers can be designed to generate waves in only one direction. For example, a wedge oscillating vertically as in Figure 6.6 would only generate waves in the positivex direction. For an immersed wedge making small vertical motions and for smallp,the linear theory is the same as that for piston wavemakers; for larger vertical strokesand for largep,aswell as for other shapes the reader is referred toWang(1974),who solved the plunger problem using a conformal



---PAGE-201---



Chap.6 Problems 185

###### I

Figure 6.8 Schematic of wedge-shaped plunger wavemakers.

transformation. Hepresents figuresofamplitude/stroke ratios versus dimensionless geometrical parameters for wedge-shaped wavemakers as shown in Figure 6.8.

###### REFERENCES

DALRYMPLE,R. A., and R. G. DEAN,“ The Spiral Wavemaker for Littoral Drift FLICK,R. E., and R. T. GUZA,“Paddle Generated Waves in Laboratory Channels,” J. GALVIN,C. J., Jr., “Wave-Height Prediction for Wave Generators in Shallow Water,” MADSEN,0.S., “On the Generation of Long Waves,” J. Geophys. Res.,Vol. 76,No. 36, MADSEN,0.S., “A Three-Dimensional Wavemaker, Its Theory and Application,” J. MEI, C. C., “Shoaling of Spiral Waves in a Circular Basin,” J. Geophys.Rex,Vol. 78, MILGRAM,J. H., “Active Water-Wave Absorbers,” J.Fluid Mech.,Vol. 43, Pt. 4,1970 SOMMERFELD,A., Mechanics ofDeformable Bodies,Vol. 2 of Lectures on Theoretical URSELL,E, R. G. DEAN,and Y. S.Yu, “Forced Small Amplitude Water Waves: A WANG,S., “Plunger-Type Wavemakers: Theory and Experiment,” J.Hydraulics Res.,

Studies,” Proc. 13th ConJ:Coastal Eng.,ASCE, 1972. Waterways, Ports, Coastal Ocean Div., ASCE,Vol. 106, Feb. 1980. Tech. Memo 4, U.S.Army, Coastal Engineering Research Center, Mar. 1964. 1971. Hydraulics Res., Vol. 12,No. 2, 1974. No. 6,1973.

Physics,Academic Press, NewYork, 1964. Comparison ofTheory and Experiment,” J. Fluid Mech.,Vol. 7, Pt.. 1,1960. Vol. 12, No. 3,1974.

###### PROBLEMS

- 6.1 A piston wavemaker operates over only halfthe water depth and oscillates with frequency CT and a maximum velocity U O . (a) Determine the wave height away from the wavemaker in terms of UOif the


wavemaker operates over the tophalfof the water column.



---PAGE-202---



186 Wavemaker Theory Chap. 6

- (b) An alternative design is to operate the wavemaker over the bottom half of the water column. Plot the ratio of wave heights (away from the wavemaker),Htop/Hbotlornas a function ofkh,whereH,,, indicates the wave height in part (a). Which wavemaker is more efficientand why?
- (c) Calculate the ratio H/S for shallow water using the simplified approach and compare with the results developed in parts (a) and (b).


- 6.2 Show, using the simplified shallow water approach, that the ratio of wave height near the cylinder towave height stroke for a vertical cylinder, oscillating vertically with a stroked and generating circular waves, is

H kR d 2

_ = _

where R is the radius of the cylinder.

- 6.3 What are the stroke and power necessary to generate a 2-s period 20-cm-high wave in 2 m of water for both flap and piston wavemakers.
- 6.4 A long rectangular barge with draft d in shallow water is heaving (moving vertically) with a velocity Vocos at. (a) Determine the amplitude ofthe wavesgeneratedby this motion if the barge (b) Determine the damping ofthebarge motion due towave generation. (Hint:
- 6.5 Determine the equations for instantaneous and mean power required for wavemakers using the wave-induced pressure on the wavemaker. Determine, for a wavemaker with a displacement ofS(z)=S coshk(h+z),the instantaneous and mean power required. Why might it be advantageous to incorporate a flywheelinto the generating mechanism?
- 6.6 Using conservation of energy flux, show how the waves due to a circular wavemaker (see Problem 6.2), would decay in height with radial distance.
- 6.7 Examine the energy flux at the wavemaker due to the progressiveand standing wave mode components. Discuss your results.
- 6.8 Show that the set (cosh k, (h +z), cos [ks(n)(h+z)], n = 1, 2,. .., a))are orthogonal over the range -h <z < 0, given the dispersion relationships for a, k,, and ks(n).
- 6.9 Develop the theory for waves made by a circular cylinder wavemaker with vertical axis moving in piston motion.
- 6.10 Develop dimensionless expressions for the maximum total forces on piston and flap-type wavemakers.
- 6.11 Develop the three-dimensional wavemaker theory for waves in a long wave tank. The side walls are located at 1y I =I, and the waves are made by a paddle with a mean position ofx =0, yet which varies in stroke over the vertical and acrossthe tank width (Madsen, 1974).


width is given. It is easiest to use energy arguments here.)



---PAGE-203---



Statistics and

###### ec

Dedication

###### LORD RAYLEIGH

John William Strutt (1842-1919), the third BaronRayleigh,for whom the Rayleigh probability distribution is named, received (with Sir William Ramsey)the Nobel Prizein 1905for the discovery of argon.

He was born in Langford Grove, Essex, England, and entered Trinity College, Cambridge, in 1861,becoming a Fellow in 1866.

Over his career, Rayleigh wrote 446 papers that ranged from his noted Treatise on the Theory of Sound, published in 1877, to works in electromagnetism and physical optics. These works have been collected in Scientific Papers. His research interests included electricity and psychic phenomena and theoretical/experimental work on the explanation of the sky’scolor.

In 1879he gained appointment as the second Cavendish Professor and in 1884 became the director of the Cavendish Laboratory at Cambridge University. In 1894 he retired from these positions to do research in his private laboratory in Terling Place, Witham, Essex, where he was Baron (after the death of his father in 1873).

In 1908 he becamethe Chancellor of Cambridge University.Rayleigh died in 1919and was buried in WestminsterAbbey.

###### 7.1 INTRODUCTION

Previous chapters have discussed waves that are monochromatic (i.e., they have only one frequency). (The term “monochromatic” derives from the analogy of water waves to light waves and the relation of color to frequency.) However, by simply lookingat the actual sea surface,one sees that the surface



---PAGE-204---



188 Wave Statistics andSpectra Chap. 7

is composed of a large variety of waves moving in different directions and with different frequencies, phases, and amplitudes. For an adequate description of the sea surface, then, a large number of waves must be superimposed to be realistic (as mentioned in Chapter 1). This chapter discusses the methods by which this is done and the characteristics of the sea surface.

###### 7.2 WAVE HEIGHT DISTRIBUTIONS

Designing in the ocean requires an adequate knowledge of possible wave heights. For example, in the design of a structure, the engineer may be faced with designing for the maximum expected wave height, the “highest possible” waves, or some other equivalent wave height. Historically, several wave heights have become popular as characterizing the sea state. These are the HII3(the significant wave height) and the H,,, wave heights. To envision what these definitions mean, consider a group ofN wave heights measured at a point. Ordering these waves from the largest to the smallest and assigningto them a number from 1to N,two statistical measures may be obtained. First, Hl,3is defined as the average of the first (highest) N /3 waves. Correspondingly, Hpwould be defined as the average of the first pN waves, with p < 1. (HIwould be the average wave height.) Second, the probability that the wave height is greater than orequal to an arbitrary wave heightfiis

P(N >A)=N where n is the number of waves higher than A.We note for later use that

###### P(H<fi)=1-n/N.

The root-mean-square wave height for our group of waves, H,,,, is defined as

which is always larger than H Iin a real sea.

7.2.1 Single Wave Train

It is clear that for the sea surface described by a single sinusoid wave, q(t)=(Ho/2)cos at,the waves are all of the same height and that Hp= HOfor anyp and H,,, =Ho.

7.2.2 Wave Groups

Tomake the sea surface somewhat more realistic, another wave train is added, with slightly different frequency, in order to make wave groups, aswas



---PAGE-205---



Sec. 7.2 Wave Height Distributions 189

done in Chapter 4.

q=5cos(Q -$)t +$cos(0+$)t

2

(7.3)

=Hocos at cos *t =H(t)cos at

2 2

which represents a propagating wave system evaluated at x =0.

The resulting wave system has a carrier wave at frequency a and a slowly modulated wave height 2H0cos(Aa/2)t(seeFigure4.12).Therefore, to examine the wave height distribution for the wave system, we need only to look at the envelope from t = 0 to n/Aa (or from the antinode to the first node).

To determine H,, we average the wave height envelope from t =0 to pn/Aa,since the wave heights decrease monotonically from the maximum to the minimum.

A0 2

H p = - 2Ho cos-t dt

(7.4)

Ho ' Pn Pn 2

H, =4- sin The rms wave height can be derived:

A0 2

H2rms =- J''Au 4Hi cos2-t dt

nlAa 0

or

Hrms =JZHO

We can therefore expressthe Hpwave height in terms ofH,,, which will be a more definable wave height for real seas.

Hp= 2JZHrmssinP-X

(7.7) and sinceH,,, must be equal to 2Ho,we have,' from Eq. (7.6),

PR 2

Example7.1

Awave group consistingoftwo sinusoidsofequal heightand slightly different periods isgeneratedin a laboratorywave tank and recordedby a fixed wave gage.What are the values ofH,,, Hlllo,HI/,,andHIin termsofHrmS?

'Alternatively,t hiscanbeobtainedfromEq.(7.7)asinthelimitasp-0.



---PAGE-206---



Wave Statistics and Spectra Chap. 7

190

Solution.

Hmax=JzH,, =1.414H-

###### Hiiio = 2oJz Hmssin = 1.408Hm,

n 20

7.2.3 Narrow-Banded Spectra: The Rayleigh

Distribution

For a more realistic case, we assume that the sea surface is composed of a large number of sinusoids, but with their frequencies near a common value, a.Thisisreferred to asa narrow-banded sea (in that all the frequenciesare in a narrow frequency band about a).Therefore, for M component frequencies

q(t)= cH-mcos(amt-Em)

- (7.9)
- (7.10)


m=l 2

or equivalently,in complex notation,2

r m=l2

The notation Re{.) refers to taking only the real part, Re(e'"') = cos at. Factoring out the carrier wave of frequency ayields

I

tt(t)=Re p5L!iei~(~m-~)~-~ml

(7.11) Again, to define the wave height distribution, we need only to examine

the statistics of the slowly varying envelope, B(t):

B(t)=5H,eIl(um-u)l-€ml

(7.12)

m=l 2

*Fromcomplexvariabletheory,e'" =cosc7t +i sinat,where i = G.Theseformulascan be

readily derivedif we expressemasa Maclaurin series.

(ix)* (1x1~( i ~ ) ~ & " = l + i x + - + - + -

2! 3! 4!

=(1 -2+ g ...)+i(x --x3+...

1

2! 4! 3!

The termsin the two sets oflarge parentheses are the power series expansionfor cosineand sine.



---PAGE-207---



Sec. 7.2 Wave Height Distributions 191

From statistical theory, it can be shown (e.g., Longuet-Higgins, 1952)

that if the individual components of B are statistically independent and a large number M is used, then the probability of the wave heightbeing greater than or equal to an arbitrary wave height(A)is given by

P(H > A)= e-(fi/Hrrn# (7.13)

This theoretical probability can be compared to our rank-ordered group which is called the Rayleigh distribution. of waves, N, Eq. (7.1):

###### - n

P ( H a H )=-

(7.14)

###### N

or equating,

(7.15)

This expression provides a means to determine the number of waves out of the total number N which have a height greater than or equal to a certain

heightfi whichH.isAlternatively,exceeded bywen canwavessolvein ourthis groupexpressionof N.toBydeterminetaking thethenaturalheight

logarithms of both sides, we find that

###### fi=H r m S E

- (7.16)
- (7.17)


H=HrmsK

The height that is exceededby pN of the waves is therefore

Example 7.2

At a pier inAtlantic City, New Jersey,400consecutive wave heights are measured. The H,,, is determined by Eq. (7.2).(a) Assuming that the sea state is narrow-banded, determine how many waves are expected to exceed H = 2H,,,. (b) What height is exceeded by half the waves? (c)What height isexceeded by only one wave?

Solution.

- (a)To answer the first part, Eq. (7.15)isused.

=Ne-(2)’

= 7.3 N 7 waves Approximately seven waves, less than 2% of the total number, exceed 2Hr,,.

- (b)The height H exceeded by half the waves (n =N/2,orp = I) is


###### H = H,,, = 0.833Hms



---PAGE-208---



192 Wave Statistics and Spectra Chap. 7

For H ~ , Nwe have p = 1/N or HIIN= K N H,, = 2.45Hr,,. It is perhaps not too surprising that the more waves present in the group (i.e., large N), the higher the maximum wave willbe.This is due to the fact that the Rayleigh probability function decays asymptotically to zero for large H, but never reaches zero. Thus all wave heights are statisticallybut not necessarilyphysically possible.

7.2.4 The Rayleigh Probability Density Function

The wave height probability density function fH follows from the Rayleigh probability distributionP(H < Z?):

Thisfunction is plotted in Figure7.1.Maximizingwith respect toHyieldsthe maximum probability for &/HrmS= 1/4,or the most frequent wave is H = 0.707Hm,.

From statistical theory we can obtain important relationships using the distribution function for the wave height.

The mean wave height is defined as

-_- &HrmS=O.886Hm,

(7.19)

2

To find the average height of the highestpN waves, we first recall that

0 1.o 2.0

H I H m

Figure 7.1

The Rayleigh probability distribution function. The area under the

curve is unity.



---PAGE-209---



Sec. 7.3 The Wave Spectrum 193

the heightfiexceeded by the pN waves is

Next,

- (7.20)
- (7.21)


where x is a dummy variable. Integrating by parts, we get

where erfc ( x )is the complementary error function (see Abramowitz and Stegun, 1965).

InTable 7.1 various values ofHp/Hrmsare presented. It is clear that asp becomes smaller, there is a significant change from the results obtained by the simple wave group model (see Example 7.1).

TABLE 7.1 Relationship of Hpto H,,, using the Rayleigh Distribution

Forristall(l978) has shown that for real seasof large magnitude, the Rayleigh distribution tends to overpredict the larger wave heights. This is presumably due to the breaking phenomenon “trimming” these larger heights.

###### 7.3 THE WAVE SPECTRUM

The waves recorded at a wave staffgenerally are composed of components of many frequenciesa, and amplitudes a, with different phasesE,:

cc

###### q(t)= 2a, cos(ant-E,)

(7.22)

n=O



---PAGE-210---



194 Wave Statistics and Spectra Chap. 7

###### t t- t t

U

U U

0

Energy spectrum

Amplitude spectrum

Energy density Continuous amplitude spectrum spectrum

Figure 7.2 (a)Typesofspectra;(b)broad versusnarrow-banded energy spectrum.

If the amplitudes a,, are plotted versus frequency,an amplitude spectrum results. More commonly used, however, is the energy spectrum, which is a plot of af. Both of these spectra are line or discrete spectra in that each frequency component is discrete.The energy density spectrum, on the other hand, is a plot ofai/Aoversusa,which is more popular, as the area under the curve is a measure of the total energy in the wave field. It is more likely in nature that the spectrum be comprised of a continuous range of frequencies

or

~(t=)Re[Lma(o)~?["-I'~)~do} (7.23)

where a(a)do is the amplitude of each wave and a(@might be called the amplitude density function. Examples of these spectra are shown in Figure 7.2a. The shape of the spectrum varies with the types of seasand whether it is broad- or narrow-banded (Figure 7.2b).

7.3.1 Spectral Analysis

The procedure of extracting spectra from wave records is an evolving field and a complete presentation of spectral analysisis beyond the scope of this book. However, some rudimentary aspects of it will be discussed. Of primary importance is the fact that the use of computers in time-series analysis has made it far more convenient to deal with digitized data3and spectral analysis is usually done by the fast Fourier transform (FFT) tech-

'The time seriesof q(t)digitizedat an interval of At is the sequenceof numbers:q(At), q(2 At), rj(3 At),and so on.



---PAGE-211---



Sec. 7.3 The Wave Spectrum 195

nique, popularized by Cooley andTukey (1965).It should be noted parenthetically that almost all our knowledge about spectral analysis comes to the ocean engineers via the electronic and communications fields.

7.3.2 Fourier Analysis

The basis for spectral analysis is the Fourier series, named for Joseph Fourier (1768-1830). The premise of Fourier analysis follows from the fact that any (piecewise continuous) function JTt)can be represented over an interval of time (tto t + T)as a sum of sines and cosines, wheret is arbitrary andJTt)is assumed to be (or is) periodic over the time period, T. The Fourier series is written as

m

A t )= C (a,cos not +b, sin not) (7.24)

n=O

where o= 2z/T and bo= 0 as sin (0) = 0, and uois simply the mean of the record. The coefficients a, and b, can be obtained by minimizing the mean

###### E=16"'[At)-C(a,cosnot+b,sinnot) dt

squared error of the function E, which is defined as

I'

m

(7.25)

T n=O Minimizing yields

- (7.26a)
- (7.26b)


Expressing these equations fully, we have

1

J'+'[JTt) -2(uncosnot+b,sinnot) cosmotdt=0

m

I

m

###### LltT[At)-z ( a ncos not + b, sin not) sin mot dt =0

Using the following orthogonality properties of the trigonometric functions:

T/2 m = n + O

sin not sin mot dt = [o, m+n

6"'sinnotcosmotdt=0

###### m = n = O cos not cos mot dt =:



---PAGE-212---



196 Wave Statisticsand Spectra Chap. 7

and carrying out the integration following from Eqs. (7.26b),we obtain a0 =-Jrirfit) dt

- a,=2.rTAt)cosnotdt
- b, =2J'+'flt) sin not dt


- (7.27a)
- (7.27b) (7.27~)


###### T

for n = 1, 2,...,cc for n = 1, 2,.. .,co

T

###### T

Example 7.3 A square wave centered about t =0, with an amplitude of unity and a period of 4 s, can be described in the interval 1t 1 <2 as

(7.28) (see Figure 7.3).

Since the function is an even function, that is flt) = fl-t), all the bn's are identically zero. (Try it if you do not believe it.) Solving, then, solely for the an's,using Eq. (7.27b), we get

a,=5Ts'o(1)cos.($It dt+:lz(-l) cosn($)t dt

or

(7.29)

4 . nx

Un =-nn S1n -2

Figure 7.3 Fourier series tit to a square wave.As the results are symmetric about the origin, only the positive axis has been shown. The parameter N denotes the number of terms in the Fourier series.



---PAGE-213---



Sec. 7.3 The Wave Spectrum 197

Forn aneven number,a,,=0,and forn odd,a,,=(-1)”+’(4/nn)forn =1,3, 5,. ..;thus

At)=-cosE -4COS6nt+ COS!ont-Aces14nt+ ., (7.30)

4

n T 3 n T 5 n T 7 n T

Figure 7.3 shows the fit of the series to the function for one, two, and three terms. For a good representation to a function, it is necessary that a sufficient number of termsNbe taken in the summation (practicality dictates that N not be infinite). How large N should be can be determined by finding the mean square value of the functionflt).

1d f2(t)dt=- dt+T[ a+~2(a,cosnot+b,sinnot) dt

I’ (7.31)

t+T N

T T

l N

=a; +- 2 (at,+bt,)

2 n=l

This is referred to as Parseval’s theorem, and it implies that if one-half the sum of the squares of the coefficients does not approximately equal the averagemean square value offlt), more terms shouldbe taken (Nlarger).It is often more meaningful in this comparison to subtract out the mean offlt) prior to using Parseval’s theorem, as a; can dominate the summation.

For the square wave in the example,

-!-s2.f’(t)dt = 1

T -2

For various values of n we have [from Eq. (7.29)] 0.811, N = I 0.900, N = 3

I

n+’-----=aS,+bS,2 10.950,0.933, NN==75

I1.00, N=00

7.3.3 Complex Series Representations

The exponential form of the Fourier series is obtained from the Euler identities

eina‘=cosnot +i sin not e-inat=cos not - i sin not

(7.32)

where i = fi.By adding and subtracting these two relationships,we have



---PAGE-214---



198

Wave Statistics and Spectra Chap. 7

the identities

einuf + e-inul

cos nat =

2

sinnot=einui -e-inul =-i( einuf-e-inut)

2i

These expressions are then substituted into the Fourier series as represented in Eq. (7.24):

(7.33)

If the dummy subscript in the term modifying e-inufis changed to -n, we can write

N

###### At)= C: F(n)einuf

(7.34) where

n=-N

i 22 (7.35)

a,, - ib, a, + ib,

for n >,0

F(n)=

for n < 0

SinceF(-n) =P ( n ) ,where the asterisk means complex conjugate, the righthand side of Eq. (7.34) is real. The F(n)may be obtained equivalently from the time series by

(7.36) using Eqs. (7.35), (7.27b), and (7.27~).

Equations (7.34) and (7.36) constitute a Fourier transform pair. For discrete data, obtained at Z points, the Fourier transform pair must be replacedby sumsor

###### I N

###### F(n)=-2Am At)e-2nimn"

- (7.37)
- (7.38)


Zm=l

where T =I At and At is the time between samples, and

112

Am At)= 2 F(n)e2"i"n"

n=-II2



---PAGE-215---



Sec. 7.3 The Wave Spectrum 199

Figure 7.4 Argand diagramfor F(n). Real axis

Any complex number such as F(n)can be expressed in terms of an amplitude and a phase, using an Argand diagram (see Figure 7.4), which shows the real number along the abscissa and the imaginary numbers on the ordinate.

###### F(n)= IF(n)I e-i'n

(7.39)

where

and

E,,=tan- an

The phaseE , gives the relationship of each particular harmonic term to the origin. For example, if the functionflt) is even, then all the b,'s are zero and the phases are either 0" or 180". If the function is odd, the E , values are either n/2 or 3n/2for all n. If theflt) is translated with respect to the origin, the phases change, but IF(n)I remains the same.Thus the IF(n)I'sprovide a good characterization of a function.

7.3.4 Covariance Function

The covariance function, or the correlation function of two timevarying quantitiesfi'(t) andA(t), can be defined as

C,(Z) =Ll f(t2f(t+5)dt (7.40)

r+T

###### T

where T is a time lag. If i = j = 1, then C,(Z) is the autocorrelation function, while if i +j,this quantity is the cross-correlationor cross-covariance function.



---PAGE-216---



200 Wave Statistics and Spectra Chap. 7

There are two important uses of the autocovariance function. The first is to identify periodicity within the time seriesfi(t). For periodic data, CIl(7) will be periodic with the same period as fi(t).The second utility for a covariance function is that it is related directly to the energy spectrum, aswill be shown shortly.

It can be shown that CIl(z)= c11(-7),that is, CII(7)is symmetric about the origin, and that the covariance is independent of the phase angles of the components offi(t).

If we now substitute the Fourier series representation forA(t+ t)into the equation for the covariance, we obtain

N12

1 N / 2 r+T

###### =- 2 f(t)einurdt I;,(n)dnm (7.41)

T ~ = - N I ~1

###### N12 NI2

m.wherec(n)isthecomplexconjugateofthecomplexFouriercoefficientsof

For the autocovariance,

(7.42) F,(n)12 cos naz

since CIl(z)is symmetric. For the case where the time lag 7is zero,

###### N12

(7.43) which recovers Parseval's theorem.

7.3.5 Power Spectrum

The Fourier transform of the covariance function is defined as the power spectrum (fori =j)or the cross spectrum (fori +j).For water waves it is more appropriate to call it the energy spectrum (i =j),as in the context the components of the spectrum are the squares of the wave amplitude at each frequencywhich are related to wave energy. Taking the Fourier transform of C,,(7),we obtain

(7.44)



---PAGE-217---



Sec. 7.3 The Wave Spectrum 201

for -N/2 <n <N/2,which is the two-sided energy spectrum. In practice, the one-sided energy spectrum is used, which is physically more intuitive as it does not involve negative frequencies,-no.

n > 0 n = 0

@;l(n)= 2 IF1(n)12, (7.45) @{l(O) = IF,(O)1 2 ,

for 0<n <N / 2 only.

In the past, the procedure described above to obtain the wave spectrum was the only practical procedure available. This method, called the meanlagged products method, involved the computation of the covariance function and then its Fourier transform was calculated to obtain the power spectrum. This laborious method was necessary, instead of the more direct technique of just taking the Fourier transform of the wave record to obtain theF(n)coefficients and then finding IF(n)I', asit was very time consuming to obtain the Fourier transform. However, in the last two decades, with the implementation of the fast Fourier transform (FFT), which drastically reduced the amount of time necessary for computation, the more direct technique is now favored. In fact, most computer library systems have FFT algorithms available.

The cross spectrum QJn)(for i + j )is obtained in a similar manner as

Q1,(n)='s Cf,(z)e-fnurdz=c(n)F,(n) (7.46)

@ f f .

f+T

###### T I

or, it is the product of the Fourier coefficients of time seriesj andthe complex conjugate of the coefficients for series i. The cross spectrum is in general complex, the real part is denoted the cospectrum, and the imaginary, the quad(rature) spectrum,orQl,(n)=Co,(n)+iQuad,(n).

There are numerous intricacies of spectral estimation, such as stability and resolution of the spectrum, length of time series necessary, digitizing frequency, and so on. The interested reader is referred to other references for this; see, for example, Jenkins andWatts (1968).

7.3.6 The ContinuousSpectrum

The amplitude, phase, and energy spectra that have been discussed have been discrete; that is, there are contributions only at discrete frequencies, for example, for the energy spectrum Qll(n), and the spacing on the frequency axis is

###### 2R

(7.47)

A a = -

###### T

The discrete nature of the spectra is a direct result of considering the time



---PAGE-218---



202 Wave Statistics and Spectra Chap.7

series to be periodic. Natural phenomena such asgustinessin the atmosphere orwater waves are usually considered to be aperiodic, and therefore there are a number of analytic continuous wave spectra which are used in design.

The formal derivation of aperiodic spectral relationships will not be presented here. It suffices to note that the procedure is one of considering the interval of periodicity Ttoapproach infinity andrecognizingthat in the limit the contributionsaredensely packed onthe frequency axis [cf.Eq. (7.47)] and thus approach a continuous distribution.

In practice, to represent the periodic energy spectrum as a continuous spectrum, the following simple transformation ensures that the total energy isconserved:

IF(G)l 2 ACT= IF(n)I Z (7.48) where o;, = n A c and it is seen that for the one-sided spectra IF(n)I and IF ( @I2,

+cu

(7.49)

n=O

###### 7.4 THE DIRECTIONAL WAVE SPECTRUM

During a storm, such as a hurricane, a great number of waves are present on the sea surface, coming from many different directions. To characterize this, a directional wave spectrum is used.Thisgeneralizes the frequency spectrum, (7.23), by adding the variable 8, the wave direction, in addition to the wave frequency.Thus for each frequency there may be a number of wave trains from different directions. This directional wave system is expressed as4

where B is the angle made by the wave orthogonal and the x axis. reduces to

For waves measured at a point, say the origin, asa function of time, this

(7.51)

Measurement of the directional spectrum and its use in design has recently become widespread in the ocean industry. In fact, in relatively deep water, the directional nature of the sea surface during storms is at least as important as the nonlinearities present due to large waves. (For shallow

requiresthatk,=-kn,butthatinthedepth-dependentterms,k-Ik.I,toensurethedecaywith

‘The artifice of negative frequencies is required here to ensure that q(t) is real. Note that this

depth.



---PAGE-219---



Sec. 7.4 The DirectionalWave Spectrum 203

water conditions, the nonlinearities aregenerally much more significant than in deep water.)

As an example of the formulations necessary to develop the directional spectra, we will consider measurements made by a surface-piercing wave gage [Eq. (7.50)] and a two-component current meter, oriented such that it measures the horizontal components (u, v).

- u(t)= F 1

n=-N/2

na

- v(t)= 5


The velocities u and v can be represented as

"gk,,cos 0

###### K,(z)F(n,O)einufdo

- (7.52)
- (7.53)

where, as developed in Chapter 4,

and the associated velocity potential is

- (7.54)


na

"gknsin 13

###### K,(z)F(n,O)einufd0

n=-N/2

The energy density spectrum @,,(n) is obtained analytically by first determining the covariance function C,,(z).

###### C,dz) =-!J"'q(t) i2'F(n,O)einu(r+r)d0dt

T n=-NI2 (7.55)

###### C,,(z) = 12'P ( n ,0')de'12'F(n,0)dOefnm

n=-NI2

The integrands are periodic functions, and it can be shown (by expandingF(n,0)in a complex Fourier series) that C,,(z) can be written as

The energy density spectrum of the surface displacement @,,(n) is the Fourier transform of C,,(z), or

(7.57)



---PAGE-220---



204 Wave Statistics and Spectra Chap. 7

This quantity QV,,(n)is the energy at each frequencya,, and it is seen to be the integral over the directions 8.The directional energy density spectrum is IF(n,6)I',which gives the distribution of energy with direction as well as frequency. Alternatively, if we examine the energy density spectra of the horizontal velocities. we obtain

- (7.58)
- (7.59)
- (7.60a)


###### ~""(=n)KZJ sin2e

Zn

###### ~ ( n@ I 2, do for -N G n G N

where K =gkK,(z)/na.

Finally, the cross-spectra

mUv(n)=K Jzn cosepqn,e)

do

(7.60b)

r 2 n

(7.60~)

To obtain the directional wave spectrum, a method developed by Longuet-Higgins et al. (1963) may be used. The directional spectrum is expressed as a Fourier series,

m m

IF(^, e)1' = C~ , ( n )cosrn8+ CBm(n)sin me (7.61)

m=O m=l

Now, A, and B, can be evaluated in the foregoing expressions for the

energy spectra.Thus

@ q @ ) = nAo(n) (7.62a)

(7.62b)

(7.62e)

From the equations above, the first five harmonics of the directional spectra can be determined in terms of the cross-spectra.The reader should verifythat the spectrum Qvv(n)would yield an additional but not independent equation in Ao(n)andAz(n).



---PAGE-221---



Sec. 7.4 The Directional Wave Spectrum 205

Different methods for obtaining the directional spectrum using wave staffs or pressure transducers have been discussed or utilized. Panicker and Borgman (1970) discuss various gage arrays and Borgman (1979)presents a unified approach to arrays using different types of sensors. Seymour and Higgins (1978)have developed the slope array, which uses pressure transducersto provide estimates of the directional spectrum.

Example 7.4: DirectionalWave Spectrumfrom a LinearArray

Pawka (1974) uses a linear array of pressure transducers parallel to shore. Using, instead, wave staffs, a method of determining the directional spectra will be illustrated, differing only in the fact that the pressure response factor is not included for ease of presentation.

Consider three wave gages distributed at x =0, 11,and I 2 along the x axis with they axis pointing offshore. For each gage the wave records with time are

NIZ r 2 n

q0(t)= C J F(n,0)d0e-'"" (7.63a)

n=-NIZ 0

where k, is related to n a by the dispersion relationship

###### (no)'=gk, tanh k,h (7.64) and k-, =-k,.

Ifthe cross spectrum betweenqoand vlis examined, we find that

Qol(n)=12^IF(n,0)12eik~c0ds0e '1 (7.65)

for-N/2 <n <N/2.Again expressing the directional spectrum 1F(n,0)1 in terms of a Fourier series, as in Eq. (7.61) and substituting into Eq. (7.65), integrals of the followingform result:

Izncosm0eiknc0s9'1d0=nimJm(k,ll) (7.66)

S'"sinmee'k-cos911do=0

and

(7.67)

whereJ,,,(knll)is the mth-order Bessel function of the first kind. Therefore,

###### Qo,(n)=n 2imAm(n)Jm(k,ll) (7.68)

M

m=O



---PAGE-222---



206 Wave Statistics and Spectra Chap. 7

The other possible cross-spectra are

###### M

Qo2(n)=n C imAm(n)Jm(kn12), 0 n co (7.69)

m-O

M

012(n)= n imAm(n)Jm(kn(12- 11)) (7.70)

W=O

The energy spectrum for each gage is

With three gages we have three cross-spectra and one autospectrum (since the three autospectraare the same)or seven real linear equationsfor seven real unknown

- (7.72)
- (7.73)


and

where (Co),,and (Quad), refer to the real and imaginary parts of the cross-spectrum,

###### q.

Theresulting values ofAotoA6 thusdefine the directional energy spectrum.The fact that the BmLare not obtained means that the resulting directional spectrum is symmetric about 8=0.That is, there is an ambiguity in the results in the sense that the sensor array cannot tell ifwaves are coming from the +ydirection or the -y direction and hence the physical reason for the array being parallel to shore, as the assumption can be made that waves do not come from shore (of course, wave reflection or a significant wind generation area behind the array could affect these results).

It is important to notice that if the gages are spaced evenly, that is, 12 =211,then two of the equationsin the matrices are redundant, and only five Fourier coefficients can be obtained instead of seven.



---PAGE-223---



Sec. 7.5 Time-Series Simulation 207

###### 7.5 TIME-SERIES SIMULATION

Simulation refers to the calculation of phenomena of interest to investigate their characteristics or to evaluate the effectiveness of various designs to measure or withstand the phenomena. An example is the simulation of directional waves to investigate the forces caused on a particular structural design. Numerical simulation is feasible through the extremely efficient FFT procedures noted earlier. In principle, simulations for one-dimensional and directional spectra are essentially the same; the procedure will be discussed here for a directional spectrum.

Consider a continuous directional spectrum IF (q 0)I2, representing the continuous directional spread ofenergy over direction 0and frequencyO. For numerical simulation, the water surface displacement q is expressed as

(7.74)

n 4 m-I

cos (not - kmnxX -kmn? -emn)

in which the above represents a total ofM x N/2wavelets,with M directions at each ofN/2 frequencies.The phase anglesern,are considered to be random, in accordance with the concept of the generation of a wavelet over a fetch which is longcompared to the wavelength. Sincethe set ofemnis random, any number of simulations can be carried out based on a single spectrum; each simulation is termed a “realization” of the spectrum and is interpreted as one of an infinite number of possiblewave systemsthat could result from a storm that caused the spectrum of interest. Thus statistics can be developed describing the probability of the maximum wave height or force or probability of exceeding design limits, and so on.

In carrying out the simulation, the FFT is generally used due to its speed.Thus it should be recognized that Eq. (7.74) represents a periodic time series and any attempt to apply a simulation for a greater period than the interval of periodicity (=2 n / A o ) would not yield any additional information and probably would be misleading.To apply the FFTto simulation, it is more useful to express Eq. (7.74) as

(7.75)

in which a, and bndepend on x and y and include the contributions from all directions at the nth frequency,

###### M

###### a, = 2 JIF(On,0, I’AernAOcos(kmJ +knmJ +Emn)

m=l (7.76)

###### b,= C J I F (o ~,OmI’AOm AOsin(knmxx+k,,J +e m n )

M

m=l



---PAGE-224---



As an illustration of a simulation, suppose that a wave gage array has been designed to determine the directional spectrum. For selected input directional spectra, simulations could be carried out and from these the directional spectra calculated. The use of various record sampling lengths, various levels of random noise added to the input, and so on, would assist in evaluating both the methodology developed for extracting the directional spectrum and the effectiveness of the array for different directional spectra.A specific example would be one in which the longshore component of energy flux at a particular point is of primary interest. Simulations would assist in the evaluation of the ranking of different array designs for extracting the parameter of interest for a range of directional spectra considered likely to occur.

###### 7.6 EXAMPLE OF USE OF SPECTRAL METHODS TO DETERMINE MOMENTUM FLUX

In Chapter 10 it will be shown that the onshore flux of the longshore component of momentum S,, is given by

S ---sin28E CG

xy-2 c (7.77)

in which 8is measured counterclockwise with respect to the xaxis and thex axis is directed shoreward, and E is the usual total energy per unit surface area. Equation (7.77) represents the contribution for a particular frequency and wave direction. If measurements of waves are made such that the directional spectrum is obtained, the contribution is given, in terms of the directional spectrum, as

YIF(~,e m ) 1 2(1 + 2knh )sin26, A6, (7.78)

Sxy(n, Om) =

4 sinh 2knh

where y =pg,the specificweight of water.The contribution to the momentum flux component on a frequency-by-frequency basis yields

2knh )5IF(n,& ) I 2 sin28, A8, (7.79)

sinh 2knh m=l

and the total longshore component of the onshore component ofmomentum flux is

(7.80)



---PAGE-225---



Chap. 7 References 209

7.6.1 Measurement of S., in Shallow Water

If shallow water wave conditions prevail, an interesting and simple application of spectral theory affords a direct determination of the momentum flux component Sxy.

The integral counterparts to Eq. (7.74) expressed for the u and v components of water particle velocity are

- u(z,t )= n=N/2c J2”F(n,e)gcose
- v(z,t )=nyJ2’F(n,e)asine


cosh k(h +z) sinh kh

###### ernofde (7.81)

n=-N/Z

cosh k(h +z) iflot

e de (7.82)

n=-N/2 sinh kh Consider the time averageof the product of u and v:

u v = 2 J IF(n,e)12-sin20

n=N/2 271 d . cosh2k(h+z) n=-N/Z 2 sinh’ kh

dB (7.83)

~

which upon using the dispersion equation (3.44) and shallow water approximations becomes

(7.84) which can be shown to be proportional to S,,, that is,

###### Sxy=p h h (7.85)

Thus the time-averaged product of the output from a biaxial current meter could be used to determine an estimate of the total value of SxpA running average of this product would provide a useful measure of the longshore forces exerted on the surf zone by the incident waves. The result displayed in Eq. (7.85) should not be surprising since the definition of Sxyis

0

Sxy= J h puv dz (7.86)

and for shallow water conditions, u and v are uniform over depth.

###### REFERENCES

ABRAMOWITZ,M., and I. A. STEGUN.Handbook ofMathematical Functions, uover, BORGMAN,L. E., “Directional Spectral Models for Design Use for Surface Waves,” COOLEY,R. J. W., and J. W. TUKEY,“An Algorithm for the Machine Calculation of

NewYork, 1965. Preprints, OffshoreTechnol. Conf.’,1979. Complex Fourier Series,”Math. Comput.,Vol. 19, 1965.



---PAGE-226---



FORRISTALGL.,Z., “On the Statistical Distribution of Wave Heights in a Storm,” J.

Geophys. Res.,Vol. 83, No. (3,1978.

JENKINS,G. M., and D. G. WATTS,Spectral Analysis and Its Applications, Holden-

Day, San Francisco, 1968.

LONGUET-HIGGINS,M. S., “On the Statistical Distribution of the Heights of Sea

Waves,”J. Mar: Res., Vol. 11, pp. 245-266,1952.

LONGUET-HIGGINS,M. S., D. E. CARTWRIGHT,and N. D. SMITH,“Observations of the

Directional Spectrum of Sea Waves Using the Motions of a Floating Buoy,” in Ocean Wave Spectra, Proceedings of a Conference Held at Easton, Prentice-Hall, Englewood Cliffs, N. J., 1963, pp. 111-131.

PANICKER,N. N., and L.E. BORGMAN,“Directional Spectra fromWave GageArrays,” Proc. 12th Conf: CoastalEng., ASCE, 1970, pp. 117-136. PAWKA,S., “Study of Wave Climate in Nearshore Waters,” Proc. Int. Symp. Ocean

WaveMeas. Anal., ASCE, 1974,Vol. 1, pp. 745-760. PIERSON,W. J., “The Representation of Ocean SurfaceWavesby aThree-Dimensional Stationary Gaussian Process,”NewYork University, New York, 1954.

SEYMOUR,R. J., and A. L. HIGGINS,“Continuous Estimation of Longshore Sand

Transport,” Proc. Coastal Zone ’78,ASCE,Vol. 3,1978.

###### PROBLEMS

In a wave train consisting of 600 waves with a rms wave height H,, of 4 m, what is the probability that the height of a particular wave will exceed 6 m? What is the probability that the height of at least one of the 600 waves will exceed 6 m?

7.1

Recognizing- thatthetotalareaunderaspectrumisq,thatforasinglesinusoid

7.2

$ = H2/8,and that for a Rayleigh distribution Hl13= 1.416Hm,, develop a realtionship between HI/,and the square root of the area under the spectrum

%Ills.

7.3

For the time functions below: (a)determine the Fourier coefficientsa,,and b,; (b) the phase anglesE,; (c) the complex Fourier coefficients; (d) the two-sided energy spectra; (e) the cross-spectrum.

fi(t)= 1 +2 cos at +2 sin at -3 cos 3at

fi(t)=2+3siniat--:>+4cos4at

The cross-correlation function C12(t)associated with a pair of time functions fl(t) andfi(t) isgiven by

7.4

Cl2(~)= 3 cos2at sin at Iffi(t) is given as

fi(t) =f + cosat +isin 2at - sin 3at +4cos4at findR(t).



---PAGE-227---



Chap. 7 Problems 211

- 7.5
- 7.6

Demonstrate that an arbitrary shift of the time origin by an amount t' changes the individual values ofa, and 6, but does not change ,/=. Using two wave gages located a distance I apart, show that the wave direction for a sea that has a unique direction for each frequency is

- 7.7 For a directional wave system as expressed by Eq. (7.51), derive the following cross-spectra:

@?Idn1, @fj4J?I/Jdn ), %J?I/JY)(~ 1, @(dq/Jx~JqJx)(n)> @@q/dy)(J@y)(n)

Develop the counterparts to Eq. (7.62) for the coeficients of the directional spectrum.

- 7.8 Develop the first five harmonics of a directional spectrum based on records of the water surfaceand the surface slopes,that is,
- 7.9 Compare the values ofHlllo,H I/,,andHIobtained by the Rayleigh distribution and by the two-component model. Discuss and develop a reasonable qualitative explanation for the differences.Also compare H,,, obtained from the two approaches.




---PAGE-228---



###### WaveForces

Dedication

###### WILLIAM FROUDE

William Froude(1810-1879) iswell known for the dimensionless parameter that bears his name. This parameter, utilized in model testing involving a liquid free surface, such as would occur in testing of ships, harbor response or wave forces on structures, is a ratio of the inertial forces extant to the gravitational forces.

Froude was born in Dartington, England,and received his bachelor’s degree in mathematicsfrom Oriel College, Oxford, in 1832and his master’s degree in 1837. After graduation he worked for lsambard K. Brunel, the well-known civil engineer and naval architect. Brunel asked himin 1856to study the waves generatedby ships. In1859he movedto Torquay, an Admiralty establishment, to continue his work in naval architecture. During this time he studied trochoidal waves and developed techniques to reduce ship roll. In 1870 he began a series of experiments to study the resistance of ships using a covered towing tank 76 m long, 10 m wide, and 3 m deep. He used dynamometers to measure the forces of various modelsof ship hulls and scaled these up to prototype scale.

###### 8.1 INTRODUCTION

An important application of water wave mechanics is the determination of the forces induced by waves on fixed and compliant structures and the motions of floating objects. All objects, whether floating on the sea or attached to the bottom, are subjected to wave forces, and therefore these forcesare of central interestto the designer of these structures.

The investigationof wave forces has been under way for a considerable

212



---PAGE-229---



Sec. 8.2 PotentialFlowApproach 213

time and numerous studies have been carried out for the case of wave forces on a vertical pile, yet no wave force calculation procedure has been developed to date for this most simple case for which there is uniform agreement. Although for long-crested waves, with a single fundamental period, theories are available which accurately represent the water particle motions in the absenceof a pile for a wide range of wave characteristics, at present there isno reliable procedure for calculating the wave interaction with a structure for all conditions of interest. Watching a wave impinge on a vertical pile, the complexity of the problem becomes immediately obvious. As the wave crest approaches the pile, a bow wave forms and run-up occurs on the front of the pile, while a wake develops at the rear. We know from fluid mechanics that the wake signifies separated flow, which is impossible to treat analytically. Moreover at Reynolds numbers of interest, the flow is generally turbulent. As the wave crest passes and the trough reaches the pile, the flow field reverses and the previously formed wake may wash back past the pile as a new wake is formed. All of these phenomena clearly violate our previous assumptions of irrotational flow with small-amplitude waves and small velocities.

Later discussions will describe the wave forces as comprised of an inertia and drag force component. In the case of structures that are large relative to the wave length, the wake effects are not important; the inertia forcedominates, and accurate calculation methods exist. For objects that are small, the wake plays a dominant role on both the drag and inertia force components, and the roughness characteristics of the object are also of significance.In the latter case, no reliable analytical approaches are available and experimental results provide the major design basis.

###### 8.2 POTENTIAL FLOW APPROACH

The treatment of ideal flow about a circular cylinder will provide a framework for wave force discussions to follow. If, for convenience, we consider a section of vertical piling far from the free surface, then to obtain a first approximation for the wave force we integrate the pressure distribution around the piling using potential flow. For a circular piling, it is convenient to use polar coordinates (I; 0, z) in the horizontal plane. In this system, the Laplace equation in three dimensions is

###### a2+ 1a4 a2+ a2+

-+--+-+-=O

v2+ = ar2 r ar r2ae2 az2

and the velocity components are

A solution to this equation, which is uniform in the vertical direction,



---PAGE-230---



214 Wave Forces Chap. 8

&r,8)=U(t)r(1+-3cos8

At r= a,the radius of the pile, there is a no-flow condition in the r direction as expected.

U(t),the far-field velocity, is considered to vary sinusoidally with the wave period T. In plan view the flow around the cylinder is as shown in Figure 8.1. (Note the absence of a wake in potential flow.)

Tocalculatethe pressure distribution around the cylinder,the unsteady form of the Bernoulli equation is applied at the cylinder wall and far upstream at a point wherer =I, 8=0,and 1>>a:

+gz+-------

+gz+'-----

###### 2 at 2 at 8=0

(8.5)

The elevation terms cancel, leaving the pressure difference between the free stream pressure in the fluid and that at that cylinderas

(8.6) Substituting from the velocity potential yields

###### dU

p(a,8)-p(l,0) =p[m(l-4 sin' 8)+2a-cos8-I"] (8.7)

2 dt dt

where terms of O(a2/12)have been dropped as extremely small.The pressure term is thus due to two different contributions, the steady flow term, proportional to U2(t),and an acceleration or inertial term, due to dU(t)/dt. Let us examine them term by term.

Figure 8-1 Potentialflowaround a circularcylinder.



---PAGE-231---



Sec. 8.2 PotentialFlow Approach 215

8.2.1 Steady Flow Term

The steady pressure contribution as a function of angular position around the pile is

p(u,8)-p(l, 0)=PU'(t)----(1 -4 sin' 8)

###### 2

This pressure distribution is shownin Figure8.2.The pressure is symmetrical about the pile and in the absence of a wake, the pressure at the rear ofthe pile is the same as that at the front. Intuitively, the net pressure force in the downstream direction should be zero. Integrating the pressure around the pile, noting that we use the component of the force in the downstream direction as illustrated in Figure 8.3, yields the steady (drag) force per unit elevation dFD,where

###### dFD = J2np(u,8)a cos 8d8 (8.9)

=~ * ' ~-4~sin2(8)+lp(l,0)1acos8dB

###### or

###### dFD =0 (8.10)

Therefore, as expected from the pressure symmetry, there is no force on the pile in ideal steady flow. However, this is contrary to the actual results determined from real flows; an experience familiar to all is the force occurring on one's arm when extended out the window of a moving car. This discrepancy has been called DAlembert's paradox and it puzzled the early hydrodynamicists.The reason for the paradox, as alluded to before, is the unrealistic assumption of potential flow, which precludes the formation of boundary layers and a wake.

###### Figure 8.2 Pressure distribution around cylinder for case of ideal flow. Note the low pressure at the sides, 0= 90", and the symmetry with respect to 0= 0" and e=90".



---PAGE-232---



###### 216 Wave Forces Chap. 8

.X-

Figure 8.3 Calculation of elemental force in x direction. AFxis positive in the downstream(-x) direction.

The real pressure distribution around a cylinder in steady flow is a function of the Reynolds number IR, defined as IR = UD/v,where U is the velocity normal to the cylinder axis, D is the pile diameter, and v =p/p, the kinematic viscosity of the fluid, which is the ratio of the dynamic viscosityp to the fluid density p. In Figure 8.4, Goldstein (1938) shows the measured pressure distribution around cylinders for two Reynolds numbers compared to the theoretical ideal flow result. For the upstream portion of the cylinder, with 8G 8,, the separation angle, ?he pressure may be described approximately by potential flow; however, for 8> 8,, which is a function of the Reynolds number, the pressure appears nearly constant. We can therefore approximate the force on a cylinder by using the potential flow solution for 0 G 8G 8, and using a constant pressure in the wake, as follows:

dF -2Jn’hpq(1-4sin28)acos8d8+2 (8.11)

###### =pU2(t)a[s”(10 -4sin20)cos8d8+LIpu2(l)/2cos8do]

1.o

0 P - Po

~

l P U 2 -1.0

- -2.0
- -3.0


###### 0 30 60 90 120 150 180 210 240 270 300 330 360

0 (degrees)

###### -----

Theoretical -MeasuredIR=6.7Xlo5 -----Measured IR=1.9X lo5

Figure8.4 Measured pressure distributions around cylinders. (From Goldstein, 1938.)



---PAGE-233---



###### Sec. 8.2 Potential Flow Approach 217

100

t- D Imml -

80

60

0 0.05

40 20

###### Measured

10

###### 8

0 42.0

6

###### e 80.0

4

c ---Theory duetoLamb

0 300.0

1

0.8

0.

0.6

0.4

###### 0.2

0.110-1 I l lI00’ I 1 I10’1 I I l l1021 I I i lIlo3 I I l l1o4’ ’ I l l105’ I I ’ I

106

R = UDlU

Figure8.5 Variation of drag coefficient, CDwith Reynolds number [R for a smooth circular cylinder.(From H. Schlichting,Boundary Layer Theory. Copyright 0 1968 by McGraw-Hill Book Company. Used with the permission of McGraw-HillBook Company.)

The term within the brackets is a function of Reynolds number lR, as both % , and Pwake vary with Reynolds number. Therefore, the force per unit length, dF,can be related to a function, CD,which varies with R,allowing us to write the force on the pile per foot of elevation as

(8.12)

whereD =piling diameter=2a and for the case of a circular cylinder is equal to A =projected area/unit elevation of the cylinder (i.e., A = 2a).The last form of Eq. (8.12) applies to two- and three-dimensional objects, with the stated definition ofA. The function CDis called the “drag coefficient”and its variation with Reynolds number is empirically known for steady flows as shown in Figure 8.5 for a smooth cylinder of circular cross section. In practice, CDis generally on the order of unity and depends on piling roughness in addition to Reynolds number.

8.2.2 Unsteady Flow

Examining the remaining term in the potential flow expression for the pressure [Eq. (8.7)], we have, integrating the component of force in the downstream direction,

###### dFI= 92a2cos2%d%-Jb-2nP-dU(t)lacos%d% (8.13)

dt dt



---PAGE-234---



218 Wave Forces Chap. 8

The second term on the right-hand side integrates to zero, thereby contributing no net force.The first term, however, yields

dFI =pa2 27r dt

(8.14)

=2pna2 dU-

dt

The term xuzis the volume V of the pile per unit length, so that the final expression can be written as

dU dFI = CMpV-

(8.15)

dt

where CMis defined as the inertia coefficient, which in this case (of potential flow about a circular cylinder) is equal to 2.0. Thus there is a force called the inertial force caused by the fluid accelerating past the cylinder, even in the absence of friction.The general form [Eq. (8.15)] for the inertia force component is valid for two- and three-dimensional objects of arbitrary shapes, except that the inertia coefficient can vary with the flow direction.

The inertia coefficient, in practice, can be discussed meaningfully as the sum of two terms,

###### C M = l + k , (8.16)

where the second term, k,, is called the added mass which depends on the shape of the object. The interpretation of the inertia coefficient is that the pressure gradient required to accelerate the fluid exerts a so-called “buoyancy” force on the object, corresponding to the unity term in Eq. (8.16).An additional local pressure gradient occurs to accelerate the neighboring fluid around the cylinder. The force necessary for the acceleration of the fluid around the cylinder yields the added mass term, km.

Let us first consider the force on an object due to the unaffected pressure gradient in an accelerating fluid. If the pressure gradient is uniform across the dimension of the object, the knowledge available for vertical buoyancy forces in a hydrostatic fluid can be applied. In the latter case, the hydrostatic buoyancy force FBon an object of volume V in a fluid of specific weight y is

FB=yV (8.17)

and for a hydrostaticlluid, the pressure gradient dplaz and specific weight y are related by

y = - - aP

(8.18)

dZ

Therefore,



---PAGE-235---



Sec. 8.2 Potential Flow Approach 219

(8.19)

Returning to the effect of a horizontal pressure gradient associated with an accelerating fluid, the “buoyancy-like” force component is

(8.20) and from the Euler equations, -ap/ax may be replaced byp (du/dt),yielding

du

FB =pvdt (8.21) and by comparing Eqs. (8.20), (8.15), and(8.16), the origin oftheunity termin CMis clear (i.e., it is due directly to the pressure gradient). The added mass, which is shape dependent, is caused by the disturbance of the flow field. It appears that in all cases, CMshould be greater than unity.

For two-dimensional flow about a cylinder of elliptical cross section, the added mass coefficient k,,,can be shown (Lamb, 1945)to be

b a

krn =- (8.22)

3

Ir

.-

r)

e

i-

8

Value for cylinder of circular cross section

.-m

###### -Y

I

i

I k,,,,added mass component

###### - - -- -----_ _ , -- -.-.__ -- .-.____--_-

I

I

I

Prcssure gradient component = 1

I

I

0 1 2 3

alb

Figure8.6 Inertia coeffkient foracylinderofellipsoidcross section.



---PAGE-236---



220 Wave Forces Chap. 8

where a and b are the semiaxesaligned with and transverse to the line of acceleration, respectively. Equation (8.22) is plotted in Figure 8.6, which demonstratesthe occurrenceof a small k, for a streamlined body.

Example 8.1

It is instructive to consider the case where a circularcylinder is acceleratingt hrough a quiescent ideal fluid.Isthe force exertedon the cylinderby the fluid the sameaswhen the fluid accelerates past the cylinder? We expect that since there is no pressure gradient in the fluid, the force would only be due to the added mass coefficient. Therefore, the force should not be the same. To determine this, we write the twodimensionalvelocity potential for a moving cylinder as

a*

###### &r, 8,t)=u(t)-cos8

(8.23)

r

where now, U(t)represents the velocity of the cylinder. It is clear that this equation satisfiesthe followingkinematic boundary condition on the cylinder

U,I,=~ =u(t)cose (8.24)

The pressure at the wall of the cylinder due to the fluid acceleration is given as

###### (8.25)

where 1 is as defined before for the case of a stationary cylinder. Integrating the downstream componentof the pressure force around the cylinder, we have

###### dF, = J2’[p(a,8)la cos 8 d8

###### L 2”p%a2 COS’8d e+1p--cos8dB+L2>(1,O)acos8d0

= 2n dUa3

###### dt I (8.26)

In addition to thisforceby the fluidonthe acceleratingcylinder,a forceis necessary,of course, to acceleratethe mass of the cylinder itself. Therefore,the total force required to accelerate a cylinder through water could be greater or less than if the water accelerated past the cylinderdependingon whether the mass of the cylinder is greater or less than that of the displaced water.

In interpreting the physics and terminology associated with the added mass concept it is helpful to consider the energetics of the case of a circular cylinder accelerating through a fluid.As noted previously, the force per unit length exertedbyan accelerating circular cylinder onthesurroundingfluidis, from Eq. (8.26),



---PAGE-237---



Sec. 8.3 ForcesDueto Real Fluids 221

2 dU

Fl = pk,,,na - (8.27) where k, = 1 for a circular cylinder.

at

Let us now calculate the kinetic energy of the accelerated fluid as a function of time. The radial and angular components of velocity are, from Eq. (8.23),

###### a4 a’

###### u,=--= v(t)-cose

- (8.28)
- (8.29)
- (8.30)


ar r2

The total fluid kinetic energy KE at any time is

The time rate of changeof kineticenergy should equal the product of the force and the velocity,(FI.U),that is, the rate at which work is being done by the cylinder, which is verified as follows:

-- -pa2 -auu

(8.31)

at at

and by comparison with Eq. (8.26), we see that this is exactly equal to F . U. Thus the added mass coefficient represents the ratio of the additional massof fluid that is accelerated with the cylinderto the mass of the fluid displacedby the cylinder.

###### 8.3 FORCES DUE TO REAL FLUIDS

8.3.1 The Morison Equation

Previously, we have treated the inertia and steady-state drag force components independently.However, in a wave field both forces occur and vary continuously with time. Morison et al. (1950) proposed the following formula for the total wave force;which isjust the sum of the two forces,drag and inertia.

dF =dF0 +dFI

(8.32)

###### DU

=1CDpAu1uI +chfpv-Dt



---PAGE-238---



222 Wave Forces Chap. 8

Equation (8.32) is frequently referred to as the “Morison equation.”

It is noted that in Eq. (8.32), an absolute value sign on one of the velocity terms ensures that the drag force is in the direction of the velocity, which changes direction as the wave passes.

8.3.2 Total Force Calculation

To determine the total force on a vertical pile, the force per unit elevation must be integrated over the immersed length of the pile.

###### F+F

(8.33)

In genera CDand possibly CMvary over the length of the pin; as the Reynolds number surely does. Therefore, we cannot integrate these equations directly. If, however, we take constant values of CDand CMand use linear wave theory’ and consider only the local acceleration term, the integration can be carried out up to the rneunfieesur-uceto give an approximation to the total force.

cosh2 k(h +z )

-at) ~ C O S(hi-at)I dz

F = p X L l ( ? ! ) i $2 sinh2kh COS (hi

(8.34) ~CMZD~S’Hcosh k(h +z ) 4 4 2 sinh kh

+ - sin (kxl-at)dz

F = pCDDH2g (2kh +sinh 2kh)

cos (hi- at) ~ C O S(kxi - at)I (8.35)

4 sinh 2kh 4

pnD2H 4k 2

+ C M --d sin (kxl-at)

or F = CDDnE cos(hi- at) ~ C O S(kxl- at)l (8.36)

D

+CMRDE- tanh kh sin (kxl-at) where xlis the location of the pile (conveniently,this can usually be taken as

H

xI=O),E(=tipgH2)isthe waveenergyper unit surfacearea, andnisthe ratio

of group velocity CGto wave celerity C, as given by Eq. (4.82b). The ratio

‘Inactual design, a nonlinear theory (see Chapter11) should be used for horizontal velocity and acceleration.



---PAGE-239---



Sec. 8.3 ForcesDue to RealFluids 223

D/H can be interpreted in terms of the relative importance of the inertia to drag force components. The total moment about the seafloor can be obtained similarly by integrating

###### M =l : dM =l:(h +z)dF

###### (8.37)

= I: 4 Dt

nDzDu

J:(h +z)~CD~DU1u I dz + (h+z)~CM--dz

which yields’

M=CDDnEcos(kxi-Gt) Ico~(kxi-~t[)h)[1--2n( 2khsinh2kh

1 cosh 2kh - 1+2(kh)*

1[ cashkh-‘J]

D H kh sinh kh

+ CMXDE- tanh kh sin (kxl-a) h 1 -

(8.38)

in which each of the terms above is recognized as the total force component times the respective lever arm (the lever arms are in the braces, { .}).The reader should demonstrate that, as expected from physical reasoning, the asymptotes for these lever arms are h/2 and h for shallow and deep water conditions, respectively.

8.3.3 Methodology for DeterminingDragand

Inertia Coefficients

In practice, the reliable determination of drag and inertia coefficients presents a very challenging problem, particularly from field data. The required measurements include the time-varying force F,,, at a particular elevation on a pile, and the corresponding instantaneous water particle velocities and accelerations. Given this information, CDand C, may be determined by a variety of approaches. Only until the recent development of reliable current meters have the water particle kinematics been available to researchers. Previous investigators have had to rely on calculated kinematics based on measurements of the water surface profile. Even if the kinematics are accurately predicted, which is open to some question, particularly if small-amplitude wave theory is used for large waves, then Morison’s equation is only one equation with two unknowns, CDand CM.Two methods have been used to surmount this problem. The first is tocorrelate forces with water particle kinematics only at times when the velocities or accelerations are

’The integrationagainisonly carried out toz = 0as opposed to z = q,for the sakeofsimplicity of the final result.



---PAGE-240---



224 Wave Forces Chap. 8

zero. For a small-amplitude wave of a singleperiod, thiscorrespondsto times of zero or extreme water surface displacements, respectively. At such times either the drag or inertia term is zero and therefore, there is only one unknown in the equation. For example, at the wave crest, the acceleration (inertia force) is zero and CDwould be found as follows:

(8.39)

and a similar equation would apply for the inertia coefficientat times when the velocity (dragforce component) is zero.

Disadvantages of this approach are that considerable data are not utilized: for instance, the data between the crest and the still water crossing. With real storm-driven waves, the times are not obvious at which zeros of velocities or accelerations occur. This can be seen from Figure 8.7, which represents the largest wave measured during HurricaneCarlain almost 100ft of water in the Gulfof Mexico (Dean, 1965).

A second method, used by Dean andAagaard (1970),is tominimize the mean squared error E’ between measured and predicted forces.This procedure, in order to account for Reynolds number dependency,involvesclassifying the digitized data into groups with approximately the same Reynolds number. For each group, then, e2is minimized with respect to the unknowns, CDand CM.

1 ’

###### E’ =- 2(Fmi-F,J2

(8.40)

I i=l

where the lowercase subscripts rn and p refer to measured and predicted forces and I is the total number of data points for the data group. The

I 1 I I I I I I I I I I I I

Time (s)

###### Figure 8.7 Largest measured wave from Hurricane Carla, September1961.(From Dean, 1965.)



---PAGE-241---



Sec. 8.3 ForcesDueto Real Fluids 225

minimization procedure results in two equations in the two unknowns, that is,

(8.41)

Multiplying through and simplifying, the equations are

which can be abbreviated as

(8.43)

where A, B, D, F, and G are known constants for a given set of data. Eliminating unknowns yields

GB -DF C D = B~-AF and (8.44)

D B- GA CM= B~-AF

Once the coefficients have been obtained, the mean squared error can be found by expandingEq. (8.40),

I

E2= 2pm8-2 D c -~~ G C+MACi +~ BCDCM+FCL (8.45)

i=l

###### or

I

E2 - 2 Fij=ACi -2 D c +~~ B C D C M-~ G C+MFCL (8.46)

r=l

It is interesting to note that the last equation is an equation for an ellipse when plotted with CDand CMas axes.This is most readily seen for the case of symmetricwave data, in which the constant B would be equal to zero3due to the symmetry of the velocity and antisymmetry of the accelerationabout the

Du

'It isinterestingto note that most actualdata sets approximatethis condition of-u I u I =0.

Dt



---PAGE-242---



226 Wave Forces Chap.8

crest and trough. Rewriting the equation above and completing the square,

###### (8.47)

I

D2 G2 i-l A F

###### =e2- C F mi+-+-

Setting the right-hand side equal to a new constant, J, the equation can be written in a standard ellipse form:

###### (8.48)

The center of the ellipse is located at CD= D/A and CM= G/F, which are the values that give the minimum mean squared error for symmetric data [cf. Eq.(8.44)forB=01.Theratioofthetwoaxesism.Theeccentricityofthe ellipseise = Ji--A/F ifA <F or e = J1-I;/Aifl; <A.For a perfect circle, e =0;for an extremely flattened ellipse,e + 1.0. The eccentricityof the ellipse is a measure of the conditioning of the data. If the ellipses are as shown in Figure 8.8, the data are well conditioned for the drag coefficient, but poorly conditioned for determination of CM,as CMcould take on a range of values without changingthe error appreciably. Obviously,the best conditioned data for both coefficients occurs when the ellipses become circles, A = F. In practice, when the data are grouped by Reynolds numbers, typically the low iQ data are poorly conditioned for the drag coefficient, but they yield good results for CM,while the opposite is true forhigh Reynolds number data. This is due largely, for example, for the first case, because the drag forces would

.-

###### I

o (cD)n,m 1.o k

CD

Figure 8.8 Illustration of error surface for data that are well conditioned for determining CD.



---PAGE-243---



###### Sec. 8.3 ForcesDueto Real Fluids 227

###### 2.0

I I ( l I I I I l l 1 I I I T

- - 002 --

V 8 -

00

- - 8

-

- - -
- - -


1.0

0.8

0.6

D' 0.4

0.2

0.1

1 1 I \ I / I 1 1 1 1 I I I

Figure8.9 Drag coefficient variation with Reynolds number as determined by Dean andAagaard (1970).Copyright 1970 SPE-AIME.

only be a small portion of the total force. Figures 8.9 and 8.10 show drag and inertia coefficient results as a function of Reynolds number as obtained by Dean and Aagaard (1970). There is a dependency on Reynolds number apparent for the drag coefficient; however, the inertia coefficient appears to be a constant value, 1.33. Note the reduction of k,,, to 0.33 from 1.0 for potential flow. Many other data exist forCDand CMbased on different values of (D/H)and using other parameters. Because of the complexity of the problem no one functional relationship for CDor CMpresently is known. The values above are recommended for the present for small-diameter vertical piling (say less than 5 ft) when the force is drag dominant, as in most field data for pile-supported platforms.

8.3.4 W ~ v Fe O ~ ~ X~iiS Bipeiincs Resting on the

Seafloor

Pipelines are frequently used to convey gas, oil, and other products across the seafloor.Aknowledge of the wave forces acting on pipelinesresting on the seafloor is essential to a design that will ensure the stability of the



---PAGE-244---



I

###### 228

Wave Forces Chap. 8

###### fl

0.6

###### 0.2

I 1 I l l I I I l l I I I I

0.1

Dia.

Symbol

(ft.) Inline Resultant

3.71’

4*

*Waterdepth-33ft “Waterdepth-100ft

Figure 8.10 Inertia coefficient variation with Reynolds number as determined by Dean andAagaard (1970). Copyright 1970 SPE-AIME

pipeline. For our purposes here, we will focus on the case of a long-crested wave propagating with its crest parallel to the pipeline (see Figure 8.11).

In earliersections,we have seen the streamline pattern about a cylinder in an infinite fluid medium. The presence of the plane boundary for the problem being considered here causes interesting streamline patterns and associated forces. Figure 8.12 shows the ideal flow case and it is seen that the streamlines above the cylinder are concentrated, thereby resulting in a maximum lift force coinciding with the time of maximum velocities. If, however, there is a small gap between the cylinder and the seafloor, the concentrationof streamlines beneath the cylindercauses a negativelift force (i.e., directed downward). This phenomenon has been recognized for many years and was of considerable concern to dirigible pilots landing in a crosswind.As the dirigible would approach the ground a strong downward forcewould occur, only to changeto a positive lift forceas the craft “touched down.” The problem was solved by winching the dirigible down under conditions of considerable positive buoyancy. If pipelinesare not adequately ballasted or anchored, they may experience sufficientlift to be raised off the seafloor, then experience a negative lift due to high velocities between the pipe and bottom, resulting in a possibly damaging oscillation.



---PAGE-245---



Sec. 8.3 ForcesDueto Real Fluids 229

-

-Pipeline of circular

cross section

Pipeline resting on seafloor subject to oscillating water particle

Figure8.11

kinematics.

For the case of ideal flow of a fluid about a cylinder resting on the bottom, it can be shown that there are inertia forces in the horizontal and vertical directions. In addition, a lift force occurs; but there is no drag force due to the symmetry of the streamline pattern. The inertia forces (per unit length)in thex and z directions and the lift forceFLfor the pipeline seated on the seafloorare given by

- (8.49)
- (8.50)
- (8.51)


3 - ---l

Streamlines

\ A 4

-4 -3 -2 -1 0 1 2 3 4 xla

Figure8.12 Idealized flow field over a cylindrical pipe resting on the seafloor.



---PAGE-246---



230 Wave Forces Chap. 8

in which according to potential flow (Wilson and Reid, 1963) C M , = CMz= 3.29 (8.52)

###### c,=4.493 (8.53)

It is noted that the vertical acceleration is very small near the seafloor and under the crest acts in a direction to stabilize the pipeline. Under the trough, both the vertical inertia force and lift forces are directed upward; however, for design waves, the velocities under the trough are generally substantially less than under the crest. Thus the uplift forces under the crest will usually be greater than under the trough.

For the case of real flow fields about a pipeline, both the Reynolds number andrelative water particle displacement are of importance. Formost design conditions, the flow will be fully separated and if the particle displacement is greater than twice the pipe diameter, drag and inertia coefficients on the order of 1.0appear reasonable. If the relative displacement (water particle displacement/cylinder diameter) is less than 1.0,experimental data by Wright andYamamoto (1979)have shown that the potential flow results are applicable. Valuable experimental results are also presented by Sarpkaya (1976).

8.3.5 Relative Importance of Dragand Inertia

Force Components

In some situations the drag orinertia force will dominate over the other, thus simplifying the Morison equation.Todetermine the condition for which this happens, consider the value of the ratio dFIm/dFDm.For wave forces on a pile, we know that the maximum velocities occur in the upper portions of the water column. As a reasonable estimate, let us examine the ratio at z =0.

The maximum value of the inertia force for small-amplitude waves occurs at the still water crossing, where du/dt is a maximum. The maximum drag force occurs at the wave crest. If we substitute these values (for z = 0) from Chapter 4:

#### v:)max=f~?cothkh

- (8.55)
- (8.56)


( u * ) , ~ ~= ):( a2coth’kh

2



---PAGE-247---



Sec. 8.3 ForcesDue to Real Fluids 231

we obtain

- (8.57)
- (8.58)
- (8.59)


In deep water, the ratio equals

In shallow water,

For the maximum force per unit elevation of the piling then, it is clear that since CMand CDare O(l), the ratio D/H is relevant in determining the importance of the inertia force. For large structures, with diameters much greater than the incident wave height, the inertia force will predominate in deep water; in shallower water, where kh becomes small, the importance of the inertia force decreases.To determine which force predominates, we will determine the curve for which the two forces are equal. Equating Eq. (8.57)to 1, we have

###### H = CMR

- -tanh kh . D CD

###### (8.60)

This curve is shown in Figure 8.13 for CD/CM= 0.5. For ratios of H/D above the curve, the drag force predominates. Note that in shallow water, the drag force tends to predominate over the inertia force.

2n

5.0

!!

###### D

0

###### Figure 8.13 H/D versus h/L, for condition of equal maximum drag and inertia force components.



---PAGE-248---



232 Wave Forces Chap.8

It is also instructive to consider the total force expressed in terms of a

simple harmonic velocity given by

(8.61)

u = Um COS at

instead of a form related to the wave height. The total force on a unit length of cylinder is

The ratio of maximum inertia to drag force component is (dF,)max 1 C M ~ D2 CM~ 1 (dFD)max CDUm CDUmT/D

###### -I----=X -___ (8.63)

and from Eq. (8.61), it can be shown that um/arepresents the maximum displacementS of a water particle from its neutral position. Therefore,

###### (8.64)

The forms above are interesting because of the backgroundand significance of the parameters umT/Dand S/D. The parameter umT/Dwas first proposed by Keulegan and Carpenter (1958)and is sometimes referred to as the “Keulegan-Carpenter” parameter or the “period” parameter, while S/D is referred to as the “displacement” parameter. It is noted that, for small and large values of these parameters, the inertia and drag force components dominate, respectively. It is very important, but not surprising,that reliable values of CDare most readily determined for large values ofthese parameters and reliable values of CMare best determined from data for which these parameters are small. Moreover, it is found that if these parameters are

Phase angle 0 (deg)

###### Figure 8.14 Measured force variation for S/D = 2.5. (Based on Keulegan and Carpenter,1958.)



---PAGE-249---





---PAGE-250---



234 Wave Forces Chap. 8

small, the form of the wave force time history is well represented by the theory; however, if these parameters are large, the form may deviate significantly from that predicted by theory (see Figure 8.14 for the form of a measured force record for S/D N 2.5). The reason for the behavior noted is that if S/D is small, the particle excursion is so small that friction and wake effects do not develop strongly and the flow field resembles that given by potential theory. As shown in Figure 8.15, as presented by Sarpkaya and Garrison (1963) for a constantly accelerating flow, the inertia coefficient CMis approximated quite well by the potential flow value of 2 for S/D values less than 0.5. For higher values the inertia and drag coefficients decrease and increase, respectively. For S/D values larger than 2.0, the drag and inertia coefficients oscillate with time (S/D),presumably due to eddy shedding.

Figures 8.16 and 8.17 present drag and inertia coefficients obtained by Keulegan and Carpenter (1958) versus the period parameter for forces measured at the node of a standing wave system. (The interpretation of the inertia coefficient being less than unity is that this occursfor a drag-dominant case and that the phasing of the forces are more related to the phases of the near cylinder wake kinematics than to those at far field. Since the drag and inertia coefficients are correlated to the phasing of the far-field kinematics, the inertia force as correlated to the far field is “contaminated by drag force effects.)

8.3.6 MaximumTotal Force on an Object

For an object subjected to simple harmonic oscillations, the timevarying total force can be expressed by Eq. (8.36),which can be abbreviated as

F~=FDCOSatICOSatI- FIsinat (8.65)

in which FDand F, represent the maxima of the drag and inertia force components, respectively, and can be determined readily by comparing Eqs. (8.36) and (8.65).

It is often ofinterest to determine the maximum totd force. Noting that the maximum total force will occur for cos at > 0,Eq. (8.65)can be written in the following form, from which the maximum can be determined by the normal procedures of differential calculus.

###### Fr=FDcos’ ot -FIsin at (8.66)

-dFT =0 =-2FDa cos (at), sin (at),,,-F p cos (at),

###### (8.67)

dt

Although not immediately obvious, there are two roots to Eq. (8.67). The first is found by dividing through by a cos (at),, yielding



---PAGE-251---



3 -

- 2 -

CD

- 1

Figure8.16 Variationofdrag coefficient withperiodparameterasdeterminedby Keulegan and Carpenter(1958).

I I I 1

Dlameter(inc1ies). 3 2.5 2 1.75 1.5 1.25 I 0.75 0.5 Corresponding symbol 0 A 0 0 0 A 8 0 4-

0

0

$3 -

o A 8 - 0 + + + +

\

07P" ",

hC-8" + : O

* -+-

0

+ -

-p A m

0

I I I I

3

- 2




CM

1

Diameter(ii1ches). 3 2.5 2 1.75 1.5 1.25 I 0.75 0.5

Correspondingsymbol: 0 A 0 0 e A a 0 +

I I I I

!5

25 50 75 100 U,, TID

0

Figure 8.17 Inertia coefficient variation withperiod parameteras determinedby Keuleganand Carpenter(1958).

###### 235



---PAGE-252---



236 Wave Forces Chap. 8

sin (at),=--Fi

(8.68)

2FD

which, when substituted into Eq. (8.66), and recalling that cos’ (a),

= 1 - sin’ (at),,givesUS

(8.69)

The need for a second root is apparent upon examination of Eq. (8.68)

and recognizing that if F I / ~ F D> 1, the first root is no longer possible. The second root to Eq. (8.67) is cos (at),=0, which was discarded by dividing this equation by cos (at),. If cos (at),=0, sin (at),=-1 and the maximum total force is

###### FT,=FI (8.70)

The interpretation of this second root can be seen by examining Figure 8.18.Because of the inflection of cos2ot at ot =-n/2, if Fi> 2FD,the inertia force term decreases with increasing at more rapidly than the term involving cos’ at increases. Hence the maximum total force is pure inertia.

It is of interest to verify that the causeof the secondroot is the nature of the quadratic drag term. For example, if the drag force component were linear,

FT=FDcos at -FI sin at (8.71)

then, using the same procedures as before, there is only one root and the maximum total force is always given by

&F,=FDcos’of-F,sinat

L ,F, cos ofI cos ot I

###### I

Figure 8.18 Illustration of force component combination for the case of

IF11 = - ? ) & I .



---PAGE-253---



###### 8.4 INERTIA FORCE PREDOMINANT CASE

As noted previously, if the structure is large relative to the length of the water particle excursion, flow separation will not occur, the drag force component is negligible, and the flow field can be treated by the classical methods of potential flow.There are sufficient numbers of structures in this classto be of practical interest and the applications include both wave forces and impulsive loading (i.e., due to earthquake motions). Two approaches have been developedand will be reviewed below.The first isan analytical approach and can be applied only for limited geometries.The secondis a numerical method which is applicablefor arbitrary geometries.

8.4.1 Rigorous and Approximate Analytical Methods for Wave Loading on Large Objects

MacCamy-Fuchs diffraction theory. As waves impinge on a vertical pile, they are reflected, or scattered, as in the case of a vertical wall, but in many directions. The scattering of acoustic and electromagneticwaves by a circular cylinder has longbeen known and understood. MacCamy and Fuchs (1954)applied the known theory to water waves. For linear wave theory,their resultsare exact, and can be used topredict CMfor a pile for whichD/H >> 1. The velocity potential for the incident wave can be written as

-gH cash k(h+z)

###### 41=- cos(kx-ot)

- (8.73)
- (8.74)


2~ cosh kh

where Re means the real part of the now complex expression. From complex

variables,i = fi,ande'i(h-uf)=cos (kx-at)fi sin(kx-at).Ifthe problem is expressed in terms of polar coordinates where r and 8 are in the horizontal plane and z vertical, the incident wave may be written as

m

2a cosh kh which satisfies the Laplace equation in polar form, and also the linearized form of the kinematic and dynamic free surface boundary conditions.

As this wave impinges on the pile, a reflected wave (which also satisfies the Laplace equation) radiates away and is assumed to have the following symmetric (about 8)form,



---PAGE-254---



238 Wave Forces Chap.8

cosh k(h+z) m=O cosh kh

###### +R = C A, cos mB[Jm(kr)+ iYm(kr)]e-lu‘

m (8.76)

Equation (8.76) satisfies the Laplace equation and, for large kr, this solution has a periodic form which propagates away from the pile, ensuring that the assumed form satisfiesthe radiation boundary condition. Superimposing the incident and reflected waves gives the total flow field. The only remaining boundary condition is the no-flow condition at the cylinder,-d(@, +@&dr

=0atr =a. Satisfyingthis condition determines the values of the terms in the infinite seriesA, (m=0,1,. . .,m).The final velocity potential is

gH cosh k(h+z)e-irrr @,+R = 20 cosh kh

Re

(Jm(kr)+ iYm(kr))]}cos rnB)

rm(ka)

JL(ku)- iYm(ka)

where the primes denote derivatives of the Bessel functions with respect to their arguments.

Using the unsteady form of the Bernoulli equation to obtain the pressure, the force per unit length on the pile may be obtained.

2pgH cosh k(h+z) k cosh kh

###### dFI= - (8.78)

where

Comparing this to the general formula for inertial force,

###### (8.80)

where V=nD2/4and &/at is calculated at the center of the pile, we find that CM= 4G(D/L)/n3(D/L)2.A plot of CMand a versus D/L is shown in Figure 8.19. Note that CMand a reduce to 2.0 and 0,respectively,for small values of D/L, as predicted from potential flow theory for a cylinder in an oscillating flow.

Large rectangular objects. In the MacCamy-Fuchs diffraction theory, the scattering of waves by the pile was included in the inertial force expression, thus allowing the determination of CMfor that case. If, however, the interaction between a structure and waves is not known, approximate



---PAGE-255---



20

0

- -100
- -200


Figure8.19 Variation of inertia coefficient CMand phase angle a of maximum force with parameterD/L.

###### techniques at least allow the determination of the inertia force due to the pressure gradient. Experiments would be needed to determine the added mass, k,.

###### Example8.2

A large rectangular object with dimensions 11,12, and I3 in the x,y,and z directions is located somewhere within the water column. Calculatethe horizontal inertial force on the structure due to a wave propagating in the x direction.

Solution. As before, we would like to integrate the dynamic pressure around the object. Figures 8.20 and 8.21 depict the object and Srefersto the distance between the mean water level and the bottom of the object.The dynamic pressure induced by the waves in the absence of the structure is

In the configurations shown there is no variation of pressure in they direction, as the waves are assumed to be long-crested and propagating in the x direction. In this example, the object will be considered to be totally submerged (Fig. 8.21).

Consider first the approximate wave-induced pressure on the face that isin the x direction, located at x =xI,face (1). The total pressure force on this face, PI,is

PI=IsI~P(X,z,t )dz= 2coshkh

-s+/3 IggHcos( h i-at)ls-s+/3coshk(h+z)dz (8.82)



---PAGE-256---



###### 240 Wave Forces Chap.8

###### z

###### X

Figure 8.20 Dynamic wave pressures on rectangular object.

###### or

-(sinhk(h-S+f3)-sinhk(h-5'))1 (8.83)

l9gH cos(hi-at) 1

PI = 2 cosh kh

[k

Using a trigonometric identity, we get

Figure8.21 Wave forces on fixed rectangular object within free surface.



---PAGE-257---



Sec.8.4 Inertia Force Predominant Case 241 On the face atx =x1+11,the opposing force is

r-s+I?

(8.85)

- cos [k(x,+11)-at]cosh k

2 cosh kh The net force in the x direction isthen P I-P2,as defined asFx: Fx=Pi - Pz (8.86)

###### -- l,1213pgHkcoshk(h - S + 13/2)sinh (k1,/2)sin (kl1/2)sin

2 cosh kh k13/2 k1,/2 This can be rewritten in a more familiar form,

###### sinh (k13/2)sin (k11/2)du k13/2 k11/2 dt

F x=pV

- (8.87)
- (8.88)


where duldt is evaluated at the center of the rectangular object. In the limit as the size of the object becomes small, the term

sinh (k13/2)sin (k11/2) ~ k/3/2 k11/2 11~13-Q

as expected from the buoyancy ana10gy.~Remember, however, that the interaction of the structure with the waves was not accounted for, and thus the added mass is not included in this derivation. Therefore, the actual CMshould be larger than the terms above.The vertical forcecan be calculated in a similar manner (Dean and Dalrymple, 1972),yielding

###### sinh (k13/2)sin (k11/2)dw k13/2 k1,/2 at

###### Fz=pV (8.89)

where again awlat is evaluated at the center of the object. If the tank is situated on the bottom, such that the wave-induced pressure is not transmitted to the bottom of the tank, F, is different.

coth (k13)sin (k11/2)dw k13 k11/2 at

Fz= -pV (8.90)

where dwldt is now evaluated at the center of the top of the object. The interested reader is referred to model tank experiments ofversowski and Herbich (1974)and to

Chakrabarti(1973) for a verification of these formulae. Chakrabarti(1973)has developed the inertia force equations for other objects, valid for linear theory, such as a half-cylinder on the bottom and a hemisphere.

Waveforces on and motions ofafloating body. There are many naval architecture and marine engineering problems which are of importance to the ocean engineer. In this section a very approximate treatment will be

4Thefunctions(sin w)/wand (sinh w)/ware shown in Figure8.24.



---PAGE-258---



242 Wave Forces Chap. 8

presented for forces on and motions of floating bodies; the reader is referred to more extensive developments for additional detail and depth.

Generally, unless a large floating body is propelled, the size and/or streamlining are such that the dominant forces are related to the water particle accelerations rather than the drag forceswhich are velocity related. If we first consideran unrestrained floatingobject that is small compared to the wave length, sincethis object displaces its own weight of water, it is clear that the forces on the object are exactly those that would have occurred on the displaced fluid and hence the motions of the object will be the same as would have occurred for the displaced fluid. This result also appliesto the case of a small neutrally buoyant object at some mean elevation within the water column. For objects that are restrained or large such that the kinematics change significantly over the object dimension, the situation becomes more complex as the object affectsthe waves. In the followingsection, a simplified case is consideredfor a rectangularobject either fixed or freely floatingin the free surface.The treatment is similar to, but more general than the analysis for the submergedrectangularobject.

Consider the case of a rectangular object fixed in the free surface as shown in Figure 8.22. The waves advance at an arbitrary angle0, measured

Figure8.22 Waves propagating with angle(Y past a rectangularbarge of draft d.



---PAGE-259---



Sec. 8.4 Inertia Force Predominant Case 243

counterclockwise from the x axis. Representing the water surface displacement as

H 2

v = -cos(kxx+k,y -at) (8.91)

where k, = k cos 8and k, = k sin 8and d =gk tanh kh, the “undisturbed” pressure field due to this wave is given by

H cosh k(h+z) 2 cosh kh

cos(kxx+kyy-at)

###### P = E - (8.92)

The forces due to this pressure field will be examined as a dominant contributor;however,it should be recognized that there is considerablewave reflection from the object and that this effectcould contribute significantlyto the wave forces.

The computation of forceswill be illustrated in some detail for the surge (x)mode of motion. The force is given by

Fx=s”-‘yD P(-$,y,z)dzdy-J‘y’2-/,I2 p($,y ,Z)dzdy

(8.93)

in which d isthe draft of the object. Inserting Eq. (8.92)for the pressure and carrying out the integration yields

###### -4pg(H/2) (sinh kh - sinh k(h -d)) k,l, kyl,

F, = sin -sin -sin at (8.94)

###### k, k cosh kh 2 2

which can be rendered dimensionless by normalizing with respect to the displaced weight:

H sinh kh - sinh k(h - d )sin k,1,/2 sin k,1,/2

###### -=--k,F X Pg dlx1y 2 kd cosh kh kJx/2 kylyI2

sin at (8.95)

The interpretation of the equation above is interesting. Considering

long waves, Eq. (8.95)reduces to

-- H .

F X ---k, sin at =pg dlxl, 2

###### (8.96)

As noted, comparison with Eq. (8.91)will show that this represents the instantaneous slope of the water surface in the x direction evaluated at the center of the platform. In other words, for very long waves, the horizontal wave forcecomponent is simplythat due to the body tendingto “slide”down the sloping surface (see Figure 8.23). Also, it is clear that if the wave propagation direction is 90”,then k, =0 and F, =0.



---PAGE-260---



244 Wave Forces Chap. 8

Figure 8.23 Wave forces on a “small” floatingobject are equivalentto the weight of the object acting down a surface slope.

For the more complete equation, the sin w/wterms arealways lessthan unity (unless the argument is zero) and represent the reduction due to the finite length of the object; that is, the effective slope over the length of the object is less than the maximum slope (see Figure 8.24 for a plot of sin w/w).

The swayforce0,direction)can be written down by inspection fromEq. (8.95), and is

###### --FY --H-ky (sinhkh - sinh k(h-d))sin kxlx/2sin kYly/2sin at (8.97) Pg dlxly 2 kd cosh kh kxW2 kyIyI2

sin w

~

###### W

0 1.o 2.0 3.0 1 4 . 1

W

###### Figure8.24 Variation of the functions sin w/w and sinh w/w with w.



---PAGE-261---



Sec. 8.4 Inertia Force Predominant Case 245

The computation of the moments is somewhat more complicated than the forces.The pitch moment (about the y axis) will first be developed; the roll moment (about the x axis) could be written down by inspection.

The pitch moment about the center of gravity consists of a primary contribution due to pressure on the (large) horizontal bottom surface and a smaller contribution from the two ends of the object.

Referring to Figure 8.25 the pitch moment about the center of gravity Mo,is

###### Ma,=I, +I2 +13 (8.98)

###### ZI= so(z-z1)p(-$,y ,z)dzdy

where

- (8.99)
- (8.100)
- (8.101)


-ly/2 -d

in which zIrepresents the distance of the center of gravity above the mean water line, the first two integrals,I , and Z2, represent the contributions from the two ends, and the third integral is the moment due to the pressures acting on the bottom of the barge. The resulting expression for pitch moment is

Figure8.25 Definition sketchforpressuresactingon a fixed rectangularbarge to cause pitch moments.



---PAGE-262---



246 Wave Forces Chap. 8

###### (8.102)

cash k(h- d)

in which

sin x

###### S(X) = -

(8.103)

X

and G = kd sinh k(h - d )- [cosh kh - cosh k(h - d)] (8.104)

+kz, [sinhkh -sinh k(h-d)]

The roll and yaw moment would be obtained similarly;however, the expressions will not be presented here.

8.4.2 Numerical Methodsfor Wave Loading on Large Objects of Arbitrary Shapes

For problems of this class, Garrison and a number of colleagues(1971, 1972, 1973, and 1974) have utilized numerical approaches in which the surface of the structure of interest is represented as a number of surface elements with an oscillating source located at the center of each of these elements. These sources,when combined with the incident wave field, satisfy the appropriate boundary conditions. In the following sections, the method will be outlined briefly and representative results presented; the reader is referred to the original papers for greater detail.

Although the boundary value problem will not be specified in detail, it is noted that it consists of the usual no-flow boundary conditions on the seafloorand the structure. For purposesof illustration, and sincethe problem is consideredto be linear,it may be discussed in two parts. First, consider the object to be “transparent” to the flow which is due only to the incident wave field. Velocity components would occur normal to the surface of the structure. Denote this velocity as VnI(S),that is, the normal velocity through the structuredue to the incident wave field.The objective then is to determine a second velocity potential which satisfies the Laplace equation, all of the boundary conditions, and which yields a velocity V,,(S) which is due to the Green’sfunctionand exactly cancelsthe normal velocity on the structuredue to the incident velocity field, that is,

###### Vn&3 = -VnI(S) (8.105)

Green’s functions, G, are developedwhich satisfy the Laplaceequation



---PAGE-263---



Sec. 8.4 Inertia Force Predominant Case 247

and the bottom and free surface boundary conditions, and are denoted by G(x,5) (8.106)

in which the generalized field vector coordinate is representedas x and the surfacecoordinate asthe vector5.The forms of the Green's functionsmay be found for various problemsin Garrison et al. (1971,1972,1973,and 1974).The velocity potential at any location,x,isgiven by

in whichf(5) represents the proper weighting of all contributions on the surface S; this factor is determined in accordance with Eq. (8.105), that is

(8.108)

The solutionto this equation is carried out numerically by partitioning the surface into N area elements and expressingthe integral as a matrix with N elements such that

###### and

(8.110) The coefficient matrix is first calculated from Eq. (8.110) and then Eq.

(8.109)is inverted to find the weighting factor matrixJ.

Examples. Garrison and Stacey (1977)have presented calculationsof wave forces on a number of large offshore structures, including several for which exact solutions were available and other more complex structures for which wave tank experiments were conducted. Figure 8.26 shows a vertical cylindrical caisson for which calculations were carried out. The exact and approximate results are presented in Figure 8.27 for a caisson with a heightto-radius ratio of unity.

As a second example, consider the case of a CONDEEP structure

Figure 8.26 Fixed vertical caisson. (From Garrison and Stacey, 1977.)



---PAGE-264---



---- Approximate(numerical)solution

-Exactsolution

2.4

###### - 2.0

h

###### - 1.6

NU

5v

%J

###### I

1

###### E 1.2

4*

###### 0.8

0.4

0.4 0.8 1.2 1.6 2.0

0

2rralL

Figure 8.27 Horizontal inertia coefficients for vertical caisson for e/u = 1.0. (From Garrisonand Stacey,1977.)

5.0

4.0

h

2

'3.0

vc

*I

###### X

rz"

###### r

- 0

2- 2.0

m

K

N

- 1


.-

----- 0 14.0

Theory Exp. Per. (s)

z!5

###### --- 0 15.5

1.o

r

###### 5.0 10.0 15.0 20.0 25.0 : .o

Wave height, H(m)

Figure8.28 Measured and calculated maximum horizontal forces on 20-m CONDEEPplatform.(FromGarrisonand Stacey,1977.)

248



---PAGE-265---



Sec. 8.4 Inertia Force Predominant Case 249

consisting of 19 cylinders extending upward approximately 47 m from the bottom; above this level three tapered cylinders extend up through the water surface and support the platform deck. In the idealization of this structure, Garrison and Stacey represented the lower caisson structure and portions of the three support columns by a distribution of sources; the upper portions of the three support columns were represented by the Morison equation [Eq. (8.32)]. Comparisons of calculated and measured maximum horizontal and vertical forces and moments are presented in Figures 8.28, 8.29, and 8.30.

8.4.3 Analytical Methodsfor Impulsive Loading

on a Large Circular Cylinder

The forces imposed on a structure due to its motions can be determined in some cases from the solution of the wavemaker (Chapter 6 )problem. For example, Jacobsen (1949)has presented the solution for the case of a vertical right circular cylinder oscillating in a direction perpendicular to its axis; Garrison and Berklite (1973) have also presented this solution with some corrections to Jacobsen’s solution. There is no incident wave field and the boundary condition on the cylinder is expressed as

u(a,e)= ucosecosgt (8.111)

in which a is the cylinder radius and 8 is the azimuth relative to the line of oscillation;the remainder of this “wavemaker” boundary value problem is as previously formulated. The solution is somewhat similar to that for the MacCamy-Fuchs problem and occurs as Bessel functions; the reader is referred to Garrison and Berklite or Dalrymple and Dean (1972) for the details.Although the solution is developed for a simple harmonic oscillation of the cylinder, it is possible, due to the linearity of the problem, to employ linear superposition and represent arbitrary time displacements such as those caused by earthquake motions of the seabed.

8.4.4. Forces Due to Impulsive Motions of Large Structures of Arbitrary Shape

The methodology employed by Garrison and Berklite (1973) for this more difficult problem is quite similar to that described previously for the case of large objects of arbitrary shape in which the use of Green’s functions was outlined.The only differencesare that there is no incident wave field and the normal velocity on the surface of the structure is now specified in accordance with the motions of the structure rather than specified as zero as for the case of a motionless structure. The linearity of the equations governing the problem allows each of the six motion components’ to be solved

’Heave, pitch, roll,yaw, surge,and sway.



---PAGE-266---



Wave height, H(m)

###### Figure8.29 Measured and calculated maximum vertical forces on 20-mCONDEEP platform.(From Gamson and Stacey,1977.)

1.50

I I I I

1.25

h

1.00

E

vc

'DI

0.75

X

- f

5

u

- g 0.50


E

----- A 14.0 --- 0 15.5

Theory Exp. Per.(s)

0.25

0 17.0

0 5.o 10.0 15.0 20.0 25.0 30.0 Wave height, H(m)

###### Figure8.30 Measured and calculated maximum momentson 20-m CONDEEP platform. (From Gamsonand Stacey,1977.)

250



---PAGE-267---



Sec. 8.4 Inertia Force Predominant Case 251

separately and then combined later. For any given structure, the added mass coefficientswere found by Garrison and Berkliteto be frequencydependent, and at very high and low frequenciesit was possibleto simplifythe combined free surfaceboundary condition for periodic motion.

(8.112)

to

4 =0, olarge (8.113) or

###### a4

-=0, osmall (8.114) and

az

P = d (8.115)

The low-frequency limit corresponds to the case of a “rigid lid” boundary; that is, the motion is so slow that there is very little displacementat the free surface and the high-frequency limit corresponds to the case of standing waves iocated near the structure, with very little generation of waves propagatingaway from the structure.

It is of interest to note that the solutions for the limiting cases represented by Eqs. (8.113) and (8.114) do not represent wave-like behavior, but rather casesof antisymmetrical flow about the free surface and uniform flow as idealized in Figures 8.31 and 8.32, respectively.

a4

Interpretation of free surface boundary condition -=0 (for low-

Figure8.31 frequency motions).

az



---PAGE-268---



252 Wave Forces Chap. 8

Figure8.32 Interpretation of free surface boundary condition 4 =0 (for highfrequency motions).

###### Example 8.3

Consider the caseof a vertical circularcylinder oscillating alongthex axis.The added mass for the cylinder is presented in Figure 8.33 for the case of a rigid boundary (d&dz =0)and(4=0). It is seenthat for the caseofa rigid boundary, the added mass coefficientis unity as expected and that for the solution correspondingto a boundary condition,4=0,the added mass approaches unity ash/a becomes large.

Low frequency (rigid uppcr boundary) 1.o

0.8

###### *E

'z5 0.6

i-"

E9"

I

E 0.4

-2

h a tion

P

###### 9

###### 0.2

0 5 10

hla

Figure8.33 Added mass coefficient k,,, versus ratio h/a for oscillating right circular cylinder. (Adapted from Garrison and Berklite, 1973.)



---PAGE-269---



###### Sec. 8.4 InertiaForcePredominantCase

###### 253

All dimensions are normalized with

- q-DT.04 respect to the tank half-width.


Elevation

Withrigidboundary-

6.53 End view Plan

Figure8.34 Dimensions of oil storage tank analyzed by Gamson and Berklite(1973).

A second example presented by Garrison and Berklite is that of an oil storagetank locatedon the seaflooras shown in Figure 8.34.The added mass and lever arm are presented in Figure 8.35.

k, = FH/pUA,A = disp. vol.

-

1.4

-

1.2

motion

F

###### -

- -Y

al

0

i0,

.-.

lz

- - ;0.8-

y1

2

%

- - 0.6 d


-

###### 0.45

- +" 1.0

z

###### E

###### -

c

8 0.40

e

With free surface

e

###### -

-

8 0.35

cm

- 0'4t

a

-

0.30

01 I I I I I I

1.o 2.0 3.0 4.0 5.0 6.0

Depth, h

Figure 8.35 Added massk, andleverarm 1for anoilstoragetank onthe seafloor. (From Garrison and Berklite,1973.)



---PAGE-270---



254 Wave Forces Chap. 8

###### 8.5 SPECTRAL APPROACH TO WAVE FORCE PREDICTION

The Morison equation for wave forces on a structural member is nonlinear in the water particle velocity u appearing in the drag force component [cf. Eq. (8.32)]. A second possible source of nonlinearity for the case of a surfacepiercing piling is due to the variation in total immersed water depth due to the fluctuation of the free surface. However, in cases where the inertia force is dominant, the drag force component is negligible and the equation is now linear in the water particle acceleration u. In addition, since the maximum acceleration occurs for the wave phase corresponding to zero water surface displacement, q =0, there is no contribution at this phase from the second possible source of nonlinearity.

In view of the discussion above, for the case of inertia dominance, the local and total force are approximately linear in the wave height H , and the spectral methods described in Chapter 7 apply directly. From Eq. (8.35)the relationship can be expressed as

(Ff)maX= G(a)H (8.116) in which for the total force on a structure,

pnD2

G(a) = C M -+? (8.117)

###### 8k

Borgman (1965a), (1965b),and(1967)has investigated the application of spectral methods to the problem of wave forces for the case in which the drag force components are not negligible. Only the most simple result of Borgman’s approach will be presented here; the reader is referred to the original papers for additional detail. The incremental wave force dF on an elemental length ds of vertical piling located a distance s above the seafloor can be expressed as

dF=(wuXcosat lcosatI-~cMpnD2urnasinat

2 4

in which urnrepresents the maximum of the horizontal velocity component. To apply linear spectral approaches, it is necessary to linearize the above equation. An intuitive form is

dF = (=urn cos at - cMpnD2u,a sin at (8.119)

2 4

Borgman shows that the force spectrum SdF(a)is related to the sea surface spectrum S,(a) by

###### Sdda)= 1 I2Sq(@ (8.120)



---PAGE-271---



Chap. 8 References 255

in which

where

urn cosh ks Xu(o,s) = -= -Q

(8.122)

IqJ sinh kh

and the linearized drag coefficient CDLis defined in terms of the actual drag coefficientCDand the root-mean-square velocity Ur,, at the levels by

- (8.123)
- (8.124)


That is, CDLhas dimensions of velocity and U,,, is defined by

For the case of total wave forces over the entire water depth, the integrationof Eq. (8.120)is carried out onlyup to the mean freesurface,z =0, and the result is

in which

lhU,,,(S) coshksds

- (8.126)
- (8.127)


GI(@=

sinh kh

G~(cT)a‘

=-k

Borgman (1967) has extended this method to the computation of moments and to multileggedplatforms.

###### REFERENCES

BORGMAN,L. E., “A Statistical Theory for Hydrodynamic Forces on Objects,” Hydraulic Engineering Laboratory Rep. HEL 9-6, University of California at Berkeley, Oct. 1965a.

BORGMAN,L. E., “The SpectralDensity for OceanWave Forces,” Hydraulic Engineering Laboratory Rep. HEL 9-8, University of California at Berkeley, Dec. 1965b.



---PAGE-272---



256 Wave Forces Chap. 8

BORGMAN,L. E., “Spectral Analysis of Ocean Wave Forces on Piling,” J. Waterways HarborsDiv.,ASCE,Vol. 93, No. WW2, May 1967. CHAKRABARTI,S., “Wave Forces on Submerged Objects of Symmetry,” J. Waterways, Harbors Coastal Eng. Div.,ASCE,Vol. 99, No. WW2, May 1973.

DALRYMPLE,R. A., and R. G. DEAN,“The Spiral Wavemaker for Littoral Drift

Studies,” Proc. 13th Conf: CoastalEng.,ASCE, 1972. DEAN,R. G., “Stream Function Representation of Nonlinear Ocean Waves,” J. Geophys.Res.,Vol. 70, No. 18,1965. DEAN,R. G., and F! M. AAGAARD,“Wave Forces, Data Analysis and Engineering Calculation Method,” J. Petrol. Technol.,Mar. 1970.

DEAN,R. G., and R. A. DALRYMPLED,i scussion of J. B. Herbich and G. E. Shank, “Forces Due to Waves on Submerged Structures,” J. Waterways,Harbors Coastal Eng. Div.,ASCE,Vol. 98, No. WW1, Feb. 1972.

GARRISON,C. J., “Dynamic Response of Floating Bodies,” Proc. Offshore Technol. Conf:,1974, Paper 2067.

GARRISON,C. J., and R. B. BERKLITE,“Impulsive Hydrodynamics of Submerged

Rigid Bodies,” J. Eng. Mech. Div.,ASCE,Vol. EMl, Feb. 1973.

GARRISON,C. J., and F!Y.CHOW,“ Wave Forceson Submerged Bodies,” J. Waterways,

Harbors Coastal Eng. Div.,ASCE,Vol. 98, No. WW3, Aug. 1972.

GARRISON,C. J., and V. S. RAO,“Interaction of Waves with Submerged Objects,” J.

Waterways,Harbors Coastal Eng. Div.,ASCE,Vol. 97, No. WW2,1971.

GARRISON,C. J., and R. STACEY“, Wave Loads on North Sea Gravity Platforms: A Comparison of Theory and Experiment,’’ Proc. Offshore Technol. Conf, 1977, Paper 2794.

GARRISON,C. J., A. TBRUM, C. IVERSON, S. LEWSETH,and C. C. EBBESMEYER,“Wave Forces on Large Objects-A Comparison between Theory and Model Tests,” Proc. Offshore Technol.Conf:,1974,Paper 2137.

GOLDSTEIN,S., Modern Developments in Fluid Dynamics,Vol. 2, Oxford University

Press, London, 1938.

JACOBSEN,L. S.,“Impulsive Hydrodynamicsof Fluid inside aCylindricalTank and of Fluid Surrounding a Circular Pier,” Bull. Seismol. SOC.Am., Vol. 39, No. 3, 1949. KEULEGAN,G. H., and L. H. CARPENTER“,F orces on Cylinders and Plates in an

Oscillating Fluid,” J.Res. Nut. Bur. Stand.,Vol. 60, No. 5, May 1958. LAMB,H., Hydrodynamics, Dover, NewYork, 1945. MACCAMYR, . C., and R. A. FUCHS,“ Wave Forces on Piles: A Diffraction Theory,” MORISON,J. R., M.P. O’BRIEN,J. W. JOHNSON,and S. A. SCHAAF“, The Force

Tech. Memo 69, Beach Erosion Board, 1954.

Exerted by Surface Waves on Piles,” Petrol. Trans., AIME, Vol. 189, 1950.

SARPKAYA,“T.V, ortex Shedding and Resistance in Harmonic Flow about Smooth and Rough Circular Cylinders at High Reynolds Numbers,” Rep. NPS-59SL76021,U.S. Naval Postgraduate School, Feb. 1976.

SARPKAYA,T., and C. J. GARRISON,“Vortex Formation and Resistance in Unsteady

Flow,” Trans.ASME, Mar. 1963. SCHLICHTING,H., Boundary Layer Theory,McGraw-Hill, New York, 1968.



---PAGE-273---



Chap. 8 Problems 257

VERSOWSKI,F? E., andJ. B. HERBICH,“Wave Forces on Submerged Model Structures,”

Proc. Offshore Technol. Conf.’, OTC 2042, Vol. 11,1974.

WILSON,B. W., and R. 0.REID, Discussion of “Wave Force Coefficients for Offshore Pipelines,” J. Waterways HarborsDiv.,ASCE,Vol. 89,No.WW1,1963.

WRIGHT,J. C., and T.YAMAMOTO,“Waves Forces on Cylinders near Plane Boundanes,”J. Waterways, Ports, Coastal Ocean Div.,ASCE,Vol. 105,No.WWl, Feb. 1979.

###### PROBLEMS

- 8.1 The triangular cross section shown below is being considered for underwater petroleum storage. The “tank” would be in shallow water, sothe waves may be regarded as long.

- (a) Develop a relationship for the horizontal wave force on the tank. Express your answer in dimensionless form, normalizing by the displaced water weight.
- (b) At what position of the wave profile would the horizontal wave force be a maximum?


- 8.2 What is the maximum uplift force on the slab below due to a wave of 10-m height and 12-speriod? Assume that the presence of the slab does not interfere with the wave motion. At what phase of the motion will be maximum uplift occur?




---PAGE-274---



258 Wave Forces Chap. 8

- 8.3 Given the followingwave conditions: H = 15.6ft T = 1 4 ~ h=20ft


- (a) Consider the case of a single piling supporting a small observation deck. From corrosion considerations, the thickness of the tubular piling is 1 in. Assuming that the dragmoment predominates, developan equation for the stress 0 in the outer fiber of the base of the piling as a function of the diameterD.
- (b) What is the required diameterD if the maximum allowableais ,,a =20,000 psi?
- (c) For the diameter determined in part (b), calculate the maximum inertia moment component and express as a percentage of the maximum drag


(a) Allowingmoment component.a freeboard for the lower deck elevationof10ft, at what elevation

would this be?

Equationsfor CalculatingStress

###### M S

a=-= stress on outer fiber

###### n

S = section modulus = +D4 -0:)

320



---PAGE-275---



Chap. 8 Problems 259

- 8.4 Given
- 8.5
- 8.6
- 8.7
- 8.8
- 8.9

H = 15.6ft T =14s h = 2 0 f t

- (a) Calculate and tabulate the maximum total wave force on the two vertical cylinders shown above as a function of wave approach direction a for a = 0",30", 60",and 90".
- (b) What is the ratio of maximum inertia to drag force for the larger cylinder?
- (c) What would be the total overturning moment for the direction a- of


Determine the inertia coefficients (horizontal and vertical) for a pipeline exactly half buried in the bottom. Based on the experimental results presented in Figure 8.4 and using the CD versus W relationship presented in Figure 8.5, develop a relationship of the separation angle0, versus Reynolds number W.Use the approach of Eq. (8.11) and assume thatpwakecan be taken asp(a,0,). Compare and comment on your results with those in Figure 8.4.

Refemng to Eq. (8.13), and accounting for the effect of separation, develop a fairlysimple equation forthe added mass coefficient versus separation angle0,. (Hint:Use the same considerations suggested in Problem 8.6.)

Discuss the reasons for the decrease in CM with increasing D/L, using the results of the MacCamy-Fuchs theory. Consider the case of waves propagating past and aligned with the major axisof a barge.

- (a) If the dominant forces on the barge are due to being "immersed" in the wave pressurefield, develop an equation forthe surgedisplacementxg(f)of the barge.
- (b) Demonstrate that xe(f) is exactly the same as the average horizontal displacement of the water particles displacedby the barge.


maximum force?

- 8.10 Acircular cylinderof diameter D and length1is held fixed in a horizontal plane at an elevation s above the bottom in a total water depth h as shown below. Considering only the inertia force component and a linear wave of height H and period Tto the propagating in the x direction, develop expressions for the




---PAGE-276---



260

Wave Forces Chap. 8

time-varying components of forces in the x and y directions, F,(t) and FY(f), and the moment M&) about the z axis.

i

###### $+Au6

- 8.11 SimplifyEqs. (8.35) and (8.38) for the cases of shallow and deep water. Discuss the variation of drag and inertia force and moment components with wave period for these two regions. Also evaluate the lever arms implied by the results.
- 8.12 A circular cylinder is immersed in an idealized flow of free stream velocity U. The cylinder is instrumented with strain gages to measure the force at the two locations shown. Develop an expression for the force per unit cylinder length measured by each of the two sets of strain gages. Interpret the sign of the force.
- 8.13 Consider a cylinder with axis horizontal located one-quarter wave length below the mean free surface with a wave of height H and period T propagating with crests parallel to the cylinder axis. The water depth is h. (a) Developanexpression for the time-varying magnitude and direction of the


total wave force (i.e., drag plus inertia) actingon the cylinder.

(b) Discuss your results for the limiting case of shallow and deep water. (c) Specifically for the case of deep water, discuss and interpret the time

variation of the magnitude and direction of the total wave force.



---PAGE-277---



###### Waves Over Real Seabeds

Dedication

###### JOSEPH VALENTIN BOUSSINESQ

JosephValentin Boussinesq(1842-1929) laid the foundations of hydrodynamics, together with Cauchy, Poisson, and St.-Venant. His work in waves is largely remembered for the solitary wavetheory that bears his name and the Boussinesq approximation, which facilitates the study of stratified flow.

Boussinesq was born in St.-Andre-de-Sangonis, France, and earned his baccalaureate from a seminary in Montpellier. Despite his informal educationinthe sciences, he produceda paper on capillarity in 1865and presentedit to theAcademie des Sciences. From1866to 1872 hetaught at the Colleges of Agde, LeVigan, andGap. Hisdoctoral work on the spreading of heat in 1867 won him the attention of Barre de St.Venant.

In1873hebecame a professor at Lille and subsequentlyassumed the chair of physical and experimental mechanicsin Paris.

Boussinesq’s scientific work ranged over manyfields of classical physics: light and heat, ether, fluid forces on bodies,waves, hydraulics, vortex motions, and elasticity. He also studied philosophical and religious matters such as determinism and free will.

###### 9.1 INTRODUCTION

Historically, the mathematical treatment of water wave theory by various investigators has been carried out with the assumption of a rigid, impermeable horizontal seabed. In nature, of course, the actual bottom varies drastically from locales in the Gulf of Mexico where the muds behave as viscous fluids, to rippledporoussand beds,to rough rocky bottoms. The degreeofbed rigidity (as measured by the shear modulus, say), the porosity, and the roughness all influence the water waves to varying degrees. This interaction

261



---PAGE-278---



with the bed results in wave damping and a local changein wave kinematics. Significant wave damping can occur if the bed is very soft, or if the waves propagate a long distance; in either case, shoalingformulas developed earlier are no longer strictly valid.

If the presence of the wave over the bed causes significant bed deformation and stresses,the possibility exists of soil failure and significant forceson buried pipelines and on bottom-mounted structures.

9.2 WAVES OVER SMOOTH, RIGID, IMPERMEABLE BOTTOMS

9.2.1 Laminar Boundary Layer

The equations governing the water waves in a viscous fluid are the Navier-Stokes equation [Eqs. (2.39a) and (2.39c)], shown here in linearized form.

- -=---at pax+v(ax.-+- a,J
- -=--- (9.2) where v (=p/p)is the kinematic viscosity.


au i ap a2u a2u

It is useful to examine the relative sizes of the various terms in these equations; this can be done best by putting them in dimensionless form. Therefore, knowing a priori for waves that a length scale is the inverse of the wave number and a time scale is the inverse of the wave frequency, we can write

X f Z’ t’

x = - z = - t =-, u=aou’ P =pgap‘

###### k’ k’ o

where a is the wave amplitude and the primed variables are dimensionless. Substituting into the equations for the xdirection, we get

-=--- (9.3)

The two dimensionless quantities that result are of different orders of magnitude.The first, the inverse of the square ofa Froude number (C/@) is of order unity [writtenas O(l)], from the dispersion relationship, while the second term, vk2/o,is the inverse of a Reynolds number and O(lO-’ to for normal ocean waves. Hence, in general, this term may be neglected-an a posteriori justification of something that was already done in Chapter 3.

Neglecting the frictional stresses implies that there is a slip boundary condition at the bottom, z = -h, as from Chapter 3we know that the bottom



---PAGE-279---



Sec. 9.2 Waves Over Smooth, Rigid, ImpermeableBottoms 263

velocity is nonzero. However, physically, there is no flow at the bottom, due to the presence of fluid viscosity; hence our argument above must be modified.

Consider that near the bottom there is a small region where u varies radically with elevation. The vertical length scale there must be different and thus, rescaling, we have z =Sz’, where 6 is the thickness of the region over which u changes rapidly. Again, the horizontal equation of motion is

###### (9.4)

The last term can become of O(1)if 6 a m.The length scale 6isa convenient measure for the laminar boundary layer thickness and it is very small. For example, for a 5-swave, 6 a 1 mm.

To summarize the scaling argument, very near the bottom, O(6),

viscous effects can become very important. It is therefore convenient to divide the flow field into two parts, an irrotational and a rotational component, or

u = up+ u, (9.5) where u, satisfies the Euler equation,

au, 1 ap at pax

_-

and U, satisfies the approximate rotational equation

###### _--v- (9.7)

au, a2u,

at az2

The reader should verify thevalidity ofthisprocedure using Eq. (9.1)and the principle of superposition. It is expected that u, goes to zero away from the boundary.

For water waves, we know u, from Chapter 3.

(9.8a) Q cosh kh

or, in complex notation,

where only the real part.is used here and in the following complex-valued expressions. To find u,, separation of variables is used, and keeping only the term that decays away from the bed, we find that’

’The u, term is exactly the same expression as found by solving the problem of an oscillating bottom in a still fluid (Lamb, 1945,Sec. 345).



---PAGE-280---



u, =AeJ-iu/v(z+h)ei(kX-or) =~e-(l-')Ju/2/zv(z+h)ei(~-uf) (9.9)

The complex nature of the exponent of the(z+h)term indicates that there is an exponential decayaway from the bed modified byan oscillating term. The no-slip boundary condition atz =-h,u =up+ur=0,fixesA ,

A = - -gak- 1 (9.10)

a cosh kh

The real part ofthe total horizontal velocity u is therefore U = gak [coshk(h +z)cos(kx-at)

a cosh kh (9.11) -e-Jo/2v(r+h)cos(kx-ot + (z+h))]

2v

which shows there is a phase shift of the viscous term with elevation. The horizontal velocity profile near the bed is shown in Figure 9.1, for a given wave, with k6 =0.01and6= Jv/2a.

The vertical velocity in the bottom boundary layer is most conveniently found from the continuity equation,

gak [sinhk(h+z)ei(v+n/2)

Q cosh kh (9.12)

- r--


###### 7

I k6=0.01

4

Figure 9.1 Normalized velocity profiles for various phase positions y~ in a laminar boundary layer. For x = 0, the velocity profiles depict the fluid motion in the boundary layer as the crest arrives.

0 1.o

-1.0

U

-.

ub



---PAGE-281---



Sec. 9.2 Waves Over Smooth, Rigid, Impermeable Bottoms 265 where v/ = kx - at and s is the elevation above the bottom. The vertical velocity consists of two terms near the bottom. The first is the wave-induced term and the second is the boundary layer correction term, which, incidentally, is much smaller than u,.

The instantaneous shear stress exerted on the bed may be obtained from the Newtonian shear stress term

###### 7x2=PV(-az+-)ax 1z=-h

au aw

- (9.13)
- (9.14)


of which only the first term is large,

or

The bed shear stress is thus harmonic in time and lags the free surface displacement by 45".The mean bed shear stress is zero.

A conventional form for a shear stress in an oscillatory flow is

(9.15)

where u b is the bottom velocity given by potential flow outside of the boundary layer (i.e., the potential flow value) and f is a friction factor. In terms of the maximum value (z,,),a,, we use

(9.16)

where [b is the maximum of the (inviscid) horizontal excursion of the water particle at the bottom. Relating the conventional form of the shear stress to the previously derived form,

- (9.17)
- (9.18)
- (9.19)


or, after some manipulation,

j--8

R where Rb is the Reynolds number defined as Rb=-UbCb

V



---PAGE-282---



266 Waves Over Real Seabeds Chap. 9

###### 100 , I I I I

###### I

1 3

5 w 10 I

20 $

###### 40 5

100 *

600200 2‘2

1rn-0

2800

###### Lower limit of rough turbulent regime

102 103 I04 105 106 1o7

Reynolds number

Figure 9.2 Stanton diagram for friction factor under waves as a function of Rh and f h / k e . The line labeled “Laminar” denotes Eq. (9.18). (From Kamphuis, 1975.)

The friction factor is plotted versus R b in Figure 9.2.For smooth bottoms, the expression is valid for Rb up to lo4.

Due to the presence of the shear stress, there is work done by the waves against the shear stress within the fluid. The mean rate of energy dissipation per unit time is given by

where the overbar denotes the time average over a wave period ands =h +z. The largest term in this expression is

(9.21)

=pv v k m E

sinh 2kh If in the conservation of energy equation we set

dE

(9.22)

-= -ED

dt

where E = pga‘ and a = which is the assumed damping law for the wave amplitude, where a = a. at t =0, we have for a damping coefficient,

(Yb = (9.23) 40 cosh’ kh 2sinh 2kh

Clearly,sincetheboundary layerthickness6(=m)isingeneral

small,the damping is also small. For a 5-s wave in 5 m of water, with a l-mm-



---PAGE-283---



Sec. 9.2 WavesOver Smooth, Rigid, Impermeable Bottoms 267

thick boundary layer,ab= 4.8 x s-I,or for a wave to decay to e-' =0.368 requires I x lo4s or a propagation distance equal to 126 km. (This is only considering the bottom effect.)

Example 9.1

Determine the amount ofdampingthat will occur after a wave propagates a distanceI in water of constant depth h.

Solution. Using Eq. (9.21),we get

dE dE vk dt dx sinh 2kh

-= C, -=-eD = -___ E

- (9.24)
- (9.25)
- (9.26)


Now, since h and k are not functionsofx,we can write this as

_dE= -

Integrating yields

nu sinh 2kh

where the boundary condition of E =Eo at x =0 was used. The wave amplitude at x=1whereI = 100km will be

(9.27)

In the irrotational part of the wave motion, the loss of energy can be calculated in the same manner:

Integrating

###### ED = 2pva2gk2

###### (9.29)

where

For this internal damping, a,= 2vk2.

If we compare the two damping rates, we find that in deep water the latter damping is greater, as the bottom does not affect the waves, whereas in shallow water

(9.30)



---PAGE-284---



Since in shallow water, kh < n/lO and kd is much smaller, the bottom damping is much more significant.

At the free surface, there exists another boundary layer which contributes a small damping (Phillips, 1966),

vk 2 tanh kh

f f f = (9.31) Thisis alwaysmuch smallerthan the interior and the bottom boundary

layer damping:

- (9.32)
- (9.33)


9.2.2 Turbulent Boundary Layers

When wavesbecome largeorthe bottom is rough, the boundary layer is turbulent. In fact, for most casesin nature, a turbulent boundary layer exists. This implies (in analogy to steady flow over flat plates) that the boundary layer is thicker, the shear stress on the bottom is larger,and it depends on the square of the bottom velocity rather than linearly.

Experimental work by Jonsson (1966), Kamphuis (1975),and Jonsson and Carlsen (1976)aswell as theoretical work by Kajiura (1968)has provided insightinto the nature of the turbulent boundary layer and its dependencyon Reynoldsnumber and the relative roughness of the bed, which is defined as ke/&,,where k, is the equivalent sand grain size on the bed and cb is the excursion of the wave-induced water particle motion at the bottom in the absence of the boundary layer. Kamphuis (1975)indicates, with some reservations due to accuracy,that k, can be related to the distribution of sand sizes present on the bottom by

k, =2d90

where d90is the sand size for which 90% of the sand is finer. Using a Stantontype diagram (as used for pipe friction factors), Kamphuis has plotted the frictionfactorfversus Reynolds number and relative roughness as shown in Figure 9.2.As in pipe flow, for rough turbulent flow, there is no effect of &, and Kamphuis proposed that

- (9.34)

and

- (9.35)


-1 + en-1 =-0.35 --4 en 4k for ke/Cb<0.02 2 J f 2 J f 3 cb



---PAGE-285---



Sec. 9.2 Waves Over Smooth, Rigid, Impermeable Bottoms 269

These equations are valid when

- (9.36a)
- (9.36b)


or, more stringently,

###### -2-k, 2200

cb R b

which is the condition for rough turbulent flow, whenIRb > 5 x lo4. The mean bottom shear stressdue to the action of the wavesisstillzero:

Pf

cos (luc-at) (cos(kx-at) I (9.37)

=-(UbJ28

###### = O

The energy damping however is nonzero and determined by the relationship

-

r x y u b = ED

###### or

###### ED =Pf-(ubJ3 COS* (kx- at) (COS(kx- at) I

- (9.38)
- (9.39)


8

Averaging over a wave period, we have

3

which clearly increases as the depth decreases. obtained from the energy equation.

The decay of the wave height with distance over a flat bottom can be

###### or

- (9.40)
- (9.41)


-pgc1 -=--da2 pf d 2 R dx 6nsinh3kh

a3

Solving for the wave amplitude a by separation,we find that

a(x)= 1 +-2f a0k'adc

- .

###### 3n(2kh+ sinh 2kh)sinh kh



---PAGE-286---



kh

Figure9.3 Damping of waves due to damping in a turbulent boundary layer.

This relationship is plotted in Figure 9.3. The amount of wave height decay clearly increases with friction factor as expected and depends on the water depth. In deep water a/aogoes to unity as the bottom friction becomes negligible, while the shallow water asymptote is

(9.42)

The energy loss for a wave with a turbulent boundary layer can be compared to the laminar boundary layer case by relation to the two formulas (9.21)and (9.39):

###### Evk Ja/2v

(9.43)

6nsinh3kh



---PAGE-287---



Sec. 9.3 Water Waves Over a Viscous Mud Bottom 271

The smallest value off is its laminar value fL. Expressingf as /-ifLfor the turbulent case where pis greater than 1,the ratio is reduced to

(9.44)

or/3 > 1.66 for turbulent boundary layer to give greater damping. In general, this is the case, as can be deduced from the wave friction factor diagram.

- Example 9.2


A wave of 5m amplitudepropagates a distance 1with an average depth of 30 m. What isthe final wave height? Given is h = 30 m, T = 10s, d~ =0.3mm, and I = 100 km.

Solution. From the dispersion relationship, k = 0.0457 m-’. Next the friction factor must be determined.

- (9.45)
- (9.46)
- (9.47)


= 0.00022

###### and

[ R b = - = - =Ubcb a’a

= 3.3 x 105

v v vsinh’kh From Figure 9.2,f= 0.004.

The quantityfk2ao=(0.004) (0.0457)2(5) (100,000)=4.18 and = 0.956

a - 1

_ -

2 1 311

a0

1+--Cfk2adc)

(2kh +sinh 2kh) sinh kh

###### or

a = 4.78 m

This represents a 4% decrease in wave amplitude due to bottom frictional damping (over a smooth bottom).

###### 9.3 WATER WAVES OVER A VISCOUS MUD BOTTOM

One representation of a soil bottom would be to characterize it as a viscous fluid. Examples of this type of bottom exist around the world, particularly near the mouths of large sediment-bearing rivers, such as in the Gulf of Mexico near Louisiana (Gade, 1958)and the coast of Surinam (Wells and Coleman, 1978).The mud bottom often damps out wave energy so rapidly that these areas can serve as a harbor of refuge for fishermen caught far away from home port by storms.

The mathematical treatment follows by assuming a laminar flow of a highly viscous liquid overlain by an inviscid fluid. The surface water wave



---PAGE-288---



###### 272 Waves Over RealSeabeds Chap. 9

Water

Figure 9.4 Schematicofwaves over a mud bottom.

described by linear theory will drive an interfacial wave on the mud-water boundary that induces flows in the lower layer. These flows are rapidly damped by viscosity. Figure 9.4 shows a schematic of the waves and fluid regions.

9.3.1 Water Wave Region

In the overlying fluid, the Laplace equation and the linearized free surfaceboundary condition as discussedin Chapter 3 must be satisfied by the fluid motions. Further at the mud-water interface, continuity of pressure and vertical velocities must hold across the interface.

In the upper fluid region, denoted region 1, the velocity potential is assumed to be

4,(x, z,t )=(A cosh k(h+z)+B sinh k(h+z))e'(kx-u') (9.48)

The c$l is clearly periodic in space and time, and satisfies the Laplace equation (3.19). The LDFSBC (3.3313) yields

Acoshkh+Bsinhkh=* (9.49)

while the LKFSBC (3.29) yields

###### iaao

A sinh kh +B cosh kh =-

(9.50)

###### k

The Bernoulli constant C(t)has been taken to be zero, to ensure a zero spatial mean for ~ ( t which) , has been assumed as the real part of ~(x,t)=aoe'(k"-ur).



---PAGE-289---



Sac. 9.3 Water Waves Over a ViscousMudBottom 273

With two equations and three unknowns,A, B,and k,we can solve fortwo of them.

###### A = iaO‘Osh kh (gk -d tanh kh) ak

- (9.51)
- (9.52)


iao cosh kh ak

(d-gk tanh kh)

###### B=

Now, if we were solving the rigid bottom case, as in Chapter 3, we would finallyspecify that the vertical flow, at z =-h, was zero.Thiswould requireB to be zero, which implies that the terms within the parentheses must be zero. Hence the dispersion relationship, relatingk to a,results as before. However, in this case, since the bottom is not fixed and its location is unknown a priori, two interfacial boundary conditions are necessary to find an equivalent dispersion relationship. First, however, the fluid motion within the mud will be prescribed.

9.3.2 Mud Region

For convenience,we will assume that the mud region is infinite in depth (practically,this requires that it be at least as deep asL/2,whereL is the wave length). Furthermore, a boundary layer approach will again be used; that is, the flow will be assumed inviscid except in the boundary layer regions (which,of course, can be very large).This is valid (Mei and Liu, 1973)as long

- as the kinematicviscosity v is very small. Therefore, the fluid mud region will be described by a solution to the Laplace equation, which is spatially and temporally periodic, since it is driven by the water wave. The potential function is then presumed to be of the followingform, where d is unknown:


42(x,z, t )=dek(z+Wei(b-4

- (9.53)
- (9.54)


A boundary layer correction for c$2 is prescribed.

u2 = fe(l -i) J ~ / 2 v ( ~ + h ) ~ i ( b - o f )

Recall from the laminar boundary layer treatment for wavesthat the vertical boundary layer velocity correction is very small.

The vertical velocity in each region must be the same as the motion at the interface (this is a kinematic boundary condition), so we have

(9.55) wherex(x, t )is the vertical displacement of the interface, assumed to be

x(x, t )= moei(b-ut) (9.56)



---PAGE-290---



274 Waves Over Real Seabeds Chap. 9

Linearizing the kinematic boundary condition yields

###### -=---ax a41 w2 o nz=-h

- (9.57)
- (9.58)
- (9.59)


at dz 82

###### or

-iamo =-kB = -dk

Thus

d = B

and

###### mo=--ikB

(7

The continuity of pressure, which states that the pressure must be the same on both sides of the interface (since it is free and is assumed to have no surface tension, it cannot develop a force), can be written (in linear form) as

p i =p2 on z =-h + x

###### or

on z =-h + x (9.60)

Note that the last term on the right-hand side is necessary due to the two fluid densities present. Linearizing,we obtain

- (9.61)

Substituting for 42,andz results in the followingequation relatingA toB:

- (9.62)


We have, however, already developed equations for A and B in terms of k [Eqs.(9.51)and (9.52)Jand by substituting forA andB,we find the dispersion relationship, or

gk (1+tanh kh)$ + (gk)2tanh kh =0

(9.63) This relationship, relatingk to 0,can be factored as

(I? -gk)d(2-+tanhkh1-(;:--11gktanhkh1=0 (9.64)



---PAGE-291---



Sec. 9.3 Water Waves Over a Viscous MudBottom 275

Thus two possible roots exist for waves propagating in the positive x direction:

d = g k (9.65) and

###### oz=

(9.66)

+tanh kh

PI

These two dispersion relationshipsare plotted in Figure 9.5.The two possible wave modes can be distinguishedby the ratio ofthe amplitudesofthe surface wave and interfacial wave, which is foreach case (Lamb, 1945)

-a0 = ekh (9.67a)

###### mo

0 0.5 1.o I .s 2.0 2.5 3.0

kh

Figure 9.5 The dispersion relationshipfor waves over an infinitely deep denser lower fluid. Note that the deep waterasymptotes are $/gk =(p2/pI- 1)@2/pI+ 1) for the model wave.



---PAGE-292---



5=-e-1)e-W (9.67b)

276 Waves Over Real Seabeds Chap. 9

###### mo

Therefore, the two casesaredistinguishedby which is larger,the surface or the interfacialamplitude,and whether the interfaceisin phase with or 180" out of phase with the free surface.

The first wave mode,c?=gk, isinteresting,asfrom Eq. (9.62),A / B = 1. The expressions for the two velocity potentials are

###### +,=+2 =Aek(h+z)el(k.-ct) (9.68)

Thus the two regions, above and below the interface, are indistinguishable. The presence of a lower, more dense layer has no effect on the wave motion. This result, which is only true for the case of an infinitely deep mud layer, results from the factthat the interface is a constant pressuresurface. Heuristically, we could remove the overlying water and the interfacial wave could propagate as a surface with the same (deep water) celerity. In shallow water, this would not be true as the interfacial wave no longer corresponds to a constant pressure surface.

For this mode of wave motion, there is no discontinuity of horizontal velocity across the interface and hence there is no boundary layer and no associated damping. (There would be damping if the mud were highly viscous, as damping would take place outside the boundary layers.) For the shallowwater case, damping does occur and Dalrymple and Liu (1978)have treated this problem.

The other wave mode with the large out-of-phase interfacial wave creates an unusual effectin the upper layer.Thefree surfacedisplacement can be viewed as a right-side-up wave, while the interfacial wave is an upsidedown wave propagating at the same speed and in the same direction. In between the two, it could be intuitively expected that a quasi-bottom might exist, and in fact, one does. At the elevation zo in the upper layer where w(x, zo)= -dc$/dz = 0, there is no vertical flow and this then is the false bottom. For this elevation, it can be shown (Problem 9.1) that the dispersion relationship in Eq. (9.66) reduces to

c? =gk tanh klzol (9.69) The damping in the lower layer is determined by matching the horizon-

tal velocities at the interface.

--=_-a+, +u2 atz=-h

(9.70) yielding f = ik(d - A ) or

ax dx

f = - - e (a2- gk) (9.71)

'0 kh

U



---PAGE-293---



Sec. 9.4 Waves Over Rigid, Porous Bottoms 277

The damping in the boundary layer is found as

- (9.72)
- (9.73)


Of the two possible wave modes discussed, the problem remains as to which mode is more “realistic.” The quotation marks are used as both solutions are in fact realistic, but the means by which the waves aregenerated determines the mode. For example, for waves propagating into a muddy region, it is probable that the first mode (d=gk)is the most likely one, as the wave lengths associated with the second mode are very short, particularly for small values ofp2/pl.However, asp2/pIbecomes large, it is possible that both modes are excited. If, on the other hand, the waves are generated at the interface by a displacement of the mud, it is more likely the second mode will be the only one present. This wave, which exists primarily at the interface, propagates very slowly, due to the fact that the restoring force which causes the wave to propagate is a result of the density differences between the two fluids.

- Example 9.3


Determine the wave lengths of the two possible modes of wave propagation over an infinitely deep mud layer, with p2/pI= 1.2. The overlying water column is 4.6 m in depth and the wave period is 8 s.

Solution. In Figure 9.5, the ordinate may be written as dh/gkh for convenience. d h/g is computed as 0.287 for this case. For mode 1 we have dh/gkh = 1 at kh =0.287. This yields a wave length of 100m. For the second mode, we have to use an iterative technique. If we guess kh = 2.0, from the figure we find for kh = 2.0 and pz/pI= 1.2 that dh/gkh 1:0.087. Dividing this number into d h / g yields kh; kh = 3.30.Therefore, an estimate of 2 for kh was too low. Now we estimate kh as 3.0, which yields dhlg = 0.09, or kh = 3.19. Iterating, we find that 3.16 is a good value. Therefore, L = 9.1 m. By comparison, the wave length ofthe wave over a rigid bottom

- at 4.6 m is 51 m.


###### 9.4 WAVES OVER RIGID, POROUS BOTTOMS

Sandy seabeds can be characterized as a porous medium, thus permitting mathematical treatment. Since Darcy’s experiments in the BOOS, investigators have treated soils as a continuum, with spatially averaged flows, rather than worrying about the flows in the tortuous channels between the sand grains. The solution of this problem will be similar to the preceding case.A governing equation will be developed for the flows in the bed;these flows will be matched to those induced by the waves in the fluid region, and the



---PAGE-294---



damping due to the forced flow in the granular medium will be calculated.

For a fullsaturated soil,which is assumed tobe incompressible (as is the fluid), the conservation of mass leads to

###### v . u = o (9.74)

whereu is the discharge velocity or the average velocity acrossa given area of soil (including both the intercepted areas of the soil particles and the pores between them). Darcy's law relates the velocity to the pressure gradients in the fluid:

K

u =--vp,

(9.75)

P

where K is a constant called the permeability, which is a characteristic of the soil, and p is the dynamic viscosity of the fluid.2The governing equation for the fluid in the soil is obtained by substituting for u into the conservation of mass equation, Eq. (9.74),or

v.(-;vp,j=0 (9.76)

or

v2ps= 0

Thus the pore pressure satisfies the Laplace equation, as does the velocity potential in the fluid. In order to match the two solutions, psand 6,the boundary conditions will be that the pressure be continuous across the soilwater interface, as are the vertical velocities.

The assunled progressive wave forms of (band psare

$(x, z)=[A cosh k(h +z) +B sinh k(h +z)] e'(kr-ur)

(9.77)

and

k(h+z) e~(kr-~t) (9.78)

pS(x,t )=De

The continuity of pressure across the interface requires that

P(X, -h) =P s k -h) (9.79)

where the subscript s again denotes the soil region pressure. Rewriting, we have

(9.SO)

'This equation, which neglects the acceleration terms, assumes that theflowcan be treatedquasistatically.An order-of-magnitude analysis bearsthis out for most sand beds.



---PAGE-295---



Sec. 9.4 Waves Over Rigid, Porous Bottoms 279

or

###### -iupA =D

For the vertical velocities to be continuous,

or

###### B = - -KD

(9.81)

###### P

So far we have two equations for the three unknowns A,B, and D;now we use the linear free surface boundary conditions to relate them to the wave amplitude a and to obtain the dispersion relationship. The linear dynamic free surface boundary condition yields

###### V = - - -a4--E ( A cash kh +B sinh kh)e'(k"-"')=&(h-"l)

(9.82) Substituting forA and B from above yields

###### g at g

D=pga(coshkh[1-(y)tanhMI}-' (9.83)

Application of the linear kinematic free surface boundary condition provides the dispersion relationship,

(9.84)

###### iua =Ak sinh kh +Bk cosh kh

or, substituting for a,A , and B, in terms ofD,results in

###### V

where v =p/p, the kinematic viscosity. Reordering gives

C)

###### d-gk tanh kh =-i - (gk-dtanh kh) (9.86)

This dispersion relationship is complex, yielding a complexk, which may be written as k =k, +ik,.The real part of k represents the real wave number, that is, it is related to the wavelength, while the imaginary component determines the spatial damping rate. This follows by examining the free surface profile,

###### (9.87)



---PAGE-296---



Thus there is exponential damping due to k,being greater than zero.

The quantity aK/v in Eq. (9.86) is generally small. For sand, K ranges from about to m2,while the kinematic viscosity is O(10-6).Therefore, aK/vranges from to which is small.

Approximate solutions can be obtained from the dispersion relationship. In intermediate depth we can replace coshkh =coshk,h +ik,hsinhk,h, as a priori we expect k,h << 1 ; similarly for sinh kh. Substituting into Eq. (9.86) for the hyperbolic functions and k, we can separate it into real and imaginary parts.

###### Real: (d-Rgk,)-Rgkihkr tanh k,h

=gk, tanh k,h -(gk,+Rd)k,h (9.88) Imaginary: (d-Rgk,)k,htanh k,h

###### =gk,(R +k,h)+(gk,+R d )tanh k,h (9.89)

where R = aK/v. Neglecting the small products of Rk, and k; in the real expression gives

c ? N gk, tanh k,h (9.90) while the second expression, after some algebra, yields

###### 2(aK/v)k; k, N

(9.91) as found by Reid and Kajiura (1957).This result is plotted in Figure 9.6.

###### 2k,h +sinh 2k,h

In shallow water, Ikh I <z/lO, the dispersion relationship can be written as

d-gk’h =-iRgk (1--”g”> (9.92) Substituting again k =k,+ik,and separating into real and imaginary parts gives

Real: d-g(k;?-kf)h= Rgk, (9.93)

Imaginary: 2gkrkih=-Rkrg (1 -$)

- (9.94)
- (9.95)
- (9.96)


Solving for kiand k,gives us

These expressions are more accurate in shallow water than the previous expressions. The shallow water asymptote for k,is (1/2h)(Ko/v).



---PAGE-297---



# 0.10'E7

###### Sec. 9.4 Waves Over Rigid, Porous Bottoms 281

2

I I I I I I l l

###### L

0.01 2 3 4 5 6 4 0 . 1

2 3 4 5 6 7 1.0 2 3 4 5 6 7 1 0 . 0

###### Shallow Deep

k0h

Figure9.6 Dimensionlessdampingcoefficientversus depth.

Liu (1973)included a laminar boundary layer at the fluid-soil interface, so as to eliminate the discontinuity in the horizontal velocity, and developed an approximate expression for the combined damping due to the porous media and the laminar boundary layer.These can be shown to O(aK/v)to be the sum ofthedamping rates dueto the porous media, Eq.(9.91),and that due to the laminar boundary layer, Eq. (9.27):

###### k;=2krh+2krsinh 2k,h ( ? + k r g ) (9.97)

The damping rate ofenergy per unit time and per unit area ED is related by k,by the energy conservation equation,

###### (9.98)



---PAGE-298---



282 Waves Over Real Seabeds Chap. 9

or approximately for a constant depth and E = pgaie-2kix,

pg2a2Kkr

- (9.99)
- (9.100)


ED = 2 v cosh2krh for the porous damping alone and

ED = -+-

including the laminar boundary layer.

###### REFERENCES

DALRYMPLE,R. A., and F? L.-E LIU,“Waves over Soft Muds: A Two-Layer Fluid GADE,H. G., “Effectsofa Non-rigid Impermeable Bottom on Plane SurfaceWaves in JONSSON,I. G., “Wave Boundary Layers,” Proc. 10th Con$ Coastal Eng., ASCE, JONSSON,I. G., and N. A. CARLSEN,“Experimental andTheoretical Investigations in

Model,” J. Phys. Ocean.,Vol.8, pp. 1121-1131, 1978. ShallowWater,”J. Max Res.,Vol. 16, pp. 61-82,1958. Tokyo, 1966, pp. 127-148.

an Oscillatory RoughTurbulent Boundary Layer,”J. HydraulicsRes.,Vol. 14,1976. KAJIURA,K., “A Model of the Bottom Boundary Layer in Water Waves,” Bull.

Earthquake Res. Znst. (Japan),VoL 46, pp. 75-123,1968. KAMPHUIJS.,W., “Friction Factor under Oscillatory Waves,” J. Waterways, Harbors

Coastal Eng. Div.,ASCE,Vol. 101,pp. 135-144,1975. LAMB,H., Hydrodynamics,Dover, NewYork, 1945. LIU,I? L.-E, “Damping ofwaterWaves over Porous Bed,” J. Hydraulics DIV.,ASCE, MEI,C. C., and F? L.-E LIU,“A Note on the Damping of Surface Gravity Waves in a

Vol. 99, pp. 2263-2271, 1973.

Bounded Liquid,” J. Fluid Mech.,Vol. 59, p. 279,1973.

PHILLIPS,0. M., The Dynamics of the Upper Ocean, Cambridge University Press,

Cambridge, 1966.

REID,R. O., and K. KAJIURA,“On the Damping of Gravity Waves over a Permeable Seabed,” Trans.Am. Geophys. Union,Vol. 38,1957.

WELLS,J.T.,andJ. M. COLEMAN,“Longshore Transport of Mud by Waves: Northeastern Coast of South America,” in H. J. MacGillavry and D. J. Beets (eds.), 8th Caribbean Geol. Conf. (Willemstad), Geol.Mijnbouw,Vol. 57, pp. 353-359, 1978.

###### PROBLEMS

Show that the dispersion relationship given for waves propagating over a viscous mud can be expressed as d =gk tanh k JZOI [Eq. (9.69)]. For Example 9.3, find the damping ED for both modes.

9.1

9.2



---PAGE-299---



###### Chap.9 Problems 283

- 9.3 Develop and solve the boundary value problem for waves propagating over a porous layer of thicknessd.
- 9.4 The dynamic bottom pressure under a wave can be written as

pg a cos (kx-at) Ax, -W = cosh kh

With this as the boundary condition at z =-h for the pressure pr(x,z ) in a porous medium, develop the expression forps(x,z).Compare this solution to that obtained in the text. What are the physical differences?

Relate the laminar damping under a progressive wave with distance [Eq. (9.27)] to the damped long wave [Eq. (5.80)]. What isfin terms of for the long wave? Why the difference from Eq. (9.18)?

- 9.5




---PAGE-300---



###### 10

###### Nonlinear Properties Derivable from Small-Amplitude Waves

###### Dedication HERMANN LUDWIG FERDINAND VON HELMHOLTZ

Hermann Ludwig Ferdinand von Helmholtz (1821-1894) was born in Potsdam, southwest of Berlin. The dedication of this chapter to Helmholtzis inrecognitionof his extensive contributions to fluiddynamics and physics in general. While he did work in the area of waves, his major contributionto this text isthe Helmholtzequation, which governs the motionof waves in harbors.

Helmholtz enteredthe Pepiniere Berlin Universityin 1838to study medicine. During his formal education, Gustav Magnus and others influenced him to expand his interest to natural sciences. In 1842 he graduated, successfully defending his work on ganglia. From 1842 to 1845,simultaneousto Kelvin’sactivities,he investigatedthe mechanical equivalent of heat. In 1849 he took a professorship in physiology at Konigsburg, where he developed an interest in the importance of electricityinthe working of the human body and studied ophthalmology and color vision. In 1855 he movedto Bonn and in 1858to another chair at Heidelberg.There he developed his theories on vortex motion, free streamline flows, and the viscosity of water. In 1871 he succeeded Magnus at the University of Berlin, where he built a physical sciences institute which educated many well-known scientists, such as Heinrich Hertz and Max Planck. Planck has been quoted as observing: “Wir hatten das Gefuhl, dass er sich selber mindestens ebenso langweilte wie wir” (“We had the feeling that he himselfwas at leastas boredas we

284



---PAGE-301---



Sec. 10.2 Mass Transportand Momentum Flux 285

were”). Clearly, he engenderedatestimonial distinctfrom the one Lamb received from his students.

In 1883 Helmholtzbecame a Prussian noble in recognition of his scientific contributions. In 1888 he assumed the leadership of the PhysicalTechnical Government Institute (Reichsanstalt) in Charlottenburg, West Berlin.

Other areas of interest for Helmholtz included the physiology of optics, binocularvision, acoustics, and the physiologyof the ear, sound (harmony),and electrodynamics.

###### 10.1 INTRODUCTION

Wave energy and power, which were derived in Chapter 4, are nonlinear quantities obtained from the linear wave theory-nonlinear in the sense that they involve the wave height to the second power. In this chapter other nonlinear quantities will be sought which have a bearing on coastal and ocean design.These quantities, which are time averaged, are correct to second order in ak,yet have their origin strictly in linear theory. InChapter 11 a further and more complete study of nonlinear waves is undertaken.

###### 10.2 MASS TRANSPORT AND MOMENTUM FLUX

If a small neutrally buoyant float is placed in a wave tank and its trajectory traced as waves pass by, a small mean motion in the direction of the waves can be observed. The closer to the water surface, the greater the tendency for this net motion.Thismotion of the float, which is indicative of the mean fluid motion, is a nonlinear effect, as the trajectory of the water particles from linear theory are predicted to be closed ellipses (see Chapter 4).

There are two approaches for examining this mass transport: the Eulerian frame, using a fixed point to measure the mean flux of mass, or the Lagrangian frame, which involves moving with the water particles.

10.2.1 Eulerian Mass Transport

Examining the horizontal velocity at any point below the water surface and averaging over a wave period shows that

(10.1)

However, in the region between the trough and the wave crest, the horizontal velocity must be obtained by the Taylor series. For example, for the surface velocities we have, approximately,’

‘Neglectingsome contributions from second-order theory.



---PAGE-302---



286 NonlinearProperties Derivablefrom Small-Amplitude Waves Chap. 10

(10.2) cos (kx-at)+ga2k2~ tanh kh cost(kx-at)

###### gak cosh k(h +z)

---

a cash kh

Z=O a

---gak cos(kx-at)+a2kacos2(kx-at)

###### a

The surfacevelocity is periodic, yet faster at the wave crest than at the wave trough, as the second term is always positive at these two phase positions. This asymmetry of velocity indicates that more fluid moves in the wave direction under the wave crest than in the trough region.This is, in fact, true. If we average u(x,q) over a wave period (an operation denoted by an overbar), there is a mean transport of wate?

###### u(x, a2ku (ka)’C

###### q)dt =~ =~

(10.3)

2 2

To obtain the total mean flux, or flow of mass, we perform the following integration, whereM is defined as the mass transport

(10.4)

a result first presented by Starr (1947).Note that the first term in Eq. (10.4)is zero; again, there is no mean flow except due to the contribution of the region bounded verticallyby q.Thedepth-averaged time-mean velocity,due to mass transport, is

(10.5)

10.2.2 LagrangianMass Transport

The Eulerian velocity discussed above is obtained by examining the velocity at a fixed point. A Lagrangian velocity is one obtained by moving with a particle as it changes location. The velocity of a particular water particle with a mean position of(xl,zI)isu(xl+C,zI+0,where rand rare locations on the trajectory of the particle. An approximation to the instantaneous velocity is

(10.6)

’Clearly, u(x,q)is much less than the phase speedofthe wave, C.



---PAGE-303---



Sec. 10.3 MeanWater Level 287

Using the values of the trajectory obtained in Chapter 4 [Eqs. (4.9) and (4.10) evaluated at (xl,ZJ], uLcan be written as

gak cosh k(h +z )

UL=- cos (kx - Ct) (10.7)

o cosh kh

+ [cosh’k(h +z) sin2(kx-ot)+sinh’ k(h +z) cos’ (kx-ot)]

sinh’ kh The mean value of uLis

a’ok cosh 2k(h +z) -ga’k’ cosh 2k(h +z)

U L(XI +c,ZI +4= -

-

(10.8)

2 sinh’ kh o sinh 2kh

This mean Lagrangian velocity indicates that the water particles drift in the direction of the waves and move more rapidly at the surface than at the bottom.

Integrating over the water column to obtain the total transport and multiplying by the density of the fluid yields, as before,

(10.9)

- 10.3 MEAN WATER LEVEL The Bernoulli equation at the free surface, Eq. (3.13), is


Expanding to the free surfaceby theTaylor series yields tofirst order in qafter time averaging (which is denoted by the overbar),

###### (a+/a~)~+(a+/az)~- a’+ -

+gq -q- =C(t)

(10.11)

2 at az

where is a mean displacement in water level from z = 0. Substituting for q and 4 from the linear progressive wave theory, we have

(10.12)

There areseveral choices for C(t)here, depending on the problem. Ifthe problem is one ofwaves propagating from deep to shallow water,a customary

boundary condition is iiszeroin deepwater,whichfixesc(t)=0 everywhere.Thus i is alwaysnegative,becoming more so as the wave enters shallowwater until breaking commences.This is called the setdown. Alternatively, we can force the x axis (z =0)to be the mean water level at some fixed



---PAGE-304---



###### 288 Nonlinear PropertiesDerivablefrom Small-AmplitudeWaves Chap. 10

-

xIby setting C(t)=Axl)gin Eq. (10.12),wherefis now a constant.As another example, in an enclosed tank where the amount of water in the tank must be conserved, a continuity argument must be invoked for C(t).If the tank is of length 1,then

__

1J'$x) dx=0

- (10.13a)
- (10.13b) The mean water level associated with standing waves is


###### I

or, from Eq. (10.12),

___

-q=- C(t)+ (cosh 2kh cos 2kx - 1)

g 4sinh2kh This is left as an exercise for the reader (Problem 10.3).

###### 10.4 MEAN PRESSURE

The mean pressure under a wave can be most easily obtained by timeaveraging the Bernoulli equation:

d+ u2+w2 p(z)=p--p--pgz+C(t)

- (10.14a)
- (10.14b)


dt 2

or

- u2+ wL p(z)=-p 7-pgz +C(t)

L

under a progressive wave. Ifc(t)=0,the case for shoaling progressive waves, then it is clear that the mean pressure is decreased from its hydrostatic value.

- As (u, w)decrease with depth into the water, the mean pressure approaches hydrostatic with depth. Substituting into the equation above yields


pgu2kcosh 2k(h +z) p(z) = 2 sinh 2kh

- -Pgz (10.15) Alternatively,ifthe coordinate system is located at the mean water level such

thatc(t)=f(xl)gand =0,itcanbeshownthat

P(Z*) = -pw2 -pgz* (10.16) from the z of the other coordinate system (see Fig-

~

where z* differs by ure 10.1).



---PAGE-305---



Sec. 10.5 Momentum Flux 289

.I /--

Still water level [~(r)= 01 Mean water level [@)= fgl

Figure 10.1

The two vertical reference systems and associated Bernoulli con-

stants.

Under a standing wave of amplitude a ,

p(z)=- pga2k [cosh2k(h +z)-cos2kx]-pgz (10.17)

4sinh 2kh and at the bottom,

p(-h) = pgaZk (cos2kx - 1 ) +pgh

(10.18)

4sinh 2kh

10.5 MOMENTUM FLUX

- At a point above the trough level, there is a mean momentum fluxas well as mass flux. The mean vertically averaged momentum flux correct to second order in ku is


(10.19)

whereC,is the groupvelocity, the speed at which the wave energy propagates.

The flux of momentum in the direction of the wave past a section and the pressure force per unit width is defined as

I,=MC,+l:p(z)dz (10.20)

From Newton’s second law, this quantity is unchanged between any two sections unless forces are applied. Evaluating the last integral yields the expression

I, =MC, +fpgh’

- (10.21)
- (10.22)


1,can be rewritten as

Z, =S, +4pg(h+$’



---PAGE-306---



290 Nonlinear Properties Derivablefrom Small-Amplitude Waves Chap. 10

where S, is the radiation stress in the direction of the waves.

S, I:P (Z )dz-tpg(h+i)’+MC,=E(2n-i) (10.23)

The difference between the two forms for Z is that the latter explicitly

includes the mean water level i.Each form is important for different

applications. For the flux of momentum transverse to the wave direction, we have

rn

____.-

(10.24) The sum of momentum flux and pressure force in the transverse

direction is

I,=1:p(z)dz=tpgh2

or

where

= -pghi to O(ka)2

###### =E(n-t )

If a progressive wave is propagating at some angle 8to the x axis, then S,, and S, are modified to the following forms:

(10.25) (10.26)

in which n is the ratio of group velocity to wave celerity (n= CG/C).In addition, for this case there is an additional term representing the flux in the x direction of the y component of momentum, denoted Sxy:

###### S,,=Ibpuvdz=Ibp(uv)dz (10.27)

v 0

and employing linear wave theory, it can be shown that

S --nl5 sin28

(10.28)

xy- 2



---PAGE-307---



Sec. 10.5 MomentumFlux 291

It is of interest to note that, if the bathymetry is composed of straight and parallel contours and if no energy dissipation or additions occur, there is no change in Sxyfrom deep to shallow water.

For further information on radiation stressesand their uses, the reader is referred to Longuet-Higgins and Stewart (1964), Longuet-Higgins (1976), and Phillips (1966).

Example10.1:Wave Setdownand Setup

As waves shoal and break on a beach, the momentum flux in the onshore direction is reduced and results in compensating forceson the water column. Consider a train of waves encountering the coast with normal incidence. For a short distance dx (Figure 10.2), a force balance can be developed

###### I , =1 2 -Rx (10.29a) dI dx dI dx dx 2 dx 2

I --_= I + R,

(10.29b)

or finally,

dI dx -dX=R,

(10.29~)

using the Taylor series expansion, where I is evaluated at the center and R, is the reaction force ofthebottom in the(-x)direction. Using the radiation stress approach,

###### 6=d[sxx+;pg(h+ij)2]

###### dx dx

(10.30)

Figure 10.2 Schematic diagram for calculation ofwave setup or setdown.



---PAGE-308---



292 Nonlinear Properties Derivable from Small-Amplitude Waves Chap. 10

For a mildly sloping bottom, the reaction force R is due to the weight of the column of fluid and thus

- dh dx

Rx =pg(h + q)-dx

Substituting yields

###### 1 dS,, dt] pg(h + t]) dx dx

- ~ _ _ = - (10.31)

There is therefore a change in mean water surface slope whenever there is a change in S.,. The change in offshore of the breaker line is described by Eq. (10.12), which describes a gradual reduction of the mean water level as the shoreline is approached.Atx =xb,the breaker line, the wave amplitudeisa =K (h +$12, whereK isthe breaking index (Chapter4)9and 6(in shallow water) is

asgiven by Longuet-Higgins and Stewart (1964)or

(10.32)

The setdown therefore is less than 5%of the breaking depth for K = 0.8. the setupis found from the force balance, Eq. (10.31):

Inside the surf zone, where a(x)=K(h+$12, based on a spilling breaker model,

Simplifying yields

- (10.33)
- (10.34)


Finally,

Evaluating the constant at x =xb, the breaker h e , where r] = l]b, gives finally

###### -Nx)=tb+ 3'/8 [hb-h(x)]

(10.35)

1+ 3d/8

The mean water surface displacement thus increases linearly with depth asthe shore isapproached.This water surface slope provides a hydrostatic pressure gradient directed offshore to counter the change of wave momentum by breaking across the shoreline.

(10.36)



---PAGE-309---



Chap. 10 References 293 or, for K =0.8, i(0)is about 15% ofthe breaker depth or about 19% ofthebreaking wave height.

Example 10.2:Applied LongshoreWave Thrust

For waves propagating obliquely into the surfzone, breaking will result in a reduction in wave energy and an associated decrease in S,, [cf.Eq. (10.28)],which is manifested as an applied longshore wave thrust F, on the surf zone. For straight and parallel bottom contours, thrust per unit area is given by

###### F

(10.37)

Y - dX

Thus gradients of the momentum flux terms provide a useful framework for the drivingforces in the nearshore zone. In the present case, the longshore wave thrust per unit area is resisted by shear stresses on the bottom and lateral faces of the water column (Longuet-Higgins, 1970).

###### 10.6 SUMMARY

The results of linear wave theory may be used to calculate nonlinear mean quantities, correct to second order in ku. These quantities, such as mass transport and mean momentum flux, play a major role in coastal engineering. In fact, the mean momentum flux of the waves in the longshore direction, relative to a coastline, is related to the currents engendered at the coastline and the amounts of sediments transported along the coast. See, for an overview, the book by Komar (1976). In the open ocean, the mean momentum flux results in the drifting of objects, such as ships, ice flows, and oil slicks.

###### REFERENCES

KOMAR,€! D., Beach Processes and Sedimentation, Prentice-Hall, Englewood Cliffs, N.J. 1976. LONGUET-HIGGINS,M. S.,“Longshore Currents Generated by Obliquely Incident Sea Waves, 1,”J. Geophys. Rex,Vol. 75, No. 33, 1970.

LONGUET-HIGGINSM,. S., “The Mean Forces Exerted by Waves on Floating or Submerged Bodies, with Applications to Sand Bars and Wave Power Machines,” Proc. Roy. SOC.A,Vol. 106, June 1976.

LONGUET-HIGGINS,M. S.,and R. W. STEWART,“Radiation Stresses in Water Waves:A Physical Discussion with Applications,” Deep-sea Res.,Vol. 2, 1964. PHILLIPS,0. M., The Dynamics ofthe Upper Ocean, Cambridge University Press,

Cambridge, 1966.

STARR,V. I?, “A Momentum Integral for SurfaceWaves in Deep Water,”J. Mar. Rex,

Vol. 6, No. 2, 1947.



---PAGE-310---



294 Nonlinear Properties Derivable from Small-Amplitude Waves Chap. 10

###### PROBLEMS

- 10.1 Determine the mean water level due to a wave train impinging on a perfectly reflecting vertical wall with an angle 8.
- 10.2 Calculate the mean water level associated with an edge wave,

,# , = e-k(yco$-zsinp) cos kx sin at

0

wherey is positive offshore, x is alongshore, and/3 is the bottom slope.

- 10.3 Show that the setdown under a standingwave system is

~

V ( X ) = a2k (cosh2kh cos 2kx - 1)

4 sinh 2kh

- 10.4 Show by two different methods that for the origin of the vertical coordinate taken at the mean water line, the mean pressure for a progressive wave system

is

~-

p =-pgz -pw2

One method is suggested in the paragraph following Eq. (10.15). A second method involves integration of the vertical equation of motion from an arbitrary depth z up to the free surface, the use of the Leibniz rule, and time averaging over a wave period.

- 10.5 For the case of straight and parallel bottom contours, combine energy conservation consideration with Snell's law to demonstrate that S, is the same from deep to shallow water.
- 10.6 Verify Eqs. (10.25) and (10.26) for the radiation stresses developed by a wave train traveling at an angle '6 to the x axis. Use &x, y , z, t ) as developed in Chapter 4.




---PAGE-311---



###### Nonlinear Waves

Dedication

###### SIR GEORGE GABRIEL STOKES

Sir George Gabriel Stokes (1819-1903) was born in Skreen, Ireland.He entered Bristol College at 16 and matriculated at Pembroke College, Cambridge, in 1837. He became a Fellow of PembrokeCollege in 1841 and in 1849 received the Lucasian Professorship of Mathematics at Cambridge-the same professorship held by Airy from 1826.To bolster his teaching salary he also taught at the Government School of Mines.

Stokes's contributions range from optics, acoustics, and hydrodynamicsto viscous fluid problems(a unit of viscosity is namedfor him) and to the proof that the wave of maximum height has a crest angle of 120". He also did a great deal of work related to the concept of ether which was hypothesizedto exist between the planets and stars.

In1842hesolved three-dimensional flow problems by introducing an axisymmetric stream function. In 1849 he developed the dynamical theory of diffraction using Bessels series and Fourier integral theory, and in 1852 he received the Rumford Medalof the RoyalSociety for the discovery of the nature of natural fluorescence.

His inclusion in this chapter derives from the development of Stokes waves, large-amplitude waves that he conceived through a nonlinearwave theory.This theory, althoughusuallyextendedto higher orders of accuracy than he was able to achieve, remains in use today.

In 1845 Stokes produced a number of papers on viscousflow. He was unaware that the French scientists Navier, Poisson, and St.-Venant had treated these problems, and he independently derived the nowcalled Navier-Stokes equations.

Stokes received a number of awards and prizes as well as numerous honorary doctorates for his work, a process that culminated in 1889when he became a Baronet.

295



---PAGE-312---



296 Nonlinear Waves Chap. 1 1

###### 11.IINTRODUCTION

The water waves that have been discussed thus far have been small-amplitude waves, which satisfied linearized forms of the kinematic and dynamic free surface boundary conditions. We have seen that the linear wave theory has been useful in many respects, even when the requirements of linear theory, small kH/2, have been violated. In this chapter, extension of the linear theory to a second-order Stokes (1847)theory and then an “any”-order theory will be developed. The desire is to develop a water wave theory to best satisfy the mathematical formulation of the water wave theory. In shallow water a different expansion will then be explored, where the classical Stokes expansion is inefficient.

###### 11.2 PERTURBATION APPROACH OF STOKES

Reviewing the periodic water wave boundary value problem for waves propagating in the +x direction, we have linear and nonlinear boundary conditions applied to a linear governing differential equation.

11.2.1 Linear Equation and Boundary Conditions

V24=0 governing differential equation (11.1) _-=” 0 on z =-h bottom boundary condition (11.2)

az

&x, z, t )=+(x +L,z, t) lateral boundary condition $(x, z, t )=&x, z, t + 7‘) periodicity requirement

(11.3) (11.4)

1 1.2.2 Nonlinear Boundary Conditions

Dynamic free surface boundary condition (DFSBC):

Kinematic free surface boundary condition (KFSBC):

(11.6) It is convenient at this juncture to put the governing equations and the

related boundary conditions into dimensionless forms. We define the follow-



---PAGE-313---



Sec. 11.2 Perturbation Approach of Stokes 297

ing dimensionless variables, developed in terms of g , a, and k, which are gravity, the wave amplitude, and the wave number, respectively.

###### X = kx Z = kz

T = & E t

The governing equation is thus

###### -+-=oa2@ a2@

ax2 az2 (11.7)

The periodicity and lateral boundary conditions remain the same in dimensionless form; however, the free surface boundary conditions are modified to be

P +(ka)’ + -(ku)-a@+2 = Q(t) on Z =kun (11.8)

2 dT

where P will be taken as zero on the free surface. (Note that if ku = 0, then Z = 0; there are no waves and therefore only a trivial solution exists.) The KFSBCbecomes

an aadn am

_- --= -- on 2 = kun (11.9)

dT (ka)axax az

In our previous derivation of small-amplitude wave theory, we expanded the nonlinear conditions about Z = 0, the mean water level, and then neglected products of very small quantities, such as (da>/~3X)~.This clearly was neglecting terms of order (ku)’when compared to ku.

In the perturbation approach, we will assume that the solution will



---PAGE-314---



298 Nonlinear Waves Chap. 1 1 depend on the presumed small quantity ka, which we will define as E. The linear solution will not depend on E, while the second order will, the third order will depend on E’, and so on. Therefore, we will decompose all quantities into a power series in E , which is presumed to be less than unity. n=nI+En2+E2n3+’ * * @=@ I + +c2@3+ . . . 0=01+€ 0 2 +€203 + * * *

(I1.10) Q(t)=EQI(T)+ E’Qz(T)+e3Q3(T)+ * . *

Again, as we a priori do not know the location of the free surface Z = (ku)n(X,T), we will resort to expanding the nonlinear free surface boundary conditions about Z = 0 in terms of ell, retaining the higher-order terms up to E’, denoted as O(E’).Using the Taylor series we have

###### Q(t) o nZ =O

and

###### ( az axax a@ an man) a;( a@ az ar axax

+€-- +En- --+€-- (11.12)

###### e2n2a3@

- 0 o nZ =O

###### 2 az3

wherewe have accounted forthe factthat n and Q(T)are not functions of

elevation.

Substituting the perturbation expansions, Eqs. (1l.lO), into the linear conditions, Eqs. (11.I) to (11.4),we have, retaining only terms of first order in E (the others being much smaller)

v2@l+€V2@,2+ . . . =0 (11.13)

a@,az E a@dzL + . . . = O atZ=-kh @I(X,z,r)+€@Z(X,2,T)+ * . . =@I(X+L,z,T)+E@*(X+L,z,T) @l(X,Z, T)+€@2(X,Z, T)+ * * * =@I(X,Z , T + Tp)+€@2(X,2,T + Tp)

where Tpis the dimensionless wave period, 27~10.At the free surface, we obtain for the DFSBC and KFSBC, respectively:



---PAGE-315---



Sec. 11.2 Perturbation Approachof Stokes 299

f[(37+(271-3- 3+n,+ (11.14)

###### I . . .

2 ax aT aT - aT-a2cPaz

= Qi(V+~Q2(r). * * onZ=O (11.15) = O onZ=O

am an, anZ m,an, a2@, az az aT aT ax ax az2

###### ---€ _ _ _ _ _ _ E-+E---En

I - " '

The original nonlinear boundary value problem has now been reformulated into an infinite set of linear equations of ascending orders.To visualize the manner in which the linear equations are obtained, consider the following general form of the perturbed equations:

Al +€ A 2 +€'A3 * . . =BI +E B+~€'B3 . 1 * (11.16)

The required condition that the equality holds for arbitrary Eis that the

coefficientsof like powers of E must be equal. Therefore,

A1 = BI A2 =B2 A3= B3, etc.

This procedure will now be used to separate the equations by order.

11.2.3 First-Order Perturbation Equations

If we gather together all the terms that do not depend on E, the linear equations result.

V2@, =0

8%-0 onZ=-kh dZ

onZ=O (11.17)

anl aaI onZ=O

--aT az

@IW,z,r)=@I(X+2x,2,T) @i(x,Z, r)=@i(X,2,T + Tp)

These are the equations that were used in Chapter 3.



---PAGE-316---



300 Nonlinear Waves Chap. 11

The solutions are, in dimensionless form,

n=cos(X- OT)

- (11.18)
- (11.19)


O: =tanh kh Q i(r> =0

which in dimensional form are Eqs. (3.42), (3.43),and (3.34).

11.2.4 Second-Order Perturbation Equation

Tothe order of E ,

v2a2 = 0

aa2-0 onZ=-kh

az

am2 anz aa,an, a2al onZ=O

+n,-

###### az ar ax ax az2

n, --aaz-Q 2 ( T ) = - 0

onZ=O

ar

###### @2(X z,r)=%(X +2n, z,T) @Ax,z,T)=@2(x,z,T +Tp)

Note that all the equations and conditions are linear in the variables of interest,Q2(X,2,T)and n2(X,T),but the free surface boundary conditions have inhomogeneous terms that depend on the first-order solution. Sincethe first-order solution is known, the terms on the right-hand side are known also.

To solve for the second-order solution it is convenient to use the combined free surfaceboundary condition, which is found by eliminating 112 from the free surface conditions,

(11.20)

For convenience, the right-hand side of this expression will be defined as D.



---PAGE-317---



Sec. 11.2 Perturbation Approach of Stokes 301

Substituting for @, and n,from Eqs. (11.18) into the expressionfor D and

using trigonometric identities, it is possible to express D simply as

###### 3wi sinh 2kh

D = sin 2(X - oT) (11.21) As a trial solution for Q2(X,Z, T),the following form is taken:

###### @2(X,2,T)=a2cosh 2(kh+Z )sin 2(X -wT) (11.22)

which satisfies the Laplace equation and the bottom boundary condition. Examining the second-order combined free surface boundary condition, Eq. (11.20),it is clear that dQz(T)/dT =0,as it cannot depend on sin 2(X - wT)as do all the other terms (beingonly a function of time), and thus the inequality could not otherwise be satisfied. Therefore, Q2(t)=constant, Q2.Substituting

into the combined condition yields a2. 3 w 8 sinh4kh

###### a 2 = - - (11.23)

Therefore,

To determine the corresponding free surface elevation, n2(X,T), the second-order dynamic free surface boundary condition is used,

###### on Z = 0 (11.25)

dT

Substituting for Q2and QIyields, in dimensional form,

H2 d 16 g sinh’ kh

[cash2kh +cos 2(kx-~ t ) ] (11.26)

+Q*---I

+1H2aZ[I +cos 2(kx-a)]

###### 8g

where H , is the first-order wave height (HI= 2a).

There are two options that can be applied to this equation in order to proceed. First, as in Chapter 10, we can specify the Bernoulli constant to be zero, corresponding to no setdown in deep water and then separating q into a mean andafluctuating6term.

472=i +$2 (11.27)



---PAGE-318---



302 NonlinearWaves Chap. 11

and from Eq. (11.26),

-q = - H;a2 = -

H:k 8 sinh 2kh

###### (11.28)

16 g sinh’ kh

- as in Chapter 10,and

( 11.29)

- ka2coshkh

q 2 = 4 sinh3kh

--(2 +cash 2kh)cos2 ( h-at)

The second alternative is to specifyh asthe mean water level depth and then qhas a zero mean. Then the Bernoulli constant is

‘=16sinh’H:c?kh

(11.30)

and the fluctuatingpart of q2, as before is given by Eq. (11.29).The resulting second-orderwave profile is much more peaked at the wave crest and flatter

- at the wave troughs than the previous sinusoidalwave form. Thisisshown in Figure 11.1.


The velocity potential and water surface displacement,to second order then, in dimensional form are

###### 4 =€4,+E242

( 11.31)

and q=cql+e2q2 (11.32)

1.o

0

- -1.0
- -1.0‘ I


Figure 11.1 A second-order stokes water surface profile as composed of q, and eq2contributions where E = ku.



---PAGE-319---



Sec. 11.2 Perturbation Approach of Stokes 303

###### HI

q=-cos(kx-at)+-

H’k ‘Osh kh (2+cosh 2kh)cos 2(kx-at)

2 16 sinh3kh

The dispersion equation relating ato k remains the same,

d =gk tanh kh (11.33)

However, it is noted that a correction occurs to the dispersion equation at the third order.

Convergence. A measure of the validity of the Stokes expansion procedure is whether or not the series for 4 converges. This can be checked for the second-order theory by examining the ratio of the second-order term to the first-order term, which must be less than 1 in order for the series for4, Eq. (ll.lO), to converge.’

€4’ 3 kacosh2kh << 4,

###### R=-=-

(11.34) 8 cosh kh sinh3kh

In deep water, defined as kh > n,the asymptotic forms of hyperbolic

functions can be substituted to reduce R to

R = 3e-2khka ( 11.35 )

R is thus very small in deep water, particularly since ka has been assumed small previously. The highest value in deep water would occur for kh = n, ku = n/7,occurring for the wave of maximum steepness,

or

###### 3K 7

(11.36) In shallow water, kh < n/lO, the hyperbolic functions can again be

R =-e-’” = 0.0025

replaced by the asymptotic values,

###### R=--=-3ka 3 ($)<,

(11.37)

8 k3h3 64n’

The relative depth kh thus becomes an important parameter in shallow water. In fact,ku < 8(I~h)~/3;this is a severe restriction on wave height, as this can be written as a/h < (8/3)(kh)’,where kh is small.The maximum that the ratio u/h can obtain is a/h = 8n2/300for kh =n/10, or the maximum wave amplitude is about one-fourth of the water depth. (In shallower water, this ratio must decrease.) However, as mentioned in Chapter 4,the wave amplitude for breaking is almost 0.4 the water depth. Therefore, for high waves in

then+1termdividedby thenthtermbe lessthanunityasn-co.

‘Properlyforthe power seriesfor4in termsofE toconverge, theratio test requiresthat ratioof



---PAGE-320---



304 Nonlinear Waves Chap. 1 1

shallow water, the Stokes expansion is not very good, at least when carried out to only the second order.

The term in parentheses in Eq. (11.37)is called the Ursell parameter (Ursell, 1953), which, for second-order Stokes theory to be valid, has a magnitude

###### L2H 64n2 h3 3

###### -<<- ( 11.38)

The value of the Ursell parameter actually should be less than indicated above, due to the fact that in shallow water the theoretical wave form will develop an anomalous bump in the trough for large waves due to the largeness of the second-order term. To investigate this, the free surface equation will be examined at the trough and the second derivative will be obtained. From the calculus, a negative second derivative indicates a concave downward curvature, or, for this application, a secondary crest or bump.

H V T = 2 16 sinh3kh

H2k‘Osh kh(2 +cosh 2kh)cos2(kx -a) (11.39)

-cos(kx- at)+-

and

###### - = - k 2 - - H2k3‘Osh kh(2+cosh 2kh) ax2 2 4 sinh3kh

for kx - crt = n (11.40) Setting the second equation to zero and solving for ka yields

sinh3kh cosh kh(2+cosh 2kh)

###### ka = (11.41)

This is the maximum value of ka for which there is no bump in the trough. In

deep water,the maximum permissible ka from this equation is 4,whichis

greater than the limiting steepness value of n/7;therefore, in deep water a secondary crest will not occur in the wave profile, while in shallow water, the maximum value of ka is

###### (11.42)

In comparing this rate to that for R, determined previously, this latter condition is eight times more stringent. In fact, the Ursell parameter reduces to

###### L ~ H 8n2

-<-

(11.43) Therefore, for shallow water, the requirement that the wave be singlecrested

###### h3 3



---PAGE-321---



Sec. 11.3 The Stream FunctionWave Theory 305

should be used as the criterion for the maximum height wave. This idea has been used for fifth-order Stokes waves by Ebbesmeyer (1974).

Kinematics. The velocities under the second-order wave are, in dimensional form,

3 H2akcosh 2k(h +z )cos2(kx -at)

+-16 sinh4kh

(11.44)

w=--=--’6 gk sinh k(h +z, sin (kx -at) dz 2 a cosh kh 3 H2aksinh 2k(h +z)sin 2(kx-at) 16 sinh4kh

###### +-

The presence of the second-order term increases the velocities, but in a manner that varies along the wave due to the 2(kx - at)phase function. For the horizontal velocity the velocities are greater under the crest but are reduced under the trough when compared to linear wave theory.

The total horizontal acceleration is, to second order,

Du-=- H cosh k(h + z ) H 2 sin 2(kx - at) (11.45) Dt 2 gk cosh kh 4 sinh 2kh

###### sin (kx- oi)--gk2

+- H2dk cosh 2k(h +z )sin 2(kx-at)

8 sinh4kh

The total vertical acceleration isfound similarly (see Problem 11.1).

###### 11.3 THE STREAM FUNCTIONWAVE THEORY

Should the reader have followedthrough the details of the second-orderwave theory, it would have been quite arduous. Clearly, higher-order Stokian wave theories [third order, Borgman and Chappelear (1958);fifth order, Skjelbreia and Hendrickson (1961)l become quite difficult. Expanding to even higher orders becomes extremely formidable. For this reason, it was desirable to have wave theories that could be developed on the computer to any order. The first such theory was developed by Chappelear (1961) involving the use of the velocity potential. Dean (1965) used the stream function to develop the stream function wave theory, which was computationally simpler than Chappelear’s technique.



---PAGE-322---



306 NonlinearWaves Chap. 11

Cokelet (1977) has extended the method originally developed by Schwartz(1974) to allow a very accurate calculation of the characteristics of water waves, including heights ranging up to near breaking. The procedure involves expressing the complex potential solution in a Fourier series and represents the Fourier coefficients as series in terms of a perturbation parameter. An interesting result is that the wave speed, wave energy, and wave momentum all exhibit maxima atwave heights slightly smaller than the breaking height.

At present, the Cokelet method appears to yield the most accurate results for nearly breakingwaves; however, the differences from the numerical theories (Chappelear and Dean) are generally small and the Cokelet approach is not known to have been applied to design.

11.3.1 Formulationand Solution

In Chapter 3 the linear form of the stream function for water waveswas given as

or if the coordinate system is moved with celerity of the wave, C, thereby rendering the system steady, as

Hg sinh k(h+z )cos

‘(X, z ) = c z --20 cosh kh (11.47) The advantage of moving the coordinate system with speed C is that the problem is rendered steady, thus reducing the number of terms in the boundary conditions.

The boundary value problem for progressive water waves is, in stream function form,

![(*>’+(z>’]+gq=eB,aconstant,onz=‘ ( x ) ,

V2y/= 0, throughout the fluid (11.48a)

(11.48b)

2 az the DFSBC

-=---” ”” on z =‘(x), the KFSBC (11.48~)

ax az ax’

Using the stream function, the latter condition is true by definition; that is, the free surface, wherever it is, is a streamline. This condition, therefore, is satisfiedexactly.

###### ’a

-=0 onz=-h, BBC (11.48d) ‘( X, z)= ‘(X +L, z), lateral boundary condition (11.48e)

ax



---PAGE-323---



Sec. 11.3 The StreamFunctionWave Theory 307

Now, from analogy to the second-order wave theory, we might assume that the Nh-orderstream function might look like

and

(I1.50)

Note that for the linear theory, we must have the coefficient

X(1) =-Eis-___1 CT sinh kh

The only condition not satisfied by this assumed form is the dynamic free surface boundary condition. The X ( N )are, therefore, chosen to satisfy this condition. Onthe computer, this condition is satisfied atI discrete points along the wave profile, each point being denoted by i. The DFSBC is thus evaluated at each i point along the profile, giving QB,. According to the DFSBC, all the QB, must be equal to QB, where QB is a constant.

+:I:( (9:+gilt=QB (11.51)

###### QB, = 2

However, to get the QBI,the X(n)’s (n= 1, 2,. .., N) must be known to calculatedy//dz,dV/ldx,and q.The procedure then must be an iterative one; values ofX(n)are used to determine the QB,, the QB, are then used to get new X(n),and so on, until the boundary condition is satisfied.

The measure of the satisfaction of the boundary condition will be defined as El,which is the mean squared error to the boundary condition

(11.52) where

For an exact solution, E , must be zero. different from zero, q(x)must have a zero mean, that is,

As occurred with the second-order analytical solution for which QB is

(2/L)SL”0 q(x)dx = 0



---PAGE-324---



308 Nonlinear Waves Chap. 1 1

Further, for design purposes, it is desirable to be able to prescribe the wave height a priori. These last two conditions can be considered as constraints to the condition that Elbe zero, or at least very small.Tosolve for the X(n)’s,El must be minimized, subject to the constraints. Note that there are two additional unknowns, due to the necessity of also determining the wavelength L and the value of the free surface streamline y(x,u), which is a constant. Using the method of Lagrange multipliers (Hildebrand, 1965),we minimize the objective function 0,:

2A1L S“’O

O f = E l + - V(X)~X+[A~~(O)-V(;)- -H] (11.53)

where 1,and A2are Lagrange multipliers. The objective function is nonlinear and in order to facilitate the solution, it is expanded by a truncated Taylor series:

(11.54) where AX(ny’is a small correction to X(n):

###### X”l(n) =X’(n) +AX’(n) (11.55)

and the superscriptj indicates the number of iterations that have been made. Minimizing the expanded objective function with respect to all theX(n),plus AI and 12yields a series of linear equations for the A F ( n )for fixedj.

Solving the equations for AX(n)in matrix form yields the solution for iteration, j + 1. This process is repeated for several iterations until 0;’is acceptably small. This technique is simply a Newton-Raphson procedure, but applied to a set of nonlinear equations (see, e.g., Gerald, 1978).

The stream function wave theory has been used to generate40 representations of nonlinear waves by Dean (1974) and the results tabulated in dimensionless form. Using these tables, most designs using nonlinear wave theory can be carried out without the use of a computer.

Chaplin (1980) has developed an improved approach to that of Dean (1965)for calculatingthe stream function coefficients, although it is not clear that his method is an improvement over that of Dalrymple (1974), which is presented above. Chaplin formulates the problem in dimensionless form with h, H, and T as the independent parameters and the dimensionless surface displacements as the unknowns. The method, which is more complex, but yields greater accuracy, particularly for nearly-breaking waves, commencesby determining a set of orthonormal functions representing the terms in the series given by Eq. (11.49). These functions then allow a more direct solution of the stream function coefficients which satisfy the dynamic free surface boundary condition [Eq. (11.48b)l. The method has the advantage that, in contrast to that originally developed by Dean, a maximum in wave length (or celerity) is represented at wave heights slightly smaller than



---PAGE-325---



Sec. 11.4 Finite-Amplitude Waves in Shallow Water 309

breaking. Chaplin carried out comparisons of a number of parameters and concluded that for waves up to 75%of the breaking height the errors in the tables of Dean were lessthan 1%exceptin extremelyshallowwater. For waves of 90% of the breaking height the errors were less than 5% in most cases.

Extension of the theory to waves on vertically sheared currents has been done by Dalrymple (1974) and Dalrymple and Cox (1976), and for irregular measured water surfaces by Dean (1965). The latter procedure involves determining the best-fit stream function to a given water surface profile.

###### 11.4 FINITE-AMPLITUDE WAVES IN SHALLOW WATER

In the Stokesperturbation procedure, the perturbation parameter wasku,the wave steepness. In very shallow water the Stokes wave profile [Eq. (11.32)] becomes (using shallow asymptotic expansions for the hyperbolic functions)

~(xt ), =a cos(kx-at)+-3ka2 cos 2(kx -at)

(11.56)

4(kh)3

The second term is a function of wave amplitude and length, as well as the water depth, being proportional to the Ursell number or (u/h)(L2/h’),which will be defined as the ratio alp, where a 5 a/h, /3 = h2/L2.In fact, the Stokian wave profile for higher orders in shallow water is an expansion using the ratio alp as the perturbation parameter. This implies that alp must be much less than unity or a <<p. In shallow water, this requires quite a short wavelength or a small-amplitude wave, as discussed previously. It would be desirable for design purposes to have a perturbation expansion in shallow water which would at least allowa andp to be of the same magnitude.This can be achieved with a different perturbation procedure than that used previously.

First, the shallow water wave will be assumed tobe propagating without change in form; thus, by moving with the wave celerity C, the motion becomes stationary,and a stream function approach becomes convenient, as in the preceding section.

(Ey+($y +2g(h+q)=Q onz=h+rj (11.57a)

The free surface boundary conditions are

###### and

y =Ch o n z = h + q (11.57b)

In this context, the coordinate system is taken to be on the bottom and Q is the Bernoulli constant. At the bottom,

y = O onz=O (11.57~)



---PAGE-326---



310 NonlinearWaves Chap. 1 1

This condition ensuresthat there is no flow through the horizontal bottom, as w = - = oay/ onz=O

ax

For a wave propagating on a quiescent fluid, Q =Cz+2gh,whichis determined from the dynamic free surface boundary by moving far upstream of the wave, where the wave motion is negligible.

It is again convenient to express the equation in nondimensional form prior to the perturbation procedure. In contrast to the Stokes expansion, however, the x, z coordinates will be nondimensionalized differently,recognizing the fact that there will be larger gradients in the vertical direction than the horizontal.

###### n=-tl

a (11.58)

The governing Laplace equation, in terms of the nondimensional variables, is written as

p-+-=oazYax2 a2YazZ (11.59a) where, again,p = (h/L)'.

The two free surface conditions are

Y=-- C

o n Z = 1 +all (11.59b)

###### diG

where

a

a = - (11.59~)

h

and



---PAGE-327---



Sec. 1 1.4 Finite-AmplitudeWaves in Shallow Water 311

Bydifferentiating2with respect toX,we can eliminate the constants to obtain the form we will use:

###### p-aYa2Yaxax'-+ap-aYaxaxazax-a2Y -an+--aYazaxaza2Y +a---+-aYa2ulanazaz2ax axan

(11.60) = O o n Z = l + d

Usinga Frobenius power series solution technique, we will assumea solution in terms of a series in Z (see, e.g., Wylie, 1960):

m

(11.61)

To satisfy the bottom boundary condition,fo must be zero. Substituting the assumed solution into the dimensionless Laplace equation and grouping terms yields

(11.62)

For this equation to be satisfied for any Z, the coefficientsof the z" terms must be zero. Therefore,

h=O

f P d2fr

3 - 6 dX2 & = O j-----=--P d'f3 P ' d"fi

- (11.63)
- (11.64)


5 -

20dX2 120dX4

f6=0

and soon. Therefore, the series may be written

###### Y = Z f , -P- z3dY-l-+--- P2Z5dYI+ . . .

6 dX2 120 dX4 or

'Since Z at the free surface is a function ofX,the total derivativeis used.



---PAGE-328---



312 Nonlinear Waves Chap. 11

Clearly, we now have a series in terms ofb, the relative depth parameter. The objective is to determine the functional form offi in order that Y satisfiesthe two free surface boundary conditions. Substituting the expansion for Y into the kinematic and dynamic free surface boundary conditions yields

(1 +arIfi--P(l1 d2fi C

+arI)’-+O(p)=--

(11.65)

###### 6 dX2 4G

P-0 +an)2--++fi---(1d ! d2fi dfi P +arI)2fiL+-++o(p‘)=Odf3 drI (11.66)

2 d XdX2 dX 2 dX3 dX

First, examining the zeroth-order solution for Y in P, that is, the solution depending on p”, it is clear that the horizontal velocity, U = - dY/dZ, is uniform over depth, asfi is not a function of Z. In this case, the kinematic boundary condition reduces to

(l+dI)f1=- C

###### 4G

or

C (11.67) Substituting into Eq. (11.66)will yield, to orderp”, an expression for C:

fi =-(1+an)-’

###### 4G

-C’a(drI/dX) +-=Od n

(11.68)

gu(1 dX or

(1 1.69)

For this last equation to be true everywhere, the term within the parentheses must be zero. Therefore,

###### c2=gh(1 +any

(11.7Oa)

or3

CN@(1+y) toorder(a2,$) (11.70b)

To the first approximation. in a,we have the usual shallow water wave

celerity,whichdependssolelyonthemeanwaterdepth,C=m.Thewave

’Recall the binominal seriesapproximation:

( l + l $ = I + n € + - n(n - 1)

€2

2!



---PAGE-329---



Sec. 1 1.4 Finite-AmplitudeWaves in Shallow Water 313

form ll can be arbitrarily chosen for this case. The next approximation, to @a2,p"),provides a correction term,$an,whichindicatesthat the largerthe local water surface displacement, the faster the local wave speed.This result was first due toAiry(1845).Thedifficulty is that we originallypostulated that we were moving the coordinate system with wave speed C,which was assumed to be constant for the wave. Clearly, this is not the case,so we expect the wave to deform as it propagates, with the higher portions of the wave profile moving fasterthan the lower portions, sothat, in fact,the wave profile continually steepens in front until our assumption of a being small is violated. Physically, the wave eventually breaks in the form of a bore. Theoretically, we must find a better solution, one that yields a constant celerity.

To a higher order, O(a2,an,the solution is assumed to be

fi=-(lc +an)-'+/3A

(11.71)

###### G

whereA is an unknown function of x. Substituting into the kinematic free surface boundary condition and retaining terms 0 0 yields the following equation forA in terms of lland its derivatives:

A=--a- c [W_ _ 2a_ (">'I-~ (1 1.72)

6 &jdX2 l + a n dX

Substituting5 andA into the dynamicfreesurface boundary condition yields a very complicated expression, which, however, to O(a2,an reduces to this nonlinear equation:

gdX[ l -$(1-3all)

- (11.73)
- (11.74)


or

This equation is the steady-state form of the Korteweg-DeVries (1895) equation. The solution to the linearized form of this eq~ation,~which is of O(a,a/?),is

n=cos2KX

with the followingequation for the wave celerity:

(1 1.76)

That is, neglectingthe second term.



---PAGE-330---



314 NonlinearWaves Chap. 1 1

The effect of including the parameter p is to reduce the celerity, just the oppositeof the parameter a.In fact,by introducingp, the relative depth (i.e., making it different from zero, the infinite wave length case), we have developed a wave movingat constant C,a wave that does not form a bore as did the solution whenp =0.This wave is equivalent to the small-amplitude wave theory we have developedin the first eight chapters. In fact, it is easy to show that the celerity given above is equal to the first two terms in the shallow water expansionof Eq. (3.35).

11.4.1 The Solitary Wave

We will now seek a solution containing both a and p such that their influence results in nonlinear waves of permanent form. The equation above can be solved without the necessity of linearization. The procedure is to integrateonce with respect to X.

- (11.77)

Multiply by dn/dX and integrateagain to yield

- (11.78)


whereD and E are constants of integration. If we solve this equation for the case of a single wave which has no influenceat infinity,then ll=dn/dX=0at X = co. Clearly, D and E must be zero, from Eqs. (11.77) and (11.78). The remaining equation is, therefore,

For the wave form to be symmetric about the X axis,dll/dX must go to zero at ll= 1,the wave crest.Thus

- (11.80) or
- (11.81)


###### 1- a

and the equation becomes

(11.82)



---PAGE-331---



Sec. 11.4 Finite-Amplitude Waves in Shallow Water 315

The solution is

ll=s e c h 2 eX or in dimensional form

- (11.83)
- (11.84)


q=a s e c h 2 G x

This is called the solitary wave of Boussinesq (1872). Munk (1949) has advocated the use of superimposed solitary waves to describe waves in the surf zone. The solitary wave form is shown in Figure 11.2.The entire wave profile is positive for this wave; there is no q less than zero. The a therefore represents the height of the wave and h the depth at infinity.The volume of water contained in a solitary wave, V,over a distance -I <x <I, that is, the amount of water above the mean water level, is found by integrating the profile.

- (11.85)
- (11.86)


For I equal to infinity, the hyperbolic tangent is unity and

Vm=4hE-

Clearly, for engineering use, an infinitely long wave has no value; however, the effectivelengthof the solitary wave is much less. For example,95%of this volume is contained within the distance

I=- 2.12h43 (11.87)

-

0.6

0.4

0.2

###### 3 2.0

0 " ' t ' t " l ' ' " " ~ ' ' ~ ~

###### "I 0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6 -41.8 I 2.0 2.2 2.4

95%

###### Figure 11.2 Dimensionlessfree surface profile ofa solitary wave.



---PAGE-332---



316 Nonlinear Waves Chap. 1 1

For example, if u/h =0.5,then 95%of the volume is within a space of about six water depths.

The water particle velocities under the solitary wave are found by U = -dY/dZ and W =dY/dX from Eqs. (11.64),(11.71), and (11.72).

- (11.88)
- (11.89)


Substituting forfi

from Eqs. (11.71) and (11.72) for the horizontal velocity

yields

U =-[C

+cm-(cUrI)2+aj? z2 -d2n toO(a2,aj?)

JG -I

###### (6 2 ) dX2]

or

" j

where ll is given as a function of position by Eq. (11.83).The first term in brackets, that is, the minus 1, is to account for the speed of translation of the coordinate system. For a fixed observer, this term would be neglected. The remainder of the expression for U consists of terms proportional to n; therefore, away from the crest the velocity becomes small. Under the crest of a solitarywave,n = 1 and the expressionfor Uisgreatlysimplified:

(11.91)

or in dimensional form,

(11.92)

For the vertical velocity

1

C Olp d311

W =-Fa q2an- 1) ---(Z -Z3) to 0((r2,afl (11.93)

4G dx 6 dX3



---PAGE-333---



Sec. 11.4 Finite-AmplitudeWaves in Shallow Water 317

###### or

=-2lletanh%X

wherellis given by Eq. (11.83)and

- (11.95)

In dimensional form

- (11.96)


dX

For applications of the solitary wave theory, the reader is referred to the extensivework of Munk (1949).

11.4.2 CnoidalWave Theory

In 1895,Korteweg and Devries (1895)developed a shallow water wave theory which allowed periodic waves to exist. These waves have the unique feature of reducing to the solitary wave theory at one limit and to a profile expressed in terms of cosines at the other limit, thus spanning the range between the linear and solitary theories. The wave profile is developed in terms of a Jacobian elliptic integral, cn(u), and they called the theory “cnoidal” to be consonant with the sinusoidal, orAiry theory.

The development of the periodic theory followsthe previous perturbation procedure for solitary waves with the exception that in Eq. (11.78)we cannot force the unknown constantsD and E to be zero. If, however, for our cnoidal waves we force ll = 0 at Z = 1, defined as the wave trough, then dll/dX should be zero there also, as the wave form is periodic. Therefore,E must be zero and the integrated equation becomes

###### l d l l ’ a llz

###### 6(dx) +%r13 -F- +on=0 (11.97)

2

where

###### (11.98)



---PAGE-334---



318 Nonlinear Waves Chap. 1 1

At the wavecrest,n =1 and againdn/dX=0;thusD can bereadilyfound:

- (11.99)
- (11.100)


The equation is now

or

(1 1.101) where

S = l - F -P (11.102)

###### a

The substitutionII=cos2xwillbeusedto transform this equation into a more tractable form, involvingx. From the imposed conditions on l7at the crest and trough, the values ofxare seen to be 0and n/2 for the crest and first trough, respectively. Substituting, we obtain

###### ax =dX

1 +S -sin2X

###### or

1 1

###### X =

F(k.9x) (11.103)

4 P where

###### (11.104)

and whereF(k,x) is the notation for the elliptic integralof the first kind with modulus k andamplitude X.The amplitudeofxis then given, from the theory of elliptic functions, as



---PAGE-335---



Sec. 1 1.4 Finite-Amplitude Waves in Shallow Water

319

( 11.105)

###### or

II=cn2(X @)mod(k)

(11.106)

or in dimensional form,

v=acn2(x V E ) =acn2[F(k,x)] ( 11.107)

4h3k2 To be consistent, the parameter a has been used in the definition for 7; however, in this connection, a is the wave height, as in the solitary wave theory.

The Jacobian elliptic function cn is a periodic function with a period of 4K, where K is the complete elliptic integral of the first kind, K = F(k, lc/2), as shown in Figure 11.3.The function cn’u is periodic with period 2K.The wave length of the cnoidal wave is found by setting X equal to unity in the argument of cn u.Therefore,

G l = 2 K

- (11.108)
- (11.109)


or

The parameter k is uniquely related to wave amplitude a, the length L , and the water depth h. A graph of k versus the Ursell parameter U,, K(k),and E(k),the complete elliptic integral of the second kind, is shown in Figure 11.4. For shallow water (Chapter3)h/L < 1/20,and therefore the Ursell parameter has a minimum value of U,= 400(a/h).For nearly-breaking waves, a (the wave height) is about 0.8h.This gives an Ursell value of 320and a k value of

1

0

Figure11.3 TheJacobianelliptic -, -

function, cn u.



---PAGE-336---



###### 320 Nonlinear Waves Chap. 11

0 100

Figure 11.4 Complete elliptic integrals of the first and second kinds and the Ursell parameter as a functionof the modulusk.

0.999999 or larger for shallow water. Various water surface profiles are shown in Figure 11.5 for various values of k.

The parameter h refers to the water depth at the wave trough. To

determinethemeanwaterdepth,thewaveprofileisaveragedanddenotedn.

-n=l'cn2(2KX)dX

- (11.110)
- (11.111)


or

whereE is the complete elliptic integral of the second kind.The total depth is then (h+6).

The cnoidal wave celerity can be found using the definition for F, S, and k following Eqs. (11.98), (11.102), and (11.104). Solving for C, we have

(11.112)

To find the related wave period, we use the definition of L (C= LIT),

(11.113) from Eqs. (11.109) and (11.112).

C



---PAGE-337---



###### 321



---PAGE-338---



322 Nonlinear Waves Chap. 11

be pointedout.Ask-,1,thewavelengthbecomesinfinite,asK(1)-ogand

Several interesting asymptotic features of the cnoidal wave should

cn2(x)-sech2(x),thesolitarywave.5Ontheotherhand,ask-0,cn(x)-,

cos(x),andK-n/2,andthewaveformchanges:

###### q=acn2(2KX)-,acos2(xv-) =acos2($) (11.114)

which can be written in terms of elevation from the bottom as

(1 1.115)

where h + 4 2 denotes the elevation of the mean water level above the bottom. This also follows from Eq. (ll.lll), as the ratio of E/K goes to (1-k2/2)forK-0.Thuscnoidalwavetheoryspanstherangefromsinusoidal or Airy theory in deep water to solitary wave theory in shallow water.

The velocities under a cnoidal wave can be found as for the solitary wave, Eqs. (11.90)and (11.96).

(1 1.1 16)

###### +2(2k-1)(x>’- 3*’(;)lh’]}

where

The leading terms for u and w are, as might be expected, the same as those developedfor the long waves in Chapter 5 [seeEqs. (5.2) and (5.3)].

###### 11.5 THE VALIDITY OF NONLINEAR WAVE THEORIES

It is important toknow which of the various water wave theories to applyto a particular problem, where the wave characteristics and water depth are specified. For example, is the linear wave theory suitable or must cnoidal theorybe used?In order to addressthese problems, the validityof the various

jIwagaki (1968), using this asymptotic behavior, has developed the hyperbolicwave theory (valid forK > 3), which means that k > 0.98,which is a blend of solitary andcnoidal theory having the mathematical advantage of the solitary theory and some of the properties ofthe cnoidal theory.



---PAGE-339---



Sec. 11.5 The Validity of Nonlinear Wave Theories 322

theories must be known. This "validity" is composed of two parts: thc mathematical validity and the physical validity. The first is the ability of an) given wave theory to satisfy the mathematically posed boundary valut problem. For example, all the theories in the book satisfy the bottom boundary condition exactly, but the cnoidal and solitary wave theories onlj approximately satisfy the Laplace equation within the fluid. All of thc theories only satisfy the dynamic free surfaceboundary approximately,whilc the kinematic free surface boundary condition is satisfied (to the numerica accuracyof the computer) by the stream function theory. On the other hand the physical validity refers to how well the prediction of the various theorie: agrees with actual measurements. This part of the validity has been difficull to obtain due to the problem of wave tank design and measurement require. ments. The interested reader is referred to Dean (1974).

The analytical validity of many wave theories was examined by Dear (1970) (see also Dean, 1974). Figure 11.6shows the results of the comparisor of the theories, denoting the regions for which each theory provides the besi fit to the dynamic free surfaceboundary condition. As would be expected,the

10"

1I 5

10-1

###### .y1

h

N

10-2

c

v

(-I

N

h

###### s

10-2

10-2 10-1 10" 10'

hiT2 (ftis2)

###### Figure 11.6 Periodic wave theories providing best fit to dynamic free surface boundary condition (analytical theories only).



---PAGE-340---



324 Nonlinear Waves Chap. 11

###### cnoidal wave theory does well in shallow water, while in deep water, the StokesV wave theory proved to be more applicable. Somewhat surprisingly the linear wave theory did well for the intermediate water depths. However, when high-order stream function wave theory is used, it provides the best fit ofall the theories, even in shallow water (although quite high orders, such as twentieth order, are necessary).

###### REFERENCES

AIRY,G. B., “Tides andWaves,” Encyclopaedia Metropolitana, 1845. BORGMAN,L. E., and J. E. CHAPPELEAR,“The Use of the Stokes-Struik Approxima-

tion for Waves of Finite Height”, Proc. 6th Con$ Coastal Eng., ASCE, Council on Wave Research, Berkeley, Calif., 1958.

BOUSSINESQ,J. “Theorie des ondes et des remous qui se propagent le long d‘un canal rectangulaire horizontal, en communiquant au liquide contenu dans ce canal des vitesses sensiblement pareilles de la surface au fond,” J. Math. PuresAppl.,Vol. 17,

pp. 55-108,1872.

CHAPLIN,J. R., “Developmentsof Stream FunctionWave Theory, “Proc.17th Con$ Coastal Eng., ASCE,Vol. 3, 1980, pp. 179-205. CHAPPELEAR,J. E., “Direct Numerical Calculation of Nonlinear Ocean Waves,” J. Geophys.Res.,Vol. 66, No. 2, pp. 501-508,1961.. COKELET,E. D., “Steep GravityWaves in Water ofArbitrary Uniform Depth,” Philos.

Trans.Roy. SOC.Lond.A,Vol. 286, pp. 183-230,1977.

DALRYMPLE,R. A., “A Finite Amplitude Wave on a Linear Shear Current,” J. Geophys.Rex,Vol. 79, No. 30, pp. 4498-4504, 1974.

DALRYMPLE,R. A., and J. C. Cox, “Symmetric Finite Amplitude Rotational Water

Waves,”J. Phys. Ocean.,Vol. 6, No. 6,1976. DEAN,R. G., “Stream Function Representation of Nonlinear Ocean Waves,” J. Geophys.Res.,Vol. 70, No. 18, pp. 4561-4572,1965. DEAN,R. G., “Relative ValidityofwaterWaveTheories,” J. Waterways Harbors Div.,

ASCE,Vol. 96, No. WW1, pp. 105-119, Feb. 1970.

DEAN,R. G.,“Evaluation and Development ofwaterWave Theories for Engineering Application,” Vols. 1and 2, Spec. Rep. 1, U.S. Army, Coastal Engineering Research Center, Fort Belvoir,Va., 1974.

EBBESMEYER,C. C., “Fifth Order Stokes Wave Profiles,” J. Waterways, Harbors Coastal Eng. Div.,ASCE,Vol. 100, No. WW3, pp. 264-265,1974.

GERALD,C.E,Applied Numerical Analysis,2nd ed., Addison-Wesley,Reading, Mass.,

1978.

HILDEBRAND,E B., Methods of Applied Mathematics, 2nd ed., Prentice-Hall, EngleIWAGAKI,Y., “Hyperbolic Waves and Their Shoaling, “Proc.10th Con$ Coastal Eng.,

wood Cliffs,N.J., 1965. ASCE, London, 1968.



---PAGE-341---



Chap. 1 1 Problems 325

KORTEWEG,D. J., and G. DE VRIES, “On the Change of Form of Long Waves Advancing in a Rectangular Channel, and on a New Type of Long Stationary Waves,”Philos. Mag.,5th Ser., Vol. 39, pp. 422-443,1895.

MUNK,W. H., “The Solitary Wave Theory and Its Applications to Surf Problems,”

Ann. N.I:Acad. Sci.,Vol. 51, pp. 376-424, 1949.

SCHWARTZ,L. W., “Computer Extension andAnalytic Continuation of Stokes’ Expan-

sion for Gravity Waves,”J.Fluid Mech.,Vol. 62,1974.

SKJELBREIA,L., and J. A. HENDERSON,“Fifth Order Gravity Wave Theory,”Proc. 7th

Con6 Coastal Eng.,ASCE, 1961, pp. 184-196. STOKES,G. G., “On the Theory of Oscillatory Waves,” Trans. Camb. Philos. SOC., URSELL,E, “The Long-Wave Paradox in theTheory of Gravity Waves,”Proc. Camb. WIEGEL,R. L., “A Presentation of Cnoidal Wave Theory for Practical Application,”J. WIEGEL,R. L., Oceanographical Engineering, Prentice-Hall, Englewood Cliffs, N.J., WYLIE,C. R., Jr., Advanced Engineering Mathematics, 2nd ed., McGraw-Hill, New

Vol. 8, pp. 441-455,1847. Philos. Soc.,Vol. 49,1953, pp. 685-694. Fluid Mech. Vol. 7, Pt. 2 (1960). 1964. York, 1960.

###### PROBLEMS

Verify that the total horizontal acceleration given in Eq. (11.45)for the Stokes wave theory is correct to second order. Determine the total vertical acceleration.

11.1

Develop the horizontal and vertical velocities, correct to O(a,cup) for r] =a coskx,Eq. (11.75). Compare with linear (Airy)theory.

11.2

For shallow water waves, develop the equation correct to O(a2,afl for the pressure under the waves. Determine the region of validity for the second-order Stokes theory. Which value of the Ursell parameter is more restrictive? Calculate the pressure under Stokeswaves, correct to second order. What is the a’, /3” order solution of Eq. (11.74)?What is the physical significance of this flow? Verify Eqs. (11.90)and (11.96). Assumingequipartitioning of the energyand finding the potential energy, show that the total energy in a solitary wave per unit crest width is

11.3

11.4

11.5 11.6

11.7 11.8



---PAGE-342---



###### 12

A Series of Experiments for a Laboratory Course Component in Water Waves

###### 12.1 INTRODUCTION

There are several important reasons to include a laboratory component as a portion of a course in water waves. First, since the field of water waves is evolving rapidly with new significant developments, the experience in laboratory techniques will develop a student’s capability to test new analytic results and will provide a better basis for evaluating the validity of experimental results reported in the literature. Second, and probably of greater significance, is the confidence (hopefully) and perspective gained by the student in conducting measurements and assessingthe associated theoretical results.

###### 12.2 REQUIRED EQUIPMENT

Most of the equipmentrequired for the experimentsto be described is usually available with wave tank facilities.

12.2.1 Wave Tank

The sizeof the wave tank is not critical, but should be of a sufficientsize that capillary waves are not significantand that a plane beach of small slope (say 1:15) can be placed in the tank and still allow room for measurements. It

326



---PAGE-343---



Sec. 12.2 RequiredEquipment 327

assists greatly if a portion of the tank is glass- or Lucite-walled. Also, a movable carriage mounted on level rails is useful for transporting the wave gage and possiblyother equipment. The tank at the University of Delaware is approximately24 m long, 1 m deep, and 0.5 m wide, although a smaller tank would be suitable. The experiments to be described will be based on a capability to generate monochromatic waves; however, the range of experiments would be greatly expanded with the availability of a spectral-generating capability.

12.2.2 Wave Gages and Recording Equipment

Laboratory wave gages and recording oscillographs are quite standard and will not be described in detail. Either capacitanceor resistancegages are suitable.It is helpful to mount the wavegages on a point gage supporttoallow static calibrations to be carried out readily (see Figure 12.1). Generally, two wave gages are required with output on the same oscillograph and as noted previously, it is desirable if one of the gages is movable on a level surface.

12.2.3 Velocity Sensor

Asmall laboratory version of a biaxial electronic current meter is useful in conducting measurements of the water particle velocity field. If an equivalent current meter is not available, it is possible to measure water particle excursionsvisually.

Mount for point gage

To signal conditioning A

and oscillograph

###### Figure 12.1 Wave gage mounted on graduated point gage support.



---PAGE-344---



328 Experimentsfor LaboratoryCourseComponent in Water Waves Chap. 12

Manifold

-iEl / ,Total headpressure

Streamlined strut

Elevation view

Plan view section AA

Figure 12.2 Two possible arrangementsformeasuringpressure field in waves:(a) permanenttaps through Lucite wall ofwave tank; (b) movable pressure port with pressure tubing housed in movable streamlined strut.

12.2.4 PressureSensor

A reasonably sensitive pressure sensor is desirable. A strain gage total head sensor with a range of 0.005 to 1 psi is very satisfactory.If the observational section of the wave tank is made of Lucite it may be possible to drill ports and connect these to a manifold as shown in Figure 12.2a. If the walls are glass or it is not desired to tap through the walls, a somewhat streamlined strut can be placed flush with the tank wall (see Figure 12.2b).With either systemit is essentialto be able to bleed any air from lines connecting the port to the sensor.

12.2.5 Wave Forces

A “portal-type’’forcegageisinexpensiveto construct and useful sinceit responds to forces and is insensitive to moments. Figure 12.3 portrays the main features ofa portal gage.Theupper and lower plates arerigid relativeto the side plates. The sensing is by four strain gages connected to a full bridge



---PAGE-345---



###### Sec. 12.2 Required Equipment 329

attachment to

Strain gage

Strain gage

E%bMomentsensor

Can be made of various thicknesses for different

Portal gage

sensitivities

###### @tTosTi

conditioning and recorder

Strain bridge for forces

Support rod

Object on which forcLs and moments are to be measured

Fiked /

resistors Strain bridge for moments

Figure 12.3 Force and momentsensors.

circuit as shown. For purposes of measuringa wide range of forces with good sensitivity,different sets of web plates can be constructed.The strain E at the extremes (top and bottom) of the web plates can be shown to be

3 Fl 2 Ewt2

€=-- (12.1)

in which F is the applied force, 1, w, and t are the plate length, width, and thickness,respectively,andE is the modulus ofelasticityofthe material. The natural frequencyu,,of the system is



---PAGE-346---



330 ExperimentsforLaboratory Course Componentin Water Waves Chap. 12

(12.2)

###### MT

in which Mr is the total mass of the system, including any added hydrodynamic mass. The natural frequency should be significantlyhigher than the highest excitation frequency.

If, in addition to the total force on an object, it is desired to determine the location of the effective force,a set ofstrain gages can be added to the rod to yield moments, as shown in Figure 12.3.

Note that it is extremely important to have firm connections or the natural frequency will be too low.

###### 12.3 EXPERIMENTS

Following is a list of nine experiments that can be carried out. It should be possible to complete the experiment and a substantial portion of the report documentation during the class time allotted to each experiment.

Experiment No. Description Wave length, profile, and group velocity as a function of wave period, Wave profiles and particle trajectories as functions of wave height, water Pressure variations as a function of wave height, water depth, and wave

- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9


water depth, and wave height depth, and wave period; progressive and standing waves period; progressive and standing waves

Wave height transformation in shoaling water; wave breaking Wave reflection from beach; comparison with Miche’s theory Wave reflection from a partial vertical barrier; comparison with approxi-

mate theory Wave forceson cylinders and spheres Plane wavemaker Approximate wavemaker theory for a perfectly reflecting “beach”

The report describing the laboratory experiment should be fairly concise.A reasonable format for the reports is as follows:

- 1. Purpose-stating the objectives of the experiment.
- 2. Background and/or theory-describing the problem and presenting theoretical relationships to be tested.
- 3. Equipment description-this section can be quite brief, especially if the equipment has been used previously and is described in an earlier report.
- 4. Procedure-describing the experimental, data reduction, and/or analysis procedures.




---PAGE-347---



Sec. 12.3 Experiments 331

5. Results (and conclusions)-presentation of results and possible reasons for any significant differencesbetween theory and experiment. Can you suggest a procedure (experimental or analytical) that would verify or disprove your suggested reasons for any differences noted between theory and experimental results?

The report, excludinggraphs and data sheets, should not exceed several pages. Items 1 through 4 and any graphs for item 5 can be a laboratory group effort; the conclusions and interpretation of results in item 5 should be an individual effort. The “group effort” portions of the report can be copies; however, each group member should turn in a complete report.

Each of the experiments above is described briefly in the following sections.

12.3.1 Experiment 1:Wave Length, Profile, and Group Velocity as a Functionof Wave Period,Water Depth, and Wave Height

The purpose of this experiment is to compare measured wave profiles, wave lengths, and group velocities with the corresponding values as predicted by small-amplitude wave theory.

Small-amplitude wave theory.

WaveProfile q. The wave profile q generated by a simple harmonic wavemaker is

q=-cos(I-t)H 2nt 2nx 2

###### (12.3)

where H, T,L, x,and t are the wave height, wave period, wave length, and distance and time coordinates, respectively.

###### WaveLength L.

The small-amplitude relationship for wave length L is

###### h

L = Lotanh 2n L

###### (12.4)

where h is the water depth and Lois the “deep water” wave length expressed by

Lo =gT2~

(12.5)

2n

The quantity L/Lo is plotted againsth/Loin Figure 3.9.

The group velocity Cc is the speed at which the wave energy propagates and is also the speed of propagation of the leading

###### Group Velocity Cc.



---PAGE-348---



332 Experimentsfor Laboratory CourseComponent inWaterWaves Chap. 12

edge of a train of waves. The group velocity can be expressed as

CG=92 tanh(22) [1+

- (12.6)
- (12.7) The ratio CG/COis also plotted againsth/Lo(Figure3.9).


sinh 4n(h/L)

where Cois the deep water celerity, that is C0=-gT 2n

Measurements. The major piece of equipment for this experiment is the wave tank. Two capacitance wave gages connected to a two-channel oscillographare used to senseand record the moving water surface.

For each of the runs, the water depth, wave height, and wave period should be observed.

WaveLength. The wave length can be establishedby first spacingthe two wave gages approximately one wave length apart along the channel.A final spacingcan be establishedby adjusting the position of one gage until the oscillograph tracesare observed to be in phase.

Group Velocity.

The group velocity is determined by spacing the two wavegages5to 10 m apart and then starting the wave generator.The “leading edge” or front of the wave train will travel at the group velocity.The group velocity can be calculated from the known separation distance between the two gages and the observed difference in “leading edge” arrival times at the two gages.

It isdesirableto obtain a reasonablyhigh speed oscillograph record of one or two wave periods.

WaveProfile.

12.3.2 Experiment 2: Wave Profilesand Particle Trajectories as Functionsof Wave Height, Water Depth, and Wave Period; Progressive and StandingWaves

The purpose of this experiment is to compare measured and theoretical profiles and water particle trajectories of progressive and standing waves.

Background. The maximum water particle displacements I[I and

I<Iin thex andz directions,respectively, can be expressedas functionsof the incident and reflected wave heights, the mean position of the particle in the waves (both horizontally and vertically), and the wave period and water depth (see Figure 12.4).



---PAGE-349---



###### Sec. 12.3 Experiments 333

###### +

z

Figure 12.4 Definition sketch for experiment 2: (a) progressive wave; (b) pure standing wave.

###### H

q =-cos(kx- Ct)

- (12.8)
- (12.9)


2

H coshk(h+z) 2 sinh kh H sinhk(h+z ) 2 sinh kh

l C l = -

ltl =-

H

q =-cos kx cosa2

2 H coshk(h+z)sinkx 2 sinh kh

lCl =-

H sinhk(h+z)coskx l<l=-2 sinh kh

tan kx



---PAGE-350---



334 Experimentsfor LaboratoryCourseComponent inWater Waves Chap. 12

Measurements

Progressive Waves. With the barrier removed, generate a progressive wave system.

- 1. Measure the wave characteristics
- 2. Using approximately neutrally buoyant particles, measure ICI and I I at two depths within the wave. Standing Waves. Establish a standing wave system using the vertical


barrier as a reflector.

- 1. Measure the characteristics of the standing wave system.
- 2. Using approximately neutrally buoyant particles measure the maximum water particle displacement components ICl and I <I and inclination of streamlines at any depth at the node and antinode positions and also at a position intermediate to these positions.


Reference: See pp. 80-89.

12.3.3 Experiment 3: Pressure Variations as a Function of Wave Height, Water Depth, and Wave Period; Progressive and Standing Waves

The purpose of this experiment is to compare measured and theoretical pressure variations within progressive and standing waves.

Background. The pressure deviations from hydrostatic pressure as derived for small amplitude waves is

cosh k(h +z) p = p g r l cosh kh

(12.10)

in which q(x,t )can be the water surface displacement for either progressive, standing, or partially standing waves.

Measurements. Measure the pressure fluctuations near the bottom and at three additional elevations along a tank wall, for a progressive and a standing wave system. Also measure simultaneously the water surface displacement at the longitudinal position (x) of the pressure sensor. Both the amplitudes and phases of these measured pressure fluctuations are to be compared with theory. For the standing wave system, conduct the measure-



---PAGE-351---



Sec. 12.3 Experiments 335

ments at two different positions along the standingwave envelope.Waves of two different periods should be used.

Equipment. The equipment consists of a wave gage, a total head pressure sensor, and a recording oscillograph. If the wave tank is Lucitewalled, it may be worthwhile to drill and tap several permanent pressure taps to be used in conjunction with a manifold. If the tank is glass-walled, a streamlined pressure strut support can be placed along the side of the tank at the desired location (see Figure 12.2).

12.3.4 Experiment 4: Wave Height Transformation in Shoaling Water; Wave Breaking

The purpose of this experiment isto investigate the characteristicsofprogressive and standing breaking water waves and to compare these results with the available theory.

Theory for breakingwaves

Progressive Water Waves. The breaking characteristics of progressive water waves have been studied theoretically in deep and shallow water. In shallow water, for beaches of mild slope, the relationship is

###### H

(12.11)

-= 0.78

###### h

and it is remarked that slopes greater than about 1:40 increase this ratio substantially. For deep water, the deep water steepness (Hb/L,) at breaking

###### (2)max=0.142 (12.12)

whereLo= 1.2(gT2/27r)for breaking waves, including nonlinear effects.These asymptotes and some data are presented in Figure 12.5. Additionally, for deep and shallow water, it is predicted that at the inception of breaking, the “interior” angle of the wave is 120”as shown in Figure 12.6.

For relatively steep slopes in shallow water, there is considerable scatter of the data, as shown in Figure 12.7.

Standing Waves. For standing waves the limiting theoretical steep-

ness is

( =0.218 (12.13)



---PAGE-352---



###### 336

Experiments for LaboratoryCourse Component in Water Waves Chap. 12

- 0.01 2 4 6 80.1 2 4 6 8 1 2 4 6 810
- 1 8 6 4
- 2


###### N.

h

###### c

###### N.

v

###### 1 8 6

h

a?

4

9 BEB tank

###### 2

0.01

0.01 2 4 6 80.1 2 4 6 8 1 2 4 6 810

h/T2(ft/s2)

Figure 12.5 Breaking index curve. (From Reid and Bretschneider,1953.)

and the maximum qcand minimum ql water surface displacementat breaking are

qc= 0.6478 qr = 0.3538

(12.14)

and the “interior” angle of the wave is 90”. developed, although the experimental results indicate the followingratio:

For shallow water, no theory for the limiting standing wave has been

(f)b =1.37 (12.15)

###### I

Figure 12.6 Crest angle at maximum steepness.

a = 120°



---PAGE-353---



###### Sec. 12.3 Experiments 337

Hb/T2 (m/s2)

0 0.02 0.04 0.06 0.08 0.10 0.12 0.14 0.16 0.18 0.20 0.22 0.24 0.26 0.28 0.30

I I I 1 I I I I I I I I I I I 1

###### 1.8

I I I I I I I I I 1

Legend

Assumed maximum breaker height Hbldb = 1.56

Symbol Slope Investigators

1.6

V 1.5 Calvin o 1:lO Calvin o 1 : l O Iverson

0 1.15 JenandLin

###### 1.4

1:20 Calvin

1.20 lversen I :20 Weggel and Maxwell

| |
|---|


| |
|---|


###### 1.2

0 1:30 lversen A 1:50 lversen

Reid and Bretschneider

+ ?

y 1.0

I1

4

9

0.8

0.6

Limitingsteepness=0.875+ -'I

0.4

- 0.2


(Michell theory) --Y

###### ++ I

I I I I I I I 1 I I

0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 H,/T2 (ft/s2)

Figure 12.7 Experimental observationsofdb/Hbversusbreaker steepnessHblT2. (FromWeggel, 1972.)

Measurements

Progressive Waves. Due to the difficulty of measuring kinematics, our experimental study will concentrate on the ratio of wave height to water depth in shallow water. For three wave periods and one water depth (in the uniform depth section), measure the wave height and water depth at which breaking occurs.Also attempt to observe the location of incipient instability. Comment on any extraneous effects in the wave tank, such as reflections from the beach and the effect that these may have on this breaking ratio.You should observe the breaking process carefully to provide a description in your report.



---PAGE-354---



338 Experiments for LaboratoryCourse Component in Water Waves Chap. 12

Standing Waves. For standing waves, using a barrier to provide wave reflection, the experimental efforts will concentrate on measuring:

1. Breaking wave height as a function of water depth and wave 2. The downward acceleration at the antinode. At breaking this

length. value should be equal to the gravitational acceleration. Again careful observations of the breaking process should be made of

standing waves in order to provide a perceptive description in the report.

12.3.5 Experiment5: Wave Reflection from

Beach; Comparisonwith Miche’s Theory

The purpose of this experiment is to compare measured and “theoretical” beach reflection coefficients and to investigate the “wave height envelope” for standing wave systems.

Background;

Standing WaveSystems. The wave system incident on and reflected from the beach can be represented schematically as shown in Figure 12.8, where, accordingto small-amplitude wave theory, the incident and reflected wave systems are

Hi

###### qi =- cos(kx- at) qr=-cos(kx+at +s)

2 (12.16)

Hr

2

t Reflected wave, q,

+ Incident wave, q, Wave helght envelope

###### Figure 12.8 Experimental arrangement for experiment 5.



---PAGE-355---



Sec. 12.3 Experiments 339 in which HIand Hrare the incident and reflected wave heights, respectively, and

27l

(JE-

T

The combined wave system qcis

q c = r l i + rlr (12.17)

The total vertical displacement, 2Iqc1, of the combined wave system can be shown to be

2lqcl = JfZ? +2HlH,cos (2kx +6)+H,Z (12.18)

Equation (12.18) defines a quantity referred to as the “wave height envelope” as a function of distance along the channel. The maximum and minimum of this expression are

2I~c Imax =Hi +Hr (12.19) and

2Iq c Imin =Hi -Hr (12.19)

The reflection from the beach can be defined in terms of a reflection and occur at positions along the channel separated by L/4. coefficient,

&=-=Hr 2I~c lmax -2I~c lmin (12.20)

Ht 2I~c lmax -t- 2I~c Imm

The minimum and maximum values of the reflection coefficient are 0 and

- 1.0,respectively.


###### Miche’s “Theory”.

A very approximate “theory” for the reflection coefficient from a plane smooth beach has been developed by A. Miche. Miche defines a critical deep water wave steepness (Ho/Lo)cntin terms of the beach slopej?:

(12.21)

Miche’s results predict that the beach reflection coefficient will vary with deep water wave steepness, H,/L,, in the followingmanner:

K,= 1,

(12.22)



---PAGE-356---



340 Experimentsfor LaboratoryCourse Component in Water Waves Chap. 12

###### K,= HdLO ’ L O crit

The deep water wave height referred to in these equations is that of the incident wave. The relationship between the deep water wave height and the incident wave height is

(12.23) where the ratio C&, is plotted versush/L, in Figure 3.9.

Measurement. For two wave periods, the wave height envelope is to be establishedby moving a wave gage along the channel over a distance of at least one wave length. From these envelopes, the measured beach reflection coefficients can be determined and compared with those of Miche’s theory

12.3.6 Experiment6: Wave Reflection from a PartialVertical Barrier; Comparisonwith Approximate Theory

The purpose of this experiment is to derive an approximate theory for the wave height transmitted past the vertical partial barrier shown in Figure 12.9 and to test the theory for various wavelengths and a fixed “gap opening” of height A.

Backgroundandtheory. A portion ofthe wave energyincident on the barrier will be reflectedas a reflectedwave component and a portion will pass beneath the barrier and form a transmitted wave component. As a first approximation to determining the height of the transmitted wave component, one couldassume thatall the progressivewave energy being propagated at those levels below the lower edge of the barrier is transmitted past the

-

-

Reflected wave Incident wave

Transmitted wave

Figure 12.9 Experimental arrangement.



---PAGE-357---



Sec. 12.3 Experiments 341

barrier and results in a transmitted wave. Developan approximate theory on this basis and express the result in the form of transmission coefficient IC,, where

K~= function of (kA, kh) (12.24)

For a ratioA/h=i,plotIC,as a function ofkh for the rangen/lO<kh <n.Also plot the deep and shallow water asymptotes for K~.If no energy is lost in the reflection-transmission process, then

Hf+H: =H: (12.25) or defining a reflection coefficient,

###### K[ =Hi

(12.26) then rc: +$= 1.

-

###### Hi

Measurements. For A/h = i, measure the wave envelope for x <0 and the transmitted wave height Ht for x > 0. From the wave envelope, determine H, and H, and compare your experimental values of xt with the approximate theory.

Calculate the sum I$+ # for your individual experiments and determine the percentage energy loss in the reflection-transmission process.

Carry out the measurements and calculations described above for four differentwave lengths.

12.3.7 Experiment 7: Wave Forceson Cylinders

and Spheres

The purpose of experiment 7a is to measure wave forces and moments on a circular cylinder and to determine the “best fit” drag and inertia coefficients associatedwith these measurements. Experiment 7b will consist of the measurement of wave forceson a sphere with the prior calculation of wave forces based on drag and inertia coefficients obtained from the literature (see,e.g., Grace and Casciano, 1969).

Measurements. The measurements will be conducted using a portaltype force gage and a cantilever moment gage (see Figure 12.10). In addition, the wave profile near to the object should be measured.

Theory of wave forces. The Morison equation for horizontal wave forces is written for an elemental length of a cylinder as (see Figure 12.11)

dF=CDpA, ds + C,pd Vu

(12.27)

2



---PAGE-358---



###### 342 Experimentsf or LaboratoryCourse Component inWater Waves Chap. 12

###### Piston

-“Portal” force gage wavemaker Moment gage 4--+

Figure 12.10 Test arrangement for measuring wave forcesand moments.

in which

CD= drag coefficient CM=inertia coefficient

p = mass density of water

A, = cylinder area per unit length projected onto a vertical plane ds = elemental length of cylinder

perpendicular to the velocity vector

dV =elemental volume in length, ds

u, u =horizontal component of water particle velocity and

acceleration, respectively

For a circular cylinder, Eq. (12.27) becomes

dF=CDpD~u l u l ds+CMp-E D 2u ds

- (12.28)
- (12.29)


2 4

which, for linear water wave kinematics, can be integrated to

H2kh cos at 1cos at I

F=yCJI-

-sinh2kh I+- + 1+- -yCM--lrD2 sinat[sinhkh(1+x)]

8 sinh 2kh

[2Lh ( l)( l)] 8 coshkh

Elemental force on a

Figure 12.11

cylinder.



---PAGE-359---



Sec. 12.3 Experiments 343

and the total moment about the bottom of the tank is M=yCDD-H2hkh cos at lcos at I

[" +:lh)*+- +'Ihsinh2kh(1+x>+--&(1-cosh2kh(1+x>)]

8 sinh 2kh

###### 2kh (2kh)

- Y c M-7cD2Hhsingt[(1+z )sinhkh(1+:) +&(1-coshkh(1+f))]

###### (12.30)

8 cosh kh

For a sphere, the equation is

###### 7cD2u l u l + C,p- 7cD3u. (12.31)

F = Cop------4 2 6

Scope of measurements. For a sphere and/or cylinder, measure the waves, wave forces, and moments for two wave periods of approximately 1.0 and 2.5 s. Measure the wave reflection in the tank.

For the two combinations of experimental wave conditions, calculate the waves, wave forces, and wave moments on the object and compare with those measured.

12.3.8 Experiment8: PlaneWavemaker

The purpose of this experiment isto evaluate the wavemaker theory for the piston-type wavemaker used in our studies.Although the beach isafairly efficient energy dssipator, the wave envelope should be measured to remove the effect of the reflected wave in the measurements.

Wavemaker theory for a piston-type wavemaker. The wavemaker theory for a piston-type wavemaker (aspresented in Chapter 6) is

###### H-= ~ ( C O 2khS ~ - 1) S sinh 2kh +2kh

###### (12.32)

See Figure 12.12 for a plot of H/S versus kh.

Measurements. Measure the wave generated for approximately 10 wave periods (say 0.8 < T < 2.5 s) for which the waves are well behaved. Evaluate the effect of reflection by measuring the wave envelope.



---PAGE-360---



344 Experimentsfor Laboratory CourseComponent inWaterWaves Chap. 12

I 1 I I I I I

- 0

2

0

Theory

-

###### .m

4x = S/2 sin 2ntlT

- -

###### Q

-

1

###### T -

Channel bottom

-

Definition sketch

1 I I I I I l 1 2 3 4 5 6 I 8

0

2nhIL

Figure 12.12 Test of wavemaker theory for small wave steepnesses.0,experiments correctedfor reflection;0, experiments not correctedfor reflection. (From Ursell et al., 1960.)

12.3.9 Experiment9: ApproximateWavemaker

Theoryfor a PerfectlyReflecting"Beach"

The purposeofthis experimentis to develop an approximate theory for the waves in a wave tank with perfectly reflectingboundaries and to conduct measurementsto evaluate this theory.

Theory. The approximate theory will be developedfor the case below. Although this problem is for shallow water waves in order to satisfy the boundary condition requirements, in comparing the results with measurements, the actual wave characteristics (particularly the wavelength) appropriate to the water depth and period should be used.

Consider the vertical barrier located at an arbitrary distance 1from a piston-type wavemaker (see Figure 12.13). Assuming that shallow water waves aregenerated, calculateand plot the ratioH/S as a functionofl/L.For this problem 0 = 1rad/s and h = 1ft.

Measurements. With a rigid vertical barrier located in the tank, conduct sufficient wave height measurements at the barrier over as wide a range of wave periods as possible to verify the approximate theory. Note that it will be helpful (perhaps in locating the barrier) if the theory is developed and incorporated in the planning phase of the experiment.



---PAGE-361---



###### Chap. 12 References 345

Piston-type -

wavemaker s =S/2 sin at

Figure 12.13 Experimentalarrangementforexperiment9.

REFERENCES GRACE,R.A., and E M. CASCIAN“O,O ceanWave Forces on a Subsurface Sphere,”J. REID,R.O., and C. L. BRETSCHNEIDER,“Surface Waves and Offshore Structures,” URSELL,E, R. G. DEAN,and Y. S.Yu, “Forced Small Amplitude Water Waves: A WEGGEL,J. R., “Maximum Breaker Height,” J. Waterways,Harbors CoasfatEng.

WaterwaysHarbors Div.,ASCE,Aug., 1969. TexasA. andM.Res. Found. Tech.Rept.,Oct. 1953. ComparisonofTheory and Experiment,”J. Fluid Mech.,Vol.7,Pt. 1,1960. Div,,ASCE,Vol. 98, WW4, Nov. 1972.



---PAGE-362---





---PAGE-363---



###### Subject Index

Airy, Sir George, 78 Accelerations

Conservation laws energy, 106 mass, 7 waves, 103

progressive wave, 80 second order, 305 total, 16

long waves, 134 Continuity equation, 10 Coriolis acceleration, 154 Coriolis parameter, 154 Covariance, 199 Cross-correlation, 199 Cross-covariance, 199 Cross product, 20 Cross spectrum, 201 Curl, 23 Cylindrical coordinates, 32

Added mass coefficient, 218ff Amphidromic waves, 155 Auto-correlation, 199

Bathystrophic storm tide, 161 Bernoulli equation, 33 Boundary conditions

bottom, 46 dynamic free surface, 48 kinematic, 44 kinematic free surface, 47 lateral, 50 wavemaker, 173

Damping coefficient internal damping, 267 laminar bottom boundary layer, 266 long waves, 146 porous media, 280

Boundary layer free surface, 268 laminar, 262 turbulent, 268

Darcy’s law, 278 Derivative, total, 9 Diffraction, 116 Diffraction theory, MacCamy-Fuchs,

Boussinesq, J.V., 261 Breaking of waves, 112 Buoyancy, 13

237 Directional wave spectrum, 202 Dispersion relationship, 58

Capillary wave, 69 Celerity, 3, 59 Cnoidal wave theory, 317

approximations, 71 mudlwater, 274 porous medialwater, 279

347



---PAGE-364---



348 Subject Index

Displacement parameter, 232 Displacements

Green's function, 246 Green's Law, 138 Groups, 188 Group velocity, 98

progressive wave, 80 standing wave, 88

Divergence, 22 Dot product, 19 Drag coefficient, for cylinder, 217,

227,235

Havelock, Sir Thomas H., 170 Helmholtz, Hermann, 284 Hydrostatic pressure, 11 Hyperbolic wave theory, 322

Energy kinetic, 96 long waves, 137 potential, 94 total, 97

Impulsive forces, 250 Inertia coefficients

Energy absorber, 178 Energy dissipation

cylinder, 218, 227, 235, 238 pipeline, 230

laminar boundary layer, 266 porous medium, 280 turbulent, 269 viscous internal, 267 viscous mud, 277

Inertia force component, circular Interfacial wave, waterfmud, 272 Irrotationality, 26

cylinder, 217

Energy flux, 97 long waves, 138

Kelvin, Lord, 131 Kelvin wave, 155 Keulegan-Carpenter parameter, 232 Kinetic energy, 96

Equations of motion, 16 long waves, 135, 136 Equivalent sand grain size, k,, 268 Euler equations, 18 Euler, Leonhard, 6

in flow field about a

moving circular cylinder, 221 Korteweg-DeVries equation, 313

FFT (fast Fourier transform), 201, 207 Force

Lamb, Sir Horace, 1 Laplace, Pierre Simon, 41 Laplace equation, 23 Lift coefficient, 230 Longshore wave thrust, 293 Long wave equations, 137

caisson, 247 cylinder, 222 floating body, 241 large cylinders, 237 pipeline, 227 rectangular objects, 238 vertical wall, 90 Fourier Analysis, 195 Friction, long waves, 146 Friction factor, 146

Mass transport Eulerian, 285 Lagrangian, 286

laminar, 265 turbulent, 268

Froude, William, 212

Mean pressure, 288 Mean water level, 287 Merian formula, 146 Moment, cylinder, 233 floating body, 245 Momentum flux, 289

Geostrophic effects, 154 Gradient, 21



---PAGE-365---



Subject Index 349

Morison equation, 221 Mud, 271

Standing wave, 57, 61 partial, 90 wavemaker, 174

Stokes, G. G., 295 Storm surge, 157 Stream function

Parseval’s theorem, 197, 200 Periodicity condition, 52 Permeability, 278 Perturbation, 298 Pipelines, wave forces on, 227 Porous media, 277 Potential energy, 94 Power spectrum, 200 Pressure

definition, 28 waves, 71

Stream function wave theory, 305 Streamline, 30

Taylor series, 7 Tides, co-oscillating, 138 Time series, simulation, 207 Trajectories

hydrostatic, 11 mean, 288 wave-induced, 83, 89

Pressure response factor, 84 Probability density function, 192 Progressive wave, 62

progressive, water particle, 80 standing, water particles, 88

Transmission

second order, 300

abrupt transition, 141 coefficient, 143

Radiation stress, 290 Rayleigh, Lord, 187 Rayleigh distribution, 190ff Reflection

Unit vector, 19 Ursell parameter, 319

coefficient, 143 transition, abrupt, 141 Refraction coefficient, 108 Reynolds number, 216

Vector differential operator, 21 Velocities

cnoidal wave, 322 long wave, 132 solitary wave, 316 standing wave, 86 stokes wave, 305

Seiching, 144 Separation of variables, 53 Setdown, 287 Setup, 292 Shear stress

Velocity potential circular cylinder, 214 definition, 25 progressive wave, 62 second order, 302 standing wave, 57, 61

bed, 265 bottom, 146 definition, 14

Shoaling coefficient, 108 Significant wave height, 188 Snell’s law, 105 Solitary wave, 314 Spectra

Wake, 216 Wave absorbers, 178 Wave equation, 137 Wave force maximum, 234 Wave height

amplitude, 194 energy, 194 narrow banded, 190, 194

Spectral analysis, 194 Spectral wave forces, 254

RMS, 188 significant, 188



---PAGE-366---



350

SubjectJndex

Wave length, 59 Wavemakers

plunger, 184 Power requirement, 177 shallow water, 171 snake, 179 spiral, 170, 181

cylindrical, 180 flap, 176 piston, 176



---PAGE-367---



###### Author lndex

Aagaard, Pi M., 224,227,228 Abramowitz, M., 118, 193 Airy, G. B., 303 Arthur, R. S., 109

Dalrymple, R. A., 69, 115, 124, 170, 181,

241,250,276,308, 309 Dean, R. G., 69,93,144,170,177,181, 224, 227, 228, 241, 250, 305, 308,309,323, 344

de Vries, G., 313, 317

Baer, L., 157 Berkhoff,J. C. W., 123 Berklite, R. B., 250 Birkemeier,W. A., 115 Bland, D. R., 43 Borgman, L. E., 205, 254, 305 Bousinesq, J., 315 Bretschneider, C., 336 Brink-Kjaer, O., 124 Buhr Hanson, J., 116

Ebbesmeyer, C. C., 305 Eckart, C., 72 Eubanks, R. A., 115

Flick, R. E., 178 Forristall, C. Z., 193 Freeman, J. C., 157 Fuchs, R. A.: 237

Carlsen, N. A., 268 Carpenter, L. H., 232 Cartwright, D. E., 204 Casciano, E M., 341 Chakrabarti, S., 241 Chaplin, J. R., 308 Chappelear, J. E., 305 Cokelet, E. D., 306 Coleman, J. M., 271 Collins, J. I., 105 Cooley, R. J. W., 195 Cox, J. C., 309

Gade, H., 271 Galvin, C. J., 113, 171 Garrison, C. J., 235, 246, 247, 250 Gaughan, M. K., 115 Gerald, C., 308 Goldstein, S., 216 Grace, R. A., 341 Guza, R. T., 178

351



---PAGE-368---



352 Author Index

Henderson, J. A., 305 Herbich, J., 241 Higgins,A. L., 205 Hilaly, N., 144 Hildebrand, E B., 308 Hinwood, J. B., 157 Hunt, J. N., 72

Noda, E. K., 105, 112

O'Brien, M. F ,! 221

Panicker, N. N., 205 Pawka, S., 205 Penny, W. G., 117 Phillips, 0.M., 268, 291 Pierson, W J., 210 Platzman, G.W., 156 Price, A. T., 117 Proudman, J., 146, 155

Ippen, A. T., 4 Iwagaki,Y.,322

Jacobsen, L. S., 250 Jenkins, G. M., 201 Johnson, J. W., 221 Jonsson, I. G., 124, 268 Jung, G. H., 157

Radder, A. C., 124. Reid, R. O., 230, 280, 336 Rumer, R. R., 151 Rupert, V. C., 105

Kaijura, K., 268, 280 Kamphuis, J. W., 266, 268 Keulegan, G. H., 232 Kirby, J. T., 124 Komar, J. D., 115, 293 Korteweg, D. J., 313, 317

Sarpkaya, T., 230,233 Schaaf, S.A., 221 Schlichting, H., 217 Schwartz, L. W., 306 Seymour, R. J., 205 Shiau, J., 151 Skjelbreia, L., 305 Smith, N. D., 204 Smith, R., 124 Sommerfeld, A., 118, 173 Sonu, C. J., 105 Sprinks, T., 124 Stacey, R., 247 Starr, V. I?, 286 Stegun, I. A., 118, 193 Stewart, R. W., 291, 292 Stokes, G. G., 296 Svendsen, I. A., 116

Laitone, E. V., 5 Lamb, H., 4, 140, 168, 219, 263, 275 Liu, I? L.-E, 124, 273, 276, 281 Longuet-Higgins, M. S., 191, 204, 291,

292, 293

Lorentz, H. A., 147 Lozano, C. J., 124

MacCamy, R. C., 237 Madsen, 0.S., 178, 186 McCowan, J., 113 Mei, C. C., 181, 273 Miche, A., 359 Milgram, J. H., 178 Morison, J. R., 221 Munk, W. H., 109, 115, 315, 317

Taylor, Sir G., 156 Thompson, W. (Lord Kelvin), 155 Tukey, J. W., 195



---PAGE-369---



Author Index 353

Wells, J. T.,231 Wiegel, R. L., 4, 130, 321 Wilson, B. W., 146, 148, 230 Wilson, W. S., 112 Witham, G. B., 4 Wright, J. C., 230 Wu, J., 157 Wylie, C. R., 311

Ursell, E, 93, 177, 304, 344

Van Dorn, W. C., 157 Versowski, F? E., 241

Wallis, I. G., 157 Wang, S., 184 Watts, D. G., 201 Weggel, J. R., 113, 337 Wehausen, J. V., 5

Yamamoto,T., 230 Yu,Y. S.,177, 344



---PAGE-370---





---PAGE-371---



