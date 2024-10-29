import tkinter as tk
from tkinter import ttk

class StyleTable:
    def __init__(self, parent):
        # Crear frame contenedor
        self.frame = tk.Frame(parent, bg="#f5f5f5", bd=2, relief="groove")

        # Estilo de la tabla
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Custom.Treeview",
            background="#ffffff",  # Fondo blanco para filas normales
            fieldbackground="#f0f0f0",  # Fondo del área de entrada
            foreground="#000000",  # Texto negro
            rowheight=30,  # Altura de las filas
            bordercolor="#999999",  # Bordes grises
            borderwidth=1,
        )
        style.map("Custom.Treeview", background=[("selected", "#c1e4e9")])

        style.configure(
            "Custom.Treeview.Heading",  # Corrección aquí
            background="#f5f5f5",
            foreground="#000000",
            font=("Helvetica", 16, "bold"),
        )

        self.tree = ttk.Treeview(
            self.frame,
            columns=("id", "Song", "Genre", "Origin"),
            show="headings",
            style="Custom.Treeview",
        )
        self.tree.heading("id", text="ID")
        self.tree.heading("Song", text="Cancion")
        self.tree.heading("Genre", text="Genero")
        self.tree.heading("Origin", text="Origen")

        for col in ("id", "Song", "Genre", "Origin"):
            self.tree.column(col, width=100, anchor="center")

        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.grid(column=0, row=0, sticky="nsew")
        scrollbar.grid(column=1, row=0, sticky="ns")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

    def load_data(self, data):

        for i, record in enumerate(data):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.tree.insert(
                "", "end", values=(
                    record.get("id"),  # Usa .get() para evitar KeyError
                    record.get("Song"),
                    record.get("Genre"),
                    record.get("Origin")
                ), tags=(tag,)
            )

        # Colores para las filas
        self.tree.tag_configure("evenrow", background="#ffffff")
        self.tree.tag_configure("oddrow", background="#f0f0f0")

    def get_frame(self):
        return self.frame
