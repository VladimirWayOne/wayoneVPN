import asyncio
from telebot.async_telebot import AsyncTeleBot
from telebot import TeleBot
from telebot import types

from dotenv import load_dotenv
import os
from utils.logger import setup_logger
from utils.db_actions import *

from connectors.db_con import PgSQLCon


from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
load_dotenv()

bot_logger = setup_logger('bot_log', 'bot_log.log')

# bot = AsyncTeleBot(os.getenv("bot_token"))
bot = AsyncTeleBot(os.getenv("BOT_TOKEN"))
db_con = PgSQLCon(dbname=os.getenv("DB_USER"), usr=os.getenv("DB_USER"), pwd=os.getenv(
    "DB_PWD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))


def vpn_actions_keyboard():
    # keyboard = [
    #     [
    #         InlineKeyboardButton("Добавить ключ", callback_data="1"),
    #         InlineKeyboardButton("Удалить ключ", callback_data="2"),
    #     ],
    #     [InlineKeyboardButton("Список ключей", callback_data="3")],
    # ]

    # return InlineKeyboardMarkup(keyboard)
    types.ReplyKeyboardRemove()
    menu_btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_btn1 = types.KeyboardButton("Добавить ключ")
    menu_btn2 = types.KeyboardButton("Удалить ключ")
    menu_btn3 = types.KeyboardButton("Список ключей")
    menu_btns.add(menu_btn1, menu_btn2, menu_btn3)
    return menu_btns


@bot.message_handler(commands=['help', 'start'])
async def start(message: types.Message):
    user_full_name = message.from_user.full_name
    user_id = message.from_user.id
    user_nick = message.from_user.username
    bot_logger.debug(f"{user_full_name},{user_id}, {user_nick}")
    add_user(db_con, user_id=user_id,
             fullname=user_full_name, username=user_nick)

    await bot.send_message(message.chat.id, 'Действия с ВПН:', reply_markup=vpn_actions_keyboard())


asyncio.run(bot.polling())
