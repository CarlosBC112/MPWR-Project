from email import message

from fastapi import FastAPI, Form,File,UploadFile
import os, asyncio
from deepgram import Deepgram
from dotenv import load_dotenv
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Union

from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate


load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
claude = ChatAnthropic(api_key=ANTHROPIC_API_KEY,  model="claude-sonnet-4-20250514")
print("Claude API Key starts with:", ANTHROPIC_API_KEY[:10])
print("Model:", "claude-3-sonnet")
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
            <h2>Ask a question</h2>
            <form action="/submit" method="post">
                <input type="text" name="question" placeholder="Type your question here" />
                <input type="submit" value="Submit" />
            </form>
            <h2>Upload an audio file for transcription</h2>
            <form action="/transcribe/" method="post" enctype="multipart/form-data">
                <input type="file" name="file" />
                <input type="submit" value="Upload & Transcribe" />
            
            </form>
        </body>
    </html>
    """
@app.post("/submit")
def submit_form(question: str = Form(...)):
    return {"your_question": question}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


#Defines a PYdantic Model for data validation
class Item(BaseModel):
    name: str
    price:float
    in_stock:bool


@app.post("/items/")
def create_item(item: Item):
    return{
        "message": "Item received!",
        "item": item.dict()

    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


