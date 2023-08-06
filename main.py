import os
import pillow_heif
from PIL import Image

def heic_to_jpg(heic_path, jpg_path):
    # Open the .heic file using pyheif
    heif_file = pillow_heif.read_heif(heic_path)
    
    # Convert the .heic image data to a Pillow image object
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    
    # Save the Pillow image object as .jpg
    image.save(jpg_path, "JPEG")

def batch_convert_heic_to_jpg(directory_path):
    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.lower().endswith(".heic"):
                heic_file_path = os.path.join(root, filename)
                jpg_file_path = os.path.join(root, os.path.splitext(filename)[0] + ".jpg")
                heic_to_jpg(heic_file_path, jpg_file_path)
                os.remove(heic_file_path)

# Example usage
directory_path = "/Users/joshuagao/Library/Mobile Documents/iCloud~md~obsidian/Documents/Donna/Notion"
batch_convert_heic_to_jpg(directory_path)
