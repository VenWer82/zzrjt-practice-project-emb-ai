''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
app = Flask('Sentiment Analyzer')
#Initiate the flask app : TODO

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    try:
        text_to_analyze = request.args.get('textToAnalyze')
        if not text_to_analyze:
            return "Empty Field, Try again"
        result = sentiment_analyzer(text_to_analyze)
        label = result['label']
        score = result['score']
        if label is None:
            return 'Invalid text input, try again'
        return f'The analyzed text is of sentiment {label}, and the score is {score}'
    except Exception:
        return {'message': 'Internal server error'}, 500

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
