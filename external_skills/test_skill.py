import windowTalker.window
import windowTalker.crgb

categories = ("light_word", "reboot_word")

triggers = {
    "light_word": {
        "ru": ("свет", "люмос"),
        "en": ("light", "lumos")
    },
    "reboot_word": {
        "ru": ("перезагрузка", "окно", "перезагрузи"),
        "en": ("reboot", "window")
    }
}

the_light_is_on_reply = {
    "ru": "Да будет свет!",
    "en": "The light is on!"
}

the_light_is_off_reply = {
    "ru": "Погружаемся во тьму...",
    "en": "The light goes off.."
}


def light_muscle(ctx):
    w = windowTalker.window.Window()
    w.fetch_state()
    pixels = w.fetch_pixels()
    print(sum([p.red + p.green + p.blue for p in pixels]))
    if w.state.mode != "draw":
        w.set_mode("draw")
        w.set_color(windowTalker.crgb.CRGB.BLACK)
        return the_light_is_off_reply[ctx.lang_code] if ctx.lang_code in the_light_is_off_reply else \
        the_light_is_off_reply["ru"]
    else:
        w.set_mode("aq")
        return the_light_is_on_reply[ctx.lang_code] if ctx.lang_code in the_light_is_on_reply else \
        the_light_is_on_reply["ru"]

    return "OK"


def reboot_muscle(ctx):
    w = windowTalker.window.Window()
    w.reboot()
    return the_light_is_on_reply[ctx.lang_code] if ctx.lang_code in the_light_is_on_reply else the_light_is_on_reply["ru"]


actions = {
    "light_word": light_muscle,
    "reboot_word": reboot_muscle
}
