from gamma_correction.gamma_correction import gamma_correction

import numpy as np
from cv2 import resize, INTER_CUBIC


def background_addition(foreground_image, background_image):
    foreground_corrected = gamma_correction(foreground_image, gamma=0.6)
    background_corrected = gamma_correction(background_image, gamma=0.6)

    height, width = foreground_corrected.shape[:2]

    bg_resized = resize(background_corrected, (width, height), interpolation=INTER_CUBIC)

    for i in range(width):
        for j in range(height):
            pixel = foreground_corrected[j, i]
            if np.allclose(pixel, [0, 0, 0], rtol=10, atol=10):
                foreground_corrected[j, i] = bg_resized[j, i]

    return foreground_corrected
