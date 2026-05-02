import json
import requests

def emotion_detector(text_to_analyze):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)       

    if response.status_code == 400:
        return None;

    return response.text


def format_emotion_detector(text_to_analyze):
    response = emotion_detector(text_to_analyze)

    if response is None:
        results = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        formatted_response = json.loads(response)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        results = {}
        for key, value in emotions.items():
            results[key] = value

        dominant_emotion = max(emotions, key=emotions.get)
        results["dominant_emotion"] = dominant_emotion

    return results