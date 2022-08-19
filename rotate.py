from skimage import transform, io, img_as_ubyte
import os
from glob import glob
import numpy as np

def nameImage(dir):

    qCarac = -len(dir)-1
    name_image = ""
    i = 0

    for x in range(-1, qCarac, -1):
        if dir[x] == "\\":
            break
        i = i + 1
    return dir[(len(dir) - i): -4]




angle_rotate = [-50, 60]


img_original = glob(os.path.join(os.getcwd() + "\\data-augmentation\\images\\",'*.jpg'))
img_rotate_save = os.getcwd() + "\\data-augmentation\\images_rotate\\"
i=0

for fn in img_original:

    print("FN: " + fn)
    name_img = nameImage(fn)

    tomatoLeafRotate = io.imread(fn)

    for x in angle_rotate:
        rotatedLeaf = transform.rotate(tomatoLeafRotate, angle=x, cval=0)


        io.imsave(img_rotate_save + name_img + "_" + str(x) + ".jpg" , img_as_ubyte(rotatedLeaf))





