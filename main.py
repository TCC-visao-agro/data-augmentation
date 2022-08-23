from transform.transform import *
from background_addition.background_addition import background_addition
from os.file_management import FileManagement


def main():
    file_management = FileManagement()

    classes = file_management.get_classes()

    for leaf_class in classes:
        leaves = file_management.get_leaves(leaf_class)

        for leaf in leaves:
            tomato_leaf = file_management.get_leaf(leaf)

            first_background = file_management.get_random_bg()
            second_background = file_management.get_random_bg()

            first_background_flipped = flip(first_background)
            second_background_flipped = flip(second_background)

            rotated_image = rotate(tomato_leaf)

            first_image_mounted = background_addition(foreground_image=tomato_leaf,
                                                      background_image=first_background_flipped)

            second_image_mounted = background_addition(foreground_image=rotated_image,
                                                       background_image=second_background_flipped)

            file_management.save(first_image_mounted)
            file_management.save(second_image_mounted)


if __name__ == "__main__":
    main()
