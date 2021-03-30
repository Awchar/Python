import os
import json


json_file = open('Data/Data.json','r')
json_data = json.load(json_file)
json_file.close()

def File_Count():
    MCount = 0
    VCount = 0
    CCount = 0
    ICount = 0
    OCount = 0
    main_path = '/media/angad/WD/'
    for root,dirs, files in os.walk(main_path):
        for filename in files:
            path = os.path.join(root,filename)
            if filename.endswith(tuple(json_data['Compress'])):
               CCount +=1
            elif filename.endswith(tuple(json_data['Music'])):
                MCount +=1
            elif filename.endswith(tuple(json_data['Image'])):
                ICount +=1
            elif filename.endswith(tuple(json_data['Video'])):
                VCount +=1
            else:
                OCount +=1
    json_data['Music Count'] = MCount
    json_data['Video Count'] = VCount
    json_data['Image Count'] = ICount
    json_data['Compress Count'] = CCount
    json_data['Other Count'] = OCount
    json_file = open('Data/Data.json','w')
    json.dump(json_data,json_file,indent=4)
    json_file.close()

            
File_Count()
