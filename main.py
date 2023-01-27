import Logic.Queries.BasicQuery
import Logic.Download
import os
from pathlib import Path
import asyncio

ytQuery = Logic.Queries.BasicQuery
ytDownload = Logic.Download
userYTPath = ytQuery.basicQuery()
# getUserStream = ytQuery.findStream(userYTPath)
newVideoName = input("Please enter a name for the downloaded file: ")
#downloadVideo = ytDownload.downloadAudio(userYTPath, newVideoName)
download_video_name = f'download_{newVideoName}.mp4'
output_video_name = f'{newVideoName}.mp4'
mp4Input = ytDownload.downloadAudio(userYTPath, newVideoName)
ytDownload.convertAudio(download_video_name, output_video_name)


