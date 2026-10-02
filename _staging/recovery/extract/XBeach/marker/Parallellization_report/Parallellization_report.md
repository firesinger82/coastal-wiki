

{0}------------------------------------------------

# of the program XBea h

## Willem Vermin (SARA)<sup>∗</sup> Dano Roelvink (UNESCO)†

### 2008-08-19

### Abstra t

Here we des
ribe the parallelization of the omputer program XBea
h. XBea
h is a two-dimensional model for wave propagation, long waves and mean ow, sediment transport and morphologi
al hanges of the nearshore area, bea
hes, dunes and ba
k-barrier during storms. It is a publi
 domain model that has been developed with funding and support by the US Army Corps of Engineers, by a onsortium of UNESCO-IHE, Delft Hydrauli
s, Delft University of Te
hnology and the University of Miami. The typi
al run times of the program range from hours to days, so it was de
ided to parallelize the program. The parallelization was done by Willem Vermin at SARA and funded by NCF grant NRG-2007.06

| 1 | Des ription of the program XBea h |                                                           |   |
|---|-----------------------------------|-----------------------------------------------------------|---|
| 2 |                                   | Des ription of the parallelization pro ess                | 2 |
|   | 2.1                               | Choi e of parallelization paradigm<br>                    | 2 |
|   | 2.2                               | Reorganizing the program                                  | 3 |
|   | 2.3                               | Distribution of data<br>                                  | 3 |
|   |                                   | 2.3.1<br>Some more details about the distribution of data | 3 |
|   | 2.4                               | Parallelization method used<br>                           | 4 |
|   |                                   | 2.4.1<br>Input and output                                 | 4 |
|   |                                   | 2.4.2<br>Dening the distribution parameters               | 5 |
|   |                                   | 2.4.3<br>Communi ation subroutines                        | 5 |
|   |                                   | 2.4.4<br>Communi ation of data<br>                        | 5 |
| 3 |                                   | S alability results                                       | 5 |
| 4 |                                   | Con lusion                                                | 7 |

<sup>∗</sup>

<sup>†</sup>d.roelvinkunes
o-ihe.org

{1}------------------------------------------------

| 5 | $\operatorname{Tec}$ | hnical details                        | 7 |
|---|----------------------|---------------------------------------|---|
|   | 5.1                  | General conventions                   | 7 |
|   | 5.2                  | Parallelization by code spotting      | 8 |
|   | 5.3                  | Some MPI related subroutines          | 9 |
|   | 5.4                  | Code generation: program makeincludes | 0 |
|   | 5.5                  | Some notes about Fortran90 and MPI    | 2 |
|   | 5.6                  | Compilation and running               | 3 |
|   |                      | 5.6.1 Compilation                     | 3 |
|   |                      | 5.6.2 Running the program             | 4 |

## 1 Description of the program XBeach

The program is written in Fortran 90 and counts circa 12000 non-comment lines, divided over 30 files. The program is reasonably well structured. The relevant data is defined in about 100 arrays (1 to 4 dimensional). A number of subroutines, each with a special function, acts at each time step upon the data. The main subroutines are:

- timestep: determines an appropriate value for the next time step
- wave bc: wave boundary conditions update
- flow bc: flow boundary conditions update
- wave stationary or wave timestep: to carry out wave time step
- $\bullet$  flow\_timestep: to carry out flow time step
- $\bullet$  transus: to carry out suspended transport time step
- bed\_update: to carry out bed level update
- varoutput: to output the desired results

These subroutines are repeatedly called after one another, to modify the arrays describing the state of the system.

# 2 Description of the parallelization process

### 2.1 Choice of parallelization paradigm

The program acts on a number of arrays, each describing different aspects of the same rectangular area. In general, to compute a new value of an array element A(i,j), the values of A(i,j), A(i-1,j), A(1,j+1) and so on are needed, along with the corresponding values of other arrays. Therefore a parallelization scheme, involving the distribution of the data among the available processors seems feasible Each processor would compute 'its' piece and communicate the borders with the neighbor processors.

{2}------------------------------------------------

## Reorganizing the program

The program is written in fortran90, but not all features of fortran90 were used. It was still possible to all a subroutine with wrong parameters (type or number), without getting an error message from the ompiler. Therefore, all les were modied to generate a module, ontaining the relevant data and the subroutines. This already un
overed some in
onsisten
ies in the program.

The large number of variables made it di
ult to keep the program in an orderly state. The program ontains several housekeeping routines su
h as: the output routine, the allo
ation and initialization of the distributed data and the reation of debug ode. In these parts long lists des
ribing a
tions on the variables were oded. Therefore it was de
ided to make this housekeeping more simple and less error prone by reating a ode generating program: makein-

This method enables the possibility to refer to a variable by the ASCII representation of its name, and to perform a
tions on all dened variables, without having to know whi
h variables there are. This simplied the ode for the output routine onsiderably, along with the ode for the distribution and olle
tion of the data. It makes it also possible to reate a routine that he
ks the onsisten
y of the data for all variables, very useful during debugging.

It was de
ided that the data should be distributed among the pro
esses in two dimensions, as presented below:

| 0 | 3 | 6 | 9  |
|---|---|---|----|
| 1 | 4 | 7 | 10 |
| 2 | 5 | 8 | 11 |

This is a 3x4 distribution, using 12 pro
esses. The numbers in the drawing represent the enumeration of the pro
esses, starting with zero (MPI onvention). During the omputations, pro
ess 4 ex
hanges data with pro
esses 1,3,7 and 5, while pro
ess 9 only ex
hanges data with pro
esses 6 and 10.

Call the global matrix A, dimensioned as A(M,N). Call the sub matri
es a0, a1 et
., ea
h dimensioned as a0(m,n), a1(m,n) et
, where m and n an be dierent 

{3}------------------------------------------------

for ea
h matrix a. In the same olumn the values of n are equal, in the same row the values of m are equal. The matri
es overlap, take as example a4:

- the rst row ontains the same information as the one before the last row
- the last row (a4(m,:)) ontains the same information as the se
  ond row of a4(m,:) == a5(2,:)
- the rst olumn ontains the same information as the se
  ond last olumn a4(:,1) == a1(:,n-1)
- the last olumn ontains the same information as the one before the last olumn of the matrix right a4(:,n) == a7(:,2)

The matri
es on the edges (a0,a1,a3, et
.) do not share their edge(s) whi
h are part of the edges of matrix A with another matrix. The omputing domain of a matrix in the middle (a4 for example), shares the elements a4(2:m-1,2:n-1) with A. For matri
es on the edges for example the shared elements are a1(2:m-1,1:n-1). On ea
h time step, the elements that are shared with A are omputed, with the neighbors. For example the row a3(m-1,:) would be sent to the row a4(1,:). In the program about 100 of these matri
es are used, some of them with one or two extra dimensions. However, only a relatively small number of these arrays have to be ommuni
ated between pro
esses.

Parallelization method used

### Input and output

2.4

a4(1,:) == a3(m-1,:)

The input and output of data is performed by one pro
ess: the master pro
ess with MPI rank zero. Depending on the properties of the data the following

- Broad
  ast: the data is opied as is to all pro
  esses (global variables, parameters of the system, et
  .)
- Divide and distribute (all matri
  es that des
  ribe the state of the system in a grid. The appropriate parts of matrix A (see above) are sent to the pro
  esses)

Before the master pro
ess an output the data, it is olle
ted from all pro
esses. Using one pro
ess for input and output has the advantage that the program will also run on systems where only the master pro
ess has the apability to read and write to a le system.

{4}------------------------------------------------

### Dening the distribution parameters

At the start of the program, a suitable distribution s
heme is determined. Given the number of pro
esses available (P) and the number of gridpoints in x and y dire
tion, the pro
essorgrid is determined su
h that the total length of the ommuni
ation edges is minimized. The pro
essorgrid is dened by two integers: MP and NP. In the example above: P=12, MP=3, NP=4. Subsequently, the dimensions of the lo
al matri
es (a0, a1, a2 et
.) are determined, su
h that all these matri
es are as equal as possible in size.

A number of interfa
e subroutines has been written, tailored to the problem at hand, so that the a
tual MPI alls are not visible in the program. For example, in stead of oding something like:

```
all M P I _ S e n d r e 
 v( a (: ,2) , m , M P I _ D O U B L E _ P R EC IS IO N , &
                          n e i g h b o u r_lef t , tag , &
                          a (: , n ) , m , M P I _ D O U B L E _ P R EC IS IO N , &
                          n e i g h b o u r_ righ t , tag , &
                          M P I _ C O M M _WORL D , M P I _ S T A T U S _ IGN ORE ,&
                          ierror )
```

```
all x m p i _ s h i f t (a , ': n ')
```

meaning: get the last olumn of a lled in. This statement su
es to get the last olumn of all matri
es a updated.

The original program was he
ked for the pla
es where ommuni
ation is ne
 essary to maintain onsisten
y. For example, if a matrix is updated, but the border rows and olumns are untou
hed, these rows and olumns need to be updated (i.e. re
eived from the neighbors) to maintain onsisten
y. Later in this arti
le we will dive somewhat more in the te
hni
al aspe
ts.

## S alability results

The program was exe
uted, using a standard test ase: 'humptest.zip'. In this example the size of the global matri
es is 101x501. The Lisa system of SARA was used to run the s
aling tests. The Lisa system is equipped with an in niband network between the nodes. The MPI library is OpenMPI-1.2.6 <sup>2</sup> Fortran90 ompiler is gfortran3 . Computing time of the serial program is about 5 minutes. The number of timesteps is lowered to speed up the s
aling measurements and development of the program. In pra
ti
e, the program would run for

https://subtra
.sara.nl/userdo
/wiki/lisa/des
ription

http://www.open-mpi.org/

http://g

.gnu.org/fortran/

{5}------------------------------------------------

Results using one pro
essor per node. Ea
h node has two oneore pro
essors. The program s
ales up to 40 pro
esses: he performan
e using 40 pro
esses is a. 20 times the performan
e of the serial version.

Results using 2 oneore pro
essors per node. The speedupurve is some-

{6}------------------------------------------------

what irregular (probably due to the load variations in the rest of the system: Lisa is very heavily used), but the speedup is about the same as in the above ase, using only half the number of nodes.

Results for running the program on nodes equipped with 2 quadore nodes, making 8 ores per node. Also here we observe a good s
aling up to 40 pro
esses (using 5 nodes).

This parallelization was su

essful: usable s
alability is 40 pro
esses and probably more. The speedup is about 20 for a quite modest model. Larger models will result in better s
alability.

Here is a detailed des
ription about the parallelization method and the subroutines that were reated during the pro je
t.

• Code that is only to be exe
uted in the parallel version has to be surrounded as following:

```
all x m p i _ s h i f t( s % uu , ':1 ')

all x m p i _ s h i f t( s % uu , ' m : ')
```

{7}------------------------------------------------

• Don't use 'stop' but all halt\_program:

```
use x m p i _ m o d u l e
if ( error = 1) then
    stop ! wrong

all h a l t _ p r o g r a m ! good
```

• The following variables are available using xmpi\_module

| name         | meaning                            | value in serial |
|--------------|------------------------------------|-----------------|
| xmpi_rank    | MPI rank of this pro ess           | 0               |
| xmpi_size    | number of pro esses                | 1               |
| xmaster      | is this the master pro ess?        | .true.          |
| xmpi_isleft  | is a(:,1) part of a global border? | .true.          |
| xmpi_isright | is a(:,n) part of a global border? | .true.          |
| xmpi_istop   | is a(1,:) part of a global border? | .true.          |
| xmpi_isbot   | is a(m,:) part of a global border? | .true.          |
| xmpi_p ol    | my  olumn number in pro essor grid | 1               |
| xmpi_prow    | my row number in pro essor grid    | 1               |

• Take are that every input/output statement is done on master only, maybe followed by a broad
ast.

```
use x m p i _ m o d u l e
    if ( x m a s t e r) then
           write (* ,*) ' R e a d i n g x'
           read * , x

all x m p i _ b 
 a s t( x )
```

• Fun
tions readkey\_int and readkey\_dbl are MPI-aware, but not readkey:

```
use r e a d k e y _ m o d u l e
t i m i n g s = r e a d k e y _ i n t ( ' params . txt ' , ' timings ' ,1 ,0 ,1)
if ( x m a s t e r) then ! for readkey , test is needed

all r e a d k e y( ' params . txt ' , ' tsglobal ' , fname )
  open (10 , file = fname )
  read (10 ,*) x

all x m p i _ b 
 a s t( x )
```

### Parallelization by ode spotting

In the program, all relevant matri
es are de
lared as a(1:nx+1,1:ny+1) and have a pla
e in a 'spa
epars' derived type. In the serial version there is one 

{8}------------------------------------------------

su
h derived type, in the parallel version there are two: one alled 'sglobal' (often abbreviated as 'sg'), the other 'slo
al' ('sl'). sglobal is lled in on the master pro
ess and has spa
e for all data; slo
al ontains only the distributed data. sglobal%nx and sglobal%ny are the dimensions of the global grid, whereas slo
al%nx and slo
al%ny are the dimensions of the lo
al distributed matri
es. Using this method there is no need to hange anything at the ode itself, one only has to take are that data is ommuni
ated when appropriate. Below is a table with examples of ode patterns and the orresponding a
tions needed. (1:nx+1,1:ny+1).

| pattern                                       | a tion                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| a<br>=<br><br>b<br>                           | No<br>a tion<br>needed                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                               | all<br>x m p i _ s h i f t(a , ':1 ')                                                                                                                                                                                                                                                                                                                                                                                               |
| a (: ,2: ny )=<br>                            | all<br>x m p i _ s h i f t (1 , ':n ')                                                                                                                                                                                                                                                                                                                                                                                              |
| a (: ,1)<br>=<br>                             | all<br>x m p i _ s h i f t(a , ':1 ')                                                                                                                                                                                                                                                                                                                                                                                               |
| a ( nx +1 ,:)<br>=<br>                        | all<br>x m p i _ s h i f t(a , 'm : ')                                                                                                                                                                                                                                                                                                                                                                                              |
| a (2 ,:)<br>=<br><br>a (3: nx +1 ,:)<br>=<br> | This<br>one<br>needs<br>some<br>s p e   i a l<br>a t t e n t i o n.<br>In<br>the<br>p a r a l l e l<br>ase ,<br>the<br>first<br>line<br>has<br>only<br>m e a n i n g<br>in<br>the<br>m a t r i   e s a t<br>the<br>top .<br>The<br>se ond<br>line<br>is<br>ok<br>for<br>the<br>top<br>matri es ,<br>but<br>for<br>the<br>other<br>ones ,<br>a (2 ,:)<br>must<br>be<br>o m p u t e d<br>in<br>t h e s a m e<br>way<br>as<br>a (3 ,:) |

In general, some a
tions are ne
essary when:

- a border olumn or row gets a spe
  ial treatment, or is not assigned at all: this is treated with a all to xmpi\_shift
- another row or olumn gets a spe
  ial treatment. In that ase one has to take a good look at the ode to nd the appropriate a
  tion.

are made before they are used. Of ourse, if one or more of the borders are never a
tually used in su
h a way that it inuen
es the output of the program, the orresponding xmpi\_shift is not ne
essary.

The subroutines that interfa
e to MPI are divided in three ategories:

about the ommuni
ation patterns that are needed

- general (general\_mpi.F90): this are subroutines that fun
  tion regardless
- xmpi (xmpi.F90): subroutines that are aware of the parallel environment of the program, they know about the layout of the matri
  es and know
- spa
  e (spa
  eparams.F90): subroutines that know about the data in a spa
  epars derived data type

{9}------------------------------------------------

Some important subroutines and interfaces are listed here. The source code contains instructions how to use them.

file: general mpi.F90, module: general mpi module

| name                 | function                             |
|----------------------|--------------------------------------|
| matrix_distr         | distributes matrix                   |
| vector_distr_send    | distributes vector                   |
| matrix_coll          | collects matrix on master process    |
| decomp               | computes optimal division            |
| $\det\_$ submatrices | determines optimal sizes of matrices |
| shift_borders        | communicates all borders, obsolete   |

file: xmpi.F90, module: xmpi module

| name                          | function                             |
|-------------------------------|--------------------------------------|
| xmpi_initialize               | initializes MPI                      |
| xmpi_finalize                 | finalizes MPI                        |
| halt_program                  | halts program, serial and parallel   |
| xmpi_determine_processor_grid | determines processor grid            |
| ${\rm xmpi\_bcast}$           | broadcast a variable                 |
| xmpi_allreduce                | performs an MPI_Allreduce            |
| xmpi_reduce                   | performs an MPI_Reduce               |
| ${\rm xmpi\_shift}$           | get values for border from neighbour |
| ${\rm xmpi\_getrow}$          | get a row from another matrix        |

file: spaceparams.F90, module: spaceparams

| name                            | function                                 |
|---------------------------------|------------------------------------------|
| space_consistency               | for debugging, checks consistency        |
| space_copy_scalars              | copies scalars from and to spacepars     |
| space_distribute_scalars        | distribute sclaras in spacepars          |
| space_distribute                | distributes matrices                     |
| $space\_shift\_borders$         | communicate all borders, obsolete        |
| $\operatorname{space\_collect}$ | collects spacepar variables on master    |
| printsum                        | debugging: prints sum of matrix elements |

## 5.4 Code generation: program makeincludes

In some parts of the program, some kind of bookkeeping is necessary. This can result in boring long pieces of code, difficult to maintain. For example: when the data is read in by the master process, it needs to be distributed among the processes. Since there are more than 100 variables defined in spacepars, at least 100 lines of code would be necessary, and it is all too easy to forget to distribute a newly introduced variable. Therefore a code generating program is developed - "makeincludes" - that reads a simple formatted file, and produces a number of files to be included in the program. The following is now achieved:

• variables in spacepars are defined in one file: the name, the number of dimensions, the dimensions self, and the desired method of distribution:

{10}------------------------------------------------

see the le spa
eparams.tmpl. This le also ontains a des
ription of the layout desired.

- automati ode generation for the de
  laration of the spa
  epars derived type.
- the possibility to get to the value of a variable by using it's name in ASCII (see the example program demo.F90). This proves to be very useful for the subroutine varoutput (varoutput.F90)
- it is easy to write a ode that visits all the variables in spa
  epars, without having to know whi
  h variables are available. This was very useful during debugging and nding the ause of in
  onsisten
  ies that reped in. (See for example subroutine spa
  e\_
  onsisten
  y in spa
  eparams.F90)

The program makein
ludes generates the following les:

- spa
  ede
  l.gen: ontains the ode needed for the de
  laration of a spa
  epars derived type.
- spa
  e\_allo
  \_s
  alars.gen: allo
  ates the simple variables in spa
  epars. This is ne
  essary, be
  ause now all variables in spa
  epars are de
  lared as point-
- spa
  e\_allo
  \_arrays.gen: ontains the ode to allo
  ate the 1,2,3 and 4 dimensional arrays in spa
  epars.
- mnemoni
  .gen: denes variables with names like mnem\_E: the variable mnem\_E is equal to the string 'E'. Furthermore, an array mnemoni
  s is
- indextos.gen: ontains ode whi
  h, given an index, returns a derived type with a pointer to the variable for whi
  h mnemoni
  s(index) is equal to the
- spa
  e\_ind.gen, spa
  e\_inp.gen: they dene pointers to the variables in the derived type. Primary goal is to make the ode more readable.
- hartoindex.gen: ode to onvert the name of a variable into an index

- hartoindex (mnemoni
  .F90): returns the index number of the name given
- indextos (spa
  eparams.F90): returns a pointer to a variable with a given

Program demo.F90 ontains an example ode to demonstrate how to use this.

{11}------------------------------------------------

Using MPI in Fortran90 needs some pre
autions. This is aused by the way Fortran90 handles arrays when alling a non-Fortran90 subroutine (as is the ase with MPI). In Fortran77, the address of the rst element of an array is passed, in Fortran90, however, in general a pointer to the rst element of a opy of the array is passed. This is ne
essary be
ause in general it is not possible to tell if the array is ontiguous, or a se
tion of another array. For example:

```
s u b r o u t i n e demo ( x )
r e a l , d im e n s i o n ( : , : ) : : x

 a l l MPI_B
ast ( x , s i z e ( x ) ,MPI_REAL, 0 ,MPI_COMM_WORLD)
! 
 a l l MPI_B
ast ( x ( 1 , 1 ) , s i z e ( x ) ,MPI_REAL, 0 ,MPI_COMM_WORLD) ! e r r o r
program t e s t
r e a l , d im e n s i o n ( 1 0 0 , 1 0 0 ) : : y

 a l l demo ( y ( 1 : 1 0 0 : 2 , : ) )
```

In this example, MPI\_B
ast will be alled with a opy of x, whi
h is no problem: Fortran90 takes are that after the MPI\_B
ast the array is opied ba
k. The se
ond MPI\_B
ast line would be in error, be
ause the address of x(1,1) would be passed, and MPI\_B
ast would broad
ast 50x100 elements, ontiguous, starting at x(1,1).

In general, Fortran90 will not make a opy if the array is ontiguous, and

```
 a l l demo ( y )
```

So, in general, do not use an array-element as starting address of a buer (whi
h is ommon pra
ti
e in Fortran77), but use the whole array.

Another problem arises with non-blo
king sends and re
eives:

```
s u b r o u t i n e demo ( x )
r e a l , d im e n s i o n ( : , : ) : : x

 a l l MPI_Isend ( x , s i z e ( x ) ,MPI_REAL, . . . ) ! wrong

 a l l MPI_Wait ( . . . )
program t e s t
r e a l , d im e n s i o n ( 1 0 0 , 1 0 0 ) : : y

 a l l demo ( y ( 1 : 1 0 0 : 2 , : ) )
```

This will in general give unexpe
ted results. MPI\_Isend will get the address of a opy of x, and return while the a
tual send is still pending. However, after return of MPI\_Isend, Fortran90 will free the opy of x, so an invalid buer (the freed opy of x) will be sent. The same reasoning applies for MPI\_Ire
v: MPI\_Ire
v would result in re
eiving data in an invalid buer. The a
tual behaviour of the program is unpredi
table.

The solution is to make sure that MPI\_Isend is working with the array itself, so one has to make a opy:

{12}------------------------------------------------

```
s u b r o u t i n e demo ( x )
r e a l , d im e n s i o n ( : , : ) : : x
r e a l , d im e n s i o n ( s i z e ( x , 1 ) , s i z e ( x , 2 ) ) : : xx

 a l l MPI_Isend ( xx , s i z e ( xx ) ,MPI_REAL, . . . )

 a l l MPI_Wait ( . . . )
```

Another problem an exist using the MPI\_S
atterv and the like subroutines. These subroutines expe
t a des
ription of the layout of the data (the soalled ounts and displa
ements arrays). Also in this ase it is important to make sure that the data is ontiguous, otherwise the displa
ements an be invalid.

### 5.6Compilation and running

The parallel ode is developed on systems running Linux. Here follows a des
ription how to ompile and run the program. On Windows systems, the details

### Compilation

A Makele is provided, in prin
iple ompilation is as easy as:

```
USEMPI = yes make i n s t a l l # p r o d u 
 e a p a r a l l e l v e r s i o n:
                                # xbea
h . mpi
make i n s t a l l # p r o d u 
 e a serial v e r s i o n:
```

to get the parallel and serial versions. They are installed in the dire
tory ../bin . Important ma
ro's are:

| name   | fun tion                                   |
|--------|--------------------------------------------|
| USEMPI | when dened: generate parallel program      |
| USEMPE | when dened: produ e tra e les for jumpshot |
| F90    | the fortran  ompiler to use                |

The Makele is pretty simple, it should not be di
ult to adapt to a lo
al situation. Do not dene USEMPE for a produ
tion version of the program.

When ompiling Fortran90 les, it is important to have orre
t dependen ies, espe
ially when module les are generated (as is the ase here) and when one wants to run make in parallel (make -j) to speed up the ompilation pro
ess. Therefore a simple s
ript has been made, makedepo, whi
h takes are of dependen
ies. It is alled by the Makele when no le named DEPENDENCIES is present. One an for
e a re-generation of this le by

```
make dep
```

Other things one an make:

```
make 
lean # gets rid of . o and . mod files
                   # and test p r o g r a m s
make r e a l 
 l e a n # gets rid of e v e r y t h i n g ex
ept
                   # files needed for 
 o m p i l a t i o n
```

{13}------------------------------------------------

```
make t e s t g e n m o d u l e # make p r o g r a m t e s t g e n m o d u l e
                          # that tests the 
 o m m u n i 
 a t i n g
make demo # make p r o g r a m demo
```

Furthermore, a s
ript 'maketags' is provided, whi
h produ
es a tags <sup>4</sup> le, very useful in ombination with the vim or ema
s program editors.

### Running the program

We give two examples, one for OpenMPI, one for MPICH2, to run the program on 8 pro
esses:

### OpenMPI

```
m p i e x e 
 -n 8 dire
tory - to - bin / xbea
h . mpi
m p d b o o t [ -n number - of - nodes -f file - with - node - names ℄
```

m p i e x e - np 8 dire
tory - to - bin / xbea
h . mpi

tags: http://
tags.sour
eforge.net/