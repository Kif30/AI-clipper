import whisper

# load model (tiny = fast, medium/large = more accurate)
model = whisper.load_model("small")

# transcribe video
result = model.transcribe("C:\\Users\\syeda\\OneDrive\\Desktop\\projects\\ai clipper\AI-clipper\\videoplayback.mp4")

# print the text
print(result["text"])
