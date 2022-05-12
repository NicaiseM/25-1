import telebot
from random import randrange
from config import telegram_token

bot = telebot.TeleBot(telegram_token)

@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.send_message(message.chat.id, 'Здравствуй, игрок! Введи "/new_game" для начала игры!')

@bot.message_handler(commands=['new_game'])
def handle_text(message):
    global date, count
    print(message)
    bot.send_message(message.chat.id, 'Я загадал число от 1 до 10. Угадаешь его? У тебя 3 попытки!')
    date = randrange(1, 10)
    count = 0

@bot.message_handler(content_types=['text'])
def handle_text(message):
    global count
    if count < 3:
        count += 1
        try:
            attempt = int(message.text)
        except ValueError:
            bot.send_message(message.chat.id, 'Не является числом.')
            return
        if attempt > date:
            bot.send_message(message.chat.id, f'Загаданное число меньше {attempt}, попробуй еще раз.')
        elif attempt < date:
            bot.send_message(message.chat.id, f'Загаданное число больше {attempt}, попробуй еще раз.')
        elif attempt == date:
            bot.send_message(message.chat.id, f'Ты угадал! Было загадано число {attempt}! Сыграем еще?\nВведи "/new_game" для начала игры!')
    else:
        bot.send_message(message.chat.id, 'Количество попыток исчерпано.')

bot.polling(none_stop=True)
