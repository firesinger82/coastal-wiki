module instrumented_dispatch
implicit none
type parameters
 integer :: form, bulk
end type
type state
 integer :: unused=0
end type
integer :: called
logical :: continued
   integer, parameter :: FORM_SOULSBY_VANRIJN        =  0
   integer, parameter :: FORM_VANTHIEL_VANRIJN       =  1
   integer, parameter :: FORM_VANRIJN1993            =  2
   integer, parameter :: FORM_NIELSEN2006            =  3
   integer, parameter :: FORM_MCCALL_VANRIJN         =  4
   integer, parameter :: FORM_WILCOCK_CROW           =  5
   integer, parameter :: FORM_ENGELUND_FREDSOE       =  6
   integer, parameter :: FORM_MPM                    =  7
   integer, parameter :: FORM_WONG_PARKER            =  8
   integer, parameter :: FORM_FL_VB                  =  9
   integer, parameter :: FORM_FREDSOE_DEIGAARD       =  10
   integer, parameter :: FORM_INTRASEDTR             =  11 
contains
subroutine dispatch(s,par)
type(state) :: s
type(parameters) :: par
      select case (par%form)
       case (FORM_SOULSBY_VANRIJN,FORM_VANTHIEL_VANRIJN,FORM_VANRIJN1993)
         ! Soulsby van Rijn and Van Thiel de Vries & Reniers 2008 formulations
         call sedtransform(s,par)
       case (FORM_NIELSEN2006)
         call Nielsen2006(s,par)
         if (par%bulk==0) then
            return
         endif
       case (FORM_INTRASEDTR)
         call intra_sedtr(s,par)       

       case (FORM_MCCALL_VANRIJN)
         call mccall_vanrijn(s,par)
         if (par%bulk==0) then
            return
         endif
      end select
continued=.true.
end subroutine
subroutine sedtransform(s,par)
type(state) :: s
type(parameters) :: par
called=1
end subroutine
subroutine Nielsen2006(s,par)
type(state) :: s
type(parameters) :: par
called=2
end subroutine
subroutine mccall_vanrijn(s,par)
type(state) :: s
type(parameters) :: par
called=3
end subroutine
subroutine intra_sedtr(s,par)
type(state) :: s
type(parameters) :: par
called=4
end subroutine
end module
program probe
use instrumented_dispatch
implicit none
type(parameters) :: par
type(state) :: s
integer :: f,b
do f=0,11
 do b=0,1
  par%form=f
  par%bulk=b
  called=0
  continued=.false.
  call dispatch(s,par)
  write(*,'(3(I0,1X),L1)')f,b,called,continued
 enddo
enddo
end program
