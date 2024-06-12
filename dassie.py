# Dassie — v0.7
# Global redesign
import os

from gtts import gTTS
from playsound import playsound
# import pyttsx3 as pt3
import speech_recognition as sr

from sessions import sessions_manager
from knowledge.lang_detector import available_languages_codes

import knowledge.static as knst

session_id = sessions_manager.create_session()

voice_answers = True


def say(phrase: str, slow=False):
    gtts_i = gTTS(text=phrase, lang="ru", slow=slow)
    gtts_i.save("tmp.wav")
    playsound("tmp.wav")
    os.remove("tmp.wav")


def get_lang_voices():
    engine = pt3.init()

    ret = {}
    to_find = available_languages_codes.copy()

    for v in engine.getProperty("voices"):
        lang = ""
        for l in v.languages:
            lang += l.lower()
        for tgt in to_find:
            if tgt in lang:
                ret[tgt] = v.id
                to_find.remove(tgt)
                break

    return ret


if __name__ == '__main__':
    # initialize the voice system
    # if voice_answers:
    #     voices = get_lang_voices()
    #     voice = pt3.init()
    # else:
    #     voices = None
    #     voice = None

    r = sr.Recognizer()

    wanna_sleep = False
    while True or not wanna_sleep:
        try:
            with sr.Microphone() as source:
                print("Дасси >> Слушаю...")
                audio = r.listen(source, phrase_time_limit=7)
                inp = r.recognize_google(audio, language="ru-RU")
                print("   Вы >>", inp)

            # inp = input("   Вы >> ")
            reply = sessions_manager.reply(session_id, inp)
            if reply.silent_response:
                continue

            answer, lang = reply.response, reply.lang_code
            wanna_sleep = reply.brain.wanna_sleep
            print("Дасси >>", answer)
            if voice_answers:
                # voice.setProperty('voice', voices[lang])
                answer_no_pm = ""
                # clear all the punctuation marks
                for c in answer.lower():
                    if c not in knst.punct_marks:
                        answer_no_pm += c
                # voice.say(answer_no_pm)
                # voice.runAndWait()
                say(answer_no_pm)
        except sr.exceptions.UnknownValueError as exc:
            continue
        except Exception as exc:
            print("Сорян, зафакапил...", exc)

