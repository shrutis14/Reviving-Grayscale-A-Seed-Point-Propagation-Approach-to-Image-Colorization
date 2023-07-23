function[dataset] = base(data_path,images,j,gaborArray)
dataset = [];
for i = j:j
    %disp(i);
    %image_path = strcat(data_path, images{i});
    image_path=data_path;
    I=imread(image_path);
    I = imresize(I,[240 320]);
    %imshow(I);
    if size(I, 3) ~= 3
        continue
    end
    
    [daisy,gabor] = totalFeature(I,gaborArray);
    [interestPoints] = slic(I);
    [u,~] = size(interestPoints);
    feat_col=cell(u,4);
    for j = 1:u
        [feature,rgbval] = ipFeature(I,daisy,gabor,interestPoints{j,2},interestPoints{j,1});
        feat_col{j,1}=transpose(feature);
        feat_col{j,4}=double(rgbval)/255;
        feat_col{j,2}=(interestPoints{j,2});
        feat_col{j,3}=(interestPoints{j,1});
        %disp(j)
    end
    dataset = [dataset; feat_col];
end
%disp("--------------------------");
end
