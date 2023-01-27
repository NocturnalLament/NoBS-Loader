import Logic.Queries.BasicQuery
import Logic.Download
import os
from pathlib import Path


ytQuery = Logic.Queries.BasicQuery
ytDownload = Logic.Download
userYTPath = ytQuery.basicQuery()
# getUserStream = ytQuery.findStream(userYTPath)
newVideoName = input("Please enter a name for the downloaded file: ")
downloadVideo = ytDownload.downloadAudio(userYTPath, newVideoName)
