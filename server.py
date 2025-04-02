# Import the Flask class from the flask module
from flask import Flask,render_template,request

from EmotionDetection.emotion_detection import emotion_detector
# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)
# Define a route for the root URL ("/")

@app.route("/")
def get_default():
    # Function that handles requests to the root URL
    return render_template("index.html")

@app.route("/emotionDetector")
def get_emotion():
    query = request.args.get("textToAnalyze")
    resp = emotion_detector(query)
    output = "For the given statement, the system response is "
    for key, value in resp.items(): 
         if (key == "dominant_emotion"):
            if output.endswith(", "):
                output = output[:-2] + "." + "The dominant emotion is " + value + "."
         else:
            output += f"{key}: {value}, "

    return output
            