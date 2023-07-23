function [feature, chrominance] = extractFeature(testImage)
patchNum = 7; % patch size
edge = (patchNum-1)/2; % edge size
daisyNum = 32; % dim of daisy feature
gaborNum=40;%dim of gabor filter
I=imread(testImage);
if size(I, 3) == 3
    test_gray = rgb2gray(I);
else
    error('testImage parameter must be RGB color image');
end

%%test_gray = im2gray(I);
%% generate daisy feature
disp('Generate Daisy feature')
daizy = compute_daisy(test_gray, 7, 1, 3, 8);

%% Make input feature matrix.
test_gray = uint8(test_gray);
[r, c] = size(test_gray);


row = randi(r);
col = randi(c);

%% Patch feature.
if (row < edge) || (col < edge) || (row > r - edge) || (col > c - edge)
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

% Daisy feature
patch = display_descriptor(daizy, row-1, col-1);
daisyFeature = reshape(patch, daisyNum, 1);
feature = [patchFeature; daisyFeature];
R = I(:,:,1); 
G = I(:,:,2); 
B = I(:,:,3);
chrominance = [R(row, col) G(row, col) B(row, col)];
end