import io
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter,Command

API_TOKEN = '5430260479:AAFv03vcKPUNvJmBPsq9xlT7HhdFw6IIkP4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

start_keyboard= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-taom")
        ],
        [
            KeyboardButton(text="2-taom")
        ],
        [
            KeyboardButton(text="Ichimliklar")
        ],
        [
            KeyboardButton(text="Salatlar")
        ],
        ],
    resize_keyboard=True
)

taomlar_1_keyboard= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Shorva"),
            KeyboardButton(text="Mastava")
        ],
        [
            KeyboardButton(text="Chechevichniy sup"),
            KeyboardButton(text="Lag`mon"),
            KeyboardButton(text="Vegeterianskiy sup")
        ],
        [
            KeyboardButton(text="Orqaga")
        ],
        ],
    resize_keyboard=True
)

taomlar_2_keyboard= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Manti"),
            KeyboardButton(text="Somsa")
        ],
        [
            KeyboardButton(text="Osh"),
            KeyboardButton(text="Dimlama"),
            KeyboardButton(text="Qozon kabob")
        ],
        [
            KeyboardButton(text="Orqaga")
        ],
        ],
    resize_keyboard=True
)

Salatlar_keyboard= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Vinigred"),
            KeyboardButton(text="Olivie")
        ],
        [
            KeyboardButton(text="Sezar"),
            KeyboardButton(text="Grecheskiy"),
            KeyboardButton(text="Achuchuk")
        ],
        [

        ],
        [
            KeyboardButton(text="Orqaga")
        ],
        ],
    resize_keyboard=True
)

Ichimliklar_keyboard= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Fanta"),
            KeyboardButton(text="Pepsi")
        ],
        [
            KeyboardButton(text="Choy"),
            KeyboardButton(text="Limonad"),
            KeyboardButton(text="Suv")
        ],
        [
            KeyboardButton(text="Orqaga")
        ],
        ],
    resize_keyboard=True
)


@dp.message_handler(commands=["start"])
async def st_st(message: types.Message):
    await message.answer("Assalomu alaykum. Siz Restoran menyusiga kirdingiz", reply_markup=start_keyboard)

@dp.message_handler(text="1-taom")
async def taom_1(message: types.Message):
    await message.answer("1-taomni tanlang: ", reply_markup=taomlar_1_keyboard)


@dp.message_handler(text="Shorva")
async def shorva(message:types.Message):
    await message.answer("Shorvaning 1 kosasini narxi 16.000 sum")

@dp.message_handler(text="Mastava")
async def mastava(message: types.Message):
    await message.answer("Mastavaning 1 kosasini narxi 20.000 sum")

@dp.message_handler(text="Chechevichniy sup")
async def ch_sup(message: types.Message):
    await message.answer("Chechevichniy supning 1 kosasini narxi 26.000 sum")

@dp.message_handler(text="Lag`mon")
async def lamon(message:types.Message):
    await message.answer("Lag`monning 1 kosasini narxi 30.000 sum")

@dp.message_handler(text="Vegeterianskiy sup")
async def veg_sup(message:types.Message):
    await message.answer("Vegeterianskiy supning 1 kosasini narxi 40.000 sum")

@dp.message_handler(text="2-taom")
async def taom_2(message: types.Message):
    await message.answer("2-taomni tanlang: ", reply_markup=taomlar_2_keyboard)

@dp.message_handler(text="Manti")
async def manti(message: types.Message):
    await message.answer("Mantining 2ta sini narxi 5.000 sum")

@dp.message_handler(text="Somsa")
async def Somsa(message: types.Message):
    await message.answer("Somsaning 2ta sini narxi 7.000 sum")

@dp.message_handler(text="Osh")
async def Osh(message: types.Message):
    await message.answer("Oshning 1 kilogramini narxi 35.000 sum")

@dp.message_handler(text="Dimlama")
async def Dimlama(message: types.Message):
    await message.answer("Dimlamaning 1ta portiyasini narxi 30.000 sum")

@dp.message_handler(text="Qozon kabob")
async def Qozon_kabob(message: types.Message):
    await message.answer("Qozon kabobning 1ta portiyasini narxi 25.000 sum")

@dp.message_handler(text="Salatlar")
async def salat(message: types.Message):
    await message.answer("Salatni tanlang: ", reply_markup=Salatlar_keyboard)

@dp.message_handler(text="Vinigred")
async def Vinigred(message: types.Message):
    await message.answer("Vinigred salatining narxi 10.000 sum")

@dp.message_handler(text="Olivie")
async def Olivie(message: types.Message):
    await message.answer("Olivie salatining narxi 7.000 sum")

@dp.message_handler(text="Sezar")
async def sezar(message: types.Message):
    await message.answer("Sezar salatining narxi 15.000 sum")

@dp.message_handler(text="Grecheskiy")
async def G_salat(message: types.Message):
    await message.answer("Grecheskiy salatining narxi 8.000 sum")

@dp.message_handler(text="Achuchuk")
async def Achuchuk(message: types.Message):
    await message.answer("Achuchuk salatining narxi 5.000 sum")

@dp.message_handler(text="Ichimliklar")
async def ichimlik(message: types.Message):
    await message.answer("Ichimlik tanlang: ", reply_markup=Ichimliklar_keyboard)

@dp.message_handler(text="Fanta")
async def fanta(message: types.Message):
    await message.answer("Fantaning 1 litrini narxi 6.000 sum")

@dp.message_handler(text="Pepsi")
async def pepsi(message: types.Message):
    await message.answer("Pepsining 1litrini narxi 9.000 sum")

@dp.message_handler(text="Choy")
async def choy(message: types.Message):
    await message.answer("Choyning 1 choynagini narxi 4.000 sum")

@dp.message_handler(text="Limonad")
async def limonad(message: types.Message):
    await message.answer("Limonadning 1ta butlkasini narxi 10.000 sum")

@dp.message_handler(text="Suv")
async def suv(message: types.Message):
    await message.answer("Suvning 1 litrini narxi 3.000 sum")

@dp.message_handler(text="Orqaga")
async def orqa(message: types.Message):
    await message.answer("Bosh menyu",reply_markup=start_keyboard)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)