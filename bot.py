import telebot
import requests

import sessions.sessions_manager as um
from safe.bot_tg import main_bot_token
from dassie_audio import bot_audio

token = main_bot_token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['feedback'])
def feedback_command(message):
    received = message.text
    if received == "/feedback":
        bot.reply_to(message, "Обратную связь вы можете оставить по этой ссылке, либо же ещё раз отправить сообщение \"/feedbaсk\" и в конце написать отзыв! Ваше мнение поможет сделать Дасси ещё лучше!")
    else:
        start_index = len("/feedback") + 1
        message_len = len(received)

        feedback_text = ""
        for i in range(start_index, message_len):
            feedback_text += received[i]

        requests.post('http://demidob.000webhostapp.com/dassi/feedback/fb.php', data={'text' : feedback_text, 'uid' : message.from_user.id})

        bot.reply_to(message, "Огрооомнейшее спасибо за обратную связь)) Я понял, она такая: " + feedback_text)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    received = message.text
    id = message.from_user.id
    print(id, "–", received)

    if not um.session_exists(id):
        um.create_session(session_id=id, location="50,50")

    data = um.reply(message.from_user.id, received)["answer"]
    out = data[0]
    print(out)
    bot.send_message(message.from_user.id, str(out))


@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    id = message.from_user.id

    if not um.session_exists(id):
        um.create_session(session_id=id, location="50,50")

    received = bot_audio.handle_voice(message, bot, token)
    data = um.reply(message.from_user.id, received)["answer"]
    out = data[0]
    bot.send_message(id, str(out))


bot.polling(none_stop=True)
