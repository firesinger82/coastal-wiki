module probe_types
  implicit none
  type spacepars
    integer :: pad=0
  end type
  type parameters
    real(8) :: dt=0d0
  end type
  type timepars
    integer :: pad=0
  end type
end module
module xmpi_module
  integer :: xmpi_orank=0
contains
   subroutine halt_program(normal)
      logical,intent(in),optional :: normal
      logical                     :: lnormal
      integer                     :: ierr

      if(present(normal)) then
         lnormal = normal
      else
         lnormal = .true.
      endif

      write(0,*) 'halt_program called by process', xmpi_orank
      if (lnormal) then
         call backtrace
      endif

#ifdef USEMPI
      if (lnormal) then
         call xmpi_abort
      else
         call MPI_Abort(xmpi_ocomm,1,ierr)
      endif
#else
      stop 1
#endif
   end subroutine halt_program
end module
module logging_module
contains
  subroutine writelog(a,b,c)
    character(*) :: a,b,c
    print '(a)', c
  end subroutine
end module
module output_module
  use probe_types
  use xmpi_module
contains
  subroutine output(sglobal,s,par,tpar,update)
    type(spacepars) :: sglobal,s
    type(parameters) :: par
    type(timepars) :: tpar
    logical,optional :: update
    print '(a)', 'stub output reached'
  end subroutine
   subroutine output_error(s, sglobal, par, tpar)

      use logging_module

      implicit none

      type(spacepars)                     :: s,sglobal
      type(parameters)                    :: par
      type(timepars)                      :: tpar

      !call output(s, sglobal, par, tpar, update=.false.)
      call writelog('lse','','An extra output timestep is created to inquire the last timestep')
      call writelog('lse','','    before an error occured')
      call halt_program

   end subroutine output_error
end module
module core_probe
  use iso_c_binding, only: c_int
  use probe_types
  type(spacepars) :: s,sglobal
  type(parameters) :: par
  type(timepars) :: tpar
  integer :: error=0
contains
   integer(c_int) function outputext()
      use output_module,        only: output, output_error
      ! store first timestep
      call output(sglobal,s,par,tpar,.false.)
      if(error==0) then
         outputext = 0
      elseif(error==1) then
         call output_error(s,sglobal,par,tpar)
         outputext = 1
      endif

   end function outputext
end module
program error_path_probe
  use core_probe
  character(8) :: arg
  integer :: rc
  call get_command_argument(1,arg)
  read(arg,*) error
  rc=outputext()
  print '(a,i0)', 'RETURNED=',rc
end program
