from flask import Flask, request, send_file, jsonify
from TTS.api import TTS
import uuid
import os

app = Flask(__name__)

# Load model
MODEL_NAME = "hynt/F5-TTS-Vietnamese-100h"
tts = TTS(MODEL_NAME, progress_bar=False, gpu=False)

@app.route("/tts", methods=["POST"])
def synthesize():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    filename = f"/tmp/{uuid.uuid4().hex}.wav"
    tts.tts_to_file(text=text, file_path=filename)

    return send_file(filename, mimetype="audio/wav", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)
