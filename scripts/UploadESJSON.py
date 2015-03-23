import os
import requests
import json

rootdir = '/vagrant/files'
REMOTE_URLcred = 'https://cp94zbqxv3:estftr8mkx@km-prototype-1076374862.eu-west-1.bonsai.io/knowledgelive/information' #for live

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        loc = os.path.join(subdir, file)
        ext = os.path.splitext(file)[-1].lower()

        if ext == ".json":
            json_data = open(loc)
            data = json.load(json_data)
            id_value = data["id"]
            payload = json.load(open(loc))
            headers = {'content-type': 'application/json'}
            r = requests.post(REMOTE_URLcred+'/'+id_value, data=json.dumps(payload), headers=headers)
            print r.status_code
            if r.status_code == 201:
                print loc+' has been uploaded'
        else:
            print file+' is not a JSON file'

            
            