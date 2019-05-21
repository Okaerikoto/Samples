# 25/09/18 - Install OpenCV 2 with CUDA 10 and contrib

## Tags :  
OpenCV2 CUDA

## Problème: 
La build d'opencv génère des erreurs suivantes 
 - CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
CUDA_nppi_LIBRARY (ADVANCED)
 - nvcc fatal : Unsupported gpu architecture 'compute_20'
 - fatal error LNK1181: cannot open input file 'opencv_calib3d243d.lib'

## Cause
OpenCV fait pour Cuda 8

## Solution

Modifier les paramètres de recherche de CUDA de cmake dans opencv.

```
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
CUDA_nppi_LIBRARY (ADVANCED)
```

When trying to compile OpenCV 2, for example OpenCV 2.4.13.6, with CUDA 9 there are mainly two issues:
 - The nppi library was splitted up under CUDA 9 into a series of libraries, preventing the shipped `FindCUDA.cmake` script from finding it
 - and the `FindCUDA.cmake` does not handle the latest GPU architectures correctly.
The first problem can be fixed following this StackOverflow question. Specifically, adapting `FindCUDA.cmake` as follows: replace

```1. find_cuda_helper_libs(nppi)```
with
```
1. find_cuda_helper_libs(nppial)
2. find_cuda_helper_libs(nppicc)
3. find_cuda_helper_libs(nppicom)
4. find_cuda_helper_libs(nppidei)
5. find_cuda_helper_libs(nppif)
6. find_cuda_helper_libs(nppig)
7. find_cuda_helper_libs(nppim)
8. find_cuda_helper_libs(nppist)
9. find_cuda_helper_libs(nppisu)
10. find_cuda_helper_libs(nppitc)
```

A few lines below, the set statement for CUDA_npp_LIBRARY needs to reflect these changes:

```1. set(CUDA_npp_LIBRARY "${CUDA_nppc_LIBRARY};${CUDA_nppial_LIBRARY};${CUDA_nppicc_LIBRARY};${CUDA_nppicom_LIBRARY};${CUDA_nppidei_LIBRARY};${CUDA_nppif_LIBRARY};${CUDA_nppig_LIBRARY};${CUDA_nppim_LIBRARY};${CUDA_nppist_LIBRARY};${CUDA_nppisu_LIBRARY};${CUDA_nppitc_LIBRARY};${CUDA_npps_LIBRARY}")```

Similarly, replace

```1. unset(CUDA_nppi_LIBRARY CACHE)```

with

```
1. unset(CUDA_nppial_LIBRARY CACHE)
2. unset(CUDA_nppicc_LIBRARY CACHE)
3. unset(CUDA_nppicom_LIBRARY CACHE)
4. unset(CUDA_nppidei_LIBRARY CACHE)
5. unset(CUDA_nppif_LIBRARY CACHE)
6. unset(CUDA_nppig_LIBRARY CACHE)
7. unset(CUDA_nppim_LIBRARY CACHE)
8. unset(CUDA_nppist_LIBRARY CACHE)
9. unset(CUDA_nppisu_LIBRARY CACHE)
10. unset(CUDA_nppitc_LIBRARY CACHE)
```

In OpenCVDetectCuda.cmake, two more adjustements are necessary to tackle the second problem. In particular, the `_generations` variable needs to reflect the latest GPU generations and needs to correctly map them to the corresponding compute capabilities. To this end, `1. set(_generations "Fermi" "Kepler" "Maxwell" "Pascal" "Volta")` can be used. Then, a few lines below, the case distinction needs to include these generations:

```
1. set(__cuda_arch_ptx "")
2. if(CUDA_GENERATION STREQUAL "Fermi")
3. set(__cuda_arch_bin "2.0")
4. elseif(CUDA_GENERATION STREQUAL "Kepler")
5. set(__cuda_arch_bin "3.0 3.5 3.7")
6. elseif(CUDA_GENERATION STREQUAL "Maxwell")
7. set(__cuda_arch_bin "5.0 5.2")
8. elseif(CUDA_GENERATION STREQUAL "Pascal")
9. set(__cuda_arch_bin "6.0 6.1")
10. elseif(CUDA_GENERATION STREQUAL "Volta")
11. set(__cuda_arch_bin "7.0")
12. elseif(CUDA_GENERATION STREQUAL "Auto")
13. # ...
14. endif()
 ```
  
Finally, to avoid compilation errors, the NVCC flag --expt-relaxed-constexpr needs to be set. To this end, FindCUDA.cmake needs to be adapted:

```1. set(nvcc_flags "--expt-relaxed-constexpr")```

OpenCV 2 should now be ready to be compiled with CUDA 9. As the correct GPU generation might not be selected automatically, make sure to use `-DCUDA_GENERATION` when running CMake to set the correct generation.

 - `nvcc fatal : Unsupported gpu architecture 'compute_20'`

CUDA 9.x + does not support compute_20 (Fermi), probably you will have to disable it, maybe with ccmake you can disable it manually? not sure which variable in your project is the one that is setting this, but probably you will see several numbers like 2.0, 3.0, etc. You just need to delete 2.0

 - `fatal error LNK1181: cannot open input file 'opencv_calib3d243d.lib'`
A priori du au problème de build des fonctionalités basées sur cuda, disparait une fois l'erreur ci-dessus règlée.


## Source
Install opencv with contrib 
 - https://github.com/opencv/opencv_contrib

Compile opencv 2.4.13.6 with cuda 10
 - https://stackoverflow.com/questions/46584000/cmake-error-variables-are-set-to-notfound
 - https://davidstutz.de/compiling-opencv-2-4-x-with-cuda-9/
 - https://stackoverflow.com/questions/48383846/nvcc-fatal-unsupported-gpu-architecture-compute-20-while-cuda-9-1caffeopen

