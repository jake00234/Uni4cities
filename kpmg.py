
import azure.cognitiveservices.speech  as speechsdk
import key

print("Say something")

intent_config = speechsdk.SpeechConfig(subscription=key.speech_sub, region="westus", speech_recognition_language = "ko-KR")
intent_recognizer = speechsdk.intent.IntentRecognizer(speech_config=intent_config)

model = speechsdk.intent.LanguageUnderstandingModel(app_id=key.speech_id_key)
intents = [
    (model, "None"),
    (model, "이해하지못함"),
    (model, "이해함")

]
intent_recognizer.add_intents(intents)

# Starts intent recognition, and returns after a single utterance is recognized. The end of a
# single utterance is determined by listening for silence at the end or until a maximum of 15

intent_result = intent_recognizer.recognize_once()

# Check the results
if intent_result.reason == speechsdk.ResultReason.RecognizedIntent:
    print("Recognized: \"{}\" with intent id `{}`".format(intent_result.text, intent_result.intent_id))
elif intent_result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(intent_result.text))
elif intent_result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(intent_result.no_match_details))
elif intent_result.reason == speechsdk.ResultReason.Canceled:
    print("Intent recognition canceled: {}".format(intent_result.cancellation_details.reason))
    if intent_result.cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(intent_result.cancellation_details.error_details))
# </IntentRecognitionOnceWithMic>