from flask import Blueprint, request, jsonify
from textblob import TextBlob

correct_spelling_route = Blueprint('correct_spelling_route', __name__)

@correct_spelling_route.route('/correct', methods=['POST'])
def correct_spelling_route_handler():
    incorrect_text = request.json.get('text', '')

    if not incorrect_text:
        return jsonify({'error': 'No text provided'}), 400

    blob = TextBlob(incorrect_text)
    corrected_text = str(blob.correct())

    return jsonify({'original': incorrect_text, 'corrected': corrected_text})
