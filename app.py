from flask import Flask, request, jsonify
from textblob import TextBlob
from routes import correct_spelling_route

app = Flask(__name__)

app.register_blueprint(correct_spelling_route)

if __name__ == '__main__':
    app.run(debug=True, port=5002)  

