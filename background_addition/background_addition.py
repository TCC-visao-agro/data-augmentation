import cv2
from gamma_correction.gamma_correction import gamma_correction

import numpy as np
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
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, threshold_image = cv2.threshold(gray_image, 20, 255, cv2.THRESH_BINARY)

    gray = cv2.morphologyEx(threshold_image, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))

    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    large_contours = []
    for contour in contours:
        if cv2.contourArea(contour) > 10000:
            large_contours.append(contour)

    gray = np.uint8(np.zeros(gray.shape))
    segmented_leaf = cv2.drawContours(gray, large_contours, -1, 255, cv2.FILLED)

    return segmented_leaf.astype(bool)
