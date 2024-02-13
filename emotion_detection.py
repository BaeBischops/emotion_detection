'''The emotional detection module'''
import json
import requests

def emotion_detector(text_to_analyse):
    '''
    Parses emotional response from Watson NLU service.

    Args:
        response (requests.Response): Response from Watson NLU.
            It should contain emotional analysis data in JSON format.

    Returns:
        dict: Emotional label and score from response.
            The dictionary structure is as follows:
            {
                'label': str or None,
                'score': float or None
            }
            'label' represents the overall emotional label assigned to the text, such as 'positive' or 'negative'.
            'score' represents the confidence score associated with the assigned label.
            If the response is successful (status code 200), both 'label' and 'score' are populated.
            If the response indicates an error (status code 500), both 'label' and 'score' are set to None.

    Raises:
        ValueError: If the response object is None or empty.
        json.JSONDecodeError: If there's an error in decoding the JSON response.
        Exception: If there's an error in parsing the emotional response data.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=10)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None

    return {'label': label, 'score': score}
