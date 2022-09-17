from rembg import remove
from cv2 import resize, INTER_CUBIC
import cv2

width, height = 224, 224
image = cv2.imread("image.jpg")
bg_resized = resize(image, (width, height), interpolation=INTER_CUBIC)
output = remove(bg_resized)

cv2.imshow("output", output)
cv2.waitKey(0)


