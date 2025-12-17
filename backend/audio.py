import subprocess
from pathlib import Path

AUDIO_DIR = Path("uploads/audio")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

def extract_audio(video_path: Path) -> Path:
    audio_path = AUDIO_DIR / f"{video_path.stem}.wav"

    cmd = [
        "ffmpeg",
        "-i", str(video_path),
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        str(audio_path)
    ]

    subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True
    )

    return audio_path
