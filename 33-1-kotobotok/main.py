import telebot
from config import telegram_token

bot = telebot.TeleBot(telegram_token)

@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.send_message(message.chat.id, 'Привет, котик!')
    
@bot.message_handler(content_types=['text'])
def handle_text(message):
    print(message)

    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Как твои дела?')
    elif message.text == 'Отлично':
        bot.send_message(message.chat.id, '✨ Какой ты молодец, котик!✨ (=⌒‿‿⌒=)')
        bot.send_message(message.chat.id, 'Давай расскажу стишок, чтобы стало еще лучше!')
    elif message.text == 'Хорошо':
        bot.send_message(message.chat.id, 'Хорошо, когда котику хорошо! (=⌒‿‿⌒=)')
        bot.send_message(message.chat.id, 'Давай расскажу стишок, чтобы стало еще лучше!')
    elif message.text == 'Нормально':
        bot.send_message(message.chat.id, 'Соответствие внутренней норме это прекрасно!🌈☁☀')
        bot.send_message(message.chat.id, 'Давай расскажу стишок, чтобы закрепить успех!')
    elif message.text == 'Плохо':
        bot.send_message(message.chat.id, 'Бери цветочки, пусть дела будут хорошо! 🌷 🌸 🌹 🌺 🌻 🌼 💐 ')
        bot.send_message(message.chat.id, 'Давай расскажу стишок, чтобы поднять настроение!')
    elif message.text == 'Давай':
        bot.send_message(message.chat.id, 'Плачет киска в коридоре, у нее большое горе: злые люди бедной киске не дают украсть сосиски!')
    elif message.text == 'Да':
        bot.send_message(message.chat.id, 'Плачет киска в коридоре, у нее большое горе: злые люди бедной киске не дают украсть сосиски!')
    elif message.text == 'Спасибо':
        bot.send_message(message.chat.id, 'Котик, ты очень мил! Это тебе 🍀')
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, 'Котик капризничает, котику точно пора спать 🌙 ')
    else:
        bot.send_message(message.chat.id, 'Я не понимаю котика. Кажется, котик устал и ему пора спать ☁🌛☁')
bot.polling(none_stop=True)
