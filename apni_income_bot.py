import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("8014237094:AAF-6SBRsWxUpvoDJk8_XN2k383d_a-M7Ro")
ADMIN_ID = int(os.getenv("814312475"))
CRYPTO_ADDRESS = os.getenv("0x1eC35a66e97fDE7f4d322d4d2870872057bC7ACa")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    text = (
        f"👋 Welcome to Apni Income!\n\n"
        f"💰 Send funds to this wallet:\n"
        f"{0x1eC35a66e97fDE7f4d322d4d2870872057bC7ACa}\nNetwork: ERC20\n\n"
        f"After sending, reply with your TXID or screenshot."
    )
    await msg.answer(text, parse_mode="Markdown")

if _name_ == "_main_":
    print("🚀 Apni Income Bot started successfully.")
    executor.start_polling(dp, skip_updates=True)
