#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:29:09 2020

This script will do auto B&C as well as filter and invert, if you want.
I'll start out with the autoBC and then add  the other stuff if necessary.
The input and output directories are currently hardcoded, so you'll probably want to modify that.
The input directory can be an imaging directory with the output of wafermapper in it.
"""

#I commented out the imports that I don't think that I need. If the script doesn't work, enable them until it works.
#import time
import numpy as np
#import cv2
import os 
import gdal
import sys
#from matplotlib import pyplot as plt
#from matplotlib import image
#from scipy import ndimage
from PIL import Image
from threading import Thread
#sys.path.append('/mnt/main/code/karl/Python/')
#import Calcium2CF_autocorr

def loadImageGDAL(filepath):
    gdalObj=gdal.Open(filepath)
    rastDat=gdalObj.GetRasterBand(1)
    rawImg=rastDat.ReadAsArray()
    return rawImg

def loadImageGDAL_thread(filepath,result,stats,index):
    gdalObj=gdal.Open(filepath)
    rastDat=gdalObj.GetRasterBand(1)
    rawImg=rastDat.ReadAsArray()
    rawDatTrm=rawImg[ (rawImg>15) & (rawImg<240)]
    mean=np.mean(rawDatTrm.flatten())
    median=np.median(rawDatTrm.flatten())
    stdev=np.std(rawDatTrm.flatten())
    stats[index]=[mean,median,stdev]
    result[index]=rawImg
    return True

def redistroHisto(imDat,oldMean,newMean,oldStd,newStd):
    zeroCenterIm=imDat-oldMean
    zeroCenterAdjIm=zeroCenterIm*(newStd/oldStd)
    adjIm=zeroCenterAdjIm+newMean
    adjIm[adjIm>255]=255
    adjIm[adjIm<0]=0
    finalIm=np.uint8(adjIm)
    return finalIm

def writeImageBC_thread(filepathOut,curImg,shiftTable):
    #curImg=result
    outputImg=redistroHisto(curImg,shiftTable[0],shiftTable[1],shiftTable[2],shiftTable[3])
    outputPIL=Image.fromarray(outputImg)
    outputPIL.save(filepathOut)
    
    return True

if __name__ == '__main__':
        
    #The source directory for the wafer
    srcDir='/mnt/main/data/MasterRaw/ixQ/ixQ_waf009_IL_10nm_8x_v2/'
    dstDir='/mnt/main/data/MasterRaw/ixQ/ixQ_waf009_IL_10nm_8x_v2_procd/'
    
    dirList=os.listdir(srcDir)
    dirListClean=[s for s in dirList if s.endswith('med')]
    
    for sliceIt in range(0,1):
        curDir=dirListClean[sliceIt]
        print(curDir)
        if not os.path.exists(dstDir+curDir):
            os.mkdir(dstDir+curDir)
        imList=os.listdir(curDir)
        imListClean=[s for s in imList if s.endswith('.tif') and len(s)<30]
        sliceImDat=[{} for x in imListClean]
        imDesc=[{} for x in imListClean]
        imFullPathList=[srcDir+curDir+'/'+s for s in imListClean]
        outFullPathList=[dstDir+curDir+'/'+s for s in imListClean]

        threads=[]

        for imIt in range(len(imListClean)):
            process = Thread(target=loadImageGDAL_thread, args=[imFullPathList[imIt],sliceImDat,imDesc,imIt])
            process.start()
            threads.append(process)

        for process in threads:
            process.join()
        
        totalMean=np.mean([s[0] for s in imDesc])
        totalMedian=np.median([s[1] for s in imDesc])
        totalStdev=np.mean([s[2] for s in imDesc])
        
        totalStats=[totalMean,totalMedian,totalStdev]
        
        shiftTable=[totalMean,128,totalStdev,40]
        
        threads=[]
        
        for imIt in range(len(imListClean)):
            process = Thread(target=writeImageBC_thread, args=[outFullPathList[imIt],sliceImDat[imIt],shiftTable])
            process.start()
            threads.append(process)
            
        for process in threads:
            process.join()


##NOT E FOR FRIDAY
            #Something is going wrong with the adjusting of the iamges and the means are nowhere near 128. 
            #See the fiji stacks for diagnosis of the problem.
            
            
            
            
            
            
            
            
            