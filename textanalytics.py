

import os
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from azure.ai.textanalytics import single_analyze_sentiment
from msrest.authentication import CognitiveServicesCredentials
import key
subscription_key = key.text_key
endpoint = "https://kpmg-text.cognitiveservices.azure.com/"
key = key.text_key
def authenticateClient():
    credentials = CognitiveServicesCredentials(subscription_key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credentials=credentials)
    return text_analytics_client


def sentiment_analysis_example(endpoint, key):

    document = "나는 나에게 이렇게 좋은일 생겨날 줄 몰랐어"

    response = single_analyze_sentiment(endpoint=endpoint, credential=key, input_text=document)
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.3f}; neutral={1:.3f}; negative={2:.3f} \n".format(
        response.document_scores.positive,
        response.document_scores.neutral,
        response.document_scores.negative,
    ))
    for idx, sentence in enumerate(response.sentences):
        print("[Offset: {}, Length: {}]".format(sentence.offset, sentence.length))
        print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
        print("Sentence score:\nPositive={0:.3f}\nNeutral={1:.3f}\nNegative={2:.3f}\n".format(
            sentence.sentence_scores.positive,
            sentence.sentence_scores.neutral,
            sentence.sentence_scores.negative,
        ))

            
sentiment_analysis_example(endpoint, key)

def entity_recognition():

    client = authenticateClient()

    try:
        documents = [
            {"id": "1", "language": "ko", "text": "하락률이 가장 큰 자산"},
            {"id": "2", "language": "ko",
                "text": "하락률이 가장 높은 자산"},
            {"id": "3", "language": "ko",
                "text": "하락률 이 큰 자산"},
            {"id": "4", "language": "ko", "text": "오십오퍼센트요"},
            {"id": "5", "language": "ko", "text": "오십오퍼센트"},
            {"id": "6", "language": "ko", "text": "55% 라고 생각합니다"},
            
            
        ]
        response = client.entities(documents=documents)

        for document in response.documents:
            print("Document Id: ", document.id)
            print("\tKey Entities:")
            for entity in document.entities:
                print("\t\t", "NAME: ", entity.name, "\tType: ",
                      entity.type, "\tSub-type: ", entity.sub_type)
                for match in entity.matches:
                    print("\t\t\tOffset: ", match.offset, "\tLength: ", match.length, "\tScore: ",
                          "{:.2f}".format(match.entity_type_score))

    except Exception as err:
        print("Encountered exception. {}".format(err))

entity_recognition()


def key_phrases():
    
    client = authenticateClient()

    try:
        documents = [
            {"id": "1", "language": "ko", "text": "하락률이 가장 큰 자산"},
            {"id": "2", "language": "ko", "text": "하락률이 가장 높은 자산"},
            {"id": "3", "language": "ko","text": "하락률 이 큰 자산"},
            {"id": "4", "language": "ko", "text": "오십오퍼센트요"},
            {"id": "5", "language": "ko", "text": "오십오퍼센트"},
            {"id": "6", "language": "ko", "text": "55% 라고 생각합니다"},
            
            
        ]

        for document in documents:
            print(
                "Asking key-phrases on '{}' (id: {})".format(document['text'], document['id']))

        response = client.key_phrases(documents=documents)

        for document in response.documents:
            print("Document Id: ", document.id)
            print("\tKey Phrases:")
            for phrase in document.key_phrases:
                print("\t\t", phrase)

    except Exception as err:
        print("Encountered exception. {}".format(err))
key_phrases()