"""

This is a echo bot.

It echoes any incoming text messages.

"""


import logging

import datetime

from aiogram import Bot, Dispatcher, executor, types

from prayerTimes import fetchPrayerTime

currentDate = datetime.datetime.now()
date = currentDate.strftime("%d")


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

    await message.reply("Шаҳри (ноҳияи) худро интихоб кунед:")




@dp.message_handler()

async def echo(message: types.Message):

    # old style:

    # await bot.send_message(message.chat.id, message.text)


    await message.answer(message.text)



if __name__ == '__main__':
    # fetchPrayerTime("Dushanbe", "Tajikistan", "02", "2023")
    executor.start_polling(dp, skip_updates=True)