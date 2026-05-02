"""
Emotion Detector Server module
Executable Flask server for the emotion detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import format_emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Call Emotion Detector analyzes text to detect specific emotional tones and returns them with 
    corresponding confidence scores. From the returned list, display the domainant emotion based
    on the highest score.
    """

    text_to_analyze = request.args.get('textToAnalyze')
    response = format_emotion_detector(text_to_analyze)
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        result = "<b>Invalid text! Please try again!</b>"
    else:
        filtered_dict = {k: v for k, v in response.items() if k != "dominant_emotion"}
        output = ", ".join(f"'{k}': {v}" for k, v in filtered_dict.items())
        result = f"For the given statement, the system response is {output}. \
            The dominant emotion is <b>{dominant_emotion}</b>."

    return result


@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application page
    over the Flask framework for Emotion Detection.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000)