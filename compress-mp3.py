from pydub import AudioSegment

def compress_mp3(input_file, output_file, bitrate='1k'):
    # Load the input MP3 file
    audio = AudioSegment.from_file(input_file, format="mp3")

    # Set the desired output bitrate
    audio.export(output_file, format="mp3", bitrate=bitrate)

    print(f"Compressed MP3 saved as {output_file}")

# Provide the input file path, output file path, and desired bitrate
input_file = "/path/to/your/input/file.mp3"
output_file = "/path/to/your/output/file.mp3"
bitrate = '1k'  # Adjust the bitrate as per your requirement   

# Call the function to compress the MP3 file
compress_mp3(input_file, output_file, bitrate)
