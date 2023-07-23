function [feature,rgbval] = ipFeature(I,daizy,gabor,row,col)
patchNum = 7; % patch size
edge = (patchNum-1)/2; % edge size
daisyNum = 32; % dim of daisy feature
gaborNum = 40;%dim of gabor filter
test_gray = rgb2gray(I);
%test_gray= imresize(test_gray,[320 240]);
%% Make input feature matrix.
test_gray = uint8(test_gray);
%% Patch feature.
[r,c] = size(test_gray);
if (row <= edge) || (col <= edge) || (row >= r - edge) || (col >= c - edge)
    patch = test_gray(row, col)*uint8(ones(patchNum,patchNum));
    for a=-edge:edge
        for b=-edge:edge
            if((row+a>0) && (row+a<=r) && (col+b>0) && (col+b<=c))
                patch(edge+1+a, edge+1+b) = test_gray(row+a, col+b);
            end
        end
    end
else
    patch = test_gray(row-edge:row+edge,col-edge:col+edge);
end
patchFeature = reshape(patch, patchNum*patchNum, 1);
patchFeature = double(patchFeature) / 255;
patchFeature = num2cell(patchFeature);

% Daisy feature
patch = display_descriptor(daizy, row-1, col-1);
daisyFeature = reshape(patch, daisyNum, 1);
daisyFeature = num2cell(daisyFeature);
% gabor feature
[u,v] = size(gabor);
gaborMatrix = cell(u,v);
for i = 1:u
    for j = 1:v
        gaborMatrix{i,j} = gabor{i,j}(row,col); 
    end
end
gaborFeature=reshape(gaborMatrix,gaborNum,1);

feature = [patchFeature; daisyFeature; gaborFeature];
R = I(:,:,1); 
G = I(:,:,2); 
B = I(:,:,3);
rgbval = [R(row, col) G(row, col) B(row, col)];
end