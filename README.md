# Photo Time Tag Corrector

## Why I Wrote This App

The Photo Time Tag Corrector is a tool designed to address the issue of incorrect time tags in photos after migration or transfer between photo storage services. It offers a solution to fix the time tags of photos without modifying the original files, ensuring that the correct timestamp is associated with each image.

## Overview

I created this app because I was transitioning away from Google Photos, and during the migration, I noticed that some photos, especially older ones, had incorrect time tags after being moved to a new location like Immich. This inconsistency puzzled me, as the time tags were correct when viewed in Google Photos. I wanted to understand what was causing this issue and find a way to correct the wrong time tags without modifying the original photos.

## How It Works (For Developers)

The Photo Time Tag Corrector is built using Python and leverages various libraries to read and manipulate photo metadata. The app reads the metadata from the photos, including the creation date and time, and compares it with the expected timestamp from the Google Photos database. If a discrepancy is detected, the correct timestamp is extracted and applied to the photo's metadata.\n\nThe app provides a user-friendly command-line interface, making it easy for developers to specify the source folder containing the photos and the desired destination folder for the corrected photos. The process runs quickly, and the corrected photos are saved in the destination folder without altering the original files.

## Usage

To use the Photo Time Tag Corrector, follow these steps:\n\n1. Clone the repository to your local machine:\n   ```\n   git clone https://github.com/yourusername/photo-time-tag-corrector.git\n   ```\n\n2. Navigate to the project folder:\n   ```\n   cd photo-time-tag-corrector\n   ```\n\n3. Install the required dependencies (ensure you have Python installed):\n   ```\n   pip install -r requirements.txt\n   ```\n\n4. Run the application with the appropriate arguments:\n   ```\n   python photo_time_tag_corrector.py --source /path/to/source/folder --destination /path/to/destination/folder\n   ```\n\n   Replace '/path/to/source/folder' with the path to the folder containing the photos that need correction, and '/path/to/destination/folder' with the desired location for the corrected photos.

## Examples

### Example 1: Correct Time Tags for Photos in "OldPhotos" Folder\n\n```\npython photo_time_tag_corrector.py --source /path/to/OldPhotos --destination /path/to/CorrectedPhotos\n```\n\nThis command will process all photos in the "OldPhotos" folder and save the corrected photos in the "CorrectedPhotos" folder.\n\n### Example 2: Correct Time Tags for Photos in "VacationPics" Folder\n\n```\npython photo_time_tag_corrector.py --source /path/to/VacationPics --destination /path/to/VacationPics/Corrected\n```\n\nThis command will process all photos in the "VacationPics" folder and save the corrected photos in a new subfolder named "Corrected" within the "VacationPics" folder.

---

Feel free to customize and expand the README.md file further to include additional details, such as contributing guidelines, license information, and any other relevant information about the Photo Time Tag Corrector app.
