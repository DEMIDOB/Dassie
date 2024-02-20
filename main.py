# Dassie — v0.6
# Global redesign

import pyttsx3 as pt3

from sessions import sessions_manager
from knowledge.lang_detector import available_languages_codes

session_id = sessions_manager.create_session()

voice_answers = True


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
    if voice_answers:
        voices = get_lang_voices()
        voice = pt3.init()
    else:
        voices = None
        voice = None

    wanna_sleep = False
    while not wanna_sleep:
        inp = input("   Вы >> ")
        reply = sessions_manager.reply(session_id, inp)
        answer, lang = reply['answer']
        wanna_sleep = reply['sleep']
        print("Дасси >>", answer)
        if voice_answers:
            voice.setProperty('voice', voices[lang])
            voice.say(answer)
            voice.runAndWait()
