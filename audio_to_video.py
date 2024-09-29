from moviepy.editor import AudioFileClip, ImageClip
import glob
import os
import shutil
import re  # Importing the re module for regular expressions

# Specify the folder containing the audio files and the folder for converted videos
audio_folder = r"input_folder_path"  # Replace with the path to your audio folder
output_folder = r"output_folder_path"  # Replace with the path to your output folder

# Ensure the output folder exists, if not, create it
os.makedirs(output_folder, exist_ok=True)

# Get all audio files in the folder (e.g., with .3gp extension)
audio_files = glob.glob(os.path.join(audio_folder, "*.3gp"))  # Adjust for other extensions if needed

counter = 1
# Static image file to use for all videos
image_file = "sir.png"

# Loop through each audio file and create a video for each
for audio_file in audio_files:
    # Replace spaces with underscores in the audio filename
    new_audio_file = audio_file.replace(" ", "_")
    if audio_file != new_audio_file:
        os.rename(audio_file, new_audio_file)
        audio_file = new_audio_file  # Update reference to renamed file

    # Load the audio and image files
    audio_clip = AudioFileClip(audio_file)
    image_clip = ImageClip(image_file, duration=audio_clip.duration)

    # Resize the image to match a standard video resolution (e.g., 720p)
    image_clip = image_clip.resize(width=1920, height=1080).set_position('center')

    # Set the audio to the image
    image_clip = image_clip.set_audio(audio_clip)

    # Define the output video filename based on the audio filename, removing any numbers before "Sir_Kamran"
    base_filename = os.path.splitext(os.path.basename(audio_file))[0]
    # Remove any leading numbers followed by an underscore or space
    base_filename = re.sub(r'\d+[\s_]*', '', base_filename)
    output_filename = f"{base_filename}_{counter}.mp4"

    output_filepath = os.path.join(audio_folder, output_filename)

    # Export the final video to the audio folder
    image_clip.write_videofile(output_filepath, codec="libx264", fps=30)

    # Move the converted file to the output folder
    moved_file_path = shutil.move(output_filepath, os.path.join(output_folder, output_filename))

    # Remove the original audio file
    os.remove(audio_file)

    # Print a message indicating the file has been processed along with the number of the file
    print(f"{counter} file(s) converted: {audio_file} to {moved_file_path}")

    counter += 1

print("Conversion complete! Files moved to output folder.")
