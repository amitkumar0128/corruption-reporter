from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
  return f"This is Home Page!!!"
