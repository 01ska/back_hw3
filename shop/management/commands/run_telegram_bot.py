from django.core.management.base import BaseCommand
from django.db import IntegrityError
import telebot
from shop.models import Product

# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         print("Hello world!")


# bot = telebot.TeleBot("TOKEN") # Вставьте сюда свой токен
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         print("Starting bot...")
#         bot.polling()
#         print("Bot stopped")

bot = telebot.TeleBot("6624612270:AAHJ2m76oeT3WKeQUsgLgOF19VvRKqAz_6A") # Вставьте сюда свой токен
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")
    
class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")

@bot.message_handler(commands=['products'])
def products(message):
    products = Product.objects.all()
    for product in products:
        bot.send_message(message.chat.id, product.name)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

