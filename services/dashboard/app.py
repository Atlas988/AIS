from fastapi import FastAPI

app = FastAPI(title="Dashboard")

@app.get("/")
def root():
    return {"message": "Dashboard placeholder"}
