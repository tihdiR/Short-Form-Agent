# tts_client.py
import os
from elevenlabs import ElevenLabs
from dotenv import load_dotenv

load_dotenv() 

#voices = ["Adam", "Antoni", "Arnold", "Bella", "Domi", "Elli", "Josh", "Rachel", "Sam"]

class TTSClient:
    def __init__(self, voice_id="cgSgspJ2msm6clMCkdW9"):
        self.client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
        self.voice_id = voice_id

    def generate_audio_with_timing(self, text: str):
        response = self.client.text_to_speech.convert_with_timestamps(
            voice_id=self.voice_id,
            text=text,
            model_id = "eleven_flash_v2_5",
            voice_settings={
                "speed":1.2 
            }
        )
        return response
