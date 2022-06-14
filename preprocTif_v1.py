#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:04:17 2019

@author: karl
"""

import time
import numpy as np
#import cv2
import os 
import gdal
import sys
from matplotlib import pyplot as plt
from matplotlib import image
from scipy import ndimage
from PIL import Image
#from scipy import signal

def invertImg(inputArray):
    outputArray=255-inputArray
    return outputArray

#def filtImg2(inputArray, medSize=3):
#    outputArray=signal.medfilt(inputArray,kernel_size=medSize)
#    return outputArray

def filtImg(inputArray, medSize=3):
    outputArray=ndimage.median_filter(inputArray,medSize)
    return outputArray

def normHist(inputArray, lowCut=10, highCut=245, stDev=50):
    #gets out the artifacts
    imgTrim=inputArray[np.logical_and(inputArray>lowCut,inputArray<highCut)]
    #get the mean and std
    imgMean=np.mean(imgTrim)
    imgStd=np.std(imgTrim)
    #center the distribution
    centeredArray = (inputArray+(128-imgMean))
    stDevRatio = stDev / imgStd
    scaledArray = 128+((centeredArray-128)*stDevRatio)
    scaledArray[scaledArray<0]=0
    scaledArray[scaledArray>255]=255
    outputArray = np.uint8(scaledArray)        
    return outputArray

def shimage(npRA):
    plt.imshow(npRA,cmap='gray')

srcDir = '/mnt/main/data/MasterRaw/ixQ/ixQ_waf007_IL_04nm_slow'
dstDir = '/mnt/main/data/preprocPNG/ixQ/ixQ_waf007_IL_04nm_slow'
#if sys.argv[0]:
#    srcDir=sys.argv[0]

srcDirList = ['/mnt/main/data/MasterRaw/ixQ/ixQ_waf001_IL_04nm_slow_v2',
              '/mnt/main/data/MasterRaw/ixQ/ixQ_waf002_IL_04nm_slow_inv', 
              '/mnt/main/data/MasterRaw/ixQ/ixQ_waf003_IL_04nm_slow_inv',
              '/mnt/main/data/MasterRaw/ixQ/ixQ_waf007_IL_04nm_slow',
              '/mnt/main/data/MasterRaw/ixQ/ixQ_waf008_IL_04nm_slow',
              '/mnt/main/data/MasterRaw/ixQ/ixQ_waf009_IL_04nm_slow',
              '/mnt/main/data/MasterRaw/ixQ/ixQ_waf010_IL_04nm_slow']

dstDirList = ['/mnt/main/data/preprocPNG/ixQ/ixQ_waf001_IL_04nm_slow_v2',
              '/mnt/main/data/preprocPNG/ixQ/ixQ_waf002_IL_04nm_slow_inv',
              '/mnt/main/data/preprocPNG/ixQ/ixQ_waf003_IL_04nm_slow_inv',
              '/mnt/main/data/preprocPNG/ixQ/ixQ_waf007_IL_04nm_slow',
              '/mnt/main/data/preprocPNG/ixQ/ixQ_waf008_IL_04nm_slow',
              '/mnt/main/data/preprocPNG/ixQ/ixQ_waf009_IL_04nm_slow',
              '/mnt/main/data/preprocPNG/ixQ/ixQ_waf010_IL_04nm_slow']

for wafer in [3,6]:
    srcDir = srcDirList[wafer]
    dstDir = dstDirList[wafer]
    if not os.path.isdir(dstDir):
        os.mkdir(dstDir)
    sliceList = os.listdir(srcDir)
    sliceList = [s for s in sliceList if "Montage" in s]
    for curSlice in sliceList:
        print(curSlice)
        if not os.path.isdir(dstDir + '/' + curSlice):
            os.mkdir(dstDir + '/' + curSlice)
        tifList = [s for s in os.listdir(srcDir + '/' + curSlice) if s.endswith("tif") and s.startswith("Tile")]
        for tifFile in tifList:
            if len(tifFile)<40:
                print(tifFile)
                gdalObj=gdal.Open(srcDir + '/' + curSlice + '/' + tifFile)
                rastDat=gdalObj.GetRasterBand(1)
                rawImg=rastDat.ReadAsArray()
                #normalize histo
                normd=normHist(rawImg)
                #median filter
                filtrd=filtImg(normd)
                #invert image
                invrtd=invertImg(filtrd)
                outputImg=invrtd
                outputFilename=dstDir + '/' + curSlice + '/' + tifFile[:-3] + 'tif'
        #        image.imsave(outputFilename,outputImg)
                imgOut=Image.fromarray(outputImg)
                imgOut.save(outputFilename)
            
            
    #### TESTING BLOCK #######
    #start=time.time()
    #testout = filtImg(inputArray,medSize=3)
    #stop=time.time()
    #print(stop-start)
