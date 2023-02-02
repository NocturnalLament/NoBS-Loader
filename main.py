import Logic.Queries.BasicQuery
import Logic.Download
import inquirer
from Logic import DBLogic
from Logic import Settings
import sqlite3
import os

database_path = 'DATA\\DB\\Test_Downloads.db'
#database_path = os.path.abspath(database_path)
ytQuery = Logic.Queries.BasicQuery
ytDownload = Logic.Download
db = DBLogic
#userYTPath = ytQuery.basicQuery()
def save_user_settings(settings_obj: Settings.User_Path):
    conn = sqlite3.connect(database=database_path)
    cur = conn.cursor()
    sqlite_string = '''
            INSERT INTO Settings(Name, Path, Description, AssociatedType)
            VALUES(?, ?, ?, ?)                
    '''
    cur.execute(sqlite_string, (settings_obj.PathName, settings_obj.Location, settings_obj.Description, settings_obj.FileType))
    conn.commit()
    return_to_main_menu = [inquirer.List(name='return', message='Settings saved! Would you like to return to the main menu?', choices=["Yes", "No"])]
    response = inquirer.prompt(questions=return_to_main_menu)
    response = response.get('return')
    if response == 'Yes':
        file_select()

def load_user_settings():
    conn = sqlite3.connect(database=database_path)
    cur = conn.cursor()
    sqlite_string = '''
        FROM Settings SELECT *
    '''
    results = cur.fetchall()
    return results

def user_settings():
    questions = [
        inquirer.Text(name='PathName', message='Please enter a name for your path'),
        inquirer.Text(name='PathLocation', message='Please enter the path'),
        inquirer.Text(name='PathDescription', message='Enter a description for this path'),
        inquirer.List(name='AssociatedTypes', message='What file types will be associated here?',
                                                                    choices=["MP3", "MP4", "Both MP3 and MP4"])
    ]

    responses = inquirer.prompt(questions=questions)
    settings_obj = Settings.User_Path
    settings_obj = settings_obj(
        PathName=responses.get('PathName'),
        Location=responses.get('PathLocation'),
        Description=responses.get('PathDescription'),
        FileType=responses.get('AssociatedTypes')
    )
    return settings_obj




def file_select():
    questions = [inquirer.List('media_type', message="What media type do you need?",
                                choices=["MP3", "MP4", "Downloads", "Settings"])]
    response = inquirer.prompt(questions)
    response = response.get('media_type')
    user_selection_logic(response)
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
    elif prompt_response == "Downloads":
        db = DBLogic.list_downloads()
        return None
    elif prompt_response == 'Settings':
        user_settings()



if __name__ == "__main__":
    file_select()
#    user = user_settings()
#    ins = save_user_settings(user)
    #  #to be reused in AudioFile instantiation.
    #  url_holder = url
    #  #ytQuery.add_data_to_db(name=name, url=url)
     
    #  #DBLogic.sqlite_conn('input', album_obj=url)
    #  DBLogic.sqlite_routine(url=url, conn_type='input', custom_name=name, input_type='mp3')
    #DBLogic.sqlite_conn()
        
# userYoutubeLinkInput = input("Please enter the URL to your video: ")
# # getUserStream = ytQuery.findStream(userYTPath)
# newVideoName = input("Please enter a name for the downloaded file: ")
# #downloadVideo = ytDownload.downloadAudio(userYTPath, newVideoName)
# download_video_name = f'download_{newVideoName}.mp4'
# output_video_name = f'{newVideoName}.mp4'
# success_name = newVideoName
# #mp4Input = ytDownload.downloadAudio(userYTPath, newVideoName)
# #ytDownload.convertAudio(download_video_name, output_video_name)
# ytDownload.get_user_audio(userYoutubeLinkInput, output_video_name, success_nam