"""This is a module docstring.

This module is used to run sentiment anlaysis
"""

# Import the Flask class from the flask module
from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector
# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)
# Define a route for the root URL ("/")

@app.route("/")
def get_default():
    """This is default function in the module."""
    # Function that handles requests to the root URL
    return render_template("index.html")

@app.route("/emotionDetector")
def get_emotion():
    """This is emotion anlaysis function in the module."""
    query = request.args.get("textToAnalyze")
    resp = emotion_detector(query)
    if resp['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    output = "For the given statement, the system response is "
    for key,value in resp.items():
        if key=="dominant_emotion":
            if output.endswith(", "):
                output = output[:-2]+"."+"The dominant emotion is "+value+"."
        else:
            output += f"{key}: {value}, "
    return output
            