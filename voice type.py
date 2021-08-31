import speech_recognition as sr
import pyautogui
import pyttsx3

while True:
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def talk(text):
        engine.say(text)
        engine.runAndWait()

    try:
        with sr.Microphone() as source:
            print('Listening ...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            
            if ('type' in command) :
                cmnd = command.replace('type', '')
                print(command)
                pyautogui.write(cmnd)


    except:
        pass
