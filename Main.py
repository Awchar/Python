import first
import json

json_file = open('Data/Data.json','r')
json_data = json.load(json_file)

videos = first.File(tuple(json_data['Video']))
action = first.Action(videos.Organize(organize=False))
action.Move()