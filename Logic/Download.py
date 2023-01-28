from pytube import YouTube
from pathlib import Path
import os


# So I remember this
# SWAP_FORMAT_STRING = "ffmpeg -i example_initial_file.mp4 -vn -ar 44100 -ac 2 -b:a 129k output_file.mp3"
ADDITIONAL_PATH = "\\DATA"
DOWNLOAD_AUDIO_PATH = os.path.dirname('./DATA')
# def downloadAudio(YouTubeObj, name):
#     print('Downloading...')
#     userPath = Path('Download.py').parent.resolve()
#     userPath = str(userPath) + ADDITIONAL_PATH
#     download_name = "download_" + name + '.mp4'
#     out_stream = YouTubeObj.streams.filter(progressive=True, file_extension='mp4').first().download(output_path=userPath, filename=download_name)
#     fileString = name + '.mp3'
#     out_path = str(Path(out_stream))
#     return out_path

# def convertAudio(in_name, out_name):
#     print("Converting your audio")
#     path = str(Path(f'{in_name}.mp4').parent.resolve()) + ADDITIONAL_PATH
#     command = f'ffmpeg -i {in_name} -vn {out_name}'
#     os.system(f'cd {path} && {command}')
  
def get_user_audio(url, name, success):
    print("Downloading....")
    YouTube_Stream = YouTube(url)
    YouTube_Stream = YouTube_Stream.streams.filter(only_audio=True).first()
    file_name = name.replace(" ", "_")
    success_name = success.replace(" ", "_") + '.mp3'
    userPath = Path('Download.py').parent.resolve()
#     userPath = str(userPath) + ADDITIONAL_PATH
    path_string = str(userPath) + ADDITIONAL_PATH + '\\Audio'
    YouTube_File = YouTube_Stream.download(output_path=path_string, filename=file_name)
    base, ext = os.path.splitext(YouTube_File)
    new_file = base + '.mp3'
    os.rename(YouTube_File, new_file)
    print(f'Successfully downloaded {success_name}')

def get_user_video(url, name, success):
    print("Finding video...")
    YouTube_Stream = YouTube(url=url)
    YouTube_Stream = YouTube_Stream.streams.get_highest_resolution()
    file_name = name.replace(" ", "_")
    print("Downloading...")
    path_parent= Path('Download.py').parent.resolve()
    path_string = str(path_parent) + ADDITIONAL_PATH + '\\VIDEO'
    YouTube_Stream.download(output_path=path_string, filename=file_name)
    print(f'Successfully downloaded {success}')