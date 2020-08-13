# this code generates augmented images. uncomment any of the augmentation type
# to get augmented images. (code chunk 69-78)

from PIL import Image
import os
import cv2
import glob
import numpy as np
from scipy import ndimage
from scipy.ndimage import zoom


# her db icin farkli dosyalar olustur
# her db icin farkli augmented dosyalar olustur
# duzeni koru

images = [cv2.imread(file) for file in glob.glob("/Users/boyaronur/Desktop/FACE/women_ar/women_ar_sketch_1.5/*.jpg")]

print(np.asarray(images).shape)
names = [os.path.split(file)[-1] for file in glob.glob("/Users/boyaronur/Desktop/FACE/women_ar/women_ar_sketch_1.5/*.jpg")]
print(np.asarray(names).shape)
counter = 0
os.chdir("/Users/boyaronur/Desktop/FACE/women_ar/sketch_denoise")

def clipped_zoom(img, zoom_factor, **kwargs):

    h, w = img.shape[:2]

    # For multichannel images we don't want to apply the zoom factor to the RGB
    # dimension, so instead we create a tuple of zoom factors, one per array
    # dimension, with 1's for any trailing dimensions after the width and height.
    zoom_tuple = (zoom_factor,) * 2 + (1,) * (img.ndim - 2)

    # Zooming out
    if zoom_factor < 1:

        # Bounding box of the zoomed-out image within the output array
        zh = int(np.round(h * zoom_factor))
        zw = int(np.round(w * zoom_factor))
        top = (h - zh) // 2
        left = (w - zw) // 2

        # Zero-padding
        out = np.zeros_like(img)
        out[top:top+zh, left:left+zw] = zoom(img, zoom_tuple, **kwargs)

    # Zooming in
    elif zoom_factor > 1:

        # Bounding box of the zoomed-in region within the input array
        zh = int(np.round(h / zoom_factor))
        zw = int(np.round(w / zoom_factor))
        top = (h - zh) // 2
        left = (w - zw) // 2

        out = zoom(img[top:top+zh, left:left+zw], zoom_tuple, **kwargs)

        # `out` might still be slightly larger than `img` due to rounding, so
        # trim off any extra pixels at the edges
        trim_top = ((out.shape[0] - h) // 2)
        trim_left = ((out.shape[1] - w) // 2)
        out = out[trim_top:trim_top+h, trim_left:trim_left+w]

    # If zoom_factor == 1, just return the input array
    else:
        out = img
    return out

for image in images:
    #img_rs = np.array(Image.fromarray(image).resize((32, 32), Image.ANTIALIAS))
    #im = clipped_zoom(image,1.5)
    im = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)
    #im = ndimage.rotate(image, 90)
    #im = np.flipud(image)
    #print(img_rs.shape)
    image_name = names[counter]
    counter += 1
    cv2.imwrite(image_name, im)
