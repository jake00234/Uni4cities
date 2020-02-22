key = "2fbd0184b74d47af86b065ad503ab89f"
endpoint = "https://kpmg-text.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential

text_analytics_client = TextAnalyticsClient(endpoint, TextAnalyticsApiKeyCredential(key))

documents = [
    "난 집에 갈래",
    "정말 좋은 날이야",
    "55% 라고 생각합니다.",
    "음 55% 요",
    "55% 요"
]

response = text_analytics_client.analyze_sentiment(documents, language="ko")
result = [doc for doc in response if not doc.is_error]

for doc in result:
    print("Overall sentiment: {}".format(doc.sentiment))
    print("Scores: positive={0:.3f}; neutral={1:.3f}; negative={2:.3f} \n".format(
        doc.sentiment_scores.positive,
        doc.sentiment_scores.neutral,
        doc.sentiment_scores.negative,
    ))

print("<----sentiment\n")

response = text_analytics_client.recognize_entities(documents, language="ko")
result = [doc for doc in response if not doc.is_error]

for doc in result:
    for entity in doc.entities:
        print("Entity: \t", entity.text, "\tCategory: \t", entity.category,
              "\tConfidence Score: \t", entity.score)
print("<----entity\n")

response = text_analytics_client.recognize_linked_entities(documents, language="ko")
result = [doc for doc in response if not doc.is_error]

for doc in result:
    for entity in doc.entities:
        print("Entity: {}".format(entity.name))
        print("URL: {}".format(entity.url))
        print("Data Source: {}".format(entity.data_source))
        for match in entity.matches:
            print("Score: {0:.3f}".format(match.score))
            print("Offset: {}".format(match.offset))
            print("Length: {}\n".format(match.length))
print("<----entity\n")



response = text_analytics_client.extract_key_phrases(documents, language="ko")
result = [doc for doc in response if not doc.is_error]

for doc in result:
    print(doc.key_phrases)

print("<----keyphrase\n")