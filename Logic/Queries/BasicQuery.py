from pytube import YouTube
from Logic import DownloadFile
#returns some basic information
download_classes = DownloadFile
def basicQuery():
    userYoutubeLinkInput = input("Please enter the URL to your video: ")
    userYoutubeLink = YouTube(userYoutubeLinkInput)
    return userYoutubeLink

#Query Results
def basicQueryResults(youtubeLink):
    print("Video title: ", youtubeLink.title)
    print("Number of views: ", youtubeLink.views)
    print("Length of video: ", youtubeLink.length, "seconds")
    print("Video Description: ", youtubeLink.description)
    print("Rating: ", youtubeLink.rating)
    print('\n\n=======================================\n\n')

def add_data_to_db(url, name):
    video_data = YouTube(url)
    video_title = video_data.title
    video_download_name = name.replace(" ", "_")
    video_description = video_data.description
    video_url = url
    video_length = video_data.length
    vid = download_classes.DownloadFileClass(name=video_title, download_name=video_download_name, 
                                                    url=video_url, description=video_description, 
                                                        length=video_length)
    print(vid.download_name)
