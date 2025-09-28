# JERRY-VOICE-ASSISTANT

import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary  

recognizer = sr.Recognizer()

def speak(text):
    print(f"Jerry: {text}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()


def process_command(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif command.startswith("play"):
        song_title = command.replace("play", "").strip().lower()
        found = False
        for key in musicLibrary.music:
            if song_title in key.lower():
                link = musicLibrary.music[key]
                webbrowser.open(link)
                speak(f"Playing {key}")
                found = True
                break
        if not found:
            speak("Sorry, I couldn't find that song in the library.")

    elif "now exit" in command or "now stop" in command:
        speak("Goodbye sir, see you again.")
        return "exit"

    else:
        speak("Sorry, I didn't understand that.")


def main():
    time.sleep(1)
    speak("Jerry is now active. How can I assist you?")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=3)

            activation = recognizer.recognize_google(audio)
            print(f"You said: {activation}")

            if "jerry" in activation.lower():
                speak("Yes sir")
                with sr.Microphone() as source:
                    print("Listening to the command...")
                    command_audio = recognizer.listen(source, timeout=4, phrase_time_limit=3)

                try:
                    command = recognizer.recognize_google(command_audio)
                    print(f"Command: {command}")
                    if process_command(command) == "exit":
                        break
                except sr.UnknownValueError:
                    speak("Sorry, I could not understand the command.")

        except Exception as e:
            print(f"[Error]: {e}")


if __name__ == "__main__":
    main()

