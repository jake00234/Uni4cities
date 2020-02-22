import requests
import json

# set to your own subscription key value
subscription_key ="ffc0143020ac4e2893f47c0d7e753b47"
assert subscription_key

# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = 'https://kpmg-face.cognitiveservices.azure.com/face/v1.0/detect'

data = open('./opencv_frame_0.png','rb')

headers = {'Content-Type': 'application/octet-stream','Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, headers=headers, params=params, data=data)
print(json.dumps(response.json()))