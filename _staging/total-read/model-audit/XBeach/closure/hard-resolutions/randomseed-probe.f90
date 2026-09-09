program randomseed_probe
 use wave_boundary_datastore
 implicit none
         if(allocated(waveBoundaryParameters%randomseed)) deallocate(waveBoundaryParameters%randomseed)
end program
