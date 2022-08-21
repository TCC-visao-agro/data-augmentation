import cv2
import numpy as np

imgFront = cv2.imread("img.jpg")
imgBack = cv2.imread("./bgs/bg3.jpg")

height, width = imgFront.shape[:2]

resizeBack = cv2.resize(imgBack, (width, height), interpolation=cv2.INTER_CUBIC)

removedPixels = 0

for i in range(width):
    for j in range(height):
        pixel = imgFront[j, i]
        if np.allclose(pixel, [0, 0, 0], rtol=20, atol=20):
            imgFront[j, i] = resizeBack[j, i]
            removedPixels += 1

cv2.imwrite("test.png", imgFront)
print(removedPixels)

