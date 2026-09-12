program grain_assignment_probe
  implicit none
  type parameters
    integer :: ngd
  end type
  type spacepars
    integer :: nx,ny
    real(8), allocatable :: D50top(:,:),D90top(:,:),pbbed(:,:,:,:),D50(:),D90(:)
  end type
  type(parameters) :: par
  type(spacepars) :: s
  integer :: i,j,j1,case_id
  real(8) :: local_expected
  par%ngd=2
  do case_id=1,2
    s%nx=3
    s%ny=2*(case_id-1)
    j1=1
    if(s%ny>0) j1=2
    allocate(s%D50top(4,s%ny+1),s%D90top(4,s%ny+1),s%pbbed(4,s%ny+1,1,2),s%D50(2),s%D90(2))
    s%D50=[0.0002d0,0.001d0]
    s%D90=[0.0003d0,0.0015d0]
    s%pbbed(:,:,:,1)=1d0
    s%pbbed(:,:,:,2)=0d0
    s%pbbed(3,max(s%ny,1),1,:)=[0d0,1d0]
    s%D50top=-1d0
    s%D90top=-1d0
    local_expected=sum(s%pbbed(2,j1,1,:)*s%D50)
! Exact morphevolution.F90 physical LF lines 1171-1178 begin:
         if (par%ngd>1) then
            do j=j1,max(s%ny,1)
               do i=2,s%nx
                  s%D50top =  sum(s%pbbed(i,j,1,:)*s%D50)
                  s%D90top =  sum(s%pbbed(i,j,1,:)*s%D90)
               enddo
            enddo
         endif
! Exact extracted loop ends.
    if (.not.all(abs(s%D50top-0.001d0)<1d-15)) error stop 'expected whole local D50 broadcast'
    if (.not.all(abs(s%D90top-0.0015d0)<1d-15)) error stop 'expected whole local D90 broadcast'
    if (abs(s%D50top(2,j1)-local_expected)<1d-15) error stop 'heterogeneous cell unexpectedly preserved'
    print '(a,i0,a,es12.4,a,es12.4)', 'ny=',s%ny,' cell(2,j1) expected=',local_expected,' stored=',s%D50top(2,j1)
    deallocate(s%D50top,s%D90top,s%pbbed,s%D50,s%D90)
  end do
end program
