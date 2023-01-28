import Logic.Queries.BasicQuery
import Logic.Download
import os
from pathlib import Path
import asyncio
import inquirer

ytQuery = Logic.Queries.BasicQuery
ytDownload = Logic.Download
#userYTPath = ytQuery.basicQuery()

def file_select():
    questions = [inquirer.List('media_type', message="What media type do you need?",
                                choices=["MP3", "MP4"])]
    response = inquirer.prompt(questions)
    response = response.get('media_type')
    return response

def download_audio_setup():
    userYoutubeLinkInput = input("Please enter the URL to your video: ")
    new_video_name = input("Please enter a video name: ")
    output_video_name = f'{new_video_name}.mp4'
    success_name = new_video_name
    ytDownload.get_user_audio(userYoutubeLinkInput, output_video_name, success_name)

def download_video_setup():
    user_youtube_link = input("Please enter the URL to your video: ")
    new_video_name = input("Please enter a name: ")
    output_video_name = f'{new_video_name}.mp4'
    success_name = new_video_name
    ytDownload.get_user_video(user_youtube_link, output_video_name, success_name)


# to hold the switch statement
def user_selection_logic(prompt_response):
    if prompt_response == "MP3":
        download_audio_setup()
    elif prompt_response == "MP4":
        download_video_setup()

if __name__ == "__main__":
    prompt = file_select()
    user_selection_logic(prompt_response=prompt)
        
# userYoutubeLinkInput = input("Please enter the URL to your video: ")
# # getUserStream = ytQuery.findStream(userYTPath)
# newVideoName = input("Please enter a name for the downloaded file: ")
# #downloadVideo = ytDownload.downloadAudio(userYTPath, newVideoName)
# download_video_name = f'download_{newVideoName}.mp4'
# output_video_name = f'{newVideoName}.mp4'
# success_name = newVideoName
# #mp4Input = ytDownload.downloadAudio(userYTPath, newVideoName)
# #ytDownload.convertAudio(download_video_name, output_video_name)
# ytDownload.get_user_audio(userYoutubeLinkInput, output_video_name, success_name
