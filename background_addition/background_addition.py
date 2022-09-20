from gamma_correction.gamma_correction import gamma_correction

import cv2
import numpy as np
from rembg import remove
from cv2 import resize, INTER_CUBIC


def add_background_image(foreground_image, background_image):
    foreground_corrected = gamma_correction(foreground_image, gamma=0.6)
    background_corrected = gamma_correction(background_image, gamma=0.6)

    height, width = foreground_corrected.shape[:2]

    bg_resized = resize(background_corrected, (width, height), interpolation=INTER_CUBIC)

    binary_image = find_binary_image(foreground_corrected)

    changed_background_image = bg_resized

    changed_background_image[binary_image, :] = foreground_corrected[binary_image]

    return changed_background_image


def add_background_color(foreground_image, color):
    foreground_corrected = gamma_correction(foreground_image, gamma=0.6)

    binary_image = find_binary_image(foreground_corrected)

    changed_background_image = np.full_like(foreground_corrected, color)

    changed_background_image[binary_image, :] = foreground_corrected[binary_image]

    return changed_background_image


def find_binary_image(image):
    segmented_image = remove(image)

    gray_image = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2GRAY)

    return gray_image.astype(bool)

#
# new_image = cv2.imread("image.jpg")
# output = add_background_color(new_image, [255, 255, 255])
#
# cv2.imwrite("output2.jpg", output)
