#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:51:44 2020

@author: karl
"""

import os

outputPath = '/mnt/main/data/trakem2/ixQ_lowres_quad_full_v1/'
imagePath =  '/mnt/main/data/MasterRaw/ixQ/ixQ_waf001_IL_10nm_8x_v1/'
outputFileString = 'tm2_import_ixQ_lowres_waf001.txt'
sliceNum = 1046
tileSize = 4000
overlap = 0.08
tileStep = tileSize*(1-overlap)
flobj=open(outputPath+outputFileString,"w+")
zoffset = 0
#zoffset = 168*10

if os.path.isdir(outputPath):
    g=1
else:
    print("Output Path Doesn't Exist")

if os.path.isdir(imagePath):
    g=1
else:
    print("Image Path Doesn't Exist")

montSize = (8,8)
for curSlice in range(sliceNum):
    sliceDir = 'waf001b_Sec'+str(curSlice+1).rjust(3,'0')+'_Montage_med/'
    for row in range(montSize[1]):
        for col in range(montSize[0]):
            curTileString = 'Tile_r'+str(row+1)+'-c'+str(col+1)+'_waf001b_sec'+str(curSlice+1).rjust(3,'0')+'.tif'
            imFullPath = imagePath+sliceDir+curTileString
            if os.path.exists(imFullPath):
                colLoc = int(col*tileStep)
                rowLoc = int(row*tileStep)
                outputString = imFullPath + " " + str(colLoc) + " " + str(rowLoc) + " " + str(int(curSlice*10+zoffset))
                flobj.write(outputString+"\n")
flobj.close()