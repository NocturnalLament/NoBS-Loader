import asyncio
from pytube import YouTube
from pathlib import Path
import os
import subprocess

# So I remember this
# SWAP_FORMAT_STRING = "ffmpeg -i example_initial_file.mp4 -vn -ar 44100 -ac 2 -b:a 129k output_file.mp3"
ADDITIONAL_PATH = "\\DATA\\Audio"

DOWNLOAD_AUDIO_PATH = os.path.dirname('./DATA')
def downloadAudio(YouTubeObj, name):
    print('Downloading...')
    userPath = Path('Download.py').parent.resolve()
    userPath = str(userPath) + ADDITIONAL_PATH
    download_name = "download_" + name + '.mp4'
    out_stream = YouTubeObj.streams.filter(progressive=True, file_extension='mp4').first().download(output_path=userPath, filename=download_name)
    fileString = name + '.mp3'
    out_path = str(Path(out_stream))
    return out_path

def convertAudio(in_name, out_name):
    print("Converting your audio")
    path = str(Path(f'{in_name}.mp4').parent.resolve()) + ADDITIONAL_PATH
    command = f'ffmpeg -i {in_name} -vn {out_name}'
    os.system(f'cd {path} && {command}')
  
    
