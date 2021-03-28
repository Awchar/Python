import os
import json


json_file = open('Data/Data.json','r')
json_data = json.load(json_file)
print(json_data)


main_path = '/media/angad/WD/'
for root,dirs, files in os.walk(main_path):
    for filename in files:
        path = os.path.join(root,filename)
        if filename.endswith(tuple(json_data['Compress'])):
            print(filename)