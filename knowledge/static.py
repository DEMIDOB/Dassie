import knowledge.muscles as muscles

ext_cats = ()

categories = ("goingon_phrase", "laugh", "bro_phrases", "hello_phrases", "catch_phrases", "clear_word", "mood_word", "whatdoing_words", "how_word", "whatsup_phrases", "you_word", "youknow_word", "welldone_phrases", "baddone_phrases", "drive_word", "watching_word", "speech_phrases", "joke_phrases", "song_phrases", "weather_words", "google_search", "news_get", "kate_word", "who_word", "ivan_word", "tim_word", "mary_word", "not_particle", "goodbye_phrases", "still_word", "dating_word") + tuple(ext_cats) # translate was after news
else_cates = ("joke_phrases", "song_phrases", "weather_words", "speech_phrases")
service_cates = ("who_word", "how_word", "not_particle", "still_word")

polite_words = ("пожалуйста", "спасибо", "благодарю", "благодарствую")

laugh_combinations = ("зах", "пхаах", "ах", "хха", "пх", "пха")

exit_indexes = (categories.index("goodbye_phrases"), categories.index("dating_word"))

punct_marks = (".", ",", "!", "?", "@", ";", ":", "(", ")", "[", "]", "-", "–", "|", "/", "*", "\\")

actions = { "goingon_phrase"  : muscles.goingon_phrase_action,
            "laugh"           : muscles.laugh_action,
            "bro_phrases"     : muscles.bro_phrases_action,
            "catch_phrases"   : muscles.catch_phrases_action,
            "hello_phrases"   : muscles.hello_phrases_action,
            "clear_word"      : muscles.clear_word_action,
            "mood_word"       : muscles.mood_word_action,
            "whatdoing_words" : muscles.whatdoing_words_action,
            "whatsup_phrases" : muscles.whatsup_phrases_action,
            "how_word"        : muscles.how_word_action,
            "still_word"      : muscles.still_word_action,
            "dating_word"     : muscles.dating_word_action,
            "you_word"        : muscles.you_word_action,
            "youknow_word"    : muscles.youknow_word_action,
            "welldone_phrases": muscles.welldone_phrases_action,
            "baddone_phrases" : muscles.baddone_phrases_action,
            "drive_word"      : muscles.drive_word_action,
            "watching_word"   : muscles.watching_word_action,
            "speech_phrases"  : muscles.speech_phrases_action,
            "joke_phrases"    : muscles.joke_phrases_action,
            "song_phrases"    : muscles.song_phrases_action,
            "weather_words"   : muscles.weather_words_action,
            "google_search"   : muscles.google_search_action,
            "news_get"        : muscles.news_get_action,
            "who_word"        : muscles.who_word_action,
            "kate_word"       : muscles.kate_word_action,
            "ivan_word"       : muscles.ivan_word_action,
            "tim_word"        : muscles.tim_word_action,
            "mary_word"       : muscles.mary_word_action,
            "not_particle"    : muscles.not_particle_action,
            "goodbye_phrases" : muscles.goodbye_phrases_action }