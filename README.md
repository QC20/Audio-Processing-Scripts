# Audio Processing Scripts

This GitHub repository contains two Python scripts that utilize the `pydub` library for processing MP3 audio files.

## Script 1: MP3 Compression
The first script, `compress_mp3.py`, allows you to compress an MP3 audio file to reduce its file size. This can be useful when you need to save storage space or optimize your audio files for web or other purposes.

### Requirements
To run the script, ensure you have the following installed:

- Python
- `pydub` library

You can install the `pydub` library using the following command:

```bash
pip install pydub

### Usage
- Edit the script and set the input_file, output_file, and bitrate variables to match your desired configurations.
- Execute the script to compress the MP3 file:
- python compress_mp3.py

## Script 2: MP3 File Merge
The second script, merge_mp3_files.py, allows you to merge multiple MP3 audio files into one. This can be handy when you have several audio segments that need to be combined into a single cohesive file.

### Requirements
To run the script, ensure you have Python installed.

### Usage
- Edit the script and set the folder_path and output_file variables to specify the folder containing the MP3 files to merge and the desired output file path, respectively.
- Execute the script to merge the MP3 files:
- vpython merge_mp3_files.py


Please note that the order of merging will follow the alphabetical order of filenames in the specified folder.

Note: Make sure to install the required libraries using the provided instructions before running the scripts.

Feel free to explore, modify, and use these scripts to suit your specific needs. For any issues or questions, please create an issue in this repository.

Enjoy processing your MP3 audio files with ease! 🎶
