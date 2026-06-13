from fastapi import FastAPI
from pydantic import BaseModel

from app.cleaner import TranscriptCleaner


app = FastAPI(
    title="Transcript Cleaning Pipeline",
    description="NLP based transcript preprocessing system",
    version="1.0"
)


cleaner = TranscriptCleaner()



class TranscriptRequest(BaseModel):

    text: str



class TranscriptResponse(BaseModel):

    original: str
    cleaned: str



@app.get("/")
def home():

    return {
        "message": "Transcript Cleaning API Running"
    }



@app.post("/clean", response_model=TranscriptResponse)
def clean_transcript(
        request: TranscriptRequest
):

    cleaned_text = cleaner.clean(
        request.text
    )


    return {
        "original": request.text,
        "cleaned": cleaned_text
    }