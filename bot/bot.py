from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
import asyncio

BOT_TOKEN = "8335945023:AAESENAilsT0kuo6Xfqy9evYESYJAOl7PtI"
WEBAPP_URL = "https://<your-github-username>.github.io/<repo>/index.html"  # <-- replace with your GitHub Pages URL

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton("🚀 Открыть игру", web_app=WebAppInfo(url=WEBAPP_URL)))
    await msg.answer("Нажми кнопку, чтобы открыть MiniApp:", reply_markup=kb)

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
