from pydub import AudioSegment
import os

def merge_mp3_files(folder_path, output_file):
    # Initialize an empty AudioSegment object
    merged_audio = AudioSegment.empty()

    # Iterate over the files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            # Load the audio file
            audio = AudioSegment.from_mp3(os.path.join(folder_path, filename))

            # Append the audio to the merged_audio
            merged_audio += audio
            print(filename, "has been handled.")

    # Export the merged audio to a file
    merged_audio.export(output_file, format="mp3")
    print(f"Merged audio saved as {output_file}")

# Provide the folder path and output file name
folder_path = "/path/to/your/folder"
output_file = "/path/to/your/output/long.mp3"

# Call the function to merge the MP3 files
merge_mp3_files(folder_path, output_file)
