import textblob


available_languages = {
    'ru': __import__('knowledge.ru').ru
}


def detect(phrase):
    lang = "ru"
    try:
        detected = textblob.TextBlob(phrase).detect_language()
        if detected not in available_languages:
            raise Exception(f"There is no such language: {detected}! Trying to use Russian.")
        else:
            lang = detected
    except Exception as exc:
        print(exc)

    return available_languages[lang]
