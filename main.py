"""

This is a echo bot.

It echoes any incoming text messages.

"""


import logging

import tracemalloc

import datetime

from aiogram import Bot, Dispatcher, executor, types

from prayerTimes import fetchPrayerTime

currentDate = datetime.datetime.now()
date = currentDate.strftime("%d")

tracemalloc.start()

API_TOKEN = '6254770087:AAGe_KnW_9MyEqXcVmbQb_FanURknAMp6cM'


# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

prayerTimes = fetchPrayerTime("Dushanbe", "Tajikistan", "02", "2023")
city = "Dushanbe"

@dp.message_handler(commands=['vaqtinamoz'])

async def send_welcome(message: types.Message):
    # currDate = int(date) - 1
    result = prayerTimes[int(date) - 1]['timings']
    await message.reply(f"Вакти намоз барои имруз(ш.Душанбе):\n"
                        f"Бомдод: {result['Fajr']}\n"
                        f"Пешин: {result['Dhuhr']}\n"
                        f"Аср: {result['Asr']}\n"
                        f"Шом: {result['Maghrib']}\n"
                        f"Хуфтан: {result['Isha']}\n")


@dp.message_handler(commands=['start'])

async def send_welcome(message: types.Message):


    """

    This handler will be called when user sends `/start` or `/help` command

    """
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardMarkup(text="Душанбе", callback_data="Dushanbe")
    btn2 = types.InlineKeyboardMarkup(text="Согд", callback_data="Soghd")
    btn3 = types.InlineKeyboardMarkup(text="Хатлон", callback_data="Kharlon")
    btn4 = types.InlineKeyboardMarkup(text="ГБАО", callback_data="GBAO")
    markup.add(btn1, btn2, btn3, btn4)

    await message.answer(text="Вилоят (Шахри)-и худро интихоб кунед:", reply_markup=markup)

@dp.callback_query_handler(lambda c: True)
async def process_callback_kb(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    message = callback_query.data

    prayerTimes = fetchPrayerTime(message, "Tajikistan", "02", "2023")
    result = prayerTimes[int(date) - 1]['timings']
    await bot.send_message(chat_id=chat_id, text=f"Вакти намоз барои имруз(в.{message}):\n"
                        f"Бомдод: {result['Fajr']}\n"
                        f"Пешин: {result['Dhuhr']}\n"
                        f"Аср: {result['Asr']}\n"
                        f"Шом: {result['Maghrib']}\n"
                        f"Хуфтан: {result['Isha']}\n")
    # await bot.send_message(chat_id=chat_id, text=message)

@dp.message_handler()

async def echo(message: types.Message):
    result = prayerTimes[int(date) - 1]['timings']
    await message.reply(f"Вакти намоз барои имруз(ш.Душанбе):\n"
                        f"Бомдод: {result['Fajr']}\n"
                        f"Пешин: {result['Dhuhr']}\n"
                        f"Аср: {result['Asr']}\n"
                        f"Шом: {result['Maghrib']}\n"
                        f"Хуфтан: {result['Isha']}\n")



if __name__ == '__main__':
    # fetchPrayerTime("Dushanbe", "Tajikistan", "02", "2023")
    executor.start_polling(dp, skip_updates=True)