from email import message

from fastapi import FastAPI, Form,File,UploadFile
import os
from deepgram import Deepgram
from dotenv import load_dotenv
from fastapi.responses import HTMLResponse
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
claude = ChatAnthropic(api_key=ANTHROPIC_API_KEY,  model="claude-sonnet-4-20250514")

DG_API_KEY = os.getenv("DG_API_KEY")

dg_client = Deepgram(DG_API_KEY)

app = FastAPI()
@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
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
        ("system", "You are a helpful AI assistant."),
        ("human", "{user_input}")
    ])
    chain = prompt | claude
    result = chain.invoke({"user_input": transcript})

    return {"transcript": transcript,
            "response": result.content
        }

# Simple HTML form at "/form"
#I made this the root, so when the user opens up the page
#They have access to the transcriber
@app.get("/", response_class=HTMLResponse)
def form_page():
    return """
    <html>
        <body>
            
            <h2>Upload an audio file for transcription</h2>
            <form action="/transcribe/" method="post" enctype="multipart/form-data">
                <input type="file" name="file" />
                <input type="submit" value="Upload & Transcribe" />
            
            </form>
        </body>
    </html>
    """









