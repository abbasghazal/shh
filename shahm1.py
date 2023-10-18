import telebot

import requests

from telebot import types

bot_token = '5581530921:AAEIhw4rZ7fPNPw5gW2CiWUxm34kIPYXpjk'

bot = telebot.TeleBot(bot_token)

compulsory_channel = "@BGGlG"

@bot.message_handler(commands=['start'])

def send_welcome(message):

    # Check if the user is subscribed to the compulsory channel

    if not is_subscribed(message.chat.id):

        # Create the subscription markup

        markup = types.InlineKeyboardMarkup()

        subscribe_button = types.InlineKeyboardButton(text="اشترك", url=f"https://t.me/BGGlG")

        markup.add(subscribe_button)

        # Send the subscription message

        bot.send_message(message.chat.id, "عذرا عليك الاشتراك في قناة البوت @BGGlG لكي تتمكن من استخدام البوت ", reply_markup=markup)

        return

    bot.reply_to(message, "اهلا بك في بوت الذكاء الاصطناعي ")

@bot.message_handler(func=lambda message: True)

def echo_all(message):

    text = message.text

    response = requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={text}').text

    bot.reply_to(message, response)

def is_subscribed(chat_id):

    try:

        chat_member = bot.get_chat_member(compulsory_channel, chat_id)

        if chat_member.status == 'member' or chat_member.status == 'creator' or chat_member.status == 'administrator':

            return True

    except telebot.apihelper.ApiException:

        pass

    return False

print ('تم تشغيل البوت ')
bot.infinity_polling()