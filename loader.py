import sqlite3
import pygame
from GameObject import GameObject as o

class loader():
    def __init__(self, file, e):
        self.file = file
        self.editor = e

    def load(self):
        self.conn = sqlite3.connect(self.file)
        self.cursor = self.conn.cursor()





        self.cursor.execute("SELECT * FROM Objs")
        objs_lst = self.cursor.fetchall()
        #print(objs_lst)
        for obj in objs_lst:
            name = obj[0]
            #print(name)
            pos_x = obj[1]
            pos_y = obj[2]
            img = obj[3]
            scale_x = obj[4]
            scale_y = obj[5]
            new_o = o(name, float(pos_x), float(pos_y), self.editor.scene_win)
            self.editor.create_slot_for_new_gameObject(new_o)

            new_o.scale_x = int(scale_x)
            new_o.scale_y = int(scale_y)


            if img != "None":
                i = pygame.image.load(img)
                i = pygame.transform.scale(i, (new_o.scale_x, new_o.scale_y))
                new_o.img = i
                new_o.draw()
            else:
                new_o.img = None

            self.editor.gameObjects_lst.append(new_o)

        self.cursor.execute("SELECT * FROM project_state")
        state_lst = self.cursor.fetchall()
        print(state_lst)
        for s in state_lst:
            is_compiled = s[0]
            print(is_compiled)
            if int(is_compiled) == 1:
                self.editor.compiled = True
                # self.editor.compiler.compile()
                print("is already compiled project!")
                self.editor.play()








