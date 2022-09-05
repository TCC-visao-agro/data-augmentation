from random import randint
from cv2 import imread, imwrite

import os
import uuid


class FileManagement:

    def __init__(self):
        self.leaf_class = ""
        self.leaf = ""
        self.bgs_path = "./bgs"
        self.original_images_path = "./images"
        self.rotated_images_path = "./rotated_images"

    def get_classes(self):
        return os.listdir(self.original_images_path)

    def get_leaves(self, leaf_class):
        self.leaf_class = leaf_class
        return os.listdir(f"{self.original_images_path}/{self.leaf_class}")

    def get_leaf(self, leaf):
        self.leaf = leaf
        return imread(f"{self.original_images_path}/{self.leaf_class}/{self.leaf}")

    def get_random_bg(self):
        bgs = os.listdir(self.bgs_path)
        return imread(f"{self.bgs_path}/{randint(1, len(bgs))}.jpg")

    def save(self, image):
        leaf_label = uuid.uuid4()

        original_leaf_name = os.path.basename(self.leaf).split("___")[1]

        filename = f"{leaf_label}__{original_leaf_name}"

        self.__check_if_directory_not_exists()

        imwrite(filename=f"{self.rotated_images_path}/{self.leaf_class}/{filename}", img=image)

    def __check_if_directory_not_exists(self):
        if not os.path.exists(f"{self.rotated_images_path}/{self.leaf_class}"):
            os.makedirs(f"{self.rotated_images_path}/{self.leaf_class}")
