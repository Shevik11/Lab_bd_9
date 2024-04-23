from db import DB # Імпортуємо модуль для роботи з класом де підключається база даних
import os # Імпортуємо модуль для роботи з операційною системою(файлова система)
from dotenv import load_dotenv # Імпортуємо модуль для роботи з файлом .env
import tkinter as tk # Імпортуємо модуль для роботи з графічним інтерфейсом

load_dotenv() # виклик функції для роботи з файлом .env

db = DB(host="localhost", user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database="new_ayction")
cursor = db.cursor # Створення курсора


class Tables:
    def execute_query_show_table(self):
        cursor.execute("SHOW TABLES") # Виконуємо запит
        tables = [table[0] for table in cursor.fetchall()]  # Отримуємо список таблиць, fetchall() - повертає усі
        return tables # Повертаємо список таблиць

    def display_show_tables(self):
        root = tk.Tk() # Створення головного вікна
        root.title("Таблиці в MySQL базі даних") # Встановлення заголовку
        root.geometry("600x400")  # Збільшення розмірів вікна
        root.configure(bg="grey20") # Встановлення коліру фону
        return root # Повернення головного вікна

    def text_of_show_tables(self, root, execute_query_show_table):
        table_text = tk.Text(root, wrap=tk.WORD, bg="grey20", fg="grey20") # Створення текстового поля
        table_text.pack(fill="both", expand=True) # Виведення текстового поля
        table_text.config(state=tk.NORMAL) # Встановлення стану текстового поля
        tables = execute_query_show_table() # Отримуємо список таблиць

        table_text.tag_configure("custom_tag", foreground="gold", background="grey20") # Встановлення коліру тексту та фону

        for table in tables:
            table_text.insert(tk.END, table + "\n", "custom_tag") # Виведення таблиць

        table_text.config(state=tk.DISABLED) # Встановлення стану текстового поля

    def show_tables(self):
        if not db:
            return
        root = self.display_show_tables()  # Використовуйте self, оскільки це метод класу
        self.text_of_show_tables(root, self.execute_query_show_table)  # Використовуйте self
        root.mainloop() # Виведення вікна на екран
