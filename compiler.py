from tkinter import *

class Compiler():
    def __init__(self, editor):
        self.editor = editor

    def compile(self):
        self.editor.compiled = True
        self.editor.back_win.withdraw()
        self.editor.saver.compile_table()
        self.editor.play()

