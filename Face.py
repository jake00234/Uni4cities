import requests
import json
import key

class EmotionFace:

    emotions=''

    def __init__(self,src):
# set to your own subscription key value
        subscription_key =key.face_key
        assert subscription_key

# replace <My Endpoint String> with the string from your endpoint URL
        face_api_url = 'https://kpmg-face.cognitiveservices.azure.com/face/v1.0/detect'

        data = open(src,'rb')

        headers = {'Content-Type': 'application/octet-stream','Ocp-Apim-Subscription-Key': subscription_key}

        params = {
            'returnFaceId': 'false',
            'retrunFaceRectangle':'false',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'emotion'
        }

        response = requests.post(face_api_url, headers=headers, params=params, data=data)



        json_data = json.dumps(response.json())[0]
        with open('json_data.json','w',encoding="utf-8") as make_file:
            json.dump(response.json(), make_file, ensure_ascii=False, indent="\t")

        with open('json_data.json','r') as f:
            json_data = json.load(f)
        if str(json_data[0]['faceAttributes']['emotion']):
            self.emotions = str(json_data[0]['faceAttributes']['emotion'])
        

#string = json_data[144:288]








