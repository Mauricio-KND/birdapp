from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import librosa
import os

app = FastAPI(
    title="birdapp API",
    description="Identify bird species from audio clips (soon with image support)",
    version="0.1.0"
)

@app.post("/identify-bird/")
async def identify_bird(audio: UploadFile = File(...)):
    temp_path = None  # Initialize variable outside try block
    try:
        # Validate file type
        if not audio.filename.endswith(('.wav', '.mp3')):
            raise HTTPException(status_code=400, detail="Only WAV/MP3 files allowed")
        
        temp_path = "temp_audio.wav"
        with open(temp_path, "wb") as buffer:
            buffer.write(await audio.read())
        
        waveform, sr = librosa.load(temp_path, sr=16000)
        duration = librosa.get_duration(y=waveform, sr=sr)
        
        return JSONResponse({
            "species": "Erithacus rubecula (European Robin)",
            "confidence": 0.92,
            "duration_seconds": round(duration, 2)
        })
    
    except HTTPException:
        # Re-raise HTTP exceptions (like 400 errors) without 500 wrapping
        raise
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)  # Clean up