# Makes the tile list for importing in trakem2

#select the output filename
fileOut = open("low-res-waf003.txt","w")
#these are the strings of the tiles
tileString = ["r1-c1","r1-c2","r2-c1","r2-c2"]
# x coordinates for the above strings
xCoords = [0,15073,0,15073]
# y coordinates for the above strings
yCoords = [0,0,15073,15073]
# Which wafers to run through in the following lists
waferNum =4
# The extension on the files. Can change to png if preprocessed + compressed
fileExt=".tif"
# a list of the strings in the slice directories
waferSecDirStringList = ["waf001b_Sec","waf002_Sec","waf003_Sec","waf007_Sec",
	"waf008_Sec","waf009_Sec","waf010_Sec","waf011_Sec"]
# a list of the strings in the actual image filenames
waferSecTileStringList = ["_waf001b_sec","_waf002_sec","_waf003_sec","_waf007_sec",
	"_waf008_sec","_waf009_sec","_waf010_sec","_waf011_sec"]
# directories for each of the wafers
dirStringList = ["/mnt/main/data/MasterRaw/ixQ/ixQ_waf001_IL_04nm_slow_v2/",
	"/mnt/main/data/MasterRaw/ixQ/ixQ_waf002_IL_04nm_slow_inv/",
	#"/mnt/main/data/MasterRaw/ixQ/ixQ_waf003_IL_04nm_slow_inv/",
    "/mnt/main/data/MasterRaw/ixQ/ixQ_waf003_BSD_20nm/"
#	"/mnt/main/data/MasterRaw/ixQ/ixQ_waf007_IL_04nm_slow/",
    "/mnt/main/data/MasterRaw/ixQ/ixQ_waf007_BSD_20nm_quad_2/",
	"/mnt/main/data/MasterRaw/ixQ/ixQ_waf008_IL_04nm_slow/",
	#"/mnt/main/data/MasterRaw/ixQ/ixQ_waf009_IL_04nm_slow/",
	"/mnt/main/data/MasterRaw/ixQ/ixQ_waf009_IL_10nm_8x_v2/"
    "/mnt/main/data/MasterRaw/ixQ/ixQ_waf010_IL_04nm_slow/",
	"/home/morganlab/Desktop/DroboLink/ixQ/EM/ixQ_waf011_IL_04nm_slow/"]
# The number of slices in each of the directories
sliceNumList = [168,142,31,199,190,185,137,188]
# The beginning z position of the whole stack.
# You can change this value if you are updating a stack that already exists
zPosEnd = 0

#Main loop
for wafer in range(waferNum):
    #Get the number of slices for the wafer
    sliceNum=sliceNumList[wafer] 
    # Calculate the cumulative z position
    zPos = sum(sliceNumList[:wafer])
    # Get the range of the slicenumbers for the current wafer
    sliceRangeA = range(1,sliceNum+1)
    # get the directory for this wafer
    rootDir=dirStringList[wafer]
    # loop for stepping through the slices for the current wafer
    for curSlice in sliceRangeA:
        # Make a string for the current slice directory
        curDir = rootDir + waferSecDirStringList[wafer] + format(curSlice, "03d") + "_Montage_med/"
        # Step through the Tiles for each slice
        for i in range(0,4):
            # create the files names and coordinates for the individual tiles
            fileName = "Tile_" + tileString[i] + waferSecTileStringList[wafer] + format(curSlice, "03d") + fileExt + \
                " " + str(xCoords[i]) + " " + str(yCoords[i]) + " " + str((zPos+curSlice-1)*10) + "\n"
            #write out to the output files
            fileOut.write(curDir + fileName)
