import requests
import os

# Load Deepgram API key from environment variables
DEEPGRAM_API_KEY = 'ccd9b8871e5d69219d70f63404807ebd7466b822'

def transcribe_audio(audio_url):
    """
    Sends an audio file URL to Deepgram for transcription.
    """
    headers = {
        "Authorization": f"Token {DEEPGRAM_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {"url": audio_url, "punctuate": True}
    
    response = requests.post("https://api.deepgram.com/v1/listen", headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to transcribe audio. Status Code: {response.status_code}"}
