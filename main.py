import telebot
from random import randint
from config import token

from logic import Pokemon, Fighter

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        type_pokemon =  randint(1,2)
        if type_pokemon == 1:
            pokemon = Pokemon(message.from_user.username)
        elif type_pokemon == 2:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['reroll'])
def go(message):
    type_pokemon =  randint(1,2)
    if type_pokemon == 1:
            pokemon = Pokemon(message.from_user.username)
    elif type_pokemon == 2:
            pokemon = Fighter(message.from_user.username)
    bot.send_message(message.chat.id, pokemon.info())
    bot.send_photo(message.chat.id, pokemon.show_img())

@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.fight(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

@bot.message_handler(commands=['heal'])
def attack_pok(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.heal())
    else:
         bot.send_message(message.chat.id, "У тебя нет покемона")

@bot.message_handler(commands=['info'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "У тебя нет покемона")
    else:
        pok = Pokemon.pokemons[message.from_user.username]
        bot.reply_to(message, pok.info())



bot.infinity_polling(none_stop=True)

