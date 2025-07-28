from fastapi import FastAPI, UploadFile, File, HTTPException
import cv2
import numpy as np
from deepface import DeepFace

app = FastAPI(title="Vision Service")

@app.post("/api/analyze/face")
async def analyze_face(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        resp = DeepFace.analyze(img, actions=['age', 'gender', 'emotion'], enforce_detection=False)
        return resp
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
