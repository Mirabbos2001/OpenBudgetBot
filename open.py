from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
bot_token = "6506442545:AAGps5U7nLbTTtXfc9QvkmRb-S8uKKJGJ3I"
bot = Bot(token=bot_token)
dispatcher = Dispatcher(bot)
referral_counts = {}
Admin_Id = "5122685168"
@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    user_name = message.from_user.first_name.upper()
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = [
        types.KeyboardButton('🗳 Ovoz berish'),
        types.KeyboardButton('🔗 Havola'),
        types.KeyboardButton('💰 Balans'),
        types.KeyboardButton("📝 Qo'llanma"),
        types.KeyboardButton("🤖 Bot haqida")
    ]
    keyboard.add(*buttons)
    await message.reply(f"Assalomu alaykum {user_name}. Xush kelibsiz, Quyidagi tugmalardan birini tanlang👇👇",
                        reply_markup=keyboard)
@dispatcher.message_handler()
async def handle_message(message: types.Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_name = message.from_user.first_name.upper()
    url1 = "https://openbudget.uz/boards/initiatives/initiative/31/4a15f640-3eff-4640-ac32-f0dbf4403025"
    url = "https://t.me/OpenBudgetOlmos_bot"
    Admin_url="https://t.me/MirabbosAdminBot"
    html = '''Assalomu alaykum! Ushbu bot orqali ovozingizni berib 5000 so'm olay olasiz.
Sizning ovozingiz jamoamizning rivojlanishiga ahamiyatli hisoblanadi.
.'''
    if message.text == "🤖 Bot haqida":
        bot_info_text = "Bu bot orqali ovozingizni berib 5000 so'm ga ega bo'lasiz.\n\nSizning ovozingiz jamoamizning rivojlanishiga ahamiyatli hisoblanadi.\n Agarda do'stlaringizni ham pul topishini hohlasangiz '🔗 Havola' tugmasini bosib do'stlarga ulashing\n Unutmang! Ovoz berishni yakunlab ekranni skrishot qiling va uni bizga yuboring biz sizga 5 daqiqa ichida pulni tushirib beramiz  "
        await bot.send_message(chat_id, bot_info_text)

    elif message.text == '🗳 Ovoz berish':
        await bot.send_message(chat_id, text=message.text)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Ovoz berish", url=url1))
        await bot.send_message(chat_id, text="Quyidagi havolani bosing👇👇", reply_markup=keyboard)


    elif message.text == '🔗 Havola':
        referral_link = f"https://t.me/share/url?url={url} "
        referral_message = f"Iltimos do'stlaringizga quyidagi linkni  ulashing ularga ham pul ishlashda yordam bering. Bizning bot => @OpenBudgetOlmos_bot"
        referral_button = types.InlineKeyboardButton(text=f"Do'stlarni taklif qilish\nSizning ID raqamingiz {user_id}", url=referral_link)
        referral_keyboard = types.InlineKeyboardMarkup().add(referral_button)
        referral_counts[user_id] = referral_counts.get(chat_id, 0)
        await bot.send_photo(chat_id, photo=open("OpenPhoto.jpg", "rb"), caption=referral_message,
                             reply_markup=referral_keyboard)
    elif message.text == "📝 Qo'llanma":
        qollanma_send = html
        await bot.send_video(chat_id, video=open("openbudget.mp4", "rb"), caption=qollanma_send)

    elif message.text == "💰 Balans":
        referral_count = referral_counts.get(chat_id, 0)+1
        balance = 5000 * referral_count
        response_text = f"Assalomu alaykum {user_name}. Siz {referral_count} ta do'stingizni taklif qildingiz.\nSizning ID={user_id}"
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        buttons = [
            types.KeyboardButton("💳 Pulni yechib olish"),
            types.KeyboardButton("🚫 Orqaga qaytish")
        ]
        keyboard.add(*buttons)
        await bot.send_message(chat_id, text=response_text, reply_markup=keyboard)

    elif message.text == "💳 Pulni yechib olish":
        user_name = message.from_user.first_name

        keyboard1 = types.InlineKeyboardMarkup()
        keyboard1.add(types.InlineKeyboardButton(text="Ovoz berish", url=url1))

        withdrawal_message = f"Assalomu alaykum {user_name}! Pulni yechib olish uchun  => [Adminga yozish] tugmasini bosing va unga  bank karta raqamingizni yoki telefon raqamingizni quyidagi formatda yuboring: +998XXXXXXXXX."

        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        buttons = [
                types.KeyboardButton("💳 Pulni yechib olish"),
                types.KeyboardButton("🚫 Orqaga qaytish")
            ]
        keyboard.add(*buttons)

        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton(text="Adminga yozish", url=Admin_url)
        inline_keyboard.add(inline_button)

        await bot.send_message(message.chat.id, text=withdrawal_message, reply_markup=inline_keyboard)

    elif message.text == "🚫 Orqaga qaytish":
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        buttons = [
            types.KeyboardButton('🗳 Ovoz berish'),
            types.KeyboardButton('🔗 Havola'),
            types.KeyboardButton('💰 Balans'),
            types.KeyboardButton('📝 Qo\'llanma'),
            types.KeyboardButton("🤖 Bot haqida")
        ]
        keyboard.add(*buttons)
        await bot.send_message(chat_id, text="Bosh sahifaga qaytdingiz. Iltimos, quyidagi tugmalardan birini tanlang:", reply_markup=keyboard)
if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)