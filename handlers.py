import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1018729138:AAFtMT4GQ0f262LqGWzkMh5RBHWaZstOZ8A' #test_token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


# @dp.message_handler(regexp='(^cat[s]?$|puss)')
# async def cats(message: types.Message):
#     with open('data/cats.jpg', 'rb') as photo:
#         '''
#         # Old fashioned way:
#         await bot.send_photo(
#             message.chat.id,
#             photo,
#             caption='Cats are here 😺',
#             reply_to_message_id=message.message_id,
#         )
#         '''
#
#         await message.reply_photo(photo, caption='Cats are here 😺')

@dp.message_handler(commands=['admin_add_club'])
async def add_club(message: types.Message):
    print(message.text)

# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#     print(message)
#     await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)