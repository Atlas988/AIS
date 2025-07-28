from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import uuid
import os

app = FastAPI(title="Ingestion Service")

DATA_DIR = "data/ingestion"
os.makedirs(DATA_DIR, exist_ok=True)

class IngestPayload(BaseModel):
    source: str
    timestamp: str

@app.post("/api/ingest")
async def ingest_data(payload: IngestPayload, file: UploadFile = File(...)):
    try:
        file_id = str(uuid.uuid4())
        file_path = os.path.join(DATA_DIR, f"{file_id}_{file.filename}")
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        return {"status": "success", "file_id": file_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
