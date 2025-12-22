# transcribe.py
import whisper
from pathlib import Path

print("Loading Whisper model ONCE...")
model = whisper.load_model("tiny")  # 🔥 USE TINY

def transcribe_audio(audio_path: Path):
    result = model.transcribe(
        str(audio_path),
        fp16=False,
        verbose=False
    )

    return [
        {
            "start": float(s["start"]),
            "end": float(s["end"]),
            "text": s["text"].strip()
        }
        for s in result["segments"]
    ]
