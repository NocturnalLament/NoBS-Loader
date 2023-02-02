import sqlite3
from pathlib import Path
from pytube import YouTube
from Logic import DownloadFile
DB_PATH = 'DATA//DB//Test_Downloads.db'

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

def sqlite_routine(conn_type, custom_name="default",url="default", input_type="default"):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    usr_sqlite = sqlite_conn_router(conn_type=conn_type)
    if conn_type == 'input':
        song = DownloadFile.DownloadFileClass(name=song_data.title, download_name=custom_name, url=url, description=song_data.description, type=input_type, length=song_data.length)
        song_data = YouTube(url=url)
        cur = cur.execute(usr_sqlite, (song.name, song.download_name, song.url, song.description, song.type, song.length))
        conn.commit()
    elif conn_type == 'read':
        cur = cur.execute(usr_sqlite)
        results = cur.fetchall()
        return results

def should_commit(download_type):
    if download_type == 'MP4':
        return True
    elif download_type == 'MP3':
        return False

def list_all(count, name, path, type, list_index=0):
        print(count)
        index = list_index
        while index < count:
            file_name = name[index]
            file_path = path[index]
            file_type = type[index]
            print('=====================================================================================================')
            print(f'Name: {file_name}')
            print(f'Path: {file_path}')
            print(f'Type: {file_type}')
            print('=====================================================================================================')
            index += 1
            continue
            
        

        

def list_downloads():
    sqlite_string = '''
        
        SELECT CustomName FROM Downloads
    
    '''

    conn = sqlite3.connect(DB_PATH)
    curr = conn.cursor()
    curr.execute(sqlite_string)
    song_name = curr.fetchall()

    sqlite_string = '''
    
        Select DownloadPath FROM Downloads
    
    '''

    curr.execute(sqlite_string)

    song_path = curr.fetchall()

    sqlite_string = '''
    
        SELECT Type FROM Downloads
    
    '''

    curr.execute(sqlite_string)

    song_types = curr.fetchall()

    list_count = len(song_types)

    list_all(list_count, song_name, song_path, song_types)



    



