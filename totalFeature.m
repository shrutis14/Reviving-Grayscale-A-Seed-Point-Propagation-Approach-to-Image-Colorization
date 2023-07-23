function [daisy,gabor] = totalFeature(I,gaborArray)
test_gray = rgb2gray(I);
%test_gray= imresize(test_gray,[320 240]);
%% generate daisy feature
%disp('Generate Daisy feature')
daisy = compute_daisy(test_gray, 7, 1, 3, 8);
%% generate gabor feature
%disp('Generate Gabor feature')
img = double(test_gray);
%% Filter the image using the Gabor filter bank
% Filter input image by each Gabor filter
[u,v] = size(gaborArray);
gabor = cell(u,v);
for i = 1:u
    for j = 1:v
        gabor{i,j} = imfilter(img, gaborArray{i,j});
    end
end
end