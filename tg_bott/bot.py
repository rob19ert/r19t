import telebot
from telebot import types
bot = telebot.TeleBot('6611223234:AAFr047Y0eeuxxfCciIEnVOW-JgthQkdjLo')

# Подключаем модуль случайных чисел 
import random
# Заготовка для первого предложения
first = ["Порисуй акварелью","Сходи на каток","Сходи на тренировку","Выучи уроки","Почитай книжки",
         "Сделай кувырок", "Научись стоять на руках","Выучи 3 стихотворения","Приберись дома", 
         "Сходи погулять", "Заведи собаку", "Выучи китайский", "Выучи C#","Потанцуй","Купи губную гармошку",
         "Пригласи случайного прохожего на ужин","Пожертвуй деньги нуждающимся", "Ходи весь день с улбыкой", 
         "Отвечай на все вопросы сегодня - да"]


@bot.message_handler(commands=['start'])
def send_random_word(message):
    random_hero = random.choice(first)
    markup = get_inline_keyboard()
    bot.send_message(message.chat.id, f"Случайное действие: {random_hero}", reply_markup=markup)


def get_inline_keyboard():
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Новое действие", callback_data="new_hero")
    markup.add(button)
    return markup


@bot.callback_query_handler(func=lambda call: call.data == "new_hero")
def button_click(call):
    random_hero = random.choice(first)
    markup = get_inline_keyboard()
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Случайное действие: {random_hero}", reply_markup=markup)

if __name__ == '__main__':
    bot.polling()