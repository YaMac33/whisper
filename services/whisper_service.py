# services/whisper_service.py
# Whisperを使った文字起こし処理を関数として提供するモジュール

import whisper

# モデルは一度だけロードして再利用
_model = whisper.load_model("small")

def transcribe_audio(audio_path: str, language: str = "ja") -> str:
    """
    指定した音声ファイルをWhisperで文字起こしする関数

    Args:
        audio_path (str): 音声ファイルのパス
        language (str): 言語コード（例: "ja", "en"）
    
    Returns:
        str: 文字起こし結果のテキスト
    """
    result = _model.transcribe(audio_path, language=language)
    return result["text"]