
from moviepy.editor import AudioFileClip, ImageClip


audio_clip = AudioFileClip("interest.mp3")
image_clip = ImageClip("sir.png", duration=audio_clip.duration)


image_clip = image_clip.set_audio(audio_clip)

image_clip.write_videofile("output_video.mp4", fps=30)
