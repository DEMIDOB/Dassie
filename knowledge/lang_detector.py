import textblob

from knowledge.request_context import RequestContext

cyrillic = {"а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
            "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"}
latin    = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"}


available_languages = {
    'ru': __import__('knowledge.ru').ru,
    'en': __import__('knowledge.en').en
}

available_languages_codes = {
    'ru', 'en'
}


def create_language_request_context(phrase, brain):
    lang = "ru"

    cyr_num = 0
    lat_num = 0

    for c in phrase:
        if c in cyrillic:
            cyr_num += 1
        elif c in latin:
            lat_num += 1


    if cyr_num >= lat_num:
        lang = "ru"
    elif len(available_languages) < 3:
        lang = "en"

    kn = available_languages[lang]
    ctx = RequestContext(input_text=phrase, brain=brain, answer_logical=dict(), sentence=[], kn=kn, lang_code=lang)

    return ctx

    # try:
    #     detected = textblob.TextBlob(phrase).detect_language()
    #     if detected not in available_languages:
    #         raise Exception(f"There is no such language: {detected}! Trying to use Russian.")
    #     else:
    #         lang = detected
    # except Exception as exc:
    #     lang = "en"
    #
    # return
