function[]=testing(p)
myFolder = "barn_all\\barn";
if ~isdir(myFolder)
  errorMessage = sprintf('Error: The following folder does not exist:\n%s', myFolder);
  uiwait(warndlg(errorMessage));
  return;
end
filePattern = fullfile(myFolder, '*.jpg');
jpegFiles = dir(filePattern);
a=transpose(struct2cell(jpegFiles));
j=[];
for i =1:length(a)
    j=[j;a{i}];
end
barn_images=cellstr(j);
%disp(barn_images);
%disp(p);
newmain(p,barn_images);