import cv2
import numpy as np
import matplotlib.pyplot as plt

img_name = 'lena'
img_format = '.png'

# img = cv2.imread(img_name + img_format, cv2.IMREAD_COLOR)
#
# cv2.imshow('image',img)
# #cv2.waitKey(0)
# cv2.destroyAllWindows()

import math
from PIL import Image
im = Image.open('lena.png')
pixelMap = im.load()
import numpy



###############  VECTORIZACION  ##################

horSize = 8
verSize = 8
#n_vectors = (im.size[0] * im.size[1]) / (horSize * verSize)
matrix_array = []



# for vect in range(n_vectors):

for i in range(0, im.size[0], horSize):
    for j in range(0, im.size[1], verSize):
        v = numpy.zeros((horSize, verSize, 3))
        for k in range(0, horSize, 1):
            for l in range(0, verSize, 1):
                v[k, l] = pixelMap[i + k, j + l]
        matrix_array.append(v)
    #vect += 1


matrix_array_dct = []

for i in range(0, im.size[0], horSize):
    for j in range(0, im.size[1], verSize):
        #v = numpy.zeros((horSize, verSize, 3))
        for k in range(0, horSize, 1):
            for l in range(0, verSize, 1):
                v[k, l] = (0,0,0)
        matrix_array_dct.append(v)





#matrix_array_tup = tuple(matrix_array.astype(int))

img = Image.new( im.mode, im.size)
pixelsNew = img.load()

vect = 0

math.cos()

for i in range(0,matrix_array.__len__()/horSize,horSize):
    for j in range(0,matrix_array.__len__()/verSize,verSize):
        for k in range(0, horSize, 1):
            for l in range(0, verSize, 1):
                if (i+k >= 512 or j+l >= 512):
                    print 'aiuda :('
                pixelsNew[i+k,j+l] = tuple(matrix_array[vect][k,l].astype(int))
        vect += 1

img.show()
img.close()
