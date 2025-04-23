from flask import Flask, request, jsonify, send_file, after_this_request
import subprocess
import uuid
import os

app = Flask(__name__)

@app.route("/speak", methods=["POST"])
def tts_infer():
    data = request.get_json()
    text = data.get("text", "")
    speed = data.get("speed", 0.8)

    if not text:
        return jsonify({"error": "Missing text"}), 400

    uid = uuid.uuid4().hex
    output_wav = f"/tmp/{uid}.wav"
    model_dir = "/model"

    command = [
        "f5-tts_infer-cli",
        "--model", "F5TTS_Base",
        "--gen_text", text,
        "--speed", str(speed),
        "--vocoder_name", "bigvgan",
        "--vocab_file", os.path.join(model_dir, "vocab.txt"),
        "--ckpt_file", os.path.join(model_dir, "model_500000.pt"),
        "-w", output_wav  # ✅ Thay vì --output_path
    ]

    try:
        subprocess.run(command, check=True)

        @after_this_request
        def cleanup(response):
            try:
                os.remove(output_wav)
            except Exception as e:
                app.logger.error(f"Cleanup failed: {e}")
            return response

        return send_file(output_wav, mimetype="audio/wav", as_attachment=True)

    except subprocess.CalledProcessError as e:
        return jsonify({
            "error": "TTS inference failed",
            "detail": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)
