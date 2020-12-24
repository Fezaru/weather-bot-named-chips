import telebot
import config
from weather_parser import get_temperatures


if __name__ == '__main__':
    bot = telebot.TeleBot(config.TOKEN)


    @bot.message_handler(content_types=['text'])
    def send_message(message):
        if message.text.lower() == 'погода':
            temps = get_temperatures()
            temp1 = temps['temp']
            temp2 = temps['temp_feels']
            bot.send_message(message.chat.id, f'Температура - {temp1} , ощущается как {temp2}')


    bot.polling(none_stop=True)
