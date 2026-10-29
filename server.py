'''
Flask server for the Emotion Detector web application.
Provides a web interface and API endpoint for emotion analysis.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    '''
    Analyzes the emotion of the given text and returns the result.
    Handles blank input with an appropriate error message.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    return (f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is <b>{dominant_emotion}</b>.")


@app.route("/")
def render_index_page():
    '''Renders the main index page.'''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
