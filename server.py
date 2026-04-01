from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    """
    Endpoint to analyze the text provided by the user and return emotion scores.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # If the response is None (e.g., due to an error), handle it accordingly
    if response is None:
        return "Invalid text! Please try again."

    # Extract emotions and dominant_emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with the sentiment analysis results
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Route to render the main application page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Execute the Flask app on localhost at port 5000
    app.run(host="0.0.0.0", port=5000)