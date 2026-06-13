from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.logger import logger
from app.cleaner import TranscriptCleaner


app = FastAPI(
    title="Transcript Cleaning Pipeline",
    description="NLP based transcript preprocessing system",
    version="1.0"
)


cleaner = TranscriptCleaner()



class TranscriptRequest(BaseModel):

    text: str = Field(
        ...,
        min_length=1,
        description="Transcript text to clean"
    )

class TranscriptResponse(BaseModel):

    original: str
    cleaned: str



@app.get("/")
def home():

    return {
        "message": "Transcript Cleaning API Running"
    }



@app.post("/clean", response_model=TranscriptResponse)
def clean_transcript(request: TranscriptRequest):

    logger.info("Cleaning request received")


    if not request.text.strip():

        logger.error("Empty transcript received")

        raise HTTPException(
            status_code=400,
            detail="Transcript cannot be empty"
        )


    cleaned_text = cleaner.clean(request.text)


    logger.info("Cleaning completed successfully")


    return {
        "original": request.text,
        "cleaned": cleaned_text
    }