from db import DB # модуль для роботи з класом де підключається база даних
import os # модуль для роботи з операційною системою(файлова система)
from dotenv import load_dotenv # модуль для роботи з файлом .env
from tkinter import messagebox # модуль для роботи з вікнами
import tkinter as tk # модуль для роботи з графічним інтерфейсом
from query_with_show import QueryWithShowing # модуль для роботи з класом де виводиться запит з виведенням

load_dotenv() # виклик функції для роботи з файлом .env


db = DB(host="localhost", user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database="new_ayction")
cursor = db.cursor
window_to_entry_query = QueryWithShowing() # Створення об'єкту класу QueryWithShowing


class QueryWithoutShow:
    def __init__(self): # Конструктор класу , init - ініціалізація
        self.bg_color = "grey20" # Встановлення коліру фону , self - поточний об'єкт
        self.fg_color = "gold" # Встановлення коліру тексту

    def window_entry_query_buttons_without_show(self, command_window, command_entry):
        save_button = tk.Button(command_window, text="Зберегти і виконати",
                                command=lambda: self.save_command_and_execute_query_without_show(command_entry),
                                font=window_to_entry_query.font(14), bg=self.fg_color, fg=self.bg_color) # в 2 рядки бо так красиво виглядає
        save_button.pack()

        exit_button = tk.Button(command_window, text="Вийти",
                                command=lambda: window_to_entry_query.destroy_window(command_window), # lambda - функція з параметрами
                                font=window_to_entry_query.font(14),  bg=self.fg_color, fg=self.bg_color) # не дивуйтесь шо bg о fg , а fd то bg
        exit_button.pack()

    def save_command_and_execute_query_without_show(self, command_entry):
        command = command_entry.get() # Отримуємо текст з поля вводу
        cursor.execute(command) # Виконуємо запит
        messagebox.showinfo("Успішно", "Запит успішно виконано!") # Виводимо повідомлення про успішне виконання запиту

    def result_without_show(self):
        command_window = window_to_entry_query.window_to_entry_query() # Створення вікна для вводу запиту
        command_entry = window_to_entry_query.window_to_entry_query_text(command_window) # Створення поля вводу
        self.window_entry_query_buttons_without_show(command_window, command_entry) # Створення кнопок
        command_window.mainloop()   # Виведення вікна на екран
