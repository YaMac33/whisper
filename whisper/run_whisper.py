# run_whisper.py
# Whisperオープンソース版を使って音声ファイルを文字起こしするサンプルスクリプト

import argparse
import whisper

def main():
    # 引数の定義
    parser = argparse.ArgumentParser(description="Whisperを使って音声を文字起こしします。")
    parser.add_argument("audio_path", type=str, help="入力音声ファイル（例: sample.wav）")
    parser.add_argument("--model", type=str, default="small", help="使用するモデルサイズ (tiny, base, small, medium, large)")
    parser.add_argument("--language", type=str, default=None, help="音声言語（自動検出なら指定不要）")
    args = parser.parse_args()

    # モデルの読み込み
    print(f"Loading Whisper model: {args.model}")
    model = whisper.load_model(args.model)

    # 音声のロードと文字起こし
    print(f"Transcribing audio: {args.audio_path}")
    result = model.transcribe(args.audio_path, language=args.language)

    # 結果を表示
    print("\n=== Transcription Result ===")
    print(result["text"])

if __name__ == "__main__":
    main()
