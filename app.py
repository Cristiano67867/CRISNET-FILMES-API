from flask import Flask, jsonify
from flask_cors import CORS
from filmesJson import FILMES
import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Hello to CRISNET FILME API"})

@app.route('/movies', methods=['GET'])
def list_movies():
    return jsonify(FILMES)
    
@app.route('/static/movies<path:filename>', methods=['GET'])
def server_image(filename):
    return send_from_directory("static/movies", filename)

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=PORT)
