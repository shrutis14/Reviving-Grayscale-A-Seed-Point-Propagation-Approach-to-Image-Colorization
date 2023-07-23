function[interestPoints] = slic(I)
[L,N] = superpixels(I,2133,"Compactness",10,"Method","slic"); 
s = regionprops(L,'centroid');
interestPoints = cat(1,s.Centroid);
interestPoints = round(interestPoints);
interestPoints=num2cell(interestPoints);
%disp(N)
end
