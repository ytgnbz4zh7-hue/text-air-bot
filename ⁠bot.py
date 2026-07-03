import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from googletrans import Translator

# СЮДА ВСТАВЬ СВОЙ НОВЫЙ ТОКЕН ИЗ BOTFATHER
TOKEN = "8888665064: AAGkXPAcLm5zJEpoSE4-
wdfzGmclhi4glUE"

bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Салом! Я бот-переводчик. Просто пришли мне текст.")

@dp.message()
async def translate(message: types.Message):
    try:
        translated = translator.translate(message.text, dest='tg')
        await message.answer(f"Тарҷума: {translated.text}")
    except Exception as e:
        await message.answer("Хатогӣ рух дод.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
