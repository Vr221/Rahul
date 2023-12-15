import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import webbrowser

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"Command: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def main():
    speak("Hello! How can I assist you today?")
    
    while True:
        command = get_command()

        if command:
            if "hello" in command:
                speak("Hello! How can I help you?")
            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}")
            elif "date" in command:
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                speak(f"Today's date is {current_date}")
            elif "search" in command:
                query = command.replace("search", "").strip()
                speak(f"Searching the web for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            elif "exit" in command or "bye" in command:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
