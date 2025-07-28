from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="NLP Service")

class TextPayload(BaseModel):
    text: str

ner = pipeline("ner", grouped_entities=True)

@app.post("/api/analyze/ner")
def analyze_ner(payload: TextPayload):
    entities = ner(payload.text)
    return {"entities": entities}
