%rawImg = imread('/mnt/main/data/MasterRaw/ixQ/ixQ_waf007_BSD_20nm_quad_2/waf007_Sec030_Montage/Tile_r2-c2_waf007_sec030.tif');
%dsImg = downSampMed(rawImg);
%dsImgInv = uint8(255-dsImg);

wafDir = '/mnt/main/data/MasterRaw/ixQ/ixQ_waf009_IL_10nm_8x_v2';
dirStruct = dir(wafDir);
folderList = {dirStruct.name};
folderList = folderList(7:end);
for folder = [1:length(folderList)]
  curFolder = [wafDir '/' char(folderList{folder})];
  printf(curFolder)
  downSampMedFolder(curFolder);
end

  