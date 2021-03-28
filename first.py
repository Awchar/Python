import os
import fnmatch
import re
from tinytag import TinyTag
import shutil
import tqdm
import json

main_path = '/media/angad/WD'
json_file = open('Data/Data.json','r')
json_data = json.load(json_file)


class File:

    def __init__(self,ext):
        self.ext = ext


    def All(self):
        print('Loading All Files ....')
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

    def __init__(self,files):
        self.files = files


    def Move(self):
        Backbone.All()
        for i in tqdm.tqdm(self.files):
            if i.endswith(tuple(json_data['Video'])):
                dst_path = Backbone.Destination(i)
                if dst_path == []:
                    pass
                else:
                    #print(dst_path)
                    print(i.split('/')[-1])
                    dst_path = os.path.join(main_path,dst_path)
                    if os.path.isfile(dst_path):
                        print('File Already Exists')
                    else:
                        try:
                            #print(dst_path)
                            shutil.move(i,dst_path)
                        except FileNotFoundError as error:
                            folder = dst_path.split('/')[0:-1]
                            folder = '/'.join(folder)
                            print(f"{folder} Folder Created.")
                            os.mkdir(folder)
                            try:
                                shutil.move(i,dst_path)
                            except Exception as d:
                                pass
                        except Exception as e:
                            pass
            elif i.endswith(tuple(json_data['Music'])):
                dst_path = Backbone.Destination(i)
                if dst_path  == []:
                    pass
                else:
                    print(i.split('/')[-1])
                    dst_path = os.path.join(main_path,dst_path)
                    if os.path.isfile(dst_path):
                        print('File Already Exists : ',i.split('/')[-1])
                    else:
                        try:
                            #print(dst_path)
                            shutil.move(i,dst_path)
                        except FileNotFoundError as error:
                            folder = dst_path.split('/')[0:-1]
                            folder = '/'.join(folder)
                            print(f"{folder} Folder Created.")
                            os.makedirs(folder)
                            try:
                                shutil.move(i,dst_path)
                            except Exception as d:
                                pass
                        except Exception as e:
                            pass
                        
    

    def Check(self):
        size = 0
        for i in tqdm.tqdm(self.files,leave=False):
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
        dst = []
        if File.endswith(tuple(json_data)):
            All_Content = Backbone.All_Text('All')
            for i in All_Content:
                show = i.split('/')[-1]
                if fnmatch.fnmatch(File,'*'+show+'*'):
                    pattern = r"Season \b[0-9]+"
                    subdir = re.search(pattern,File)
                    if bool(subdir) == True:
                        #print(subdir.group())
                        dst = os.path.join(i,os.path.join(subdir.group(),name))
                    else:
                        dst = os.path.join(i,name)
        elif File.endswith(tuple(json_data)):
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
                    for k in Backbone.All_Text(j):
                        path = "{}/{}/{}".format(i,j,k)
                        #print(path)
                        alls.append(path)
            except Exception as e:
                pass
        file_all = open('Data/All.txt','w')
        for h in alls:
            file_all.write(h+'\n')
        file_all.close()





