from moviepy import VideoFileClip, CompositeVideoClip
from gtts import gTTS
import os

def create_overlay_image(width, height, image_path):
    overlay = VideoFileClip(image_path)
    overlay = overlay.resize(width=width, height=height)
    return overlay

def create_text_to_speech(text, output_path):
    tts = gTTS(text=text, lang='en')
    tts.save(output_path)

def main(video_path, image_path, text, output_path):
    # Load video clip
    video_clip = VideoFileClip(video_path)

    # Set target aspect ratio to 9:16
    target_width = int(video_clip.size[0] * 9 / 16)
    target_height = video_clip.size[1]

    # Crop video to 9:16 ratio
    cropped_clip = video_clip.crop(x_center=(video_clip.size[0] - target_width) / 2,
                                   width=target_width,
                                   height=target_height)

    # Create overlay image
    overlay_image = create_overlay_image(target_width, target_height, image_path)

    # Set overlay position in the center
    overlay_position = (int((target_width - overlay_image.size[0]) / 2),
                        int((target_height - overlay_image.size[1]) / 2))

    # Overlay the image onto the cropped clip
    final_clip = CompositeVideoClip([cropped_clip, overlay_image.set_position(overlay_position).set_duration(cropped_clip.duration)])

    # Create text-to-speech audio
    tts_audio_path = "text_to_speech.mp3"
    create_text_to_speech(text, tts_audio_path)

    # Add text-to-speech audio to the final clip
    final_clip = final_clip.set_audio(VideoFileClip(tts_audio_path).audio)

    # Write the final video with overlay and text-to-speech
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Clean up temporary files
    os.remove(tts_audio_path)


    

def main():
    video_path = "input_video.mp4"
    image_path = "overlay_image.png"
    text = "Hello, this is the text to be spoken in the video."
    output_path = "output_video.mp4"

    main(video_path, image_path, text, output_path)


main()