
import azure.cognitiveservices.speech as speechsdk


class SpeechToText:

    text = ""

    def __init__(self):
        print("Say Something")

        speech_config = speechsdk.SpeechConfig(subscription="65177667639a4052b08c334e9be21c04", region="westus", speech_recognition_language="ko-KR")
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
      
        # Starts intent recognition, and returns after a single utterance is recognized. The end of a
        # single utterance is determined by listening for silence at the end or until a maximum of 15

        result = speech_recognizer.recognize_once()

        # Check the results
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(result.text))
            SpeechToText.text = result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(result.no_match_details))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))