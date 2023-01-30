import sqlite3
from pathlib import Path
from pytube import YouTube
from Logic import DownloadFile
DB_PATH = 'DATA//DB//Test_Downloads.db'
TABLE_QUERY_OPEN_ALL = 'SELECT * FROM Downloads'



# def sqlite_conn():
#     db = sqlite3.connect(DB_PATH)
#     cur = db.cursor()
#     cur = cur.execute(TABLE_QUERY_OPEN_ALL)
#     for row in cur:
#         print(row)

#I know that i could have used null, but I chose to initialize it with a string.
#Gotta keep this fun somehow so I don't get distracted, like by writing arbitrarily long
#comments.
sqlite_string = 'Rammstein is really cool.'

def sqlite_conn_router(conn_type):
    if conn_type == 'input':           #Set the input so the compiler doesn't scream.
        sqlite_string = '''
            INSERT INTO Downloads(CustomName, OriginalName, Url, Description, Type, Length)
            VALUES(?, ?, ?, ?, ?, ?)
        ''' 
        return sqlite_string
    elif conn_type == 'read':
        sqlite_string = 'SELECT * FROM Downloads'               #We don't need that to happen... Again.
        return sqlite_string

def sqlite_routine(url, conn_type, custom_name, input_type):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    song_data = YouTube(url=url)
    usr_sqlite = sqlite_conn_router(conn_type=conn_type)
    song = DownloadFile.DownloadFileClass(name=song_data.title, download_name=custom_name, url=url, description=song_data.description, type=input_type, length=song_data.length)
    if conn_type == 'input':
        cur = cur.execute(usr_sqlite, (song.name, song.download_name, song.url, song.description, song.type, song.length))
        conn.commit()
    elif conn_type == 'read':
        cur = cur.execute(usr_sqlite)

def should_commit(download_type):
    if download_type == 'MP4':
        return True
    elif download_type == 'MP3':
        return False

