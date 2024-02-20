import random

import windowTalker.window
from builtin_skills import speech, google_parse, news_parse, weather_parse
from knowledge.request_context import RequestContext
from laugh.gen import gen_laugh


def goingon_phrase_action(ctx: RequestContext):
    ctx.answer_logical["weather_words"] = True
    ctx.answer_logical["news_get"] = True

    return ""


def laugh_action(ctx: RequestContext):
    kn = ctx.kn
    ret = [gen_laugh(kn) + "\n", "😂\n", "🤣\n"] + kn.laugh_additions
    return random.choice(ret)


def bro_phrases_action(ctx: RequestContext):
    kn = ctx.kn
    return random.choice(kn.answers["bro_phrases"])


def catch_phrases_action(ctx: RequestContext):
    kn = ctx.kn
    return random.choice(kn.answers["catch_phrases"])


def hello_phrases_action(ctx: RequestContext):
    kn = ctx.kn
    return random.choice(kn.answers["hello_phrases"])


def clear_word_action(ctx: RequestContext):
    kn = ctx.kn
    return random.choice(kn.answers["clear_word"])


def mood_word_action(ctx: RequestContext):
    kn = ctx.kn
    return random.choice(kn.answers["mood_word"])


def whatdoing_words_action(ctx: RequestContext):
    kn = ctx.kn
    ctx.answer_logical["who_word"] = False
    return random.choice(kn.answers["whatdoing_words"])


def whatsup_phrases_action(ctx: RequestContext):
    kn = ctx.kn
    this_category = "whatsup_phrases"
    conc_category = "how_word"
    if connected(ctx.answer_logical, (conc_category, this_category)):
        return random.choice(kn.answers["whatsup_phrases"])
    else:
        return random.choice(kn.answers["dont_understand"])


def how_word_action(ctx: RequestContext):
    kn = ctx.kn
    this_category = "how_word"
    conc_category = "whatsup_phrases"
    if connected(ctx.answer_logical, (this_category, conc_category)) or connected(ctx.answer_logical,
                                                                              (this_category, "you_word")):
        return random.choice(kn.answers["whatsup_phrases"])
    elif ctx.answer_logical["weather_words"]:
        return ""
    else:
        # return random.choice(kn.answers["dont_understand"])
        return random.choice(kn.answers["how_word"])


def still_word_action(ctx: RequestContext):
    kn = ctx.kn
    # this_category = kn.categories.index("still_word")
    # conc_category = kn.categories.index("dating_word")
    # if connected(answer_logical, (this_category, conc_category)):
    #     return random.choice(kn.answers["dating_word"])
    # else:
    #     return "Что Вы имеете в виду под словом \"до\"?"
    if ctx.answer_logical["dating_word"]:
        return ""
    else:
        return "До-до! "


def dating_word_action(ctx: RequestContext):
    kn = ctx.kn
    this_category = "dating_word"
    conc_category = "still_word"
    if connected(ctx.answer_logical, (conc_category, this_category)):
        return random.choice(kn.answers["dating_word"])
    else:
        return "Увидимся?! "


def you_word_action(ctx: RequestContext):
    kn = ctx.kn
    return random.choice(kn.answers["you_word"])


def youknow_word_action(ctx: RequestContext):
    kn = ctx.kn
    return random.choice(kn.answers["youknow_word"])


def welldone_phrases_action(ctx: RequestContext):
    kn = ctx.kn
    if not ctx.answer_logical["not_particle"]:
        return random.choice(kn.answers["welldone_phrases"])
    else:
        not_dict = kn.answers["not_particle"]
        return random.choice(not_dict["welldone_phrases"])


def baddone_phrases_action(ctx: RequestContext):
    kn = ctx.kn
    not_dict = kn.answers["not_particle"]
    return random.choice(not_dict["welldone_phrases"])


def drive_word_action(ctx: RequestContext):
    kn = ctx.kn
    return random.choice(kn.answers["drive_word"])


def joke_phrases_action(ctx: RequestContext):
    kn = ctx.kn
    return random.choice(kn.answers["joke_phrases"])


def song_phrases_action(ctx: RequestContext):
    kn = ctx.kn
    return "\n" + random.choice(kn.answers["song_phrases"])


def weather_words_action(ctx: RequestContext):
    kn = ctx.kn
    ctx.answer_logical["how_word"] = False
    tmp_this_pos = str(ctx.brain.location)
    tmp_weather = weather_parse.parse(tmp_this_pos)
    return tmp_weather
    # return "Погода в {0} так себе, чувак) ".format(tmp_this_pos)


def google_search_action(ctx: RequestContext):
    kn = ctx.kn
    ctx.answer_logical["who_word"] = False
    request = generate_request(ctx.sentence, kn)
    ret = google_parse.parse(request)
    # print("http://548f352d.ngrok.io/pg/{0}".format(request))
    # response = requests.get("http://548f352d.ngrok.io/pg/{0}".format(request))
    if len(ret) < 3:
        ret = "Сорян! Такого я не нашёл(("
    return ret


def news_get_action(ctx: RequestContext):
    kn = ctx.kn
    exept_category_index = "who_word"
    ctx.answer_logical[exept_category_index] = False
    return kn.answers["news_get"] + news_parse.parse()


def who_word_action(ctx: RequestContext):
    kn = ctx.kn
    # this_category  = kn.categories.index("who_word")
    # conc_category  = kn.categories.index("ivan_word")
    # conc_category1 = kn.categories.index("tim_word")
    # conc_category2 = kn.categories.index("mary_word")
    # if connected(answer_logical, (this_category, conc_category)):
    #     return random.choice(kn.answers["ivan_word"])
    # elif connected(answer_logical, (this_category, conc_category1)):
    #     return random.choice(kn.answers["tim_word"])
    # elif connected(answer_logical, (this_category, conc_category2)):
    #     return random.choice(kn.answers["mary_word"])
    # elif not answer_logical[kn.categories.index("you_word")]:
    #     return "Таких не знаю(( соре! "
    # else:
    #     return ""
    if ctx.answer_logical["you_word"]:
        return ""
    else:
        return random.choice(kn.answers["who_word"])


def kate_word_action(ctx: RequestContext):
    kn = ctx.kn
    this_category = "kate_word"
    conc_category = "who_word"
    if connected(ctx.answer_logical, (conc_category, this_category)):
        ctx.answer_logical[conc_category] = False
        return random.choice(kn.answers["kate_word"])
    else:
        return "Шо?"


def ivan_word_action(ctx: RequestContext):
    kn = ctx.kn
    this_category = "ivan_word"
    conc_category = "who_word"
    if connected(ctx.answer_logical, (conc_category, this_category)):
        ctx.answer_logical[this_category] = False
        return f"{kn.it_is_a_joke})) " + random.choice(kn.answers["ivan_word"])
    else:
        return "ХТО ТАКХОЙ \"ВАНО\"?!??!?!!? НИПАНЯТНА!"


def tim_word_action(ctx: RequestContext):
    kn = ctx.kn
    this_category = "tim_word"
    conc_category = "who_word"
    if connected(ctx.answer_logical, (conc_category, this_category)):
        ctx.answer_logical[this_category] = False
        return f"{kn.it_is_a_joke}!) " + random.choice(kn.answers["tim_word"])
    else:
        return "ХТО ТАКХОЙ \"ТЭМАФЭЙ\"?!??!?!!? НИПАНЯТНА!"


def mary_word_action(ctx: RequestContext):
    kn = ctx.kn
    this_category = "mary_word"
    conc_category = "who_word"
    # answer_logical[this_category] = False # tmp
    if connected(ctx.answer_logical, (conc_category, this_category)):
        ctx.answer_logical[this_category] = False
        return f"Somebody. {gen_laugh(kn)}, {kn.it_is_a_joke}! " + random.choice(
            kn.answers["mary_word"])  # + "Иногда ещё не отвечает на сообщения, ну и ладно 😂 "
    else:
        return "TBGE?!"


def watching_word_action(ctx: RequestContext):
    kn = ctx.kn
    return random.choice(kn.answers["watching_word"])


1


def speech_phrases_action(ctx: RequestContext):
    kn = ctx.kn
    sent_num = random.randint(2, 5)
    return speech.gen(sent_num)


def not_particle_action(ctx: RequestContext):
    kn = ctx.kn
    return ""


def goodbye_phrases_action(ctx: RequestContext):
    kn = ctx.kn
    return random.choice(kn.answers["goodbye_phrases"])


def generate_request(sentence, kn):
    google_word_index = -1
    for google_word in kn.words["google_search"]:
        if sentence.__contains__(google_word):
            google_word_index = sentence.index(google_word)
    request_ret = ""
    for i in range(google_word_index + 1, len(sentence)):
        request_ret += sentence[i] + " "

    return request_ret


def light_on(ctx: RequestContext):
    w = windowTalker.window.Window()
    w.fetch_state()
    if ctx.answer_logical["turn_on"]:
        w.enter_draw_mode()
        w.set_color(windowTalker.crgb.WHITE)
    elif ctx.answer_logical["turn_off"]:
        w.set_mode("aq")
        w.set_color(windowTalker.crgb.WHITE)

    return "Сделано :)"

def empty(ctx: RequestContext):
    return ""


def connected(answer_logical, cc):
    if answer_logical[cc[0]] and answer_logical[cc[1]]:
        answer_logical[cc[1]] = False
        return True
    else:
        return False
