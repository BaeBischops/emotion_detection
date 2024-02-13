import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    # Extract emotions and their scores
    emotion_predictions = formatted_response.get('emotionPredictions', [])
    emotion_scores = {}
    for prediction in emotion_predictions:
        emotions = prediction.get('emotion', {})
        for emotion, score in emotions.items():
            emotion_scores[emotion] = max(emotion_scores.get(emotion, 0), score)

    # Find dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Prepare output format
    output = {
        'anger': emotion_scores.get('anger', 0),
        'disgust': emotion_scores.get('disgust', 0),
        'fear': emotion_scores.get('fear', 0),
        'joy': emotion_scores.get('joy', 0),
        'sadness': emotion_scores.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }

    return output
