from skimage import transform, io, img_as_ubyte

import numpy as np

tomatoLeaf = io.imread('./images/Tomato___Bacterial_spot/0a6d40e4-75d6-4659-8bc1-22f47cdb2ca8___GCREC_Bact.Sp 6247_final_masked.jpg')

rotatedLeaf = transform.rotate(tomatoLeaf, angle=-50, cval=0)

io.imsave("./rotated_images/rotated.jpg", img_as_ubyte(rotatedLeaf))
