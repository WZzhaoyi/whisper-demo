import time
import os
from datetime import datetime
from faster_whisper import WhisperModel
from audio import ffmpeg_convert_audio
from transcribe import transcribe_audio, seconds_to_hms
from strtool import replace_last_occurrence

if __name__ == "__main__":

    file_list = [r"C:\Users\wzzha\Downloads\115download\YRMN-020.mp4", r"C:\Users\wzzha\Downloads\115download\CEMD-341.mp4", r"C:\Users\wzzha\Downloads\115download\SDMU-074.mp4"]


    for f in file_list:
        start = time.time()
        print(f"Start to transcribe: {f}, {datetime.now()}")

        file_extension = os.path.splitext(f)[1]
        a = replace_last_occurrence(f, file_extension, '.mp3')
        v = replace_last_occurrence(f, file_extension, '.vtt')

        ffmpeg_convert_audio(f, a)
        transcribe_audio(a, v, compute_type="int8_float16")
        end = time.time()
        print(f"Time taken to transcribe: {seconds_to_hms(end - start)}s")
