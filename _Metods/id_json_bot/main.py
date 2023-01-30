import telebot
from telebot.types import Message
import json

bot_client = telebot.TeleBot(token='    !!!!          ')
ADMIN_CHAT_ID = 424241242

print('server start')

@bot_client.message_handler(commands=['start'])
def start(message: Message):
    with open('user.json', 'r') as f_o:
        data_from_json = json.load(f_o)

        user_id = message.from_user.id
        username = message.from_user.username

        if str(user_id) not in data_from_json:
            data_from_json[user_id] = {'username': username}

    with open('user.json', 'w') as f_o:
        json.dump(data_from_json, f_o, indent=4, ensure_ascii=False)
    bot_client.reply_to(message=message, text=str(f'Вы зарегистрированы: {username}.'
                                                  f'Ваш user_id: {user_id}'))