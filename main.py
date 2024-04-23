import os # модуль для роботи з операційною системою(файлова система)
import tkinter as tk # модуль для роботи з графічним інтерфейсом
from dotenv import load_dotenv # модуль для роботи з файлом .env
from db import DB # модуль для роботи з класом де підключається база даних
from tables import Tables # модуль для роботи з класом де виводиться список таблиць
from query_with_show import QueryWithShowing # модуль для роботи з класом де виводиться запит з виведенням
from query_without_show import QueryWithoutShow # модуль для роботи з класом де виводиться запит без виведення

load_dotenv() # виклик функції для роботи з файлом .env

db = DB(host="localhost", user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database="new_ayction")
cursor = db.cursor
tables = Tables()
show_query = QueryWithShowing()
execute_query = QueryWithoutShow()


def yes_window():
    new_window = tk.Toplevel()  # Створення нового вікна
    new_window.title("Нове вікно")  # Встановлення заголовку для нового вікна
    new_window.geometry("400x300")  # Збільшення розмірів вікна
    new_window.configure(bg="grey20") # Встановлення коліру фону
    return new_window


def yes_window_text(new_window):
    label = tk.Label(new_window, text="Це нове вікно", bg="grey50") # Встановлення тексту bg = background
    label.pack()    # Виведення тексту


def yes_window_buttons(new_window):
    entry_with_show_button = tk.Button(new_window, text="Запит з виведенням", command=show_query.entry_query,
                                       width=show_query.button_width(20), height=2, bg="gold") # Встановлення кнопки з відповідними функціями
    entry_without_show_button = tk.Button(new_window, text="Запит з оновленням/\nвставленням/\nвидаленням даних",
                                          command=execute_query.result_without_show, width=show_query.button_width(20),
                                          height=2, bg="gold")
    exit_button = tk.Button(new_window, text="Вийти", command=lambda: show_query.destroy_window(new_window),
                            font=show_query.font(12), width=20, bg="gold")

    entry_with_show_button.pack(pady=5) # Виведення кнопок
    entry_without_show_button.pack(pady=10) # pady - відступи по y
    exit_button.pack(pady=15)


def create_new_window_yes():
    new_window = yes_window() # Створення нового вікна
    yes_window_text(new_window) # Додавання тексту
    yes_window_buttons(new_window) # Додавання кнопок
    # Додавання кнопок з відповідними функціями


def main_window():
    root = tk.Tk() # Створення головного вікна
    root.title("Графічний інтерфейс") # Встановлення заголовку
    root.geometry("1200x800")  # Встановлення розмірів вікна
    root.configure(bg="grey20") # Встановлення коліру фону
    return root # Повернення головного вікна


def main_buttons(frame, root):
    table_button = tk.Button(frame, text="Вивести список таблиць", command=tables.show_tables, font=show_query.font(14),
                             width=show_query.button_width(20), bg="gold", fg="grey20") # fg = foreground
    yes_button = tk.Button(frame, text="Так", command=create_new_window_yes, font=show_query.font(14),
                           width=show_query.button_width(20), bg="gold", fg="grey20")
    no_button = tk.Button(frame, text="Ні", command=lambda: show_query.destroy_window(root), font=show_query.font(14),
                          width=show_query.button_width(20), bg="gold", fg="grey20")

    table_button.grid(row=1, column=0, padx=10, pady=(20, 0), columnspan=2, sticky="ew") # padx - відступи по x, sticky - вирівнювання, columnspan - зайнятість стовпців
    yes_button.grid(row=0, column=0, pady=(10, 20), sticky="e")
    no_button.grid(row=0, column=1, pady=(10, 20), sticky="w")


def main_text(root):
    label = tk.Label(root, text="Бажаєте ввести запит?", font=show_query.font(14), bg="grey50") # Встановлення тексту
    label.pack() # Виведення тексту


def container_of_widgets(root):
    frame = tk.Frame(root, bg="grey20") # Створення контейнера для кнопок
    frame.pack() # Виведення контейнера
    return frame # Повернення контейнера


def main():
    if not db:
        return
    root = main_window() # Створення головного вікна
    main_text(root) # Додавання тексту
    frame = container_of_widgets(root) # Створення контейнера для кнопок
    main_buttons(frame, root) # Додавання кнопок
    root.mainloop() # Виведення головного вікна


if __name__ == "__main__": # Перевірка чи файл є головним
    main() # Виклик функції main()
