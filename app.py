from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from googletrans import Translator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# Initialize ChatterBot
chatbot = ChatBot('RegionalBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")  # Train with English corpus

# Initialize Google Translator
translator = Translator()

# Supported languages
LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'ta': 'Tamil',
    'te': 'Telugu',
    'bn': 'Bengali',
    'mr': 'Marathi',
}

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    user_message = data['message']
    target_language = data['language']
    try:
        # Get response from ChatterBot
        response = str(chatbot.get_response(user_message))
        # Translate response to target language
        if target_language != 'en':
            translated = translator.translate(response, dest=target_language)
            response = translated.text
    except Exception as e:
        print(e)
        response = "Sorry, I couldn't process that."
    emit('response', {'response': response})

if __name__ == '__main__':
    socketio.run(app, debug=True, host='127.0.0.1', port=5000)
