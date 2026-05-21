

---PAGE-1---



3rd DRAFT

# EFDC Technical Memorandum

# Theoretical and Computational

# Aspects of Sediment and Contaminant Transport in

# the EFDC Model

Prepared for: US Environmental Protection Agency, Office of Science and Technology 401 M Street SW Washington, DC 20460

Prepared by: Tetra Tech, Inc. 10306 Eaton Place Suite 340 Fairfax, Virginia 22030

May 2002



---PAGE-2---



## Table of Contents

- 1. Introduction 3
- 2. Summary of Hydrodynamic and Generic Transport Formulations 4
- 3. Solution of the Sediment Transport Equation 9
- 4. Hydrodynamic and Sediment Boundary Layers 11
- 5. Sediment Bed Mass Conservation and Geomechanics 14
- 6. Noncohesive Sediment Settling, Deposition and Resuspension 26
- 7. Cohesive Sediment Settling, Deposition and Resuspension 34
- 8. Sorptive Contaminant Transport 47
- 9. References 53




---PAGE-3---



## 1. Introduction

This report summarizes theoretical and computational aspects of the sediment and sorptive contaminant transport formulations used in the EFDC model. Theoretical and computational aspects for the basic EFDC hydrodynamic and generic transport model components are presented in Hamrick (1992). Theoretical and computational aspects of the EFDC water quality-eutrophication model component are presented in Park et al.

(1995). The paper by Hamrick and Wu (1997) also summarized computational aspects of the hydrodynamic, generic transport and water quality-eutrophication components of the EFDC model. The EFDC model has been extensively applied to estuaries (Fredricks and Hamrick, 1996; Shen and Kuo, 1999; Shen et al., 1999; Ji et al., 2001), lakes (Jin et al., 2000; 2002), reservoirs (Hamrick and Mills, 2000), rivers (Ji, et al., 2002), and wetlands (Moustafa and Hamrick, 2000). The model has also been used for a number of fundamental process studies (Hamrick, 1994; Kuo, et al., 1996; Yang, et al., 2000).

This report is organized as follows. Chapter 2 summarizes the hydrodynamic and generic transport formulations used in EFDC. Chapter 3 summarizes the solution of the transport equation for suspended cohesive and noncohesive sediment. A discussion of near bed boundary layer processes relevant to sediment transport is presented in Chapter

4. Sediment bed mass conservation and methods for representation of the bed’s geomechanical properties are discussed in Chapter 5. Chapters 6 and 7 summarize noncohesive and cohesive sediment settling, deposition and resuspension process representations. The final chapter, Chapter 9, documents the EFDC model's sorptive contaminant transport and fate formulations.



---PAGE-4---



## 2. Summary of Hydrodynamic and Generic Transport Formulations

This section summarizes the hydrodynamic and transport equations used by the EFDC model. Reference is made to Hamrick (1992) and Hamrick and Wu (1997) for details of the computational procedure. This section does however describe modifications to the solution procedure when the model operates in a geomorphologic mode.

The EFDC model's hydrodynamic component is based on the three-dimensional hydrostatic equations formulated in curvilinear-orthogonal horizontal coordinates and a sigma or stretched vertical coordinate. The momentum equations are:

m m Hu m Huu m Hvu m m wu f m m Hv A m H p p m z z H p m m u

t x y x y y x z x y e x y

*

v y x atm y x b x z z x y z

(2.1)

H m m

2 2 1/2

y x x H x y H y x y p p x y

HA u HA u m m c D u v u m m

m m Hv m Huv m Hvv m m wv f m m Hu A m H p p m z z H p m m v

t x y x y y x z x y e x y

*

v x y atm x y b y z z x y z

(2.2)

H m m

2 2 1/2

y x x H x y H y x y p p x y

HA v HA v m m c D u v v m m

m xmy fe mxmy f u ymx v xmy (2.3)

xz , yz AvH 1 z u,v (2.4)

where u and v are the horizontal velocity components in the dimensionless curvilinearorthogonal horizontal coordinates x and y, respectively. The scale factors of the horizontal coordinates are mx and my. The vertical velocity in the stretched vertical coordinate z is w. The physical vertical coordinates of the free surface and bottom bed are zs* and zb* respectively. The total water column depth is H, and is the free surface potential which is equal to gzs*. The effective Coriolis acceleration fe incorporates the curvature acceleration terms, with the Coriolis parameter, f, according to (2.3). The Q terms in (2.1) and (2.2) represents optional horizontal momentum diffusion terms. The vertical turbulent viscosity Av relates the shear stresses to the vertical shear of the horizontal velocity components by (4.4). The kinematic atmospheric pressure, referenced to water density, is patm, while the excess hydrostatic pressure in the water column is given by:



---PAGE-5---



z p gHb gH o o (2.5)

1

where and o are the actual and reference water densities and b is the buoyancy. The horizontal turbulent stress on the last lines of (2.1) and (2.2), with AH being the horizontal turbulent viscosity, are typically retained when the advective acceleration are represented by central differences. The last terms in (2.1) and (2.2) represent vegetation resistance where cp is a resistance coefficient and Dp is the dimensionless projected vegetation area normal to the flow per unit horizontal area.

The three-dimensional continuity equation in the stretched vertical and curvilinearorthogonal horizontal coordinate system is:

t mxmyH x myHu y mxHv z mxmyw QH 0 QSS QSW (2.6)

with QH representing volume sources and sinks including rainfall, evaporation, and lateral inflows and outflows having negligible momentum fluxes. The terms QSS and QSW are the net volumetric fluxes of sediment and water between the bed and water column, defined as positive from the bed to the water column, when the model operates in a geomorphologic mode. The delta function, (0) indicates these fluxes enter the bottom layer of the water column. Integration of (2.6) over the depth gives

t mxmyH x myHu y mxHv QH QSS QSW (2.7)

In the geomorphologic mode, the water column continuity equation is coupled to a bulk volume conservation equation for the sediment bed.

t mxmyB QGW QSS QSW (2.8)

where B is the total thickness of the resolved sediment bed and QGW is the volumetric ambient groundwater inflow at the bottom of the sediment bed. The bed surface elevation is defined by

B zbb (2.9)

*

Where zbb* is the time invariant elevation at the bottom of the sediment bed. Using (2.9), equation (2.8) can be written as

t mxmy QGW QSS QSW (2.10)

Adding (2.7) and (2.10) gives

t mxmy x myHu y mxHv QH QGW (2.11)



---PAGE-6---



###### where the water surface elevation, , is defined by

zs H (2.12)

*

The EFDC model solves the external mode continuity equation (2.11) using a two-step procedure. The first step corresponding to the standard implicit external mode hydrodynamic solution is

n n n x y x y x y x y

* 1

m m m m m Hu m Hu

- 1 1/2
- 2 2


n n n y x y x H

m Hv m Hv Q

2 2

(2.13)

where is the time step between n and n+1. The intermediate time level notation, n+1/2, denotes an average between the two time levels. The second step is taken after the bed volumetric continuity equation is updated to time level n+1 and is

mxmy mxmy QG (2.14)

n 1 * n 1/2

Combining (2.13) and (2.14) gives the equivalent full step.

n n n n x y x y x y x y

1 1

m m m m m Hu m Hu

2 2

n n n n y x y x H G

1 1/2 1/2

m Hv m Hv Q Q

2 2

(2.15)

The water column depth is then updated by

Hn 1 n 1 n 1 (2.16) prior to the next hydrodynamic time step. The EFDC model includes the ability to simulate drying and wetting of shallow areas. Drying and wetting is iteratively determined during the implicit solution of equation (2.13) after the time discrete depth average horizontal momentum equations have been inserted to form an elliptic equation for the water surface elevation. The solution procedure is as follows. A preliminary solution for the water surface elevation is determined by solving (2.13) with all horizontal grid interior horizontal cell faces open. The resulting cell center water depth in each cell is then compared to a small dry depth Hdry. If the depth is greater than the dry depth, the cell is defined as wet. If the depth is less than the dry depth and less than the depth at the previous time step, the cell is defined as wet and its four flow faces are blocked. If the depth is less than the dry depth, but greater than the depth at the previous time step, the direction of flow on each cell face is checked and faces having outflow are block. Following this checking and blocking,



---PAGE-7---



(2.13) is solved again, followed by the same checking procedure. This iteration is repeated until wet or dry status of each cell does not change from that of the subsequent iteration. Typically two or three iterations are required. This implementation of drying and wetting is fully mass conservative and does not produce negative water column depths.

The generic transport equation for a dissolved or suspended material having a mass per unit volume concentration C, is

m m HC m HuC m HvC m m wC m m w C m m K

t x y x y y x z x y z x y sc

(2.17)

y x v x H x y H y z x y z c x y

HK C HK v m m C Q m m H

where KV and KH are the vertical and horizontal turbulent diffusion coefficients, respectively, wsc is a positive settling velocity went C represents a suspended material, and Qc represents external sources and sinks and reactive internal sources and sinks.

The solution of the momentum equations, (2.1) and (2.2) and the transport equation (2.17), requires the specification of the vertical turbulent viscosity, AV, and diffusivity, Kv. To provide the vertical turbulent viscosity and diffusivity, the second moment turbulence closure model developed by Mellor and Yamada (1982) and modified by Galperin et al., (1988) and Blumberg et al., (1988) is used. The MY model relates the vertical turbulent viscosity and diffusivity to the turbulent intensity, q, a turbulent length scale, l, and a turbulent intensity and length scaled based Richardson number, Rq, by:

A A ql

v A o

1 1

R R R R R R

1 1 1

q A

- 1 1
- 2 3


q q

- A

- A A C

B B

- A

B A C B A

- B

R A

- A

C

- B








6 1 1 3

1 1 1 1/3 1 1

o

6

1 2 2 1 2 1

3 1 3 6 3

- 1 1
- 1 2


6 1 3

1 1

1

- 1
- 2 1 2


R A A R A A B

9 3 6

1 3 2 1 2

(2.18)



---PAGE-8---



K K ql

v K o

1 1

K

1 3

R R

q

- A

K A

- B


6 1

1 2

o

1

2 2 2

gH b l R

z q

q H

(2.19)

(2.20)

where the so-called stability functions, A and K, account for reduced and enhanced vertical mixing or transport in stable and unstable vertically density stratified environments, respectively. Mellor and Yamada (1982) specify the constants A1, B1, C1, A2, and B2 as 0.92, 16.6, 0.08, 0.74, and 10.1, respectively.

The turbulent intensity and the turbulent length scale are determined by the transport equations:

2 2 2 2

m m Hq m Huq m Hvq m m wq

t x y x y y x z x y

3 2

A Hq m m q m m

(2.21)

q z x y z x y

2

H Bl A

1

2 2 2 2 3/2

v x y z z p p p v z q

m m u v c D u v gK b Q H

2

2 2 2 2

m m Hq l m Huq l m Hvq l m m wq l

t x y x y y x z x y

3 2 2 2

(2.22)

A Hq l l m m q l m m E E

q z x y z x y

1

2 3 1

H B Hz H z A m m E l u v gK b c D u v Q H

1

2 2 2 2 3/2 1

v x y z z v z p p p l

where (E1, E2, E3) = (1.8, 1.33, 0.25). The second term on the last line of each equation represents net turbulent energy production by vegetation drag where p is a production efficiency factor having a value less than one. The terms Qq and Ql may represent additional source-sink terms such as subgrid scale horizontal turbulent diffusion. The vertical diffusivity, Aq, is set to 0.2ql following Mellor and Yamada (1982). For stable stratification, Galperin et al., (1988) suggest limiting the length scale such that the square root of Rq is less than 0.52. When horizontal turbulent viscosity and diffusivity are included in the momentum and transport equations, they are determined independently using Smagorinsky's (1963) subgrid scale closure formulation.



---PAGE-9---



Vertical boundary conditions for the solution of the momentum equations are based on the specification of the kinematic shear stresses, equation (2.4), at the bed and the free surface. At the free surface, the x and y components of the stress are specified by the water surface wind stress

xz , yz sx , sy cs Uw2 Vw2 Uw ,Vw (2.23)

where Uw and Vw are the x and y components of the wind velocity at 10 meters above the water surface. The wind stress coefficient is given by:

s 0.001 a 0.8 0.065 w2 w2

c U V

w

(2.24)

for the wind velocity components in meters per second, with a and w denoting air and water densities respectively. At the bed, the stress components are related to the near bed or bottom layer velocity components by the quadratic resistance formulation

xz , yz bx , by cb u1 v1 u1,v1 (2.25)

2 2

where the 1 subscript denotes bottom layer values. Under the assumption that the near bottom velocity profile is logarithmic at any instant of time, the bottom stress coefficient is given by

2

- b ln( 1 / 2 o)
- c z


(2.26)

where , is the von Karman constant, 1 is the dimensionless thickness of the bottom layer, and zo=zo*/H is the dimensionless roughness height. Vertical boundary conditions for the turbulent kinetic energy and length scale equations are:

q B1 τs : z 1 (2.27)

2 2/3

q B1 τb : z 0 (2.28) l 0 : z 0,1 (2.29)

2 2/3

where the absolute values indicate the magnitude of the enclosed vector quantity. Equation (2.28) can become inappropriate under a number of conditions associated with either or both high near bottom sediment concentrations and high frequency surface wave activity. The quantification of sediment and wave effects on the bottom stress is discussed in Chapter 4.



---PAGE-10---



## 3. Solution of the Sediment Transport Equation

This section describes the solution of the transport equations for suspended sediment. The general procedure follows that for the salinity transport equation, which uses a high order upwind difference solution scheme for the advective terms, described in Hamrick (1992). Although the advection scheme is designed to minimize numerical diffusion, a small amount of horizontal diffusion remains inherent in the scheme. Due the small inherent numerical diffusion, the physical horizontal diffusion terms in (2.17) are omitted as to give:

m m HS m HuS m HvS m m wS K m m w S m m S Q Q H

t x y j x y j y x j z x y j

V E I z x y sj j z x y z j sj sj

(3.1)

where Sj represents the concentration of the jth sediment class and the source-sink term has been split into an external part, which would include point and nonpoint source loads, and internal part which could include reactive decay of organic sediments or the exchange of mass between sediment classes if floc formation and destruction were simulated. Vertical boundary conditions for (3.1) are:

K

V

S w S J z H

: 0

z j sj j jo

K

V

S w S z H

0: 1

z j sj j

(3.2)

where Jjo is the net water column-bed exchange flux defined as positive into the water column.

The numerical solution of (3.1) utilizes a fractional step procedure. The first step advances the concentration due to advection and external sources and sinks having corresponding volume fluxes by

n n n E n

1 * 1/2

H S H S Q m m

sj x y

n n n n n n x y y x z x y

1/2 1/2 1/2

m Hu S m Hv S m m w S m m

x y

(3.3)

where n and n+1 denote the old and new time levels and * denotes the intermediate fractional step results. The portion of the source and sink term, associated with volumetric sources and sinks is included in the advective step for consistency with the continuity constraint. This source-sink term, as well as the advective field (u,v,w), is defined as intermediate in time between the old and new time levels consistent with the temporal discretization of the continuity equation. Note that the sediment class subscripts



---PAGE-11---



have been dropped for clarity. The advection step uses the anti-diffusive MPDATA scheme (Smolarkiewicz and Clark, 1986) with optional flux corrected transport (Smolarkiewicz and Grabowski, 1990).

The second fractional step or settling step is given by

** * **

S S n 1 z wsS

H

(3.4)

which is solved by a fully implicit upwind difference scheme

(3.5)

** * ** 1

S S w S H

kc kc n s kc z

** * ** **

S S w S w S k kc H H

: 2 1

k k n s k n s k z

1 1 1 1

** * ** 1 1 1 2

S S w S H

n s z

marching downward from the top layer. The implicit solution includes an optional antidiffusion correction across internal water column layer interfaces.

The third fractional step accounts for water column-bed exchange by resuspension and deposition

*** ** *** 1 1 n 1 o o

S S L J H

z

(3.6)

Where Lo is a flux limiter such that only the current top layer of the bed can be completely resuspended in single time step. The representation of the water column bed exchange by a distinct fractional step is equivalent to a splitting of the bottom boundary condition (3.2) such that the bed flux is imposed intermediate between settling and vertical diffusion. For resuspension and deposition of suspended noncohesive sediment, the bed flux is given by

w J S S

*** *** 1

s o eq

(3.7)

which will be further discussed in Chapters 4 and 6. Inserting (3.7) into (3.6) gives

L w L w

*** **

1 on 1s 1 1 on 1s eq

S S S H H

z z

(3.8)



---PAGE-12---



For cohesive sediment resuspension, the bed flux is specified as a function of the bed stress and bed geomechanical properties. For cohesive sediment deposition, the bed flux is typically given by

Jo PdwsS1 (3.9)

*** ***

where Pd is a probability of deposition which will be further discussed in Chapter 7. Inserting (3.9) into (3.6) gives

P w

*** **

1 d ns1 1 1

S S H

z

(3.10)

The remaining step is an implicit vertical turbulent diffusion step corresponding

n n V n z z

1 1 *** 1 2

K S S S H

(3.11)

with zero diffusive fluxes at the bed and water surface.



---PAGE-13---



## 4. Hydrodynamic and Sediment Boundary Layers

Both two-dimensional and three-dimensional applications of the EFDC model require parameterization of near bed boundary layer processes. In the absences of high frequency surface gravity waves and when sediment transport is not being simulated, this parameterization is made through the bottom friction coefficient, (2.26) and the bottom turbulence intensity boundary conditions (2.28). The presence of high frequency surface gravity waves and near bed gradients of suspended sediment requires additional parameterization since the sediment and wave boundary layers cannot be directly resolved by typical vertical grid resolution. Approximate parameterizations of hydrodynamic and sediment boundary layer appropriate for representing the bottom stress and the water column-bed exchange of sediment under conditions including ambient flow, high frequency surface waves and high near bed suspended sediment gradients can be derived form simplified forms of the momentum and sediment transport equations and the turbulent kinetic energy equation.

- 4.1 Boundary Layer Equations First consider the horizontally homogeneous momentum equation written in vector form


1

tu p g H z AV zu

(4.1)

The horizontal velocity, pressure and water surface elevation can be decomposed into components associated with the current or mean flow and the high frequency surface gravity wave motion

###### u u u

c w

p p

w

c w

(4.2)

where the current pressure in excess of hydrostatic pressure has been set to zero. Assuming the current is steady with respect to the time scale of the wave motion and inserting (4.2) into (4.1) gives

1

tuw pw g w c H z AV z uw uc

(4.3)

On non-geophysical scales where the bottom current boundary layers does not exhibit Ekman effects, equation (4.3) can be vectorially split into components aligned with the wave and current directions



---PAGE-14---



v

- t w w w w z z w

v c w c c z z c

A

- u p g u H


2

A g u H

cos 2 0

(4.4)

A u p g u

v c w t w w w w z z w

cos

2

H A

(4.5)

v c c z z c

g u H

0

2

where c and w are the directions of the current and wave propagation, respectively, and for simplicity in notation uw and uc are the wave and current velocities in these two directions. Subtracting the wave period average of (4.4) from (4.4) gives an equation for the wave motion

v v

- t w w w w z z w z w

v v c w z z c

A A

- u p g u u H H


2 2

A A

u H

cos 2 0

(4.6)

Averaging (4.5) over the wave period gives an equation for the mean current

###### A A g u u H H

c c z v2 z c cos c w z v2 z w 0

(4.7)

Wave-current boundary layer models formulated for use with numerical circulation models typically neglect variations in the vertical turbulent viscosity at the wave time scale (Styles and Glenn, 2000) allowing (4.6) and (4.7) to be reduced to

- t w w w w z v2 z w 0

A

- u p g u H


(4.8)

A g u H

c c z v2 z c 0

(4.9)

Above the wave boundary layer, the wave velocity field is inviscid and (4.8) reduces to

tuw w pw g w 0

(4.10)



---PAGE-15---



###### which is subtracted from (4.8) to give the wave boundary layer equation

v

- t w z z w t w

A

- u u u H


2

The boundary conditions for (4.11) are

A

v

u H

z w wb

or u

0

w

As z goes to the roughness height zo, and

u w uw

(4.11)

(4.12)

(4.13)

as z becomes large. Integrating of (4.9) over the bottom hydrodynamic model layer and subtracting the results from (4.9) gives the current boundary layer equation

A

v c cb z z c

1

u H

1

(4.14)

where the c1 and cb subscripts denote the shear stresses at the top and bottom of the bottom grid layer. Integration of (4.14) gives

A z

v

u H

z c cb c cb

1

1

(4.15)

Where 1 is the dimensionless thickness of the bottom grid layer. For small z near the bed, (4.15) is approximated as a constant stress layer

A

v

u H

z c cb

The boundary condition for (4.16) is

uc 0

(4.16)

(4.17)

as z goes to the roughness height zo. In the bottom hydrodynamic layer the integral condition



---PAGE-16---



1

ucdz u

1 1 0

(4.17)

is imposed where u1 is the current velocity in the bottom grid layer. The sediment boundary layer equation can be derived form the horizontally homogeneous approximation to the sediment transport equation (3.1).

K HS w S S H

t z s V z 0

Integrating (4.18) over the bottom hydrodynamic layer gives

J J HS

sb s t

1 1

1

(4.18)

(4.19)

Where S1 is the bottom layer sediment concentration and Jsb and Js1 are the sediment fluxes at the bed and the top of the bottom grid layer. Subtracting (4.19) from (4.18) gives

K J J HS HS w S S

V s sb t z s z

1 1

H

1

(4.20)

Assuming that the temporal derivative in (4.20) is small and can be neglected, (4.20) is integrated to give

K z w S S J J J

V s z sb s sb

1

H

1

(4.21)

For small z near the bed, (4.21) is approximated as a constant flux layer

K z w S S J

s V z sb 1

H

1

(4.21x)

K w S S J H

V s z sb

The bottom boundary condition for (4.22) is

S S r

(4.22)

(4.23)



---PAGE-17---



###### as z goes to the dimensionless sediment reference height zr, which can be the roughness height. In the bottom hydrodynamic layer the integral condition

1

Sdz S

1 1 0

(4.24)

is imposed. The near bed wave, current and sediment boundary layer equations (4.11, 4.16, and 4.22) require specification of the near bed forms of the vertical turbulent viscosity and diffusion coefficients. Near the bed, the turbulent kinetic energy equation (2.21) can be approximated by its equilibrium form

3

q A K

2 2 2

v v z z z

u v g b Bl H H

1

(4.25)

where the vegetation term has been dropped since the horizontal velocity components approach zero. Introducing the definitions of Av and Kv given by (2.18) and (2.19) and solving for the turbulent intensity gives

2 2 1 2 2 2

B A l q u v B K R H

- o A z z
- o K q


1 1

(4.26)

Equation (4.25) can be also be written in terms of the shear stresses after multiplying by Av, inserting the definitions of Av and Kv given by (2.18) and (2.19), and using (2.20), to give

1/2 2 1 1/2 2 2 1/2

B q B K R A

1 1 o K q xz yz

o A

(4.27)

When (4.27) is evaluated at the bed, the results

1/2 2 1 1/2 2 2 1/2

B q B K R A

b 1 1 o K q bx by

o A

(4.28)

is equivalent to (2.28) under neutral conditions where Rq is equal to zero. High near bed sediment concentrations and associated vertical gradients can result in nonzero values of Rq immediately above the bed.

The buoyancy gradient near the bed is primarily due to gradients in suspended sediment concentration with the effect of sediment on density given by



---PAGE-18---



S S (4.29)

1 j w j sj

j sj sj

where Sj is the mass concentration of sediment class j per unit volume of the watersediment mixture. The buoyancy is expressed in terms of the sediment concentration using

S

w sj w j

b S (4.30)

j j w j w sj j

which can be used to evaluate the buoyancy gradients. When high frequency surface waves are present, the velocity components in (4.25) and (4.26) and the shear stress components in (4.26) and (4.27) can be decomposed into

- u u u
- v u u


cos cos sin sin

c c w w

c c w w

(4.31)

cos cos sin sin

xz cz c wz w

yz cz c wz w

(4.32)

where uc and uw are the current and wave velocities and c and w are the current and wave shear stress magnitudes, each aligned with the current and wave directions denoted

by c and w. Using (4.32) and (4.32), the shear and bed stress terms can be written as

###### zu 2 zv 2 zuc 2 zuw 2 2cos c w zuc zuw (4.33)

xz 2 yz2 cz2 wz2 2cos c w cz wz (4.34)

Assuming the wave velocity and shear stress to be periodic

#### u u

t t

sin sin

w wm

wz wzm

t

sgn sin

w wm

(4.35)

the wave period averages of (4.31) and (4.32) are

2 2 2 1 2 4

cos z c z w z c 2 z wm c wm z c z wm u u u u u u

(4.36)



---PAGE-19---



2 2 2 1 2 4

cos cz wz cz 2 wzm c wm cb wzm

(4.37)

Analytical solutions of the wave, current and sediment boundary layer equations (4.11, 4.16, and 4.22), as exemplified most recently by Styles and Glenn (2000), typically assume tractable forms of the vertical turbulent viscosity and diffusivity inside the wavecurrent and the current boundary layers. The following sections discuss boundary layer parameterization for neutral and stratified boundary layers in absences and presences of waves.

### 4.2 Neutral Current and Sediment Boundary Layers

###### For neutral conditions, the turbulent intensity (4.27) and the vertical turbulent exchange coefficients (2.18) and (2.19) can be written as

q B1 xz yz (4.38)

2 2/3 2 2 1/2

Av Aoql xz yz l (4.39)

n 2 2 1/4

K

n o 2 2 1/4 v o xz yz

K K ql l A

o

(4.40)

For three-dimensional, multiple vertical layer applications equation (4.16) becomes

l

u H

z c cb

Letting l/H = z, and using (4.17) gives the logarithmic profile

z u

c cb ln

z

o

(4.41)

(4.42)

Applying the integral condition (4.17) over the bottom layer gives

cb b

1 1

2

- b o

c u u

- c z


ln( 1 /2 )

For two-dimensional depth average applications (4.15) becomes

(4.43)



---PAGE-20---



l

u z H

z c cb 1

(4.44)

For consistency with the subsequent solution of the sediment boundary layer equation, the length scale is chosen as

l z H z

1

(4.45)

With the solution of (4.44) becoming

z u z z z

c cb ln o

o

(4.46)

Applying the integral constraint (4.14) to (4.46) gives

cb b

1 1

2

- b o

c u u

- c z


ln(1/2 )

(4.47)

For three-dimensional multiple layer, applications, the sediment boundary layer equation (4.22) can be written as

z J S S R w

sb z

s

(4.48)

where

A w R

- o s
- o cb


K

(4.49)

is the Rouse parameter. The solution of (4.48) is

J C S

sb

R s

w z

(4.50)

For noncohesive sediment, the constant of integration is evaluated using

S Seq : z zeq and Jsb 0 (4.51)

which sets the near bed sediment concentration to an equilibrium value, Seq, defined just above the bed under no net flux condition. Using (4.51), equation (4.50) becomes



---PAGE-21---



R eq sb eq

z J S S

z w

s

(4.52)

For nonequilibrium conditions, the net flux is given by evaluating (4.52) at the equilibrium level

J sb ws Seq Sne (4.53)

where Sne is the actual concentration at the reference equilibrium level. Equation (4.53) indicates that when the near bed sediment concentration is less than the equilibrium value a net flux from the bed into the water column occurs. Likewise when the concentration exceeds equilibrium, a net flux to the bed occurs. For the relationship (4.53) to be useful in a numerical model, the bed flux must be expressed in terms of the model layer mean concentration. For a three-dimensional application, (4.53) and the constraint (4.24) give

Jsb ws Seqe S 1 (4.54)

where

1

z S S R

ln

eq eqe eq eq

: 1 1

1

z z

R eq

1 1

1

S S R R z

: 1 1 1

eqe eq eq

1

(4.55)

defines an effective bottom layer mean equilibrium concentration in terms of the near bed equilibrium concentration. The corresponding quantities in the numerical solution bottom boundary condition (3.7) are

W S w S W w

r r s eqe

d s

(4.56)

If the dimensionless equilibrium elevation, zeq exceeds the dimensionless layer thickness, (4.54) and (4.55) can be modified to

Jsb ws Seqe S (4.57)



---PAGE-22---



1

M z S S R

ln

eq eqe eq eq

: 1 1

1

M z M z

R eq

1 1

1

S S R R M z

: 1 1 1

eqe eq eq

1

(4.58)

where the over bars in (4.57) and (4.58) implying an average of the first M grid layers above the bed. When multiple sediment size classes are simulated, the equilibrium concentration, Seq, in (4.55) and (4.58) are reduced from their uniform values by multiplying by the sediment class volume fractions at the bed surface.

For cohesive sediment resuspension, the flux is presumed known, and the constant of integration in (4.48) is determined by the integral constraint with the resulting sediment concentration distribution being

J R z J S S R

1

sb r sb R R R s r s

1 1 1 1 1

: 1

w z z w J z J

sb r sb

1

S S R w z z w

: 1 ln

1 1 1

s r s

(4.59)

For cohesive sediment deposition, the bed flux is given by

J sb PdwsSr (4.60)

where Pd is the probability of deposition. Evaluating (4.59) at the reference level, inserting into (4.60) and solving, gives the deposition flux in terms of the bottom layer concentration

1

P R z R z J P P w S R

1 1 1 : 1

d r r sb d R R R R R R d s r r r r

1 1 1 1 1 1 1 1 1

z z z z P z z

(4.61)

1 1 1

d r r sb d d s r r r r

J P P w S R z z z z

1 : 1 ln ln

1 1 1 1 1

The sediment concentration profile under depositional conditions is also give by (4.59) using the flux from (4.61).

For depth average applications, the sediment boundary layer equation (4.21) can be written as



---PAGE-23---



z l J

1

z sb 1

S S z R H w

s

A closed form solution is possible by choosing

l z H z

1

with (4.59) becoming

R J R S S z z w z

z sb 1

s

The solution of (4.61) is

Rz J C S

sb

1

R s

R w z

1

(4.59)

(4.60)

(4.61)

(4.62)

Evaluating the constant of integration using (4.51) gives

R eq sb eq

z Rz J S S

1

z R w

1

s

For nonequilibrium conditions, the net flux is given by evaluating (4.63) at the equilibrium level

1 sb s 1 1 eq eq ne R

J w S S R z

(4.63)

(4.64)

where Sne is the actual concentration at the reference equilibrium level. Since zeq is on the order of the sediment grain diameter divided by the depth of the water column, (4.64) is essentially equivalent to (4.54). To obtain an expression for the bed flux in terms of the depth average sediment concentration, equation (4.63) is integrated over the depth to give

2 1 sb s 2 1 eq eqe R

J w S S R z

(4.65)

where



---PAGE-24---



1

z S S R

ln

eq

: 1

eqe eq eq

1

z z

1 1

R eq

1

S S R R z

: 1 1 1

eqe eq eq

1

(4.66)

When multiple sediment size classes are simulated, the equilibrium concentration, Seq, in (4.66) is reduced from its uniform value by multiplying by the sediment class volume fractions at the bed surface. The corresponding quantities in the numerical solution bottom boundary condition (3.7) are

R W S w S

2 1 2 1

r r s eqe eq

R z R

2 1 2 1

W w R z

d s eq

(4.67)

For cohesive sediment resuspension, the flux is presumed known, and the constant of integration in (4.62) is determined by the integral constraint with the resulting sediment concentration distribution being

(4.68)

R z z R Rz J S

1 1 1 1 2 1 1

r r sb R R R r s

1 1

1 1 1

R z z R w z R S

1

r R R R r

1 1

R z z

: 1

1 1 1

1 1 1 1

z z z J S

r r sb

ln 1 1 4 2

z z w z z z

r s

1

r

1 1

S1 : R 1

ln

r

For cohesive sediment deposition, the bed flux is given by

J sb PdwsSr (4.69)

where Pd is the probability of deposition. The depositional flux can be determined by evaluating (4.68) at the reference level, inserting the results into (4.69), and solving for the flux. The sediment concentration profile under depositional conditions is also give by (4.68) using the depositional flux.



---PAGE-25---



### 4.3 Stratified Current and Sediment Boundary Layers

Analytical solutions for stratified current and sediment boundary layers are difficult to obtain unless tractable expressions are assumed for the near bed distribution of the vertical turbulent viscosity and diffusion coefficients. An alternative is a numerical solution of the boundary layer equations using a sub-grid embedded in the bottom hydrodynamic grid layer. The distribution of the vertical turbulent viscosity and diffusion coefficients is presumed known form the sub-grid layer solution at the previous time step using (4.26) or (4.27) to determine the turbulent intensity. The sub-grid layer solution proceeds by writing equation (4.16) in finite difference form as

k

H u u

k k s c c cb

1

A

v

(4.70)

where k denotes the sub-grid layer and

z k

1 o s

s

(4.71)

is the thickness of the sub-grid layers with ks being the number of sub-grid layers embedded in the bottom grid layer. The integral constraint (4.17) becomes

ks

k c s c

u k u

1 1

k

(4.72)

where uc1 is the current velocity in the bottom grid layer. Solving the recursion (4.70) and substituting into (4.72) gives

k k

H u k k u k A

1

s

1

s c s cb c s v

1 1

(4.73)

The velocity profile in the bottom half of the near bed sub-grid layer is assumed to be logarithmic

cb s

1 ln

uc

2

(4.74)

Inserting (4.74) into (4.73) gives



---PAGE-26---



(4.75)

k k

2 1 1

H u k k u u k A

1 1 1 ln

s

s s c s c c s v

1 1

2

which can be solved iteratively for the current velocity in the bottom sub-grid layer when the distribution of the turbulent viscosity at the sub-grid interfaces is known. The recursion (4.70) can then be solved for the velocity in the remaining sub-grid layers.

The finite difference form of the sediment boundary layer equation (4.22) is

k k v k k v k k

K K

1 1

J

w S w S H H

s s Sb s s

(4.76)

where equals 1 for upwind settling and 0.5 for central difference settling. The constraint equation is

ks

k

S k S

s k

1 1

(4.77)

For noncohesive sediment transport, the sub-grid near bottom sediment concentration S1 is specified as a function of the bed stress and the bed composition. The sediment flux and primary bottom grid layer concentration, S1, must then be determined. This is accomplished by introducing a dimensionless sediment variable

1 k k s

w S J

Sb

(4.78)

Into (4.76) to give

k k 1 k k 1

(4.79)

where

k

k k v s

K w w H w

1 1

s s s k

k k v s

K w w H w

1 1 1

s s s

Since S1 is known, the first equation becomes

(4.80)



---PAGE-27---



1 2 1 1 1

(4.81)

and (4.78) now represents a closed system of ks-1 equations. The of solution of (4.79) can be written as

k k ˆk

Which is the sum of the solutions of the two simpler linear systems

k k 1 k k

###### ˆ 1 k ˆk k ˆk 1 : k 2

1 2

1

(4.82)

(4.83)

(4.84)

The solution of (4.83) can be written as

k k k k



1 1 1 1 1

k k

(4.85)

while (4.80) is solved numerically. The dimensionless form of the constraint (4.77) is

ks

1

k

1

ks

1

(4.86)

and can be written as

1 1

(4.87)

where

ks

1

k

k

s k

1

k

1: 1 : 2

k k

1

k k

1 1

k

ks

1 ˆ

k

ks k

1

(4.88)

(4.89)



---PAGE-28---



###### Reverting to the original variables gives the bed flux

1

w J S S

1

s Sb

1

(4.90)

where S1 can be interpreted as the equilibrium sediment concentration for the bottom layer of the primary vertical grid. The flux relationship (4.90) is used to determine the sediment concentration, S1 in the bottom grid layer, using

old

S S Jsb H

1 1

1

(4.91)

where is the time step for integration of the primary grid equations. The flux is then evaluated and used to determine the vertical sediment concentration distribution in the sub-grid layers using

J S S k w

k k ˆk Sb1 : 2

1

s

(4.92)

Which follows from (4.76), (4.82), and (4.85). The sediment concentration is used to determine the buoyancy distribution in the sub-grid layers.

For cohesive sediment resuspension, the bed flux is known as a function of the bed stress and geomechanical bed properties. The sediment concentration in the bottom grid layer, S1, can be determined using (4.91). The ks-1 equations (4.76) supplemented by (4.77) then form a tri-diagonal system linear system, with a zero lower diagonal, supplemented by a full last row. The system is readily solved using the Sherman-Morrison formula (Press, et al., 1992) for the vertical distribution of sediment in the boundary layer subgrid. For cohesive sediment deposition, the bed flux can be represented by

1 1

JSbd PdwsS

(4.93)

where Pd is the probability of deposition which depends on the bed stress and a critical depositional stress. Inserting (4.93) into (4.76) gives a system of ks-1 equations which must be supplement the equation formed by introducing (4.93) and (4.91) into (4.74) or

ks

k old

1 1

S k P w S k S H

s d s s k b

1 1

(4. 94)

The resulting system of linear equations is of tri-diagonal form, with a zero a zero lower diagonal, supplemented by a full first column and a full last row. The system is readily solved using the Sherman-Morrison formula (Press, et al., 1992) for the vertical distribution of sediment in the boundary layer sub-grid.



---PAGE-29---



### 4.4 Neutral Wave, Current, and Sediment Boundary Layers

Analytical solutions of the wave, current and sediment boundary layer equations (4.11, 4.16, and 4.22), as exemplified most recently by Styles and Glenn (2000), typically assume tractable forms of the vertical turbulent viscosity and diffusivity inside the wavecurrent and the current boundary layers. Closed form solutions, using special mathematical functions, are possible for the neutral case where the sediment concentrations are low enough to assume that the buoyancy is zero. An alternate approach is to extend the numerical sub-grid approach of the previous section to include a numerical solution for the wave boundary layer. with the resulting formulation being applicable to both neutral and sediment stratified conditions. The sub-grid formulation for the wave boundary layer, which is applicable to both neutral and sediment stratified conditions will be presented in the following section, while this section presents a semianalytical solution appropriate for neutral conditions.

For both the semi-analytical and sub-grid solution of the wave, current and sediment boundary layers, the turbulent viscosity and diffusion coefficients are assumed to be time invariant with (2.18) and (2.19) written in terms of the root mean square turbulent intensity

2

Av AAo q l

(4.95)

2

Kv KKo q l

(4.96)

Equations (4.26) and (4.36) used to determine the mean square turbulent intensity

- 1
- 2


2 2 2

u u B A l

z c z wm

2 1

- o A
- o K q c wm z c z wm


q

(4.97)

2 1

1 4

B K R H

u u

cos

Converting the shears in (4.97) to stresses using (4.95) gives

2 2

A A

- 1
- 2


v v z c z wm

u u B H H

2 2 1

(4.98)

q

A B A K R A A

4

A o A o K o q v v c wm z c z wm

1

u u H H

cos

Which for neutral conditions reduces to



---PAGE-30---



2 2

A A

- 1
- 2


v v z c z wm

u u H H

2 2 4/3 1

(4.99)

q B

A A

4

v v c wm z c z wm

u u H H

cos

The neutral version of the Styles and Glenn (2000) wave current boundary layer formulation defines two regions for the turbulent intensity

1/4 2 1/3 2 2

q q q B z

- 1 4 cos :0
- 2 :


wc wc cb wbm c wm cb wbm wc w

(4.100)

1

q q

2 1/3 2 1/4 1

wc c cb wc w

q q B z

q

and three regions for the length scale

l zH z z

: :

o wc

q l H z

wc w wc wc c

q q

wc

l kzH z

:

wc c

q

(4.101)

where wc is a characteristic thickness of the wave-current boundary layer relative to the water column depth. The resulting turbulent viscosity distribution is

n v

A

A q z z z H

:

o wc o wc

n v wc

A q

A q z H q

:

o wc wc wc wc c

n v wc

A q

A q kz z H q

:

o c wc c

(4.102)

with corresponding distributions for the vertical turbulent diffusivity. Rather than solving the wave boundary layer velocity distribution using special mathematical functions and then approximating these functions by series expansions, the solution proceeds by introducing an approximate velocity distribution in the lower region

(4.103)

z z z u U i t U i t z z z z

Re w1 ln exp w2 o exp : o wc

o o



---PAGE-31---



And an exact distribution in the constant viscosity central region

(4.104)

z u u U i t z

w w Re w3 exp wc exp : wc

wc

where Uw1, Uw2, and Uw3 are complex constants and

H i

2 wc

A q

o wc

Since is of order unity, the wave boundary layer scale is on the order of

A q

o wc wc

O

H

A H

2

v wc

O

2

(4.105)

(4.106)

The solution the lower region is obtained by a Galerkin procedure. Substitution of (4.103) into (4.11) gives a residual error:

(4.107)

z z z A U U E i U U i U z z H z z

w1 ln w2 o z v2 w w w

1 2

o o o

The Galerkin weighted residual errors are then set to zero

wc

z

Edz z

ln 0

z o

o

wc

z z

o

Edz z

0

z o

o

(4.108)

Expanding (4.107) and integrating the vertical stress gradient by parts gives

(4.109)

wc wc

z A z z z A i dzU i dzU z H z z z H z z

1 1 ln ln

2

v o v

w w z o z o o o

2 2 1 2 2

o o

wc

z A i dzU U z z H

wc v w z z o o z

ln ln

2

o wc



---PAGE-32---



(4.110)

2

wc wc

z z z A z z A

1 1 ln

o v o v

i dzU i dzU z z H z z z H z

w w z o o o z o o

2 1 2 2 2

o o

z z z A

o wc o v

i dzU U z z H

w z w z o o

2

o wc

Or

a U a U b a U a U b

w w

11 1 12 2 1

w w

21 1 22 2 2

(4.111)

Where

wc

z A q a i dz

1 ln

2 11

o wc

z H z z z z A q

z o

o

wc

1 ln

o o wc

a a i dz

12 21

z z H z z z A q z

z o o o

o

2

wc

o o wc

(4.112)

- a i z H z

z

- b dzU i z z


22 2

z o o

o

wc

T

wc w

wi

ln ln

1

H z z z T

z o

o

o

wc

o wc o wi w z o o

b dzU i z z H

2

o

A T U H

v wi z

z

wc

The solution is

(4.113)

wc

z

dz i U a a z a a z T U

ln ln

wc

1 1

w z o o wi

- 1 11 12 11 12
- 2 21 22 21 22


o

w w o

U a a z z z dz a a i z z H

wc

wc o z o

o

o

Or in symbolic form



---PAGE-33---



T U A U A

wi w w

- 1 11 12
- 2 21 22


h T

wi w w

U A U A

h

(4.114)

where the complex stress amplitude Twi at the interface between the lower and central regions remains to be determined as does the constant, Uw3, in the central region solution. The two constants, Twi and Uw3, must be determined such that the velocity and its vertical gradient are continuous at the interface between the two boundary layer regions by the solution of

z T A A U z z h

wc wc o wi

ln

w o o

12 22 3

z U A U A U

wc wc o w w w

ln

11 21

z z A A T A A

o o

wi

12 22 11 21 3

U U z h z

w w wc o wc wc o

(4.115)

The solution provide the interface stress in terms of the inviscid wave velocity amplitude and in turn allows Uw1 and Uw2 to be expressed in terms of the inviscid wave velocity amplitude. The maximum wave bed stress can then be determined by

wbm Aoqwc Uw1 Uw2 (4.116) Note that in the absences of currents

1/3 1 1/2

B q (4.117)

wc 21/4 wbm

With (4.116) becoming

2

2 2

U U c U

wbm w w bw w

- 1 2
- 2 2 1 2


2

U U c

w w bw

2

2

U

w

(4.118)

The solution for the current velocity is



---PAGE-34---



z u

c cb ln

A q z

o wc o

in the lower region,

z u

c cb ln wc 1

A q z

o wc wc o

(4.119)

(4.120)

in the central region, and

q z u

cb wc c

ln

A q q z z e q z e q

o wc c e

q q

c wc

e wc o

wc c wc

(4.121)

in the upper region. To enforce the integral constraint, the current profile is integrated over the three regions to give

(4.122)

wc

z

cb cb wc

dz z A q z A q z

ln ln

wc wc o o wc z o o wc o

o

(4.123)

q

wc wc

q cb wc

c

z

dz A q z

ln 1

o wc wc o

wc

2

q q q A q q q q z

- 1 1 1 ln
- 2 2


cb wc wc wc wc wc o wc c c c o

m cb wc

q z

dz A q k q z

ln

- o wc c q e q

cb wc

- o wc c e


wc wc

c

q m m A q k q z

ln 1

2

q q A q k q z q

cb wc wc wc wc

ln 1

o wc c e c

(4.124)



---PAGE-35---



###### With the general integral constraint being

(4.125)

m o ck k

m z u

1

cb wc

z A q z

ln

wc wc o o wc o

2

q q q A q q q q z

- 1 1 1 ln
- 2 2


cb wc wc wc wc wc o wc c c c o

q m m A q q z

cb wc

ln 1

o wc c e

2

q A q q

q z q

cb wc

wc ln wc wc 1

o wc c

e c

For the thickness of the wave-current layer exceeding the lower hydrodynamic grid layer. When the wave-current boundary remains inside the bottom layer of the hydrodynamic grid, (4.125) reduces to

(4.126)

q q

3 2 2

wc c wc

z q q

wc wc o cb c wc

A q u

o c c

1

z q q z z q z q

o wc wc wc wc wc wc o e c e c

ln ln ln

Introducing (4.100) into (4.126) gives

(4.127)

c u u

cb bc c c

1 1 2 2

z c

o bc

2

q q

wc wc c

z z q q

ln 1

o e c wc

2

an expression for the current stress and bottom current friction coefficient.



---PAGE-36---



- 4.5 Stratified Wave, Current, and Sediment Boundary Layers In this case, the turbulent intensity and vertical turbulent transfer coefficients become


q B1 xz yz (4.37)

2 2/3 2 2 1/2

Av Aoql xz yz l (4.38)

n 2 2 1/4

K

n o 2 2 1/4 v o xz yz

K K ql l A

o

(4.39)

The neutral version of the Styles and Glenn (2000) wave current boundary layer formulation defines two regions for the turbulent intensity

(4.39)

1/2

q q q B z

- 1 4 cos : 0
- 2 :


1/3 2 2 1

wc wc cb wbm c wm cb wbm wc w

q q

1/3 2 1/2 1

wc c cb wc w

q q B z

q

and three regions for the length scale

l z z z

: :

o wc

q l z

wc w wc wc c

q q

wc

l kz z

:

wc c

q

(4.39)

where wc is a characteristic thickness of the wave-current boundary layer. The resulting turbulent viscosity distribution is

n v o wc o wc

A A q z z z

: :

q A A q z

n wc v o wc w wc wc

q q

c

n wc v o c wc

A A q kz z

:

q

c

(4.39)

with a corresponding distributions for the vertical turbulent diffusivity. For stratified boundary layers, Styles and Glenn modify the neutral transfer coefficients using a MoninObokov length based stability function which leads to none closed form solutions of the wave, current and sediment boundary layer equations.



---PAGE-37---



K q l K R R

v Kwc wc wc

o Kwc

1

1 3

qwc

(2.19)

2

gH b l R

2 2 z wc wc qwc

q H

wc

(2.20)

(4.26)

B q B R

###### 1 4 1 cos

4 1 1 2 2 1

wc Awc Kwc qwc cb 2 wbm c wm cb wbm

and inside the current boundary layer above the wave boundary layer

A q l A R R R R R R

v Ac c c

1 1

1 1 1

o qc Ac

- 1 1
- 2 3


qc qc

K q l K R R

v Kc c c

o Kc

1

1 3

qc

(2.18)

(2.19)

2

gH b l R

2 2 z c c qc

q H

c

B q B R

4 1 1 2

c 1 1 Kc qc cb

Ac

(2.20)

(4.26)



---PAGE-38---



## 5. Sediment Bed Mass Conservation, Armoring and Consolidation (final revision 05/21/2003)

The general conservation of mass for bed sediment has the form

S B k k J k k J k k J (5.1)

t i , t SBi A , t PAi A , t 1 PAi

k

where S is the mass concentration of per total volume of a bed layer k, B is the layer thickness, JSB is the net sediment mass flux, mass per unit area and unit time, positive from the bed to the water column, A is an armoring parameter (1 for armoring, 0 otherwise), and JPA is the parent to armoring layer flux when the top or surface layer of the bed, kt, acts to simulate armoring. The superscript i denotes the ith sediment size-type class. The sediment concentration can also be defined by

i i

i F s S (5.2)

1

where F is the sediment volume fraction, s is the sediment particle density, and is the void ratio. The sediment volume fraction is defined by

1

i i i

S B S B F (5.3)

k i i i s k s k

Assuming that the sediment particles are incompressible (5.1) can be alternately expressed by

i i i i

###### F B J J J k k k k k k (5.4)

SB PA PA t t i A t i A t i

, , , 1 1

k s s s

Summing (5.4) over the sediment size classes gives

i i i SB PA PA

B J J J k k k k k k (5.5)

, , , 1 1

t t i A t i A t i k i s i s i s

The conservation of water volume in a bed layer is given by



---PAGE-39---



B

q q

t w k w k k

: :

1

i i

J J k k

i SB i SB t kt i dep i

, max ,0 min ,0

(5.6)

i s i s

k k J J k k

,

i i

t i PA i PA A kt i kt i

max ,0 min ,0 , 1

1

t i s i s

Where without the i superscript is the bulk void ratio of the bed layer, and ’s with superscripts i denote sediment class void ratios required by the mixed material consolidation formulation to be subsequently discussed. Equations (5.5) and (5.6) combine to give

B q q

t k w k w k i i

: :

J J k k

i SB i SB t kt i dep i

, 1 max ,0 1 min ,0

i s i s

i i

J J k k

(5.7)

i PA i PA A t kt i kt i

, 1 max ,0 1 min ,0

1

i s i s

i i i PA i PA kt i kt i

J J

k k 1 max ,0 1 min ,0

, 1 1

A t

i s i s

The solution procedure for the bed uses a fractional step approach. The first step involves deposition and resuspension while the second step involves pore water flow and consolidation.

###### 5. 1 Deposition, Resuspension, and Armoring

The discrete deposition and resuspension step for the sediment class i mass conservation equation (5.1) is

i * i n , t SBi A , t PAi A , t 1 PAi

S B S B k k J k k J k k J (5.8)

k k

Or

i i n i i i

*

F B F B J J J

SB PA PA t i A t i A t i

k k k k k k (5.9)

, , , 1 1 1

k k s s s

The corresponding discrete forms of (5.5), (5.6) and (5.7) are



---PAGE-40---



n i i

*

B B J J k k k k

SB PA t i A t i

, , 1 1

k k i s i s

(5.10)

i PA

J k k

, 1

A t i i s

n i i

*

- A t t kt i kt i i s s
- B B J J k k


i SB i SB t kt i dep i

, max ,0 min ,0 1 1

k k i s s i i i PA i PA

(5.11)

J J k k k k

, , 1 max ,0 min ,0

1

n k k

*

B B

i i

J J k k

i SB i SB t kt i dep i

, 1 max ,0 1 min ,0

i s s i i

J J k k

(5.12)

i PA i PA A t kt i kt i

, 1 max ,0 1 min ,0

1

i s s i i

J J k k

i PA i PA A t kt i kt i

, 1 1 max ,0 1 min ,0

1

i

s s

When the armoring option is inactive, the deposition and resuspension step operates only on the top layer of the bed with (5.8) solved for the new top layer sediment mass per unit area

i * i n i kt kt SB

S B S B J (5.13)

using a known sediment depositional or resuspension flux. If the flux in (5.13) is positive, representing resuspension, it is limited over the time step by

J J S B (5.14)

SBi min SBRi , 1 i n

kt

where the subscript SBR represents the predicted resuspension flux. Following the solution of (5.13) for each sediment class, equations (5.12) is solved for the new top layer thickness and (5.10) is solved for the new top layer void ratio.

When the noncohesive sediment armoring option is active, equation (5.8) is applied to the top two layers of the bed



---PAGE-41---



i i n i i

*

S B S B J J S B S B J

kt kt SB PA i i n i

*

kt kt PA

1 1

- (5.15a)
- (5.15b)


with the flux limiter (5.14) being applied to (5.15a) for resuspension flux from the top layer. Two options exist for determining the parent to active layer flux. One option is to require that the total mass of sediment in the surface, active layer remains constant during the deposition-resuspension step. The total parent to active layer flux is then given by (5.10) as

i i PA SB i i

J J

i s i s

(5.16)

The class fluxes can then be assigned by

i i i PA i SB i SB i kt i kt i s i s i s

###### J J J F F (5.17)

1 max ,0 min ,0

allowing (5.15) to be updated. Equation (5.10) and (5.12) are then solved for the new thicknesses and void ratios of the parent and active layer. Another option is to require that the thickness of the active layer to be time invariant during the deposition and resuspension step. Equation (5.12) reduces to

i i i PA i PA kt i kt i

J J

1 1 max ,0 1 min ,0

i s i s

(5.18)

i i i SB i SB kt i dep i

J J

1 max ,0 1 min ,0

i s s

The sediment class fluxes can be assigned by

i i i PA kt kt

J F F Q Q

1

max ,0 min ,0 1 1

i i SW i SW s kt kt

1

(5.19)

i i

J J Q

i SB i SB SW kt i dep i

1 max ,0 1 min ,0

i s s

allowing solution of equations (5.15), (5.10), and (5.12).



---PAGE-42---



###### 5. 2 Consolidation of Homogeneous Sediment Beds

This section discusses options for representing consolidation of sediment beds containing either cohesive sediment or a mixture of noncohesive sediments defined by multiple size classes. Mixed cohesive and noncohesive bed consolidation is discussed in the subsequent section. For the second, consolidation half step, the sediment mass per unit area and the sediment volume per unit area remain constant, with (5.1) and (5.5) giving

i n 1 i * k k

S B S B (5.20)

n

1 *

###### B B

1 1

k k

(5.21)

The second half step for the water volume conservation equation (5.6) is

n

1 *

B B

q q (5.22)

w k w k k k

1 1 : :

Equations (5.21) and (5.22) can be combined to give

Bk Bk qw k qw k (5.23) an equation for the layer thickness, and

n

1 *

: :

n 1 n

1 1 *

q q B

k k w k w k k

: :

(5.24)

an equation for the void ratio. The EFDC model includes four options for consolidation and pore water flow.

The first option is a constant porosity bed, with (5.24) giving

qw :k qw:k qGW (5.25)

which indicates that the pore water specific discharge is equal to a specified groundwater specific discharge at the bottom of the lowest bed layer. The second option is a simple consolidation model based on relaxation of the vertical void ratio profile to a specified profile given by

m o m exp c t to (5.26)



---PAGE-43---



where c is a consolidation rate coefficient, and m is an ultimate minimum void ratio, which can be dependent on the vertical position in the bed. Evaluating (5.26) at two successive time levels gives

n m o m exp c n to (5.27)

n 1 m o m exp c n to (5.28) Taking their ratio gives

n

1

m

* exp

c m

(5.29)

or

kn 1 m k* m exp c (5.30) Using the new void ratio given by (5.30), the new bed layer thickness is updated by (5.21). The pore water specific discharges are then given by recursively solving (5.23)

qwk qwk Bk Bk (5.31)

n

1 1 * : :

From k = 1, kt using

qw :1 qGW (5.32)

The third option for consolidation and pore water flow is based on finite strain consolidation theory. Use of this option requires the bed layers to be composed of either cohesive or noncohesive sediment, such that a single set of constitutive relationships are used over the entire thickness of the bed. The specific discharges in (5.23) or (5,24) are determined using the Darcy equation

K q u g

z w

(5.33)

where K is the hydraulic conductivity and u is the excess pore pressure defined as the difference between the total pore pressure, ut, and the hydrostatic pressure, uh.

u u t uh (5.34)

The total pore pressure is defined as the difference between the total stress and effective stress e.



---PAGE-44---



u t e (5.35) The total stress and hydrostatic pressure are given by

(5.36)

zb

1 1 1

i i b w s

p g F dz

z i

u h pb g w zb z (5.37)

where pb is the water column pressure at the bed surface zb. Solving for the excess pore pressure using (5.34) through (5.37) gives

zb

1

s w e z w

u g dz

1 1

(5.38)

where

F (5.39)

i i s s

i

is the average sediment density. The specific discharge (5.33), can alternately be expressed in terms of the effective stress

K K q

s z e

1

g

1

w w

(5.40)

or the void ratio

K K q

e s z w w

1

g

1

(5.41)

where d /d c is a coefficient of compressibility. For consistency with the Lagrangian representation of sediment mass conservation, a new vertical coordinate , defined by

d dz

1 1

(5.42)

is introduced, with (5.40) and (5.41) becoming

K K q

e s w

1 1 1

g

w w

(5.43)



---PAGE-45---



and

K K q

s w

1 1 1

w

Where is a length scale

1 e g w

(5.44)

(5.45)

The consistency of (5.43) and (5.44) at bed layer interfaces also requires consideration. The finite difference form of (5.33) in the transformed coordinate, defined by (5.42), at an interface between bed layers can be written as

K u u q

2

i k

g

1

w k k

(5.46)

below the interface and

K u u q

2

k i

1

g

1

w k k

1 1

(5.47)

above the interface, where

k 1 k Bk (5.48)

is the transformed coordinate thickness of the bed layer. Solving (5.47) for the interface excess pore pressure and inserting the results into (5.46) gives

K u u q

2 1

k k

1

g

k w k k

1/2 1

(5.49)

where

1 1 1

k k k k

1 1 1/2 1

K k K k K k

(5.50)

defines the hydraulic conductivity at the bed layer interface between layers k and k+1. The discrete from of (5.38) in the transformed coordinate is



---PAGE-46---



u u g g

s s

- 1 1
- 2 2


(5.51)

w k w k w k w k

1 1

e e

g g

w k w k

1

which after introduction into (5.49) gives

K q

- 1/2 1/2
- 2


e e

g g K

1

k k k w k w k

1/2 1 1

s

1 1

k w k

(5.52)

where

1 s 1 k s 1 k s 1

(5.53)

1 1/2 1 1

w k k k w k w k

In terms of the void ratio, (5.52) is

2

K K q (5.54)

k s k k

1/2

1 1 1

1 1/2 1 1/2 1/2

k k k k w k

where

1 e k e k

, 1 , 1/2

k

g w k k

1

(5.55)

The effective stress and hydraulic conductivity are functions of the void ratio. For cohesive material

e o

exp

eo

e eo o

exp

(5.56)

K K

###### exp o

o K

(5.57)



---PAGE-47---



are the simplest functional relationships consistent with observational data. Figures 5.1 through 5.4, based on data presented in Cargill (1985) and Palermo et al., (1998) confirm these choices. However, they show essentially two regions of behavior, below and above a void ratio of approximately 6. For noncohesive material the linear relationships

e 1 o

eo

e eo

(5.58)

K K

###### 1 o

o K

(5.59)

are appropriate. Given the unique dependence of the specific discharge on the void ratio, the void ratio form of the consolidation step, (5.24) is selected for the solution, with the thickness of the bed layers then determined by (5.23). The specific discharges at the top and bottom of layer k, follow from (5.54) and are given by

- 1

: 1 1

- 2 1


K K q

k s w k k k

: 1

1 1 2

k k k w k k

(5.60)

K K q

k s w k k k

1 1 1

k k k w k k

For the bottom layer of the bed,

qw :1 qgwi (5.61)

where qgwi is a known specific discharge due to groundwater interaction.

For the top layer of the bed, two alternate formulations are possible. The first formulation assumes that the void ratio at the water column-sediment bed interface is specifed by dep, with (5.60a) modified to

(5.62)

2

K K q

kt s w kt dep k

1 1 1

:

kt kt w kt kt

The second formulation assumes that the excess pore pressure, u, at the water columnsediment bed interface is zero with (5.46) giving



---PAGE-48---



K u q

2 wkt 1 Kt Kt w Kt

:

g

Using (5.38) the excess pore pressure at the midpoint of the top layer is

u g g

s e

- 1
- 2


w w w

Which combines with (5.63) to give

K K q

2

e s w kt

1 1 1

:

g

Kt Kt w Kt w Kt

(5.63)

(5.64)

(5.65)

Equation (5.65) can be expressed in terms of the void ratio at the new time level n+1 by expanding the effective stress at time level n+1 in a Taylor series

n 1 n n n 1 * e e e

(5.66)

Substituting (5.61) into (5.65) gives

K K q

2

n s w kt

* 1 :

1 1 1

Kt Kt Kt w Kt

n e

K

2 1

* *

g

Kt Kt w Kt

(5.67)

The numerical values of the various parameters in the expressions for the specific discharge indicate that an implicit solution of (5.24) is necessary. This is done in two stages with an intermediate void ratio, denoted by **, determined by substituting the internal specific discharges, written as

* * *

2

K K q

** : 1

k s w k k k

1

1 1 2

(5.68)

k k k w k k

1

* * *

K K q

** : 1

k s w k k k

1 1 1

k k k w k k

1

and one of the surface specific discharges corresponding to (5.62)

(5.69)

* * * *

K K q

2

** :

s w kt dep k

1 1 1

kt kt w kt kt



---PAGE-49---



###### or (5.67)

into

* * *

K K q

2

** :

s w kt

1 1 1

kt kt kt w

* *

K

2 1

e

g

kt kt w kt

(5.70)

**

1 k k 2 k w k w k

** *

q q B

: :

(5.71)

and solving the resulting tri-diagonal system of equations. The specific discharges are then exactly calculated using (5.68) and (5.69) or (5.70). The new time level thickness of the layers is determined by (5.23) with the void ratios determined from (5.24). The linearized form of this scheme is unconditionally stable.

###### 5. 3 Consolidation of Mixed Cohesive and Noncohesive Sediment Beds

This section presents a methodology for representing consolidation of sediment beds containing both cohesive and noncohesive sediments. The methodology allows for both cohesive and noncohesive sediment in any bed layer and is based on the following assumptions. First, it is assumed that during the consolidation step, a fraction of the bed pore water volume per unit horizontal area is associated with each sediment type or

B

B (5.72)

1 wc wn

where the subscripts wc and wn denote water associated with cohesive and noncohesive sediment, respectively. Likewise the volume of sediment per unit horizontal area can be fractionally partitioned between cohesive and noncohesive

B

B (5.73)

1 sc sn

Following the Lagrangian formulation of the previous section, the total volume of sediment and the fractional sediment volume in a bed layer remain constant during a consolidation step.

t B sc t B sn 0 (5.74)



---PAGE-50---



Fractional void ratios can also be defined

wc c

sc

wn n

sn

(5.75)

(5.76)

And using (5.72) and (5.73), the void ratio of the mixture is

sc c sn n

sc sn

(5.77)

Is the sediment volume weighted average of the void ratios of the two sediment types.

The second assumption is that during the consolidation time step, the fraction of water associated with noncohesive sediment remains constant, as does the fractional void ratio. This is equivalent to the assuming that the portion of the bed layer associated with noncohesive sediment is incompressible, and that the pore water associated the noncohesive sediment is specified by n.

Consistent with the preceding assumptions, the thickness of the bed layer can be divided into cohesive and noncohesive fractions, Bc and Bn, respectively.

B B B B B B

1 1

c wc sc c sc

n wn sn n sn

(5.78)

The hydraulic conductivity of the layer can be expressed by

B B K

c n c n c n

B B K K

(5.79)

Which is equivalent to an infinite number of alternating infinitesimal cohesive and noncohesive sublayers of proportional thickness comprising the mixed bed layer. Equation (5.79) can be written as

where

K

1 1 1 c 1 n

f f K K

sc sn c n

(5.80)



---PAGE-51---



sc sc

f

sc sn

sn sn

f

sc sn

(5.81)

Are the time invariant total cohesive and noncohesive sediment fractions in the bed layer. Likewise, (5.77) can be write as

f sc c fsn n (5.82)

The final assumption for the mixed material consolidation formulation is that changes in effective stress are due entirely to changes in the cohesive void ratio. Under this assumption, the specific discharge given by (5.54) can be written as

2 1

K q f f

k

1/2

sc c k sc c k k k k

1 1/2 1

K

s

1 1

k w k

1/2 1/2

(5.83)

with (5.55) becoming

1 e k e k

, 1 , 1/2

k

g w fsc c k fsc c k

1

(5.84)

The other layer interface quantities in (5.83) remain defined by (5.50) and (5.53). When the depositional void ratio is specified for the surface layer, (5.62) is modified to

(5.85)

2

K K q

kt s w kt c dep c k

1 1 1

:

kt kt w kt kt

When the zero excess pore pressure boundary condition at the bed surface is used, (5.67) becomes

K K q f

2

n s w kt sc Kt

* 1 :

1 1 1

C

Kt Kt Kt w Kt

(5.86)

n e

K

2 1

* *

f g

sc c Kt Kt w Kt

Equation (5.71) for updating the void ratio is modified using (5.82) to give



---PAGE-52---



**

1 sc c k sc c k 2 k w k w k f f q q B

** *

: :

(5.87)

Thus the mixed bed layer consolidation formulation essentially solves of the space and time evolution of fsc c with the continuum constitutive relationship for given by

1 fsc g w

(5.88)

The formulation has the desirable characteristic of reducing to the well established coheasive formulation in the absence of noncohesive material. The solution for fsc c proceeds by introducing (5.83) and (5.85) or (5.86) into (5.87) and solving the resulting tridiagonal sytem of equations. The new specific discharges are then directly calculated using (5.83) and (5.85) or (5.86) and used to update the layer thickness using (5.23)

Bk Bk qw k qw k (5.23) Equation (5.21) is then used to solve for the void ratio

n

1 *

: :

n

1 *

###### B B

1 1

k k

(5.21)

Followed by the solution of (5.82) for the cohesive void ratio

f f

sn n c

sc

(5.82)



---PAGE-53---



- 1e-03

- 1e-02

- 1e-01

- 1e+00
- 1e+01
- 1e+02


Void Ratio

| | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | |


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

1e-04

1e-03

- 1e-02






1e-04

| | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | |


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

- Figure 5.1. Specific Weight Normalized Effective Stress Versus Void Ratio.
- Figure 5.2. Compress Length Scale, g w 1 d e /d , Versus Void Ratio.


- 1e+00
- 1e+01
- 1e+02


1e-01

Void Ratio



---PAGE-54---



- 1e-05

1e-04

1e-03

1e-02

- 1e-01

Void Ratio

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

1e-06

1e-05

1e-04

1e-03

- 1e-02




1e-06

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

- Figure 5.3. Hydraulic Conductivity Versus Void Ratio.
- Figure 5.4. Hydraulic Conductivity/(1 + Void Ratio) Versus Void Ratio


Void Ratio



---PAGE-55---



## 6. Noncohesive Sediment Settling, Deposition and Resuspension

Noncohesive inorganic sediments settle as discrete particles, with hindered settling and multiphase interactions becoming important in regions of high sediment concentration near the bed. At low concentrations, the settling velocity for the jth noncohesive sediment class corresponds to the settling velocity of a discrete particle:

w sj wsoj (6.1)

Useful expressions for the discrete particle settling velocity which depends on the sediment density, effective grian diameter, and fluid kinematic viscosity, provide by van Rijn (1984b) are:

R

dj

d m w

: 100 18

10

soj

2

R m d m g d R

1 0.01 1 : 100 1000 '

dj j j dj

d m

1.1 : 1000

j

(6.2)

where

###### ' sj 1

g g

w

(6.3)

is the reduced gravitational acceleration and

d g d R

j ' j

dj

(6.4)

is a the sediment grain densimetric Reynolds number. At higher concentrations and hindering settling conditions, the settling velocity is less than the discrete velocity and can be expressed in the form

n I

S w w

i sj soj i si

1

(6.5)



---PAGE-56---



where s is the sediment particle density with values of n ranging from 2 (Cao et al., 1996) to 4 (Van Rijn, 1984). The expression (6.2) is approximated to within 5 per cent by

I

S w n w

i sj soj i si

1

(6.6)

for total sediment concentrations up to 200,000 mg/liter. For total sediment concentrations less than 25,000 mg/liter, neglect of the hindered settling correction results in less than a 5 per cent error in the settling velocity, which is well within the range of uncertainty in parameters used to estimate the discrete particle settling velocity.

Noncohesive sediment is transported as bed load and suspended load. The initiation of both modes of transport begins with erosion or resuspension of sediment from the bed when the bed stress, b, exceeds a critical stress referred to as the Shield's stress, cs. The Shield's stress depends upon the density and diameter of the sediment particles and the kinematic viscosity of the fluid and can be expressed in empirical dimensionless relationships of the form:

2 *

u

csj csj

f R g d g d

csj dj j j

' '

(6.7)

Useful numerical expressions of the relationship (6.5), provided by van Rijn (1984b), are:

2/3 1 2/3

R R R R R R R R

0.24 : 4 0.14 : 4 10 0.04 : 10 20 0.013 : 20 150 0.055 : 150

dj dj

2/3 0.64 2/3

dj dj

2/3 0.1 2/3

csj

dj dj

2/3 0.29 2/3

dj dj

2/3

R

dj

(6.8)

A number of approaches have been used to distinguish wheather a particular sediment size class is transported as bed load or suspended load under specific local flow conditions characherized by the bed stress or bed shear velocity:

u* b (6.9)

The approach proposed by van Rijn (1984a) is adopted in the EFDC model and is as follows. When the bed velocity is less than the critical shear velocity

u*csj csj g 'dj csj (6.10)



---PAGE-57---



no erosion or resuspension takes place and there is no bed load transport. Sediment in suspension under this condition will deposit to the bed as will be subsequently discussed. When the bed shear velocity exceeds the critial shear velocity but remains less than the settling velocity,

u *csj u* wsoj (6.11)

sediment will be eroded from the bed and transported as bed load. Sediment in suspension under this condition will deposit to the bed. When the bed shear velocity exceeds both the critical shear velocity and the settling velocity, bed load transport ceases and the eroded or resuspended sediment will be transported as suspended load. These various transport modes are further illustrated by reference to Figure 1, which shows dimensional forms of the settling velocity relationship (6.2) and the critical Shield's shear velocity (6.10), determined using (6.8) for sediment with a specific gravity of 2.65. For grain diameters less than approximately 1.3E-4 m (130 um) the settling velocity is less than the critical shear velocity and sediment resuspend from the bed when the bed shear velocity exceeds the critical shear velocity will be transported entirely as suspended load. For grain diameters greater than 1.3E-4 m, eroded sediment be transported by bed load in the region corresponding to (6.11) and then as suspended load when the bed shear velocity exceeds the settling velocity.

In the EFDC model, the preceding set of rules are used to determine the mode of transport of multiple size classes of noncohesive sediment. Bed load transport is determined using a general bed load transport rate formula:

q d g d

B , cs

s

(6.12)

where qB is the bed load transport rate (mass per unit time per unit width) in the direction of the near bottom horizontal flow velocity vector. The function depends on the Shield's parameter

2 *

u g d g d

b

' '

j j

(6.13)

and the critical Shield's parameter defined by (6.7) and (6.8). A number of bed load transport formulas explicitly incorporate the settling velocity. However, since both the critical Shield's parameter and the settling velocity are unique functions of the sediment grain densimetric Reynolds number, the settling velocity can also be expressed as a function of the critical Shield's parameter with (6.12) remaining an appropriate representation.

A number of bed load formulations developed for riverine prediction (Ackers and White, 1973; Laursen, 1958; Yang, 1973; Yang and Molinas, 1982) do not readily conform to



---PAGE-58---



(1) and were not incorporated as options in the EFDC model. Two widely used bed load formulations which do conform to (6.12) are the Meyer-Peter and Muller (1948) and Bagnold (1956) formulas and their derivatives (Raudkivi, 1967; Neilson, 1992; Reid and Frostick, 1994) which have the general form

, cs cs cs

(6.14)

where

cs or Rd (6.15) The Meyer-Peter and Muller formulations are typified by

3/2 cs

(6.16)

while Bagnold formulations are typified by

cs cs

(6.17)

with Bagnold's original formula having equal to zero. The Meyer-Peter and Muller formulation has been extended to heterogeneous beds by Suzuki et al. (1998), while Bagnold's formula has been similarly extended by van Niekerk et al. (1992). The bed load formulation by van Rijn (1984a) having the form

2.1

cs

0.053

1/5 2.1

Rd cs

(6.18)

has been incorporated into the CH3D-SED model and modified for heterogeneous beds by Spasojevic and Holly (1994). Equation (6.18) can be implemented in the EFDC model with an appropriately specified . A modified formulation of the Einstein bed load function (Einstein, 1950) which conforms to (6.12) and (6.14) has been presented by Rahmeyer (1999) and will be later incorporated into the EFDC model.

The procedure for coupling bed load transport with the sediment bed in the EFDC model is as follows. First, the magnitude of the bed load mass flux per unit width is calculated according to (6.12) at horizontal model cell centers, denoted by the subscript c. The cell center flux is then transformed into cell center vector components using



---PAGE-59---



u q q

- bcx bc
- bcy bc


2 2

- u v
- v


q q u v

2 2

(6.19)

where u and v are the cell center horizontal velocities near the bed. Cell face mass fluxes are determined by down wind projection of the cell center fluxes

q q q q

- bfx bcx upwind
- bfy bcy upwind


(6.20)

where the subscript upwind denotes the cell center upwind of the x normal and y normal cell faces. The net removal or accumulation rate of sediment material from the deposited bed underlying a water cell is then given by:

m m J m q m q m q m q (6.21)

x y b y bfx e y bfx w x bfy n x bfy s

where Jb is the net removal rate (gm/m2-sec) from the bed, mx and my are x and y dimensions of the cell, and the compass direction subscripts define the four cell faces. The implementation of (6.19) through (6.21) in the EFDC code includes logic to limit the out fluxes (6.20) over a time step, such that the time integrated mass flux from the bed does not exceed bed sediment available for erosion or resuspension.

Under conditions when the bed shear velocity exceeds the settling velocity and critical Shield's shear velocity, noncohesive sediment will be resuspended and transported as suspended load. When the bed shear velocity falls below both settling velocity and the critical Shield's shear velocity, suspended sediment will deposit to the bed. A consistent formulation of these processes can be developed using the concept of a near bed equilibrium sediment concentration. Under steady, uniform flow and sediment loading conditions, an equilibrium distribution of sediment in the water column tends to be established, with the resuspension and deposition fluxes canceling each other. Using a number of simplifying assumptions, the equilibrium sediment concentration distribution in the water column can be expressed analytically in terms of the near bed reference or equilibrium concentration, the settling velocity and the vertical turbulent diffusivity. For unsteady or spatially varying flow conditions, the water column sediment concentration distribution varies in space and time in response to sediment load variations, changes in hydrodynamic transport, and associated nonzero fluxes across the water column-sediment bed interface. An increase or decrease in the bed stress and the intensity of vertical turbulent mixing will result in net erosion or deposition, respectively, at a particular location or time.



---PAGE-60---



To illustrate how an appropriate suspended noncohesive sediment bed flux boundary condition can be established, consider the approximation to the sediment transport equation (3.1) for nearly uniform horizontal conditions

K HS S w S H

v t z z s

(6.22)

Integrating (6.22) over the depth of the bottom hydrodynamic model layer gives

t HS J0 J (6.23)

where the over bar denotes the mean over the dimensionless layer thickness, . Subtracting (6.23) from (6.22) gives

K J J HS S w S

v 0 t z z s

H

(6.24)

Assuming that the rate of change of the deviation of the sediment concentration from the mean is small

t HS t HS (6.25)

allows (6.24) to be approximated by

K J J

v 0 z z s

S w S H

(6.26)

- Integrating (6.26) once gives


K z

v

S w S J J J H

z s

0 0

Very near the bed, (6.27) can be approximated by

(6.27)

K

v

S w S J H

z s

0

(6.28)

Neglecting stratification effects and using the results of Chapter 4, the near bed diffusivity is approximately

K l

v

K q u z H H

o

*

(6.29)



---PAGE-61---



Introducing (6.29) into (6.28) gives

where

R R J S S

o z

z z w

s

ws

R

u

*

(6.30)

(6.31)

is the Rouse parameter. The solution of (6.30) is

J C S

o

R s

w z

(6.32)

The constant of integration is evaluated using

S Seq : z zeq and Jo 0 (6.33)

which sets the near bed sediment concentration to an equilibrium value, defined just above the bed under no net flux condition. Using (6.33), equation (6.32) becomes

R eq o eq

z J S S

z w

s

(6.34)

For nonequilibrium conditions, the net flux is given by evaluating (6.34) at the equilibrium level

J o ws Seq Sne (6.35)

where Sne is the actual concentration at the reference equilibrium level. Equation (6.35) clearly indicates that when the near bed sediment concentration is less than the equilibrium value a net flux from the bed into the water column occurs. Likewise when the concentration exceeds equilibrium, a net flux to the bed occurs.

For the relationship (6.35) to be useful in a numerical model, the bed flux must be expressed in terms of the model layer mean concentration. For a three-dimensional application, (6.34) can be integrated over the bottom model layer to give

Jo ws Seq S (6.36)

where



---PAGE-62---



1

z S S R

ln

eq

: 1 1

eq eq eq

1

z z

R eq

1 1

1

S S R R z

: 1 1 1

eq eq eq

1

(6.37)

defines an equivalent layer mean equilibrium concentration in terms of the near bed equilibrium concentration. The corresponding quantities in the numerical solution bottom boundary condition (3.6) are

w S w S P w w

r r s eq

d s s

(6.38)

If the dimensionless equilibrium elevation, zeq exceeds the dimensionless layer thickness,

- (6.19) can be modified to


1

M z S S R

ln

eq eq eq eq

: 1 1

1

M z M z

R eq eq eq

1 1

1

S S R R M z

: 1 1 1

1

eq

(6.39)

where the over bars in (6.36) and (6.38) implying an average of the first M layers above the bed.

For two-dimensional, depth averaged model application, a number of additional considerations are necessary. For depth average modeling, the equivalent of (6.27) is

K

v z s o 1

S w S J z H

(6.40)

Neglecting stratification effects and using the results of Chapter 4, the diffusivity is

K l

v o * 1

K q u z z H H

Introducing (6.41) into (6.40) gives

1 1 1

R R z J S S

o z

z z z w

s

(6.41)

(6.42)



---PAGE-63---



A close form solution of (6.42) is possible for equal to zero. Although the resulting diffusivity is not as reasonable as the choice of equal to one, the resulting vertical distribution of sediment is much more sensitive to the near bed diffusivity distribution than the distribution in the upper portions of the water column. For equal to zero, the solution of (6.42) is

Rz J C S

o

1

R s

R w z

1

(6.43)

Evaluating the constant of integration using (6.43) gives

R eq o eq

z Rz J S S

1

z R w

1

s

(6.44)

For nonequilibrium conditions, the net flux is given by evaluating (6.44) at the equilibrium level

1 o s 1 1 eq eq ne R

J w S S R z

(6.45)

where Sne is the actual concentration at the reference equilibrium level. Since zeq is on the order of the sediment grain diameter divided by the depth of the water column, (6.45) is essentially equivalent (6.35). To obtain an expression for the bed flux in terms of the depth average sediment concentration, (6.44) is integrated over the depth to give

2 1 o s 2 1 eq eq R

J w S S R z

(6.46)

where

1

z S S R

ln

eq eq eq eq

: 1

1

z z

1 1

R eq

1

S S R R z

: 1 1 1

eq eq eq

1

(6.47)

The corresponding quantities in the numerical solution bottom boundary condition (3.6) are



---PAGE-64---



R w S w S R z

2 1 2 1

r r s eq eq

R P w w R z

2 1 2 1

d s s eq

(6.48)

When multiple sediment size classes are simulated, the equilibrium concentrations given by (6.37), (6.39), and (6.47) are adjusted by multiplying by their respective sediment volume fractions in the surface layer of the bed.

The specification of the water column-bed flux of noncohesive sediment has been reduced to specification of the near bed equilibrium concentration and its corresponding reference distance above the bed. Garcia and Parker (1991) evaluated seven relationships, derived by combinations of analysis and experiment correlation, for determining the near bed equilibrium concentration as well as proposing a new relationship. All of the relationships essential specify the equilibrium concentration in terms of hydrodynamic and sediment physical parameters

Seq Seq d, s, w,ws,u *, (6.49)

including the sediment particle diameter, the sediment and water densities, the sediment settling velocity, the bed shear velocity, and the kinematic molecular viscosity of water. Garcia and Parker concluded that the representations of Smith and McLean (1977) and Van Rijn (1984b) as well as their own proposed representation perform acceptably when tested against experimental and field observations.

Smith and McLean's formula for the equilibrium concentration is

T S

- 0.65
- 1


o eq s

T

o

(6.50)

where o is a constant equal to 2.4E-3 and T is given by

2 2 * * 2 *

u u T

b cs cs

u

cs cs

(6.51)

where b is the bed stress and cs is the critical Shields stress. The use of Smith and McLean's formulation requires that the critical Shields stress be specified for each sediment size class. Van Rijn's formula is

d S T R z

3/2 1/5

eq 0.015 s * d

eq

(6.52)



---PAGE-65---



where zeq* ( = Hzeq ) is the dimensional reference height and Rd is a sediment grain Reynolds number. When Van Rijn's formula is select for use in EFDC, the critical Shields stress in internally calculated using relationships from Van Rijn (1984b). Van Rijn suggested setting the dimensional reference height to three grain diameters. In the EFDC model, the user specifies the reference height as a multiple of the largest noncohesive sediment size class diameter.

Garcia and Parker's general formula for multiple sediment size classes is

5

A Z S

j jeq s

1 3.33 5

A Z

(6.53)

u Z R F w

* 3/5 j dj H sj

(6.54)

1/5

d F

j H

d

50

1 o 1

o

(6.55)

(6.56)

- where A is a constant equal to 1.3E-7, d50 is the median grain diameter based on all sediment classes, is a straining factor, FH is a hiding factor and is the standard deviation of the sedimentological phi scale of sediment size distribution. Garcia and Parker's formulation is unique in that it can account for armoring effects when multiple sediment classes are simulated. For simulation of a single noncohesive size class, the straining factor and the hiding factor are set to one. The EFDC model has the option to simulate armoring with Garcia and Parker's formulation. For armoring simulation, the current surface layer of the sediment bed is restricted to a thickness equal to the dimensional reference height.


## 7. Cohesive Sediment Settling, Deposition and Resuspension

The settling of cohesive inorganic sediment and organic particulate material is an extremely complex process. Inherent in the process of gravitational settling is the process of flocculation, where individual cohesive sediment particles and particulate organic particles aggregate to form larger groupings or flocs having settling characteristics significantly different from those of the component particles (Burban et al., 1989,1990; Gibbs, 1985; Mehta et al., 1989). Floc formation is dependent upon the type and concentration of the suspended material, the ionic characteristics of the environment, and the fluid shear and turbulence intensity of the flow environment. Progress has been made in first principles mathematical modeling of floc formation or aggregation, and



---PAGE-66---



disaggregation by intense flow shear (Lick and Lick, 1988; Tsai, et al., 1987). However, the computational intensity of such approaches precludes direct simulation of flocculation in operational cohesive sediment transport models for the immediate future.

An alternative approach, which has met with reasonable success, is the parameterization of the settling velocity of flocs in terms of cohesive and organic material fundamental particle size, d; concentration, S; and flow characteristics such as vertical shear of the horizontal velocity, du/dz, shear stress, Avdu/dz, or turbulence intensity in the water column or near the sediment bed, q. This has allowed semi-empirical expressions having the functional form

du W W d S q dz

se se , , ,

(7.1)

to be developed to represent the effective settling velocity. A widely used empirical expression, first incorporated into a numerical by Ariathurai and Krone (1976), relates the effective settling velocity to the sediment concentration:

a

S w w

s so

S

o

(7.2)

with the o superscript denoting reference values. Depending upon the reference concentration and the value of , this equation predicts either increasing or decreasing settling velocity as the sediment concentration increases. Equation (7.2) with user defined base settling velocity, concentration and exponent is an option in the EFDC model. Hwang and Metha (1989) proposed

n s m

aS w

2 2

S b

(7.3)

based on observations of settling at six sites in Lake Okeechobee. This equation has a general parabolic shape with the settling velocity decreasing with decreasing concentration at low concentrations and decreasing with increasing concentration at high concentration. A least squares for the paramters, a, m, and n, in (7.3) was shown to agree well with observational data. Equation (7.3) does not hav a dependence on flow characteristics, but is based on data from an energetic field condition having both currents and high frequency surface waves. A generalized form of (7.3) can be selected as an option in the EFDC model.

Ziegler and Nisbet, (1994, 1995) proposed a formulation to express the effective settling as a function of the floc diameter, df

ws adf (7.4)

b



---PAGE-67---



###### with the floc diameter given by:

1/2

f f

d

2 2

S

xz xz

(7.5)

where S is the sediment concentration, f is an experimentally determined constant and

xz and yz are the x and y components of the turbulent shear stresses at a given position in the water column. Other quantities in (7.4) have been experimentally determined to fit the relationships:

0.85 2 2

a B1 S xz xz

(7.6)

b 0.8 0.5log S xz xz B2 (7.7)

2 2

- where B1 and B2 are experimental constants. This formulation is also an option in the EFDC model.


A final settling option in EFDC is based on that proposed by Shrestha and Orlob (1996). The formulation in EFDC has the form

exp 4.21 0.147 0.11 0.039 ws S G G

(7.8)

where

2 2

G zu zv

(7.9)

is the magnitude of the vertical shear of the horizontal velocity. It is noted that all of these formulations are based on specific dimensional units for input parameters and predicted settling velocities and that appropriate unit conversion are made internally in their implementation in the EFDC model.

Water column-sediment bed exchange of cohesive sediments and organic solids is controlled by the near bed flow environment and the geomechanics of the deposited bed. Net deposition to the bed occurs as the flow-induced bed surface stress decreases. The most widely used expression for the depositional flux is:



---PAGE-68---



cd b s d s d d b cd cd

w S w T S J

:

d o

0 :

b cd

(7.10)

where b is the stress exerted by the flow on the bed, cd is a critical stress for deposition which depends on sediment material and floc physiochemical properties (Mehta et al., 1989) and Sd is the near bed depositing sediment concentration. The critical deposition stress is generally determined from laboratory or in situ field observations and values ranging form 0.06 to 1.1 N/m**2 have been reported in the literature. Given this wide range of reported values, in the absence of site specific data the depositional stress and is generally treated as a calibration parameter. The depositional stress is an input parameter in the EFDC model.

Since the near bed depositing sediment concentration in (7.10) is not directly calculated, the procedures of Chapter 5 can be applied to relate the the near bed depositional concentration to the bottom layer or depth averge concentration. Using (6.14) the near bed concentration during times of deposition can be determined in terms of the bottom layer concentration for three-dimensional model applications. Inserting (7.10) into (6.14) and evaluating the constant at a near bed depositional level gives

R d

z S T T S z

1

d d R d

(7.11)

- Integrating (7.11) over the bottom layer gives


1 1

z S T T S R z

ln

d d d d d

1 : 1 1

1

1 1 1

R eq d d d

z S T T S R R z

1

1 : 1 1 1

1

d

(7.12)

The corresponding quantities in the numerical solution bottom boundary condition (3.6) are



---PAGE-69---



1 1

z P w T T w R z

ln

d d s d d s d

1 : 1 1

1

1 1 1

R eq

z P w T T w R R z

1

1 : 1 1 1

d s d d s d

1

(7.13)

For depth averaged model application, (7.10) is combined with (6.25) and the constant of integration is evaluated at a near bed depositional level to give

R d d

Rz Rz z S T S T S

1 1 1 1 1

d d d d R

R R z

(7.14)

Integrating (7.14) over the depth gives

1 1

R z z R z S T T S R R z R

2 1 ln 1 1

d d d d d d d

1 : 1 2 1 1 1

1

(7.15)

1 1

R d d d d d d d

R z z Rz S T T S R

2 1 1

1 1 : 1 2 1 1 1 1

1

R R z R

The corresponding quantities in the numerical solution bottom boundary condition (3.6) are

1 1

R z z R z

2 1 ln 1 1

d d d d s d d s d

P w T T w R R z R

1 : 1 2 1 1 1

1

(7.16)

1 1

R d d d d s d d s d

R z z Rz P w T T w R

2 1 1

1 1 : 1 2 1 1 1 1

1

R R z R

It is noted that the assumptions used to arrive at the relationships, (7.12) and (7.15) are more teneous for cohesive sediment than the similar relationships for noncohesive sediment. The settling velocity for cohesive sediment is highly concentration dependent and the use of a constant settling velocity to arrive at (7.12) and (7.15) is questionable. The specification of an appropriate reference level for cohesive sediment is difficult. One possibility is to relate the reference level to the floc diameter using (7.5). An alternative is to set the reference level to a laminar sublayer thickness



---PAGE-70---



S z

d

Hu

*

(7.17)

where (S) is a sediment concentration dependent kinematic viscosity and the water depth is include to nondimensionlize the reference level. A number of investigators, including Mehta and Jiang (1990) have presented experimental results indicating that at high sediment concentrations, cohesive sediment-water mixtures behave as high viscosity fluids. Mehta and Jain's results indicate that a sediment concentration of 10,000 mg/L results in a viscosity ten time that of pure water and that the viscosity increases logrithmically with increasing mixture density. Use of the relationships (7.12) and (7.16) is optional in the EFDC model. When they are used, the reference height is set using

- (7.17) with the viscosity determined using Mehta and Jain's experimental relationship between viscosity and sediment concentration. To more fully address the deposition prediction problem, a nested sediment, current and wave boundary layer model based on the near bed closure presented in Chapter 4 is under development.


Cohesive bed erosion occurs in two distinct modes, mass erosion and surface erosion. Mass erosion occurs rapidly when the bed stress exerted by the flow exceeds the depth varying shear strength, s, of the bed at a depth, Hme, below the bed surface. Surface erosion occurs gradually when the flow-exerted bed stress is less than the bed shear strength near the surface but greater than a critical erosion or resuspension stress, ce, which is dependent on the shear strength and density of the bed. A typical scenario under conditions of accelerating flow and increasing bed stress would involve first the occurrence of gradual surface erosion, followed by a rapid interval of mass erosion, followed by another interval of surface erosion. Alternately, if the bed is well consolidated with a sufficiently high shear strength profile, only gradual surface erosion would occur. Transport into the water column by mass or bulk erosion can be expressed in the form

m J w S

r me s b o r r

T

me

(7.18)

where Jo is the erosion flux, the product wrSr represents the numerical boundary condition (3.6), mme is the dry sediment mass per unit area of the bed having a shear strength, s, less than the flow-induced bed stress, b, and Tme is a somewhat arbitrary time scale for the bulk mass transfer. The time scale can be taken as the numerical model integration time step (Shrestha and Orlob, 1996). Observations by Hwang and Mehta (1989) have indicated that the maximum rate of mass erosion is on the order of 0.6 gm/sm**2 which provides an means of estimating the transfer time scale in (4.10). The shear strenght of the cohesive sediment bed is generally agreed to be a linear function of the bed bulk density (Metha et al., 1982; Villaret and Paulic, 1986; Hwang and Mehta, 1989)

s as b bs (7.19)



---PAGE-71---



For the shear strength in N/m**2 and the bulk density in gm/cm**3, Hwang and Mehta (1989) give as and bs values of 9.808 and -9.934 for bulk density greater than 1.065 gm/cm**3. The EFDC model currently implements Hwang and Mehta's relationship, but can be readily modified to incorporated other functional relationships.

Surface erosion is generally represented by relationships of the form

dm J w S

or r r e b ce : b ce

dt

ce

(7.20)

or

dm J w S

or r r e exp b ce : b ce

dt

ce

(7.21)

where dme/dt is the surface erosion rate per unit surface area of the bed and ce is the critical stress for surface erosion or resuspension. The critical erosion rate and stress and the parameters , , and are generally determined from laboratory or in situ field experimental observations. Equation (7.20) is more appropriate for consolidated beds, while (7.21) is appropriate for soft partially consolidated beds. The base erosion rate and the critical stress for erosion depend upon the type of sediment, the bed water content, total salt content, ionic species in the water, pH and temperature (Mehta, et al., 1989) and can be measured in laboratory and sea bed flumes.

The critical erosion stress is related to but generally less than the shear strength of the bed, which in turn depends upon the sediment type and the state of consolidation of the bed. Experimentally determined relationships between the critical surface erosion stress and the dry density of the bed of the form

ce c s (7.22)

d

have been presented (Mehta, et al., 1989). Hwang and Mehta (1989) proposed the relationship

ce a b l c (7.23)

b

between the critical surface erosion stress and the bed bulk density with a, b, c, and l equal to 0.883, 0.2, 0.05, and 1.065, respectively for the stress in N/m**2 and the bulk density in gm/cm**3. Considering the relationship between dry and bulk density

b w d s

s w

(7.24)



---PAGE-72---



equations (7.22) and (7.23) are consistent. The EFDC model allow for a user defined constant critial stress for surface erosion or the use of (7.23). Alternate predictive expression can be readily incorporated into the model.

Surface erosion rates ranging from 0.005 to 0.1 gm/s-m**2 have been reported in the literature, and it is generally accepted that the surface erosion rate decreases with increasing bulk density. Based on experimental observations, Hwang and Mehta (1989) proposed the relationship

dm dt

0.198 log 0.23exp

e

10

1.0023

b

(7.25)

for the erosion rate in mg/hr-cm**2 and the bulk density in gm/cm**3. The EFDC model allow for a user defined constant surface erosion rate or predicts the rate using (7.25). Alternate predictive expression can be readily incorporated into the model. The use of bulk density functions to predict bed strength and erosion rates in turn requires the prediction of time and depth in bed variations in bulk density which is related to the water and sediment density and the bed void ratio by

1 b 1 w 1 s

(7.26)

Selection of the bulk density dependent formulations in the EFDC model requires implmentation of a bed consolidation simulation to predict the bed void ratio as discussed in the following chapter.

## 7. Sediment Bed Geomechanical Processes

This chapter describes the representation of the sediment bed in the EFDC model. To make the information presented self contained, the derivation of mass balance equations and comparison with formulations used in other models is also presented.

Consider a sediment bed represented by discrete layers of thickness Bk, which may be time varying. The conservation of sediment and water mass per unit horizontal area in layer k is given by:

B

s k t s k s k b sb k

J J k k J

: : , 1

(7.1)

B

w k k w t w k w k b k sb b sb k s

J J k k J J

: : , max ,0 min ,0 1

(7.2)



---PAGE-73---



where is the void ratio, s and w are the sediment and water density and Js and Jw are the sediment and water mass fluxes with k- and k+ defining the bottom and top boundaries, respectively of layer k. The mass fluxes are defined as positive in the vertical direction and exclude fluxes associated with sediment depostion and erosion. The last term in equation (7.1) represents erosion and deposition of sediment at the top of the upper most bed layer, k=kb, where

k k k k

1: ,

b b

k k

0:

b

(7.3)

Consitent with this partitioning of flux,

Js :k 0:k kb (7.4)

The last term in (7.2) represents the corresponding entrainment of bed water into the water column during sediment erosion and entrainment of water column water into the bed during deposition. The water flux, Jw:k+, at the top of the upper most layer, kb, is not necessarily zero, since it can include ambient seepage and pore water explusion due to bed consolidation.

Assuming sediment and water to be incompressible, (7.1) and (7.2) can be written as:

B J J J k k

1

k sb t s k s k b

, 1

: :

k s s

(7.5)

(7.6)

B J J q q k k

k k sb sb t w k w k b k b

: : , max ,0 min ,0 1

k s s

where the water specfic discharges

J q J q

w k w w k

: :

w k w w k

: :

(7.7)

have been introduced into (7.6). Four approaches for the solution of the mass conservation equations (7.5) and (7.6) have been previously utilized. The solution approaches, hereafter referred to as solution levels, increase in complexity and physical realism and will be briefly summarized.

The first level or simplest approach assumes specified time-constant layer thicknesses and void ratios with the left sides of (7.5) and (7.6) being identically zero. Sediment mass flux at all layer interfaces are then identical to the net flux from the bed to the water column.



---PAGE-74---



J J k k

: 1, 0:

s k sb b

:

k k J

b s k

:

J k k

:

sb b

(7.8)

Bed representations at this level, as exemplified by the RECOVERY model (Boyer, et al., 1994), typically omit the water mass conservation equations. However, it is noted that the water mass conservation is ill posed unless either q1-, the specific discharge at the bottom of the deepest layer or qkb+, the specific discharge at the top of the water column adjacent layer, is specified. If q1- is set to zero, qka+ is then required to exactly cancel the entrainment terms is (7.6).

The second level of bed mass conservation representation assumes specified time invariant layer thicknesses. The mass conservation equations (7.5) and (7.6) become

J B J J k k

1 1

sb k t s k s k b

, 1

: :

k s s

(7.9)

(7.10)

J J B q q k k

k sb sb k t w k w k b k b

: : , max ,0 min ,0 1

k s s

This system of 2 x kb equations includes kb unknow void ratios, kb unknow internal sediment fluxes, and kb+1 unknow specific discharges and is under determined unless additional information is specified. The constant bed layer thickness option in the WASP5 model (Ambrose, et al., 1993) uses specifed burial velocities to define the internal sediment fluxes

J w S J w S

s k b k k

: :

s k b k k

: : 1

w w

b k b k

: : 1

(7.11)

s k

S

1

k

(7.12)

where wb is the burial velocity and S is the sediment concentration (mass per unit total volume). Use of the burial velocity eliminates the indetermincy in (7.9) and allowing its solution for the void ratio. In the event that the sediment concentration in the upper most layer becomes negative, the layer is eliminated and the underlying layer become water column adjacent. The left side of the water mass conservation equations (7.10) is now know and the equation is more appropriately written as



---PAGE-75---



(7.13)

J J q q B k k

k sb sb w k w k k t b k b

: : , max ,0 min ,0 1

k s s

The determination of the specific discharges using (7.13) can be viewed is either under determined or physically inconsistent. As shown for the first level approach, the solution of (7.13) is ill posed unless either q1-, the specific discharge at the bottom of the deepest layer or qkb+, the specific discharge at the top of the upper most layer is independently specified. If q1- is specified and the internal specific discharges are determined from (7.13), qka+ is then required to partially cancel the entrainment terms in (7.13). As will be subsequently shown, the specific discharges can be dynamically determined using Darcy's law. However, the specific discharges determined using Darcy's law and the known void ratios are not guaranteed to satisfy (7.13) the level two formulation is dynamically inconsistent with respect to water mass conservation in the sediment bed. The constant bed layer thickness option in the WASP5 ignores this problem entirely by not considering the water mass balance and hence neglecting pore water advection of dissolved contaminants.

The third level of bed mass conservation representation assumes specified time invariant layer void ratios. The mass conservation equations (7.5) and (7.6) become

J B J J k k

1 1

sb t k s k s k b k s s

, 1

: :

(7.14)

(7.15)

J J B q q k k

k sb sb t k w k w k b k b k s s

: : , max ,0 min ,0 1

This system of equations exhibits the same under determined nature as (7.9) and (7.10). Specification of internal sediment fluxes or burial velocities allows (7.14) to be solved for the layer thicknesses. Solution of (7.15) for the specific discharges then requires the specification either q1-, the specific discharge at the bottom of the deepest layer or qkb+, the specific discharge at the top of the upper most layer. The variable bed layer thickness option in the WASP5 model (Ambrose, et al., 1993) exemplifies the third level of bed representation. Specifically, the thickness of the water column adjacent layer is allowed to vary in time, while the thicknesses of the underlying layers remain constant. A periodic time variation is specified for the bottom sediment flux in the upper most layer

J t t t N t

0 : 1

- s kb o o
- t N t


:

o

J J dt t N t t t N t

: 1

s kb sb o o t

:

o

(7.16)

where t is the standard water time step and N t is the sediment compaction time. This results in the thickness of the upper most layer periodically returning to its initial value at



---PAGE-76---



time intervals of N t unless the thickness becomes negative due to net resuspension. In that event, the underlying layer becomes the water column adjacent layer. The water mass conservation (7.15) for all but the upper most layer becomes

qk qk q 1 : k kb (7.17)

indicating that all internal specific discharges are equal a specified specific discharge at the bottom of layer 1. Given the solution for the time variation of the water column adjacent thickness and bottom specific discharge, (7.15) can be solved for the specific discharge at the top of the layer. The constant porosity bed option in EFDC is also a level three approach. In EFDC, the internal sediment fluxes are set to zero and the change in thickness of the water column adjacent layer is determined directly using (7.14) while the underlying layers have time invariant thicknesses. As a result, the internal water specific discharges are set to zero and the water entrainment and expulsion in the water column adjacent layer are determined directly from (7.15). The EFDC model is configured to have a user specified maximum number of sediment bed layer. A the start of a simulation, the number of layers containing sediment at a specific horizontal location is specified. Under continued deposition, a new water column layer is created when the thickness of the current layer exceeds a user specified value. If the current water column adjacent layer's index is equal to the maximam number of layers, the bottom two layers are combined and the remaining layers renumbered before addition of the new layer. Under continued resuspension, the layer underlying the current water column adjacent layer becomes the new adjacent layer when all sediment is resuspended form the current layer.

The fourth level of bed representation accounts for bed consolidation by allowing the layer void ratios and thicknesses to vary in time. The simplest and most elegant formulations at this level utilize a Lagrangian approach for sediment mass conservation. The Lagrangian approach requires that the sediment mass per unit horizontal area in all layers, except the upper most, be time invariant and without loss of generality, the internal sediment fluxes can be set to zero. Consistent with these requirements (7.5) becomes

B J k k

k sb t b

, 1

k s

(7.18)

Expanding the left side of the water conservation equation (7.6), and using (7.18) gives

(7.19)

B J q q k k

k sb t k w k w k b k b k s

: : , min ,0 1

The Lagrangian approach for sediment mass conservation also requires that the number of bed layers vary in time. Under conditions of continued deposition, a new water column adjacent layer would be added when either the thickness, void ratio or mass per unit area of the current water column adjacent layer reaches a predefined value. Under



---PAGE-77---



conditions of continued resuspension, the bed layer immediately under the current water column adjacent layer would become the new water column adjacent layer when the entire sediment mass of the current layer has been resuspended.

At the fourth and most realistic level of bed representation, three approaches can be used to represent bed consolidation. Two of the approaches are semi-empirical with the first assuming that the void ratio of a layer decreases with time. A typical relationship which is used for the simple consolidation option in the EFDC model is

m o m exp t to (7.20)

where o is the void ratio at the mean time of deposition, to, m is the ultimate minimum void ratio corresponding to complete consolidation, and is an empirical or experimental constant. Use of (7.20) in the EFDC model involves specifying the depositional void ratio, the ultimate void ratios and the rate constants. The ultimate void ratio can be specified as a function depth below the water column-bed interface. The actual calculation involves using the initial void ratios to determine the deposition time to, after which (7.20) is used to update the void ratios as the simulation progresses. After equation (7.20) is used to calculate the new time level void ratios, equation (7.18) provides the new layer thicknesses. The water conservation equations (7.19) can then be solved using

(7.21)

B J q q k k

k sb w k w k t k b k b

: : , min ,0 1

k s

to determine the water specific discharges, provided that the specific discharge q1-, at the bottom of layer 1 is specified. When this option is specified in the EFDC model, the specific discharge at bottom of the bottom sediment layer is set to zero. Layers are added and deleted in the manner previously described for EFDC's constant porosity option. The SED2D-WES model (Letter et al., 1998) utilizes a similar approach based on a specified time variation of bulk density

s w

b bm bo bm t to

exp 1

(7.22)

which in turn defines the variation in void ratio.

The second semi-empirical approach assumes that the vertical distribution of the bed bulk density or equivalently the, void ratio at any time is given by a self-similar function of vertical position, bed thickness and fixed surface and bottom bulk densities or void ratios. Functionally this equivalent to

V z,BT, kb, 1 (7.23)



---PAGE-78---



where V represents the function, z is a vertical coordinate measured upward from the bottom of the lowest layer, and BT is the total thickness of the bed. This approach is used in the original HSTM model (Hayter and Mehta, 1983), the new HSCTM model (Hayter et al., 1998) and is an option in the CE-QUAL-ICM/TOXI model (Dortch, et al., 1998). The determination of the new time level layer thicknesses and void ratios requires an iterative solution of equations (7.18) and (7.23). The solution is completed using (7.21) to determine the water specific discharges.

The third and most realistic approach is to dynamically simulate the consolidation of the bed. In the Lagrangian formulation, (7.18) is directly solved for the equivalent sediment thickness

B (7.24)

k k

1

k

and the water conservation equation (7.19) is integrated to determine the void ratio.

J q q k k

k t k w k: w k: , b k b min sb ,0

s

(7.25)

The specific discharges in (7.25) are determined using the Darcy equation

K q u g

z w

(7.26)

where K is the hydraulic conductivity and u is the excess pore pressure defined as the difference between the total pore pressure ut, and the hydrostatic pressure uh.

u u t uh (7.27)

The total pore pressure is defined as the difference between the total stress and effective stress e.

u t e (7.28) The total stress and hydrostatic pressure are given by

zb b w s z

1 1 1

p g dz

(7.29)

u h pb g w zb z (7.30)



---PAGE-79---



where pb is the water column pressure at the bed zb. Solving for the excess pore pressure using (7.27) through (7.30) gives

zb s

1 1

u g dz

w e w z

1

(7.31)

The specific discharge (7.26), can alternately be expressed in terms of the effective stress

zb s z e z w w z

K q K dz g

1 1

1

(7.32)

or the void ratio

zb e s

K d q K dz g d

1 1

z z w w z

1

(7.33)

where d /d c is a coefficient of compressibility. For consistency with the Lagrangian representation of sediment mass conservation, a new vertical coordinate , defined by

d dz

1 1

(7.34)

is introduced. The discrete form of (7.34) is

z z B (7.35)

k k k k k k k k

1 1

where D is the equivalent sediment thickness previously defined by (7.24). Introducing (7.34) into (7.26), (7.32), and (7.33) gives

K q u g

w 1 z

(7.36)

K K q

s e

1 1 1

g

w w

K K q

s

1 1 1

w

(7.37)

(7.38)



---PAGE-80---



where

d g d

1 e

w

(7.39)

is a compressibility length.

Three formulations for the solution the consolidation problem can be utilized. The void ratio-excess pore pressure formulation, used in the EFDC model, evaluates the specific discharges at the current time level n, using (7.36) and explicitly integrates (7.25)

(7.40)

n

J q q k k

n n sb k k n w k w k b k b

1

: : , min ,0

k s

where is the time step, to give the new time level void ratios. The layer thicknesses are then determined by explicit integration of (7.18).

n n

1

B B J k k J

sb b

, 1 1

k k s

n n sb k k b

1

k k

,

s

(7.41)

Constitutive equations required for consolidation prediction generally express the effective stress and hydraulic conductivity as functions of the void ratio. Thus the new time level void ratio is used to determine new time level values of the effective stress and hydraulic conductivity. The new time level excess pore pressures is then given by

w s 1 b e

u g

w

(7.42)

the transformed equivalent of (7.31). The primary advantage of the void ratio-excess pore pressure formulation is the simplicity of its boundary conditions

u ub : b (7.43)

u u

: 0

o

or q q

: 0

o

(7.44)

The water column-sediment bed interface boundary condition generally sets ub to zero if the surface water flow is hydrostatic but can incorporate wave induced pore pressures. The bottom boundary conditions allows either the specification of pressure or specific



---PAGE-81---



discharge. The primary disadvantage of this formulation is the stability or positivity criterion imposed on the time step

(7.40)

n n k k

n sb

J q q k k

: : , min ,0

w k w k b b k

s

n k

J k k

sb b

, max ,0

s

(7.41)

In practice, these criteria are readily satisfied if the consolidation time step is identical to the time step of the hydrodynamic model. In the event that these criteria are not met using the hydrodynamic time step, the bed consolidation is sub-cycled using an integer number of time steps, meeting (7.40) and (7.41), per each hydrodynamic time step.

Alternately, the consolidation problem can be directly formulated in terms of the effective stress or void ratio. Combining (7.25) and (7.37) using (7.39) gives the effective stress formulation

K K

s k t k

1 1 1

(7.42)

w k

K K J k k

s sb b k b

1 , min ,0 1 1

w k s

The continuum equivalent is

K K g

1

t e k e s w

:

1 1

(7.43)

J g

sb w b k b

min ,0

s

which is parabolic since is negative. Combining (7.25) and (7.38) using (7.39) gives the void ration formulation

###### K K

s k t k

1 1 1

(7.44)

w k

K K J k k

s sb b k b

1 , min ,0 1 1

w k s



---PAGE-82---



The continuum equivalent is

K K J (7.45)

s sb t k b k b

1 min ,0 1 1

w s

Equation (7.45) is the discrete form of the finite strain consolidation equation first derived by Gibson et al. (1967). Equation (7.45) was used by Cargill (1985) in the formulation of a model for dredge material consolidation and by Le Normant (1998) to represent bed consolidation in a three-dimensional cohesive sediment transport model.

The classic linear consolidation equation (Middleton and Wilcock, 1994) omits the second term associated with self weight in (7.45) and introduces a constant consolidation coefficient

K C

c 1 e

e g

w

(7.46)

reducing (7.45) to

t Cc zz (7.47) Equation (7.47) has separable solutions of the form

C

c n n

t B

exp 2 0

n n n

z B

(7.48)

which provides some justification for empirical relationship (7.20). The solution of the finite strain consolidation problem in any of its three forms requires constitutive relationships

e e

(7.49)

K K (7.50)

Bear (1979) notes that curve fitting of experimental data typically results in relationships of the form



---PAGE-83---



- o av e eo (7.51)

- o c ln e


(7.52)

C

eo

for noncohesive and coheasive soils respectively, where av is the coefficient of compressibility and Cc is the compression index. Graphical presentation of experimental forms of (7.49) and (7.50) are presented in Cargill (1985) and Palermo et al., (1998) which are generally consistent with (7.52) and suggest

K K

o ln

o

(7.53)

as a candidate relationship between the void ratio and hydraulic conductivity for cohesive sediment beds. Similarly, a linear relationship

o K Ko (7.54) would likely suffice for noncohesive sediment beds.

## 8. References

Ackers, P., and W. R. White, 1973: Sediment transport: New approaches and analysis. J. Hyd. Div. ASCE, 99, 2041-2060.

Ariathurai, R., and R. B. Krone, 1976: Finite element model for cohesive sediment transport. J. Hyd. Div. ASCE, 102, 323-338.

Ambrose, R. B., T. A. Wool, and J. L. Martin, 1993: The water quality analysis and simulation program, WASP5: Part A, model documentation version 5.1. U. S. EPA, Athens Environmental Research Laboratory, 210 pp.

Bear, J., 1879: Hydraulics of groundwater, McGraw-Hill, New York. Bagnold, R. A., 1956: The flow of cohesionless grains in fluids. Phil. Trans. Roy. Soc. Lond., Series A, Vol 249, No. 964, 235-297.

Blumberg, A. F., B. Galperin, and D. J. O'Connor, 1992: Modeling vertical structure of open-channel flow. J. Hydr. Engr., 118, 1119-1134.

Boyer, J. M., S. C. Chapra, C. E. Ruiz, and M. S. Dortch, 1994: RECOVERY, a mathematical model to predict the temporal response of surface water to contaminated



---PAGE-84---



sediment. Tech. Rpt. W-94-4, U. S. Army Engineer Waterways Experiment Station, Vicksburg, MS, 61 pp.

Burban, P. Y., W. Lick, and J. Lick, 1989: The flocculation of fine-grained sediments in estuarine waters. J. Geophys. Res., 94, 8323-8330.

Burban, P. Y., Y. J. Xu, J. McNeil, and W. Lick, 1990: Settling speeds of flocs in fresh and seawater. J. Geophys. Res., 95, 18,213-18,220.

Cargill, K. W., 1985: Mathematical model of the consolidation and desiccation processes in dredge material. U.S. Army Corps of Engineers, Waterways Experiment Station, Technical Report D-85-4.

Dortch, M., C. Ruiz, T. Gerald, and R. Hall, 1998: Three-dimensional contaminant transport/fate model. Estuarine and Coastal Modeling, Proceedings of the 5nd International Conference, M. L. Spaulding and A. F. Blumberg, Eds., American Society of Civil Engineers, New York, 75-89.

Einstein, H. A., 1950: The bed load function for sediment transport in open channel flows. U.S. Dept. Agric. Tech. Bull., 1026.

Galperin, B., L. H. Kantha, S. Hassid, and A. Rosati, 1988: A quasi-equilibrium turbulent energy model for geophysical flows. J. Atmos. Sci., 45, 55-62.

Garcia, M., and G. Parker, 1991: Entrainment of bed sediment into suspension. J. Hyd. Engrg., 117, 414-435.

Gibbs, R. J., 1985: Estuarine Flocs: their size, settling velocity and density. J. Geophys. Res., 90, 3249-3251.

Gibson, R. E., G. L. England, and M. J. L. Hussey, 1967: The theory of one-dimensional consolidation of saturated clays. Geotechnique, 17, 261-273.

Hamrick, J. M., 1992: A three-dimensional environmental fluid dynamics computer code: Theoretical and computational aspects. The College of William and Mary, Virginia Institute of Marine Science, Special Report 317, 63 pp.

Hamrick, J. M., and T. S. Wu, 1997: Computational design and optimization of the EFDC/HEM3D surface water hydrodynamic and eutrophication models. Next Generation Environmental Models and Computational Methods. G. Delich and M. F. Wheeler, Eds., Society of Industrial and Applied Mathematics, Philadelphia, 143-156.

Hayter, E. J., and A. J. Mehta, 1983: Modeling fine sediment transport in estuaries. Report EPA-600/3-83-045, U.S. Environmental Protection Agency. Athens, GA>



---PAGE-85---



Hayter, E.J., M. Bergs, R. Gu, S. McCutcheon, S. J. Smith, and H. J. Whiteley, 1998: HSCTM-2D, a finite element model for depth-averaged hydrodynamics, sediment and contaminant transport. Technical Report, U. S. EPA Environmental Research Laboratory, Athens, GA.

Hwang, K.-N, and A. J. Mehta, 1989: Fine sediment erodibility in Lake Okeechobee. Coastal and Oeanographic Enginnering Dept., University of Florida, Report UFL/COEL89/019, Gainsville, FL.

Laursen, E., 1958: The total sediment load of streams J. Hyd. Div. ASCE, 84, 1-36.

Letter, J. V., L. C. Roig, B. P. Donnell, Wa. A. Thomas, W. H. McAnally, and S. A. Adamec, 1998: A user's manual for SED2D-WES, a generalized computer program for two-dimensional, vertically averaged sediment transport. Version 4.3 Beta Draft Instructional Report, U. S. Army Corps of Engrs., Wtrwy. Exper. Sta., Vicksburg, MS.

Le Normant, C., E. Peltier, and C. Teisson, 1998: Three dimensional modelling of cohesive sediment in estuaries. in Physics of Estuaries and Coastal Seas, (J. Dronkers and M. Scheffers, Eds.), Balkema, Rotterdam, pp 65-71.

Lick, W., and J. Lick, 1988: Aggregation and disaggregation of fine-grained lake sediments. J Great Lakes Res., 14, 514-523.

Mehta, A. J., E. J. Hayter, W. R. Parker, R. B. Krone, A. M. Teeter, 1989: Cohesive sediment transport. I: Process description. J. Hyd. Engrg., 115, 1076-1093.

Mehta, A. J., T. M. Parchure, J. G. Dixit, and R. Ariathurai, 1982: Resuspension potential of deposited cohesive sediment beds, in Estuarine Comparisons, V. S. Kennedy, Ed., Academic Press, New York, 348-362.

Mehta, A. J., and F. Jiang, 1990: Some field observations on bottom mud motion due to waves. Coastal and Oeanographic Enginnering Dept., University of Florida, Gainsville, FL.

Mellor, G. L., and T. Yamada, 1982: Development of a turbulence closure model for geophysical fluid problems. Rev. Geophys. Space Phys., 20, 851-875.

Meyer-Peter, E. and R. Muller, 1948: Formulas for bed-load transport. Proc. Int. Assoc. Hydr. Struct. Res., Report of Second Meeting, Stockholm, 39-64.

Middleton, G. V., and P. R. Wilcock, 1994: Mechanics in the Earth and Environmental Sciences. Cambridge University Press, Cambridge, UK.

Nielsen, P., 1992: Coastal bottom boundary layers and sediment transport, World Scientific, Singapore.



---PAGE-86---



Park, K., A. Y. Kuo, J. Shen, and J. M. Hamrick, 1995: A three-dimensional hydrodynamic-eutrophication model (HEM3D): description of water quality and sediment processes submodels. The College of William and Mary, Virginia Institute of Marine Science. Special Report 327, 113 pp.

Rahmeyer, W. J., 1999: Lecture notes for CEE5560/6560: Sedimentation Engineering, Dept. of Civil and Environmental Engineering, Utah State University, Logan, Utah.

Raukivi, A. J., 1990: Loose boundary hydraulics. 3rd Ed. Pergamon, New York, NY. Ried, I., and L. E. Frostick, 1994: Fluvial sediment transport and deposition. in Sediment Transport and Depositional Processes, K. Pye, ed., Blackwell, Oxford, UK, 89-155.

Shrestha, P. A., and G. T. Orlob, 1996: Multiphase distribution of cohesive sediments and heavy metals in estuarine systems. J. Environ. Engrg., 122, 730-740.

Smagorinsky, J., 1963: General circulation experiments with the primative equations, Part I: the basic experiment. Mon. Wea. Rev., 91, 99-152.

Smith, J. D., and S. R. McLean , 1977: Spatially averaged flow over a wavy bed. J. Geophys. Res., 82, 1735-1746.

Smolarkiewicz, P. K., and T. L. Clark, 1986: The multidimensional positive definite advection transport algorithm: further development and applications. J. Comp. Phys., 67, 396-438.

Smolarkiewicz, P. K., and W. W. Grabowski, 1990: The multidimensional positive definite advection transport algorithm: nonoscillatory option. J. Comp. Phys., 86, 355375.

Spasojevic, M., and F. M. Holly, 1994: Three-dimensional numerical simulation of mobile-bed hydrodynamics. Contract Report HL-94-2, US Army Engineer Waterways Experiment Station, Vicksburg, MS.

Stark, T. D., 1996: Program documentation and users guide: PSDDF primary consolidation, secondary compression, and desiccation of dredge fill. Instructional Report EL-96-xx, US Army Engineer Waterways Experiment Station, Vicksburg, MS.

Suzuki, K., H. Yamamoto, and A. Kadota, 1998: Mechanism of bed load fluctuations of sand-gravel mixture in a steep slope channel, Proc. of the 11th congress of APD IAHR, Yogyakarta, pp.679-688.

Tsai, C. H., S. Iacobellis, and W. Lick, 1987: Floccualtion fo fine-grained lake sediments due to a uniform shear stress. J Great Lakes Res., 13, 135-146.



---PAGE-87---



van Niekerk, A., K. R. Vogel, R. L Slingerland, and J. S. Bridge, 1992: Routing of heterogeneous sedimetns over movable bed: Model development. J. Hyd. Engrg., 118, 246-262.

- Van Rijin, L. C., 1984a: Sediment transport, Part I: Bed load transport. J. Hyd. Engrg., 110, 1431-1455.
- Van Rijin, L. C., 1984b: Sediment transport, Part II: Suspended load transport. J. Hyd. Engrg., 110, 1613-1641.


Villaret, C., and M. Paulic, 1986: Experiments on the erosion of deposited and placed cohesive sediments in an annular flume and a rocking flume. Coastal and Oeanographic Enginnering Dept., University of Florida, Report UFL/COEL-86/007, Gainsville, FL.

- Ziegler, C. K., and B. Nesbitt, 1994: Fine-grained sediment transport in Pawtuxet River, Rhode Island. J. Hyd. Engrg., 120, 561-576.
- Ziegler, C. K., and B. Nesbitt, 1995: Long-term simulation of fine-grained sediment transport in large reservoir. J. Hyd. Engrg., 121, 773-781.


Yang, C. T., 1973: Incipient motion and sediment transport. J. Hyd. Div. ASCE, 99, 16791704.

Yang, C. T., 1984: Unit stream power equation for gravel. J. Hyd. Engrg., 110, 17831797.

Yang, C. T., and A. Molinas, 1982: Sediment transport and unit streams power function. J. Hyd. Div. ASCE, 108, 774-793.



---PAGE-88---



## 9. Figures



---PAGE-89---



|1e-01<br><br>1e+00<br>1e+01<br>| |critical shields settling velocit|shear velo y|city| |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
|1e-04<br><br>1e-03<br><br>1e-02| | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


1e-05 1e-04 1e-03 1e-02 1e-01 1e+00 grain diameter (meters)

Figure 1. Critical Shield's shear velocity and settling velocity as a function of sediment grain size.



---PAGE-90---



## 8. Sorptive Contaminant Transport

The transport of a sorptive contaminant in the water column is governed by transport equations for the contaminant dissolved in the water phase, for the contaminant sorbed to material effectively dissolved in the water phase, and for the contaminant sorbed to suspended particles. For the portion of the contaminant dissolved directly in the water phase

m m HC m HuC m HvC m m wC A m m C m m H K S K D H

t x y w x y w y x w z x y w

b i i i j j j z x y z w x y dS S dD D

(8.1)

i j

C K S

ˆ

i i w i i aS w S S

i x y

m m H

C K D C

ˆ

j j w j j

aD w D D w j

where Cw is the mass of water dissolved contaminant per unit total volume, S is the mass of contaminant sorbed to sediment class i per mass of sediment, D is the mass of contaminant sorbed to dissolved material j per unit mass of dissolved material, is the porosity, w is the fraction of the water dissolved contaminant available for sorption, Ka is the adsorption rate, Kd is the desorption rate, and is a net linearized decay rate coefficient. The sorption kinetics are based on the Langmuir isotherm (Chapra, 1997) with ˆ denoting the saturation sorbed mass per carrier mass. The sediment and dissolved material concentrations, S and D are defined as mass per unit total volume. The transport equation for the portion of material sorbed to a dissolved constituent D is,

j j j j j j j j t x y D x y D y x D z x y D

m m HD m HuD m HvD m m wD

A C m m D m m H K D

(8.2)

ˆ

b j j j j w j j z x y z D x y sD w D D

H

j j j x y dD D

m m H K D

The transport equation for the portion of material sorbed to a suspended constituent S is,

i i i i i i i i t x y S x y S y x S z x y S

m m HS m HuS m HvS m m wS A m m w S m m S

(8.3)

i i i b i i z x y S S z x y z S

H C

ˆ

i i w i i i i i x y aS w S S x y dS S

m m H K S m m H K S



---PAGE-91---



Introducing sorbed concentrations defining sorbed mass per unit total volume

###### CD D D (8.4)

j j j

CS S S (8.5) Allows equations (8.1) through (8.3) to be written as

i i i

m m HC m HuC m HvC m m wC A m m C m m H K C K C H

t x y w x y w y x w z x y w

b i i j j z x y z w x y dS S dD D

(8.6)

i j

C K S

ˆ

i i w i i aS w S S

i x y

m m H

C K D C

ˆ

j j w j j

aD w D D w j

j j j j t x y D x y D y x D z x y D

m m HC m HuC m HvC m m wC

A C m m C m m H K D

(8.7)

ˆ

b j j j w j j z x y z D x y sD w D D

H

j j x y dD D

m m H K C

i i i i t x y S x y S y x S z x y S

m m HC m HuC m HvC m m wC A m m w C m m C

i i b i z x y S S z x y z S

H C

ˆ

i i w i i i i x y aS w S S x y dS S

m m H K S m m H K C

(8.8)

The EFDC sorbed contaminant transport formulation currently employees equilibrium partitioning with the adsorption and desorption terms in (8.7) and (8.8) balancing

sDj j w Cw ˆDj Dj dDj Dj

K D K C

aSi i w Cw ˆSi Si dSi Si

K S K C

(8.9)

(8.10)



---PAGE-92---



###### Solving (8.9) and (8.10) for the sorbed to water phase concentration ratios gives

j j j D D j

C f D

P C f

D w w

1

C P P P

j j j w D Do Do j

1

ˆ ˆ

D j j

K P

j w aD D Do j

K

dD

(8.11)

i i i S S i

C f S

P C f

S w w

1

C P P P

i i i w S So So i

1

ˆ ˆ

S i i

K P

j w aS S So i

K

dS

(8.12)

where P denotes the partition coefficient, and Po is its linear equilibrium value. For linear equilibrium partitioning, P is set to Po, which in effect approximates ( )-1 terms in (8.11) and (8.12) by unity. Requiring the mass fractions to sum to unity

f f f (8.13)

w Si Dj 1

i j

gives

C f

w w i i j j

C P S P D

S D i j

j j j j D D

C P D f

D i i j j

C P S P D

S D i j

i i i i S S

C P S f

S i i j j

C P S P D

S D i j

(8.14)

The dissolved concentrations can be alternately expressed by mass per unit volume of the water phase



---PAGE-93---



C C

w w w

:

j

- C C
- D D


j D D w

:

j

J w

:

(8.15)

with (8.14) becoming

C

ww 1

:

i i j J S D w i j

C P S P D

:

j j J D w D w

C P D C P S P D

: :

i i j J S D w i j

:

i i i S S

C P S C P S P D

i i j J S D w i j

:

(8.16)

Which is a generalization of Chapra's (1997) formulation for sorption to dissolved and particulate organic carbon.

Adding equations (8.6), (8.7), and (8.8), using the equilibrium partitioning relationships (8.9) and (8.10) gives

###### 1 1

m m HC m HuC m HvC m m wC m m m m

t x y x y y x z x y x y x y

(8.17)

A m m w f C m m C m m H C H

i i b z x y S S z x y z x y i

the equation for the total concentration, C. The boundary condition at the water columnsediment bed interface, z = 0, is



---PAGE-94---



A

b i i

C w f C H

z S S i

j

C C J

i w D i i SBS j SBS S i

J

max ,0 max ,0

i S

(8.18)

SB j

C C J

i w D i i SBS j SBS S dep i

J

min ,0 min ,0

i S dep

WC

j w D

C C

i SBB i S

J

j

max ,0

i

SB

j i w D SBB j

C C J

min ,0

dep i i S dep

WC

j j w D w D

C C C C q q

j j w w

max ,0 min ,0

dep

SB WC j

j w D

C C q

C C

w D

j dif

j

dep

WC SB

where JSBS and JSBB are the suspended load and bed load sediment fluxes between the sediment bed and the water column, defined as positive from the bed, s is the sediment density, qw is the water specific discharge due to bed consolidation and groundwater interaction, defined as positive from the bed, and qdif is a diffusion velocity incorporating the effects of molecular diffusion, hydrodynamic dispersion, and biological induced mixing. The subscript SB denotes conditions in the top layer of the sediment bed, while the subscript WC denotes condition in the water column immediately above the bed, with the exception that the specific discharge and diffusion velocity are defined at the water column-bed interface. The subscript, dep, is used to denote the void ratio and porosity of newly depositing sediment. Equation (8.16) indicates that contaminant flux between the bed and water column includes, a flux of suspended sediment sorbed material; fluxes of water dissolved and sorbed to water dissolved material due to the specific discharge of water associated with consolidation and ground water interaction and water entrainment and expulsion associated with both suspended and bed load sediment deposition and resuspension; and a flux of water dissolved and sorbed to water dissolved material due to diffusion like processes. Transport of bed load sediment sorbed material is represented by direct transport between horizontally adjacent top bed layers and is included in the



---PAGE-95---



contaminant mass conservation equations for the sediment bed. The boundary condition at the water free surface is

A

b z Si Si 0 : 1

C w f C z H

i

(8.19)

Using the relationship between the porosity and void ratio

1

and (8.5) allows (8.18) to be written as

(8.20)

A

b i i

C w f C H

z S S i

i i

C J J C C S

i S SBS j SBS i i w D

max ,0 1 max ,0

i S j SB i i

C J J C C S

i S SBS j SBS i dep i w D

min ,0 1 min ,0

i S j WC

i SBB i S

J

j

C C

1 max ,0

w D i j

(8.21)

SB

i SBB j

J

C C

1 min ,0

dep i w D i S j WC

1 max ,0

j w dif w D

q q C C

j

SB

1 min ,0

j w dif w D

q q C C

j

WC

The sediment concentration can be expressed in terms of the sediment density and void ratio by

i i

i F s

S

1

(8.22)

where Fi is the fraction of the total sediment volume occupied by each sediment class



---PAGE-96---



1 i i i

S S F

i i i s s

(8.23)

Introducing (8.14) and (8.22) into (8.21) gives the final form of the bottom boundary condition

A

b i i

C w f C H

z S S i

i i i i SBS S SBS j

J f F J

C f f C S S

max ,0 max ,0

i i w D i j

SB

i i i i SBS S dep SBS j

J f F J

C f f C S S

min ,0 min ,0

i i w D i dep j

WC

i SBB

J

j

C

C

1 max ,0

(8.24)

D i j

i w S

SB

i SBB j

J

C C

1 min ,0

dep i w D i S j WC

1 max ,0

j w dif w D

q q f f C

j

SB

1 min ,0

j w dif w D

q q f f C

j

WC

Note that the form of the bed flux associated with bed load transport remains unmodified since a sediment concentration in the water column cannot be readily defined for sediment being transported as bed load.

The transport equation (8.17) for the total contaminant concentration in the water column is solved using a fractional step procedure which sequentially treats advection; settling, deposition, and resuspension; pore water advection and diffusion; and reactions. The fractional phase distribution of the contaminant is recalculated between the advection, settling, deposition and resuspension, and pore water advection and diffusion steps using (8.14). The advection step is

(8.25)

n 1/4 n x y y x z 0

HC HC m HuC m HvC wC m m m m

x y x y

with the vertical boundary conditions

##### wC 0 : z 0,1 (8.26)



---PAGE-97---



The fractional time level in (8.25) and subsequent equations is used to denote an intermediate result in the fractional step procedure. The spatially discrete from of (8.25) is solved using one of the standard high order, flux limited, advective transport solvers in the EFDC model.

The settling, deposition, and resuspension step is

n 1/2 n 1/4 i i z S S

HC HC w f C

i

(8.27)

with the boundary conditions

i i S S

w f C

i

i i i i SBS S SBS j

J f F J

C f f C S S

max ,0 max ,0

i i w D i j

SB

(8.28)

i i i i SBS S dep SBS j

J f F J

C f f C S S

min ,0 min ,0

i i w D i dep j

WC

i SBB j

J

C C

1 max ,0

i w D S j

i

SB

i SBB j

J

C C z

1 min ,0 : 0

dep i w D i S j WC

###### wSi fSiC 0 : z 1 (8.29)

###### Integrating (8.27) over a water column layer and using upwind differencing for the settling gives,

n i i i

1/2 1/2 1/4 1/2

w S f HC HC HC H S

n n S k S n k k k k i k

1 1

(8.30)

i k n

1/2

i i i S k S n

w S f

1/2

HC H S

i k i k

for a layer not adjacent to the bed, and,



---PAGE-98---



n i

1/2

f HC HC w S C

n n i i S n

1/2 1/4 1/2 1 1 1 1 1 2

S i i

S J f J F

2

n

1/2

i i i i SBS S SBS j n

max ,0 max ,0 1/2

f f C S S

i i w D sb i j

sb

n

1/2

i i i i SBS S SBS j

J f J F

(8.31)

n i

1/2 1

f f S S

C

min ,0 min ,0

i i w D j

1 1/2

n

i SBB j n

J

1/2

f f C

1 max ,0

i w D sb i S j sb

n

1/2

i SBB j n

J

1/2 1

f f C

1 min ,0

i w D i S j

1

for the first layer adjacent to the bed. Note that (8.31) is also the appropriate form for single layer or depth average application. Since the sediment settling flux is zero at the top of the free surface adjacent layer, (8.27) is integrated downward from the top layer to the bottom layer. The bottom layer equation (8.31) is solved simultaneously with a corresponding equation for the top layer of the sediment bed. The settling fluxes, wSS, and water column-sediment bed fluxes, JSB, in (8.30) and (8.31) are known from the preceding solution for sediment settling, deposition and resuspension. Terms containing the sediment sorbed fraction divided by the sediment concentration in (8.30) and (8.31) are given by

i i S S

f P S P S P D (8.32)

i i i j j

S D i j

The diffusion step is given by

A HC HC C H

n 3/4 n 1/2 b z z

(8.33)

with boundary conditions

A

1 max ,0

b j z w dif w D

C q q f f C H

j

(8.34)

SB

1 min ,0 : 0

j w dif w D

q q f f C z

dep j WC



---PAGE-99---



A

b z 0 : 1

C z H

For the first layer adjacent to the bed

n n n b

3/4 3/4 1/2

A HC HC C H

z

1 1

1 1

n j n w dif w D SB j

1/2

1 max ,0

3/4

q q f f C

1

SB n

1/2

1 min ,0

j n w dif w D

1/2 1

q q f f C

j dep

1 1

(8.35)

(8.36)

It is noted that the bed concentrations are advanced to the n+3/4 intermediate time level before the advance of the water column concentrations. While for layers not adjacent to the bed,

n n n n b b k k z z

3/4 3/4 3/4 1/2

A A HC HC C C H H

k k

1 1

(8.37)

The solution is completed by

HC k HC k HC k (8.38) an implicit reaction step.

n 1 n 3/4 n 1

Contaminant transport in the sediment bed is represented using the discrete layer formulation developed for bed geomechanical processes. The conservation of mass for the total contaminant concentration in a layer of the sediment bed is given by



---PAGE-100---



BC BC J f J F

t k k

i i i i SBS S SBS j

k kt f f BC BS BS

, max ,0 max ,0

i i w D kt i j

kt

i i i i SBS S SBS dep j

J f J F k kt C f f C S S

, min ,0 min ,0

i i w D i dep j

WC

i i SBB SBL

k kt J

, ,0

i

i SBB j

J t f f BC B

k k 1 max ,0

,

i w D kt i S j kt

(8.39)

i SBB j

J k kt f f C

, 1 min ,0

dep i w D i S j WC

1 max ,0 min ,0

j w dif k w dif k w D k j

q q q q f f BC B

k

1 , min ,0

j w dif kt w D

k kt q q f f

C

j

WC

1 1 , min ,0

j w dif k w D k j

k kt q q f f BC B

1 1

k

1 max ,0

j w dif k w D k j

q q f f BC B

1 1

k

where

k kt k kt

- 0 :

,

- 1 :


k kt

(8.40)

is used to distinguish processes specific to the top, water column adjacent layer of the bed, kt. Advective fluxes associated with pore water advection in (8.40) are represented in upwind form. In the sediment bed, the actual computational variables for sediment, contaminant, and dissolved material are their concentrations times the thickness of the bed layer. Consistent with this formulation, the fractional phase components in the bed are defined by



---PAGE-101---



BC B f

w w k i i j j k S D i j k

BC B P BS P BD

(8.41)

j j j j D D

BC P BD f

D k i i j j k S D

BC B P BS P BD

i j k

i i i i S S

BC P BS f

S k i i j j k S D i j k

BC B P BS P BD

The contaminant fluxes associated bed load sediment transport are determined as follows. The net sediment flux from the bed load transport equation

mxmyJSBB x myQSBLx x mxQSBLy (8.42)

i i i

is used to evaluate the flux associated with pore water entrainment and expulsion in (8.25) and (8.40). The transport equation for material sorbed to the bed load is

x myQSBLx SBL x mxQSBLy SBL mxmyJSBB SBL (8.43)

i i i i i i

Since the contaminant mass per sediment mass in the transport divergence corresponds to conditions in the top layer of the sediment bed, (8.43) can be written as

(8.44)

i i i S i S i i x y SBLx i x x SBLy i x y SBB SBL

f f m Q C m Q C m m J S S

And solved using an upwind approximation

i i x y SB SBL

m m J f f

i i i S i S

m Q C m Q C S S

max min

y SBLx E i y SBLx E i

C E i i

f f

i S i S y SBLx W i y SBLx W i

m Q C m Q C S S f f

max min

W C i i

i S i S x SBLy N i x SBLy N i

m Q C m Q C S S f

max min

C N i

i i S

f Q C S

i S x SBLy S i

m Q C m S

max min

x SBLy S i

S

C

(8.45)



---PAGE-102---



To evaluate the transport of bed load sorbed material between horizontally adjacent top layers of the sediment bed.

Equation (8.39) is solved using a fractional step procedure consistent with that used for the water column transport. Equation (8.41) is used to update the fractional distribution in the bed between the settling, deposition, and resuspension step and the pore water advection and diffusion step. The settling, deposition and resuspension step applies only to the top layer of the bed and is

n n kt kt

1/2

BC BC J f J F

n

1/2

i i i i SBS S SBS j n

1/2

f f BC BS BS

max ,0 max ,0

i i w D kt i j

kt

n

1/2

i i i i SBS S SBS dep j

J f J F

C f f C S S

min ,0 min ,0

i i w D i dep j

(8.46)

WC

i i SBB SBL

J

,

0

i

n

1/2

i SBB j n

J

1/2

f f BC B

1 max ,0

i w D kt i S j kt

n

1/2

i SBB j

J

f f C

1 min ,0

dep i w D i S j WC

This equation is solved simultaneously with equation (8.31) for the bottom layer of the water column. The solution is represented by

n i i n kt SB SBL

1/2

###### BC J

n i i ib

1/2 11 12

a a BC a a HC f

(8.47)

kt n n

1/2 1/2 21 22 1 1/4 1/2 1 1 1 2 2

i n i i S n

HC w S C S

S i i

where the coefficients are given by



---PAGE-103---



n

1/2

i i i i SBS S SBS j

J f J F a f f BS BS

1 max ,0 max ,0

i i w D i j

- 11

1/2

- 12


kt n

i SBB j

J

f f B

1 max ,0

i w D i S j kt

n

1/2

i i i i SBS S SBS dep j

J f J F a f f H S S

min ,0 min ,0

i i w D dep

i j n

1 1/2

i SBB j

J

f f H

1 min ,0

dep i w D i S j

1

(8.48)

n

1/2

i i i i SBS S SBS j

J f J F a f f

max ,0 max ,0

i i w D i j

21

BS BS J

kt

n

1/2

i SBB j

f f B

1 max ,0

i w D S j

i

kt

n

1/2

i i i i SBS S SBS j

J f J F a f f H S S

min ,0 min ,0

i i w D i j

22 1

1 1/2

n

i SBB j

J

f f H

1 min ,0

i w D i S j

1

Adding the two equations in (8.47) gives

n n n n kt kt

1/2 1/2 1/4 1 1 1/2

BC HC BC HC f w S C J S

n

i i i S n i i n S i SBS SBL

1/2 1/2 1 2 2

i i

(8.49)

This equation verifies the consistency of the water column-sediment bed exchange since the source and sinks on the right side include only settling into the top of the water column layer, and transfer of bed load sediment sorbed contaminant between horizontal sediment bed cells.

The pore water advection and diffusion step for the top, water column adjacent, layer is



---PAGE-104---



n n kt kt

3/4 1/2

BC BC

n j n w dif kt w D kt j

1/2

1 max ,0

3/4

q q f f BC B

kt n

1/2

1 min ,0

j n w dif kt w D kt j

3/4

q q f f BC B

kt n

1/2

1 min ,0

j n w dif kt w D

1/2 1

q q f f HC H

j

1

n j n

1/2

1

1/2

q

q f f BC B

max ,0

w

dif kt w D kt j

1 1

kt

(8.50)

which is an implicit form. Writing (8.36) in the form

n n n b

3/4 3/4 1/2

###### A HC HC C H

z

1 1 1 1

1 1/2

n j n w dif kt w D kt j

1 max ,0

3/4

q q f f BC B

SB n

1/2

1 min ,0

j n w dif kt w D

1/2 1

q q f f HC H

j

1

(8.51)

and combining with (4.49) gives

n

3/4 3/4 3/4 1/2 1/2

###### A BC HC BC HC C H

n n n n b kt kt z

1 1

1 1/2

n j n w dif kt w D kt j

1 min ,0

3/4

q q f f BC B

kt n

1/2

1 max ,0

j n w dif kt w D kt j

3/4 1

q q f f BC B

kt

1

(8.52)

This equation verifies the consistency of the representation of pore water advection and diffusion across water column-sediment bed interface since the source and sink terms on the right side of (8.52) represent fluxes at the top to the water column cell and the bottom of the bed cell.

The pore water diffusion and advection step for the remaining bed layers is given by



---PAGE-105---



n n k k

3/4 1/2

BC BC

n

1/2

1 min ,0

j n w dif k w D k

3/4 1

q q f f BC B

j

k n

1 1/2

1 max ,0

j n w dif k w D k

3/4

q q f f BC B

j

k n

1/2

1 min ,0

j n w dif k w D k

3/4

q q f f BC B

j

k

n

1/2

1

j n k w D k

3/4 1

q q

f f BC B

max ,0

w dif

j

k

1

(8.53)

For the bottom layer of the bed, k = 1, the bottom, k-, specific discharge and diffusion velocity must be specified as well as the total contaminant concentration, C0. The corresponding thickness of the unresolved layer, k = 0, is set to unity without loss of generality. The system of equations represented by (8.49) and (8.52) is implicit and is solved using a tri-diagonal linear equation solver. It is noted that the n+3/4 time level layer thickness is actually the n+1 time level thickness determined by the solution of (8.23). The specific discharges in (8.49) and (8.52) are given by (8.41) and represent those appearing in (8.23) and guarantee mass conservation for the pore water advection.

The bed transport solution is completed by

###### BC k BC k BC k (8.54) an implicit reaction step.

n 1 n 3/4 n 1



---PAGE-106---



## 9. References

Ackers, P., and W. R. White, 1973: Sediment transport: New approaches and analysis. J. Hyd. Div. ASCE, 99, 2041-2060.

Ariathurai, R., and R. B. Krone, 1976: Finite element model for cohesive sediment transport. J. Hyd. Div. ASCE, 102, 323-338.

Ambrose, R. B., T. A. Wool, and J. L. Martin, 1993: The water quality analysis and simulation program, WASP5: Part A, model documentation version 5.1. U. S. EPA, Athens Environmental Research Laboratory, 210 pp.

Bear, J., 1879: Hydraulics of groundwater, McGraw-Hill, New York. Bagnold, R. A., 1956: The flow of cohesionless grains in fluids. Phil. Trans. Roy. Soc. Lond., Series A, Vol 249, No. 964, 235-297.

- Belleudy, P., 2001: Numerical simulation of sediment mixture deposition, part 1: analysis of flume experiments. J. Hyd. Res., 38, 417-425.
- Belleudy, P., 2001: Numerical simulation of sediment mixture deposition, part 2: a sensitivity analysis. J. Hyd. Res., 39, 25-31.


Blumberg, A. F., B. Galperin, and D. J. O'Connor, 1992: Modeling vertical structure of open-channel flow. J. Hyd. Engr., 118, 1119-1134.

Boyer, J. M., S. C. Chapra, C. E. Ruiz, and M. S. Dortch, 1994: RECOVERY, a mathematical model to predict the temporal response of surface water to contaminated sediment. Tech. Rpt. W-94-4, U. S. Army Engineer Waterways Experiment Station, Vicksburg, MS, 61 pp.

Burban, P. Y., W. Lick, and J. Lick, 1989: The flocculation of fine-grained sediments in estuarine waters. J. Geophys. Res., 94, 8323-8330.

Burban, P. Y., Y. J. Xu, J. McNeil, and W. Lick, 1990: Settling speeds of flocs in fresh and seawater. J. Geophys. Res., 95, 18,213-18,220.

Cargill, K. W., 1985: Mathematical model of the consolidation and desiccation processes in dredge material. U.S. Army Corps of Engineers, Waterways Experiment Station, Technical Report D-85-4.

Dortch, M., C. Ruiz, T. Gerald, and R. Hall, 1998: Three-dimensional contaminant transport/fate model. Estuarine and Coastal Modeling, Proceedings of the 5nd International Conference, M. L. Spaulding and A. F. Blumberg, Eds., American Society of Civil Engineers, New York, 75-89.



---PAGE-107---



Einstein, H. A., 1950: The bed load function for sediment transport in open channel flows. U.S. Dept. Agric. Tech. Bull., 1026.

Fredricks, C., and J. M. Hamrick, 1996: The effect of channel geometry on gravitational circulation in partially mixed estuaries. Buoyancy Effects on Coastal and Estuarine Dynamics, D. Aubrey and C. Fredricks, Eds., AGU, 283-300.

Galperin, B., L. H. Kantha, S. Hassid, and A. Rosati, 1988: A quasi-equilibrium turbulent energy model for geophysical flows. J. Atmos. Sci., 45, 55-62.

Garcia, M., and G. Parker, 1991: Entrainment of bed sediment into suspension. J. Hyd. Engrg., 117, 414-435.

Gibbs, R. J., 1985: Estuarine Flocs: their size, settling velocity and density. J. Geophys. Res., 90, 3249-3251.

Gibson, R. E., G. L. England, and M. J. L. Hussey, 1967: The theory of one-dimensional consolidation of saturated clays. Geotechnique, 17, 261-273.

Hamrick, J. M., 1992: A three-dimensional environmental fluid dynamics computer code: Theoretical and computational aspects. The College of William and Mary, Virginia Institute of Marine Science, Special Report 317, 63 pp.

Hamrick, J. M., 1994: Linking hydrodynamic and biogeochemcial transport models for estuarine and coastal waters. Estuarine and Coastal Modeling, Proceedings of the 3rd International Conference, M. L. Spaulding et al, Eds., American Society of Civil Engineers, New York, 591-608.

Hamrick, J. M., and Wm. B. Mills, 2001: Analysis of temperatures in Conowingo Pond as influenced by the Peach Bottom atomic power plant thermal discharge. Environ. Sci. Policy, 3, s197-s209.

Hamrick, J. M., and T. S. Wu, 1997: Computational design and optimization of the EFDC/HEM3D surface water hydrodynamic and eutrophication models. Next

Generation Environmental Models and Computational Methods. G. Delich and M. F. Wheeler, Eds., Society of Industrial and Applied Mathematics, Philadelphia, 143-156.

Hayter, E. J., and A. J. Mehta, 1983: Modeling fine sediment transport in estuaries. Report EPA-600/3-83-045, U.S. Environmental Protection Agency. Athens, GA>

Hayter, E.J., M. Bergs, R. Gu, S. McCutcheon, S. J. Smith, and H. J. Whiteley, 1998: HSCTM-2D, a finite element model for depth-averaged hydrodynamics, sediment and contaminant transport. Technical Report, U. S. EPA Environmental Research Laboratory, Athens, GA.



---PAGE-108---



Hwang, K.-N, and A. J. Mehta, 1989: Fine sediment erodibility in Lake Okeechobee. Coastal and Oeanographic Enginnering Dept., University of Florida, Report UFL/COEL89/019, Gainsville, FL.

Ji, Z.-G., J. H. Hamrick, and J. Pagenkopf, 2002: Sediment and metals modeling in shallow river, J. Environ. Engrg., 128, 105-119.

Jin, K. R., J. M. Hamrick, and T. S. Tisdale, 2000: Application of a three-dimensional hydrodynamic model for Lake Okeechobee, J. Hyd. Engrg., 106, 758-772.

Jin, K. R., Z. G. Ji, and J. M. Hamrick, 2002: Modeling winter circulation in Lake Okeechobee, Florida. J. Waterway, Port, Coastal, Ocean Engrg., 128, 114-125.

Karim, M. F., and F. M. Holley, Jr., 1986: Armoring and sorting simulation in alluvial rivers. J. Hyd. Engrg., 112, 705-715.

Kleinhans, M. G., and L. C. Van Rijin, 2002: Stochastic prediction of sediment transport in sand-gravel bed rivers. J. Hyd. Engrg., 128, 412-425.

Kuo, A. Y., J. Shen, and J. M. Hamrick, 1996: The effect of acceleration on bottom shear stress in tidal estuaries. J. Waterway, Port, Coastal, Ocean Engrg., 122, 75-83.

Laursen, E., 1958: The total sediment load of streams J. Hyd. Div. ASCE, 84, 1-36. Letter, J. V., L. C. Roig, B. P. Donnell, Wa. A. Thomas, W. H. McAnally, and S. A. Adamec, 1998: A user's manual for SED2D-WES, a generalized computer program for two-dimensional, vertically averaged sediment transport. Version 4.3 Beta Draft Instructional Report, U. S. Army Corps of Engrs., Wtrwy. Exper. Sta., Vicksburg, MS. Le Normant, C., E. Peltier, and C. Teisson, 1998: Three-dimensional modelling of cohesive sediment in estuaries. in Physics of Estuaries and Coastal Seas, (J. Dronkers and M. Scheffers, Eds.), Balkema, Rotterdam, pp 65-71. Lick, W., and J. Lick, 1988: Aggregation and disaggregation of fine-grained lake sediments. J Great Lakes Res., 14, 514-523. Mehta, A. J., E. J. Hayter, W. R. Parker, R. B. Krone, A. M. Teeter, 1989: Cohesive sediment transport. I: Process description. J. Hyd. Engrg., 115, 1076-1093. Mehta, A. J., T. M. Parchure, J. G. Dixit, and R. Ariathurai, 1982: Resuspension potential of deposited cohesive sediment beds, in Estuarine Comparisons, V. S. Kennedy, Ed., Academic Press, New York, 348-362.

Mehta, A. J., and F. Jiang, 1990: Some field observations on bottom mud motion due to waves. Coastal and Oeanographic Enginnering Dept., University of Florida, Gainsville, FL.



---PAGE-109---



Mellor, G. L., and T. Yamada, 1982: Development of a turbulence closure model for geophysical fluid problems. Rev. Geophys. Space Phys., 20, 851-875.

Meyer-Peter, E. and R. Muller, 1948: Formulas for bed-load transport. Proc. Int. Assoc. Hydr. Struct. Res., Report of Second Meeting, Stockholm, 39-64.

Middleton, G. V., and P. R. Wilcock, 1994: Mechanics in the Earth and Environmental Sciences. Cambridge University Press, Cambridge, UK.

Moustafa, M. Z., and J. M. Hamrick, 2000: Calibration of the wetland hydrodynamic model to the Everglades nutrient removal project. Water Quality and Ecosystem Modeling, 1, 141-167.

Nielsen, P., 1992: Coastal bottom boundary layers and sediment transport, World Scientific, Singapore.

Park, K., A. Y. Kuo, J. Shen, and J. M. Hamrick, 1995: A three-dimensional hydrodynamic-eutrophication model (HEM3D): description of water quality and sediment processes submodels. The College of William and Mary, Virginia Institute of Marine Science. Special Report 327, 113 pp.

Rahmeyer, W. J., 1999: Lecture notes for CEE5560/6560: Sedimentation Engineering, Dept. of Civil and Environmental Engineering, Utah State University, Logan, Utah.

Rahuel, J. L., F. M. Holly, Jr., J. P. Chollet, P. J. Belleudy, 1990: Modeling riverbed evolution for bedload sediment mixtures. J. Hyd. Engrg., 115, 1521-1542.

Raukivi, A. J., 1990: Loose boundary hydraulics. 3rd Ed. Pergamon, New York, NY. Ried, I., and L. E. Frostick, 1994: Fluvial sediment transport and deposition. in Sediment Transport and Depositional Processes, K. Pye, ed., Blackwell, Oxford, UK, 89-155.

Roberts, J., R. Jepson, D. Gotthard, and W. Lick, 1998: Effects of particle size and bulk density on erosion of quartz particles. J. Hyd. Engrg., 124, 1261-1267.

Shen, J., J. D. Boon, and A. Y. Kuo, 1999: A modeling study of a tidal intrusion front and its impact on larval dispersion in the James River estuary, Virginia. Estuaries, 22, 681692.

Shen, J. and A.Y. Kuo. 1999: Numerical investigation of an estuarine front and its associated topographic eddy. J. Waterway, Port, Coastal Ocean Engrg., 125, 127-135.

Shrestha, P. A., and G. T. Orlob, 1996: Multiphase distribution of cohesive sediments and heavy metals in estuarine systems. J. Environ. Engrg., 122, 730-740.



---PAGE-110---



Smagorinsky, J., 1963: General circulation experiments with the primative equations, Part I: the basic experiment. Mon. Wea. Rev., 91, 99-152.

Smith, J. D., and S. R. McLean, 1977: Spatially averaged flow over a wavy bed. J. Geophys. Res., 82, 1735-1746.

Smolarkiewicz, P. K., and T. L. Clark, 1986: The multidimensional positive definite advection transport algorithm: further development and applications. J. Comp. Phys., 67, 396-438.

Smolarkiewicz, P. K., and W. W. Grabowski, 1990: The multidimensional positive definite advection transport algorithm: nonoscillatory option. J. Comp. Phys., 86, 355375.

Spasojevic, M., and F. M. Holly, Jr., 1990: 2-D bed evolution in natural watercoursesnew simulation approach. J. Hyd. Engrg., 116, 425-443.

Spasojevic, M., and F. M. Holly, Jr., 1994: Three-dimensional numerical simulation of mobile-bed hydrodynamics. Contract Report HL-94-2, US Army Engineer Waterways Experiment Station, Vicksburg, MS.

Stark, T. D., 1996: Program documentation and users guide: PSDDF primary consolidation, secondary compression, and desiccation of dredge fill. Instructional Report EL-96-xx, US Army Engineer Waterways Experiment Station, Vicksburg, MS.

Styles, R. and S. M. Glenn, 2000: Modeling stratified wave and current boundary layers on the continental shelf. J. Geophys. Res., 105, 24,119-24,139.

Suzuki, K., H. Yamamoto, and A. Kadota, 1998: Mechanism of bed load fluctuations of sand-gravel mixture in a steep slope channel, Proc. of the 11th congress of APD IAHR, Yogyakarta, pp.679-688.

Tsai, C. H., S. Iacobellis, and W. Lick, 1987: Floccualtion fo fine-grained lake sediments due to a uniform shear stress. J Great Lakes Res., 13, 135-146.

van Niekerk, A., K. R. Vogel, R. L Slingerland, and J. S. Bridge, 1992: Routing of heterogeneous sedimetns over movable bed: Model development. J. Hyd. Engrg., 118, 246-262.

- Van Rijin, L. C., 1984a: Sediment transport, Part I: Bed load transport. J. Hyd. Engrg., 110, 1431-1455.
- Van Rijin, L. C., 1984b: Sediment transport, Part II: Suspended load transport. J. Hyd. Engrg., 110, 1613-1641.




---PAGE-111---



Villaret, C., and M. Paulic, 1986: Experiments on the erosion of deposited and placed cohesive sediments in an annular flume and a rocking flume. Coastal and Oeanographic Enginnering Dept., University of Florida, Report UFL/COEL-86/007, Gainsville, FL.

Vogel, K. R., A. van Niekerk, R. L Slingerland, and J. S. Bridge, 1992: Routing of heterogeneous sedimetns over movable bed: Model verification. J. Hyd. Engrg., 118, 263-279.

Wu, W., S. S. Y. Wang, and Y. Jia, 2000: Nonuniform sediment transport in alluvial rivers. J. Hyd. Res., 38, 427-434.

Yang, C. T., 1973: Incipient motion and sediment transport. J. Hyd. Div. ASCE, 99, 16791704.

Yang, C. T., 1984: Unit stream power equation for gravel. Journal of Hydraulic Engineering, 110, 1783-1797.

Yang, C. T., and A. Molinas, 1982: Sediment transport and unit streams power function. J. Hyd. Div. ASCE, 108, 774-793.

Yang, Z., A. Baptista, and J. Darland, 2000: Numerical modeling of flow characteristics in a rotating annular flume. Dyn. Atmos. Oceans, 31, 271-294.

- Ziegler, C. K., and B. Nesbitt, 1994: Fine-grained sediment transport in Pawtuxet River, Rhode Island. J. Hyd. Engrg., 120, 561-576.
- Ziegler, C. K., and B. Nesbitt, 1995: Long-term simulation of fine-grained sediment transport in large reservoir. J. Hyd. Engrg., 121, 773-781.


