import os
import logging
import ffmpeg

# ffmpeg run by ffmpeg-python
def ffmpeg_convert_audio(video_path: str, audio_path: str):
    video_path = os.path.abspath(video_path)
    input_video = ffmpeg.input(video_path)
    audio = input_video.audio

    output_audio = ffmpeg.output(audio, audio_path).run()

    return output_audio

def ffmpeg_split(input_file, start_time, end_time, output_file):
    """
    Splits a video file into a segment starting at start_time and ending at end_time.
    """
    # Use FFmpeg to extract the segment from the input file
    output = ffmpeg.input(input_file, ss=start_time, t=end_time-start_time).output(output_file).run()
    return output

if __name__ == "__main__":
    # ffmpeg_convert_audio(r"C:\Users\wzzha\Downloads\115download\[Thz.la]yrmn-040.mp4", r"C:\Users\wzzha\Downloads\115download\[Thz.la]yrmn-040.mp3")
    ffmpeg_split(r"C:\Users\wzzha\Downloads\115download\[Thz.la]yrmn-040.cmd.mp3", 0, 60, r"C:\Users\wzzha\Downloads\115download\[Thz.la]yrmn-040(0-60).mp3")