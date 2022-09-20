from rembg import remove
import cv2
import numpy as np

width, height = 224, 224
image = cv2.imread("image.jpg")
bg_resized = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)
output = remove(bg_resized)
output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
bool_image = output.astype(bool)

changed_background_image = np.full_like(bg_resized, [255, 255, 255])

changed_background_image[bool_image, :] = bg_resized[bool_image]

cv2.imwrite("output2.jpg", changed_background_image)


