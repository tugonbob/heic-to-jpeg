import os
import argparse
import pillow_heif
from PIL import Image


def is_heic_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == '.heic'


def heic_to_jpeg(heic_path):
    # Open the .heic file using pyheif
    heif_file = pillow_heif.read_heif(heic_path)

    # Convert the .heic image data to a Pillow image object
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        bytes(heif_file.data),  # <-- Convert memoryview to bytes here
        "raw",
        heif_file.mode,
        heif_file.stride,
    )

    # Create save path
    path_without_extension, _ = os.path.splitext(heic_path)
    jpeg_path = path_without_extension + '.jpeg'

    # Save the Pillow image object as .jpeg
    image.save(jpeg_path, "JPEG")


def recursively_convert_dir_heic_to_jpeg(dir_path, replace):
    for root, _, files in os.walk(dir_path):
        for file in files:
            if not is_heic_file(file):
                continue

            heic_path = os.path.join(root, file)
            heic_to_jpeg(heic_path)

            if replace:
                os.remove(heic_path)

            print(f"Converted {heic_path}")


def convert_dir_heic_to_jpeg(dir_path, replace):
    for file in os.listdir(dir_path):
        if not is_heic_file(file):
            continue

        heic_path = os.path.join(dir_path, file)
        heic_to_jpeg(heic_path)

        if replace:
            os.remove(heic_path)

        print(f"Converted {heic_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A script that recursively searches through a directory for heic files and converts them into jpeg files.')
    parser.add_argument('--path', type=str, required=True,
                        help='The directory that you would like to convert heic to jpeg files to.')
    parser.add_argument('--replace', action='store_true',
                        help='Include this flag if you would like to delete the original heic file.')
    parser.add_argument('--recursive', '-r', action='store_true',
                        help='Include this flag if you would like to recursively search through dir for heic files to convert.')
    args = parser.parse_args()

    if args.recursive:
        print(f"Starting conversion in {args.path} directory and its subdirectories")
        recursively_convert_dir_heic_to_jpeg(args.path, args.replace)
    else:
        print(f"Starting conversion in {args.path} directory")
        convert_dir_heic_to_jpeg(args.path, args.replace)

    print("Conversion complete")