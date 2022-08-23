from transform.transform import *
from background_addition.background_addition import background_addition
from files_operation.FileManagement import FileManagement

TIMES_TO_AUGMENT = 5


def main():
    file_management = FileManagement()

    classes = file_management.get_classes()

    new_leaves = 0

    print("Augmenting...\n")

    for leaf_class in classes:
        leaves = file_management.get_leaves(leaf_class)

        for leaf in leaves:

            for _ in range(TIMES_TO_AUGMENT):

                tomato_leaf = file_management.get_leaf(leaf)

                background = file_management.get_random_bg()

                background_flipped = flip(background)

                rotated_image = rotate(tomato_leaf)

                image_mounted = background_addition(foreground_image=rotated_image,
                                                    background_image=background_flipped)

                file_management.save(image_mounted)
                new_leaves += 1

    print(f"Finished data augmentation. Leaves={new_leaves}")


if __name__ == "__main__":
    main()
