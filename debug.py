from telegram import Bot
import asyncio

BOT_TOKEN = "8123803682:AAENNoQJnT63ErS5w0JdPg8r4q-sxx28rBs"

async def get_updates():
    bot = Bot(token=BOT_TOKEN)
    
    # Получаем последние обновления
    updates = await bot.get_updates(limit=10)
    
    print(f"Последние {len(updates)} обновлений:")
    print("-" * 50)
    
    for update in updates:
        if update.message:
            print(f"Чат ID: {update.message.chat.id}")
            print(f"Тип чата: {update.message.chat.type}")
            print(f"Название: {update.message.chat.title if update.message.chat.title else 'Нет'}")
            print(f"Текст: {update.message.text}")
            print("-" * 30)

asyncio.run(get_updates())