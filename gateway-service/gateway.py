from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import requests
import io

app = Flask(__name__, static_url_path="", static_folder="static")
CORS(app)  # Cho phép gọi từ web

TTS_URL = "http://tts:5006/speak"
STT_URL = "http://stt:5007/listen"

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/tts", methods=["POST", "OPTIONS"])
def gateway_tts():
    if request.method == "OPTIONS":
        return '', 204
    response = requests.post(TTS_URL, json=request.get_json())
    return response.content, response.status_code, {"Content-Type": "audio/wav"}

@app.route("/stt", methods=["POST", "OPTIONS"])
def gateway_stt():
    if request.method == "OPTIONS":
        return '', 204
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "Missing file"}), 400

    response = requests.post(STT_URL, files={"file": (file.filename, file.stream, file.mimetype)})
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)