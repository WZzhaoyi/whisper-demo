

import os
import math
import webvtt
import datetime
import re
from faster_whisper import WhisperModel
from strtool import merge

def seconds_to_hms(seconds_num):
    """
    输入秒数 转换为 时分秒输出
    param: seconds_num float
    return: hms str 00:00:000
    """
    xs,zs=math.modf(seconds_num)
    m, s = divmod(zs, 60)
    h, m = divmod(m, 60)
    xs_str = "%.03f" % xs
    hms = "%02d:%02d:%02d.%s" % (h, m, s, xs_str.split('.')[1][:3])
    return hms

def remove_repeated_words(s):
    s = merge(s, 15)
    return s

def transcribe_audio(audio_path, output_path=None, model="arc-r/faster-whisper-large-v2-mix-jp", device="cuda", compute_type="float16", beam_size=5, vad_filter=True):
    model = WhisperModel(model, device=device, compute_type=compute_type)
    segments, info = model.transcribe(audio_path, beam_size=beam_size, vad_filter=vad_filter)# , vad_parameters=dict(min_silence_duration_ms=1000))
    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    vtt = webvtt.WebVTT()
    for segment in segments:
        start = segment.start
        end = segment.end
        text = segment.text
        if start != end:
            start_str = seconds_to_hms(start)
            end_str = seconds_to_hms(end)
            text_str = remove_repeated_words(text)
            vtt_cue = webvtt.Caption(start=start_str, end=end_str, text=text_str)
            vtt.captions.append(vtt_cue)
            print("[%ss -> %ss] %s" % (start_str, end_str, text_str))
    
    str_content = str(vtt.content)

    if output_path is not None:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(vtt.content)
    
    return str_content
    


if __name__ == "__main__":
    transcribe_audio(r"C:\Users\wzzha\Downloads\115download\[Thz.la]yrmn-040(0-60).mp3", r"C:\Users\wzzha\Downloads\115download\[Thz.la]yrmn-040(0-60).mp3.vtt")