#This program connects to a arduino running firmata to control it's wheels.

import pyfirmata2
import speech_recognition as sr
import pyttsx3
board = pyfirmata2.Arduino('COM3')
r = sr.Recognizer()


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


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
            wake = "hey jarvis"
            if MyText.count(wake) > 0:
                print(MyText)
                print("What can i do for you today?")
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                # Using google to recognize audio
                Command = r.recognize_google(audio2)
                Command = Command.lower()
                print(Command)
                if Command == "move forward":
                    board.digital[13].write(1)
                    board.digital[12].write(0)
                    board.digital[10].write(1)
                    board.digital[11].write(0)
                elif Command == "move backward":
                    board.digital[13].write(0)
                    board.digital[12].write(1)
                    board.digital[10].write(0)
                    board.digital[11].write(1)
                elif Command == "turn left":
                    board.digital[13].write(1)
                    board.digital[12].write(0)
                    board.digital[10].write(0)
                    board.digital[11].write(0)
                elif Command == "turn right":
                    board.digital[13].write(0)
                    board.digital[12].write(0)
                    board.digital[10].write(1)
                    board.digital[11].write(0)
                elif Command == "stop":
                    board.digital[13].write(0)
                    board.digital[12].write(0)
                    board.digital[10].write(0)
                    board.digital[11].write(0)
                    board.digital[9].write(0)
                    board.digital[8].write(0)
                elif Command == "shoot":
                    board.digital[9].write(1)
                    board.digital[8].write(0)
                else:
                    SpeakText("command is not known")
                    board.digital[13].write(0)
                    board.digital[12].write(0)
                    board.digital[10].write(0)
                    board.digital[11].write(0)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
