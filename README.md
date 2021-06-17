# mrCLEM2021
Josh Morgan Lab
Washington University in Saint Louis

# Introduction
This repository contains the scripts for image processing and registration described in ***PAPER***
These scripts run in either Python, Octave, or Matlab. The overall workflow is described below, but broadly contains the following steps:
1. Image collection
2. Image preprocessing
3. Image registration
4. Image annotation
5. Analysis

## 1. Image collection
Two-photon and confocal imaging was acquired using software included with the microscope (### and Fluoview, respectively)
EM imaging was acquired using the custom software WaferMapper (***REF***)

## 2. Image preprocessing
Raw images were first median filtered to reduce image noise. The brightness and contrast were then normalized across serial sections to aid in later processing and analysis

## 3. Image registration
Images were imported into Trakem2 (included in ImageJ) and registered using rigid, affine, and then elastic registration (described in methods)
Any visible mis-registrations were corrected using manual landmark-based affine registration in BigWarp (included in ImageJ)
Finally, the registered stack was written to a multiresolution, mip-mapped image pyramid

## 4. Image annotation


***FINISH***
***to add***
***water monitoring
***wafermapper
***toad
***
