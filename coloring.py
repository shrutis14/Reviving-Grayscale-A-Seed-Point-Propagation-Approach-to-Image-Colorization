import pandas as pd
import numpy as np
from numpy import random
from sklearn.model_selection import train_test_split
import tensorflow as tf
def colorip(p):
    df = pd.read_csv('C:\\Users\\shrut\\OneDrive\\Desktop\\final_code\\feature.csv')
    lst = [i for i in range(0,121)]
    input= df.iloc[:,lst].values
    x= df.iloc[:, 121].values
    y= df.iloc[:, 122].values
    output =df.iloc[:,[123,124,125]].values
    output = output*255
    output=output.astype(int)
    
    ra=random.randint(len(output), size=(150))
    for i in range(len(ra)):
        output[ra[i]] = [255,255,255]
    #print(ra)
    from PIL import Image
    # Load the RGB image
    # rgb_img = Image.open('wavepic.jpg')
    rgb_img = Image.open(p)
    rgb_img=rgb_img.resize((320, 240))
    # rgb_img.save('check.png')
    # Convert the image to grayscale
    grayscale_img = rgb_img.convert('L')
    grayscale_img.save('gray.png')
    # Load the grayscale image
    img = Image.open('gray.png')

    for i in range(0,len(output)):
        a=x[i]-1
        b=y[i]-1
    # Convert the RGB values to grayscale intensity
        intensity = int(0.2989 * output[i][0] + 0.5870 * output[i][1] + 0.1140 * output[i][2])
        # Replace the pixel value in the grayscale image with the intensity value
    # print(i)
        img.putpixel((b,a), intensity)
    
    # Convert the grayscale image back to RGB
    rgb_img = img.convert('RGB')

    for i in range(0,len(output)):
        a=x[i]-1
        b=y[i]-1
        # Set the RGB values of the interest points
        rgb_img.putpixel((b,a), tuple([min(255,max(0,output[i][0]-random.randint(-20,50))),min(255,max(output[i][1]-random.randint(-20,50),0)),min(255,max(0,output[i][2]-random.randint(-20,50)))]))

    # Save the modified image
    rgb_img.save('partial.png')