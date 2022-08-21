from skimage import transform, io, img_as_ubyte
from random import randint

import os

original_images_path = "./images"
rotated_images_path = "./rotated_images"

classes = os.listdir(original_images_path)

for leaf_class in classes:
    leaves = os.listdir(f"{original_images_path}/{leaf_class}")

    for leaf in leaves:
        leaf_original_path = f"{original_images_path}/{leaf_class}/{leaf}"

        tomato_leaf = io.imread(leaf_original_path)

        angle = randint(-180, 180)

        rotated_leaf = transform.rotate(tomato_leaf, angle=angle, cval=0)

        new_file_name = os.path.basename(leaf_original_path).replace(".jpg", "") + f"_rotated_{angle}"

        if not os.path.exists(f"{rotated_images_path}/{leaf_class}"):
            os.makedirs(f"{rotated_images_path}/{leaf_class}")

        io.imsave(f"{rotated_images_path}/{leaf_class}/{leaf}", img_as_ubyte(tomato_leaf))
        io.imsave(f"{rotated_images_path}/{leaf_class}/{new_file_name}.jpg", img_as_ubyte(rotated_leaf))


