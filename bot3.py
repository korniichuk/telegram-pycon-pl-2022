#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name: bot3
# Description: Asynchronous NBP bot with pyTelegramBotAPI
# Version: 0.1a1
# Owner: Ruslan Korniichuk

import asyncio
import os

from dotenv import load_dotenv
import telebot
from telebot.async_telebot import AsyncTeleBot

from nbp import get_rate, get_table

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = AsyncTeleBot(TOKEN, parse_mode='MARKDOWN')

markup = telebot.types.InlineKeyboardMarkup()
a = telebot.types.InlineKeyboardButton('table A', callback_data='a')
b = telebot.types.InlineKeyboardButton('table B', callback_data='b')
c = telebot.types.InlineKeyboardButton('table C', callback_data='c')
markup.row(a, b, c)


@bot.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, "🔥 Hello, World!",
                           reply_markup=markup)


@bot.message_handler(commands=['a'])
async def table_a(message):
    await bot.send_message(message.chat.id, get_table('a'))


@bot.message_handler(commands=['b'])
async def table_b(message):
    bot.send_message(message.chat.id, get_table('b'))


@bot.message_handler(commands=['c'])
async def table_c(message):
    await bot.send_message(message.chat.id, get_table('c'))


@bot.callback_query_handler(func=lambda call: True)
async def callback_querry(call):
    await bot.send_message(call.message.chat.id, get_table(call.data))


@bot.inline_handler(lambda query: query.query == 'rate')
async def query(inline_query):
    r1 = telebot.types.InlineQueryResultArticle(
            '1', 'USD', telebot.types.InputTextMessageContent(
                    get_rate('usd'),
                    parse_mode='MARKDOWN'))
    r2 = telebot.types.InlineQueryResultArticle(
            '2', 'EUR', telebot.types.InputTextMessageContent(
                    get_rate('eur'), parse_mode='MARKDOWN'))
    r3 = telebot.types.InlineQueryResultArticle(
            '3', 'GBP', telebot.types.InputTextMessageContent(
                    get_rate('gbp'), parse_mode='MARKDOWN'))
    await bot.answer_inline_query(inline_query.id, [r1, r2, r3])


asyncio.run(bot.infinity_polling())
