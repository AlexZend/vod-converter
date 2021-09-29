import os
import random
import shutil
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Split dataset into training and validation')
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument(
        '--input',
        dest='input_path',
        required=True,
        help=f'Path to full dataset'
    )
    required.add_argument(
        '--output',
        dest='output_path',
        required=True,
        help=f'Path to save validation data'
    )
    optional.add_argument(
        '--prop_val',
        dest='proportion_for_val',
        help="Proportion of objects for the validation sample of the total number of objects",
        required=False,
        type=float,
        default=0.2
    )
    args = parser.parse_args()
    return args


def move_file(source_path, destination_path):
    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
    else:
        raise FileNotFoundError("File %s not found" % source_path)


if __name__ == '__main__':
    args = parse_args()
    input_labels_path = args.input_path + "/Annotations/"
    input_images_path = args.input_path + "/JPEGImages/"
    output_labels_path = args.output_path + "/Annotations/"
    output_images_path = args.output_path + "/JPEGImages/"
    proportion_for_val = args.proportion_for_val

    os.makedirs(output_labels_path, exist_ok=True)
    os.makedirs(output_images_path, exist_ok=True)

    labels_files_list = os.listdir(path=input_labels_path)
    count_items_from_val = int(len(labels_files_list) * proportion_for_val)
    random_labels_list = random.sample(labels_files_list, count_items_from_val)

    for random_label in random_labels_list:
        random_image = random_label.split(".")[0] + ".png"
        move_file(input_labels_path + random_label, output_labels_path)
        move_file(input_images_path + random_image, output_images_path)
