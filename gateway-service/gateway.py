from flask import Flask, request, jsonify, send_file
import requests
import io

app = Flask(__name__)

TTS_URL = "http://tts:5001/speak"
STT_URL = "http://stt:5002/listen"

@app.route("/tts", methods=["POST"])
def gateway_tts():
    response = requests.post(TTS_URL, json=request.get_json())
    return response.content, response.status_code, {"Content-Type": "audio/wav"}

@app.route("/stt", methods=["POST"])
def gateway_stt():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "Missing file"}), 400

    response = requests.post(STT_URL, files={"file": (file.filename, file.stream, file.mimetype)})
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)