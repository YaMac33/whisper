import sys
import whisper

def main():
if len(sys.argv) < 2:
print("使い方: python run_whisper.py 音声ファイルパス")
sys.exit(1)

audio_path = sys.argv[1]

# モデルを読み込み（smallモデルを例示）
print("Whisperモデルを読み込み中...")
model = whisper.load_model("small")

# 文字起こしを実行
print("文字起こしを実行中...")
result = model.transcribe(audio_path, language="ja")

# 結果を表示
print("----- 文字起こし結果 -----")
print(result["text"])

if name == "main":
main()
