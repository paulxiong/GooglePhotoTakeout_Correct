
# GooglePhotoTakeout_Correct

## Why I Wrote This Script

The GooglePhotoTakeout_Correct script is designed to address the issue of incorrect time tags in photos after migrating or transferring photos between different services. It provides a solution to fix the time tags of photos without modifying the original files, ensuring that the correct timestamps are associated with each image.

## Overview

I created this script when I was transitioning away from Google Photos. During the migration process, I noticed that some photos, especially older ones, had incorrect time tags after being moved to a new location like Immich. This inconsistency puzzled me, as the time tags were correct when viewed in Google Photos. I wanted to understand what was causing this issue and find a way to correct the wrong time tags without modifying the original photos.

## How It Works (For Developers)

The GooglePhotoTakeout_Correct script is built using Python and leverages various libraries to read and manipulate photo metadata. The script reads the metadata from the photos, including the creation date and time, and compares it with the expected timestamp from the Google Photos database. If a discrepancy is detected, the correct timestamp is extracted and applied to the photo's metadata. The script provides a user-friendly command-line interface, making it easy for developers to specify the source folder containing the photos and the desired destination folder for the corrected photos. The process runs quickly, and the corrected photos are saved in the destination folder without altering the original files.

## Usage

To use the GooglePhotoTakeout_Correct script, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/paulxiong/GooglePhotoTakeout_Correct.git
   ```

2. Navigate to the project folder:

   ```bash
   cd GooglePhotoTakeout_Correct
   ```

3. Install the required dependencies (ensure you have Python installed):

   ```bash
   pip install -r requirements.txt
   ```

4. Run the script with the appropriate arguments:

   ```bash
   python Main.py --output_folder /path/to/destination/folder
   ```

   Replace `/path/to/destination/folder` with the path to the folder where you want to save the corrected photos.

---

## Examples

### Example 1: Correct Time Tags for Photos in Current Directory

```bash
python Main.py --output_folder ./CorrectedPhotos
```

This command will process all JSON files in the current directory and correct the time tags of the associated photos. The corrected photos will be saved in the "CorrectedPhotos" folder within the current directory.

### Example 2: Correct Time Tags for Photos in Specific Year Folder

```bash
python Main.py /path/to/GooglePhotos/2019 --output_folder /path/to/Corrected2019
```

This command will process all JSON files in the "GooglePhotos/2019" folder, correct the time tags, and save the corrected photos in the "Corrected2019" folder.

### Example 3: Correct Time Tags for Photos in Multiple Folders

```bash
python Main.py /path/to/VacationPics /path/to/PartyPics --output_folder /path/to/CorrectedPhotos
```

This command will process all JSON files in the "VacationPics" and "PartyPics" folders, correct the time tags, and save the corrected photos in the "CorrectedPhotos" folder.

### Example 4: Correct Time Tags for Photos in Subfolders Recursively

```bash
python Main.py /path/to/Photos --output_folder /path/to/CorrectedPhotos --recursive
```

This command will process all JSON files in the "Photos" folder and its subfolders recursively, correct the time tags, and save the corrected photos in the "CorrectedPhotos" folder.

### Example 5: Correct Time Tags and Skip Videos

```bash
python Main.py /path/to/AllMedia --output_folder /path/to/CorrectedMedia --skipped_folder /path/to/SkippedMedia --recursive
```

This command will process all JSON files in the "AllMedia" folder and its subfolders recursively, correct the time tags for photos, and skip videos. The corrected photos will be saved in the "CorrectedMedia" folder, and any skipped videos will be copied to the "SkippedMedia" folder for further examination.

### Example 6: Correct Time Tags and Provide Custom Skipped Folder

```bash
python Main.py /path/to/Photos --output_folder /path/to/CorrectedPhotos --skipped_folder /path/to/MySkippedPhotos --recursive
```

This command will process all JSON files in the "Photos" folder and its subfolders recursively, correct the time tags, and save the corrected photos in the "CorrectedPhotos" folder. If any photos are skipped during the process, they will be copied to the custom "MySkippedPhotos" folder for further inspection.

### Example 7: Correct Time Tags for Photos in Google Takeout Subfolders

```bash
python Main.py /path/to/GoogleTakeout/Takeout\ 2022/Google\ Photos --output_folder /path/to/CorrectedPhotos --recursive
```

This command will process all JSON files in the "GoogleTakeout/Takeout 2022/Google Photos" folder and its subfolders recursively, correct the time tags, and save the corrected photos in the "CorrectedPhotos" folder.

---

Feel free to adjust the paths and folder names in the examples to match your specific directory structure and naming conventions. These examples cover various scenarios, including processing photos in specific folders, handling subdirectories recursively, skipping videos, and providing custom folders for skipped images.

