import os
import random
import shutil

def copy_random_images(src_dir,dest_dir, num_images=600):
    # Create the destination directory if it doesn't exist

    # Get the list of subdirectories (labels)
    label_dirs = [d for d in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, d))]
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # in the original beans db we have 3 types of beans, so we will take 1/3 of the number of images for each type
    num_to_copy = int(num_images / 3)
    for label in label_dirs:
        label_dir = os.path.join(src_dir, label)
        label_images = [f for f in os.listdir(label_dir) if os.path.isfile(os.path.join(label_dir, f))]
        selected_label_images = random.sample(label_images, min(num_to_copy, len(label_images)))
        label_dest_dir = os.path.join(dest_dir, label)
        if not os.path.exists(label_dest_dir):
            os.makedirs(label_dest_dir)
        for image in selected_label_images:
            shutil.copy(os.path.join(label_dir, image), os.path.join(label_dest_dir, image))


if __name__ == "__main__":
    src_dir = '/home/clap/Documents/miniproject_bioinformatic/project/dataset_beans/train'  # Replace with the path to your dataset
    dest_dir = '/home/clap/Documents/miniproject_bioinformatic/project/dataset_beans_split'
    for images_num in [150, 500, 750]:
        dest_dir_num = dest_dir + '/sample_' + str(images_num) + '/train'
        copy_random_images(src_dir,dest_dir_num, images_num)