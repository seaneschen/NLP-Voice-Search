'''
Flask application setup and routes for the NLM powered search processor
'''
from flask import Flask, render_template, request, jsonify
from gpt_search_processor import GPTSearchProcessor
from whisper_voice_handler import WhisperVoiceHandler
from api_key_manager import APIKeyManager
app = Flask(__name__)
# Initialize the processor and handler with the API key manager
api_key_manager = APIKeyManager()
gpt_processor = GPTSearchProcessor(api_key_manager)
whisper_handler = WhisperVoiceHandler()
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = gpt_processor.query(query)
    return jsonify(results)
@app.route('/voice_search', methods=['POST'])
def voice_search():
    voice_data = request.files['voice_input']
    text_query = whisper_handler.transcribe(voice_data)
    return jsonify({'query': text_query})
@app.route('/api_key', methods=['POST'])
def api_key():
    key = request.form['api_key']
    valid = api_key_manager.validate_key(key)
    if valid:
        api_key_manager.input_key(key)
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid API key'})
if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')  # ssl_context='adhoc' will create a self-signed certificate