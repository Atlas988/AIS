from fastapi import FastAPI

app = FastAPI(title="Reasoning Service")

@app.get("/")
def root():
    return {"message": "Reasoning Service placeholder"}
