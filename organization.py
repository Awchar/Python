import sqlite3
import tqdm
import os
from tinytag import TinyTag

conn = sqlite3.connect('Data/All.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS Alls(Name TEXT,Extension TEXt,Size INT)')
c.execute('CREATE TABLE IF NOT EXISTS MUSIC(Year TEXT,Album TEXT,Title TEXT,Size INT)')

class Files:


    def __init__(self,ext):
        self.ext = ext


    def All(self):
        print('Loading Files.')
        content = []
        for root,dirs,files in os.walk('/media/angad/WD'):
            for filename in files:
                if filename.endswith(self.ext):
                    path = os.path.join(root,filename)
                    content.append(path)
                    #print(path)
        return content
        print('File Loading Compelete.')


class DataBase:

    def __init__(self,Files):
        self.Files = Files


    def Present(filename,Size):
        contents = c.execute('SELECT * FROM Alls')
        for i in contents:
            if contents[2] == Size:
                if contents[0] == filename:
                    return True

    def All(self):
        c.execute("DELETE Alls")
        print('Creating DataBase.')
        for i in tqdm.tqdm(self.Files):
            filename = i.split('/')[-1]
            ext = filename.split('.')[-1]
            size = os.stat(i).st_size
            c.execute('INSERT INTO Alls(Name,Extension,Size) VALUES(?,?,?)',(filename ,ext ,size ))
        conn.commit()
        print('DataBase Complete.')

    def Music(self):
        c.execute("DELETE FROM MUSIC")
        print('Creating Music DataBase')
        for i in tqdm.tqdm(self.Files):
            tag = TinyTag.get(i)
            year = tag.year
            album = tag.album
            size = tag.filesize
            title = i.split('/')[-1]
            c.execute('INSERT INTO MUSIC(Year,Album,Title,Size) VALUES(?,?,?,?)',(year,album,title,size))
        conn.commit()
        print('Music Database Complete.')

files = Files(('mp3','mp4','mkv','jpg','rar','zip','avi'))
music = Files('mp3')
database = DataBase(music.All())
database.Music()

