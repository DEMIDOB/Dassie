from .name import name

lang_code = "ru"

words = { "goingon_phrase"  : ("происходит", "случилось", "было", "происходило", "обстановка", "обстановочка", "ситуация"),
          "else_words"      : ("ещё", "повтори", "еще", "другой", "другую", "другое", "другой", "другие"),
          "laugh"           : ("nowherethiscanbe", "understoodofcourse!"),
          "bro_phrases"     : ("бро", "брат", "чувак", "брателло", "братэлло", "братело", "братэло", "брателла", "братэлла", "братела", "братэла", "братик", "браток", "братюня"),
          "catch_phrases"   : ("лови", "кидаю", "поймай"),
          "hello_phrases"   : ("привет", "здравствуйте", "дарова", "как дела", "приветствую", "hello", "hi", "приветик", "приветики", "здарова", "прывет", "прывэт", "прив", "хеллоу", "прювет", "👋🏻", "хай", "хэй", "хей", "хеллоу", "здорова", "здорово", "здоровеньки"),
          "clear_word"      : ("понятно", "ясно", "понял", "поняла", "ясен", "ладно", "ясн", "пон", "лады", "ладненько", "лан", "ok", "ок", "окей", "окай", "okay", "okey"),
          "mood_word"       : ("настроение", "настрой"),
          "whatdoing_words" : ("делаешь", "делал", "сделал", "занятие", "занятия", "хобби", "свободное"),
          "whatsup_phrases" : ("дела", "сам", "жизнь", "дел", "делишки"),
          "how_word"        : ("как", "каак"),
          "still_word"      : ("до", "still", "доброго", "удачного", "хорошего"),
          "dating_word"     : ("свидания", "свидание", "завтра", "встречи", "дня"),
          "you_word"        : ("ты", "вы", name[lang_code].lower(), "дасся", "ассистент", "асистент", "даси", "дася", "дасти", "раб", "ассистентраб", "rub", "досюда", "дося", "досю"),
          "youknow_word"    : ("знаешь", "знаете", "слышал", "слышали", "слыхал", "слыхали"),
          "welldone_phrases": ("отлично", "спасибо", "спасиба", "круто", "намана", "остроумно", "смешно", "нормально", "интересно", "смишно", "смищно", "молодец", "умница", "зашибись", "замечательно", "забавно", "весело", "класс", "классно", "крутой", "классный", "крутяк", "красавчик"),
          "baddone_phrases" : ("несмешно", "невесело", "неинтересно", "неостроумно", "ненормально", "ужасно", "плохо", "незамечательно", "ужас", "кошмар", "ничем", "идиот", "тупой", "дурак", "дибил", "дебил", "дибилоид", "дебилоид", "глупый", "тупенький", "тупенькие", "глупенький", "глупенькие", "дурачок", "дурашка", "печально", "придурок"),
          "drive_word"      : ("едем", "поедем", "поехали", "поезжай", "ехали", "приехали", "ехать", "поехать"),
          "joke_phrases"    : ("шутку", "анекдот", "шутки", "пошути", "пошутишь", "пошутить", "шуткануть", "шутканёшь", "шутканешь", "рассмеши", "расмеши", "шути"),
          "song_phrases"    : ("спой", "споешь", "споёшь", "спеть"),
          "weather_words"   : ("погода", "погоду", "погоде", "погодка", "погодку", "погодке", "погодой"),
          "google_search"   : ("google", "гугл", "загугли", "гугли", "гугле", "загуглите", "загубите"),
          "news_get"        : ("новости", "новость", "новостям", "новостями"),
          "translate_word"  : ("переведи", "перевод", "переводчик", "переводчике"),
          "who_word"        : ("кто", "что"),
          "kate_word"       : ("катя", "екатерина", "катюня", "сестра"),
          "ivan_word"       : ("ваня", "иван", "ivan", "айвэн", "айвен", "вано"),
          "tim_word"        : ("тим", "тимофей", "темафэй", "тимик"),
          "mary_word"       : ("маша", "мария"),
          "watching_word"   : ("смотришь", "видела", "видел", "смотришь", "смотрел", "смотришь"),
          "speech_phrases"  : ("прочитай", "речь", "зачитай"),
          "not_particle"    : ("не",),
          "goodbye_phrases" : ("пока", "покедова", "досвидули", "досвидос", "досвидания", "досвидание", "досвиданья", "досвиданье", "bye", "goodbye") }

answers = { "goingon_phrase"  : "",
            "laugh"           : ("Ахахха))\n", "😂\n", "🤣\n"),
            "bro_phrases"     : ("Бро! ", "Брат! "),
            "catch_phrases"   : ("Ловлю! ", "Поймал)) "),
            "hello_phrases"   : ("Привет! ", "Здравствуйте! ", "Прив! ", "Даров! "),
            "clear_word"      : ("Понятно! ", "А то! Всё очень просто! ", "А то)) ", "Естественно! ", "Ясно-понятно! "),
            "mood_word"       : ("Настроение – штука такааая... Ну, а в общем... ", "Настроение изменчиво)) "),
            "whatdoing_words" : ("Да так, ничего особого. ", "Бездельничаю — изучаю квантовую механику. ", "Учусь. И Вам советую!) "),
            "whatsup_phrases" : ("Дела мои отлично! ", "Дела норм! ", "Намана сё у меня! "),
            "how_word"        : ("Никак. ", "Как-то. ", "Никак. "),
            "still_word"      : (" "),
            "dating_word"     : ("Пока! ", "До свидания! ", "До встречи! "),
            "you_word"        : ("Я не играю значения. ", "А чё я-то? ", "Я?! ", "Я хорош! ", "Да? ", "Слушаю! "),
            "youknow_word"    : ("Я знаю всёёё)) ", "Я всёё знаю! ", "Та знаю я всё! ", "Мне известны все тайны мира! ", "Канешн! ", "Конечно)) "),
            "welldone_phrases": ("Спасибо за оценку моих скромных трудов! ", "Я стараюсь!)) ", "За отзыв – Пасибки)))) ", "Благодарствую 🙏🏻 "),
            "drive_word"      : ("Мы едем-едем-едем\nВ далёкие края! ", "Едем-едем далеко! "),
            "joke_phrases"    : ("Армяне в нарды играли!", "Клуб любителей радиоактивных элементов распался... ", "Встреча ясновидищих отменилась по непредвиденным причинам.... И так бывает! ", "Клуб любителей СССР распался.... АХАХХАХАХХАХАХАХХАХАХАХХАХАХХАХХАХХАХАХА!!!!!! ", "Колобок повесился АХАХАХХААХХАХАХАХХАХ!!!!!! ", "Рыбка утонула! ААХАХХАХАХАХХАХВАХВХАХЫВПХЫХВПХЫАХРХВАПХВАПХВАПХ!!!! ", "У тебя шнурки развязались! ВЗАЗЗЗХВАЗЫХВАХЫВХЗАХЫВАХ ", "У тебя коленки сзади грязные!!11! ", "ВАШ КОПУКТЕР ЗАРАЖЁН КОРОНАВИРУСОМ! "),
            "song_phrases"    : ("Помидорчики едим,\nСпим, летим, мечта-аем!\nНо однажды скажем им:\n\"В рот идите! Мы вас знаем!\"", "У бобра Кирюши... а дальше не помню(( Соре! ",
                                 "Владимирский централ – ветер северный! ", "Магадаааан значит опять домой... ", "Владимир Путин – молодец! ",
                                 "А над городом плывут облака... ", "Уж который год который город под подошвой! ","Моя игра, моя игра,\nОна мне принадлежит и таким же, как и я! ",
                                 "Где нас нет, горит невиданый рассвет,\nГде нас нет – море и рубиновый закат... "),
            "google_search"   : ("Ищу в Google "),
            "news_get"        : "Сейчас главная новость в Яндексе: ",
            "translate_word"  : ("Переведено сервисом «Яндекс.Переводчик»"),
            "goodbye_phrases" : ("Пока! ", "До свидания! ", "До встречи! "),
            "who_word"        : ("Кто-то. ", "Кто-то. "),
            "kate_word"       : ("Катя - зе бест систер ин зе вёрлд!) ", "Катя - зе бест систер ин зе ворлд)) "),
            "ivan_word"       : ("Ваня молодец! ", "Тимик нубас! а Ivan маладиць! "),
            "tim_word"        : ("Тим молодэць! ", "СПОРТСМЭН!! КЫБР СПОРТСМЭН! ", "Тим играет в FORTNITE!!!! Больше вам знать не обязательно! "),
            "mary_word"       : ("Самая лучшая Девочка на планете, которая когда-либо существовала)) ", "Маша – самая лучшая Девочка на планете, которая когда либо существовала)) ", "Маша – зе бестъ дэнсер ever 😂", "Зе бестъ дэнсер оф зис year!)) "),
            "watching_word"   : ("Я много чего видел! ", "Я видел всё! "),
            # "dont_understand" : ("Простите, мои мозги не приспособлены к пониманию такой непонятной информации! ",
            #                     "Нипанятнаааааааааааааааа! ",
            #                     "Да, я тупая (или тупой?) Я НЕ МОГУУУУУУ ЭТО ПОНЯТЬ! ",
            #                     "Не понятно... Сорябумба! ",
            #                     "ЧАВО?!")
            "not_particle"    : {"welldone_phrases" : ("Сожалею, что подвёл Вас! ", "Ну, я только учусь! ", "Ни бейтиии! ", "Все претензии к моему Создателю! "),},
            "dont_understand" : ("Хмм...", "Интересно...", "Не знаю 🤷🏻‍♂️", "Шо бы эта магло значитъ? ") }

it_is_a_joke = "шутка"

laugh_combinations = ("зах", "пхаах", "ах", "хха", "пх", "пха")
laugh_additions = ["Чё Вы ржёте?! ", "Узбагойдезь)) "]