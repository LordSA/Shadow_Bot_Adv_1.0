import openai
import speech_recognition as sr
from gtts import gTTS
import os
import time

# Set your OpenAI API key here
openai.api_key = "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"

def ask_gpt3(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to Shadow AI Voice Assistant!")
    print("Listening...")

    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            try:
                audio = recognizer.listen(source, timeout=5)
                user_input = recognizer.recognize_google(audio)
                print("You said:", user_input)

                if "goodbye" in user_input:
                    print("Shadow: Goodbye!")
                    tts = gTTS("Goodbye!")
                    tts.save("output.mp3")
                    os.system("mpg321 output.mp3")
                    break

                assistant_response = ask_gpt3(user_input)
                print("Shadow:", assistant_response)

                tts = gTTS(assistant_response)
                tts.save("output.mp3")
                os.system("mpg321 output.mp3")

                print("Listening...")
            except sr.UnknownValueError:
                print("Listening...")
                continue
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    main()
