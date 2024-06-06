import pyfirmata2
import pywhatkit
import speech_recognition as sr
import pyttsx3

import openai

openai.api_key = 'Your api key'
messages = [{"role": "system", "content": "You are a intelligent assistant."}]

wake = "hey jarvis"
light_conditions = ["on", "off"]

# from time import sleep

board = pyfirmata2.Arduino('COM3')

ledPin = board.get_pin('d:11:p')
# Initialize the recognizer
r = sr.Recognizer()

sw = ["what is", "define"]


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()



def search_chatgpt(command):
    if command:
        messages.append(
            {"role": "user", "content": Command},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})


# Loop infinitely for user to
# speak

while 1:

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            if MyText.count(wake) > 0:
                print(MyText)
                print("What can i do for you today?")
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                # Using google to recognize audio
                Command = r.recognize_google(audio2)
                Command = Command.lower()
                print(Command)
                if Command == "lamp on":
                    ledPin.write(5)
                    SpeakText("Ok sir turning lamp on")

                elif Command == "lamp off":
                    ledPin.write(0)
                    SpeakText("Ok sir turning lamp off")
                elif "what is" in Command:
                    print("hello")
                    search_chatgpt(Command)
                elif "play" in Command:
                    song = Command[Command.index("play")+2:]
                    pywhatkit.playonyt(song)

                else:
                    print("Command not recognized")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
