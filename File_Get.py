import os
import time
import ftplib
import sqlite3
from tqdm import tqdm

conn = sqlite3.connect('Data/All.db')
c = conn.cursor()

main_path = '/media/angad/WD/Other Stuff'

ftp = ftplib.FTP()
ftp.encoding='utf-8'
IP = '192.168.0.100'

def Raw_Links():
    ftp.connect(IP,2121)
    ftp.login('angad','266423')
    All_Content = []
    for first in ftp.nlst():
        #print(first)
        All_Content.append(first)
        for second in ftp.nlst(first):
            seconds = first+'/'+second
            #print(seconds)
            All_Content.append(seconds)
            for third in ftp.nlst(seconds):
                thirds = seconds+'/'+third
                #print(thirds)
                All_Content.append(thirds)
                for fourth in ftp.nlst(thirds):
                    fourths = thirds+'/'+fourth
                    #print(fourths)
                    All_Content.append(fourths)
    return All_Content


def Valid_Links():
    ftp.connect(IP,2121)
    ftp.login('angad','266423')
    valid_link = []
    for i in Raw_Links():
        if i.endswith(('mp3','mp4','mkv','pdf')):
            try:
                size = ftp.size(i)
                valid_link.append(i)
                #print('File: {}\nSize: {}'.format(i,size))
            except Exception as e:
                pass
    return valid_link

def Present(File):
    datas = c.execute('SELECT * FROM Alls')
    size = ftp.size(File)
    filename = File.split('/')[-1]
    for data in datas:
        if size == data[2]:
            if filename == data[0]:
                return True

def Download(File):
    ftp.connect(IP,2121)
    ftp.login('angad','266423')
    # Check if the latest build in the local path, if not download it.
    filename = File.split('/')[-1]
    filename = os.path.join(main_path,filename)
    bufsize=1024
    fp=open(filename,'wb')
    total=ftp.size(File)
    pbar=tqdm(total=total,leave=False)
    def bar(data):
        fp.write(data)
        pbar.update(len(data))
    print('\nBegin to download: %s'%filename,end='\r')
    ftp.retrbinary('RETR '+File,bar,bufsize)
    pbar.close()
    fp.close()



def New_File():
    new_link = []
    for i in Valid_Links():
        if Present(i) == True:
            pass
        else:
            new_link.append(i)
    return new_link


def All_Download():
    for i in tqdm(New_File(),leave=False):
        Download(i)
        size = ftp.size(i)
        ext = i.split('.')[-1]
        filename = i.split('/')[-1]
        c.execute('INSERT INTO Alls(Name,Extension,Size) VALUES(?,?,?)',(filename,ext,size))
        conn.commit()


All_Download()
