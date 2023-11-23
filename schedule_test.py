import asyncio
from datetime import datetime
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.utils import executor

TOKEN = '6756810195:AAEVKJVcrpBwFCEUcr5OO62Nr9kQuKw0gZs'
CHAT_ID = '-1001619038529'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def send_message():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await bot.send_message(chat_id=CHAT_ID, text=f"현재 시간: {current_time}")

async def job():
    while True:
        now = datetime.now()
        current_hour = now.hour
        if 6 <= current_hour <= 23:
            await send_message()
        await asyncio.sleep(1800)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(job())
    executor.start_polling(dp, loop=loop)
