
pkg load image

SPN = '/mnt/main/data/trakem2/ixQ_lowres_quad_TM2_export2/';
SPN = '/mnt/main/data/scm/tiffs/2020-02-06-migrated-segmentation-full-slice/'
SPN = '/mnt/main/data/VAST/scm_ixQ_hires_pyr/'
SPN = '/mnt/main/data/VAST/scm_ixQ_seg_pyr/'

secDir = dir(SPN);
secDir(1:2) = [];
secFold = {secDir([secDir.isdir]>0).name};

iSize = 4096;

for s = 0:500 %length(secFold)
    #sec = str2num(secFold{s})
    sec=s;
    if ~isempty(sec)
        %mipDir = [SPN secFold{s} '/'];
        mipDir = [SPN num2str(sec) '/'];
        if exist(mipDir)
          inDir = dir(mipDir);
          inDir(1:2)=[];
          mipLevs = {inDir.name};
          maxLev = 0;
  %         for i = 1:length(mipLevs);
  %             if ~isempty(str2num(mipLevs{i}));
  %                 maxLev = max(maxLev,str2num(mipLevs{i}));
  %             end
  %         end
          
          for m = maxLev : 8;
              mipSPN = [mipDir num2str(m) '/'];
              mipTPN = [mipDir num2str(m+1) '/'];
              if ~exist(mipTPN,'dir'),mkdir(mipTPN);end
              dirMipSPN = dir([mipSPN '*.png']);
              inams = {dirMipSPN.name};
              
              clear r c
              for i  = 1:length(inams);
                  nam = inams{i};
                  A = sscanf(nam,'%d_%d');
                  r(i) = A(1);
                  c(i) = A(2);
              end
              
              colormap gray
              
              for y = 0:ceil(max(r)/2)
                  for x = 0:ceil(max(c)/2)
                      I = zeros(iSize,'uint8');
                      for yD = 0:1;
                          for xD = 0:1;
                              targ = find((r == (y * 2 + yD)) & (c ==  (x * 2 + xD)));
                              if ~isempty(targ)
                                  Iraw = imread([mipSPN inams{targ}]);
                                  if size(Iraw)(1)<iSize
                                      Iraw=padarray(Iraw,[iSize-size(Iraw)(1),0],'post');
                                  end
                                  if size(Iraw)(2)<iSize
                                      Iraw=padarray(Iraw,[0,iSize-size(Iraw)(2)],'post');
                                  end
                                  Idown = imresize(Iraw,.5,'bilinear');
                                  I(yD*iSize/2+1:(yD+1)*iSize/2, xD*iSize/2+1:(xD+1)*iSize/2) = Idown;
                              end
                          end
                      end
  %                     image(I)
  %                     pause(.1)
                      
                      newName = sprintf('%d_%d.png',y,x);
                      imwrite(I,[mipTPN newName]);
                  end
              end
            end
        end
        
        
    end
end