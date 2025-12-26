// Frontend JavaScript for AI Voice Chat
let mediaRecorder;
let audioChunks = [];
let isRecording = false;

const recordBtn = document.getElementById('recordBtn');
const status = document.getElementById('status');
const chatMessages = document.getElementById('chatMessages');

// API endpoint
const API_URL = 'http://127.0.0.1:8000';

recordBtn.addEventListener('click', toggleRecording);

async function toggleRecording() {
    if (!isRecording) {
        await startRecording();
    } else {
        stopRecording();
    }
}

async function startRecording() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];
        
        mediaRecorder.ondataavailable = (event) => {
            audioChunks.push(event.data);
        };
        
        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
            await sendAudio(audioBlob);
            stream.getTracks().forEach(track => track.stop());
        };
        
        mediaRecorder.start();
        isRecording = true;
        recordBtn.classList.add('recording');
        recordBtn.textContent = '⏹️';
        status.textContent = 'Recording... Click to stop';
        status.classList.add('recording');
    } catch (error) {
        console.error('Error accessing microphone:', error);
        status.textContent = 'Microphone access denied';
    }
}

function stopRecording() {
    if (mediaRecorder && isRecording) {
        mediaRecorder.stop();
        isRecording = false;
        recordBtn.classList.remove('recording');
        recordBtn.textContent = '🎤';
        status.innerHTML = 'Processing... <span class="loading"></span>';
        status.classList.remove('recording');
    }
}

async function sendAudio(audioBlob) {
    const formData = new FormData();
    formData.append('file', audioBlob, 'audio.webm');
    
    try {
        const response = await fetch(`${API_URL}/chat/`, {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.success) {
            addMessage('user', data.transcript);
            addMessage('ai', data.response);
            status.textContent = 'Click to speak';
        } else {
            status.textContent = 'Error: ' + (data.error || 'Unknown error');
        }
    } catch (error) {
        console.error('Error:', error);
        status.textContent = 'Error sending audio';
    }
}

function addMessage(type, content) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    
    const label = document.createElement('div');
    label.className = 'message-label';
    label.textContent = type === 'user' ? 'You' : 'AI Assistant';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.textContent = content;
    
    messageDiv.appendChild(label);
    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
