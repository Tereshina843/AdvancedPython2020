from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from SECRET_token import secret_token

import requests
from bs4 import BeautifulSoup
import json

bot = Bot(token=secret_token)
dp = Dispatcher(bot)


def get_image_url(text):
    URL = 'https://yandex.ru/images/search?text=' + text

    response = requests.get(URL)


    soup = BeautifulSoup(response.content, 'html.parser')


    image_data = soup.select('.serp-item.serp-item_type_search')[0]


    try:
        return json.loads(image_data.attrs['data-bem'])['serp-item']['preview'][0]['origin']['url']
    except KeyError:
        return json.loads(image_data.attrs['data-bem'])['serp-item']['dups'][0]['url']



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm ImageBot!\nWrite any text and get a picture from it!")



@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(get_image_url(message.text))


if __name__ == '__main__':
    executor.start_polling(dp)
