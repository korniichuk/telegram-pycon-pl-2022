#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name: bot5
# Description: Asynchronous NBP bot with aiogram
# Version: 0.1a1
# Owner: Ruslan Korniichuk

import os

from aiogram import Bot, Dispatcher, executor
from aiogram.types import (
        CallbackQuery,
        InlineKeyboardButton,
        InlineKeyboardMarkup,
        InlineQuery,
        InlineQueryResultArticle,
        InputTextMessageContent,
        Message)

from dotenv import load_dotenv

from nbp import get_rate, get_table

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

markup = InlineKeyboardMarkup()
a = InlineKeyboardButton('table A', callback_data='a')
b = InlineKeyboardButton('table B', callback_data='b')
c = InlineKeyboardButton('table C', callback_data='c')
markup.row(a, b, c)


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("🔥 Hello, World!", reply_markup=markup)


@dp.message_handler(commands=['a', 'b', 'c'])
async def tables_command(message: Message):
    command = message.text[1]
    await message.answer(get_table(command), parse_mode='MARKDOWN')


@dp.callback_query_handler(lambda callback_query: True)
async def callback_querry(query: CallbackQuery):
    await bot.send_message(query.message.chat.id, get_table(query.data),
                           parse_mode='MARKDOWN')


@dp.inline_handler(lambda query: query.query == 'rate')
async def inline(inline_query: InlineQuery):
    r1 = InlineQueryResultArticle(
            id='1', title='USD', input_message_content=InputTextMessageContent(
                    get_rate('usd'), parse_mode='MARKDOWN'))
    r2 = InlineQueryResultArticle(
            id='2', title='EUR', input_message_content=InputTextMessageContent(
                    get_rate('eur'), parse_mode='MARKDOWN'))
    r3 = InlineQueryResultArticle(
            id='3', title='GBP', input_message_content=InputTextMessageContent(
                    get_rate('gbp'), parse_mode='MARKDOWN'))

    # cache_time -- maximum amount of time in seconds that the result of
    # inline query may be cached on the server.
    await bot.answer_inline_query(inline_query.id, [r1, r2, r3], cache_time=1)


if __name__ == '__main__':
    # Do not skip all incoming updates before start listening new updates
    executor.start_polling(dp, skip_updates=False)
