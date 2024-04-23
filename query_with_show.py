import csv # Імпортуємо модуль для роботи з csv-файлами
import mysql.connector # Імпортуємо модуль для роботи з базою даних
from db import DB # Імпортуємо модуль для роботи з класом де підключається база даних
import os # Імпортуємо модуль для роботи з операційною системою(файлова система)
from tkinter import messagebox  # Імпортуємо модуль для роботи з вікнами
from dotenv import load_dotenv # Імпортуємо модуль для роботи з файлом .env
import tkinter as tk # Імпортуємо модуль для роботи з графічним інтерфейсом

load_dotenv() # виклик функції для роботи з файлом .env

db = DB(host="localhost", user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database="new_ayction")
cursor = db.cursor # Створення курсора


class QueryWithShowing:
    def __init__(self): # Конструктор класу , init - ініціалізація
        self.bg_color = "grey20" # Встановлення коліру фону , self - поточний об'єкт
        self.fg_color = "gold" # Встановлення коліру тексту

    def font(self, number):
        return "Arial", number   # Встановлення шрифту


    def button_width(self, number):
        return number * 10 # Встановлення ширини кнопки

    def handle_query_execution_errors(self, error_message):
        messagebox.showerror("Помилка", error_message) # Виведення повідомлення про помилку
        pass

    def destroy_window(self, window_name):
        window_name.destroy() # Закриття вікна

    def save_to_csv_file(self, result):
        result_window = self.display_write_query() # Створення вікна для виведення запиту
        with open("query_result.csv", "w", newline="") as csvfile: # Відкриття csv-файлу
            csv_writer = csv.writer(csvfile) # Створення об'єкту для запису в csv-файл
            # Записуємо заголовки (назви стовпців)
            csv_writer.writerow([i[0] for i in cursor.description]) # description - опис
            # Записуємо дані
            for row in result:
                csv_writer.writerow(row) # Записуємо рядки
            messagebox.showinfo("Повідомлення", "Файл успішно збережено") # Виведення повідомлення про успішне збереження файлу
            self.destroy_window(result_window) # Закриття вікна
            self.destroy_window(self.command_window) # Закриття вікна

    def display_write_query(self):
        result_window = tk.Toplevel()  # Створення нового вікна
        result_window.title("Результати запиту") # Встановлення заголовку для нового вікна
        return result_window # Повернення вікна

    def write_column(self, column_names, result_window):
        for i, column_name in enumerate(column_names): # enumerate - перераховує елементи
            label = tk.Label(result_window, text=column_name) # Виведення назв стовпців
            label.grid(row=0, column=i) # Виведення стовпців

    def write_rows(self, results, result_window):
        global row_index # Глобальна змінна для того щоб використовувати її в інших функціях
        for row_index, row in enumerate(results): # enumerate - перераховує елементи
            for column_index, value in enumerate(row): # enumerate - перераховує елементи
                label = tk.Label(result_window, text=value) # Виведення рядків
                label.grid(row=row_index + 1, column=column_index) # Виведення рядків

        return row_index # Повернення номеру рядка

    def csv_buttons(self, result_window, results, column_names, row_index, save_to_csv_file): # Створення кнопок
        save_csv_button = tk.Button(result_window, text="Зберегти в CSV",
                                    command=lambda: save_to_csv_file(results)) # lambda - функція з параметрами
        save_csv_button.grid(row=row_index + 2, column=0, columnspan=len(column_names)) # Виведення кнопки

    def entry_query(self):
        self.command_window = self.window_to_entry_query() # Створення вікна для вводу запиту
        self.command_entry = self.window_to_entry_query_text(self.command_window) # Створення поля вводу
        self.window_entry_query_buttons() # Створення кнопок

    def window_to_entry_query(self):
        command_window = tk.Tk() # Створення вікна
        command_window.title("Введення команди") # Встановлення заголовку
        command_window.geometry("400x200") # Встановлення розмірів вікна
        command_window.configure(bg=self.bg_color) # Встановлення коліру фону
        return command_window # Повернення вікна

    def window_to_entry_query_text(self, command_window):
        command_label = tk.Label(command_window, text="Введіть команду:", font=self.font(14), bg=self.bg_color,
                                 fg=self.fg_color) # Виведення тексту
        command_label.pack() # Виведення тексту

        command_entry = tk.Entry(command_window, font=self.font(14), bg="grey50", fg=self.fg_color) # Виведення поля вводу
        command_entry.pack() # Виведення поля вводу
        return command_entry # Повернення поля вводу

    def window_entry_query_buttons(self):
        save_button = tk.Button(self.command_window, text="Зберегти і виконати",
                                command=self.save_command_and_execute_query, font=self.font(14), bg=self.fg_color,
                                fg=self.bg_color) # Виведення кнопки

        save_button.pack() # Виведення кнопки

        exit_button = tk.Button(self.command_window, text="Вийти",
                                command=lambda: self.destroy_window(self.command_window),
                                font=self.font(14), bg=self.fg_color, fg=self.bg_color) # lambda - функція з параметрами
        exit_button.pack() # Виведення кнопки

    def check_command(self, command):
        if not command:
            self.handle_query_execution_errors("Поле команди порожнє. Введіть SQL-запит.") # Виведення повідомлення про помилку
            self.destroy_window(self.command_window) # Закриття вікна
            raise # зупинка виконання функції

    def check_syntax_command(self, error):
        if error.errno == 1064: # Перевірка чи є помилка синтаксису
            self.handle_query_execution_errors("Пиши по людськи") # Виведення повідомлення про помилку
            self.destroy_window(self.command_window) # Закриття вікна
        else:
            self.handle_query_execution_errors(f"Помилка при виконанні запиту: {error}") # Виведення повідомлення про помилку
            self.destroy_window(self.command_window) # Закриття вікна

    def save_command_and_execute_query(self):
        command = self.command_entry.get() # Отримуємо текст з поля вводу
        self.check_command(command) # Перевірка команди
        try:
            cursor.execute(command, multi=True) # Виконуємо запит
            result_window = self.display_write_query() # Створення вікна для виведення запиту
            column_names = [column[0] for column in cursor.description] # Отримуємо назви стовпців
            results = cursor.fetchall() # Отримуємо результати запиту
            self.write_column(column_names, result_window) # Виведення стовпців
            row_index = self.write_rows(results, result_window) # Виведення рядків
            self.csv_buttons(result_window, results, column_names, row_index, self.save_to_csv_file) # Виведення кнопок
        except mysql.connector.Error as error:
            self.check_syntax_command(error) # Перевірка синтаксису команди
