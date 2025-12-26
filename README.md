# MPWR Project - AI Voice Chat Assistant

A modern, user-friendly FastAPI application that enables voice conversations with Claude AI. Simply speak into your microphone, and the app transcribes your audio using Deepgram, sends it to Claude for intelligent responses, and displays everything in a beautiful chat interface.

## Features

- 🎤 **Voice Recording** - Record audio directly from your browser
- 🔊 **Deepgram Transcription** - Convert speech to text with high accuracy
- 🤖 **Claude AI Integration** - Get intelligent, conversational responses
- 💬 **Chat Interface** - Beautiful, modern chat UI with message history
- ⚡ **Real-time Processing** - Fast transcription and AI responses
- 🎨 **Responsive Design** - Works on desktop and mobile browsers

## Project Structure

```
MPWR-Project/
├── main.py          # Backend API (FastAPI)
├── index.html       # Frontend UI
├── app.js           # Frontend JavaScript logic
├── pyproject.toml   # Python dependencies
└── README.md        # This file
```

## Prerequisites

- Python 3.13+
- Deepgram API Key
- Anthropic API Key
- UV package manager

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/CarlosBC112/MPWR-Project.git
cd MPWR-Project
```

### 2. Create Virtual Environment

```bash
uv venv
```

### 3. Install Dependencies

```bash
uv sync
```

### 4. Create `.env` File

Create a `.env` file in the project root with your API keys:

```
DG_API_KEY=your_deepgram_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

You can get these keys from:
- **Deepgram**: https://console.deepgram.com/
- **Anthropic**: https://console.anthropic.com/

### 5. Run the Application

```bash
uv run uvicorn main:app --reload
```

The app will start on **http://127.0.0.1:8000**

## Usage

1. Open http://127.0.0.1:8000 in your browser
2. Allow microphone access when prompted
3. Click the 🎤 microphone button to start recording
4. Speak your message
5. Click the button again or wait for it to stop recording
6. The app will transcribe your speech and get a response from Claude
7. View the conversation in the chat interface

## Architecture

### Frontend (`index.html` + `app.js`)
- Modern chat interface with gradient styling
- Web Audio API for microphone recording
- Real-time message display
- Loading states and error handling

### Backend (`main.py`)
- FastAPI REST API
- `/chat/` endpoint - Accepts audio files and returns transcribed text + AI response
- CORS enabled for cross-origin requests
- Static file serving for frontend files

## API Endpoints

### `POST /chat/`

**Description**: Transcribe audio and get AI response

**Request**:
- Form data with `file` field containing audio blob (audio/webm)

**Response**:
```json
{
  "success": true,
  "transcript": "User's spoken message",
  "response": "Claude's AI response"
}
```

## Dependencies

- **fastapi** - Web framework
- **uvicorn** - ASGI server
- **deepgram-sdk** - Speech-to-text
- **anthropic** - Claude AI
- **langchain** & **langchain-anthropic** - LLM framework
- **python-dotenv** - Environment variables
- **python-multipart** - File upload handling

## Troubleshooting

**Microphone not working?**
- Ensure your browser has microphone permissions
- Check that your OS hasn't blocked microphone access

**API not responding?**
- Verify your API keys are correct in `.env`
- Check that the server is running (`uv run uvicorn main:app --reload`)

**Audio not transcribing?**
- Ensure your audio is clear and not too quiet
- Deepgram works best with WAV/WebM formats

## License






