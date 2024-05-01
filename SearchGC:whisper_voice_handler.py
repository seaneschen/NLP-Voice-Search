'''
Handles voice input processing using OpenAI's Whisper model
'''
import whisper
class WhisperVoiceHandler:
    def __init__(self):
        # Load the appropriate Whisper model, ensure that the correct method is used
        self.model = whisper.load_model("base")  # This line previously caused an error
    def transcribe(self, voice_data):
        # Assuming voice_data is a file-like object with audio data
        result = self.model.transcribe(voice_data)
        return result['text']