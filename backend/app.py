from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import shutil

from audio import extract_audio

app = FastAPI()

VIDEO_DIR = Path("uploads/videos")
VIDEO_DIR.mkdir(parents=True, exist_ok=True)

@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    video_path = VIDEO_DIR / file.filename

    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    audio_path = extract_audio(video_path)

    return {
        "status": "uploaded",
        "video": video_path.name,
        "audio": audio_path.name
    }
