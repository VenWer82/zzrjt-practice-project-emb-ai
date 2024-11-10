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
      if text_to_analyze is None:
          return {'message': 'Missing paramater'}, 400

      result = sentiment_analyzer(text_to_analyze)   
      label = result['label']
      score = result['score']
      return f'The analyzed text is of sentiment {label}, and the score is {score}'
    except Exception as e:
        print(e, text_to_analyze)
        return {'message': 'Internal server error'}, 500

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host='0.0.0.0',port=5000, debug=True)
