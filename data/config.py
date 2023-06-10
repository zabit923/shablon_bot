import os
from dotenv import load_dotenv


load_dotenv()
# load_dotenv() - это функция загрузки переменных,
# которую необходимо вызвать перед использованием переменных из файла .env


BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
# переменная, которая получает значение переменной окружения BOT_TOKEN из файла .env


admins = [
    '00000000',    # это список, который содержит идентификаторы пользователей,
]                   # имеющих административный доступ к боту


chat_ids = [
    '00000000'
]



ip = os.getenv("ip")                        # IP DB
PGUSER = str(os.getenv("PGUSER"))           # Пользователь DB
PGPASSWORD = str(os.getenv("PGPASSWORD"))   # Пароль DB
DATABASE = str(os.getenv("DATABASE"))       # Название DB


POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'
