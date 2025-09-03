from services.whisper_service import transcribe_audio

text = transcribe_audio("whisper/kaisatsu.m4a", language="ja")
print(text)
