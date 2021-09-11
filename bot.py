from contextvars import Token
import config

import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

#bot init

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

#echo
@dp.message_handler()
async def filter_messages(message: types.Message):
    if "далбан" in message.text:
        await message.delete()
        
@dp.message_handler()
async def filter_messages(message: types.Message):
    if "сука" in message.text:
        await message.delete()

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
