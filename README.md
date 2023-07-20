# Audio Processing Scripts

This repository contains two Python scripts for audio processing using the `pydub` library. The first script, `merge_mp3_files.py`, merges multiple MP3 files into a single file, while the second script, `compress_mp3.py`, compresses an MP3 file by adjusting its bitrate.

## Merge MP3 Files

### Script Description

The `merge_mp3_files.py` script allows you to merge multiple MP3 files located in a specified folder into a single MP3 file.

### Dependencies

This script requires the following dependencies:
- `pydub`
- `os`

Make sure to install these dependencies before running the script. You can use `pip` to install them:
pip install pydub


### Usage

To use the script, follow these steps:

1. Open the script file `merge_mp3_files.py` in a text editor or an integrated development environment (IDE).
2. Set the `folder_path` variable to the path of the folder containing the MP3 files you want to merge.
3. Set the `output_file` variable to the desired path and filename for the merged MP3 file.
4. Save the script file.
5. Run the script using Python:
python merge_mp3_files.py

