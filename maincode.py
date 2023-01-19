import openai
import speech_recognition as sr
import pyttsx3

openai.api_key = "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"
model_engine = "text-davinci-002"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error requesting results from Google Speech Recognition service; {0}".format(e))

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def run_smart_speaker():
    while True:
        command = listen()
        response = generate_response(command)
        speak(response)
print("listening...")
run_smart_speaker()


