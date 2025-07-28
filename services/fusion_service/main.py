from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Fusion Service")

class FusionPayload(BaseModel):
    nlp_result: dict
    vision_result: dict
    audio_result: dict

@app.post("/api/fuse")
def fuse_results(payload: FusionPayload):
    combined_score = 0
    combined_score += payload.nlp_result.get("threat_score", 0)
    combined_score += payload.vision_result.get("threat_score", 0)
    combined_score += payload.audio_result.get("threat_score", 0)
    return {"combined_threat_score": combined_score / 3}
