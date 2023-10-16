import os
import logging

from aiogram import Bot, Dispatcher, executor, types

#from config import TOKEN

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def trans(m):
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g',
     'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 
     'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 
     'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 
     'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 
     'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 
     'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': 'ie', 
     'ы': 'y', 'э': 'e', 'ю': 'iu', 'я': 'ia', ' ':' '}
    
    m = list(m.lower())
    
    while 'ь' in m:
        m.remove('ь')
    
    a = list(d[el] for el in m if el in d)
    return ''.join(a).title()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    logging.info(f'{user_name=} {user_id=} sent message:{message.text}')
    text = f'Привет, {user_name}! Я помогу произвести транслитерацию в соответствии с приказом МИД РФ. Пришли необходимые ФИО'
    await message.reply(text)

@dp.message_handler()
async def send_transliteration(message: types.Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    text = trans(message.text)
    logging.info(f'{user_name=} {user_id=} sent message:{text}')

    await bot.send_message(user_id, text)


if __name__ == '__main__':
    executor.start_polling(dp)
