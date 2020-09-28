#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see rawapibot.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
import logging
import telegram
import telebot
from telegram.error import NetworkError, Unauthorized
from time import sleep


update_id = None

BOT_TOKEN = '1200994135:AAGwosYLPwpVDfLahuBIjNduhsMq2WMrp1Q'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
if message.text.lower() == 'привет':
bot.send_message(message.chat.id, 'Привет, мой создатель')
elif message.text.lower() == 'пока':
bot.send_message(message.chat.id, 'Прощай, создатель')

bot.polling())