from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

   
@app.post("/upload/")
async def upload_audio_file(file: UploadFile = File(...)):
    # Save the uploaded file
    with open(f"uploaded_{file.filename}", "wb") as buffer:
        buffer.write(file.file.read())
    
    return {"filename": file.filename}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)