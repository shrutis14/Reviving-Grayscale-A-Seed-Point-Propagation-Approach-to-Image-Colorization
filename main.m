data_path = "C:/Users/Mini project/Downloads/mini project/images/";
load('images.mat');
n = size(images);
gaborArray = gaborFilterBank(5,8,39,39);
%%for i=31:60
for i=44:44
    disp(i);
    j=i*10+1;
    [dataset] = base(data_path,images,44,gaborArray);
    T = cell2table(dataset(1:end,:));
    filename = strcat('img',num2str(i,'%d'),'.csv');
    writetable(T,filename);
    disp(j);
end