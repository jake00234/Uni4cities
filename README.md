KPMG Ideathon Challenge: Incomplete Contract Prevention AI
=============

## Background

(preliminary) News About Incomplete Contract: <https://www.mk.co.kr/news/economy/view/2020/02/173358/>
This service is designed to solve problems that may arise in the process of financial companies when selling their financial products to their consumers.
Possible problems may include:
- Omission of important points, falsehood, exaggeration
- Unable to identify individual customers
- Non-conscience and oversight halls of enterprises
- Technical limitations for non-face sales

## How it should worked

  1. AI automatically summarize given terms and conditions for financial products
  2. Get keywords from the given one
  3. Customer willing to buy reads terms and conditions
  4. AI Generates questions for customer
  5. Analyze customer's voice, face
  6. Score customer's Understanding
  7. Generate report of customer
  8. Company(maybe Bank, Insurance company.. and so on) examines customer by report

## Model flow chart
<img width="1594" alt="KakaoTalk_20200222_235852099" src="https://user-images.githubusercontent.com/44601516/75094542-65a31800-55cf-11ea-8d02-ef41d81fc541.png">


## Tech

  Microsoft Azure Cognitive Services
  Azure: <https://azure.microsoft.com/ko-kr/>
  
  By using Microsoft Azure's speech to text, text analytics, sentiment and face api, quantify consumers' understanding.
  To help enterprise reduce thier time consumption and efficient consumer management.
  
  <img src="https://azurecomcdn.azureedge.net/cvt-e761bbc71a75271f4158df1a661cf62503d2ed28725b33bbd621235dfd681d93/mediahandler/files/videofiles/thumbnails/cognitive-services-overview-animation-video/CC0754_MS_AzureCognitiveServices_StyleFramePlaceHolder-01-01%20(3).png" width="450px" height="300px" alt="Azure"></img><br/>
  
  
### Prerequisites
```
  * python3 (Python Software Foundation License)
  
  * gensim for summarizing with WordRank Method (GNU LGPLv2.1 license)
  
  * python-docx2txt for pharsing docx (MIT License)
  
  * python-docx for generating report (MIT License)
  
  * opencv for capturing camera (3-clause BSD License)

  * PyQt5 for GUI (GNU GPL and Commercial)
  
  * Azure face python sdk, Azure textanalysis python sdk, Azure speech python sdk (Commerical)
  
  * Matplotlib (Python Software Foundation License)
  
  * Numpy (3-clause BSD License)
  ```


## Contributors of Uni4cities
* 이제혁(leader)  jake00234@gmail.com
* 배영재          qodudwos@gmail.com
* 안리아          anlia.seoul@gmail.com
* 전상유          annajeon322322@gmail.com
* 황수정          hwangssu5194@gmail.com

