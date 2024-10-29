import tkinter as tk
from tkinter import messagebox
from StilTable import StyleTable


class HITMusicApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('HIT MUSIC')
        self.window.geometry('500x500')
        self.window.resizable(False, False)
        self.window.config(bg='white')

        self.style_table = StyleTable(self.window)  # Renombrado a style_table para consistencia
        self.style_table.get_frame().pack(expand=True, fill='both', pady=(10, 0))

        search_frame = tk.Frame(self.window, bg='white')
        search_frame.pack(pady=10)

        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.grid(row=0, column=0, padx=5)

        search_button = tk.Button(
            search_frame, text='Search', command=self.search_record
        )
        search_button.grid(row=0, column=1)

        self.data = []

    def load_data(self, data):
        self.data = data
        self.style_table.load_data(data)

    def search_record(self):
        search_number = self.search_entry.get()
        if not search_number.isdigit():
            messagebox.showerror("Error", "Ingrese un registro válido.")
            return

        # Cambiar "search" a la clave que estás buscando en tus datos
        record = next((r for r in self.data if r["id"] == search_number), None)  # Asegúrate de usar la clave correcta
        if record:
            self.show_record_popup(record)
        else:
            messagebox.showinfo("No encontrado", "No se encontró el registro.")

    def show_record_popup(self, record):
        popup = tk.Toplevel(self.window)
        popup.title(f"Música: {record['id']}")  # Asegúrate de que 'id' es la clave correcta
        popup.geometry('400x300')  # Ajustado el tamaño de la ventana emergente
        popup.configure(bg='white')

        for i, (key, value) in enumerate(record.items()):
            tk.Label(popup, text=f"{key}: {value}", bg="white", anchor="w").pack(
                fill="x", padx=10, pady=5
            )

    def run(self):
        self.window.mainloop()
