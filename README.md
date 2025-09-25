# MPWR Project - FastAPI + Deepgram + Claude

This project is a simple FastAPI app that:
- Accepts audio files
- Transcribes them using **Deepgram**.
- Sends the transcript to **Claude (Anthropic)** and returns an AI-generated response.
- Provides a small demo web form for file uploads.
  
Download Pycharm, it is an IDE for python

Create a new Project with FastAPI, a Custom Environment for the Interpreter type, and UV as the type:

in the terminal write git clone https://github.com/CarlosBC112/MPWR-Project.git

replace your main.py file with the one you just copied as well as create a new file called .env, this is where you will place your API keys
DG_API_KEY=your_deepgram_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

write these commands 
uv venv
uv add fastapi "uvicorn[standard]" python-multipart python-dotenv
uv add langchain langchain-anthropic anthropic
uv add "deepgram-sdk==2.12.0"   

Click run and open 
http://127.0.0.1:8000





