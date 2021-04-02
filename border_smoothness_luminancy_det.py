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






############# IMAGEN EN BYN #########################

from PIL import Image
im = Image.open('lena.png')
pixelMap = im.load()

img = Image.new( im.mode, im.size)
pixelsNew = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):

        bnValue = (pixelMap[i,j][0])/3 + (pixelMap[i,j][1])/3 + (pixelMap[i,j][2])/3
        pixelsNew[i,j] = (bnValue,bnValue,bnValue)




###################### DETECTOR DE BORDES #############################


img_2 = Image.new( im.mode, im.size)
pixelsNew_2 = img_2.load()

delta = 10
# threshold = 80

for i in range(img_2.size[0] - delta):
    for j in range(img_2.size[1] - delta):
        w1 = 0
        w2 = 0
        for k in range(1,delta,1):
            lum_value_1 = (pixelMap[i,j-k][0])/3 + (pixelMap[i,j-k][1])/3 + (pixelMap[i,j-k][2])/3
            w1 += lum_value_1/delta
            lum_value_2 = (pixelMap[i,j+k][0])/3 + (pixelMap[i,j+k][1])/3 + (pixelMap[i,j+k][2])/3
            w2 += lum_value_2/delta
        threshold = (w1+w2)/8
        if abs(w1-w2) < threshold:
            pixelsNew_2[i,j] = (0,0,0)
        else:
            pixelsNew_2[i,j] = (127,127,127)

for i in range(img_2.size[0] - delta):
    for j in range(img_2.size[1] - delta):
        w1 = 0
        w2 = 0
        for k in range(1, delta, 1):
            lum_value_1 = (pixelMap[i - k , j][0]) / 3 + (pixelMap[i - k, j][1]) / 3 + (pixelMap[i - k, j][2]) / 3
            w1 += lum_value_1 / delta
            lum_value_2 = (pixelMap[i + k, j][0]) / 3 + (pixelMap[i + k, j][1]) / 3 + (pixelMap[i + k, j][2]) / 3
            w2 += lum_value_2 / delta
        threshold = (w1 + w2) / 8
        if abs(w1 - w2) > threshold:
            if pixelsNew_2[i,j] == (127,127,127):
                pixelsNew_2[i,j] = (255,255,255)
            else:
                pixelsNew_2[i,j] = (127,127,127)
        else:
            if pixelsNew_2[i,j] == (127,127,127):
                pixelsNew_2[i,j] = (127,127,127)
            else:
                pixelsNew_2[i,j] = (0,0,0)

            #pixelsNew_2[i, j][0] += 127
            #pixelsNew_2[i, j][1] += 127
            #pixelsNew_2[i, j][2] += 127

            #pixelsNew_2[i, j][0] += 0
            #pixelsNew_2[i, j][1] += 0
            #pixelsNew_2[i, j][2] += 0





############### IMAGEN EN RELIEVE #########################

img_3 = Image.new( im.mode, im.size)
pixelsNew_3 = img_3.load()

delta = 5
#threshold = 80

for i in range(img_3.size[0] - delta):
    for j in range(img_3.size[1] - delta):
        w1 = 0
        w2 = 0
        for k in range(1,delta,1):
            lum_value_1 = (pixelMap[i,j-k][0])/3 + (pixelMap[i,j-k][1])/3 + (pixelMap[i,j-k][2])/3
            w1 += lum_value_1/delta
            lum_value_2 = (pixelMap[i,j+k][0])/3 + (pixelMap[i,j+k][1])/3 + (pixelMap[i,j+k][2])/3
            w2 += lum_value_2/delta
        lum_value = 2*abs(w1-w2)
        pixelsNew_3[i,j] = (lum_value,lum_value,lum_value)








#################### HISTOGRAMA DE LUMINANCIA ########################

import numpy

hist_array_size = im.size[0]*im.size[1]
hist_array = numpy.zeros(shape=(hist_array_size, 1))

q = 0

for i in range(im.size[0]):
    for j in range(im.size[1]):
        for k in range(1,delta,1):
            lum_value_1 = (pixelMap[i,j-k][0])/3 + (pixelMap[i,j-k][1])/3 + (pixelMap[i,j-k][2])/3
            w1 += lum_value_1/delta
            try:
                lum_value_2 = (pixelMap[i,j+k][0])/3 + (pixelMap[i,j+k][1])/3 + (pixelMap[i,j+k][2])/3
            except:
                q = q + 1
                print 'canoa' + q
            w2 += lum_value_2/delta
        lum_value = 2*abs(w1-w2)
        pixelsNew_3[i,j] = (lum_value,lum_value,lum_value)



import matplotlib.pyplot as plt
# matplotlib inline
plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

# Plot Histogram on x
x = np.random.normal(size = 1000)
plt.hist(x, bins=50)
plt.gca().set(title='Frequency Histogram', ylabel='Frequency')



im.show()
im.close()

img.show()
img.save( img_name + "_out" + img_format)
img.close()

img_2.show()
img_2.save( img_name + "_out_borders" + img_format)
img_2.close()

img_3.show()
img_3.save( img_name + "_out_relieve" + img_format)
img_3.close()