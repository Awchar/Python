import first
import json

json_file = open('Data/Data.json','r')
json_data = json.load(json_file)

music = first.File(tuple(json_data['Music']))
for i in music.Organize():
    print(i)