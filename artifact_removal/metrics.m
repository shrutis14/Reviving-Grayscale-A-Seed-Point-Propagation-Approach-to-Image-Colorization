ref = imread("images/original71.png");
A=imread('images/filter71.png');
ref = imresize(ref,[240 320]);
A = imresize(A,[240 320]);
[peaksnr, snr] = psnr(A, ref);
ssimval = ssim(A,ref)*100;
fprintf('\n %0.4f %f', peaksnr,ssimval);