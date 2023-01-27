from pytube import YouTube

#returns some basic information
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
