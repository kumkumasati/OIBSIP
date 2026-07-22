"""
Voice Assistant - Beginner Tier
--------------------------------
A simple Python voice assistant that:
  1. Captures voice input via microphone (speech_recognition)
  2. Responds to greetings ("hello")
  3. Tells the current time and date
  4. Performs a web search on a spoken topic (opens the default browser)
  5. Handles unrecognized speech gracefully by asking the user to repeat
  6. Speaks every response back using text-to-speech (pyttsx3)

Run:
    python voice_assistant.py

Say "exit", "quit", or "stop" at any time to end the program.
"""

import datetime
import webbrowser
import sys

import speech_recognition as sr
import pyttsx3


# ---------------------------------------------------------------------------
# Text-to-Speech setup
# ---------------------------------------------------------------------------
engine = pyttsx3.init()

# Optional: tweak voice properties (rate, volume, voice index)
engine.setProperty("rate", 175)      # words per minute
engine.setProperty("volume", 1.0)    # 0.0 to 1.0

# Uncomment to list available voices and pick one:
# for i, voice in enumerate(engine.getProperty("voices")):
#     print(i, voice.name)
# engine.setProperty("voice", engine.getProperty("voices")[0].id)


def speak(text: str) -> None:
    """Speak the given text out loud and also print it to the console."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


# ---------------------------------------------------------------------------
# Speech recognition setup
# ---------------------------------------------------------------------------
recognizer = sr.Recognizer()

# Tune these if the assistant mishears you often:
recognizer.energy_threshold = 300       # microphone sensitivity
recognizer.pause_threshold = 0.8        # seconds of silence marking end of a phrase


def listen() -> str:
    """
    Capture audio from the default microphone and convert it to text.
    Returns an empty string if the speech could not be understood.
    """
    with sr.Microphone() as source:
        print("\nListening... (speak now)")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=6, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Could you please repeat that?")
            return ""

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        # Speech was unintelligible
        speak("Sorry, I didn't quite catch that. Could you please repeat?")
        return ""
    except sr.RequestError:
        # API was unreachable or unresponsive
        speak("I'm having trouble reaching the speech recognition service. "
              "Please check your internet connection.")
        return ""


# ---------------------------------------------------------------------------
# Command handlers
# ---------------------------------------------------------------------------
def handle_greeting():
    speak("Hello there! How can I help you today?")


def handle_time():
    now = datetime.datetime.now()
    speak(f"The current time is {now.strftime('%I:%M %p')}.")


def handle_date():
    now = datetime.datetime.now()
    speak(f"Today's date is {now.strftime('%A, %B %d, %Y')}.")


def handle_search(command: str):
    # Strip common trigger phrases to isolate the search topic
    triggers = ["search for", "search", "look up", "google"]
    query = command
    for trigger in triggers:
        if trigger in query:
            query = query.split(trigger, 1)[1].strip()
            break

    if not query:
        speak("What would you like me to search for?")
        query = listen()
        if not query:
            return

    speak(f"Searching the web for {query}.")
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)


def handle_unknown():
    speak("I'm not sure how to help with that yet. "
          "You can ask me to say hello, tell you the time or date, "
          "or search something on the web.")


# ---------------------------------------------------------------------------
# Main command router
# ---------------------------------------------------------------------------
def process_command(command: str) -> bool:
    """
    Decide what to do based on the recognized command.
    Returns False if the assistant should stop running, True otherwise.
    """
    if not command:
        # Nothing understood; listen() already asked the user to repeat.
        return True

    if any(word in command for word in ["exit", "quit", "stop", "goodbye"]):
        speak("Goodbye! Have a great day.")
        return False

    if "hello" in command or "hi " in command or command.strip() == "hi":
        handle_greeting()
    elif "time" in command:
        handle_time()
    elif "date" in command or "day is it" in command:
        handle_date()
    elif any(word in command for word in ["search", "look up", "google"]):
        handle_search(command)
    else:
        handle_unknown()

    return True


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main():
    speak("Voice assistant activated. Say 'exit' at any time to quit.")

    running = True
    while running:
        try:
            command = listen()
            running = process_command(command)
        except KeyboardInterrupt:
            speak("Shutting down. Goodbye!")
            sys.exit(0)


if __name__ == "__main__":
    main()
