import asyncio
from telegram import Bot

BOT_TOKEN = "8123803682:AAENNoQJnT63ErS5w0JdPg8r4q-sxx28rBs"
GROUP_ID = -1003663534213

async def test():
    bot = Bot(token=BOT_TOKEN)
    
    print("🧪 Тестирую отправку в группу...")
    
    try:
        # Пробуем отправить сообщение
        await bot.send_message(
            chat_id=GROUP_ID,
            text="🤖 ТЕСТ: Бот может отправлять сообщения в эту группу!"
        )
        print("✅ Сообщение отправлено в группу!")
        
        # Пробуем получить информацию о группе
        chat = await bot.get_chat(GROUP_ID)
        print(f"✅ Группа: {chat.title}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        print("\n🔧 Возможные проблемы:")
        print("1. Бот не добавлен в группу")
        print("2. Неправильный ID группы")
        print("3. Бот удален из группы")
        print("4. Группа не существует")
        
        # Проверяем бота
        try:
            me = await bot.get_me()
            print(f"\n✅ Бот активен: @{me.username}")
        except Exception as e2:
            print(f"\n❌ Бот не работает: {e2}")

if __name__ == '__main__':
    asyncio.run(test())