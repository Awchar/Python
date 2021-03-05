import os
import fnmatch
import re
from tinytag import TinyTag
import shutil

main_path = '/media/angad/WD'


class File:

    def __init__(self,ext):
        self.ext = ext


    def All(self):
        print('Loading All Files....')
        all_files = []
        for root,dirs,files in os.walk(main_path):
            for filename in files:
                if filename.endswith(self.ext):
                    path = os.path.join(root,filename)
                    all_files.append(path)
        return all_files


    def Organize(self,organize=True):
        pattern = r"My [Videos|Movies|Documents|Music]"
        all_content = File(self.ext)
        all_files = []
        base_files = all_content.All()
        if organize ==True:
            print('Loading Organized Files....')
            for i in base_files:
                if re.search(pattern,i):
                    all_files.append(i)
        elif organize ==False:
            print('Loading UNOrganized Files....')
            for i in base_files:
                if not re.search(pattern,i):
                    all_files.append(i)
        return all_files



class Action:

    def __init__(self,Files):
        self.Files = Files


    def Move(self):
        Create_Folder()
        for i in self.Files:
            pass
    

    def Check(self):
        size = 0
        for i in self.Files:
            size += os.stat(i).st_size
        print(f"Number Of Files: {len(self.Files)}")
        print(f"Size Of All Files: {Backbone.Size(size)}")

class Backbone:

    def Size(number):
        if number < 1024:
            return str(number)+" bytes"
        elif number < (1024*1024):
            number = number/(1024)
            return str(round(number,2))+" KB"
        elif number < (1024*1024*1024):
            number = number/(1024*1024)
            return str(round(number,2))+" MB"
        elif number < (1024*1024*1024*1024):
            number = number/(1024*1024*1024)
            return str(round(number,2))+" GB"


    def Destination(File):
        name = File.split('/')[-1]
        if File.endswith(('mp4','mkv','avi')):
            All_Content = All_Text('All')
            for i in All_Content:
                show = i.split('/')[-1]
                if fnmatch.fnmatch(File,'*'+show+'*'):
                    dst = os.path.join(i,name)
        elif File.endswith('mp3'):
            tag = TinyTag.get(File)
            if tag.album == None:
                return False
            else:
                dst = os.path.join(os.path.join("My Music",str(tag.year)),os.path.join(tag.album,name)) 
        return dst 



    def All_Text(File):
        content = []
        with  open('Data/'+File+'.txt','r') as f:
            for i in f:
                content.append(i.rstrip('\n'))
        return content


    def All():
        alls = []
        for i in Backbone.All_Text('Main'):
            try:
                for j in Backbone.All_Text(i):
                    for k in All_Text(j):
                        path = "{}/{}/{}".format(i,j,k)
                        alls.append(path)
            except Exception as e:
                pass
        file_all = open('Data/All.txt','w')
        for h in alls:
            file_all.write(h+'\n')
        file_all.close()



    def Create_Folder():
        All()
        f = open('Data/All.txt','r')
        for i in f:
            folder = os.path.join(main_path,i.rstrip('\n'))
            #print(folder)
            if os.path.isdir(folder):
                pass
            else:
                try:
                    os.mkdir(folder)
                    print(f'{folder}\nFolder Create Succesfull')
                except Exception as e:
                    pass

Backbone.All()