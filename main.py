import webbrowser

import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init()


def sayToMe(talk):
    engine.say(talk)
    engine.runAndWait()


sayToMe("Добрый день! Все функции работают стабильно")
sayToMe("Скажите что-нибудь")

record = sr.Recognizer()
try:
    with sr.Microphone(device_index=1) as source:
        print("Говорите...")
        audio = record.listen(source)

        result = record.recognize_google(audio, language="ru-RU")
        result = result.lower()
        print(result)

        match result:
            case "какое сейчас время":
                now = datetime.datetime.now()
                present_time = str("Сейчас {}:{}".format(str(now.hour), str(now.minute)))
                print(present_time)
                sayToMe(present_time)
            case 'открой браузер':
                webbrowser.open("https://ya.ru")
            case _:
                sayToMe("Вы не сказали команду. Всего доброго!")


except sr.UnknownValueError:
    print("ERROR: The voice was not recognized")
except sr.RequestError:
    print("ERROR: Something was wrong")



