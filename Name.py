import os
import fnmatch
import re



main_path = '/media/angad/WD/My Videos/Hindi TvShow'
show = 'Pyaar Kii Ye Ek Kahaani'
main_path = os.path.join(main_path,show)
for root,dirs,files in os.walk(main_path):
    for filename in files:
        path = os.path.join(root,filename)
        if fnmatch.fnmatch(path,'*Season*'):
            pattern = r'Season \b[0-9]+'
            subdir = re.search(pattern,path)
            season = subdir.group()
            name = path.split('-')
            name.insert(-2,season)
            name = '-'.join(name)
            print(name)
            os.rename(path,name)