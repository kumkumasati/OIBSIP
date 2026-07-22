# Python Voice Assistant (Beginner Tier)

A simple voice-controlled assistant that listens through your microphone and
responds out loud. It can greet you, tell the time/date, search the web on a
spoken topic, and asks you to repeat yourself if it mishears you.

## Project Structure

```
voice_assistant/
├── voice_assistant.py   # main program
├── requirements.txt     # Python dependencies
└── README.md            # this file
```

## Features

- 🎙️ Captures voice input from your microphone (`speech_recognition`)
- 👋 Responds to "hello" with a greeting
- 🕒 Tells the current time and date
- 🔍 Searches the web for a topic you say out loud (opens your browser)
- 🔁 Asks you to repeat if it doesn't understand you
- 🔊 Speaks every response using text-to-speech (`pyttsx3`)

## Requirements

- Python 3.9–3.12 (recommended)
- A working microphone
- An internet connection (Google's free speech-recognition API is used
  under the hood by the `speech_recognition` library)

## Setup Instructions

### 1. Install Python
Download and install Python from https://www.python.org/downloads/ if you
don't already have it. Confirm it's installed:

```bash
python --version
```

### 2. Get the project files
Place `voice_assistant.py`, `requirements.txt`, and this `README.md` in a
folder on your computer (you already have this from the download).

### 3. Create a virtual environment (recommended)

```bash
cd voice_assistant
python -m venv venv
```

Activate it:

- **Windows (PowerShell):**
  ```powershell
  venv\Scripts\Activate.ps1
  ```
- **Windows (cmd.exe):**
  ```cmd
  venv\Scripts\activate.bat
  ```
- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install system audio dependencies

`PyAudio` (needed for microphone access) requires some system-level
libraries before `pip install` will succeed.

- **Windows:**
  Usually installs fine directly via pip (see step 5). If it fails, install
  the prebuilt wheel:
  ```powershell
  pip install pipwin
  pipwin install pyaudio
  ```

- **macOS:**
  ```bash
  brew install portaudio
  ```

- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt-get update
  sudo apt-get install python3-pyaudio portaudio19-dev espeak
  ```
  (`espeak` provides the offline TTS voice that `pyttsx3` uses on Linux.)

### 5. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the assistant

```bash
python voice_assistant.py
```

You should hear: *"Voice assistant activated. Say 'exit' at any time to
quit."* Then try saying:

- "Hello"
- "What time is it?"
- "What's today's date?"
- "Search for best pizza recipes"
- "Exit" (to quit)

## Troubleshooting

| Problem | Fix |
|---|---|
| `pyaudio` fails to install | Follow the OS-specific step 4 above; on Windows try `pipwin install pyaudio`. |
| No sound / TTS not speaking | macOS/Windows use built-in TTS voices automatically. On Linux, make sure `espeak` is installed. |
| "Could not understand audio" every time | Speak clearly and check your mic is set as the default input device in your OS sound settings. Try increasing mic volume. |
| `RequestError` from speech_recognition | Check your internet connection — Google's free recognition API needs it. |
| Wrong microphone used | List available mics with the snippet below and set the index explicitly. |

To find and select a specific microphone:

```python
import speech_recognition as sr
print(sr.Microphone.list_microphone_names())
# Then use: sr.Microphone(device_index=<index>)
```

## Next Steps (Advanced Tier Ideas)

Want to extend this into the advanced build? Consider adding:
- **NLP intent parsing** with `nltk` or a `transformers` model instead of
  simple keyword matching
- **Weather API integration** (e.g., OpenWeatherMap) for "what's the
  weather like" queries
- **Email support** via `smtplib` to send messages by voice
- **Smart home integration** (e.g., Philips Hue, Home Assistant API) to
  control lights/devices by voice command

Each of these can be added as new handler functions and routed through
`process_command()` in `voice_assistant.py`.
