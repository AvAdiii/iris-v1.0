import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize Text-to-Speech engine
tts_engine = pyttsx3.init()

def speak(text):
    """Speak the provided text."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listen for user input and return recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)  # Adjusted timeout
            print("Processing...")
            # Recognize speech using Google Web Speech API
            command = recognizer.recognize_google(audio)
            return command
        except sr.UnknownValueError:
            print("I didn't understand that.")
            return None
        except sr.RequestError as e:
            print(f"Recognizer error: {e}")
            return None
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
            return None

if __name__ == "__main__":
    speak("Initializing IRIS version 1.0")
    print("IRIS is ready. Say something!")

    while True:
        command = listen()  # Get command from microphone
        if command:
            print(f"You said: {command}")
            if "exit" in command.lower():
                speak("Goodbye!")
                break
            elif "search" in command.lower():
                speak("What should I search for?")
                search_query = listen()
                if search_query:
                    url = f"https://www.google.com/search?q={search_query}"
                    speak(f"Searching for {search_query}")
                    webbrowser.open(url)
            else:
                speak("I didn't understand that command.")
