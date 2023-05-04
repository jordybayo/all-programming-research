import speech_recognition as sr
import pyttsx3
#install sudo apt install python-espeak


print( sr.__version__)
print(sr.Microphone.list_microphone_names())

r = sr.Recognizer()
mic = sr.Microphone(device_index=0,)


def go():
    with mic as source:
        audio = r.listen(source)

        speech_text = r.recognize_google(audio)
        print(speech_text)

        speak(speech_text)

    go()


def speak(message):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-10)
    engine.say('i see a {}'.format(message))
    engine.runAndWait()

go()




