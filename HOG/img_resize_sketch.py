# this code takes sketch image as input and resizes it into 128x128

from PIL import Image
import os
import cv2
import glob
import numpy as np


images = [cv2.imread(file) for file in glob.glob("/Users/boyaronur/Desktop/AR_DB/photos/*.jpeg")]
print(np.asarray(images).shape)
names = [os.path.split(file)[-1] for file in glob.glob("/Users/boyaronur/Desktop/AR_DB/photos/*.jpeg")]
print(np.asarray(names).shape)
counter = 0
os.chdir("/Users/boyaronur/Desktop/FACE/Photo_Gray_AR")
# 32 x 32 ye cevirdim
for image in images:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_rs = np.array(Image.fromarray(image).resize((128, 128), Image.ANTIALIAS))
    print(img_rs.shape)
    image_name = names[counter]
    counter += 1
    cv2.imwrite(image_name, img_rs)
