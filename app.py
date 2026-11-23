from flask import Flask, send_from_directory
from pathlib import Path

app = Flask(__name__, static_folder=None)
BASE_DIR = Path(__file__).resolve().parent

@app.route('/')
def home():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(BASE_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
