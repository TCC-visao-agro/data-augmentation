from transform.transform import *
from background_addition.background_addition import add_background_image, add_background_color
from files_operation.FileManagement import FileManagement
from alive_progress import alive_bar

NUMBER_OF_SAMPLES = 5000
BACKGROUND_TYPE = "COLOR"  # IMAGE | COLOR
COLOR = [255, 255, 255]  # Conta apenas se o tipo for "COLOR"


def main():
    file_management = FileManagement()

    classes = file_management.get_classes()

    total_leaves = 0

    print("Augmenting...\n")

    number_of_replied_samples = 0

    for leaf_class in classes:
        leaves = file_management.get_leaves(leaf_class)

        with alive_bar(NUMBER_OF_SAMPLES, force_tty=True, title=leaf_class) as bar:
            while number_of_replied_samples < NUMBER_OF_SAMPLES:
                for leaf in leaves:
                    if number_of_replied_samples == NUMBER_OF_SAMPLES:
                        continue

                    bar.text = f"{leaf_class}"

                    tomato_leaf = file_management.get_leaf(leaf)

                    rotated_image = rotate(tomato_leaf)

                    image_mounted = None

                    if BACKGROUND_TYPE == "COLOR":
                        flipped_image = flip(rotated_image)
                        image_mounted = add_background_color(foreground_image=flipped_image, color=COLOR)

                    elif BACKGROUND_TYPE == "IMAGE":
                        background = file_management.get_random_bg()

                        flipped_background = flip(background)

                        image_mounted = add_background_image(foreground_image=rotated_image,
                                                             background_image=flipped_background)

                    file_management.save(image_mounted)
                    bar()
                    total_leaves += 1
                    number_of_replied_samples += 1

        number_of_replied_samples = 0

    leaves = file_management.get_leaves("Tomato___Spider_mites Two-spotted_spider_mite")

    tomato_leaf = file_management.get_leaf("db594718-ad38-4d28-969c-c4bac1b5bbe1___Com.G_SpM_FL 8443_final_masked.jpg")

    image_mounted = add_background_color(foreground_image=tomato_leaf, color=COLOR)

    print(f"Finished data augmentation!. Total augmented = {total_leaves}")


if __name__ == "__main__":
    main()
