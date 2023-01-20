import openai
import speech_recognition as sr
import pyttsx3

# API key for OpenAI
openai.api_key = "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"

# Model engine to use for response generation
model_engine = "text-davinci-002"

def generate_response(prompt):
    """
    Generates a response for the given prompt using the OpenAI API.
    """
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
    """
    Listens for audio input and returns a text transcript of the spoken words.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        result2 = r.recognize_google(audio, show_all=True)
        if result2["final"]:
            command = result2["alternative"][0]["transcript"]
            return command
        else:
            print("Could not understand audio")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error requesting results from Google Speech Recognition service; {0}".format(e))

def speak(text):
    """
    Speaks the given text using the pyttsx3 library.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def run_smart_speaker():
    """
    Runs the smart speaker loop, listening for audio input and generating a response.
    """
    while True:
        command = listen()
        response = generate_response(command)
        print(response)
        speak(response)

# Start listening for audio input
print("listening...")
run_smart_speaker()
