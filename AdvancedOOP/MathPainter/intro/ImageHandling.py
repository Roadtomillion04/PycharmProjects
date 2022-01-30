from PIL import Image
import numpy as np
from random import randint

# Why np.uint8? This is used for arrays representing images, with the 3 color channels having small integer values (0 to 255)
data = np.zeros(shape= (5, 4, 3), dtype= np.uint8)

    #row, col
data[4:5, 3:4] = [randint(0, 255),
                  randint(0, 255),
                  randint(0, 255)] # fill the values with RGB colors
print(data)

# Creates an image by the given 3d array, The 3rd dimension of array represents the color channels
img = Image.fromarray(obj= data, mode= 'RGB')
img.save(fp= 'image.png')
