async def on_startup(dp):
    import filters  # Импортируем фильтры
    filters.setup(dp)  # Устанавливаем фильтры

    from loader import db
    from utils.db_api.DB import on_startup
    print('Подключение к PostgreSQL')
    await on_startup(dp)

    # print('Удаление базы данных')
    # await db.gino.drop_all()

    print('Создание таблиц')
    await db.gino.create_all()
    print('Готово')

    from utils.notify_admins import on_startup_notify  # Импортируем on_startup_notify
    await on_startup_notify(dp)  # on_startup_notify отправляет уведомление администраторам о запуске бота

    print('Бот запущен')  # Выводим сообщение о запуске в терминале



if __name__ == '__main__':  # Запуск бота
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

    # запускается цикл обработки сообщений с помощью функции "executor.start_polling()".
    # В этой функции передается обработчик "dp" и функция "on_startup", которая будет вызвана после запуска бота.
    # Аргумент "skip_updates" означает, что бот будет игнорировать сообщения, пришедшие, пока он был выключен.

