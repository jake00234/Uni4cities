
import azure.cognitiveservices.speech  as speechsdk

print("Say something")

intent_config = speechsdk.SpeechConfig(subscription="619e13948165430b8b6174550a5d6006", region="westus")
intent_recognizer = speechsdk.intent.IntentRecognizer(speech_config=intent_config)

model = speechsdk.intent.LanguageUnderstandingModel(app_id="6016da04-d862-4676-8771-e97518934132")
intents = [
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