from pytube import YouTube
from pathlib import Path
import os

DOWNLOAD_AUDIO_PATH = os.path.dirname('./DATA')
def downloadAudio(YouTubeObj, name):
    print('Downloading...')
    userPath = Path('Download.py').parent.resolve()
    userPath = str(userPath) + "\\DATA\\Audio"
    out_stream = YouTubeObj.streams.filter(progressive=True, file_extension='mp4').first()
    outPutFile = out_stream.download(output_path=userPath, filename=name)
    outPutFileText = Path(outPutFile)
    #splits the text from the old extension to the new
    base = os.path.splitext(outPutFileText)[0] + ".mp3"
    os.rename(outPutFileText, base)
    
    