function[]=newmain(p,barn_images)
data_path = "barn_all\\barn\\";
%%load('k.mat');
n = size(barn_images);
gaborArray = gaborFilterBank(5,8,39,39);
%%for i=31:60
for i=17:17
    j=i*10+1;
    [dataset] = base(p,barn_images,17,gaborArray);
    T = cell2table(dataset(1:end,:));
    filename = strcat('feature','.csv');
    writetable(T,filename);
    disp('features extracted');
    %disp(p);
end