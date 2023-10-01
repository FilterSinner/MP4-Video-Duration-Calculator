import os
from moviepy.editor import VideoFileClip

# Function to calculate the duration of MP4 videos in a folder
def calculate_total_duration(folder_path):
    total_duration= 0

    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):
            video_path = os.path.join(folder_path, filename) #used to construct the full path to each individual video file within the folder
            try:
                clip = VideoFileClip(video_path)
                total_duration += clip.duration
                clip.close()
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return total_duration


folder_path = r"your\path\to\folder"

total_duration = calculate_total_duration(folder_path)

total_duration_hours = int(total_duration / 3600)
total_duration_minutes = int((total_duration % 3600) / 60)
total_duration_seconds = int(total_duration % 60)


print(f"Total duration of MP4 videos in the folder: {total_duration_hours} hours, {total_duration_minutes} minutes, {total_duration_seconds} seconds :( )")
