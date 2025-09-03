# app.py
# Flaskを使ってWhisperの文字起こしをWeb API化するサンプル

from flask import Flask, request, jsonify, render_template
import whisper
import os

app = Flask(__name__)

# Whisperモデルの読み込み（起動時に一度だけ）
model = whisper.load_model("small")

@app.route("/")
def index():
    # 音声アップロード用フォーム（templates/index.htmlを表示）
    return render_template("index.html")

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    if "audio" not in request.files:
        return jsonify({"error": "音声ファイルがアップロードされていません"}), 400

    audio_file = request.files["audio"]

    # 一時保存
    temp_path = os.path.join("temp_audio", audio_file.filename)
    os.makedirs("temp_audio", exist_ok=True)
    audio_file.save(temp_path)

    try:
        # Whisperで文字起こし
        result = model.transcribe(temp_path, language="ja")

        # 文字起こし結果を返却
        return jsonify({"text": result["text"]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        # 一時ファイルを削除
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    # デバッグモードで起動
    app.run(host="0.0.0.0", port=5000, debug=True)