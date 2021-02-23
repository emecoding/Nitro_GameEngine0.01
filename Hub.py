from Project import project as p
from tkinter import filedialog
from tkinter import *
import sys

class hub():
    def __init__(self):
        self.old_project = None
        


        self.create_win()

    def create_win(self):
        self.win = Tk()
        self.win.title("Hub 0.01")
        self.win.geometry("800x800")
        self.widgets_to_hub()
        self.win.mainloop()


    def widgets_to_hub(self):
        new_project_btn = Button(self.win, text="Create new Project", command = self.create_new_project)
        new_project_btn.pack()

        open_old_project_btn = Button(self.win, text="Open old project", command = self.load_old_project)
        open_old_project_btn.pack()

        exit_btn = Button(self.win, text="Exit", command = sys.exit)
        exit_btn.pack()

    def load_old_project(self):
        self.old_project = filedialog.askopenfilename(title="Select old project", filetypes=(("DataBase", "*.db*"), ("All files","*.*")))
        print(str(self.old_project))
        p(str(self.old_project), True, self.old_project)
        self.win.destroy()



    def create_new_project(self):
        self.w = Toplevel()
        self.w.title("New Project")
        self.w.geometry("400x400")
        name_entry = Entry(self.w)
        b = Button(self.w, text="Create", command = lambda: self.apply_new_project(name_entry.get()))
        name_entry.pack()
        b.pack()

        self.w.mainloop()

    def apply_new_project(self, name):
        self.win.destroy()
        p(name, False, None)

h = hub()




