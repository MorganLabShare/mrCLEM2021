# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:37:31 2019
# If this is too slow to load the images, you can try 
'conda install -c nanshe pylibtiff' and use his package.

fastest loading is with the arcgis tif lib stuff. for satellite images

@author: morga
"""

import os
from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter

def getImageList(imDir):
    imList=[]
    os.chdir(imDir)
    for root, dirs, files in os.walk(imDir):
        for file in files:
            if file.endswith('.tif') and len(file)==28:
                imName = os.path.join(root, file)
                imList.append(imName)
                print(imName)
    return imList
                
def loadImage(fileName):
    Image.MAX_IMAGE_PIXELS=None
    imraw = Image.open(fileName)
    return imraw

def invertImage(inputImage):
    midImage = inputImage.convert('L')
    invImage = ImageOps.invert(midImage)
    finImage = invImage.convert('P')
    return finImage

def processImage(inputImage, filtSize=3):
    midImage = inputImage.convert('L')
    filtImage = midImage.filter(ImageFilter.MedianFilter(size=filtSize))
    invImage = ImageOps.invert(filtImage)
    return invImage

def saveImage(inputImage, fileName='out.png'):
    inputImage.save(fileName, "PNG")
    return 0

def medianFilterImage(inputImage):
    filtImage = inputImage.filter(ImageFilter.MedianFilter(size=2))
    return filtImage

def autoBC(inputImage):
    print("insert code for auto brightness and contrast")

def procDir(inDir):
    imList = getImageList(inDir)
    #imListTrim = [s for s in imList if len(s)==28]
    for curIm in imList:
        #print(curIm)
        outName = curIm[:-3]+'png'
        exists = os.path.isfile(outName)
        #exists = 0
        if exists:
            print('skippingFile')
            #print(outName + ' already converted')
        else:
            imraw = loadImage(curIm)
            finImage = processImage(imraw)
            outName = curIm[:-3]+'png'
            #if exists:
            #    os.remove(outName)
            saveImage(finImage, outName)

#dirList = os.listdir('Y:\\Active\\Data\\AT\\Morgan Lab\\MasterRaw\\ixQ\\ixQ_waf008_IL_04nm_testAF')
#dirList = dirList[4:]

dirList = os.listdir('/mnt/main/data/MasterRaw/ixQ/ixQ_waf007_IL_04nm_slow')
dirList = dirList[5:]
srcDir = '/mnt/main/data/MasterRaw/ixQ/ixQ_waf007_IL_04nm_slow/'

for sliceDir in dirList:
    inDir = os.path.join(srcDir,sliceDir)
    procDir(inDir)

dstDir = '/mnt/main/data/MasterRaw/ixQ/ixQ_waf007_IL_04nm_slow/'


#dirList = os.listdir('/media/morganlab/Shadowfax/MasterRaw/ixQ/ixQ_waf007_IL_04nm')
#
#srcDir = '/media/morganlab/Shadowfax/MasterRaw/ixQ/ixQ_waf007_IL_04nm/'
#dirList = dirList[4:]
#for sliceDir in dirList:
#    inDir = os.path.join(srcDir,sliceDir)
#    procDir(inDir)
#
#
#dirList = os.listdir('/media/morganlab/Shadowfax/MasterRaw/ixQ/ixQ_waf009_IL_04nm_slow')
#dirList = dirList[3:]
#srcDir = '/media/morganlab/Shadowfax/MasterRaw/ixQ/ixQ_waf009_IL_04nm_slow/'

for sliceDir in dirList:
    inDir = os.path.join(srcDir,sliceDir)
    procDir(inDir)

os.chdir(inDir)
for root, dirs, files in os.walk(inDir):
    for file in files:
        if file.endswith(".tif"):
            inName = os.path.join(root, file)
            print(inName)
            imraw = loadImage(inName)
            iminv = invertImage(imraw)
            saveImage(iminv, inName)
            