from tkinter import *


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Photo Assistant")
        self.root.geometry('200x150')

        # create Menu bar
        self.menu_bar = Menu(self.root)

        # create file menu
        self.file_menu = Menu(self.menu_bar)
        self.file_menu.add_command(label="New", command=self.do_nothing)
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.frame = Frame(self.root)
        self.frame.pack()

        self.root.config(menu=self.menu_bar)
        self.root.mainloop()

    def create(self):
        pass

    def do_nothing(self):
        pass


if __name__ == "__main__":
    GUI()


