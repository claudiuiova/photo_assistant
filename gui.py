from tkinter import *

from src import file_manager, image_converter


manager = file_manager.FileManager()


class MainGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Photo Assistant")
        self.root.geometry('600x600')

        # --------------------------- START MENU BAR -----------------------------

        # create Menu bar
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # create file, view and help menu
        self.file_menu = Menu(self.menu_bar)
        self.view_menu = Menu(self.menu_bar)
        self.help_menu = Menu(self.menu_bar)

        self.file_menu.add_command(label="New", command=self.do_nothing)
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.view_menu.add_command(label="Theme", command=self.do_nothing)

        self.help_menu.add_command(label="About", command=self.do_nothing)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        # --------------------------- END MENU BAR -------------------------------

        # --------------------------- DEFINE FRAMES -------------------------------
        self.main_frame = Frame(self.root)
        self.buttons_frame = Frame(self.main_frame)

        self.main_frame.pack()
        self.buttons_frame.pack()

        # --------------------------- END FRAMES DEFINITION -------------------------------

        # --------------------------- DEFINE BUTTONS -------------------------------
        self.source_text_input = Text(self.main_frame, height=1, width=30)
        self.source_button = Button(self.main_frame, text="Source",
                                    command=lambda: manager.get_path(self.source_text_input, sd='s'))

        self.destination_text_input = Text(self.main_frame, height=1, width=30)
        self.destination_button = Button(self.main_frame, text="Destination",
                                         command=lambda: manager.get_path(self.destination_text_input, sd='d'))

        self.source_button.pack()
        self.source_text_input.pack()
        self.destination_button.pack()
        self.destination_text_input.pack()

        # --------------------------- END BUTTONS DEFINITION -------------------------------

        self.root.mainloop()

    def create(self):
        pass

    def do_nothing(self):
        pass
