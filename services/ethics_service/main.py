from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Ethics Service")

class DecisionPayload(BaseModel):
    action: str
    risk_score: float

@app.post("/api/decision")
def ethical_decision(payload: DecisionPayload):
    if payload.action == "lethal" and payload.risk_score < 0.9:
        return {"decision": "require_human_approval"}
    return {"decision": "auto_approve"}
