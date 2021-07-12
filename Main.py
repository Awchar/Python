import first
import json

json_file = open('Data/Data.json','r')
json_data = json.load(json_file)

videos = first.File(tuple(json_data['Video']))
for i in videos.All():
    print(i)