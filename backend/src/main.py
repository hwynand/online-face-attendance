from fastapi import FastAPI

app = FastAPI(title="Online Face Attendance")

@app.get('/')
async def hello():
    return "hello from face attendance system"
