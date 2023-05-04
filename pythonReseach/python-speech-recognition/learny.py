import speech_recognition as sr
print( sr.__version__)

r = sr.Recognizer()

harvard = sr.AudioFile('audio_files/harvard.wav')

with harvard as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.record(source,)


print(r.recognize_google(audio, language='en-US'))

