import tkinter
from tkinter import filedialog


class FileManager:
    def __init__(self):
        self.source_path = ''
        self.destination_path = ''

    def get_path(self, text_input, sd):
        if text_input.get('1.0', tkinter.END):
            text_input.delete('1.0', tkinter.END)

        path = filedialog.askdirectory()

        if sd in ['source', 's']:
            self.source_path = path
        elif sd in ['destination', 'd']:
            self.destination_path = path

        text_input.insert(tkinter.END, path)

