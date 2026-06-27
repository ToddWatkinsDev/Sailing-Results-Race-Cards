from flask import Flask, jsonify, send_from_directory
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'Results.html')

@app.route('/results-input.json')
def results_input():
    return send_from_directory(BASE_DIR, 'results-input.json')

@app.route('/api/players/<srid>')
def player_proxy(srid):
    url = f'https://sailranks.com/api/players/{srid}'
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e), 'srid': srid}), 502

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)