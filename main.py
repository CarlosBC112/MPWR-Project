from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from deepgram import Deepgram
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
claude = ChatAnthropic(api_key=ANTHROPIC_API_KEY, model="claude-sonnet-4-20250514")

DG_API_KEY = os.getenv("DG_API_KEY")
dg_client = Deepgram(DG_API_KEY)

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat/")
async def chat(file: UploadFile = File(...)):
    """Process audio file and return AI response"""
    try:
        # Read the uploaded file into memory
        audio_bytes = await file.read()

        # Send audio to Deepgram for transcription
        response = await dg_client.transcription.prerecorded(
            {"buffer": audio_bytes, "mimetype": file.content_type},
            {"punctuate": True}
        )
        transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]

        # Use Claude to respond to the transcript
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI assistant. Keep responses conversational and concise."),
            ("human", "{user_input}")
        ])
        chain = prompt | claude
        result = chain.invoke({"user_input": transcript})

        return JSONResponse({
            "transcript": transcript,
            "response": result.content,
            "success": True
        })
    except Exception as e:
        return JSONResponse({
            "error": str(e),
            "success": False
        }, status_code=500)

# Serve static files (frontend) - MUST be last
app.mount("/", StaticFiles(directory=".", html=True), name="static")









