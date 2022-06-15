# mrCLEM2021
Josh Morgan Lab
Washington University in Saint Louis

# Introduction
This repository contains the scripts for image processing and registration described in ***PAPER***
These scripts run in either Python, Octave, or Matlab. The overall workflow is described below, but broadly contains the following steps:
0. Tissue sectioning
1. Image collection
2. Image preprocessing
3. Image registration
4. Image annotation
5. Analysis

## 0. Tissue sectioning
For the ATUM-SEM to section tissue with maximal reliability, the water level in the boat is maintained during sectioning by a MATLAB script that maintains the water level by monitoring the position of light reflections on the surface of the water.


## 1. Image collection
Two-photon and confocal imaging was acquired using software included with the microscope (### and Fluoview, respectively)
EM imaging was acquired using the custom software WaferMapper (Hayworth, et al. [2014](https://doi.org/10.3389/fncir.2014.00068))

## 2. Image preprocessing
Raw images were first median filtered to reduce image noise and inverted (imPreProcPNG.py). The brightness and contrast were then normalized across serial sections to aid in later processing and analysis (AutoBCbySlice_parallel.py) 
These preprocessing scripts are run directly on the output folders from WaferMapper.

## 3. Image registration
Images were imported into Trakem2 (included in ImageJ) by creating an import list of the preprocessed images (trakem2_importListMaker.py) and registered using rigid, affine, and then elastic registration (described in methods)
Any visible mis-registrations were corrected using manual landmark-based affine registration in BigWarp (included in ImageJ)
Finally, the registered stack was written to a multiresolution, mip-mapped image pyramid

## 4. Image annotation
The 3DEM volume is loaded into VAST and annotated as described in the methods.

***FINISH***
***to add***
***water monitoring
***wafermapper
***toad
***
