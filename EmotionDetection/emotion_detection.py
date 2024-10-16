import requests
import json
import pprint


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 200:   
        formatted_response = json.loads(response.text)

        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        emotions = formatted_response['emotionPredictions'][0]['emotion']
        name_of_dominant_emotion = max(emotions, key=emotions.get)

    # If the response status code is 400, set all scores to "None" (actually, the status code for empty input is 500)
    elif response.status_code == 400 or response.status_code == 500:   
        anger_score = "None"
        disgust_score = "None"
        fear_score = "None"
        joy_score = "None"
        sadness_score = "None" 
        name_of_dominant_emotion = "None"        

    arranged_emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': name_of_dominant_emotion
    }

    #return formatted_response  # Return the response text from the API as json
    return arranged_emotions