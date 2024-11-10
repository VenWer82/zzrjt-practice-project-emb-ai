import requests

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers =  {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    json_request = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=json_request, headers=headers)
    data = response.json()['documentSentiment']
    return {'label': data['label'], 'score': data['score']}

