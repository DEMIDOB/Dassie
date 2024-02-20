from .name import name

lang_code = "en"

words = { "goingon_phrase"  : ("occurs", "happened", "was", "happened", "atmosphere", "обстановочка", "situation"),
          "else_words"      : ("else", "repeat", "again", "more"),
          "laugh"           : ("nowherethiscanbe", "understoodofcourse!"),
          "bro_phrases"     : ("bro", "brother", "dude", "broo", "brah", "broda", "maan", "man", "братэлла", "братела", "братэла", "братик", "браток", "братюня"),
          "catch_phrases"   : ("catch", "throwing", "get"),
          "hello_phrases"   : ("hello", "hi", "aloha", "howdy", "hey", "hello", "hi", "heeelllooo", "приветики", "здарова", "прывет", "прывэт", "прив", "хеллоу", "прювет", "👋🏻", "хай", "хэй", "хей", "хеллоу", "hihi", "здорово", "здоровеньки"),
          "clear_word"      : ("obvious", "clear", "understood", "understood", "clearly", "fine", "ok", "пон", "okey", "ладненько", "лан", "ok", "ок", "окей", "окай", "okay", "okey"),
          "mood_word"       : ("mood", "mindset"),
          "whatdoing_words" : ("doing", "did", "done", "hobby", "free"),
          "whatsup_phrases" : ("case", "myself", "life", "дел", "cases"),
          "how_word"        : ("how", "howww"),
          "still_word"      : ("before", "still", "lucky", "nice"),
          "dating_word"     : ("dates", "meetings", "tomorrow", "appointments", "day"),
          "you_word"        : ("you", "you", name[lang_code].lower(), "dassi", "dassia", "assistant", "assistant", "dasi", "daasi", "dasti", "slave", "slaveassistant"),
          "youknow_word"    : ("know", "know", "heard", "heard", "слыхал", "слыхали"),
          "welldone_phrases": ("amazing", "thanks", "wow", "lol" "cool", "okeysi", "wittily", "funny", "normal", "interesting", "fuuunny", "good", "attaboy", "brains", "great", "замечательно", "comic", "hilarious", "great", "cool"),
          "baddone_phrases" : ("unfunny", "mirthlessly", "uninteresting", "pointless", "abnormal", "awful", "bad", "uncool", "horror", "nightmare", "ничем", "idiot", "dumb", "fool", "moron", "imbecile", "retard", "stupid", "dumb", "foolish", "тупенькие", "глупенький", "глупенькие"),
          "drive_word"      : ("go", "drive", "come", "поезжай", "ехали", "arrived", "ride", "going"),
          "joke_phrases"    : ("joke", "anecdote", "jokes", "joke", "kid", "jest", "tease", "шутканёшь", "шутканешь", "рассмеши", "расмеши", "шути"),
          "song_phrases"    : ("sing", "споешь", "споёшь", "спеть"),
          "weather_words"   : ("weather", "погоду", "погоде", "погодка", "погодку", "погодке"),
          "google_search"   : ("google", "google", "google", "гугли", "гугле", "загуглите", "загубите"),
          "news_get"        : ("news", "new", "новостям", "новостями"),
          "translate_word"  : ("translate", "translation", "translator", "переводчике"),
          "who_word"        : ("who", "what"),
          "kate_word"       : ("kate", "catherine", "cathy", "sister"),
          "ivan_word"       : ("vania", "ivan", "ivan", "aivan", "aiven", "vano"),
          "tim_word"        : ("tim", "timophei", "temaphey", "timik"),
          "mary_word"       : ("masha", "maria", "mary"),
          "watching_word"   : ("looking", "saw", "видел", "смотришь"),
          "speech_phrases"  : ("read", "speach", "зачитай"),
          "not_particle"    : ("no", "not"),
          "goodbye_phrases" : ("bye", "byeeere", "досвидули", "досвидос", "досвидания", "досвидание", "досвиданья", "досвиданье", "bye", "goodbye"),
          "turn_on"         : ("on", ),
          "turn_off"        : ("off", ), }

answers = { "goingon_phrase"  : "",
            "laugh"           : ("ahahahahhaha))\n", "😂\n", "🤣\n"),
            "bro_phrases"     : ("Bro! ", "Brother! "),
            "catch_phrases"   : ("Catching! ", "Caught)) "),
            "hello_phrases"   : ("Hi! ", "Hello! ", "Hey! ", "Howdy! "),
            "clear_word"      : ("Understand! ", "Oh yeah! It’s easy-peasy! ", "Oh yeah)) ", "Naturally! ", "Okey, all right! "),
            "mood_word"       : ("Mood – is such a thing... Well, generally... ", "My mood is changeable)) "),

            "whatsup_phrases" : ("I’m amazing! ", "Everything is ok! ", "I’m fine, baby! "),
            "how_word"        : (" "),
            "still_word"      : (" "),
            "dating_word"     : ("Bye! ", "Goodbye! ", "See you later! "),
            "you_word"        : ("Me? ", "Why me? ", "ME?! "),
            "youknow_word"    : ("I know everything)) ", "I’m a genius, I know! ", "Та знаю я всё! ", "I know all world secrets! ", "Ofcts! ", "Of course)) "),
            "welldone_phrases": ("Thank you for your appreciation of my humble labors! ", "I do my best!)) ", "Huge thank you for the feedback)))) ", "Thanks 🙏🏻 "),
            "drive_word"      : ("We are going-we are going-we are going far away! ", "Going-going far! "),
            "joke_phrases"    : ("The radioactivity lovers' club has broken up into elements... ", "Clairvoyant meeting was canceled for unforeseen reasons.... And so it happens! ","The club of the Soviet Union collapsed!! AHAHAHAHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHA!!!! ", "Kolonok man hanged himself! AHAHAHAHAHAHHAHAAH ", "The fish drowned! AHAHHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHAAHAHHAAHAH ", "Your shoelaces are untied! AHAHAHAHAHAHHAHAHAAHHAAHHAHAAHHAHAHAHAHAHAHAHAAHAHHAAHAHHA ", "You got your knees dirty behind!!11! ", "YOUR COMPUTER IS INFECTED WITH A CORONAVIRUS! "),
            "song_phrases"    : ("We eat Tomatoes, sleep, fly, dream! But one day we will tell them:\nHey,buddy come to my mouth! We know you!", "The beaver Kirusha.... oh, I forgot the ending, sorry((! ",
                                 "Vladimir Central-north wind! ", "Magadan is listed as a house... ", "Vladimir Putin — well done! ",
                                 "And there are clouds floating over the city... ", "What a city under me! ", "My game, my game, I like it and like it, just like me! ",
                                 "Where we are not theres burning an unprecedented dawn!, Where we are not theres sea and ruby sunset... "),
            "google_search"   : ("Looking in Google "),
            "news_get"        : "Now the main news in Yandex are: ",
            "translate_word"  : ("Translated by service \"Yandex.Translator\""),
            "goodbye_phrases" : ("Bye! ", "Goodbye ", "See you later! "),
            "who_word"        : (" "),
            "ivan_word"       : ("Vania is a Good boy! ", "Тимик нубас! а Ivan маладиць! "),
            "tim_word"        : ("Tim-well done! ", "SPORTSMEN!! CYBER ATHLET", "Tim plays FORTNITE!!!! You don't need to know anything else! "),
            "mary_word"       : ("The best girl on the planed that ever existed)) ", "Mary is the best girl that ever existed on Planet Earth)) ", "Mary is the best coder ever 😂", "The best coder!)) "),
            "watching_word"   : ("I saw a lot of things! ", "I saw everything! "),
            # "dont_understand" : ("I'm sorry, my brain is not equipped to understand such incomprehensible information! ",
            #                     "IDONTUNDERSTAAAAAAAND! ",
            #                     "Yep,I’m stupid (or am I dumb?) ICANTUNDERSTANDTHAT! ",
            #                     "I don’t understand... Sorry, baby! ",
            #                     "WHAT?!")
            "not_particle"    : {"welldone_phrases" : ("I'm sorry I let You down! ", "Well, I'm just learning! ""Don’t kill me! ", "All claims to my Creator! "),},
            "dont_understand" : ("Hmmmmm...", "Sorry, what?))", "Interesting...", "I don’t know 🤷🏻‍♂️", "Wat cud tis min?? ") }

it_is_a_joke = "I'm kidding"

laugh_combinations = "hah", "hhaah", "ah", "ha"
laugh_additions = ["KalM down! :)) ", "Why are you laughing?? ;)) "]
