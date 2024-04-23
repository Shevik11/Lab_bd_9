class ChooseWindow:
    def yes_window_buttons(self, new_window):
        entry_with_show_button = tk.Button(new_window, text="Запит з виведенням", command=show_query.entry_query,
                                           width=20, height=2)
        entry_without_show_button = tk.Button(new_window, text="Запит з оновленням/\nвставленням/\nвидаленням даних",
                                              command=execute_query.func2, width=20, height=2)

        entry_with_show_button.pack(pady=1)
        entry_without_show_button.pack(pady=1)

    def create_new_window_yes():
        new_windowe = yes_window_text()
        yes_window_buttons(new_windowe)
        # Додавання кнопок з відповідними функціями

    def main_window():
        root = tk.Tk()
        root.title("Графічний інтерфейс")
        root.geometry("600x400")  # Встановлення розмірів вікна
        return root