<<<PAGE 1>>>

# EFDC+ Computer Implementation Guide

Release 8.5.0

## DSI, LLC

Jan 27, 2020

<<<PAGE 2>>>

### CONTENTS:

##### 1 Introduction 1

- 1.1 Getting Started . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1

- 1.1.1 Build Instructions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
- 1.1.2 Running . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3


- 1.2 Cartesian Grid Generator User Guide . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

- 1.2.1 Generate Uniform Grid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
- 1.2.2 Generate Radial Grid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
- 1.2.3 Generate Telescoping Grid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
- 1.2.4 Import Grids from Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


- 1.3 Input Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

- 1.3.1 Primary Run Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
- 1.3.2 Required Spatial Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
- 1.3.3 General Transport . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
- 1.3.4 Sediment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
- 1.3.5 Wave Parameter Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
- 1.3.6 Eutrophication Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
- 1.3.7 Toxics Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
- 1.3.8 Temperature Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73


- 1.4 Output Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73

- 1.4.1 Output Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
- 1.4.2 GetEFDC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74


- 1.5 Sample Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

- 1.5.1 Lake 2D Test Case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
- 1.5.2 Ohio River Test Case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
- 1.5.3 Lake Washington Test Case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79


- 1.6 License . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80


##### i

<<<PAGE 3>>>

CHAPTER

### ONE

### INTRODUCTION

One of the purposes of this guide is to provide users and developers information about how to build, run, and develop the EFDC+ code. Additionally, there will be discussion on how to setup a basic EFDC+ model and post process the results. Finally, several sample EFDC+ models will be provided.

### 1.1 Getting Started

The EFDC+ source code and associated utilities can be access by cloning the repository from the EFDC+ GitHub repository. From the command line execute the following:

git clone https://github.com/dsi-llc/EFDCPlus After cloning the EFDC+ repository the folders listed below will be available under the root directory. EFDC - Contains source code to build EFDC+, sample executables for different build options. NetCDFLib - Necessary library ﬁles for building EFDC+ so it can write NetCDF ﬁles out. GridGenerator - Contains the executable for the simple Grid Generator for EFDC+ GetEFDC - Contains source code for building utility that helps extract EFDC+ formatted binary time series data. WASP - Provides some ﬁles necessary for linkage with the WASP code (advanced user feature). SampleModels - Contains several sample EFDC+ models. docs - Contains the computer implementation guide and the theory documentation for EFDC+.

#### 1.1.1 Build Instructions

Building EFDC+ from the source code is most easily carried out with Visual Studio (VS). The Intel Fortran compiler is the preferred compiler and the most tested for building EFDC+. The simplest build method is to open the VS solution ﬁle that comes with the source code. The solution ﬁle is located in the root directory of the EFDC folder and will have the ‘.sln’ extension. The following discussion assumes the user is running Windows 7 (or greater) and has access to Visual Studio 2015 (or greater). These tools have been most throughly tested. However, it is likely that EFDC+ can be built with other versions of the Intel compiler and Visual Studio.

In addition to the source code, pre-built executables are available under each of the following folders:

- • EFDC/DebugSP64/
- • EFDC/ReleaseDP64/
- • EFDC/ReleaseSP/
- • EFDC/ReleaseSP64/


##### 1

<<<PAGE 4>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



Next, the differences in each of the build conﬁgurations will be explained.

##### Build Conﬁgurations

The different build conﬁgurations are managed by VS. Visual studio provides a convenient way for maintaining different build conﬁgurations for the same project. The build conﬁgurations can be inspected by clicking the Project tab in the top of VS and selecting properties. Each of the build conﬁgurations is listed below:

- • DEBUG SP
- • DEBUG SP 64
- • DEBUG DP
- • DEBUG DP 64
- • Release SP
- • Release SP 64
- • Release DP
- • Release DP 64


For each of the bulleted build conﬁgurations listed above, if 64 is not speciﬁed, the executables is assumed to be compiled for a 32 bit system. The table below explains the shorthand used to signify the differences in build conﬁgurations.

|SP|Single Precision|
|---|---|
|DP|Double Precision|
|64|64 bit compilation|


##### OpenMP Compilation

Compilation of EFDC+ with OpenMP allows multithreading, which typical results in a reduction of the total calculation time. The build conﬁguration requires specifying several things in the VS Properties page. These settings are already conﬁgured in the builds provided. However, the details are given below in case a user wants to make modiﬁcations or use an OpenMP library besides Intel’s.

Under: Fortran\Preprocessor

|OpenMP Conditional Compilation|Yes|
|---|---|


Under: Fortran\Preprocessor

|Process OpenMP Directives|Generate Parallel Code (/Qopenmp)|
|---|---|


Under: Fortran\Libraries

|Runtime Library|Multithreaded DLL (/libs.dll /threads)|
|---|---|


Under: Linker\Input

|Additional Dependencies<br><br>|libiomp5md.lib|
|---|---|


Below is a summary of the Intel compiler suite and Visual Studio versions that are known to work.

##### 1.1. Getting Started 2



<<<PAGE 5>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### Intel Compiler Versions Tested

- • Intel 15
- • Intel 19.3
- • Intel 19.4


##### Visual Studio Versions Tested

- • 2015
- • 2019 (Preview 4)


#### 1.1.2 Running

Running EFDC+ on a local computer can be done in several different ways. By far the simplest way is to use the EFDC Explorer. The EFDC Explorer is a Graphical User Interface (GUI) that allows EFDC+ models to be visualized and run with ease. Details on the EFDC Explorer can be found here. Alternatively, the EFDC executable can be run through the command prompt or using a batch script.

For this discussion it is assumed the user is not using the EFDC Explorer.

##### Execution Options

- • Serial: EFDC+ can be run simply on a single core of a user’s desktop. No special compilation is required for this option.
- • Multithreaded: If the executable was compiled with OpenMP libraries, multiple cores on a single machine may be utilized.


##### Multithreading with OpenMP

With the advent of Intel processors with multiple cores, various technologies have been employed to take advantage of this increased computational power. With DSI’s knowledge of the EFDC+ code and its structure, the approach selected to apply multi-threading to EFDC was OpenMP.

Additionally, Intel has implemented Hyper-Threading for their multi-core implementation. This allows a program to utilize two threads for each physical core.

Tip: Since two threads share a single core, for computationally intensive applications, only using the number of threads equal to the number of cores provides the best throughput

##### 1.1. Getting Started 3



<<<PAGE 6>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### OpenMP Performance

The performance of the different routines within EFDC+ using OpenMP is highlighted in the ﬁgure below.

It is DSI’s commitment that the EFDC_DSI_OMP models produce exactly the same results regardless of how many threads are used. Model comparisons demonstrate model differences are equal to zero i.e. model results are exactly the same, within model precision.

##### Executing and EFDC+ Run

Once an EFDC+ executable is available, it can be run directly through the command prompt or through simple batch script. A sample of batch script is given below:

|SET KMP_AFFINITY=granularity=fine,compact,1,0 TITLE Sample Title of the Problem CD "C:\Path\To\WorkingDirectory\" "C:\Path\To\Exectuable\EFDCPlus.exe" -NT2 -NOP|
|---|


Each line the script is described in greater detail below.

- • SET KMP_AFFINITY=granularity=ﬁne,compact,1,0 - Speciﬁes an environment variable that binds OpenMP threads to physical processing units. This generally gives the best performance. For additional information on what this environment variable is doing, go to this article, written by Intel.
- • TITLE: A title is optional but can be helpful if you are running multiple calculations at the same time. This title will show up at the top of the command prompt.
- • CD: This command precedes the location of your Working Directory, which is the folder containing your EFDC+ inputs.
- • The path to the location of the executable must be known and speciﬁed in the script.


##### 1.1. Getting Started 4



<<<PAGE 7>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



- • -NT2: This command line argument after the executable speciﬁes the number of threads to use. In this case only 2 are requested, but one could easily specify 3,4,5, etc. to run more threads.


Important: Do not specify a number of threads greater than the number of logical cores available on your computer.

##### Output Screen

The EFDC+ end of run screen contains the CPU usage for the run. The CPU usage is reported as the Total CPU/# Cores. This statistic is best for interpreting impacts to run times. A sample of an output screen is given below.

### 1.2 Cartesian Grid Generator User Guide

A simple GUI has been provided to help generate and visualize EFDC+ grids. Additionally, this grid generator can write out the basic input ﬁle necessary for running EFDC+. Next, an overview of how to use this grid generator will be provided.

To launch the grid generator open the GridGenerator.exe executable under the folder GridGenerator.

The interface of the tool is shown in Figure 1. To create a grid, the user can click File then select New Model or click the grid symbol from the interface as shown in Figure 2.

##### 1.2. Cartesian Grid Generator User Guide 5



<<<PAGE 8>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



###### Figure 1. Cartesian Grid Generator Interface.

###### Figure 2. Create a New Model.** The Grid Generator form will be displayed as shown in Figure 3.

##### 1.2. Cartesian Grid Generator User Guide 6



<<<PAGE 9>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



- Figure 3. Grid Options.


There are three options for generating a new grid and one option for importing existing grid ﬁles. The options are: Generate Uniform Grid, Generate Radial Grid, Generate Telescoping Grid, and Import Grid from Files. Each of these options is described below:

#### 1.2.1 Generate Uniform Grid

This option allows user to generate a Cartesian grid. When the radial button for this option is selected, the Uniform Grid Options frame is shown. In this frame the user needs to enter the Lower-Left and Upper-Right coordinates, these two corner points will temporarily limit the grid domain. Next, enter cell size in X and Y directions, which will deﬁne cell dimensions (width and length in meters of a cell), then click the calculator symbol for Number of Cells, the number of cells will be updated. Another option is that the user enters the number of cells desired ﬁrst then click the calculator symbol for Cell Size, and the dimensions of the cell will be updated.

Rotation Angle: The user should enter angle in degrees which for the grid should be rotated. UTM Zone: This is the Universal Transverse Mercator (UTM) zone, the user can enter the zone number, from 1 to 60. The user can then click the Generate button, and the grid will appear on the right window as shown in Figure 4.

##### 1.2. Cartesian Grid Generator User Guide 7



<<<PAGE 10>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



The user can also change the size of the domain by holding left-mouse click (LMC) on navigation points (P1, P2, P3, P4) and shifting to another place in the window. The values of ﬁelds of the Uniform Grid Options frame are updated as well.

To save the information entered into the Uniform Grid Options frame select the Save Parameters button. A Save As form will be displayed in order to enter a ﬁle name, then click the Save button to save as shown in Figure 5. This parameter settings ﬁle can be reused at another time by clicking on the Load Param button.

- Figure 4. Generate Uniform Grid.

- Figure 5. Save parameters.


To restrict the size of the domain use a bounding polygon, which is effectively serves as a shoreline. RMC on the Bounding Polygons text box and select Add Files. The Open form appears, and the user should select the ﬁle or ﬁles

##### 1.2. Cartesian Grid Generator User Guide 8



<<<PAGE 11>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



needs then click Open button as shown in Figure 6.

The polygon will be loaded and the Lower-Left, Upper-Right coordinates will be updated. The user now can generate a grid based on either cell size or the number of cells by clicking the Generate button. It is also possible inverse the selection, or remove the cells which are outside of the bounding polygon, by clicking the Remove Dry button as shown in Figure 7.

- Figure 6. Load bounding polygon ﬁle.

- Figure 7. Grid generation by using bounding polygon.


##### 1.2. Cartesian Grid Generator User Guide 9



<<<PAGE 12>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



Once the grid is generated, the user can save the grid by clicking the Export Grid button. The grid can be exported as

*.CVL or *.GRD format. Click the OK button to ﬁnish generating the uniform grid.

After clicking OK button, the tool returns to the interface shown in Figure 1. Select the disk symbol or Save Model under File from the interface to save an EFDC+ model for this grid as shown in Figure 8. The ﬁles that saved are shown in Figure 9 and can be loaded by EE10.

- Figure 8. Save EFDC Model for generated grid.

- Figure 9. Files of EFDC Model save out.


##### 1.2. Cartesian Grid Generator User Guide 10



<<<PAGE 13>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



#### 1.2.2 Generate Radial Grid

When you select the Generate Radial Grid from Grid Option frame, the default values are ﬁlled in the Radial Grid Options frame as shown in Figure 10. The user can deﬁne those values as required.

The user can then click the Generate button, and the grid will appear on the right window as shown in Figure 10. Export the generated grid and save the EFDC model in same way described in the section, Generate Uniform Grid.

Figure 10. Generate Radial Grid.

#### 1.2.3 Generate Telescoping Grid

When you select Generate Telescoping Grid from Grid Option frame, the default values are ﬁlled in to the Telescoping Grid frame as shown in Figure 11. The user can deﬁne those values as required.

Select the Generate button, and the grid will be displaye in the window as shown in Figure 11. Export the generated grid and save the EFDC model as described in Generate Uniform Grid above.

##### 1.2. Cartesian Grid Generator User Guide 11



<<<PAGE 14>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



- Figure 11. Generate Telescoping Grid.


- 1.2.4 Import Grids from Files This option allows user to import an existing grid ﬁle. Grid ﬁle formats that are supported include:


- • CVLGrid: DSI’s curvilinear orthogonal grid generator - CVL Grid information
- • RGFGrid: Deltares grid generator
- • Grid95
- • DXDY/LYLY: EFDC+ grid descriptors
- • ECOMSED:
- • SEAGRID
- • CH3D: Army Corp of Engineers model
- • Corners: ﬁle containing coordinates of four corners of each cell


The user should click the Import Grids radial button, and the Import Grid form will be displayed. From here the user should select the grid type from the drop-down list of Grid types as shown in Figure 12, then click the Browse button to browse to the grid ﬁle, and click OK.

In the case that there are a number of sub-grids for a water body, the Multiple grid ﬁles option needs to be checked, then the user may browse to the folder containing the grid ﬁles. To select multiple grid ﬁles at same time, hold the Ctrl key and select the grid ﬁles then click the OK button to load grid ﬁles (see Figure 13 and Figure 14).

Save the EFDC model in the same way described in section Generate Uniform Grid.

##### 1.2. Cartesian Grid Generator User Guide 12



<<<PAGE 15>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



###### Figure 12 Import from a grid ﬁle.

###### Figure 13. Import from multiple grid ﬁles – ﬁle selection.

##### 1.2. Cartesian Grid Generator User Guide 13



<<<PAGE 16>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



- Figure 14. Import from multiple grid ﬁles – result display.


Note that the user should update the UTM Zone to the correct value before clicking the OK button to generate a new model. The UTM Zone is not used for model computation but it is important for coordinate conversion, exporting to GIS formats, and writing NetCDF outputs.

### 1.3 Input Files

This section lists and describes the input ﬁles required to run different modules within EFDC+. The primary modules within EFDC+ are distinguished in the ﬁgure below.

##### 1.3. Input Files 14



<<<PAGE 17>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



#### 1.3.1 Primary Run Control

The run control ﬁles contain options to specify calculation types, time step sizes, output options, and other related controls. The most important of these ﬁles is the efdc.inp ﬁle and will be explained in detail later on.

|Input File<br><br>|Description|
|---|---|
|efdc.inp|Master EFDC+ control ﬁle|
|show.inp|Model run time reporting options|
|efdcwin.inp|Simpliﬁed control (deprecated)|


##### Restart Related Files

The restart ﬁles allow an EFDC+ calculation to start up from a speciﬁed time step part way through a calculation. Use of these ﬁles may be necessary if a calculation ended prematurely and a user wishes to restart from the last saved time step.

|Input File|File Description|
|---|---|
|restart.inp|hydrodynamic restart|
|rstwd.inp<br><br>|wetting & drying|
|temp.rst<br><br>|bed temperature restart|
|wqwcrst.inp|water quality restart|
|wqsdrst.inp<br><br>|sediment diagenesis restart ﬁle|
|wqrpemrst.inp<br><br>|rooted plant & epiphyte|


##### EFDC.INP

The efdc.inp ﬁle is extensive and speciﬁes all options for running a calculation. Historically, the options were organized by card types. As such, each card description and input parameter is given below. Each of these cards is placed in a single efdc.inp ﬁle and read in by EFDC+ at run time.

Note, when creating and efdc.inp ﬁle a line starting with * or - will be ignored and interpretted as a comment.

##### card1

|****************************************************************************** C1 RUN TITLE<br><br>* TEXT DESCRIPTION UP TO 80 CHARACTERS IN LENGTH FOR THIS INPUT FILE AND<br><br>˓→RUN C1 TITLE EFDC+ Sample input<br><br>-----------------------------------------------------------------------------<br><br>˓→-<br><br>C1A GRID CONFIGURATION AND TIME INTEGRATION MODE SELECTION<br><br>*<br><br>* IS2TIM: 0 THREE-TIME LEVEL INTEGRATION<br>* 1 TWO-TIME LEVEL INTEGRATION<br><br>*<br><br>* IGRIDH: NOT USED<br><br>*<br><br>* IGRIDV: 0 STANDARD SIGMA VERTICAL GRID OR SINGLE LAYER DEPTH ˓→AVERAGE<br><br><br>|
|---|


(continues on next page)

##### 1.3. Input Files 15



<<<PAGE 18>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



(continued from previous page)

|* 1 SIGMA-ZED (SGZ) VERTICAL LAYERING ALLOWING VARYING ˓→LAYERS FOR EACH CELL (DSI)<br><br>* 2 SIGMA-ZED (SGZ) VERTICAL GRID USING HORIZONTALLY UNIFORM ˓→LAYER THICKNESS (DSI)<br><br>* SGZMin: MINIMUM NUMBER OF LAYERS FOR SIGMA-ZED<br>* SGZHPDelta: TYPICAL RISE OF WATER ABOVE THE INITIAL CONDITIONS WHEN ˓→IGRIDV>0 (M)<br><br><br>* C1A IS2TIM IGRIDH IGRIDV SGZMin SGZHPDelta|
|---|


##### card2

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C2 RESTART, GENERAL CONTROL AND DIAGNOSTIC SWITCHES<br><br>*<br><br>* ISRESTI: 1 FOR READING INITIAL CONDITIONS FROM FILE restart.inp<br>* -1 AS ABOVE BUT ADJUST FOR CHANGING BOTTOM ELEVATION<br>* 10 FOR READING IC'S FROM restart.inp WRITTEN BEFORE 8 SEPT 92<br><br>*<br><br>* ISRESTO: -1 FOR WRITING RESTART FILE restart.out AT END OF RUN<br>* N INTEGER.GE.0 FOR WRITING restart*.out EVERY N REF TIME PERIODS<br>* ISRESTR: 1 FOR WRITING RESIDUAL TRANSPORT FILE RESTRAN.OUT<br>* ISGREGOR: 0/1 NOT USE/USE DATE STAMPED RESTART FILES<br>* ICONTINUE: RUN CONTINUATION OPTION FOR EE LINKAGE FILES WHEN ISRESTI=1<br>* 0 NO RUN CONTINUATION - EFDC WRITES EE_*.OUT FILES AS USUAL<br>* 1 ACTIVATE RUN CONTINUATION - EE LINKAGE OUTPUT WILL BE ˓→APPENDED TO THE EXISTING FILES<br><br>* ISLOG: 1 FOR WRITING LOG FILE EFDC.LOG<br>* IDUM: NOT USED<br><br>* *<br><br>* ISDIVEX: 1 FOR WRITING EXTERNAL MODE DIVERGENCE TO SCREEN<br>* ISNEGH: 1 FOR SEARCHING FOR NEGATIVE DEPTHS AND WRITING TO SCREEN<br>* ISMMC: <0 FLAG TO GLOBALLY ACTIVATE WRITING EXTRA MODEL RESULTS LOG ˓→FILES<br><br><br>*<br><br>* ISBAL: 1 FOR ACTIVATING MASS, MOMENTUM AND ENERGY BALANCES AND<br>* WRITING RESULTS TO FILE bal.out<br>* IDUM: NOT USED<br>* ISHOW: >0 TO SHOW RUNTIME STATUS ON SCREEN, SEE INSTRUCTIONS FOR FILE ˓→SHOW.INP<br><br><br>* C2 ISRESTI ISRESTO ISRESTR ISGREGOR ISLOG ISDIVEX ISNEGH ISMMC ISBAL<br><br>˓→ICONTINUE ISHOW|
|---|


##### 1.3. Input Files 16



<<<PAGE 19>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card3

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C3 EXTERNAL MODE SOLUTION OPTION PARAMETERS AND SWITCHES<br><br>*<br><br>* RP: OVER RELAXATION PARAMETER<br>* RSQM: TARGET SQUARE RESIDUAL OF ITERATIVE SOLUTION SCHEME<br>* ITERM: MAXIMUN NUMBER OF ITERATIONS<br>* IRVEC: 0 CONJUGATE GRADIENT SOLUTION - NO SCALING<br>* 9 CONJUGATE GRADIENT SOLUTION - SCALE BY MINIMUM DIAGONAL<br>* 99 CONJUGATE GRADIENT SOLUTION - SCALE TO NORMAL FORM<br><br>* *<br><br>* IATMP: 0 DO NOT USE ATMOSPHERIC PRESSURE IN THE CALPUV SOLUTION<br>* 1 USE ATMOSPHERIC PRESSURE IN THE CALPUV SOLUTION IF NASER > 1<br>* IWDRAG: 0 USE ORIGINAL EFDC WIND DRAG FORMULATION<br>* 1 USE ORIGINAL EFDC WIND DRAG FORMULATION WITH RELATIVE WATER ˓→VELOCITY CORRECTION<br><br>* 2 HERSBACH 2011, EUROPEAN CENTRE FOR MEDIUM-RANGE WEATHER ˓→FORECASTS (ECMWF)<br><br>* 3 USE SIMPLIFIED COARE 3.6 APPROACH AT NEUTRAL ATM AND RELATIVE ˓→WATER VELOCITY CORRECTION<br><br>* DUMMY:<br>* ITERHPM: NOT USED<br>* IDRYCK: ITERATIONS PER DRYING CHECK (ISDRY.GE.1) 2.LE.IDRYCK.LE.20<br>* ISDSOLV: 1 TO WRITE DIAGNOSTICS FILES FOR EXTERNAL MODE SOLVER<br>* FILT3TL: FILTER COEFFICIENT FOR 3 TIME LEVEL EXPLICIT ( 0.0625 )<br><br><br>* C3 RP RSQM ITERM IRVEC IATMP IWDRAG DUMMY ITERHPM IDRYCK<br><br>˓→ISDSOLV FILT3TL|
|---|


##### card4

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C4 LONGTERM MASS TRANSPORT INTEGRATION ONLY SWITCHES<br><br>*<br><br>* ISLTMT: NOT USED<br>* ISSSMMT: 0 WRITES MEAN MASS TRANSPORT TO RESTRAN.OUT AFTER EACH<br>* AVERAGING PERIOD (FOR WASP/ICM/RCA LINKAGE)<br>* 1 WRITES MEAN MASS TRANSPORT TO RESTRAN.OUT AFTER LAST<br>* AVERAGING PERIOD (FOR RESEARCH PURPOSES)<br>* 2 DISABLES MEAN MASS TRANSPORT FIELD CALCULATIONS & RESTRAN.OUT<br>* ISLTMTS: NOT USED<br>* ISIA: NOT USED<br>* RPIA: NOT USED<br>* RSQMIA: NOT USED<br>* ITRMIA: NOT USED<br>* ISAVEC: NOT USED<br><br><br>* C4 ISLTMT ISSSMMT ISLTMTS ISIA RPIA RSQMIA ITRMIA ISAVEC|
|---|


##### 1.3. Input Files 17



<<<PAGE 20>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card5

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C5 MOMENTUM ADVEC AND HORIZ DIFF SWITCHES AND MISC SWITCHES<br><br>*<br><br>* ISCDMA: 1 FOR CENTRAL DIFFERENCE MOMENTUM ADVECTION (USED FOR 3TL ONLY)<br>* 0 FOR UPWIND DIFFERENCE MOMENTUM ADVECTION (USED FOR 3TL ONLY)<br>* 2 FOR EXPERIMENTAL UPWIND DIFF MOM ADV (FOR RESEARCH PURPOSES)<br>* ISHDMF: 1 TO ACTIVE HORIZONTAL MOMENTUM DIFFUSION<br>* 2 TO ACTIVE HORIZONTAL MOMENTUM DIFFUSION WITH WATER COLUMN ˓→DIFFUSION<br><br>* ISDISP: 1 CALCULATE MEAN HORIZONTAL SHEAR DISPERSION TENSOR OVER LAST ˓→MEAN MASS TRANSPORT AVERAGING PERIOD<br><br>* ISWASP: 4 OR 5 TO WRITE FILES FOR WASP4 OR WASP5 MODEL LINKAGE, 17˓→WASP7HYDRO, 99 - CE-QUAL-ICM<br>* ISDRY: 0 NO WETTING & DRYING OF CELLS ALLOWED<br>* 11 CONSTANT DRYING DEPTH SPECIFIED BY HDRY ON CARD 11<br>* WITH NONLINEAR ITERATIONS<br>* 99 VARIABLE WETTING & DRYING DEPTHS USING CELL FACE MASKING<br>* AND NONLINEAR ITERATIONS, USING HDRY AS THE NOMINAL DRY DEPTH<br>* ISQQ: 1 TO USE STANDARD TURBULENT INTENSITY ADVECTION SCHEME<br>* ISRLID: 1 TO RUN IN RIGID LID MODE (NO FREE SURFACE)<br>* ISVEG: 1 TO IMPLEMENT VEGETATION RESISTANCE<br>* 2 IMPLEMENT WITH DIAGNOSTICS TO FILE CBOT.LOG<br>* ISVEGL: 1 TO INCLUDE LAMINAR FLOW OPTION IN VEGETATION RESISTANCE<br>* ISITB: 1 FOR IMPLICIT BOTTOM & VEGETATION RESISTANCE IN EXTERNAL MODE<br><br>*<br><br>* IHMDSUB: 1 TO USE A SUBSET OF CELLS FOR HMD CALCULATIONS, MAPHMD.INP<br>* IINTPG: 0 ORIGINAL INTERNAL PRESSURE GRADIENT FORMULATION<br>* 1 JACOBIAN FORMULATION<br>* 2 FINITE VOLUME FORMULATION<br><br><br>* * C5 ISCDMA ISHDMF ISDISP ISWASP ISDRY ISQQ ISRLID ISVEG ISVEGL<br><br>˓→ ISITB IHMDSUB IINTPG|
|---|


##### card6

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C6 DISSOLVED AND SUSPENDED CONSTITUENT TRANSPORT SWITCHES<br><br>* TURB INTENSITY=0,SAL=1,TEM=2,DYE=3,SFL=4,TOX=5,SED=6,SND=7,CWQ=8<br><br>*<br><br>* ISTRAN: 1 OR GREATER TO ACTIVATE TRANSPORT<br>* ISTOPT: NONZERO FOR TRANSPORT OPTIONS, SEE USERS MANUAL<br>* ISCDCA: 0 FOR STANDARD DONOR CELL UPWIND DIFFERENCE ADVECTION (3TL ONLY)<br>* 1 FOR CENTRAL DIFFERENCE ADVECTION FOR THREE TIME LEVEL STEPS ˓→(3TL ONLY)<br><br>* 2 FOR EXPERIMENTAL UPWIND DIFFERENCE ADVECTION (FOR RESEARCH) ˓→(3TL ONLY)<br><br>* ISADAC: 1 TO ACTIVATE ANTI-NUMERICAL DIFFUSION CORRECTION TO<br>* STANDARD DONOR CELL SCHEME<br>* ISFCT: 1 TO ADD FLUX LIMITING TO ANTI-NUMERICAL DIFFUSION CORRECTION<br>* ISPLIT: 1 TO OPERATOR SPLIT HORIZONTAL AND VERTICAL ADVECTION<br>|
|---|


(continues on next page)

##### 1.3. Input Files 18



<<<PAGE 21>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* (FOR RESEARCH PURPOSES)<br>* ISADAH: 1 TO ACTIVATE ANTI-NUM DIFFUSION CORRECTION TO HORIZONTAL<br>* SPLIT ADVECTION STANDARD DONOR CELL SCHEME (FOR RESEARCH)<br>* ISADAV: 1 TO ACTIVATE ANTI-NUM DIFFUSION CORRECTION TO VERTICAL<br>* SPLIT ADVECTION STANDARD DONOR CELL SCHEME (FOR RESEARCH)<br>* ISCI: 1 TO READ CONCENTRATION FROM FILE restart.inp<br>* ISCO: 1 TO WRITE CONCENTRATION TO FILE restart.out<br><br><br>* C6 ISTRAN ISTOPT ISCDCA ISADAC ISFCT ISPLIT ISADAH ISADAV ISCI<br><br>˓→ ISCO|
|---|


##### card7

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C7 TIME-RELATED INTEGER PARAMETERS<br><br>*<br><br>* NTC: NUMBER OF REFERENCE TIME PERIODS IN RUN<br>* NTSPTC: NUMBER OF TIME STEPS PER REFERENCE TIME PERIOD<br>* NLTC: NUMBER OF LINEARIZED REFERENCE TIME PERIODS<br>* NLTC: NUMBER OF TRANSITION REF TIME PERIODS TO FULLY NONLINEAR<br>* NTCPP: NUMBER OF REFERENCE TIME PERIODS BETWEEN FULL PRINTED OUTPUT<br>* TO FILE EFDC.OUT<br>* NTSTBC: NUMBER OF TIME STEPS BETWEEN USING A TWO TIME LEVEL TRAPEZOIDAL<br>* CORRECTION TIME STEP, ** MASS BALANCE PRINT INTERVAL **<br>* NTCNB: NUMBER OF REFERENCE TIME PERIODS WITH NO BUOYANCY FORCING(NOT ˓→USED)<br><br>* NTCVB: NUMBER OF REF TIME PERIODS WITH VARIABLE BUOYANCY FORCING<br>* NTSMMT: NUMBER OF NUMBER OF TIME STEPS TO AVERAGE OVER TO OBTAIN<br>* MASS BALANCE RESIDUALS OR MEAN MASS TRANSPORT VARIABLES (e.g. ˓→WASP Linkage)<br><br>* NFLTMT: USE 1 (FOR RESEARCH PURPOSES)<br>* NDRYSTP: IF > 0 THEN NUMBER OF TIME STEPS BEFORE AN ISOLATED CELL WILL BE ˓→FORCED TO GO DRY<br><br>* EFDC+ WILL TRACK THE 'WASTED' WATER IN QDWASTE<br>* NRAMPUP: NUMBER OF INITIAL LOOPS TO HOLD TIMESTEP CONSTANT FOR DYNAMIC ˓→TIME-STEPPING<br><br>* NUPSTEP: MINIMUM NUMBER OF ITERATIONS FOR EACH TIME STEP WHEN GROWING ˓→DTDYN<br><br><br>* C7 NTC NTSPTC NLTC NTTC NTCPP NTSTBC NTCNB NTCVB NTSMMT<br><br>˓→NFLTMT NDRYSTP NRAMPUP NUPSTEP|
|---|


##### card8

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C8 TIME-RELATED REAL PARAMETERS<br><br>*<br><br>* TCON: CONVERSION MULTIPLIER TO CHANGE TBEGIN TO SECONDS<br>* TBEGIN: TIME ORIGIN OF RUN<br>* TREF: REFERENCE TIME PERIOD IN sec (i.e. 44714.16S OR 86400S)<br>|
|---|


(continues on next page)

##### 1.3. Input Files 19



<<<PAGE 22>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* CORIOLIS: CONSTANT CORIOLIS PARAMETER IN 1/sec =2*7.29E-5*SIN(LAT)<br>* ISCORV: 1 TO READ VARIABLE CORIOLIS COEFFICIENT FROM LXLY.INP FILE<br>* ISCCA: WRITE DIAGNOSTICS FOR MAX CORIOLIS-CURV ACCEL TO FILEEFDC.LOG<br>* ISCFL: 1 WRITE DIAGNOSTICS OF MAX THEORETICAL TIME STEP TO CFL.OUT<br>* GT 1 TIME STEP ONLY AT INTERVAL ISCFL FOR ENTIRE RUN<br>* ISCFLM: 1 TO MAP LOCATIONS OF MAX TIME STEPS OVER ENTIRE RUN<br>* DTSSFAC: DYNAMIC TIME STEPPING IF DTSSFAC > 0.0<br>* DTSSDHDT: DYNAMIC TIME STEPPING RATE OF DEPTH CHANGE FACTOR (USED WHEN > ˓→0)<br><br>* DTMAX: MAXIMUM TIME STEP FOR DYNAMIC STEPPING (SECONDS)<br><br><br>* C8 TCON TBEGIN TREF CORIOLIS ISCORV ISCCA ISCFL<br><br>˓→ISCFLM DTSSFAC DTSSDHDT DTMAX|
|---|


##### card9

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C9 SPACE-RELATED AND SMOOTHING PARAMETERS<br><br>*<br><br>* IC: NUMBER OF CELLS IN I DIRECTION<br>* JC: NUMBER OF CELLS IN J DIRECTION<br>* LC: NUMBER OF ACTIVE CELLS IN HORIZONTAL + 2<br>* LVC: NUMBER OF VARIABLE SIZE HORIZONTAL CELLS<br>* ISCO: 1 FOR CURVILINEAR-ORTHOGONAL GRID (LVC=LC-2)<br>* NDM: NUMBER OF DOMAINS FOR HORIZONTAL DOMAIN DECOMPOSITION<br>* ( NDM=1, FOR MODEL EXECUTION ON A SINGLE PROCESSOR SYSTEM OR<br>* NDM=MM*NCPUS, WHERE MM IS AN INTEGER AND NCPUS IS THE NUMBER<br>* OF AVAILABLE CPU'S FOR MODEL EXECUTION ON A PARALLEL ˓→MULTIPLE PROCESSOR SYSTEM )<br><br>* LDM: NUMBER OF WATER CELLS PER DOMAIN (LDM=(LC-2)/NDM, FOR MULTIPLE ˓→VECTOR PROCESSORS,<br><br>* LDM MUST BE AN INTEGER MULTIPLE OF THE VECTOR LENGTH OR<br>* STRIDE NVEC THUS CONSTRAINING LC-2 TO BE AN INTEGER MULTIPLE ˓→OF NVEC )<br><br>* ISMASK: 1 FOR MASKING WATER CELL TO LAND OR ADDING THIN BARRIERS<br>* USING INFORMATION IN FILE MASK.INP<br>* ISCONNECT: 1 FOR USER DEFINED N-S CONNECTION OF CELLS USING INFO IN FILE ˓→MAPPGNS.INP<br><br>* 2 FOR USER DEFINED E-W CONNECTION OF CELLS USING INFO IN FILE ˓→MAPPGEW.INP<br><br>* 3 FOR BOTH E-W AND N-S CONNECTIONS<br>* NSHMAX: NUMBER OF DEPTH SMOOTHING PASSES<br>* NSBMAX: NUMBER OF INITIAL SALINITY FIELD SMOOTHING PASSES<br>* WSMH: DEPTH SMOOTHING WEIGHT<br>* WSMB: SALINITY SMOOTHING WEIGHT<br><br><br>* * * C9 IC JC LC LVC ISCO NDM LDM ISMASK CONNECT<br><br>˓→NSHMAX NSBMAX WSMH WSMB|
|---|


##### 1.3. Input Files 20



<<<PAGE 23>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



- card10

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C10 LAYER THICKNESS IN VERTICAL<br><br>*<br><br>* K: LAYER NUMBER, K=1,KC<br>* DZC: DIMENSIONLESS LAYER THICKNESS (THICKNESSES MUST SUM TO 1.0)<br><br><br>* * * C10 K DZC|
|---|


- card11


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C11 GRID, ROUGHNESS AND DEPTH PARAMETERS<br><br>*<br><br>* DX: CARTESIAN CELL LENGTH IN X OR I DIRECTION<br>* DY: CARTESIAN CELL LENGTH IN Y OR J DIRECTION<br>* DXYCVT: MULTIPLY DX AND DY BY TO OBTAIN METERS<br>* IMDXDY: GREATER THAN 0 TO READ MODDXDY.INP FILE<br>* ZBRADJ: LOG BDRY LAYER CONST OR VARIABLE ROUGH HEIGHT ADJ IN METERS<br>* ZBRCVRT: LOG BDRY LAYER VARIABLE ROUGHNESS HEIGHT CONVERT TO METERS<br>* HMIN: MINIMUM DEPTH OF INPUTS DEPTHS IN METERS<br>* HADJ: ADJUSTMENT TO DEPTH FIELD IN METERS<br>* HCVRT: CONVERTS INPUT DEPTH FIELD TO METERS<br>* HDRY: DEPTH AT WHICH CELL OR FLOW FACE BECOMES DRY<br>* HWET: DEPTH AT WHICH WITHDRAWALS FROM CELL ARE TURNED OFF<br>* BELADJ: ADJUSTMENT TO BOTTOM BED ELEVATION FIELD IN METERS<br>* BELCVRT: CONVERTS INPUT BOTTOM BED ELEVATION FIELD TO METERS<br><br><br>* C11 DX DY DXYCVT IMD ZBRADJ ZBRCVRT HMIN HADJ HCVRT<br><br>˓→ HDRY HWET BELADJ BELCVRT|
|---|


- card11a


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C11A TWO-LAYER MOMENTUM FLUX AND CURVATURE ACCELERATION CORRECTION FACTORS<br><br>* (ONLY USED FOR 2 TIME LEVEL SOLUTION & ISDRY=0 PMC-Check to see if still ˓→true)<br><br>* ICK2COR: 0 NO CORRECTION<br>* ICK2COR: 1 CORRECTION USING CK2UUC,CK2VVC,CK2UVC FOR CURVATURE<br>* ICK2COR: 2 CORRECTION USING CK2FCX,CK2FCY FOR CURVATURE<br>* CK2UUM: CORRECTION FOR UU MOMENTUM FLUX<br>* CK2VVM: CORRECTION FOR UU MOMENTUM FLUX<br>* CK2UVM: CORRECTION FOR UU MOMENTUM FLUX<br>* CK2UUC: CORRECTION FOR UU CURVATURE ACCELERATION (NOT ACTIVE)<br>* CK2VVC: CORRECTION FOR VV CURVATURE ACCELERATION (NOT ACTIVE)<br>* CK2UVC: CORRECTION FOR UV CURVATURE ACCELERATION (NOT ACTIVE)<br>* CK2FCX: CORRECTION FOR X EQUATION CURVATURE ACCELERATION<br>|
|---|


(continues on next page)

##### 1.3. Input Files 21



<<<PAGE 24>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* CK2FCY: CORRECTION FOR Y EQUATION CURVATURE ACCELERATION<br>* C11A ICK2COR CK2UUM CK2VVM CK2UVM CK2UUC CK2VVC CK2UVC CK2FCX CK2FCY<br>|
|---|


- card11b


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C11B CORNER CELL BOTTOM STRESS CORRECTION OPTIONS (2TL ONLY)<br><br>*<br><br>* ISCORTBC: 1 TO CORRECT BED STRESS AVERAGING TO CELL CENTERS IN CORNERS<br>* 2 TO USE SPATIALLY VARYING CORRECTION FOR CELLS IN CORNERC.INP<br>* ISCORTBCD: 1 WRITE DIAGNOSTICS EVERY NSPTC TIME STEPS (NOT USED)<br>* FSCORTBC: CORRECTION FACTOR, 0.0 GE FSCORTBC LE 1.0<br>* 1.0 = NO CORRECTION, 0.0 = MAXIMUM CORRECTION, 0.5 SUGGESTED<br><br><br>* C11B ISCORTBC ISCORTBCD FSCORTBC|
|---|


- card12


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C12 TURBULENT DIFFUSION PARAMETERS<br><br>*<br><br>* AHO: CONSTANT HORIZONTAL MOMENTUM AND MASS DIFFUSIVITY m*m/s<br>* AHD: DIMESIONLESS HORIZONTAL MOMENTUM DIFFUSIVITY (ONLY FOR ISHDMF>0)<br>* AVO: BACKGROUND, CONSTANT OR EDDY (KINEMATIC) VISCOSITY m*m/s<br>* ABO: BACKGROUND, CONSTANT OR MOLECULAR DIFFUSIVITY m*m/s<br>* AVMX: MAXIMUM KINEMATIC EDDY VISCOSITY m*m/s (DS-INTL)<br>* ABMX: MAXIMUM EDDY DIFFUSIVITY m*m/s (DS-INTL)<br>* VISMUD: CONSTANT FLUID MUD VISCOSITY m*m/s<br>* AVCON: EQUALS ZERO FOR CONSTANT VERTICAL VISCOSITY AND DIFFUSIVITY<br>* WHICH ARE SET EQUAL TO AVO AND ABO, OTHERWISE SET TO 1.0<br>* ZBRWALL: SIDE WALL LOG LAW ROUGHNESS HEIGHT. USED WHEN HORIZONTAL<br>* MOMENTUM DIFFUSION IS ACTIVE AND AHO OR AHD ARE NONZERO<br><br><br>* C12 AHO AHD AVO ABO AVMX ABMX VISMUD<br><br>˓→ AVCON ZBRWALL|
|---|


- card12a


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C12A TURBULENCE CLOSURE OPTIONS<br><br>*<br><br>* ISSTAB: 0 FOR GALPERIN et al. STABILITY FUNCTIONS IN CALAVBOLD ˓→(ISQQ=1)<br><br>* 1 FOR GALPERIN et al. STABILITY FUNCTIONS ˓→(ISQQ=1)<br><br>* 2 FOR KANTHA AND CLAYSON (1994) STABILITY FUNCTIONS ˓ (ISQQ=1)<br><br><br>|
|---|


→ (continues on next page)

##### 1.3. Input Files 22



<<<PAGE 25>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* 3 FOR KANTHA (2003) STABILITY FUNCTIONS ˓→(ISQQ=1)<br><br>* (NOTE: OPTION SELECTED HERE OVERRIDES ISTOPT(0) ON C6)<br>* 4 VINCON-LEITE, ET.AL. (2014) APPROACH ˓→(ISQQ=1)<br><br>* ISSQL: 0 SETS QQ AND QQL STABILITY FUNCTIONS PROPORTIONAL TO<br>* MOMENTUM STABILITY FUNCTIONS (EXCEPT FOR ISSTAB=3)<br>* 1 SETS QQ AND QQL STABILITY FUNCTIONS TO CONSTANTS<br>* (FOR ISSTAB = 0,1,2) THIS OPTION NOT ACTIVE<br>* ISAVBMX: SET TO 1 TO ACTIVATE MAX VISCOSITY AND DIFFUSIVITY OF AVMX ˓→AND ABMX<br><br>* ISFAVB: SET TO 1 OR 2 TO AVG OR SQRT FILTER AVO AND AVB<br>* ISINWV: SET TO 2 TO WRITE EE_ARRAYS.OUT<br>* ISLLIM: 0 FOR NO LENGTH SCALE AND RIQMAX LIMITATIONS<br>* 1 LIMIT RIQMAX IN STABILITY FUNCTION ONLY<br>* 2 DIRECTLY LIMIT LENGTH SCALE AND LIMIT RIQMAX IN STABILITY ˓→FUNCTION<br><br>* IFPROX: 0 FOR NO WALL PROXIMITY FUNCTION<br>* 1 FOR PARABOLIC OVER DEPTH WALL PROXIMITY FUNCTION<br>* 2 FOR OPEN CHANNEL WALL PROXIMITY FUNCTION<br>* XYRATIO: LARGE ASPECT RATIOS, IF XYRATIO>1.1 AND >DX:DY THEN ZERO XY ˓→TERMS FMDUY AND FMDVX (EFDC+)<br><br>* BC_EDGEFACTOR: BOUNDARY CELLS MOMENTUM CORRECTION FACTOR (0 TO 1)<br><br><br>* C12A ISSTAB ISSQL ISAVBMX ISFAVB ISINWV ISLLIM IFPROX XYRATIO BC_<br><br>˓→EDGEFACTOR|
|---|


##### card13

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C13 TURBULENCE CLOSURE PARAMETERS<br><br>*<br><br>* VKC: VON KARMAN CONSTANT<br>* CTURB1: TURBULENT CONSTANT (UNIVERSAL)<br>* CTURB2: TURBULENT CONSTANT (UNIVERSAL)<br>* CTE1: TURBULENT CONSTANT (UNIVERSAL)<br>* CTE2: TURBULENT CONSTANT (UNIVERSAL)<br>* CTE3: TURBULENT CONSTANT (UNIVERSAL)<br>* CTE4: TURBULENCE CONSTANT E4 (SOMETIMES CALL E3) WALL FUNCTION IN Q*Q*L ˓→EQUATION<br><br>* CTE5: TURBULENCE CONSTANT E5 - 2ND OPEN CHANNEL WALL FUNCTION IN Q*Q*L ˓→EQUATION<br><br>* RIQMAX: MAXIMUM TURBULENT INTENSITY RICHARDSON NUMBER FOR STABLE ˓→CONDITIONS<br><br>* QQMIN: MINIMUM TURBULENT INTENSITY SQUARED<br>* QQLMIN: MINIMUM TURBULENT INTENSITY SQUARED * LENGTH-SCALE<br>* DMLMIN: MINIMUM DIMENSIONLESS LENGTH SCALE<br><br><br>* C13 VKC CTURB1 CTURB2 CTE1 CTE2 CTE3 CTE4 CTE5 RIQMAX<br><br>˓→ QQMIN QQLMIN DMLMIN|
|---|


##### 1.3. Input Files 23



<<<PAGE 26>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



- card14


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C14 TIDAL & ATMOSPHERIC FORCING, GROUND WATER AND SUBGRID CHANNEL PARAMETERS<br><br>*<br><br>* MTIDE: NUMBER OF PERIOD (TIDAL) FORCING CONSTITUENTS<br>* NWSER: NUMBER OF WIND TIME SERIES (0 SETS WIND TO ZERO)<br>* NASER: NUMBER OF ATMOSPHERIC CONDITION TIME SERIES (0 SETS ALL ZERO)<br>* ISGWIT: 0 DISABLE GROUND WATER<br>* 1 TO ACTIVATE SOIL MOISTURE BALANCE WITH DRYING AND WETTING<br>* 2 TO ACTIVATE GROUNDWATER INTERACTION WITH BED AND WATER ˓→COLUMN (GWMAP & GWSER)<br><br>* 3 TO ZONED TEMPORALLY CONSTANT IN(+)/OUT(-) SEEPAGE RATE (M/ ˓→S) (GWSEEP & GWMAP)<br>* ISCHAN: >0 ACTIVATE SUBGRID CHANNEL MODEL AND READ MODCHAN.INP<br>* ISWAVE: 1-FOR BOUNDARY LAYER IMPACTS ONLY (WAVEBL.INP),<br>* 2-FOR BOUNDARY LAYER & CURRENT IMPACTS (WVnnn.INP)<br>* 3-FOR INTERNALLY COMPUTED WIND WAVE BOUNDARY LAYER IMPACTS ˓→(DSI)<br><br>* 4-FOR INTERNALLY COMPUTED WIND WAVE BOUNDARY LAYER AND ˓→CURRENT IMPACTS (DSI)<br><br>* ITIDASM: 1 FOR TIDAL ELEVATION ASSIMILATION (NOT ACTIVE)<br>* ISPERC: 1 TO PERCOLATE OR ELIMINATE EXCESS WATER IN DRY CELLS<br>* ISBODYF: TO INCLUDE EXTERNAL MODE BODY FORCES FROM FBODY.INP<br>* 1 FOR UNIFORM OVER DEPTH, 2 FOR SURFACE LAYER ONLY<br>* ISPNHYDS: 1 FOR QUASI-NONHYDROSTATIC OPTION<br><br><br>* C14 MTIDE NWSER NASER ISGWIT ISCHAN ISWAVE ITIDASM ISPERC ISBODYF<br><br>˓→ISPNHYDS|
|---|


- card14a


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C14C TIME & SPACE VARYING FORCING<br><br>*<br><br>* INTERGER FLAGS: 0 NOT USE TIME & SPACE VARYING DATA FILE<br>* 1 READ FROM AN ASCII FILE *FLD.INP<br>* 2 READ FROM A BINARY FILE *FLD.FLD<br><br>*<br><br>* ITOPO: TOPOGRAPHIC UPDATES (E.G., DREDGING/DUMPING, LAND ˓→RECLAIMATION)<br><br>* IROUG: BOTTOM ROUGHNESS (E.G., SEASONAL ROUGHNESS)<br>* IVEGE: VEGETATION (E.G., SEASONAL VEGETATION)<br>* ISEEP: GROUNDWATER/SEEPAGE<br>* IWIND: WIND (CYCLONES)<br>* IPRES: BAROMETRIC PRESSURE (CYCLONES)<br>* ISHEL: WIND SHELTER<br>* ISHAD: ATMOSPHERIC SHADING<br>* IRAIN: RAINFALL<br>* IEVAP: EVAPORATION<br>* ISNFL: SNOW FALL<br>* ISNTK: SNOW THICKNESS<br>* IICTK: ICE THICKNESS<br>|
|---|


(continues on next page)

##### 1.3. Input Files 24



<<<PAGE 27>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* ZLJER: SEDZLJ EROSION RATE<br>* C14C ITOPO IROUG IVEGE ISEEP IWIND IPRES IRAIN IEVAP ISHEL<br><br><br>˓→ ISHAD ISNFL ISNTK IICTK ZLJER|
|---|


##### card15

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C15 PERIODIC FORCING (TIDAL) CONSTITUENT SYMBOLS AND PERIODS<br><br>*<br><br>* SYMBOL: FORCING SYMBOL (CHARACTER VARIABLE) FOR TIDES, THE NOS SYMBOL<br>* PERIOD: FORCING PERIOD IN SECONDS<br><br><br>* C15 SYMBOL PERIOD|
|---|


##### card16

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C16 SURFACE ELEVATION OR PRESSURE BOUNDARY CONDITION PARAMETERS<br><br>*<br><br>* NPBS: NUMBER OF SURFACE ELEVATION OR PRESSURE BOUNDARY CONDITIONS<br>* CELLS ON SOUTH OPEN BOUNDARIES<br>* NPBW: NUMBER OF SURFACE ELEVATION OR PRESSURE BOUNDARY CONDITIONS<br>* CELLS ON WEST OPEN BOUNDARIES<br>* NPBE: NUMBER OF SURFACE ELEVATION OR PRESSURE BOUNDARY CONDITIONS<br>* CELLS ON EAST OPEN BOUNDARIES<br>* NPBN: NUMBER OF SURFACE ELEVATION OR PRESSURE BOUNDARY CONDITIONS<br>* CELLS ON NORTH OPEN BOUNDARIES<br>* NPFOR: NUMBER OF HARMONIC FORCINGS<br>* NPFORT: FORCING TYPE, 0=CONSTANT, 1=LINEAR, 2= QUADRATIC VARIATION<br>* NPSER: NUMBER OF TIME SERIES FORCINGS<br>* PDGINIT: ADD THIS CONSTANT ADJUSTMENT GLOBALLY TO THE SURFACE ELEVATION<br><br><br>* C16 NPBS NPBW NPBE NPBN NPFOR NPFORT NPSER PDGINIT|
|---|


##### card17

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C17 PERIODIC FORCING (TIDAL) SURF ELEV OR PRESSURE BOUNDARY COND. FORCINGS<br><br>*<br><br>* NPFOR: FORCING NUMBER<br>* SYMBOL: FORCING SYMBOL (FOR REFERENCE HERE ONLY)<br>* AMPLITUDE: AMPLITUDE IN M (PRESSURE DIVIDED BY RHO*G), NPFORT=0<br>* COSINE AMPLITUDE IN M, NPFORT.GE.1<br>* PHASE: FORCING PHASE RELATIVE TO TBEGIN IN SECONDS, NPFORT=0<br>* SINE AMPLITUDE IN M, NPFORT.GE.1<br>* NOTE: FOR NPFORT=0 SINGLE AMPLITUDE AND PHASE ARE READ, FOR NPFORT=1<br>|
|---|


(continues on next page)

##### 1.3. Input Files 25



<<<PAGE 28>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* CONST AND LINEAR COS AND SIN AMPS ARE READ FOR EACH FORCING, FOR<br>* NPFORT=2, CONST, LINEAR, QUAD COS AND SIN AMPS ARE READ FOR EACH<br>* FOR EACH FORCING<br><br><br>* C17 NPFOR SYMBOL AMPLITUDE PHASE|
|---|


##### card18

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C18 PERIODIC FORCING (TIDAL) SURF ELEV OR PRESSURE ON SOUTH OPEN BOUNDARIES<br><br>* IPBS: I CELL INDEX OF BOUNDARY CELL<br>* JPBS: J CELL INDEX OF BOUNDARY CELL<br>* ISPBS: 0 FOR ELEVATION SPECIFIED<br>* 1 FOR RADIATION-SEPARATION CONDITION, ZERO TANGENTIAL VELOCITY<br>* 2 FOR RADIATION-SEPARATION CONDITION, FREE TANGENTIAL VELOCITY<br>* 3 FOR ELEVATION SPECIFIED, FREE TANGENTIAL VELOCITY<br>* NPFORS: APPLY HARMONIC FORCING NUMBER NPFORS<br>* NPSERS: APPLY TIME SERIES FORCING NUMBER NPSERS<br>* NPSERS1: APPLY TIME SERIES FORCING NUMBER NPSERS1 FOR 2ND SERIES (NPFORT. ˓→GE.1)<br>* TPCOORDS: TANGENTIAL COORDINATE ALONG BOUNDARY (NPFORT. ˓→GE.1)<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C18 IPBS JPBS ISPBS NPFORS NPSERS GRPID ! ID|
|---|


##### card19

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C19 PERIODIC FORCING (TIDAL) SURF ELEV OR PRESSURE ON WEST OPEN BOUNDARIES<br><br>*<br><br>* IPBW: SEE CARD 18<br>* JPBW:<br>* ISPBW:<br>* NPFORW:<br>* NPSERW:<br>* TPCOORDW:<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C19 IPBW JPBW ISPBW NPFORW NPSERW GRPID ! ID|
|---|


##### 1.3. Input Files 26



<<<PAGE 29>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card20

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C20 PERIODIC FORCING (TIDAL) SURF ELEV OR PRESSURE ON EAST OPEN BOUNDARIES<br><br>*<br><br>* IPBE: SEE CARD 18<br>* JPBE:<br>* ISPBE:<br>* NPFORE:<br>* NPSERE:<br>* TPCOORDE:<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C20 IPBE JPBE ISPBE NPFORE NPSERE GRPID ! ID|
|---|


##### card21

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C21 PERIODIC FORCING (TIDAL) SURF ELEV OR PRESSURE ON NORTH OPEN BOUNDARIES<br><br>*<br><br>* IPBN: SEE CARD 18<br>* JPBN:<br>* ISPBN:<br>* NPFORN:<br>* NPSERN:<br>* TPCOORDN:<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C21 IPBN JPBN ISPBN NPFORN NPSERN GRPID ! ID|
|---|


##### card22

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C22 SPECIFY NUM OF SEDIMENT AND TOXICS AND NUM OF CONCENTRATION TIME SERIES<br><br>*<br><br>* NDYE: NUMBER OF DYE CLASSES (DEFAULT = 1)<br>* NTOX: NUMBER OF TOXIC CONTAMINANTS (DEFAULT = 1)<br>* NSED: NUMBER OF COHESIVE SEDIMENT SIZE CLASSES (DEFAULT = 1)<br>* NSND: NUMBER OF NON-COHESIVE SEDIMENT SIZE CLASSES (DEFAULT = 1)<br>* NCSER1: NUMBER OF SALINITY TIME SERIES<br>* NCSER2: NUMBER OF TEMPERATURE TIME SERIES<br>* NCSER3: NUMBER OF DYE CONCENTRATION TIME SERIES<br>* NCSER4: NUMBER OF SHELLFISH LARVAE CONCENTRATION TIME SERIES<br>* NCSER5: NUMBER OF TOXIC CONTAMINANT CONCENTRATION TIME SERIES<br>* EACH TIME SERIES MUST HAVE DATA FOR NTOX TOXICANTS<br>* NCSER6: NUMBER OF COHESIVE SEDIMENT CONCENTRATION TIME SERIES<br>* EACH TIME SERIES MUST HAVE DATA FOR NSED COHESIVE SEDIMENTS<br>* NCSER7: NUMBER OF NON-COHESIVE SEDIMENT CONCENTRATION TIME SERIES<br>* EACH TIME SERIES MUST HAVE DATA FOR NSND NON-COHESIVE SEDIMENTS<br>* ISSBAL: SET TO 1 FOR SEDIMENT MASS BALANCE<br>|
|---|


(continues on next page)

##### 1.3. Input Files 27



<<<PAGE 30>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* C22 NDYE NTOX NSED NSND NCSER1 NCSER2 NCSER3 NCSER4 NCSER5<br><br>˓→NCSER6 NCSER7 ISSBAL|
|---|


##### card22b

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C22B Shellfish<br><br>* * C22B NSF ISFFARM NSFCELLS|
|---|


##### card23

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C23 VELOCITY, VOLUME SOURCE/SINK, FLOW CONTROL, AND WITHDRAWAL/RETURN DATA<br><br>*<br><br>* NQSIJ: NUMBER OF CONSTANT AND/OR TIME SERIES SPECIFIED SOURCE/SINK<br>* LOCATIONS (RIVER INFLOWS,ETC) .<br>* NQJPIJ: NUMBER OF CONSTANT AND/OR TIME SERIES SPECIFIED SOURCE<br>* LOCATIONS TREATED AS JETS/PLUMES .<br>* NQSER: NUMBER OF VOLUME SOURCE/SINK TIME SERIES<br>* NQCTL: NUMBER OF PRESSURE CONTROLLED WITHDRAWAL/RETURN PAIRS<br>* NQCTLT: NUMBER OF PRESSURE CONTROLLED WITHDRAWAL/RETURN TABLES<br>* NHYDST: NUMBER OF HYDRAULIC STRUCTURE DEFINITIONS<br>* NQWR: NUMBER OF CONSTANT OR TIME SERIES SPECIFIED WITHDRAWAL/RETURN<br>* PAIRS<br>* NQWRSR: NUMBER OF TIME SERIES SPECIFYING WITHDRAWAL,RETURN AND<br>* CONCENTRATION RISE SERIES<br>* ISDIQ: SET TO 1 TO WRITE DIAGNOSTIC FILE, DIAQ.OUT<br>* NQCTLSER: NUMBER OF GATE OPENING TIME-SERIES FOR HYDRAULIC STRUCTURE ˓→CONTROL<br><br>* NQCRULES: NUMBER OF OPERATIONAL RULES FOR HYDRAULIC STRUCTURE CONTROL<br><br><br>* C23 NQSIJ NQJPIJ NQSER NQCTL NQCTLT NHYDST NQWR NQWRSR ISDIQ<br><br>˓→NQCTLSER NQCRULES|
|---|


##### card24

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C24 VOLUMETRIC SOURCE/SINK LOCATIONS, MAGNITUDES, AND CONCENTRATION SERIES<br><br>*<br><br>* IQS: I CELL INDEX OF VOLUME SOURCE/SINK<br>* JQS: J CELL INDEX OF VOLUME SOURCE/SINK<br>* QSSE: CONSTANT INFLOW/OUTFLOW RATE IN (m^3/s)<br>* NQSMUL: MULTIPLIER SWITCH FOR CONSTANT AND TIME SERIES VOL S/S<br>* = 0 MULT BY 1. FOR NORMAL IN/OUTFLOW (L*L*L/T)<br>|
|---|


(continues on next page)

##### 1.3. Input Files 28



<<<PAGE 31>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* = 1 MULT BY DY FOR LATERAL IN/OUTFLOW (L*L/T) ON U FACE<br>* = 2 MULT BY DX FOR LATERAL IN/OUTFLOW (L*L/T) ON V FACE<br>* = 3 MULT BY DX+DY FOR LATERAL IN/OUTFLOW (L*L/T) ON U&V FACES<br>* NQSMF: IF NON ZERO ACCOUNT FOR VOL S/S MOMENTUM FLUX (NEGATIVE VALUES ˓→REVERSE FLOW DIRECTION)<br><br>* = 1 MOMENTUM FLUX ON WEST U FACE<br>* = 2 MOMENTUM FLUX ON SOUTH V FACE<br>* = 3 MOMENTUM FLUX ON EAST U FACE<br>* = 4 MOMENTUM FLUX ON NORTH V FACE<br>* IQSERQ: ID NUMBER OF ASSOCIATED VOLUME FLOW TIME SERIES<br>* ICSER1: ID NUMBER OF ASSOCIATED SALINITY TIME SERIES<br>* ICSER2: ID NUMBER OF ASSOCIATED TEMPERATURE TIME SERIES<br>* ICSER3: ID NUMBER OF ASSOCIATED DYE CONC TIME SERIES<br>* ICSER4: ID NUMBER OF ASSOCIATED SHELL FISH LARVAE RELEASE TIME SERIES<br>* ICSER5: ID NUMBER OF ASSOCIATED TOXIC CONTAMINANT CONC TIME SERIES<br>* ICSER6: ID NUMBER OF ASSOCIATED COHESIVE SEDIMENT CONC TIME SERIES<br>* ICSER7: ID NUMBER OF ASSOCIATED NON-COHESIVE SED CONC TIME SERIES<br>* QWIDTH: WIDTH OF THE DISCHARGE FOR FOR MOMENTUM FLUX (M)(NQSMF /= 0)<br>* QSFACTOR: FRACTION OF TIME SERIES FLOW NQSERQ ASSIGNED TO THIS CELL<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C24 IQS JQS QSSE NQSMUL NQSMF IQSERQ ICSER1 ICSER2<br><br>˓→ICSER3 ICSER4 ICSER5 ICSER6 ICSER7 QWIDTH QSFACTOR GRPID ! ID|
|---|


##### card25

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C25 TIME CONSTANT INFLOW CONCENTRATIONS FOR TIME CONSTANT VOLUMETRIC SOURCES<br><br>*<br><br>* SAL: SALT CONCENTRATION CORRESPONDING TO INFLOW ABOVE<br>* TEM: TEMPERATURE CORRESPONDING TO INFLOW ABOVE<br>* DYE: DYE CONCENTRATION CORRESPONDING TO INFLOW ABOVE<br>* SFL: SHELL FISH LARVAE CONCENTRATION CORRESPONDING TO INFLOW ABOVE<br>* TOX: NTOX TOXIC CONTAMINANT CONCENTRATIONS CORRESPONDING TO<br>* INFLOW ABOVE WRITTEN AS TOXC(N), N=1,NTOX A SINGLE DEFAULT<br>* VALUE IS REQUIRED EVEN IF TOXIC TRANSPORT IS NOT ACTIVE<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C25 SAL TEM DYE1 SFL GRPID ! ID<br><br>0 20 0 0 1 ! Chehalis River<br>0 20 0 0 2 ! Humptulips River<br>|
|---|


##### card26

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C26 TIME CONSTANT INFLOW CONCENTRATIONS FOR TIME CONSTANT VOLUMETRIC SOURCES<br><br>*<br><br>* SED: NSED COHESIVE SEDIMENT CONCENTRATIONS CORRESPONDING TO<br>* INFLOW ABOVE WRITTEN AS SEDC(N), N=1,NSED. I.E., THE FIRST<br>* NSED VALUES ARE COHESIVE A SINGLE DEFAULT VALUE IS REQUIRED<br>|
|---|


(continues on next page)

##### 1.3. Input Files 29



<<<PAGE 32>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* EVEN IF COHESIVE SEDIMENT TRANSPORT IS INACTIVE<br>* SND: NSND NON-COHESIVE SEDIMENT CONCENTRATIONS CORRESPONDING TO<br>* INFLOW ABOVE WRITTEN AS SND(N), N=1,NSND. I.E., THE LAST<br>* NSND VALUES ARE NON-COHESIVE. A SINGLE DEFAULT VALUE IS<br>* REQUIRED EVEN IF NON-COHESIVE SEDIMENT TRANSPORT IS INACTIVE<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C26 SED1 SED2 SED3 SED4 SED5 SED6 SED7<br><br>˓→ SED8 GRPID ! ID (8 SEDS + 0 SNDS)<br><br>100 100 0 0 0 0 0<br><br>˓→ 0 1 ! Chehalis River 100 100 0 0 0 0 0<br><br>˓→ 0 2 ! Humptulips River<br>|
|---|


##### card27

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C27 JET/PLUME SOURCE LOCATIONS, GEOMETRY AND ENTRAINMENT PARAMETERS<br><br>*<br><br>* ID: ID COUNTER FOR JET/PLUME<br>* ICAL: 0 BYPASS, 1 ACTIVE (NORMAL - TOTAL LAYER FLOW AT DIFFUSER), 2 - W/ ˓→R (USE W/R SERIES)<br>* IQJP: I CELL INDEX OF JET/PLUME<br>* JQJP: J CELL INDEX OF JET/PLUME<br>* KQJP: K CELL INDEX OF JET/PLUME (DEFAULT, QJET=0 OR JET COMP DIVERGES)<br>* NPORT: NUMBER OF IDENTICAL PORTS IN THIS CELL<br>* XJET: LOCAL EAST JET LOCATION RELATIVE TO DISCHARGE CELL CENTER (m) (NOT ˓→USED)<br><br>* YJET: LOCAL NORTH JET LOCATION RELATIVE TO DISCHARGE CELL CENTER (m)(NOT ˓→USED)<br><br>* ZJET: ELEVATION OF DISCHARGE (m)<br>* PHJET: VERTICAL JET ANGLE POSITIVE FROM HORIZONTAL (DEGREES)<br>* THJET: HORIZONTAL JET ANGLE POS COUNTER CLOCKWISE FROM EAST (DEGREES)<br>* DJET: DIAMETER OF DISCHARGE PORT (m)<br>* CFRD: ADJUSTMENT FACTOR FOR FROUDE NUMBER<br>* DJPER: ENTRAINMENT ERROR CRITERIA<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C27 ID ICAL IQJP JQJP KQJP NPORT XJET YJET ZJET<br><br>˓→ PHJET THJET DJET CFRD DJPER GRPID ! ID|
|---|


##### card28

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C28 JET/PLUME SOLUTION CONTROL AND OUTPUT CONTROL PARAMETERS<br><br>*<br><br>* ID: ID COUNTER FOR JET/PLUME<br>* NJEL: MAXIMUM NUMBER OF ELEMENTS ALONG JET/PLUME LENGTH<br>* NJPMX: MAXIMUM NUMBER OF ITERATIONS<br>* ISENT: 0 USE MAXIMUM OF SHEAR AND FORCED ENTRAINMENT<br>|
|---|


(continues on next page)

##### 1.3. Input Files 30



<<<PAGE 33>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* 1 USE SUM OF SHEAR AND FORCED ENTRAINMENT<br>* ISTJP: 0 STOP AT SPECIFIED NUMBER OF ELEMENTS<br>* 1 STOP WHEN CENTERLINE PENETRATES BOTTOM OR SURFACE<br>* 2 STOP WITH BOUNDARY PENETRATES BOTTOM OR SURFACE<br>* NUDJP: FREQUENCY FOR UPDATING JET/PLUME (NUMBER OF TIME STEPS)<br>* IOJP: 1 FOR FULL ASCII, 2 FOR COMPACT ASCII OUTPUT AT EACH UPDATE<br>* 3 FOR FULL AND COMPACT ASCII OUTPUT, 4 FOR BINARY OUTPUT<br>* IPJP: NUMBER OF SPATIAL PRINT/SAVE POINT IN VERTICAL<br>* ISDJP: 1 WRITE DIAGNOSTICS TO JPLOG__.OUT<br>* IUPJP: I INDEX OF UPSTREAM WITHDRAWAL CELL IF ICAL=2<br>* JUPJP: J INDEX OF UPSTREAM WITHDRAWAL CELL IF ICAL=2<br>* KUPJP: K INDEX OF UPSTREAM WITHDRAWAL CELL IF ICAL=2<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C28 ID NJEL NJPMX ISENT ISTJP NUDJP IOJP IPJP ISDJP<br><br>˓→ IUPJP JUPJP KUPJP GRPID ! ID|
|---|


##### card29

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C29 JET/PLUME SOURCE PARAMETERS AND DISCHARGE/CONCENTRATION SERIES IDS<br><br>*<br><br>* ID: ID COUNTER FOR JET/PLUME<br>* QQJP: CONSTANT JET/PLUME FLOW RATE IN (m^3/s)<br>* FOR ICAL = 1 OR 2 (FOR SINGLE PORT)<br>* NQSERJP: ID NUMBER OF ASSOCIATED VOLUME FLOW TIME SERIES<br>* NQWRSERJP: ID NUMBER OF ASSOCIATED WITHDRAWAL-RETURN TIME SERIES (ICAL=2)<br>* ICSER1: ID NUMBER OF ASSOCIATED SALINITY TIME SERIES<br>* ICSER2: ID NUMBER OF ASSOCIATED TEMPERATURE TIME SERIES<br>* ICSER3: ID NUMBER OF ASSOCIATED DYE CONC TIME SERIES<br>* ICSER4: ID NUMBER OF ASSOCIATED SHELL FISH LARVAE RELEASE TIME SERIES<br>* ICSER5: ID NUMBER OF ASSOCIATED TOXIC CONTAMINANT CONC TIME SERIES<br>* ICSER6: ID NUMBER OF ASSOCIATED COHESIVE SEDIMENT CONC TIME SERIES<br>* ICSER7: ID NUMBER OF ASSOCIATED NON-COHESIVE SED CONC TIME SERIES<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C29 ID QQJP NQSERJP NQWRSERJP ICSER1 ICSER2 ICSER3 ICSER4 ICSER5<br><br>˓→ICSER6 ICSER7 GRPID ! ID|
|---|


##### card30

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C30 TIME CONSTANT INFLOW CONCENTRATIONS FOR TIME CONSTANT JET/PLUME SOURCES<br><br>*<br><br>* SAL: SALT CONCENTRATION CORRESPONDING TO INFLOW ABOVE<br>* TEM: TEMPERATURE CORRESPONDING TO INFLOW ABOVE<br>* DYE: DYE CONCENTRATION CORRESPONDING TO INFLOW ABOVE<br>* SFL: SHELL FISH LARVAE CONCENTRATION CORRESPONDING TO INFLOW ABOVE<br>* TOX: NTOX TOXIC CONTAMINANT CONCENTRATIONS CORRESPONDING TO<br>* INFLOW ABOVE WRITTEN AS TOXC(N), N=1,NTOX A SINGLE DEFAULT<br>|
|---|


(continues on next page)

##### 1.3. Input Files 31



<<<PAGE 34>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* VALUE IS REQUIRED EVEN IF TOXIC TRANSPORT IS NOT ACTIVE<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C30 SAL TEM DYE1 SFL GRPID ! ID|
|---|


##### card31

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C31 TIME CONSTANT INFLOW CONCENTRATIONS FOR TIME CONSTANT JET/PLUME SOURCES<br><br>*<br><br>* SED: NSED COHESIVE SEDIMENT CONCENTRATIONS CORRESPONDING TO<br>* INFLOW ABOVE WRITTEN AS SEDC(N), N=1,NSED. I.E., THE FIRST<br>* NSED VALUES ARE COHESIVE A SINGLE DEFAULT VALUE IS REQUIRED<br>* EVEN IF COHESIVE SEDIMENT TRANSPORT IS INACTIVE<br>* SND: NSND NON-COHESIVE SEDIMENT CONCENTRATIONS CORRESPONDING TO<br>* INFLOW ABOVE WRITTEN AS SND(N), N=1,NSND. I.E., THE LAST<br>* NSND VALUES ARE NON-COHESIVE. A SINGLE DEFAULT VALUE IS<br>* REQUIRED EVEN IF NON-COHESIVE SEDIMENT TRANSPORT IS INACTIVE<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C31 SED1 SED2 SED3 SED4 SED5 SED6 SED7<br><br>˓→ SED8 GRPID ! ID (8 SEDS + 0 SNDS)|
|---|


##### card32

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C32 SURFACE ELEV OR PRESSURE DEPENDENT FLOW INFORMATION<br><br>*<br><br>* IQCTLU: I INDEX OF UPSTREAM OR WITHDRAWAL CELL<br>* JQCTLU: J INDEX OF UPSTREAM OR WITHDRAWAL CELL<br>* IQCTLD: I INDEX OF DOWNSTREAM OR RETURN CELL<br>* JQCTLD: J INDEX OF DOWNSTREAM OR RETURN CELL<br>* NQCTYP: FLOW CONTROL TYPE<br>* = -2 FLOW AS FUNCTION OF UPSTREAM ELEVATION RATING CURVE OF A ˓→GROUP OF CELLS<br><br>* = -1 FLOW AS FUNCTION OF UPSTREAM DEPTH (STAGE RATING CURVE)<br>* = 0 FLOW AS FUNCTION OF ELEVATION OR PRESSURE DIFFERENCE TABLE<br>* = 1 SAME AS 0 WITH ACCELERATING FLOW (E.G. TIDAL INLET)<br>* = 2 FLOW DERIVED FROM UPSTREAM AND DOWNSTREAM WS ELEVATIONS<br>* = 3 LOWER CHORD OPTION USING UPSTREAM DEPTH WHEN WSEL > ˓→BQCLCE<br><br>* = 4 LOWER CHORD OPTION USING ELEVATION DIFFERENCE WHEN WSEL > ˓→BQCLCE<br><br>* = 5 CULVERT<br>* = 6 SLUICE GATE<br>* = 7 WEIR<br>* = 8 ORIFICE<br>* = 9 FLOATING SKIMMER WALL (NOT AVAILABLE)<br>* = 10 SUBMERGED WEIR (NOT AVAILABLE)<br>* NQCTLQ: ID NUMBER OF CONTROL CHARACTERIZATION TABLE<br>|
|---|


(continues on next page)

##### 1.3. Input Files 32



<<<PAGE 35>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* NQCMUL: MULTIPLIER SWITCH FOR FLOWS FROM UPSTREAM CELL<br>* = 0 MULT BY 1. FOR CONTROL TABLE IN (L*L*L/T)<br>* = 1 MULT BY DY FOR CONTROL TABLE IN (L*L/T) ON U FACE<br>* = 2 MULT BY DX FOR CONTROL TABLE IN (L*L/T) ON V FACE<br>* = 3 MULT BY DX+DY FOR CONTROL TABLE IN (L*L/T) ON U&V FACES<br>* HQCTLU: OFFSET FOR UPSTREAM HEAD (m)<br>* SET TO CELL'S BOTTOM ELEVATION TO USE ELEVATION INSTEAD OF ˓→DEPTH FOR NQCTYP = -1 or 3<br><br>* HQCTLD: OFFSET FOR DOWNSTREAM HEAD (m)<br>* QTCLMU: MULTIPLIER TO SPLIT THE TOTAL QCTL RATING TABLE INTO CELL ˓→SPECIFIC FLOWS [ONLY USED IF NQCTYP = -2]<br><br>* QTCLGRP: NUMBER IDENTIFIER TO ASSOCIATE PHYSICALLY BASED FLOW GROUPS ˓→ [ONLY USED IF NQCTYP = -2]<br><br>* BQCLCE: LOWER CHORD ELEVATION (m) [ONLY ˓→USED IF NQCTYP = 3 OR 4]<br><br>* NQCMINS: MINIMUM NUMBER OF STEPS REQUIRED ABOVE LOWER CHORD [ONLY ˓→USED IF NQCTYP = 3 OR 4]<br><br><br>*<br><br>* *** LOOKUP TABLE HEAD DETERMINATION (HUP & HDW) FOR LOW CHORD<br>* *** NQCTYP = 3: HUP = HP(LU) + HCTLUA(NCTLT) + HQCTLU(NCTL)<br>* *** NQCTYP = 4: HUP = HP(LU) + BELV(LU) + HCTLUA(NCTLT) + ˓→HQCTLU(NCTL)<br><br>* *** NQCTYP = 4: HDW = HP(LD) + BELV(LD) + HCTLDA(NCTLT) + ˓→HQCTLD(NCTL)<br><br><br>*<br><br>*HS_FACTOR: DISCHARGE DISTRIBUTION FACTOR (ONLY USED FOR NQCTYP>4)<br>*HS_NTIMES: NUMBER OF TIMES HYDRAULIC STRUCTURE DEFINITION CHANGES ˓→(IN DEVELOPMENT)<br><br>*HS_TRANSITION: NUMBER OF SECONDS TO TRANSITION FROM TIME (T) TO TIME (T+1) ˓→(IN DEVELOPMENT)<br><br>*GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C32 IQCTLU JQCTLU IQCTLD JQCTLD NQCTYP NQCTLQ NQCMUL HQCTLU HQCTLD<br><br>˓→QTCLMU QTCLGRP BQCLCE NQCMINS FACTOR NTIMES TRANSIT GRPID ! ID|
|---|


##### card33

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C33 FLOW WITHDRAWAL, HEAT OR MATERIAL ADDITION, AND RETURN DATA<br><br>*<br><br>* IWRU: I INDEX OF UPSTREAM OR WITHDRAWAL CELL<br>* JWRU: J INDEX OF UPSTREAM OR WITHDRAWAL CELL<br>* KWRU: K INDEX OF UPSTREAM OR WITHDRAWAL LAYER<br>* IWRD: I INDEX OF DOWNSTREAM OR RETURN CELL<br>* JWRD: J INDEX OF DOWNSTREAM OR RETURN CELL<br>* KWRD: J INDEX OF DOWNSTREAM OR RETURN LAYER<br>* QWRE: CONSTANT VOLUME FLOW RATE FROM WITHDRAWAL TO RETURN<br>* NQWRSERQ: ID NUMBER OF ASSOCIATED VOLUME WITHDRAWAL-RETURN FLOW AND<br>* CONCENTRATION RISE TIME SERIES<br>* NQWRMFU: IF NON ZERO ACCOUNT FOR WITHDRAWAL FLOW MOMENTUM FLUX<br>* = 1 MOMENTUM FLUX ON WEST U FACE<br>* = 2 MOMENTUM FLUX ON SOUTH V FACE<br>* = 3 MOMENTUM FLUX ON EAST U FACE<br>|
|---|


(continues on next page)

##### 1.3. Input Files 33



<<<PAGE 36>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* = 4 MOMENTUM FLUX ON NORTH V FACE<br>* NQWRMFD: IF NON ZERO ACCOUNT FOR RETURN FLOW MOMENTUM FLUX<br>* = 1 MOMENTUM FLUX ON WEST U FACE<br>* = 2 MOMENTUM FLUX ON SOUTH V FACE<br>* = 3 MOMENTUM FLUX ON EAST U FACE<br>* = 4 MOMENTUM FLUX ON NORTH V FACE<br>* BQWRMFU: UPSTREAM MOMENTUM FLUX WIDTH (m)<br>* BQWRMFD: DOWNSTREAM MOMENTUM FLUX WIDTH (m)<br>* ANGWRMFD: ANGLE FOR HORIZONTAL FOR RETURN FLOW MOMENTUM FLUX<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C33 IWRU JWRU KWRU IWRD JWRD KWRD QWRE NQW_RQ NQWR_U<br><br>˓→NQWR_D BQWR_U BQWR_D ANG_D GRPID ! ID|
|---|


##### card34

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C34 TIME CONSTANT WITHDRAWAL AND RETURN CONCENTRATION RISES<br><br>*<br><br>* SAL: SALINITY RISE<br>* TEM: TEMPERATURE RISE<br>* DYE: DYE CONCENTRATION RISE<br>* SFL: SHELLFISH LARVAE CONCENTRATION RISE<br>* TOX#: NTOX TOXIC CONTAMINANT CONCENTRATION RISES<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C34 SAL TEM DYE1 SFL GRPID ! ID|
|---|


##### card35

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C35 TIME CONSTANT WITHDRAWAL AND RETURN CONCENTRATION RISES<br><br>*<br><br>* SED#: NSEDC COHESIVE SEDIMENT CONCENTRATION RISE<br>* SND#: NSEDN NON-COHESIVE SEDIMENT CONCENTRATION RISE<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C35 SED1 SED2 SED3 SED4 SED5 SED6 SED7<br><br>˓→ SED8 GRPID ! ID (8 SEDS + 0 SNDS)|
|---|


##### 1.3. Input Files 34



<<<PAGE 37>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card36

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C36 SEDIMENT INITIALIZATION AND WATER COLUMN/BED REPRESENTATION OPTIONS<br><br>* DATA REQUIRED IF ISTRAN(6) OR ISTRAN(7) <> 0<br><br>*<br><br>* ISEDINT: 0 FOR CONSTANT INITIAL CONDITIONS<br>* 1 FOR SPATIALLY VARIABLE WATER COLUMN INITIAL CONDITIONS<br>* FROM SEDW.INP AND SNDW.INP<br>* 2 FOR SPATIALLY VARIABLE BED INITIAL CONDITIONS<br>* FROM SEDB.INP AND SNDB.INP<br>* 3 FOR SPATIALLY VARIABLE WATER COL AND BED INITIAL CONDITIONS<br>* ISEDBINT: 0 FOR SPATIALLY VARYING BED INITIAL CONDITIONS IN MASS/AREA<br>* 1 FOR SPATIALLY VARYING BED INITIAL CONDITIONS IN MASS FRACTION<br>* OF TOTAL SEDIMENT MASS (REQUIRES BED LAYER THICKNESS<br>* FILE BEDLAY.INP)<br>* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE<br>* 1 USE SEDZLJ SUB-MODEL WITH EE8.X/SNL EROSION RATE LOOKUP ˓→TABLES AND BED PROPERTIES BY COREID<br><br>* 2 USE SEDZLJ SUB-MODEL WITH COMPUTED EROSION RATES E = ˓→A*TAU**N AND BED PROPERTIES BY COREID<br><br>* 3 USE SEDZLJ SUB-MODEL WITH COMPUTED EROSION RATES E = ˓→A*TAU**N AND FULL BED PROPERTY<br><br>* SPECIFICATION USING SEDB, BEDLAY, BEDBDN AND BEDDDN<br><br>*<br><br>* ISMUD: 1 INCLUDE COHESIVE FLUID MUD VISCOUS EFFECTS USING EFDC<br>* FUNCTION CSEDVIS(SEDT)<br>* ISBEDMAP: 0 DO NOT USE USE BEDMAP.INP, ALL CELLS COMPUTED<br>* 1 USE BEDMAP.INP TO SPECIFIED HARD BOTTOM<br><br>*<br><br>* ISEDVW: 0 FOR CONSTANT OR SIMPLE CONCENTRATION DEPENDENT<br>* COHESIVE SEDIMENT SETTLING VELOCITY<br>* >1 CONCENTRATION AND/OR SHEAR/TURBULENCE DEPENDENT COHESIVE<br>* SEDIMENT SETTLING VELOCITY. VALUE INDICATES OPTION TO BE USED<br>* IN EFDC FUNCTION CSEDSET(SED,SHEAR,ISEDVWC)<br>* 1 HUANG AND MEHTA - LAKE OKEECHOBEE<br>* 2 SHRESTHA AND ORLOB - FOR KRONES SAN FRANCISCO BAY DATA<br>* 3 ZIEGLER AND NESBIT - FRESH WATER<br>* 98 LICK FLOCCULATION<br>* 99 LICK FLOCCULATION WITH FLOC DIAMETER ADVECTION<br>* ISNDVW: 0 USE CONSTANT SPECIFIED NON-COHESIVE SED SETTLING VELOCITIES<br>* OR CALCULATE FOR CLASS DIAMETER IF SPECIFIED VALUE IS NEG<br>* >1 FOLLOW OPTION 0 PROCEDURE BUT APPLY HINDERED SETTLING<br>* CORRECTION. VALUE INDICATES OPTION TO BE USED WITH EFDC<br>* FUNCTION CSNDSET(SND,SDEN,ISNDVW) VALUE OF ISNDVW INDICATES<br>* EXPONENTIAL IN CORRECT (1-SDEN(NS)*SND(NS)**ISNDVW<br>* KB: MAXIMUM NUMBER OF BED LAYERS (EXCLUDING ACTIVE LAYER)<br>* ISDTXBUG: 1 TO ACTIVATE SEDIMENT AND TOXICS DIAGNOSTICS<br><br><br>* C36 ISEDINT ISEDBINT NSEDFLUME ISMUD ISBEDMAP ISEDVW ISNDVW KB<br><br>˓→ISDTXBUG|
|---|


##### 1.3. Input Files 35



<<<PAGE 38>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card36a

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C36A SEDIMENT INITIALIZATION AND WATER COLUMN/BED REPRESENTATION OPTIONS<br><br>* DATA REQUIRED EVEN IF ISTRAN(6) AND ISTRAN(7) ARE 0<br><br>*<br><br>* ISBEDSTR: 0 USE HYDRODYNAMIC MODEL STRESS FOR SEDIMENT TRANSPORT<br>* 1 SEPARATE GRAIN STRESS FROM TOTAL IN COHESIVE AND NON-COHESIVE ˓→COMPONENTS<br><br>* 2 SEPARATE GRAIN STRESS FROM TOTAL APPLY TO COHESIVE AND NON˓→COHESIVE SEDS<br>* 3 USE INDEPENDENT LOG LAW ROUGHNESS HEIGHT FOR SEDIMENT ˓→TRANSPORT<br><br>* READ FROM FILE SEDROUGH.INP<br>* 4 SEPARATE GRAIN STRESS FROM TOTAL USING COHESIVE/NON-COHESIVE ˓→WEIGHTED<br><br>* ROUGHNESS AND LOG LAW RESISTANCE (IMPLEMENTED 5/31/05)<br>* 5 SEPARATE GRAIN STRESS FROM TOTAL USING COHESIVE/NON-COHESIVE ˓→WEIGHTED<br><br>* ROUGHNESS AND POWER LAW RESISTANCE (IMPLEMENTED 5/31/05)<br>* ISBSDIAM: 0 USE D50 DIAMETER FOR NON-COHESIVE ROUGHNESS<br>* 1 USE 2*D50 FOR NON-COHESIVE ROUGHNESS<br>* 2 USE D90 FOR NON-COHESIVE ROUGHNESS<br>* 3 USE 2*D90 FOR NON-COHESIVE ROUGHNESS<br>* ISBSDFUF: 1 CORRECT GRAIN STRESS PARTITIONING FOR NON-UNIFORM FLOW EFFECTS<br>* DO NOT USE FOR ISBEDSTR = 4 AND 5<br>* COEFTSBL: COEFFICIENT SPECIFYING THE HYDRODYNAMIC SMOOTHNESS OF<br>* TURBULENT BOUNDARY LAYER OVER COHESIVE BED IN TERMS OF<br>* EQUIVALENT GRAIN SIZE FOR COHESIVE GRAIN STRESS<br>* CALCULATION, FULLY SMOOTH = 4, FULLY ROUGH = 100.<br>* NOT USED FOR ISBEDSTR = 4 AND 5<br>* VISMUDST: KINEMATIC VISCOSITY TO USE IN DETERMINING COHESIVE GRAIN ˓→STRESS<br><br>* ISBKERO: 1 FOR BANK EROSION SPECIFIED BY EXTERNAL TIME SERIES<br>* 2 FOR BANK EROSION INTERNALLY CALCULATED BY STABILITY ANALYSIS ˓→(Not Active)<br><br><br>* C36A ISBEDSTR ISBSDIAM ISBSDFUF COEFTSBL VISMUDST ISBKERO|
|---|


##### card36b

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C36B SEDIMENT INITIALIZATION AND WATER COLUMN/BED REPRESENTATION OPTIONS<br><br>* DATA REQUIRED EVEN IF ISTRAN(6) AND ISTRAN(7) ARE 0<br><br>*<br><br>* ISEDAL: NOT USED<br>* ISNDAL: 1 TO ACTIVATE NON-COHESIVE ARMORING EFFECTS (GARCIA & PARKER)<br>* 2 SAME AS 1 WITH ACTIVE-PARENT LAYER FORMULATION<br>* IALTYP: 0 CONSTANT THICKNESS ARMORING LAYER<br>* 1 CONSTANT TOTAL SEDIMENT MASS ARMORING LAYER<br>* IALSTUP: 1 CREATE ARMORING LAYER FROM INITIAL TOP LAYER AT START UP<br>* ISEDEFF: 1 MODIFY NON-COHESIVE RESUSPENSION TO ACCOUNT FOR COHESIVE ˓→EFFECTS<br><br><br>|
|---|


(continues on next page)

##### 1.3. Input Files 36



<<<PAGE 39>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



(continued from previous page)

|* USING MULTIPLICATION FACTOR: EXP(-COEHEFF*FRACTION COHESIVE)<br>* 2 MODIFY NON-COHESIVE CRITICAL STRESS TO ACCOUNT FOR COHESIVE ˓→EFFECTS<br><br>* USING MULT FACTOR: 1+(COEHEFF2-1)*(1-EXP(-COEHEFF*FRACTION ˓→COHESIVE))<br><br>* HBEDAL: ACTIVE ARMORING LAYER THICKNESS<br>* COEHEFF: COHESIVE EFFECTS COEFFICIENT<br>* COEHEFF2: COHESIVE EFFECTS COEFFICIENT<br><br><br>* C36B ISEDAL ISNDAL IALTYP IALSTUP ISEDEFF HBEDAL COEHEFF COEHEFF2|
|---|


##### card37

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C37 BED MECHANICAL PROPERTIES PARAMETER SET 1<br><br>* DATA REQUIRED IF NSED>0, EVEN IF ISTRAN(6) = 0<br><br>*<br><br>* SEDSTEP : SEDIMENT BED INTERACTION TIME STEP (SECONDS)<br>* SEDSTART: START TIME FOR BED/WATER COLUMN INTERACTION (DAYS)<br>* IBMECH: 0 TIME INVARIANT CONSTANT BED MECHANICAL PROPERTIES (UNIFORM BED ˓→ONLY)<br><br>* 1 SIMPLE CONSOLIDATION CALCULATION WITH CONSTANT COEFFICIENTS<br>* 2 SIMPLE CONSOLIDATION WITH VARIABLE COEFFICIENTS DETERMINED<br>* EFDC FUNCTIONS CSEDCON1,2,3(IBMECH)<br>* 3 COMPLEX CONSOLIDATION WITH VARIABLE COEFFICIENTS DETERMINED<br>* EFDC FUNCTIONS CSEDCON1,2,3(IBMECH). IBMECH > 0 SETS THE<br>* C38 PARAMETER ISEDBINT=1 AND REQUIRES INITIAL CONDITIONS<br>* FILES BEDLAY.INP, BEDBDN.INP AND BEDDDN.IN<br>* 9 TYPE OF CONSOLIDATION VARIES BY CELL WITH IBMECH FOR EACH<br>* DEFINED IN INPUT FILE CONSOLMAP.INP<br>* IMORPH: 0 CONSTANT BED MORPHOLOGY (IBMECH=0, ONLY)<br>* 1 ACTIVE BED MORPHOLOGY: NO WATER ENTRAIN/EXPULSION EFFECTS<br>* 2 ACTIVE BED MORPHOLOGY: WITH WATER ENTRAIN/EXPULSION EFFECTS<br>* HBEDMAX: TOP BED LAYER THICKNESS (m) AT WHICH NEW LAYER IS ADDED OR IF<br>* KBT(I,J)=KB, NEW LAYER ADDED AND LOWEST TWO LAYERS COMBINED<br>* BEDPORC: CONSTANT BED POROSITY (IBMECH=0, OR NSED=0)<br>* ALSO USED AS POROSITY OF DEPOSITION NON-COHESIVE SEDIMENT<br>* SEDMDMX: MAXIMUM FLUID MUD COHESIVE SEDIMENT CONCENTRATION (MG/L)<br>* SEDMDMN: MINIMUM FLUID MUD COHESIVE SEDIMENT CONCENTRATION (MG/L)<br>* SEDVDRD: VOID RATIO OF DEPOSITING COHESIVE SEDIMENT<br>* SEDVDRM: MINIMUM COHESIVE SEDIMENT BED VOID RATIO (IBMECH > 0)<br>* SEDVDRT: BED CONSOLIDATION RATE CONSTANT (sec) (IBMECH = 1,2), EXP(-DELT/ ˓→SEDVDRT)<br>* > 0 CONSOLIDATE OVER TIME TO SEDVDRM<br>* = 0 CONSOLIDATE INSTANTANEOUSLY TO SEDVDRM (0.0>=SEDVDRT<=0. ˓→0001)<br>* < 0 CONSOLIDATE TO INITIAL VOID RATIOS<br><br><br>* C37 SEDSTEP SEDSTART IBMECH IMORPH HBEDMAX BEDPORC SEDMDMX SEDMDMN SEDVDRD<br><br>˓→SEDVDRM SEDVRDT|
|---|


##### 1.3. Input Files 37



<<<PAGE 40>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card38

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C38 BED MECHANICAL PROPERTIES PARAMETER SET 2<br><br>* DATA REQUIRED IF NSED>0, EVEN IF ISTRAN(6) = 0<br><br>*<br><br>* IBMECHK: 0 FOR HYDRAULIC CONDUCTIVITY, K, FUNCTION K=KO*EXP((E-EO)/EK)<br>* 1 FOR HYD COND/(1+VOID RATIO),K', FUNCTION K'=KO'*EXP((E-EO)/EK)<br>* BMECH1: REFERENCE EFFECTIVE STRESS/WATER SPECIFIC WEIGHT, SEO (m)<br>* IF BMECH1<0 USE INTERNAL FUNCTION, BMECH1,BMECH2,BMECH3 NOT ˓→USED<br><br>* BMECH2: REFERENCE VOID RATIO FOR EFFECTIVE STRESS FUNCTION, EO<br>* BMECH3: VOID RATIO RATE TERM ES IN SE=SEO*EXP(-(E-EO)/ES)<br>* BMECH4: REFERENCE HYDRAULIC CONDUCTIVITY, KO (m/s)<br>* IF BMECH4<0 USE INTERNAL FUNCTION, BMECH1,BMECH2,BMECH3 NOT ˓→USED<br><br>* BMECH5: REFERENCE VOID RATIO FOR HYDRAULIC CONDUCTIVITY, EO<br>* BMECH6: VOID RATIO RATE TERM EK IN (K OR K')=(KO OR KO')*EXP((E-EO)/EK)<br><br><br>* C38 IBMECHK BMECH1 BMECH2 BMECH3 BMECH4 BMECH5 BMECH6|
|---|


##### card39

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C39 COHESIVE SEDIMENT PARAMETER SET 1 REPEAT DATA LINE NSED TIMES<br><br>* DATA REQUIRED IF NSED>0, EVEN IF ISTRAN(6) = 0<br><br>*<br><br>* SEDO: CONSTANT INITIAL COHESIVE SEDIMENT CONC IN WATER COLUMN<br>* (MG/LITER=GM/M^3)<br>* SEDBO: CONSTANT INITIAL COHESIVE SEDIMENT IN BED PER UNIT AREA<br>* (GM/SQ METER) IE 1CM THICKNESS BED WITH SSG=2.5 AND<br>* N=.6,.5 GIVES SEDBO 1.E4, 1.25E4<br>* SDEN: SEDIMENT SPEC VOLUME (IE 1/2.25E6 M^3/GM)<br>* SSG: SEDIMENT SPECIFIC GRAVITY<br>* WSEDO: CONSTANT OR REFERENCE SEDIMENT SETTLING VELOCITY<br>* IN FORMULA WSED=WSEDO*( (SED/SEDSN)^SEXP )<br>* SEDSN: (NOT USED)<br>* SEXP: (NOT USED)<br>* TAUD: BOUNDARY STRESS BELOW WHICH DEPOSITION TAKES PLACE ACCORDING<br>* TO (TAUD-TAU)/TAUD<br>* ISEDSCOR: 1 TO CORRECT BOTTOM LAYER CONCENTRATION TO NEAR BED ˓→CONCENTRATION<br><br>* ISPROBDEP: 0 KRONE PROBABILITY OF DEPOSITION USING COHESIVE GRAIN STRESS<br>* 1 KRONE PROBABILITY OF DEPOSITION USING TOTAL BED STRESS<br>* 2 PARTHENIADES PROBABILITY OF DEPOSITION USING COHESIVE GRAIN ˓→STRESS<br><br>* 3 PARTHENIADES PROBABILITY OF DEPOSITION USING TOTAL BED STRESS<br><br><br>* C39 SEDO SEDBO SDEN SSG WSEDO SEDSN SEXP TAUD ISEDSCOR<br><br>˓→ISPROBDEP|
|---|


##### 1.3. Input Files 38



<<<PAGE 41>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card40

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C40 COHESIVE SEDIMENT PARAMETER SET 2 REPEAT DATA LINE NSED TIMES<br><br>* DATA REQUIRED IF NSED>0, EVEN IF ISTRAN(6) = 0<br><br>*<br><br>* IWRSP: 0 USE RESUSPENSION RATE AND CRITICAL STRESS BASED ON PARAMETERS<br>* ON THIS DATA LINE<br>* >0 USE BED PROPERTIES DEPENDEDNT RESUSPENSION RATE AND CRITICAL<br>* STRESS GIVEN BY EFDC FUNCTIONS CSEDRESS,CSEDTAUS,CSEDTAUB<br>* FUNCTION ARGUMENTS ARE (BDENBED,IWRSP)<br>* 1 HWANG AND MEHTA - LAKE OKEECHOBEE<br>* 2 HAMRICK'S MODIFICATION OF SANFORD AND MAA<br>* 3 SAME AS 2 EXCEPT VOID RATIO OF COHESIVE SEDIMENT FRACTION IS USED<br>* 4 SEDFLUME WITHOUT CRITICAL STRESS<br>* 5 SEDFLUME WITH CRITICAL STRESS<br>* >= 99 SITE SPECIFIC<br>* IWRSPB:0 NO BULK EROSION<br>* 1 USE BULK EROSION CRITICAL STRESS AND RATE IN FUNCTIONS<br>* CSEDTAUB AND CSEDRESSB<br>* WRSPO: REF SURFACE EROSION RATE IN FORMULA<br>* WRSP=WRSP0*( ((TAU-TAUR)/TAUN)**TEXP ) (gm/M^2/sec)<br>* TAUR: BOUNDARY STRESS ABOVE WHICH SURFACE EROSION OCCURS (m/s)**2<br>* TAUN: (NOT USED, TAUN=TAUR SET IN CODE)<br>* TEXP: EXPONENT OF WRSP=WRSP0*( ((TAU-TAUR)/TAUN)**TEXP )<br>* VDRRSPO: REFERENCE VOID RATIO FOR CRITICAL STRESS AND RESUSPENSION RATE<br>* IWRSP=2,3<br>* COSEDHID: COHESIVE SEDIMENT RESUSPENSION HIDING FACTOR TO REDUCE COHESIVE<br>* RESUSPENSION BY FACTOR = (COHESIVE FRACTION OF ˓→SEDIMENT)**COSEDHID<br><br><br>* C40 IWRSP IWRSPB WRSPO TAUR TAUN TEXP VDRRSPO COSEDHID|
|---|


##### card41

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C41 NON-COHESIVE SEDIMENT PARAMETER SET 1 REPEAT DATA LINE NSND TIMES<br><br>* DATA REQUIRED IF NSND>0, EVEN IF ISTRAN(7) = 0<br><br>*<br><br>* SNDO: CONSTANT INITIAL NON-COHESIVE SEDIMENT CONC IN WATER COLUMN<br>* (MG/LITER=GM/M^3)<br>* SNDBO: CONSTANT INITIAL NON-COHESIVE SEDIMENT IN BED PER UNIT AREA<br>* (GM/SQ METER) IE 1CM THICKNESS BED WITH SSG=2.5 AND<br>* N=.6,.5 GIVES SNDBO 1.E4, 1.25E4<br>* SDEN: SEDIMENT SPEC VOLUME (IE 1/2.65E6 M^3/GM)<br>* SSG: SEDIMENT SPECIFIC GRAVITY<br>* SNDDIA: REPRESENTATIVE DIAMETER OF SEDIMENT CLASS (m)<br>* WSNDO: CONSTANT OR REFERENCE SEDIMENT SETTLING VELOCITY<br>* WSNDO < 0, SETTLING VELOCITY INTERNALLY COMPUTED<br>* SNDN: (NOT USED)<br>* SEXP: (NOT USED)<br>* TAUD: (NOT USED)<br>* ISNDSCOR: (NOT USED)<br>|
|---|


(continues on next page)

##### 1.3. Input Files 39



<<<PAGE 42>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



(continued from previous page)

|* C41 SNDO SNDBO SDEN SSG SNDDIA WSNDO SNDN SEXP TAUD<br><br>˓→ISNDSCOR|
|---|


##### card42

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C42 NON-COHESIVE SEDIMENT PARAMETER SET 2 REPEAT DATA LINE NSND TIMES<br><br>* DATA REQUIRED IF NSND>0, EVEN IF ISTRAN(7) = 0<br><br>*<br><br>* ISNDEQ: 0 USER SPECIFIED SPATIALLY AND TEMPORALLY CONSTANT EQUILIBRIUM ˓→CONCENTRATION<br><br>* ISNDEQ: >1 CALCULATE ABOVE BED REFERENCE NON-COHESIVE SEDIMENT<br>* EQUILIBRIUM CONCENTRATION USING EFDC FUNCTION<br>* CSNDEQC(SNDDIA,SSG,WS,TAUR,TAUB,SIGPHI,SNDDMX,IOTP)<br>* WHICH IMPLEMENT FORMULATIONS OF<br>* 1 GARCIA AND PARKER<br>* 2 SMITH AND MCLEAN<br>* 3 VAN RIJN<br>* 4 SEDFLUME WITHOUT CRITICAL STRESS<br>* 5 SEDFLUME WITH CRITICAL STRESS<br>* ISBDLD: 0 BED LOAD PHI FUNCTION IS CONSTANT, SBDLDP<br>* 1 VAN RIJN PHI FUNCTION<br>* 2 MODIFIED ENGULAND-HANSEN<br>* 3 WU, WANG, AND JIA<br>* 4 (NOT USED)<br>* 5 (NOT USED)<br>* TAUR: EQUILIBRIUM CONCENTRATION (g/m**3)<br>* TAUN: Not Used<br>* TCSHIELDS: Not Used<br>* ISLTAUC: Not Used<br>* IBLTAUC: 1 TO IMPLEMENT BEDLOAD ONLY WHEN STRESS EXCEEDS TAUC FOR EACH ˓→GRAINSIZE<br><br>* 2 TO IMPLEMENT BEDLOAD ONLY WHEN STRESS EXCEEDS TAUCD50<br>* 3 TO USE TAUC FOR NONUNIFORM BEDS, THESE APPLY ONLY TO BED LOAD<br>* FORMULAS NOT EXPLICITLY CONTAINING CRITICAL SHIELDS STRESS ˓→SUCH AS E-H<br><br>* IROUSE: 0 USE TOTAL STRESS FOR CALCULATING ROUSE NUMBER<br>* 1 USE GRAIN STRESS FOR ROUSE NUMBER<br>* ISNDM1: 0 SET BOTH BEDLOAD AND SUSPENDED LOAD FRACTIONS TO 1.0<br>* 1 SET BEDLOAD FRACTION TO 1. USE BINARY RELATIONSHIP FOR ˓→SUSPENDED<br><br>* 2 SET BEDLOAD FRACTION TO 1, USE LINEAR RELATIONSHIP FOR ˓→SUSPENDED<br><br>* 3 USE BINARY RELATIONSHIP FOR BEDLOAD AND SUSPENDED LOAD<br>* 4 USE LINEAR RELATIONSHIP FOR BEDLOAD AND SUSPENDED LOAD<br>* ISNDM2: 0 USE TOTAL SHEAR VELOCITY IN USTAR/WSET RATIO<br>* 1 USE GRAIN SHEAR VELOCITY IN USTAR/WSET RATIO<br>* RSNDM: VALUE OF USTAR/WSET FOR BINARY SWITCH BETWEEN BEDLOAD AND ˓→SUSPENDED LOAD<br><br><br>* C42 ISNDEQ ISBDLD TAUR TAUN TCSHIELDS ISLTAUC IBLTAUC IROUSE<br><br>˓→ISNDM1 ISNDM2 RSNDM|
|---|


##### 1.3. Input Files 40



<<<PAGE 43>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card42a

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C42A NON-COHESIVE SEDIMENT PARAMETER SET 3 (BED LOAD FORMULA PARAMETERS)<br><br>* DATA REQUIRED IF NSND>0, EVEN IF ISTRAN(7) = 0<br><br>*<br><br>* ISBDLDBC: 0 DISABLE BEDLOAD<br>* 1 ACTIVATE BEDLOAD OPTION. USES SEDBLBC.INP TO SPECIFY CELLS<br>* SBDLDA: ALPHA EXPONENTIAL FOR BED LOAD FORMULA<br>* SBDLDB: BETA EXPONENTIAL FOR BED LOAD FORMULA<br>* SBDLDG1: GAMMA1 CONSTANT FOR BED LOAD FORMULA<br>* SBDLDG2: GAMMA2 CONSTANT FOR BED LOAD FORMULA<br>* SBDLDG3: GAMMA3 CONSTANT FOR BED LOAD FORMULA<br>* SBDLDG4: GAMMA4 CONSTANT FOR BED LOAD FORMULA<br>* SBDLDP: CONSTANT PHI FOR BED LOAD FORMULA<br>* ISBLFUC: BED LOAD FACE FLUX , 0 FOR DOWN WIND PROJECTION,1 FOR DOWN ˓→WIND<br><br>* WITH CORNER CORRECTION,2 FOR CENTERED AVERAGING<br>* BLBSNT: ADVERSE BED SLOPE (POSITIVE VALUE) ACROSS A CELL FACE ABOVE<br>* WHICH NO BED LOAD TRANSPORT CAN OCCUR. NOT ACTIVE FOR ˓→BLBSNT=0.0<br><br><br>* C42A IBEDLD SBDLDA SBDLDB SBDLDG1 SBDLDG2 SBDLDG3 SBDLDG4 SBDLDP ISBLFUC<br><br>˓→ BLBSNT|
|---|


##### card43a

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C43A TOXIC CONTAMINANT INITIAL CONDITIONS<br><br>* USER MAY CHANGE ORDER OF MAGNITUDE OF WATER AND SED PHASE TOXIC ˓→CONCENTRATIONS<br><br>* AND PARTITION COEFFICIENTS ON C44 - C46 BUT MUST BE CONSISTENT UNITS<br><br>*<br><br>* NTOXN: TOXIC CONTAMINANT NUMBER ID<br>* ITXINT: 0 FOR SPATIALLY CONSTANT WATER COL AND BED INITIAL CONDITIONS<br>* 1 FOR SPATIALLY VARIABLE WATER COLUMN INITIAL CONDITIONS<br>* 2 FOR SPATIALLY VARIABLE BED INITIAL CONDITIONS<br>* 3 FOR SPATIALLY VARIABLE WATER COL AND BED INITIAL CONDITION<br>* ITXBDUT: SET TO 0 FOR INITIAL BED GIVEN BY TOTAL TOXIC CONCENTRATION (mg/ ˓→m^3)<br>* SET TO 1 FOR INITIAL BED GIVEN BY TOTAL SEDIMENT NORMALIZED ˓→CONCENTRATION (mg/kg)<br><br>* TOXINTW: INIT WATER COLUMN TOT TOXIC VARIABLE CONCENTRATION (ug/L)<br>* TOXINTB: INIT SED BED TOXIC CONCENTRATION. SEE ITXBDUT FOR UNITS<br>* UNITS : UNITS OF TOXIC CLASS (text)<br><br><br>* C43A NTOXN ITXINT ITXBDUT TOXINTW TOXINTB UNITS COMMENTS|
|---|


##### 1.3. Input Files 41



<<<PAGE 44>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



- card43b


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C43B TOXIC KINETIC OPTION FLAGS<br><br>*<br><br>* NTOXN: TOXIC CONTAMINANT NUMBER ID<br>* ITOXKIN(1): 0 DO NOT USE BULK DECAY<br>* : 1 USE BULK DECAY FOR WATER COLUMN AND SEDIMENT<br>* ITOXKIN(2): 0 DO NOT USE BIODEGRADATION<br>* : 1 USE BIODEGRADATION FOR WATER COLUMN AND SEDIMENT<br>* ITOXKIN(3): 0 DO NOT USE VOLATILIZATION<br>* : 1 USE VOLATILIZATION FOR RIVER AND LAKE CONDITIONS. LAKE USES ˓→O'CONNOR<br><br>* : 2 USE VOLATILIZATION FOR RIVER AND LAKE CONDITIONS. LAKE USES ˓→MACKAY & YEUN<br><br>* ITOXKIN(4): 0 DO NOT USE PHOTOLYSIS (NOT IMPLEMENTED)<br>* : 1 USE PHOTOLYSIS FOR WATER COLUMN (NOT IMPLEMENTED)<br>* ITOXKIN(5): 0 DO NOT USE HYDROLYSIS (NOT IMPLEMENTED)<br>* : 1 USE HYDROLYSIS FOR WATER COLUMN (NOT IMPLEMENTED)<br>* ITOXKIN(6): 0 DO NOT USE DAUGHTER PRODUCTS (NOT IMPLEMENTED)<br>* : 1 USE DAUGHTER PRODUCTS (NOT IMPLEMENTED)<br><br><br>* C43B NTOXN KIN(1) KIN(2) KIN(3) KIN(4) KIN(5) KIN(6) COMMENTS|
|---|


- card43c


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C43C TOXIC TIME STEPS AND VOLATILIZATION SWITCHES<br><br>*<br><br>* TOXSTEPW: TIME STEP IN SECONDS FOR TOXIC KINETICS IN WATER COLUMN AND ˓→BED<br><br>* TOXSTEPB: TIME STEP IN SECONDS FOR TOXIC BED PROCESSES OF DIFFUSION ˓→AND MIXING<br><br>* TOX_VEL_MAX: VELOCITY SWITCH FOR VOLATILIZATION APPROACH: LAKE < TOX_VEL_ ˓→MAX > RIVER<br>* TOX_DEP_MAX: DEPTH SWITCH FOR VOLATILIZATION APPROACH: LAKE > TOX_DEP_ ˓→MAX < RIVER<br>* ITOXTEMP: TEMPERATURE OVERRIDE IF ISTRAN(2)=0<br>* 1 - CONSTANT TEMPERATURE = TOXTEMP<br>* >1 - TIME VARYING TEMPERATURE SERIES FROM TSER(ITOXTEMP-1)<br>* TOXTEMP: CONSTANT TEMPERATURE FOR TOXICS CALCULATIONS(DEG C)<br><br><br>* C43C STEPW STEPB VEL_MAX DEP_MAX ITOXTEMP TOXTEMP|
|---|


##### 1.3. Input Files 42



<<<PAGE 45>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



card43d

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C43D TOXIC BULK DECAY AND BIODEGRADATION PARAMETERS<br><br>*<br><br>* NTOXN: TOXIC CONTAMINANT NUMBER ID<br>* TOX_BLK_KW: BULK DECAY RATE IN THE WATER COLUMN (1/SECOND)<br>* TOX_BLK_KB: BULK DECAY RATE IN THE SEDIMENT BED (1/SECOND)<br>* TOX_BLK_MXD: MAXIMUM DEPTH OF BULK DECAY IN THE SEDIMENT BED (METERS)<br>* TOX_BIO_KW: BIODEGRADATION RATE IN THE WATER COLUMN (1/SECOND)<br>* TOX_BIO_KB: BIODEGRADATION RATE IN THE SEDIMENT BED (1/SECOND)<br>* TOX_BIO_MXD: MAXIMUM DEPTH OF BIODEGRADATION IN THE SEDIMENT BED (METERS)<br>*TOX_BIO_Q10W: Q10 TEMPERATURE ADJUSTMENT COEFFICIENT FOR WATER COLUMN<br>* BIODEGRADATION(dimensionless)<br>*TOX_BIO_Q10B: Q10 TEMPERATURE ADJUSTMENT COEFFICIENT FOR SEDIMENT BED<br>* BIODEGRADATION(dimensionless)<br>* TOX_BIO_TW: REFERENCE TEMPERATURE FOR BIODEGRADATION IN WATER COLUMN (DEG ˓→C)<br><br>* COEFF = TOX_BIO_KW(NT)*TOX_BIO_Q10W(NT)^((TEM(L,K)-TOX_BIO_TB(NT))/10)<br>* TOX_BIO_TB: REFERENCE TEMPERATURE FOR BIODEGRADATION IN SEDIMENT BED (DEG ˓→C)<br><br>* COEFF = TOX_BIO_KB(NT)*TOX_BIO_Q10B(NT)^((TEMB(L)-TOX_BIO_TB(NT))/10)<br><br><br>* C43D NTOXN BLK_KW BLK_KB BLK_MXD BIO_KW BIO_KB BIO_MXD Q10W Q10B<br><br>˓→ BIO_TW BIO_TW COMMENTS|
|---|


card43e

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C43E TOXIC VOLATILIZATION PARAMETERS<br><br>*<br><br>* NTOXN: TOXIC CONTAMINANT NUMBER ID<br>* TOX_MW: MOLECULAR WEIGHT (G/MOLE)<br>* TOX_HE: HENRY'S LAW COEFFICIENT FOR THE TOXIC (ATM-M3/MOLE)<br>* TOX_KV_TCOEFF: MASS TRANSFER TEMPERATURE COEFFICIENT (DIMENSIONLESS)<br>* TOX_KV_TCOEFF**(TEM(L,KC)-20)<br>* TOX_ATM: ATMOSPHERIC CONCENTRATION OF TOXIC (micro G/L)<br>* TOX_VOL_ADJ: ADJUSTMENT FACTOR (DIMENSIONLESS)<br><br><br>* C43E NTOXN TOX_MW TOX_HE TCOEFF ATM VOL_ADJ COMMENTS|
|---|


- card44


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C44 TOXIC SORPTION OPTION, DIFFUSION AND MIXING<br><br>*<br><br>* NTOXN: TOXIC CONTAMINANT NUMBER ID (1 LINE OF DATA BY DEFAULT)<br>* ISTOC: 0 INORGANIC SOLIDS BASED PARTITIONING ONLY (Kd APPROACH)<br>* 1 FOR DISS AND PART ORGANIC CARBON SORPTION, POC IS SPECIFIED<br>* 2 FOR DISS ORGANIC CARBON SORPTION AND POC FRACTIONALLY<br>|
|---|


(continues on next page)

##### 1.3. Input Files 43



<<<PAGE 46>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* DISTRIBUTED TO INORGANIC SEDIMENT CLASSES<br>* 3 FOR NO DISS ORGANIC CARBON SORPTION AND POC FRACTIONALLY<br>* DISTRIBUTED TO INORGANIC SEDIMENT CLASSES<br>* DIFTOX: DIFFUSION COEFF FOR TOXICANT IN SED BED PORE WATER (M^2/s)<br>* DIFTOXS: DIFFUSION COEFF FOR TOXICANT BETWEEN WATER COLUMN AND<br>* PORE WATER IN TOP LAYER OF THE BED(M^2/s)<br>* > 0.0 INTERPRET AS DIFFUSION COEFFICIENT (M^2/s)<br>* < 0.0 INTERPRET AS FLUX VELOCITY (m/s)<br>* PDIFTOX: PARTICLE MIXING DIFFUSION COEFF FOR TOXICANT IN SED BED (M^2/s)<br>* (if negative use zonal files PARTMIX.INP and PMXMAP.INP)<br>* DPDIFTOX: DEPTH IN BED OVER WHICH PARTICLE MIXING IS ACTIVE (m)<br><br><br>* C44 NTOXN ISTOC DIFTOX DIFTOXS PDIFTOX DPDIFTOX|
|---|


- card45


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C45 TOXIC CONTAMINANT SEDIMENT INTERACTION PARAMETERS<br><br>* *<br><br>* NTOXC: TOXIC CONTAMINANT NUMBER ID. NSEDC+NSEDN LINES OF DATA<br>* FOR EACH TOXIC CONTAMINANT (DEFAULT = 2)<br>* NSEDN/NSNDN: FIRST NSED LINES COHESIVE, NEXT NSND LINES NON-COHESIVE.<br>* REPEATED FOR EACH CONTAMINANT<br>* ITXPARW: O FOR NORMAL WC PARTITIONING<br>* 1 FOR SOLIDS DEPENDENT WC PARTITIONING ˓→TOXPAR=PARO*(CSED**CONPAR)<br><br>* TOXPARW: WATER COLUMN PARO (ITXPARW=1) OR EQUIL TOX CON PART COEFF BETWEEN<br>* EACH TOXIC IN WATER AND ASSOCIATED SEDIMENT PHASES (LITERS/MG)<br>* CONPARW: EXPONENT IN TOXPAR=PARO*(CSED**CONPARW) IF ITXPARW=1<br>* ITXPARB: Not Used<br>* TOXPARB: SEDIMENT BED PARO (ITXPARB=1) OR EQUIL TOX CON PART COEFF BETWEEN<br>* EACH TOXIC IN WATER AND ASSOCIATED SEDIMENT PHASES (LITERS/MG)<br>* CONPARB: Not Used<br>* 1 0.8770 -0.943 0.025 C45 NTOXN NSEDN ITXPARW TOXPARW CONPARW ITXPARB TOXPARB CONPARB<br>|
|---|


- card45a


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C45A TOXIC CONTAMINANT NON-SEDIMENT BASED ORGANIC CARBON (OC) INTERACTION<br><br>˓→PARAMETERS<br><br>*<br><br>* ISTDOCW: 0 CONSTANT DOC IN WATER COLUMN OF STDOCWC (DEFAULT=0.)<br>* 1 TIME CONSTANT, SPATIALLY VARYING DOC IN WATER COLUMN FROM docw. ˓→inp<br>* ISTPOCW: 0 CONSTANT POC IN WATER COLUMN OF STPOCWC (DEFAULT=0.)<br>* 1 TIME CONSTANT, SPATIALLY VARYING POC IN WATER COLUMN FROM pocw. ˓→inp<br>* 2 TIME CONSTANT, FPOC IN WATER COLUMN, SEE C45C<br>|
|---|


(continues on next page)

##### 1.3. Input Files 44



<<<PAGE 47>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* 3 TIME CONSTANT, SPATIALLY VARYING FPOC IN WATER COLUMN FORM ˓→fpocw.inp<br><br>* 4 FUNCTIONAL SPECIFICATION OF TIME AND SPATIALLY VARYING<br>* FPOC IN WATER COLUMN<br>* ISTDOCB: 0 CONSTANT DOC IN BED OF STDOCBC (DEFAULT=0.)<br>* 1 TIME CONSTANT, SPATIALLY VARYING DOC IN BED FROM docb.inp<br>* ISTPOCB: 0 CONSTANT POC IN BED OF STPOCBC (DEFAULT=0.)<br>* 1 TIME CONSTANT, SPATIALLY VARYING POC IN BED FROM pocb.inp<br>* 2 TIME CONSTANT, FPOC IN BED, SEE C45D<br>* 3 TIME CONSTANT, SPATIALLY VARYING FPOC IN BED FROM fpocb.inp<br>* 4 FUNCTIONAL SPECIFICATION OF TIME AND SPATIALLY VARYING<br>* FPOC IN BED, REQUIRES CODE MODIFICATION FOR EACH APPLICATION ˓→(ADVANCED)<br><br>* STDOCWC: CONSTANT WATER COLUMN DOC (ISTDOCW=0)<br>* STPOCWC: CONSTANT WATER COLUMN POC (ISTPOCW=0)<br>* STDOCBC: CONSTANT BED DOC (ISTDOCB=0)<br>* STPOCBC: CONSTANT BED POC (ISTPOCB=0)<br><br><br>* C45A ISTDOCW ISTPOCW ISTDOCB ISTPOCB STDOCWC STPOCWC STDOCBC STPOCBC|
|---|


##### card45b

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C45B TOXIC CONTAMINANT NON-SEDIMENT BASED ORGANIC CARBON (OC) INTERACTION<br><br>˓→PARAMETERS<br><br>* *<br><br>* NTOXC: TOXIC CONTAMINANT NUMBER ID. FOR EACH TOXIC CONTAMINANT<br>* NOC : FIRST LINE FOR DISSOLVED ORGANIC CARBON (DOC)<br>* SECOND LINE FOR PARTICULATE ORGANIC CARBON (POC)<br>* REPEATED FOR EACH CONTAMINANT<br>* ITXPARWC: O FOR NORMAL WC PARTITIONING<br>* 1 FOR SOLIDS DEPENDENT WC PARTITIONING ˓→TOXPAR=PARO*(CSED**CONPAR)<br><br>* TOXPARWC: WATER COLUMN PARO (ITXPARW=1) OR EQUIL TOX CON PART COEFF ˓→BETWEEN<br><br>* EACH TOXIC IN WATER AND ASSOCIATED SEDIMENT PHASES (liters/mg)<br>* CONPARWC: EXPONENT IN TOXPAR=PARO*(CSED**CONPARW) IF ITXPARW=1<br>* ITXPARBC: Not Used<br>* TOXPARBC: SEDIMENT BED PARO (ITXPARB=1) OR EQUIL TOX CON PART COEFF ˓→BETWEEN<br><br>* EACH TOXIC IN WATER AND ASSOCIATED SEDIMENT PHASES (liters/mg)<br>* CONPARBC: Not Used<br>* 1 0.8770 -0.943 0.025 C45B NTOXN NOC ITXPARWC TOXPARWC CONPARWC ITXPARBC TOXPARBC CONPARBC<br><br><br>˓→<br><br>*CARBON*|
|---|


##### 1.3. Input Files 45



<<<PAGE 48>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



- card45c

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C45C TOXIC CONTAMINANT POC FRACTIONAL DISTRIBUTIONS IN WATER COLUMN<br><br>* 1 LINE OF DATA REQUIRED EVEN IT ISTRAN(5) IS 0. DATA USED WHEN<br>* ISTOC(NT)=1 OR 2<br><br>*<br><br>* NTOXN: TOXIC CONTAMINANT NUMBER ID. NSEDC+NSEDN 1 LINE OF DATA<br>* FOR EACH TOXIC CONTAMINANT (DEFAULT = 2)<br>* FPOCSED1-NSED: FRACTION OF OC ASSOCIATED WITH SED CLASSES 1,NSED<br>* FPOCSND1-NSND: FRACTION OF OC ASSOCIATED WITH SND CLASSES 1,NSND<br><br><br>* C45C NTOXN FPOCSED1 FPOCSED2 FPOCSED3 FPOCSED4 FPOCSED5 FPOCSED6<br><br>˓→FPOCSED7 FPOCSED8 GRPID ! ID (8 SEDS + 0 SNDS)|
|---|


- card45d


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C45D TOXIC CONTAMINANT POC FRACTIONAL DISTRIBUTIONS IN SEDIMENT BED<br><br>* 1 LINE OF DATA REQUIRED EVEN IT ISTRAN(5) IS 0. DATA USED WHEN<br>* ISTOC(NT)=1 OR 2<br><br>*<br><br>* NTOXN: TOXIC CONTAMINANT NUMBER ID. NSEDC+NSEDN 1 LINE OF DATA<br>* FOR EACH TOXIC CONTAMINANT (DEFAULT = 2)<br>* FPOCSED1-NSED: FRACTION OF OC ASSOCIATED WITH SED CLASSES 1,NSED<br>* FPOCSND1-NSND: FRACTION OF OC ASSOCIATED WITH SND CLASSES 1,NSND<br><br><br>* C45D NTOXN FPOCSED1 FPOCSED2 FPOCSED3 FPOCSED4 FPOCSED5 FPOCSED6<br><br>˓→FPOCSED7 FPOCSED8 GRPID ! ID (8 SEDS + 0 SNDS)|
|---|


- card46


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C46 BUOYANCY, TEMPERATURE, DYE DATA AND CONCENTRATION BC DATA<br><br>*<br><br>* BSC: BUOYANCY INFLUENCE COEFFICIENT 0 TO 1, BSC=1. FOR REAL PHYSICS<br>* TEMO: REFERENCE, INITIAL, EQUILIBRIUM AND/OR ISOTHERMAL TEMP IN DEG ˓→C<br><br>* HEQT: EQUILIBRIUM TEMPERATURE TRANSFER COEFFICIENT M/sec<br>* ISBEDTEMI: 0 READ INITIAL BED TEMPERATURE FROM TEMPB.INP<br>* 1 INITIALIZE AT START OF COLD RUN<br>* KBH: NOT USED<br>* RKDYE: FIRST ORDER DECAY RATE FOR DYE VARIABLE IN 1/sec<br>* NCBS: NUMBER OF CONCENTRATION BOUNDARY CONDITIONS ON SOUTH OPEN<br>* BOUNDARIES<br>* NCBW: NUMBER OF CONCENTRATION BOUNDARY CONDITIONS ON WEST OPEN<br>* BOUNDARIES<br>* NCBE: NUMBER OF CONCENTRATION BOUNDARY CONDITIONS ON EAST OPEN<br>* BOUNDARIES<br>* NCBN: NUMBER OF CONCENTRATION BOUNDARY CONDITIONS ON NORTH OPEN<br>|
|---|


(continues on next page)

##### 1.3. Input Files 46



<<<PAGE 49>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* BOUNDARIES<br>* C46 BSC TEMO HEQT ISBEDTEMI KBH RKDYE NCBS<br><br><br>˓→NCBW NCBE NCBN|
|---|


card46a

|-----------------------------------------------------------------------------<br><br>˓→C46A ICE EFFECTS C<br><br>ISICE: 0 ICE IMPACTS NOT SIMULATED. AUTOMATICALLY LIMITS ASER. ˓→INP DRY BULB TO > 0.0<br><br>1 READ ICE THICKNESS FROM FILE ISER.INP (LEGACY ICECOVER.<br><br>˓→INP)<br><br>2 SPECIFIED ON/OFF DATES FOR ICE (ENTIRE MODEL)<br>3 CALCULATION COUPLED WITH HEAT MODEL<br>4 CALCULATION COUPLED WITH HEAT MODEL AND FRAZIL TRANSPORT<br><br><br>NISER: NUMBER OF ICE TIME SERIES FOR ISICE=1 TEMPICE: WATER TEMPERATURE AT WATER ICE INTERFACE FOR ISICE <= 2 CDICE: DRAG COEFFICIENT BETWEEN ICE/WATER (DEFAULT = 0.001) ICETHMX: MAXIMUM ICE COVER THICKNESS FOR ISICE>2, METERS RICETHK0: ICE THICKNESS FOR ISICE=2 (CONSTANT, METERS)<br><br>C C46A ISICE NISER TEMPICE CDICE ICETHMX RICETHK0|
|---|


card46c

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C46C ATMOSPHERIC LOCATION AND WIND FUNCTION COEFFICIENTS<br><br>*<br><br>* SOLAR_LNG = LONGITUDE TO BE USED TO COMPUTE SOLAR RADIATION (Decimal ˓→degree)<br><br>* SOLAR_LAT = LATITUDE TO BE USED TO COMPUTE SOLAR RADIATION (Decimal ˓→degree)<br><br>* COMPUTESR = OVERRIDE SOLAR RADIATION IN ASER.INP WITH COMPUTED [.TRUE/. ˓→FALSE.]<br>* USESHADE = USE CELL SPECIFIC SHADE VALUES USING SHADE.INP [.TRUE/.FALSE.]<br>* IEVAP = EVAPORATION OPTION FOR WATER FLUX ONLY (ALWAYS USED FOR HEAT ˓→EXCHANGE)<br><br>* 0 - DO NOT INCLUDE IN WATER BUDGET<br>* 1 - USE SPECIFIED EVAP FROM ASER.INP<br>* 2 - COMPUTE EVAP USING ORIGINAL EFDC EQUATION<br>* 3-10 - COMPUTE USING WIND FUNCTION USING WINDFA, WINDFB, WINDFC<br>* 11 - COMPUTE EVAP USING RYAN-HARLEMAN<br>* 12 - COMPUTE EVAP USING ARIFIN ET AL. (2016)<br>* WINDFA = WIND FUNCTION FACTOR A FUNCTION = A + B*WIND2M + C*WIND2M^2<br>* WINDFB = WIND FUNCTION FACTOR B UNITS: W/M^2/millibar<br>* WINDFC = WIND FUNCTION FACTOR C C46C SOLAR_LNG SOLAR_LAT COMPUTESR USESHADE IEVAP WINDFA<br><br><br>˓→WINDFB WINDFC|
|---|


##### 1.3. Input Files 47



<<<PAGE 50>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card46e

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C46E DYE CLASS PARAMETERS<br><br>*<br><br>* CLASS #<br>* ITYPE = DYE CLASS TYPE<br>* 0 - CONSERVATIVE<br>* 1 - NON-CONSERVATIVE WTIH OPTIONAL SETTLING AND/OR DECAY<br>* 2 - AGE OF WATER<br>* KRATE0 = 0th ORDER DECAY/GROWTH RATE AT REFERENCE TEMPERATURE (TREF) ˓→degC (1/s)<br><br>* KRATE1 = FIRST ORDER DECAY/GROWTH RATE AT REFERENCE TEMPERATURE (TREF) ˓→degC (1/s)<br><br>* TADJ = TEMPERATURE ADJUSTMENT COEFFICIENT (DIMENSIONLESS)<br>* TREF = REFERENCE TEMPERATURE (degC)<br>* ICFLAG = TYPE OF INITIAL CONDITION<br>* 0 - USE CONSTANT INITIAL CONCENTRATION SPECIFIED IN DYEIC<br>* 1 - READ FROM DYE.INP<br>* DYEIC = CONSTANT INITIAL CONCENTRATION (MG/L)<br>* SETTLE = SETTLING RATE (M/DAY)<br>* UNITS = UNITS OF DYE CLASS (text)<br><br><br>* C46E CLASS ITYPE KRATE0 KRATE1 TADJ TREF SETTLE ICFLAG<br><br>˓→DYEIC UNITS|
|---|


##### card47

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C47 LOCATION OF CONC BC'S ON SOUTH BOUNDARIES<br><br>*<br><br>* ICBS: I CELL INDEX<br>* JCBS: J CELL INDEX<br>* NTSCRS: NUMBER OF TIME STEPS TO RECOVER SPECIFIED VALUES ON CHANGE<br>* TO INFLOW FROM OUTFLOW<br>* NSSERS: SOUTH BOUNDARY CELL SALINITY TIME SERIES ID NUMBER<br>* NTSERS: SOUTH BOUNDARY CELL TEMPERATURE TIME SERIES ID NUMBER<br>* NDSERS: SOUTH BOUNDARY CELL DYE CONC TIME SERIES ID NUMBER<br>* NSFSERS: SOUTH BOUNDARY CELL SHELLFISH LARVAE TIME SERIES ID NUMBER<br>* NTXSERS: SOUTH BOUNDARY CELL TOXIC CONTAMINANT CONC TIME SERIES ID NUM.<br>* NSDSERS: SOUTH BOUNDARY CELL COHESIVE SED CONC TIME SERIES ID NUMBER<br>* NSNSERS: SOUTH BOUNDARY CELL NON-COHESIVE SED CONC TIME SERIES ID NUMBER<br>* GRPID: ID NUMBER OF BOUNDARY GROUP C C47 IBBS JBBS NTSCRS NSSERS NTSERS NDSERS NSFSERS NTXSERS NSDSERS<br><br><br>˓→NSNSERS GRPID ! ID|
|---|


##### 1.3. Input Files 48



<<<PAGE 51>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card48

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C48 TIME CONSTANT BOTTOM CONC ON SOUTH CONC BOUNDARIES<br><br>*<br><br>* SAL: ULTIMATE INFLOWING BOTTOM LAYER SALINITY<br>* TEM: ULTIMATE INFLOWING BOTTOM LAYER TEMPERATURE<br>* DYE: ULTIMATE INFLOWING BOTTOM LAYER DYE CONCENTRATION<br>* SFL: ULTIMATE INFLOWING BOTTOM LAYER SHELLFISH LARVAE CONCENTRATION<br>* TOX: NTOX ULTIMATE INFLOWING BOTTOM LAYER TOXIC CONTAMINANT<br>* CONCENTRATIONS NTOX VALUES TOX(N), N=1,NTOX<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C48 SAL TEM DYE1 SFL GRPID ! ID|
|---|


##### card49

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C49 TIME CONSTANT BOTTOM CONC ON SOUTH CONC BOUNDARIES<br><br>*<br><br>* SED: NSED ULTIMATE INFLOWING BOTTOM LAYER COHESIVE SEDIMENT<br>* CONCENTRATIONS FIRST NSED VALUES SED(N), N=1,NSND<br>* SND: NSND ULTIMATE INFLOWING BOTTOM LAYER NON-COHESIVE SEDIMENT<br>* CONCENTRATIONS LAST NSND VALUES SND(N), N=1,NSND<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C49 SED1 SED2 SED3 SED4 SED5 SED6 SED7<br><br>˓→ SED8 GRPID ! ID|
|---|


##### card50

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C50 TIME CONSTANT SURFACE CONC ON SOUTH CONC BOUNDARIES<br><br>*<br><br>* SAL: ULTIMATE INFLOWING SURFACE LAYER SALINITY<br>* TEM: ULTIMATE INFLOWING SURFACE LAYER TEMPERATURE<br>* DYE: ULTIMATE INFLOWING SURFACE LAYER DYE CONCENTRATION<br>* SFL: ULTIMATE INFLOWING SURFACE LAYER SHELLFISH LARVAE CONCENTRATION<br>* TOX: NTOX ULTIMATE INFLOWING SURFACE LAYER TOXIC CONTAMINANT<br>* CONCENTRATIONS NTOX VALUES TOX(N), N=1,NTOX<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C50 SAL TEM DYE1 SFL GRPID ! ID|
|---|


##### 1.3. Input Files 49



<<<PAGE 52>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card51

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C51 TIME CONSTANT SURFACE CONC ON SOUTH CONC BOUNDARIES<br><br>*<br><br>* SED: NSED ULTIMATE INFLOWING SURFACE LAYER COHESIVE SEDIMENT<br>* CONCENTRATIONS FIRST NSED VALUES SED(N), N=1,NSND<br>* SND: NSND ULTIMATE INFLOWING SURFACE LAYER NON-COHESIVE SEDIMENT<br>* CONCENTRATIONS LAST NSND VALUES SND(N), N=1,NSND<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C51 SED1 SED2 SED3 SED4 SED5 SED6 SED7<br><br>˓→ SED8 GRPID ! ID|
|---|


##### card52

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C52 LOCATION OF CONC BC'S ON WEST BOUNDARIES AND SERIES IDENTIFIERS<br><br>*<br><br>* ICBW: I CELL INDEX<br>* JCBW: J CELL INDEX<br>* NTSCRW: NUMBER OF TIME STEPS TO RECOVER SPECIFIED VALUES ON CHANGE<br>* TO INFLOW FROM OUTFLOW<br>* NSSERW: WEST BOUNDARY CELL SALINITY TIME SERIES ID NUMBER<br>* NTSERW: WEST BOUNDARY CELL TEMPERATURE TIME SERIES ID NUMBER<br>* NDSERW: WEST BOUNDARY CELL DYE CONC TIME SERIES ID NUMBER<br>* NSFSERW: WEST BOUNDARY CELL SHELLFISH LARVAE TIME SERIES ID NUMBER<br>* NTXSERW: WEST BOUNDARY CELL TOXIC CONTAMINANT CONC TIME SERIES ID NUM.<br>* NSDSERW: WEST BOUNDARY CELL COHESIVE SED CONC TIME SERIES ID NUMBER<br>* NSNSERW: WEST BOUNDARY CELL NON-COHESIVE SED CONC TIME SERIES ID NUMBER<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C52 IBBW JBBW NTSCRW NSSERW NTSERW NDSERW NSFSERW NTXSERW NSDSERW<br><br>˓→NSNSERW GRPID ! ID|
|---|


##### card53

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C53 TIME CONSTANT BOTTOM CONC ON WEST CONC BOUNDARIES<br><br>*<br><br>* SAL: ULTIMATE INFLOWING BOTTOM LAYER SALINITY<br>* TEM: ULTIMATE INFLOWING BOTTOM LAYER TEMPERATURE<br>* DYE: ULTIMATE INFLOWING BOTTOM LAYER DYE CONCENTRATION<br>* SFL: ULTIMATE INFLOWING BOTTOM LAYER SHELLFISH LARVAE CONCENTRATION<br>* TOX: NTOX ULTIMATE INFLOWING BOTTOM LAYER TOXIC CONTAMINANT<br>* CONCENTRATIONS NTOX VALUES TOX(N), N=1,NTOX<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C53 SAL TEM DYE1 SFL GRPID ! ID|
|---|


##### 1.3. Input Files 50



<<<PAGE 53>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card54

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C54 TIME CONSTANT BOTTOM CONC ON WEST CONC BOUNDARIES<br><br>*<br><br>* SED: NSED ULTIMATE INFLOWING BOTTOM LAYER COHESIVE SEDIMENT<br>* CONCENTRATIONS FIRST NSED VALUES SED(N), N=1,NSND<br>* SND: NSND ULTIMATE INFLOWING BOTTOM LAYER NON-COHESIVE SEDIMENT<br>* CONCENTRATIONS LAST NSND VALUES SND(N), N=1,NSND<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C54 SED1 SED2 SED3 SED4 SED5 SED6 SED7<br><br>˓→ SED8 GRPID ! ID|
|---|


##### card55

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C55 TIME CONSTANT SURFACE CONC ON WEST CONC BOUNDARIES<br><br>*<br><br>* SAL: ULTIMATE INFLOWING SURFACE LAYER SALINITY<br>* TEM: ULTIMATE INFLOWING SURFACE LAYER TEMPERATURE<br>* DYE: ULTIMATE INFLOWING SURFACE LAYER DYE CONCENTRATION<br>* SFL: ULTIMATE INFLOWING SURFACE LAYER SHELLFISH LARVAE CONCENTRATION<br>* TOX: NTOX ULTIMATE INFLOWING SURFACE LAYER TOXIC CONTAMINANT<br>* CONCENTRATIONS NTOX VALUES TOX(N), N=1,NTOX<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C55 SAL TEM DYE1 SFL GRPID ! ID|
|---|


##### card56

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C56 TIME CONSTANT SURFACE CONC ON WEST CONC BOUNDARIES<br><br>*<br><br>* SED: NSED ULTIMATE INFLOWING SURFACE LAYER COHESIVE SEDIMENT<br>* CONCENTRATIONS FIRST NSED VALUES SED(N), N=1,NSND<br>* SND: NSND ULTIMATE INFLOWING SURFACE LAYER NON-COHESIVE SEDIMENT<br>* CONCENTRATIONS LAST NSND VALUES SND(N), N=1,NSND<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C56 SED1 SED2 SED3 SED4 SED5 SED6 SED7<br><br>˓→ SED8 GRPID ! ID|
|---|


##### 1.3. Input Files 51



<<<PAGE 54>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card57

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C57 LOCATION OF CONC BC'S ON EAST BOUNDARIES AND SERIES IDENTIFIERS<br><br>*<br><br>* ICBE: I CELL INDEX<br>* JCBE: J CELL INDEX<br>* NTSCRE: NUMBER OF TIME STEPS TO RECOVER SPECIFIED VALUES ON CHANGE<br>* TO INFLOW FROM OUTFLOW<br>* NSSERE: EAST BOUNDARY CELL SALINITY TIME SERIES ID NUMBER<br>* NTSERE: EAST BOUNDARY CELL TEMPERATURE TIME SERIES ID NUMBER<br>* NDSERE: EAST BOUNDARY CELL DYE CONC TIME SERIES ID NUMBER<br>* NSFSERE: EAST BOUNDARY CELL SHELLFISH LARVAE TIME SERIES ID NUMBER<br>* NTXSERE: EAST BOUNDARY CELL TOXIC CONTAMINANT CONC TIME SERIES ID NUM.<br>* NSDSERE: EAST BOUNDARY CELL COHESIVE SED CONC TIME SERIES ID NUMBER<br>* NSNSERE: EAST BOUNDARY CELL NON-COHESIVE SED CONC TIME SERIES ID NUMBER<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C57 IBBE JBBE NTSCRE NSSERE NTSERE NDSERE NSFSERE NTXSERE NSDSERE<br><br>˓→NSNSERE GRPID ! ID|
|---|


##### card58

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C58 TIME CONSTANT BOTTOM CONC ON EAST CONC BOUNDARIES<br><br>*<br><br>* SAL: ULTIMATE INFLOWING BOTTOM LAYER SALINITY<br>* TEM: ULTIMATE INFLOWING BOTTOM LAYER TEMPERATURE<br>* DYE: ULTIMATE INFLOWING BOTTOM LAYER DYE CONCENTRATION<br>* SFL: ULTIMATE INFLOWING BOTTOM LAYER SHELLFISH LARVAE CONCENTRATION<br>* TOX: NTOX ULTIMATE INFLOWING BOTTOM LAYER TOXIC CONTAMINANT<br>* CONCENTRATIONS NTOX VALUES TOX(N), N=1,NTOX<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C58 SAL TEM DYE1 SFL GRPID ! ID|
|---|


##### card59

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C59 TIME CONSTANT BOTTOM CONC ON EAST CONC BOUNDARIES<br><br>*<br><br>* SED: NSED ULTIMATE INFLOWING BOTTOM LAYER COHESIVE SEDIMENT<br>* CONCENTRATIONS FIRST NSED VALUES SED(N), N=1,NSND<br>* SND: NSND ULTIMATE INFLOWING BOTTOM LAYER NON-COHESIVE SEDIMENT<br>* CONCENTRATIONS LAST NSND VALUES SND(N), N=1,NSND<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C59 SED1 SED2 SED3 SED4 SED5 SED6 SED7<br><br>˓→ SED8 GRPID ! ID (8 SEDS + 0 SNDS)|
|---|


##### 1.3. Input Files 52



<<<PAGE 55>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card60

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C60 TIME CONSTANT SURFACE CONC ON EAST CONC BOUNDARIES<br><br>*<br><br>* SAL: ULTIMATE INFLOWING SURFACE LAYER SALINITY<br>* TEM: ULTIMATE INFLOWING SURFACE LAYER TEMPERATURE<br>* DYE: ULTIMATE INFLOWING SURFACE LAYER DYE CONCENTRATION<br>* SFL: ULTIMATE INFLOWING SURFACE LAYER SHELLFISH LARVAE CONCENTRATION<br>* TOX: NTOX ULTIMATE INFLOWING SURFACE LAYER TOXIC CONTAMINANT<br>* CONCENTRATIONS NTOX VALUES TOX(N), N=1,NTOX<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C60 SAL TEM DYE1 SFL GRPID ! ID|
|---|


##### card61

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C61 TIME CONSTANT SURFACE CONC ON EAST CONC BOUNDARIES<br><br>*<br><br>* SED: NSED ULTIMATE INFLOWING SURFACE LAYER COHESIVE SEDIMENT<br>* CONCENTRATIONS FIRST NSED VALUES SED(N), N=1,NSND<br>* SND: NSND ULTIMATE INFLOWING SURFACE LAYER NON-COHESIVE SEDIMENT<br>* CONCENTRATIONS LAST NSND VALUES SND(N), N=1,NSND<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C61 SED1 SED2 SED3 SED4 SED5 SED6 SED7<br><br>˓→ SED8 GRPID ! ID (8 SEDS + 0 SNDS)|
|---|


##### card62

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C62 LOCATION OF CONC BC'S ON NORTH BOUNDARIES AND SERIES IDENTIFIERS<br><br>*<br><br>* ICBN: I CELL INDEX<br>* JCBN: J CELL INDEX<br>* NTSCRN: NUMBER OF TIME STEPS TO RECOVER SPECIFIED VALUES ON CHANGE<br>* TO INFLOW FROM OUTFLOW<br>* NSSERN: NORTH BOUNDARY CELL SALINITY TIME SERIES ID NUMBER<br>* NTSERN: NORTH BOUNDARY CELL TEMPERATURE TIME SERIES ID NUMBER<br>* NDSERN: NORTH BOUNDARY CELL DYE CONC TIME SERIES ID NUMBER<br>* NSFSERN: NORTH BOUNDARY CELL SHELLFISH LARVAE TIME SERIES ID NUMBER<br>* NTXSERN: NORTH BOUNDARY CELL TOXIC CONTAMINANT CONC TIME SERIES ID NUM.<br>* NSDSERN: NORTH BOUNDARY CELL COHESIVE SED CONC TIME SERIES ID NUMBER<br>* NSNSERN: NORTH BOUNDARY CELL NON-COHESIVE SED CONC TIME SERIES ID NUMBER<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C62 IBBN JBBN NTSCRN NSSERN NTSERN NDSERN NSFSERN NTXSERN NSDSERN<br><br>˓→NSNSERN GRPID ! ID|
|---|


##### 1.3. Input Files 53



<<<PAGE 56>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card63

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C63 TIME CONSTANT BOTTOM CONC ON NORTH CONC BOUNDARIES<br><br>*<br><br>* SAL: ULTIMATE INFLOWING BOTTOM LAYER SALINITY<br>* TEM: ULTIMATE INFLOWING BOTTOM LAYER TEMPERATURE<br>* DYE: ULTIMATE INFLOWING BOTTOM LAYER DYE CONCENTRATION<br>* SFL: ULTIMATE INFLOWING BOTTOM LAYER SHELLFISH LARVAE CONCENTRATION<br>* TOX: NTOX ULTIMATE INFLOWING BOTTOM LAYER TOXIC CONTAMINANT<br>* CONCENTRATIONS NTOX VALUES TOX(N), N=1,NTOX<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C63 SAL TEM DYE1 SFL GRPID ! ID|
|---|


##### card64

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C64 TIME CONSTANT BOTTOM CONC ON NORTH CONC BOUNDARIES<br><br>*<br><br>* SED: NSED ULTIMATE INFLOWING BOTTOM LAYER COHESIVE SEDIMENT<br>* CONCENTRATIONS FIRST NSED VALUES SED(N), N=1,NSND<br>* SND: NSND ULTIMATE INFLOWING BOTTOM LAYER NON-COHESIVE SEDIMENT<br>* CONCENTRATIONS LAST NSND VALUES SND(N), N=1,NSND<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C64 SED1 SED2 SED3 SED4 SED5 SED6 SED7<br><br>˓→ SED8 GRPID ! ID|
|---|


##### card65

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C65 TIME CONSTANT SURFACE CONC ON NORTH CONC BOUNDARIES<br><br>*<br><br>* SAL: ULTIMATE INFLOWING SURFACE LAYER SALINITY<br>* TEM: ULTIMATE INFLOWING SURFACE LAYER TEMPERATURE<br>* DYE: ULTIMATE INFLOWING SURFACE LAYER DYE CONCENTRATION<br>* SFL: ULTIMATE INFLOWING SURFACE LAYER SHELLFISH LARVAE CONCENTRATION<br>* TOX: NTOX ULTIMATE INFLOWING SURFACE LAYER TOXIC CONTAMINANT<br>* CONCENTRATIONS NTOX VALUES TOX(N), N=1,NTOX<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C65 SAL TEM DYE1 SFL GRPID ! ID|
|---|


##### 1.3. Input Files 54



<<<PAGE 57>>>

EFDC+ Computer Implementation Guide, Release 8.5.0

card66



|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C66 TIME CONSTANT SURFACE CONC ON NORTH CONC BOUNDARIES<br><br>*<br><br>* SED: NSED ULTIMATE INFLOWING SURFACE LAYER COHESIVE SEDIMENT<br>* CONCENTRATIONS FIRST NSED VALUES SED(N), N=1,NSND<br>* SND: NSND ULTIMATE INFLOWING SURFACE LAYER NON-COHESIVE SEDIMENT<br>* CONCENTRATIONS LAST NSND VALUES SND(N), N=1,NSND<br>* GRPID: ID NUMBER OF BOUNDARY GROUP<br><br><br>* C66 SED1 SED2 SED3 SED4 SED5 SED6 SED7<br><br>˓→ SED8 GRPID ! ID|
|---|


Card66a

|-----------------------------------------------------------------------------C66A CONCENTRATION DATA ASSIMILATION<br><br>*<br><br>* NLCDA: NUMBER OF HORIZONTAL LOCATIONS FOR DATA ASSIMILATION<br>* TSCDA: WEIGHTING FACTOR, 0 to 1, 1 = FULL ASSIMILATION<br>* ISCDA: 1 FOR CONCENTRATION DATA ASSIMILATION VALUES (NC=1,7)<br><br><br>* C66A NLCDA TSCDA ISCDA|
|---|


- card66b


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C66B CONCENTRATION DATA ASSIMILATION<br><br>*<br><br>* ITPCDA: 0 ASSIMILATED DATA FROM TIME SERIES<br>* 1 ASSIMILATED DATA FROM ANOTHER CELL IN GRID<br>* ICDA: I INDEX OF CELL ASSIMILATING DATA<br>* JCDA: J INDEX OF CELL ASSIMILATING DATA<br>* ICCDA: I INDEX OF CELL PROVIDING DATA, ITPCDA=1<br>* JCCDA: J INDEX OF CELL PROVIDING DATA, ITPCDA=1<br>* NCSERA: ID OF TIME SERIES PROVIDING DATA<br><br><br>* C66B ITPCDA ICDA JCDA ICCDA JCCDA NS NT ND NSF<br><br>˓→ NTX NSD NSN|
|---|


##### 1.3. Input Files 55



<<<PAGE 58>>>

EFDC+ Computer Implementation Guide, Release 8.5.0

card67



|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C67 DRIFTER DATA (FIRST 4 PARAMETERS FOR SUB DRIFTER, SECOND 6 FOR SUB<br><br>˓→LAGRANGIAN)<br><br>*<br><br>* ISPD: 1 TO ACTIVE SIMULTANEOUS RELEASE AND LAGRANGIAN TRANSPORT OF<br>* NEUTRALLY BUOYANT PARTICLE DRIFTERS AT LOCATIONS INPUT ON C68<br>* 2 TO ACTIVATE DS-INTERNATIONAL'S LPT DRIFTER COMPUTATIONS ˓→(DRIFTER.INP)<br><br>* NPD: NUMBER OF PARTICLE DRIFTERS<br>* NPDRT: TIME STEP AT WHICH PARTICLES ARE RELEASED<br>* NWPD: NUMBER OF TIME STEPS BETWEEN WRITING TO TRACKING FILE<br>* DRIFTER.OUT<br>* ISLRPD: 1 TO ACTIVATE CALCULATION OF LAGRANGIAN MEAN VELOCITY OVER TIME<br>* INTERVAL TREF AND SPATIAL INTERVAL ILRPD1<I<ILRPD2,<br>* JLRPD1<J<JLRPD2, 1<K<KC, WITH MLRPDRT RELEASES. ANY AVERAGE<br>* OVER ALL RELEASE TIMES IS ALSO CALCULATED<br>* 2 SAME BUT USES A HIGHER ORDER TRAJECTORY INTEGRATION<br>* ILRPD1 WEST BOUNDARY OF REGION<br>* ILRPD2 EAST BOUNDARY OF REGION<br>* JLRPD1 NORTH BOUNDARY OF REGION<br>* JLRPD2 SOUTH BOUNDARY OF REGION<br>* MLRPDRT NUMBER OF RELEASE TIMES<br>* IPLRPD 1,2,3 WRITE FILES TO PLOT ALL,EVEN,ODD HORIZ LAG VEL VECTORS<br><br><br>* C67 ISPD NPD NPDRT NWPD ISLRPD ILRPD1 ILRPD2 JLRPD1 JLRPD2<br><br>˓→MLRPDRT IPLRPD|
|---|


##### card68

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C68 INITIAL DRIFTER POSITIONS (FOR USE WITH SUB DRIFTER)<br><br>*<br><br>* RI: I CELL INDEX IN WHICH PARTICLE IS RELEASED IN<br>* RJ: J CELL INDEX IN WHICH PARTICLE IS RELEASED IN<br>* RK: K CELL INDEX IN WHICH PARTICLE IS RELEASED IN<br><br><br>* C68 RI RJ RK|
|---|


##### card69

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C69 CONSTANTS FOR CARTESIAN GRID CELL CENTER LONGITUDE AND LATITUDE<br><br>*<br><br>* CDLON1: 6 CONSTANTS TO GIVE CELL CENTER LAT AND LON OR OTHER<br>* CDLON2: COORDINATES FOR CARTESIAN GRIDS USING THE FORMULAS<br>* CDLON3: DLON(L)=CDLON1+(CDLON2*FLOAT(I)+CDLON3)/60.<br>* CDLAT1: DLAT(L)=CDLAT1+(CDLAT2*FLOAT(J)+CDLAT3)/60.<br>* CDLAT2:<br>|
|---|


(continues on next page)

##### 1.3. Input Files 56



<<<PAGE 59>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



(continued from previous page)

|* CDLAT3:<br>* C69 CDLON1 CDLON2 CDLON3 CDLAT1 CDLAT2 CDLAT3<br>|
|---|


##### card70

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C70 CONTROLS FOR WRITING ASCII OR BINARY DUMP FILES<br><br>*<br><br>* ISDUMP: GREATER THAN 0 TO ACTIVATE<br>* 1 SCALED ASCII INTEGER (0<VAL<65535)<br>* 2 SCALED 16BIT BINARY INTEGER (0<VAL<65535) OR (-32768<VAL<32767)<br>* 3 UNSCALED ASCII FLOATING POINT<br>* 4 UNSCALED BINARY FLOATING POINT<br>* ISADMP: GREATER THAN 0 TO APPEND EXISTING DUMP FILES<br>* NSDUMP: NUMBER OF TIME STEPS BETWEEN DUMPS<br>* TSDUMP: STARTING TIME FOR DUMPS - DAYS (NO DUMPS BEFORE THIS TIME)<br>* TEDUMP: ENDING TIME FOR DUMPS - DAYS (NO DUMPS AFTER THIS TIME)<br>* ISDMPP: GREATER THAN 0 FOR WATER SURFACE ELEVATION DUMP<br>* ISDMPU: GREATER THAN 0 FOR HORIZONTAL VELOCITY DUMP<br>* ISDMPW: GREATER THAN 0 FOR VERTICAL VELOCITY DUMP<br>* ISDMPT: GREATER THAN 0 FOR TRANSPORTED VARIABLE DUMPS<br>* IADJDMP: 0 FOR SCALED BINARY INTEGERS (0<VAL<65535)<br>* -32768 FOR SCALED BINARY INTEGERS (-32768<VAL<32767)<br><br><br>* C70 ISDUMP ISADMP NSDUMP TSDUMP TEDUMP ISDMPP ISDMPU ISDMPW ISDMPT<br><br>˓→IADJDMP|
|---|


##### card71

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C71 CONTROLS FOR HORIZONTAL PLANE SCALAR FIELD CONTOURING - RESIDUAL ONLY<br><br>*<br><br>* ISSPH: NOT USED<br><br>*<br><br>* NPSPH: NOT USED<br>* ISRSPH: 1 TO WRITE FILE FOR RESIDUAL SCALAR VARIABLE IN HORIZONTAL PLANE<br><br>*<br><br>* ISPHXY: 0 DOES NOT WRITE I,J,X,Y IN ***CNH.OUT AND R***CNH.OUT FILES ˓→(RESIDUAL ONLY)<br><br>* 1 WRITES I,J ONLY IN ***CNH.OUT AND R***CNH.OUT FILES (RESIDUAL ˓→ONLY)<br><br>* 2 WRITES I,J,X,Y IN ***CNH.OUT AND R***CNH.OUT FILES (RESIDUAL ˓→ONLY) *<br>* DATA LINE REPEATS 7 TIMES FOR SAL,TEM,DYE,SFL,TOX,SED,SND<br>* C71 ISSPH NPSPH ISRSPH ISPHXY<br><br><br>|
|---|


##### 1.3. Input Files 57



<<<PAGE 60>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



card71a

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C71A CONTROLS FOR HORIZONTAL PLANE SEDIMENT BED PROPERTIES CONTOURING<br><br>*<br><br>* ISBPH: NOT USED<br><br>*<br><br>* ISBEXP: 0 >0 EXPLORER BINARY FORMAT, OUTPUT FREQUENCY<br>* NPBPH: NOT USED<br>* ISRBPH: NOT USED<br>* ISBBDN: NOT USED<br>* ISBLAY: NOT USED<br>* ISBPOR: NOT USED<br>* SBSED: NOT USED<br><br>*<br><br>* ISBSED: NOT USED<br><br>*<br><br>* ISBVDR: NOT USED<br>* ISBARD: NOT USED<br><br><br>* C71A ISBPH ISBEXP NPBPH ISRBPH ISBBDN ISBLAY ISBPOR ISBSED ISBSND<br><br>˓→ISBVDR ISBARD|
|---|


card71b

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C71B FOOD CHAIN MODEL OUTPUT CONTROL<br><br>*<br><br>* ISFDCH: 1 TO WRITE OUTPUT FOR HOUSATONIC RIVER FOOD CHAIN MODEL<br>* NFDCHZ: NUMBER OF SPATIAL ZONES<br>* HBFDCH: AVERAGING DEPTH FOR TOP PORTION OF BED (METERS)<br>* TFCAVG: TIME AVERAGING INTERVAL FOR FOOD CHAIN OUTPUT (SECONDS)<br><br><br>* C71B ISFDCH NFDCHZ HBFDCH TFCAVG|
|---|


- card72


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C72 CONTROLS FOR EFDC_EXPLORER LINKAGE<br><br>*<br><br>* ISPPH: >0 TO WRITE FILE FOR EFDC_EXPLORER LINKAGE (EE_WS.OUT, EE_VEL. ˓→OUT, EE_WC.OUT)<br>* 100 TO ACTIVATE THE HIGH FREQUENCY DOMAIN OUTPUT READING SNAPSHOT. ˓→INP<br>* NPPPH: NUMBER OF WRITES PER REFERENCE TIME PERIOD<br>* ISBEXP: 0 DO NOT WRITE SEDIMENT BED RESULTS TO EE_BED.OUT<br>* >0 WRITE TO EE_BED EVERY ISBEXP EE LINKAGE SNAPSHOTS<br><br><br>* C72 ISPPH NPPPH ISBEXP NRPEMEE|
|---|


##### 1.3. Input Files 58



<<<PAGE 61>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card73

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C73 CONTROLS FOR HORIZONTAL PLANE RESIDUAL VELOCITY VECTOR PLOTTING<br><br>*<br><br>* ISVPH: NOT USED<br>* NOT USED<br>* NPVPH: NOT USED<br>* ISRVPH: 1 TO WRITE FILE FOR RESIDUAL VELOCITY PLOTTING IN<br>* HORIZONTAL PLANE<br>* IVPHXY: NOT USED<br>* NOT USED<br>* NOT USED<br>* NOT USED<br><br><br>* C73 ISVPH NPVPH ISRVPH IVPHXY|
|---|


##### card74

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C74 NOT USED<br><br>*<br><br>* ISECSPV: NOT USED<br><br>*<br><br>* NPSPV: NOT USED<br>* ISSPV: NOT USED<br><br>*<br><br>* ISRSPV: NOT USED<br>* ISHPLTV: NOT USED<br><br><br>* * * C74 ISECSPV NPSPV ISSPV ISRSPV ISHPLTV|
|---|


##### card75

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C75 NOT USED<br><br>*<br><br>* ISECSPV: NOT USED<br>* NIJSPV: NOT USED<br>* SEC ID: NOT USED<br><br><br>* C75 ISECSPV NIJSPV SEC ID|
|---|


##### 1.3. Input Files 59



<<<PAGE 62>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card76

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C76 NOT USED<br><br>*<br><br>* ISECSPV: NOT USED<br>* ISPV: NOT USED<br>* JSPV: NOT USED<br><br><br>* C76 ISECSPV ISPV JSPV|
|---|


##### card77

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C77 NOT USED<br><br>*<br><br>* ISECVPV: NOT USED<br><br>*<br><br>* NPVPV: NOT USED<br>* ISVPV: NOT USED<br><br>*<br><br>* ISRSPV: NOT USED<br><br><br>* C77 ISECVPV NPVPV ISVPV ISRSPV|
|---|


##### card78

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C78 NOT USED<br><br>*<br><br>* ISCEVPV: NOT USED<br>* NIJVPV: NOT USED<br>* ANGVPV: NOT USED<br>* SEC ID: NOT USED<br><br><br>* C78 ISECVPV NIJVPV ANGVPV SEC ID|
|---|


##### card79

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C79 NOT USED<br><br>*<br><br>* ISECVPV: NOT USED<br>* IVPV: NOT USED<br>* JVPV: NOT USED<br><br><br>* C79 ISECVPV IVPV JVPV|
|---|


##### 1.3. Input Files 60



<<<PAGE 63>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### card80

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C80 CONTROLS FOR 3D FIELD OUTPUT<br><br>*<br><br>* IS3DO: 1 TO WRITE TO 3D ASCII INTEGER FORMAT FILES, JS3DVAR.LE.2 SEE|<br>* 1 TO WRITE TO 3D ASCII FLOAT POINT FORMAT FILES, JS3DVAR.EQ.3 C57|<br>* 2 TO WRITE TO 3D CHARACTER ARRAY FORMAT FILES (NOT ACTIVE)<br>* 3 TO WRITE TO 3D HDF IMAGE FORMAT FILES (NOT ACTIVE)<br>* 4 TO WRITE TO 3D HDF FLOATING POINT FORMAT FILES (NOT ACTIVE)<br>* ISR3DO: SAME AS IS3DO EXCEPT FOR RESIDUAL VARIABLES<br>* NP3DO: NUMBER OF WRITES PER LAST REF TIME PERIOD FOR INST VARIABLES<br>* KPC: NUMBER OF UNSTRETCHED PHYSICAL VERTICAL LAYERS<br>* NWGG: IF NWGG IS GREATER THAN ZERO, NWGG DEFINES THE NUMBER OF !2877|<br>* WATER CELLS IN CARTESIAN 3D GRAPHICS GRID OVERLAY OF THE<br>* CURVILINEAR GRID. FOR NWGG>0 AND EFDC RUNS ON A CURVILINEAR<br>* GRID, I3DMI,I3DMA,J3DMI,J3DMA REFER TO CELL INDICES ON THE<br>* ON THE CARTESIAN GRAPHICS GRID OVERLAY DEFINED BY FILE<br>* GCELL.INP. THE FILE GCELL.INP IS NOT USED BY EFDC, BUT BY<br>* THE COMPANION GRID GENERATION CODE GEFDC.F. INFORMATION<br>* DEFINING THE OVERLAY IS READ BY EFDC.F FROM THE FILE<br>* GCELLMP.INP. IF NWGG EQUALS 0, I3DMI,I3DMA,J3DMI,J3DMA REFER<br>* TO INDICES ON THE EFDC GRID DEFINED BY CELL.INP.<br>* ACTIVATION OF THE REWRITE OPTION I3DRW=1 WRITES TO THE FULL<br>* GRID DEFINED BY CELL.INP AS IF CELL.INP DEFINES A CARTESIAN<br>* GRID. IF NWGG EQ 0 AND THE EFDC COMP GRID IS CO, THE REWRITE<br>* OPTION IS NOT RECOMMENDED AND A POST PROCESSOR SHOULD BE USED<br>* TO TRANSFER THE SHORT FORM, I3DRW=0, OUTPUT TO AN APPROPRIATE<br>* FORMAT FOR VISUALIZATION. CONTACT DEVELOPER FOR MORE DETAILS<br>* I3DMI: MINIMUM OR BEGINNING I INDEX FOR 3D ARRAY OUTPUT<br>* I3DMA: MAXIMUM OR ENDING I INDEX FOR 3D ARRAY OUTPUT<br>* J3DMI: MINIMUM OR BEGINNING J INDEX FOR 3D ARRAY OUTPUT<br>* J3DMA: MAXIMUM OR ENDING J INDEX FOR 3D ARRAY OUTPUT<br>* I3DRW: 0 FILES WRITTEN FOR ACTIVE CO WATER CELLS ONLY<br>* 1 REWRITE FILES TO CORRECT ORIENTATION DEFINED BY GCELL.INP<br>* AND GCELLMP.INP FOR CO WITH NWGG.GT.O OR BY CELL.INP IF THE<br>* COMPUTATIONAL GRID IS CARTESIAN AND NWGG.EQ.0<br>* SELVMAX: MAXIMUM SURFACE ELEVATION FOR UNSTRETCHING (ABOVE MAX SELV )<br>* BELVMIN: MINIMUM BOTTOM ELEVATION FOR UNSTRETCHING (BELOW MIN BELV)<br><br><br>* C80 IS3DO ISR3DO NP3DO KPC NWGG I3DMI I3DMA J3DMI J3DMA<br><br>˓→ I3DRW SELVMAX BELVMIN|
|---|


##### card81

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C81 OUTPUT ACTIVATION AND SCALES FOR 3D FIELD OUTPUT<br><br>*<br><br>* VARIABLE: DUMMY VARIABLE ID (DO NOT CHANGE ORDER)<br>* IS3(VARID): 1 TO ACTIVATE THIS VARIABLE<br>* JS3(VARID): 0 FOR NO SCALING OF THIS VARIABLE<br>* 1 FOR AUTO SCALING OF THIS VARIABLE OVER RANGE 0<VAL<255<br>* AUTO SCALES FOR EACH FRAME OUTPUT IN FILES OUT3D.DIA AND<br>|
|---|


(continues on next page)

##### 1.3. Input Files 61



<<<PAGE 64>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* ROUT3D.DIA OUTPUT IN I4 FORMAT<br>* 2 FOR SCALING SPECIFIED IN NEXT TWO COLUMNS WITH OUTPUT<br>* DEFINED OVER RANGE 0<VAL<255 AND WRITTEN IN I4 FORMAT<br>* 3 FOR MULTIPLIER SCALING BY MAX SCALE VALUE WITH OUTPUT<br>* WRITTEN IN F7.2 FORMAT (IS3DO AND ISR3DO MUST BE 1)<br><br><br>* C81 VARIABLE IS3D JS3D SMAX SMIN|
|---|


##### card82

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C82 INPLACE HARMONIC ANALYSIS PARAMETERS<br><br>*<br><br>* ISLSHA: 1 FOR IN PLACE LEAST SQUARES HARMONIC ANALYSIS<br>* MLLSHA: NUMBER OF LOCATIONS FOR LSHA<br>* NTCLSHA: LENGTH OF LSHA IN INTEGER NUMBER OF REFERENCE TIME PERIODS<br>* ISLSTR: 1 FOR TREND REMOVAL<br>* ISHTA : 1 FOR SINGLE TREF PERIOD SURFACE ELEV ANALYSIS<br>* 90 C82 ISLSHA MLLSHA NTCLSHA ISLSTR ISHTA<br>|
|---|


##### card83

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C83 HARMONIC ANALYSIS LOCATIONS AND SWITCHES<br><br>*<br><br>* ILLSHA: I CELL INDEX<br>* JLLSHA: J CELL INDEX<br>* LSHAP: 1 FOR ANALYSIS OF SURFACE ELEVATION<br>* LSHAB: 1 FOR ANALYSIS OF SALINITY<br>* LSHAUE: 1 FOR ANALYSIS OF EXTERNAL MODE HORIZONTAL VELOCITY<br>* LSHAU: 1 FOR ANALYSIS OF HORIZONTAL VELOCITY IN EVERY LAYER<br>* CLSL: LOCATION AS A CHARACTER VARIABLE<br><br><br>* C83 ILLSHA JLLSHA LSHAP LSHAB LSHAUE LSHAU CLSL|
|---|


##### card84

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C84 CONTROLS FOR WRITING TO TIME SERIES FILES<br><br>*<br><br>* ISTMSR: 1 OR 2 TO WRITE TIME SERIES OF SURF ELEV, VELOCITY, NET<br>* INTERNAL AND EXTERNAL MODE VOLUME SOURCE-SINKS, AND<br>* CONCENTRATION VARIABLES, 2 APPENDS EXISTING TIME SERIES FILES<br>* MLTMSR: NUMBER HORIZONTAL LOCATIONS TO WRITE TIME SERIES OF SURF ELEV,<br>* VELOCITY, AND CONCENTRATION VARIABLES<br>* NBTMSR: TIME STEP TO BEGIN WRITING TO TIME SERIES FILES (Inactive)<br>|
|---|


(continues on next page)

##### 1.3. Input Files 62



<<<PAGE 65>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* NSTMSR: TIME STEP TO STOP WRITING TO TIME SERIES FILES (Inactive)<br>* NWTMSR: NUMBER OF TIME STEPS TO SKIP BETWEEN OUTPUT<br>* NTSSTSP: NUMBER OF TIME SERIES START-STOP SCENARIOS, 1 OR GREATER<br>* TCTMSR: UNIT CONVERSION FOR TIME SERIES TIME. FOR SECONDS, MINUTES,<br>* HOURS,DAYS USE 1.0, 60.0, 3600.0, 86400.0 RESPECTIVELY<br><br><br>* * C84 ISTMSR MLTMSR NBTMSR NSTMSR NWTMSR NTSSTSP TCTMSR|
|---|


##### card85

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C85 CONTROLS FOR WRITING TO TIME SERIES FILES<br><br>*<br><br>* ITSSS: START-STOP SCENARIO NUMBER 1.GE.ISSS.LE.NTSSTSP<br>* MTSSTSP: NUMBER OF STOP-START PAIRS FOR SCENARIO ISSS<br><br><br>* C85 ITSSS MTSSTSP|
|---|


##### card86

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C86 CONTROLS FOR WRITING TO TIME SERIES FILES<br><br>*<br><br>* ITSSS: START-STOP SCENARIO NUMBER 1.GE.ISSS.LE.NTSSTSP<br>* MTSSS: NUMBER OF STOP-START PAIRS FOR SCENARIO ISSS<br>* TSSTRT: STARTING TIME FOR SCENARIO ITSSS, SAVE INTERVAL MTSSS<br>* TSSTOP: STOPPING TIME FOR SCENARIO ITSSS, SAVE INTERVAL MTSSS<br>* -1000. C86 ISSS MTSSS TSSTRT TSSTOP COMMENT<br>|
|---|


##### card87

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C87 CONTROLS FOR WRITING TO TIME SERIES FILES<br><br>*<br><br>* ILTS: I CELL INDEX<br>* JLTS: J CELL INDEX<br>* NTSSSS: WRITE SCENARIO FOR THIS LOCATION<br>* MTSP: 1 FOR TIME SERIES OF SURFACE ELEVATION<br>* MTSC: 1 FOR TIME SERIES OF TRANSPORTED CONCENTRATION VARIABLES<br>* MTSA: 1 FOR TIME SERIES OF EDDY VISCOSITY AND DIFFUSIVITY<br>* MTSUE: 1 FOR TIME SERIES OF EXTERNAL MODE HORIZONTAL VELOCITY<br>* MTSUT: 1 FOR TIME SERIES OF EXTERNAL MODE HORIZONTAL TRANSPORT<br>* MTSU: 1 FOR TIME SERIES OF HORIZONTAL VELOCITY IN EVERY LAYER<br>* MTSQE: 1 FOR TIME SERIES OF NET EXTERNAL MODE VOLUME SOURCE/SINK<br>|
|---|


(continues on next page)

##### 1.3. Input Files 63



<<<PAGE 66>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|* MTSQ: 1 FOR TIME SERIES OF NET EXTERNAL MODE VOLUME SOURCE/SINK<br>* CLTS: LOCATION AS A CHARACTER VARIABLE<br><br><br>* C87 ILTS JLTS NTSSSS MTSP MTSC MTSA MTSUE MTSUT MTSU<br><br>˓→ MTSQE MTSQ CLTS|
|---|


##### card88

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C88 High frequency output for specific locations and times<br><br>*<br><br>* HFREOUT: 1 use high frequency dates for output<br>* 0 specific output option is not used<br><br><br>* C88 HFREOUT|
|---|


##### card89

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C89 NOT USED<br><br>*<br><br>* MMDVSFP: NOT USED<br>* DMSFP: NOT USED<br><br><br>* C89 MMDVSFP DMVSFP|
|---|


##### card90

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C90 NOT USED<br><br>*<br><br>* MMLVSFP: NOT USED<br>* TIMVSFP: NOT USED<br>* IVSFP: NOT USED<br>* JVSFP: NOT USED<br><br><br>* C90 MMLVSFP TIMVSFP IVSFP JVSFP|
|---|


##### 1.3. Input Files 64



<<<PAGE 67>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



- card91


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C91 OPTIONS FOR GENERATION OF NETCDF FILE(S)<br><br>*<br><br>* NCDFOUT: OPTION FOR NETCDF EXPORT<br>* =1 GENERATE NETCDF FILE NC<br>* =0 NO GENERATION<br>* DEFLEV: LEVEL OF COMPRESSION OF NETCDF FILE FROM 0 TO 9<br>* ROTA: =1 ROTATING 2D VELOCITY FIELD TO THE TRUE EAST AND TRUE ˓→NORTH<br><br>* =0 NO ROTATION TO TRUE EAST AND TRUE NORTH<br>* UTMZ: UTM ZONE<br>* >0 FOR NORTHERN HEMISPHERE; <0 FOR SOUTHERN HEMISPHERE, ˓→0 TO IGNORE<br><br>* BASEDATE: YYYY-MM-DD (NO BLANK)<br>* BASETIME: HH:MM:SS (NO BLANK)<br>* PROJ: PROJECT NAME IS A STRING OF MAXIMUM LENGTH 20<br>* WITHOUT ANY BLANKS<br><br><br>* C91 NCDFOUT DEFLEV ROTA BLK UTMZ HREST BASEDATE BASETIME<br><br>˓→PROJ|
|---|


- card91a

|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C91A OPTIONS FOR NETCDF OUTPUT<br><br>*<br><br>* TYPE File creation option<br>* =1: Single file<br>* =0: Multiple daily files<br>* BEGIN Start julian day of writing netcdf file<br>* END End julian day of writing netcdf file C91A TYPE BEGIN END<br>|
|---|


- card91b


|-----------------------------------------------------------------------------<br><br>˓→-<br><br>C91B OPTIONS FOR NETCDF OUTPUT<br><br>*<br><br>* ISNCDF(I) OPTION FOR OUTPUT, I=1:12<br>* = 0: NO<br>* = 1: YES<br><br>*<br><br>* 1 2 3 4 5 6 7 8 9 ˓→ 10 11 12<br><br><br>C91B SAL TEM DYE SLF TOX SED SND WQL LPT<br><br>˓→ SHR WIN WAV|
|---|


##### 1.3. Input Files 65



<<<PAGE 68>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



#### 1.3.2 Required Spatial Files

|Input File<br><br>|Description|
|---|---|
|cell.inp<br><br>|Describes the cell mapping and which type of cell goes where.|
|celllt.inp<br><br>|Auxiliary cell type ﬁle|
|dxdy.inp|Horizontal cell dimensions, depth, bottom elevation, roughness, vegetation class|
|lxly.inp<br><br>|Horizontal cell center coordinates and cell orientation|
|corners.inp<br><br>|Provides x,y coordinates corners for Lagrangian Particle Tracking module|


##### Optional Spatial Files

|Input File<br><br>|Description|
|---|---|
|mask.inp|Speciﬁes thin barriers if NMASK > 0|
|layermask.inp<br><br>|Speciﬁes thin barriers for layer faces if NBLOCKED > 0 (for EFDC+ 10.1 and later)|
|mappgns.inp<br><br>|Speciﬁes north-south (J/V face) direction grid connections|
|mappgew.inp<br><br>|Speciﬁes east-west (I/U face) direction grid connections|
|moddxdy.inp<br><br>|Modiﬁes cell dimensions originally speciﬁed in dxdy.inp|
|sgzlayer.inp<br><br>|Speciﬁes the bottom active water layer if IGRIDV=1|


The primary input ﬁles that specify the geometry of the problem are given in greater detail below.

##### Cell Input File

The cell.inp ﬁle is a 2x2 matrix with length in the i or x direction equal to IC and a length in the j or y direction of JC. IC and JC are speciﬁed on card9 of EFDC.INP

In the table below each cell type is described. These numbers are what are inputted into the ICxJC matrix in the cell.inp ﬁle.

|Cell Number|Description|
|---|---|
|0|dry land cell not bordering a water cell on a side or corner.|
|1<br><br>|triangular water cell with land to the northeast|
|2<br><br>|triangular water cell with land to the southeast|
|3|triangular water cell with land to the southwest|
|4<br><br>|triangular water cell with land to the northwest|
|5|quadrilateral water cell|
|9<br><br>|dry land cell bordering a water cell on a side or corner or a ﬁctitious dry land cell bordering an open boundary water cell on a side or a corner|


In the example ﬁle listed below IC=10 and JC=6. Note, the ﬁrst 4 rows are comments as well as the ﬁrst 4 rows. The cell mapping begins from the bottom left corner.

|C cell.inp file, i columns and j rows C 0 1 C 1234567890 C<br><br>6 999999000 5 945519999 4 955555559|
|---|


(continues on next page)

##### 1.3. Input Files 66



<<<PAGE 69>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



(continued from previous page)

|3 955555559 2 935529999 1 999999000|
|---|


##### DXDY Input File

The dxdy.inp ﬁle speciﬁes many of the physical properties of each cell. Every cell described in the cell.inp ﬁle must be described in this ﬁle.

|Variable|Description|
|---|---|
|I<br><br>|Array index in x direction|
|J|Array index in y direction|
|DX|Cell dimension in x direction, meters|
|DY<br><br>|Cell dimension in y direction, meters|
|DEPTH<br><br>|Initial water depth, meters|
|BOTTOM ELEV|Bottom bed elevation, meters|
|ZROUGH<br><br>|Log law roughness height, zo, meters|
|VEG TYPE|Vegetation type class, integer value|


Below is part of a sample input ﬁle that speciﬁes part of a single column of the geometry.

|C DXDY.INP FILE, IN FREE FORMAT ACROSS COLUMNS for the first 25 Active Cells C Project: EFDC+ Test Case C BOTTOM Veg C I J DX DY DEPTH ELEV ZROUGH TYPE<br><br>4 30 0.115800 0.021000 0.1100 0.0000 2.0000E-03<br>4 31 0.115800 0.022100 0.1100 0.0000 2.0000E-03<br>4 32 0.115800 0.023200 0.1100 0.0000 2.0000E-03<br>4 33 0.115800 0.024300 0.1100 0.0000 2.0000E-03<br>4 34 0.115800 0.025500 0.1100 0.0000 2.0000E-03<br>4 35 0.115800 0.026800 0.1100 0.0000 2.0000E-03<br>4 36 0.115800 0.028100 0.1100 0.0000 2.0000E-03<br>4 37 0.115800 0.029500 0.1100 0.0000 2.0000E-03<br>4 38 0.115800 0.031000 0.1100 0.0000 2.0000E-03<br>4 39 0.115800 0.032600 0.1100 0.0000 2.0000E-03<br>4 40 0.115800 0.034200 0.1100 0.0000 2.0000E-03<br>4 41 0.115800 0.035900 0.1100 0.0000 2.0000E-03<br>4 42 0.115800 0.037700 0.1100 0.0000 2.0000E-03<br>4 43 0.115800 0.039600 0.1100 0.0000 2.0000E-03<br>4 44 0.115800 0.041600 0.1100 0.0000 2.0000E-03<br>4 45 0.115800 0.043700 0.1100 0.0000 2.0000E-03<br>4 46 0.115800 0.045800 0.1100 0.0000 2.0000E-03<br>4 47 0.115800 0.048100 0.1100 0.0000 2.0000E-03<br>4 48 0.115800 0.050000 0.1100 0.0000 2.0000E-03<br>4 49 0.115800 0.050000 0.1100 0.0000 2.0000E-03<br>4 50 0.115800 0.050000 0.1100 0.0000 2.0000E-03<br>4 51 0.115800 0.050000 0.1100 0.0000 2.0000E-03<br>4 52 0.115800 0.050000 0.1100 0.0000 2.0000E-03<br>4 53 0.115800 0.050000 0.1100 0.0000 2.0000E-03<br>4 54 0.115800 0.050000 0.1100 0.0000 2.0000E-03<br>4 55 0.115800 0.050000 0.1100 0.0000 2.0000E-03<br>|
|---|


##### 1.3. Input Files 67



<<<PAGE 70>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



##### LXLY Input File

The lxly.inp ﬁle speciﬁes the cell centered location and the rotation of each cell.

|Variable|Description|
|---|---|
|I|Array index in x direction|
|J<br><br>|Array index in y direction|
|X<br><br>|x cell center coordinate, longitude, meters, or km|
|Y<br><br>|y cell center coordinate, longitude, meters, or km|
|CUE<br><br>|Rotation matrix component, i|
|CVE|Rotation matrix component|
|CUN<br><br>|Rotation matrix component|
|CVN<br><br>|Rotation matrix component|
|Wind Shelter| |


Below is part of a sample input ﬁle that speciﬁes part of a single column of the geometry.

|C LXLY.INP FILE, IN FREE FORMAT ACROSS LINE for 25 Active Cells C Project: EFDC+ Test Case C WIND C I J X Y CUE CVE CUN CVN SHELTER<br><br>4 30 0.045400 1.010500 1.00000 0.00000 0.00000 1.00000 0.00<br>4 31 0.045400 1.032000 1.00000 0.00000 0.00000 1.00000 0.00<br>4 32 0.045400 1.054600 1.00000 0.00000 0.00000 1.00000 0.00<br>4 33 0.045400 1.078400 1.00000 0.00000 0.00000 1.00000 0.00<br>4 34 0.045400 1.103300 1.00000 0.00000 0.00000 1.00000 0.00<br>4 35 0.045400 1.129400 1.00000 0.00000 0.00000 1.00000 0.00<br>4 36 0.045400 1.156900 1.00000 0.00000 0.00000 1.00000 0.00<br>4 37 0.045400 1.185750 1.00000 0.00000 0.00000 1.00000 0.00<br>4 38 0.045400 1.216000 1.00000 0.00000 0.00000 1.00000 0.00<br>4 39 0.045400 1.247800 1.00000 0.00000 0.00000 1.00000 0.00<br>4 40 0.045400 1.281200 1.00000 0.00000 0.00000 1.00000 0.00<br>4 41 0.045400 1.316250 1.00000 0.00000 0.00000 1.00000 0.00<br>4 42 0.045400 1.353100 1.00000 0.00000 0.00000 1.00000 0.00<br>4 43 0.045400 1.391800 1.00000 0.00000 0.00000 1.00000 0.00<br>4 44 0.045400 1.432400 1.00000 0.00000 0.00000 1.00000 0.00<br>4 45 0.045400 1.475000 1.00000 0.00000 0.00000 1.00000 0.00<br>4 46 0.045400 1.519700 1.00000 0.00000 0.00000 1.00000 0.00<br>4 47 0.045400 1.566700 1.00000 0.00000 0.00000 1.00000 0.00<br>4 48 0.045400 1.615800 1.00000 0.00000 0.00000 1.00000 0.00<br>4 49 0.045400 1.665800 1.00000 0.00000 0.00000 1.00000 0.00<br>4 50 0.045400 1.715800 1.00000 0.00000 0.00000 1.00000 0.00<br>4 51 0.045400 1.765800 1.00000 0.00000 0.00000 1.00000 0.00<br>4 52 0.045400 1.815800 1.00000 0.00000 0.00000 1.00000 0.00<br>4 53 0.045400 1.865800 1.00000 0.00000 0.00000 1.00000 0.00<br>4 54 0.045400 1.915800 1.00000 0.00000 0.00000 1.00000 0.00<br>4 55 0.045400 1.965800 1.00000 0.00000 0.00000 1.00000 0.00<br>|
|---|


##### 1.3. Input Files 68



<<<PAGE 71>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



#### 1.3.3 General Transport

Hydrodynamic Parameter Files

|Input File<br><br>|Description|
|---|---|
|AHMAP.INP|Spatially varying Smagorinsky (AHD) and background eddy viscosity (AHO) if AHD < 0.0|
|AVMAP.INP|Spatially varying AVO/ABO if AVO < 0.0|
|MAPHMD.INP|List of cells to compute horizontal momentum diffusion if IHMDSUB > 0|
|VEGE.INP|Vegetation class deﬁnitions|
|VEGSER.INP<br><br>|Vegetation class time series|
|WSER.INP|Time series ﬁle for wind speed and direction|
|WNDMAP.INP|Cell weightings ﬁle for WSER series when NWSER > 1|
|SUBSET.INP<br><br>|List of cells and timing for high frequency time series output|
|SNAPSHOTS.INP|List of additional times to write the EE_*.OUT linkage ﬁles|
|RESTART.INP|Primary restart/hot start ﬁle for hydrodynamics and most other modules|
|RSTWD.INP<br><br>|Restart ﬁle for wetting & drying parameters (ISDRY > 0)|


Volumetric and Level Boundary Conditions

|Input File|Description|
|---|---|
|QSER.INP<br><br>|Time series ﬁle for ﬂow type boundary conditions|
|PSER.INP|Time series ﬁle for pressure type open boundary conditions|
|QWRS.INP|Time series ﬁle for withdrawl-return ﬂows and concentration rise/fall|
|QCTL.INP<br><br>|Lookup tables for free surface elevation or pressure controlled ﬂow|
|QCTLSER.INP|Time series of equation based parameters control time-series|
|QCRULES.INP|Operation rules for hydraulic structure control|
|GWATER.INP<br><br>|Groundwater interaction by inﬁltration and evapotranspiration|
|GWSEEP.INP<br><br>|Groundwater interaction by ambient groundwater ﬂow|
|GWSER.INP|Groundwater inﬂow/outﬂow and concentration|
|GWMAP.INP|Spatially varying map of GSWER series ID|


Salt Module

|Input File|Description|
|---|---|
|SALT.INP<br><br>|Water column initial conditions for salinity|
|SSER.INP|Time series ﬁle for salinity boundary conditions|


Lagrangian Particle Tracking

|Input File<br><br>|Description|
|---|---|
|DRIFTER.INP|Particle group settings and particle seeding locations|


##### 1.3. Input Files 69



<<<PAGE 72>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



Shellﬁsh Module

Dye Module

|Input File|Description|
|---|---|
|SFBSER.INP<br><br>|Shellﬁsh larave behavior settings|
|SFL.INP<br><br>|Water column initial conditions for shellﬁsh|
|SFSER.INP<br><br>|Time series ﬁle for shellﬁsh boundary conditions|


|Input File<br><br>|Description|
|---|---|
|DYE.INP|Water column initial conditions for dye|
|DSER.INP<br><br>|Time series ﬁle for dye boundary conditions|


#### 1.3.4 Sediment

Original Sediment Module

|Input File<br><br>|Description|
|---|---|
|SEDW.INP|Water column initial conditions for cohesive sediments|
|SEDB.INP<br><br>|Sediment bed initial conditions for cohesive sediments|
|SDSER.INP|Time series ﬁle for cohesive boundary conditions|
|SNDW.INP|Water column initial conditions for non-cohesive sediments|
|SNDB.INP|Sediment bed initial conditions for non-cohesive sediments|
|SNSER.INP|Time series ﬁle for non-cohesive boundary conditions|
|BEDBDN.INP<br><br>|Sediment bed initial conditions for bulk density|
|BEDDDN.INP|Sediment bed initial conditions for dry density, porosity or void ratio|
|BEDLAY.INP|Sediment bed initial conditions for layer thickness|
|SEDBLBC.INP<br><br>|Non-cohesive bedload outﬂow or recirculation boundary conditions|
|SEDROUGH.INP<br><br>|Spatially varying grain roughness height for determining grain stress, ISBEDSTR = 3|
|CONSOLMAP.INP<br><br>|Spatially varying consolidation approach when IBMECH = 9|
|SSCOHSEDPMAP.INP<br><br>|Spatially varying cohesive critical bed shear stress and surface erosion rate, IWRSP(1) > 98|
|BEDMAP.INP<br><br>|Spatially varying ﬂag for hard-bottom bypass of erosion/deposition calculations|
|BEMAP.INP|Bank erosion cell map|
|BESER.INP|Bank erosion time series|


##### 1.3. Input Files 70



<<<PAGE 73>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



SEDZLJ Module

|Input File|Description|
|---|---|
|BED.SDF|SEDZLJ control ﬁle with active and deposited erosion parameters|
|ERATE.SDF<br><br>|SEDFlume core properties for existing sediment bed|
|CORE_FIELD.SDF<br><br>|Sptially varying assignment of core ID’s from ERATE.SDF|
|SEDW.INP<br><br>|Water column initial conditions for cohesive sediments|
|SDSER.INP|Time series ﬁle for cohesive boundary conditions|
|SNSER.INP<br><br>|Time series ﬁle for non-cohesive boundary conditions|
|SNDW.INP<br><br>|Water column initial conditions for non-cohesive sediments|
|SEDB.INP<br><br>|Sediment bed initial conditions for cohesive sediments NSEDFLUME = 2 (10.0)|
|SNDB.INP|Sediment bed initial conditions for non-cohesive sediments NSEDFLUME = 2 (10.0)|
|BEDBDN.INP<br><br>|Sediment bed initial conditions for bulk density NSEDFLUME = 2 (10.0)|
|BEDDDN.INP|Sediment bed initial conditions for dry density, porosity or void ratio NSEDFLUME = 2 (10.0)|
|BEDLAY.INP|Sediment bed initial conditions for layer thickness NSEDFLUME = 2 (10.0)|
|SEDBLBC.INP<br><br>|Non-cohesive bedload outﬂow or recirculation boundary conditions|
|SEDBED_HOT.SDF|Restart/hot start ﬁle of SEDZLJ sediment conditions|


#### 1.3.5 Wave Parameter Files

|Input File|Description|
|---|---|
|WAVE.INP<br><br>|External wave model linkage ﬁle|
|WAVETIME.INP<br><br>|List of times in days that correspond to the wave conditions in external wave linkage ﬁles|
|WAVECELLS.INP<br><br>|List of cells to compute wave action if IUSEWVCELLS > 0 and ISWAVE > 2|
|WAVEBL.INP<br><br>|External wave model linkage ﬁle for boundary layer only (deprecated)|
|SWAN_GRP.INP<br><br>|SWAN wave model linkage control ﬁle|
|SWAN_LOC.INP<br><br>|X and Y locations of the SWAN models cell centriods|
|SWAN_TBL.INP<br><br>|SWAN model results for linking to EFDC+|


#### 1.3.6 Eutrophication Module

|Input File|Description|
|---|---|
|WQ3DWC.INP<br><br>|Eutrophication module control ﬁle for the water column processes|
|KINETICS.INP<br><br>|Dissolved oxygen kinetics by zone deﬁnitions|
|WQALGG.INP|Water column algae kinetic zone deﬁnitions|
|MACALGMP.INP|Macroalgae/Periphyton kinetic zone deﬁnitions|
|WQSETL.INP|Algal and particulate ettling rate zone deﬁnitions|
|WQWCMAP.INP<br><br>|Spatially varying kinetic zones|
|WQICI.INP|Eutrophication constituent|
|CWQSRxx.INP|Eutrophication constituent [xx] concentration time series (IWQPSL = 2)|
|WQPSL.INP<br><br>|Eutrophication constituents mass loading time series|
|SUNDAY.INP<br><br>|Time series of daily average solar radiation and fraction of day|
|WQWCRST.INP|Eutrophication restart ﬁle for the water column|


##### 1.3. Input Files 71



<<<PAGE 74>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



Diagensis Sub-Module

|Input File<br><br>|Description|
|---|---|
|WQ3DSD.INP|Sediment diagenesis control ﬁle|
|WQSDICI.INP|Sediment diagenesis initial conditions ﬁle|
|WQSDMAP.INP|Sediment diagenesis cell zone map|
|WQBENMAP.INP|Spatially varying mud & sand fractions if IWQBEN = 2|
|WQSDRST.INP|Sediment diagenesis restart ﬁle ASCII format|
|WQSDRST.BIN<br><br>|Sediment diagenesis restart ﬁle binary format|


RPEM Sub-Module

|Input File|Description|
|---|---|
|WQRPEM.INP<br><br>|Rooted Plant and Epiphyte (RPEM) control ﬁle|
|WQRPEMSIC.INP|Spatially varying carbon initial conditions for roots and shoots|
|WQRPEMRST.INP<br><br>|RPEM restart ﬁle|


Mechanical Hydrokinetic Device Files

|Input File<br><br>|Description|
|---|---|
|MHK.INP|Mechanical Hydrokinetic device control ﬁle|


#### 1.3.7 Toxics Module

|Input File<br><br>|Description|
|---|---|
|TOXW.INP<br><br>|Water column initial conditions for toxics|
|TOXB.INP|Sediment bed initial conditions for toxics|
|TXSER.INP<br><br>|Time series ﬁle for toxics|
|PARTMIX.INP|Particle mixing properties in the sediment bed|
|PMXMAP.INP|Spatially varying sediment bed particle mixing zones|
|DOCW.INP<br><br>|Spatial varying, time constant dissolved organic carbon in water column|
|DOCB.INP<br><br>|Spatial varying, time constant dissolved organic carbon in sediment bed|
|FOCB.INP<br><br>|Particulate organic carbon in bed and pseudo-poc in bed|
|FPOCB.INP<br><br>|Spatialy varying, time constant particulate organic carbon fraction for each sediment class in bed|
|FPOCW.INP|Spatial varying, time constant particulate organic carbon fraction for each sediment class in water column|
|POCB.INP<br><br>|Spatialy varying, time constant particulate organic carbon in bed|
|POCW.INP<br><br>|Spatial varying, time constant particulate organic carbon in water column|
|FOODCHAIN.INP<br><br>|Spatial averaging map for food chain model output|
|PSEUDO_FOCB.INP<br><br>|Spatialy varying, time constant psueo-POC fraction for each sediment class in bed for food chain|


##### 1.3. Input Files 72



<<<PAGE 75>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



#### 1.3.8 Temperature Module

|Input File|Description|
|---|---|
|TEMP.INP|Water column initial conditions for temperature|
|TSER.INP<br><br>|Time series ﬁle for temperature boundary conditions|
|ASER.INP<br><br>|Time series ﬁle for atmospheric parameters|
|ATMMAP.INP|Cell weightings ﬁle for ASER series when NASER > 1|
|PSHADE.INP<br><br>|Spatially varying solar radiation shading|
|SVHTFACT.INP<br><br>|Spatially varying surface heat exchange parameters for DSI full heat balance if ISVHEAT > 0|
|TEMB.INP<br><br>|Spatially varying initial bed temperature and bed thermal thickness|


Ice Sub-Module

|Input File|Description|
|---|---|
|ISER.INP<br><br>|Time series of user speciﬁed ice cover for ISICE = 1|
|ICEMAP.INP|Cell weightings ﬁle for ISER series when NISER > 1 for ISICE = 1|
|ISTAT.INP<br><br>|Time series of user speciﬁed ice for whole domain when ISICE = 2|
|ICE.INP<br><br>|Initial conditions for ice cover when using heat coupled ice (ISICE > 2)|


### 1.4 Output Files

This section describes the binary output ﬁles produced by EFDC+ during a calculation.

#### 1.4.1 Output Files

These output ﬁles are written out by EFDC+ in a binary format. The easiest way to view the results is using EE Modeling System (EEMS). A demo of EEMS is available and can be accessed by going to the EEMS website. Alternatively, a rudimentary postprocessing tool is available, referred to as GetEFDC. GetEFDC is a Fortran 90 program that can read the binary formats and can be modiﬁed to output into another format like a text ﬁle. A detailed description of GetEFDC is found on the next page.

In the table below each of the binary output ﬁles is listed and described.

|Output ﬁle name|Description|
|---|---|
|EE_WS.OUT<br><br>|Water depth|
|EE_WC.OUT|Water column and top layer of sediments|
|EE_BC.OUT|Computed boundary ﬂows|
|EE_BED.OUT<br><br>|Sediment bed layer information|
|EE_WQ.OUT|Water quality information for the water column|
|EE_SD.OUT<br><br>|Sediment diagensis information|
|EE_RPEM.OUT<br><br>|Rooted plant and epiphyte model|
|EE_SEDZLJ.OUT|Sediment bed data for sedzlj sub-model|
|EE_HYD.OUT|Water depth and velocity|


Some of these outputs are optional based on the options set in the efdc.inp ﬁle.

##### 1.4. Output Files 73



<<<PAGE 76>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



#### 1.4.2 GetEFDC

GetEFDC is a Fortran utility to read the binary output ﬁles produced by EFDC+. GetEFDC is a a starting point for the user to create their own analysis of EFDC+ output. It is expected that a user utilizing this tool has knowledge of Fortran and can modify GetEFDC to meet their speciﬁc needs.

##### Source Code

The source code for GetEFDC is listed below. It written all in Fortran and is straightforward to compile with a modern compiler (e.g. gfortran or Intel).

Main program:

• getefdc.f90 and 8 Modules:

- • infomod.f90
- • efdcpromod.f90
- • tecmod.f90
- • geteeoutmod.f90
- • xyijconv.f90
- • gethfreqout.f90
- • globalvars.f90


If IGRIDV > 0 then the output is based on the vertical layer deﬁned in sgzlayer.inp.

##### Build GetEFDC

A makefile is located under the /GetEFDC/src directory. This can be used to compile on a Linux machine. Alternatively, this program can be compiled on Windows using Visual Studio.

Running GetEFDC The syntax for running the utility is as follows:

|GetEFDC.exe getefdc.inp|
|---|


##### Input File

getefdc.inp is the master ﬁle that stores all the information about the parameters of interest which the user is trying to extract. This ﬁle must be edited for every change to input parameters. A sample of the master ﬁle is included in the GetEFDC folder. The input parameters in this ﬁle are as follows:

- • The full path of the folder containing efdc.inp ﬁle
- • LAYK The number of layer in the vertical to get data for 2DH display (>0)


- – = 0 Extract the depth-averaged data
- – >0 Extract the data at layer of k
- – =-1 Extract High Frequency output


##### 1.4. Output Files 74



<<<PAGE 77>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



- – =-2 Extract data for time series (TS) at a height above bed (m)
- – =-3 Read TMP.DAT ﬁle and write an array data ﬁle for TECPLOT


- • ZOPT This parameter is used in case of LAYK=-2

- – =1 Extract TS data at the depth under water surface
- – =2 Extract TS data at the height above bottom


- • JULTIME Julian time point for a selected layer, if > MAXTIME then JULTIME=MAXTIME JULTIME = 0 Extract data for all snapshots
- • NLOC Number of locations (cells) to extract data. The location can be given as Index (I,J) or UTM coordinates (X,Y) via the parameter INDEX.
- • ROTA The option for rotation of velocity components (U,V)

- – = 0 Extract (U,V) without rotation
- – = 1 (U,V) components are rotated to the true east and true north directions


- • INDEX

- – = 0 UTM (X,Y) of cells are used
- – = 1 Indices (I,J) of cells are used


- • VPROF The option to extract data for vertical proﬁle, 0 (No)/ 1(Yes)
- • TECPLOT The option to extract data for 2DH Tecplot, 0 (No)/ 1(Yes)
- • NDRIFTER: A successive set of number of particles to extract data for (X,Y,Z)
- • I/X I Indices or X abscissa of cells to extract data
- • J/Y J Indices or Y coordinates of cells to extract data
- • ZINT Height under water surface or above bed to extract data in case LAYK=-2


Please note that the lines which start with ** in the getefdc.inp ﬁle are comments and will be ignored.

##### Sample GetEFDC Input File

|** COMMENT LINES START WITH "*"<br><br>** GETEFDC VER. 161128 IS USED TO:<br><br>** EXTRACT EFDC BINARY FILES *.OUT (EFDC 6.0 OR LATER) TO NETCDF AND ASCII FILES FOR:<br><br>** 1.TIME SERIES AT SOME LOCATIONS DETERMINED BY (I,J) OR (X,Y)<br>** 2.TECPLOT OF ONE LAYER (K>=0) AT OME SPECIFIC SNAPSHOT<br>** 3.ARRAYS OF DATA<br><br><br>**<br><br>** OBLIGATORY INPUT FILES:<br><br>** 0.GETEFDC.INP: THIS FILE<br>** 1.EFDC.INP<br>** 2.LXLY.INP<br>** 3.DXDY.INP<br>** 4.CELL.INP<br>** 5.CORNERS.INP<br>** 6.MAPPGNS.INP<br>** 7.MAPPGEW.INP<br><br><br>**<br><br>** THE FOLLOWING BINARY FILES WILL BE READ ACCORDING TO SELECTED ITEMS<br><br>** 1.EE_WS.OUT|
|---|


(continues on next page)

##### 1.4. Output Files 75



<<<PAGE 78>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|** 2.EE_VEL.OUT<br>** 3.EE_WC.OUT<br>** 4.EE_WQ.OUT<br>** 5.EE_DRIFTER.OUT<br>** 6.EE_BC.OUT<br>** 7.EE_BED.OUT<br>** 8.EE_TUR.OUT<br><br><br>**<br><br>** OUPUT OF GETEFDC IS STORED IN RESULT FOLDER<br><br>**<br><br>*****************************************************************************<br><br>** THE FULL PATH OF INP FILES is determined by the file efdc.inp:<br><br>** E:\Projects\EFDC_Testing\restart\caloo-autorun_1\efdc.inp<br><br>**<br><br>*****************************************************************************<br><br>** OPTIONS FOR OUTPUT:<br><br>** LAYK = K>0: DATA AT LAYER NUMBER K TO BE EXPORTED AT TIME=JULTIME<br><br>** 0: DEPTH-AVERAGED DATA IS EXPORTED<br><br>** -1: Get High Frequency output FOR CELLS<br>** -2: Extract data for Time series at a height above bed (m)<br>** -3: LOAD TMP.DAT AND EXPORT TECPLOT<br><br><br>**<br><br>** ZOPT = 1: FOR THE DEPTH UNDER WATER SURFACE IF LAYK=-2<br><br>** 2: FOR THE HEIGHT ABOVE BOTTOM IF LAYK=-2<br><br>** NDRIFTER : N1:N2 A SET OF DRIFTER TO GET (X,Y,Z)<br><br>** ** ** JULTIME : JULIAN TIME FOR SELECTED LAYER<br><br>** > MAXTIME THEN JULTIME=MAXTIME<br><br>** 0 DATA FOR ALL SNAPSHOT<br><br>** NLOC : NUMBER OF CELLS TO EXTRACT TIMESERIES<br><br>** ROTA = 1: (U,V) AT CELL CENTER ROTATED TO TRUE EAST AND TRUE NORTH<br><br>** 0: (U,V) AT CELL FACES WITHOUT ROTATION<br><br>** INDEX = 1: (I,J) OF CELLS ARE GIVEN ** 0: (X,Y) OF CELLS ARE GIVEN ** VPROF = 1: EXPORT VERTICAL PROFILE<br><br>** = 0: NO EXPORTATION FOR VERTICAL PROFILE<br><br>**<br><br>** TECPLOT = 1: EXPORT DATA FOR TECPLOT<br><br>** = 0: NO TECPLOT EXPORTATION<br><br>**<br><br>*****************************************************************************<br><br>** LAYK JULTIME NLOC ROTA INDEX VPROF TECPLOT ZOPT NDRIFTER 4 0 2 1 1 1 1 1 1:5<br><br>*****************************************************************************<br><br>** I/X : I Index or X of cell<br><br>**<br><br>** J/Y : J Index or Y of cell<br><br><br>**<br><br>** ZINT : THE DEPTH UNDER WS OR HEIGHT ABOVE BED (m)<br><br>** FOR TIME SERIES EXTRACTION IF LAYK=-2<br><br>**<br><br>*****************************************************************************<br><br>** I/X J/Y ZINT(m)<br><br>** 314782.0 3941547.0 0.5 3 44 0.5|
|---|


(continues on next page)

##### 1.4. Output Files 76



<<<PAGE 79>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0

(continued from previous page)



|3 45 0.7|
|---|


##### Output Files

After running GetEFDC a sub-folder RESULT is generated in the folder #output of the working model. The extracted ﬁles are ASCII with the following conventions for the ﬁle names:

- • First characters group shows the constituent, such as SAL for salinity
- • Second character group is TSK_ which is the time series of the layer K, such as TSK_4 is time series for the layer K=4
- • The last character group is _DOM for the domain or CEL for the selected cells
- • The vertical proﬁles for the constituents at the selected cells use the group _PROF in the ﬁle names, such as SAL_PROF.DAT


### 1.5 Sample Models

Several completed model input ﬁles are provided under SampleModels. All of these models can be run with EFDC+ version 8.5 and the grid can be visualized with the GridGenerator utility.

Next, Each of these models is decribed in greater detail.

#### 1.5.1 Lake 2D Test Case

A complete sample model of a lake is provided to highlight the ability of EFDC+ to simulate the hydrodynamics, temperature, and water quality. The model can be found in SampleModels\Lake_T_HYD_WQ. In the model there are 355 horizontal grid cells 1 vertical layer.

##### 1.5. Sample Models 77



<<<PAGE 80>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



#### 1.5.2 Ohio River Test Case

A complete model is given which simulates the hydrodynamics in the Ohio River. This model can be found in SampleModels\Ohio_River_4. In addition to hydrodynamics, the dye module is used to simulate pulses into the Ohio River from Mill Creek in Cincinnati.

In the model there are 510 horizontal grid cells and 1 and 4 vertical layers. An overview of the grid is provided in the ﬁgure below.

##### 1.5. Sample Models 78



<<<PAGE 81>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



#### 1.5.3 Lake Washington Test Case

A completed sample model of Lake Washington is provided SampleModels/Lake_Washington. This model can be run with EFDC+ version 8.5 and the grid can be visualized with the GridGenerator.

This model simulates hydrodynamics in Lake Washington. The model uses temperature modules with the Sigma-Zed vertical layering option to simulate thermal stratiﬁcation in Lake Washington, Seattle, USA. The Sigma Zed model is unique to EFDC+ and is designed to reduce pressure gradient errors with an approach that is computationally efﬁcient.

The model has 1,183 horizontal grid cells and 55 vertical layers. The model domain is shown in the ﬁgure below.

##### 1.5. Sample Models 79



<<<PAGE 82>>>

##### EFDC+ Computer Implementation Guide, Release 8.5.0



### 1.6 License

Copyright 2019 DSI, LLC Licensed under the Apache License, Version 2.0 (the “License”); you may not use this ﬁle except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the speciﬁc language governing permissions and limitations under the License.

##### 1.6. License 80

