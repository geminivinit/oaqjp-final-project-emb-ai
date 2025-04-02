import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    #print(formatted_response)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    max_score = max(emotions.values())
    dominant_emotion = [key for key, val in emotions.items() if val == max_score][0]
    emotions['dominant_emotion'] = dominant_emotion
    return emotions