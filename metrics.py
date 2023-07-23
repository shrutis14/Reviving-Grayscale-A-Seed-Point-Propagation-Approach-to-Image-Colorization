from math import log10, sqrt
import cv2
import numpy as np
from skimage.metrics import structural_similarity

import os
from os import listdir


def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

# names = ['ar1','barn1','zg1','wave','oh1']
# names = ['alley' ,'apse','dessert','doorway','yard']


def metrics(original,colorized):
    img1 = cv2.imread(original)
    img1 = cv2.resize(img1,(320,240))
    img2 = cv2.imread(colorized)
    value = PSNR(img1, img2)
    (score,diff) = structural_similarity(img1,img2,full=True,channel_axis=2)
    return [value,score]
    