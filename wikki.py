import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7511889467:AAFnpgjF7NsqpL0ykE8sD1rau-ZVr0x_v2o'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, proxy='http://proxy.server:3128')
dp = Dispatcher(bot)

start_keyboards = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton("Bosh sahifa"), types.KeyboardButton("Qidiruv🔎")],
    [types.KeyboardButton("UZ 🇺🇿"), types.KeyboardButton("RU 🇷🇺"), types.KeyboardButton("EN 🏴󠁧󠁢󠁥󠁮󠁧󠁿")]
], resize_keyboard=True)


@dp.message_handler(commands=['start'])
async def salom_ber(message: types.Message):
    await message.answer(text="Assalomu aleykum, xush kelibsiz!", reply_markup=start_keyboards)


@dp.message_handler(lambda massage: " Qidiruvv🔎" in massage.text)
async def salom_ber(message: types.Message):
    await message.answer(text="Wikipediadan qidirish qidirish ucun savol baring")
@dp.message_handler()
async def wiki_javob(massage: types.Message):
    savol = massage.text
    try:
        wikipedia.set_lang('uz')
        javob =wikipedia.summary(savol)
        await massage.answer(text=f"sizining savolingiz: {savol}\n\nJavvobimiz:\n{javob}")
    except:
        await massage.answer(text=f"sizining savolingiz: {savol}\n\nJavvobimiz:\nTopilmadi")

    try:
        wikipedia.set_lang('RU')
        javob =wikipedia.summary(savol)
        await massage.answer(text=f"sizining savolingiz: {savol}\n\nJavvobimiz:\n{javob}")
    except:
        await massage.answer(text=f"sizining savolingiz: {savol}\n\nJavvobimiz:\nTopilmadi")

    try:
        wikipedia.set_lang('EN')
        javob =wikipedia.summary(savol)
        await massage.answer(text=f"sizining savolingiz: {savol}\n\nJavvobimiz:\n{javob}")
    except:
        await massage.answer(text=f"sizining savolingiz: {savol}\n\nJavvobimiz:\nTopilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
