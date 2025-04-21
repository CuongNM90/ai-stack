from flask import Flask, request, jsonify
from TTS.api import TTS
import tempfile
import os

app = Flask(__name__)

# ✅ Make sure this works with upgraded TTS
tts = TTS.from_pretrained("tts_models/vi/vivos/glow-tts")

@app.route("/speak", methods=["POST"])
def speak():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "Missing 'text' field"}), 400

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        tts.tts_to_file(text=text, file_path=f.name)
        with open(f.name, "rb") as audio_file:
            audio_data = audio_file.read()
        os.unlink(f.name)
        return audio_data, 200, {"Content-Type": "audio/wav"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)
