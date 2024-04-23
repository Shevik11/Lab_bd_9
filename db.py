import mysql.connector # Імпортуємо бібліотеку для роботи з базою даних


class DB:

    def __init__(self, host: str, user: str, password: str, database: str): # Конструктор класу , init - ініціалізація
        self.connection = mysql.connector.connect( # Підключення до бази даних
            host=host,
            user=user,
            password=password,
            database=database,
            autocommit=True # Автоматичне підтвердження
        )
        self.cursor = self.connection.cursor() # Створення курсора
