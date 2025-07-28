from fastapi import FastAPI

app = FastAPI(title="Audio Service")

@app.get("/")
def root():
    return {"message": "Audio Service placeholder"}
