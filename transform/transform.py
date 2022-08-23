from skimage import transform
from random import randint
from numpy import fliplr, flipud


def rotate(image):
    random_angle = randint(-180, 180)

    return transform.rotate(image=image, angle=random_angle, cval=0), random_angle


def flip(image):
    random_value = randint(0, 2)

    if random_value == 0:
        return fliplr(image)
    if random_value == 1:
        return flipud(image)
    else:
        return image
