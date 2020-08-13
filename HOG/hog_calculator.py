### this code takes photograph image and the sketch image than extracts
# their HOG features. It calculates distances between those and writes it.
# The size of the image set should be corrected everytime image set changes.



import numpy as np
from scipy import ndimage
import scipy.misc
import os
from PIL import Image
import pandas as pd
import glob
import cv2
from scipy import ndimage
import scipy.misc
import math
from numpy import dot
from numpy.linalg import norm
from skimage import data, color, feature
import skimage.data
from skimage import io

#images = [scipy.misc.imread(file) for file in glob.glob("/Users/boyaronur/Desktop/FACE/resized_photos_AR_128/*.jpeg")]
#names = [os.path.split(file)[-1] for file in glob.glob("/Users/boyaronur/Desktop/FACE/resized_photos_AR_128/*.jpeg")]
#images2 = [scipy.misc.imread(file) for file in glob.glob("/Users/boyaronur/Desktop/FACE/resized_sketch_AR_128/*.jpg")]
#names2 = [os.path.split(file)[-1] for file in glob.glob("/Users/boyaronur/Desktop/FACE/resized_sketch_AR_128/*.jpg")]

directory = '/Users/boyaronur/Desktop/FACE/women_cuhk/women_photo_denoise'
os.chdir(directory)
directory_dir  = os.listdir(directory)
directory_dir = sorted(directory_dir)
print("PHOTO")
print(directory_dir)

tensor = np.ndarray(shape = (54, 128*128), dtype = np.float64)

for i in range(0,54):
    print(directory_dir[i])
    img = io.imread(directory_dir[i], as_gray=True)
    tensor[i,:] = np.array(img, dtype='float64').flatten()


photos_tensor = tensor.reshape(54, 128, 128)

directory = '/Users/boyaronur/Desktop/FACE/women_cuhk/women_sketch'
os.chdir(directory)
directory_dir  = os.listdir(directory)
directory_dir = sorted(directory_dir)
print("SKETCH")
print(directory_dir)

tensor2 = np.ndarray(shape = (54, 128*128), dtype = np.float64)


for i in range(0,54):
    print(directory_dir[i])
    img = io.imread(directory_dir[i], as_gray=True)
    tensor2[i,:] = np.array(img, dtype='float64').flatten()


sketch_tensor = tensor2.reshape(54, 128, 128)

dist_euc_cuhk = np.ndarray(shape=(54,54))
dist_cos_cuhk = np.ndarray(shape=(54,54))
dist_chi_cuhk = np.ndarray(shape=(54,54))

def chiSquared(p,q):
    return 0.5*np.sum((p-q)**2/(p+q+1e-6))


counter1 = 0
for i in range(0,54):

    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hog_vec, hog_vis = feature.hog(photos_tensor[i], orientations=9, pixels_per_cell=(8, 8),
                        cells_per_block=(2, 2), visualise=True)
    counter2 = 0
    for j in range(0,54):
        hog_vec2, hog_vis2 = feature.hog(sketch_tensor[j], orientations=9, pixels_per_cell=(8, 8),
                                cells_per_block=(2,2), visualise=True)

        dist_euclidean = math.sqrt(sum((hog_vec - hog_vec2)**2)) #/ matrix_1.size
        cos_sim = 1 - np.inner(hog_vec, hog_vec2)/(norm(hog_vec)*norm(hog_vec2))
        chi_sq = chiSquared(hog_vec, hog_vec2)
        dist_euc_cuhk[counter1,counter2] = dist_euclidean
        dist_cos_cuhk[counter1,counter2] = cos_sim
        dist_chi_cuhk[counter1,counter2] = chi_sq
        print(dist_euclidean)
        counter2 = counter2 + 1

    counter1 = counter1 + 1

print(counter1)
print(counter2)
print(dist_chi_cuhk)
os.chdir("/Users/boyaronur/Desktop")
np.savetxt("euclidean_cuhk_women_ph_denoise.csv", dist_euc_cuhk, delimiter=",")
np.savetxt("chi_sq_cuhk_women_ph_denoise.csv", dist_chi_cuhk, delimiter=",")
np.savetxt("cosine_cuhk_women_ph_denoise.csv", dist_cos_cuhk, delimiter=",")
