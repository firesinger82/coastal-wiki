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
module getter_probe
  use probe_types
  use iso_c_binding
  type(spacepars) :: s
  type(parameters) :: par
  type(timepars) :: tpar
contains
  subroutine compute_dt(s,par,tpar,it,ilim,jlim,dtref)
    type(spacepars) :: s
    type(parameters) :: par
    type(timepars) :: tpar
    integer :: it,ilim,jlim
    real(8) :: dtref
    dtref=dtref+1d0
    par%dt=dtref
  end subroutine
   subroutine get_time_step(timestep) bind(C, name="get_time_step")
      !DEC$ ATTRIBUTES DLLEXPORT :: get_time_step

      real(c_double) :: timestep
      integer :: ilim = 0
      integer :: jlim = 0
      integer :: it = 0
      real*8 :: dtref = 0.d0

      call compute_dt(s,par, tpar, it, ilim, jlim, dtref)
      timestep = par%dt
   end subroutine get_time_step
end module
program saved_getter_probe
  use getter_probe
  real(8) :: a,b
  call get_time_step(a)
  call get_time_step(b)
  if (a/=1d0.or.b/=2d0) error stop 'getter local state did not persist'
  print '(a,f3.0,a,f3.0)', 'stub dtref first=',a,' second=',b
end program
