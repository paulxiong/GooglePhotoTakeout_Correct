import os
import json
from PIL import Image, UnidentifiedImageError
from datetime import datetime
import piexif
import argparse
import shutil

def get_image_creation_time(image_path):
    with Image.open(image_path) as img:
        try:
            exif_data = img._getexif()
            if exif_data and 36867 in exif_data:
                return exif_data[36867]
        except (AttributeError, IndexError):
            # Handle GIF files without EXIF data using piexif
            pass
    return None

def is_image_file(file_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp', '.tiff', '.heic']
    _, ext = os.path.splitext(file_path)
    return ext.lower() in image_extensions    

def process_json_file(json_path, output_folder, skipped_folder=None):
    try:
        with open(json_path, encoding="utf-8-sig") as json_file:  # Explicitly specify encoding
        # with open(json_path) as json_file:
            data = json.load(json_file)
            title = data.get("title")
            photo_taken_time = data.get("photoTakenTime")

            if not title or not photo_taken_time:
                print(f"Skipped {json_path} due to missing 'title' or 'photoTakenTime'.")
                return

            photo_taken_timestamp = photo_taken_time.get("timestamp")
            if not photo_taken_timestamp:
                print(f"Skipped {json_path} due to missing 'timestamp' in 'photoTakenTime'.")
                return

            image_path = os.path.join(os.path.dirname(json_path), title)
            print(f"Constructed image path: {image_path}")  # Add this line for debugging
            if not os.path.exists(image_path):
                print(f"Skipped {json_path} because the image '{title}' doesn't exist.")
                return

            if not is_image_file(image_path):
                print(f"Skipped {json_path} because the file is not an image.")
                return

            image_creation_time = get_image_creation_time(image_path)
            if image_creation_time:
                print(f"Skipped {json_path} because EXIF data already exists.")
                if skipped_folder:
                    move_to_skipped_folder(title, skipped_folder)
            else:
                new_image_path = os.path.join(output_folder, title)
                new_image_path = get_unique_file_name(new_image_path)
                image = Image.open(image_path)

                # Convert the timestamp to datetime and then to bytes-like object
                photo_taken_datetime = datetime.utcfromtimestamp(int(photo_taken_timestamp)).strftime("%Y:%m:%d %H:%M:%S")
                exif_data = {"Exif": {36867: photo_taken_datetime}}
                exif_bytes = piexif.dump(exif_data)

                # Create a new image with the same data and save it with the modified EXIF
                new_image = Image.new(image.mode, image.size)
                new_image.putdata(list(image.getdata()))
                new_image.save(new_image_path, exif=exif_bytes, quality=100)
                print(f"Modified {title} and saved to {new_image_path}")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON file: {json_path}. Ignoring and continuing.")
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError in JSON file: {json_path}. Ignoring and continuing.")
    except UnidentifiedImageError as e:
        print(f"Cannot identify image file: {image_path}. Ignoring and continuing.")
def move_to_skipped_folder(title, skipped_folder):
    if not os.path.exists(skipped_folder):
        os.makedirs(skipped_folder)
    image_path = os.path.join(os.path.dirname(skipped_folder), title)
    new_image_path = get_unique_file_name(os.path.join(skipped_folder, title))
    shutil.copy(image_path, new_image_path)
    print(f"Skipped {title} and copied to {skipped_folder}")

def get_unique_file_name(file_path):
    name, ext = os.path.splitext(file_path)
    counter = 1
    while os.path.exists(file_path):
        file_path = f"{name}_{counter}{ext}"
        counter += 1
    return file_path

def process_json_files_in_folder(input_folder, output_folder, skipped_folder=None, recursive=False):
    json_files = []
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))

    for json_file in json_files:
        print(f"Processing file: {json_file}")
        process_json_file(json_file, output_folder, skipped_folder)

def main():
    parser = argparse.ArgumentParser(description="Process JSON files to modify image EXIF data. The source dir/files won't be changed/moved.\n"
                                                 "Examples:\n"
                                                 "1. Process JSON files in the current directory:\n"
                                                 "   python Main.py\n"
                                                 "2. Process JSON files in a specific folder:\n"
                                                 "   python Main.py /path/to/folder\n"
                                                 "3. Process JSON files recursively in the current directory:\n"
                                                 "   python Main.py -r\n"
                                                 "4. Specify a custom output folder for modified images:\n"
                                                 "   python Main.py -o custom_output_folder\n"
                                                 "5. Specify a custom skipped folder for copied skipped images:\n"
                                                 "   python Main.py -s custom_skipped_folder\n"
                                                 "6. Process JSON files recursively and use custom output and skipped folders:\n"
                                                 "   python Main.py -r -o custom_output_folder -s custom_skipped_folder")

    parser.add_argument("input_folder", nargs="?", default=".", help="Input folder where JSON files are located.")
    parser.add_argument("-o", "--output_folder", default="output", help="Output folder to save modified images.")
    parser.add_argument("-s", "--skipped_folder", help="Folder to copy skipped images.")
    parser.add_argument("-r", "--recursive", action="store_true", help="Search for JSON files recursively.")

    args = parser.parse_args()
    input_folder = args.input_folder
    output_folder = args.output_folder
    skipped_folder = args.skipped_folder
    recursive = args.recursive

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if skipped_folder:
        skipped_folder = os.path.join(os.path.abspath(skipped_folder), "")  # Ensure the trailing slash
        if not os.path.exists(skipped_folder):
            os.makedirs(skipped_folder)
    else:
        print("No 'skipped_folder' provided. Skipped images will not be copied.")

    if not recursive:
        print(f"Processing files in '{input_folder}'...")
        process_json_files_in_folder(input_folder, output_folder, skipped_folder)
    else:
        for root, _, files in os.walk(input_folder):
            print(f"Processing files in '{root}'...")
            process_json_files_in_folder(root, output_folder, skipped_folder)

if __name__ == "__main__":
    main()
