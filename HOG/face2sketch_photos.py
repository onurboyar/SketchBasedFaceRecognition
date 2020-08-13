# this code takes photograph images as input and converts them into a sketch - like images.

import cv2
import os
from PIL import Image
import numpy as np
import glob
import scipy.ndimage

images = [cv2.imread(file) for file in glob.glob("/Users/boyaronur/Desktop/cmpe58z/cuhk/cropped/photos-2/*.jpg")]
print(np.asarray(images).shape)
names = [os.path.split(file)[-1] for file in glob.glob("/Users/boyaronur/Desktop/cmpe58z/cuhk/cropped/photos-2/*.jpg")]
print(np.asarray(names).shape)

os.chdir("/Users/boyaronur/Desktop/cmpe58z/cuhk/cropped/photos_32_cuhk")

def dodgeV2(image, mask):
  return cv2.divide(image, 255-mask, scale=256)

def grayscale(rgb):
 return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def dodge(front,back):
 result=front*255/(255-back + 0.0001)
 result[result>255]=255
 result[back==255]=255
 return result.astype('uint8')

counter = 0

for image in images:
    print('ss')
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray_2 = grayscale(image)
    img_gray_inv = 255 - img_gray
    img_gray_inv_2 = 255 - img_gray_2
    img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(61, 61),
                            sigmaX=15, sigmaY=0)
    blur_img = scipy.ndimage.filters.gaussian_filter(img_gray_inv_2,sigma=30)
    img_blend = dodgeV2(img_gray, img_blur)
    img_blend_2 = dodge(blur_img, img_gray)
    img_rs = np.array(Image.fromarray(img_blend).resize((32, 32), Image.ANTIALIAS))

    cv2.imwrite(names[counter], img_rs)
    counter+=1
