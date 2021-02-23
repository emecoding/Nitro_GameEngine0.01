import pygame
import sys
from tkinter import *
from tkinter import messagebox

from compiler import Compiler
from saver_nitro import saver
from GameObject import GameObject as o
from loader import loader
from Rigidbody import Rigidbody
from BoxCollider import BoxCollider
import os

pygame.init()

#widths: S: 400px, H: 200px, I: 300px

class editor():
    def __init__(self, project, is_old_project, old_project_files):
        self.project = project

        self.gameObjects_lst = []
        self.gameObjects_btns_lst = []

        self.inspector_label_is_in_use = False

        self.playing = False

        self.compiled = False
        self.compiler = Compiler(self)

        self.file_name = ""
        self.objs_table_name = "Objs"
        self.is_old_project = is_old_project
        self.old_project_file = old_project_files

        self.clock = pygame.time.Clock()


        self.set_up_editor()




        '''print(self.is_old_project)
        if self.is_old_project == True:
            print(self.old_project_file)
            self.loader = loader(self.old_project_file, self)
            self.loader.load()'''






    def generate_file_name(self):
        f_name = self.project.name + ".db"
        return f_name

    def set_up_editor(self):
        self.back_win = Tk()
        self.back_win.title("Project")
        self.back_win.geometry("+900+10")
        self.back_win.geometry("900x900")

        if self.is_old_project:
            self.set_up_scene_win()
            self.saver = saver(self.gameObjects_lst, self.old_project_file, self.objs_table_name, self.is_old_project, self.compiled)
            self.set_up_labels()
            self.loader = loader(self.old_project_file, self)
            self.file_name = self.old_project_file
            self.loader.load()
        else:
            self.set_up_scene_win()
            self.file_name = self.generate_file_name()
            self.saver = saver(self.gameObjects_lst, self.file_name, self.objs_table_name, self.is_old_project, self.compiled)
            self.set_up_labels()




        self.back_win.mainloop()

    def set_up_scene_win(self):
        self.scene_win = pygame.display.set_mode((600, 400))

    def set_up_labels(self):
        self.hierarchy_label = Label(self.back_win,)
        self.hierarchy_label.grid(row=0, column=0, padx=0, pady=0)

        self.inspector_label = Label(self.back_win)
        self.inspector_label.grid(row=0, column=0, padx=200)
        self.inspector_label.place(x=725, y=0)

        self.command_label = Label(self.back_win)
        self.command_label.grid(row=1, column=1, padx=900)
        self.command_label.place(x=0, y=700)

        create_new_gameObject_btn = Button(self.command_label, text="Create new GameObject", command = self.create_new_gameObject)
        create_new_gameObject_btn.pack()



        play_btn = Button(self.command_label, text="Play", command =self.play)
        play_btn.pack()

        save_btn = Button(self.command_label, text="Save", command= lambda: self.saver.save(self.compiled))
        save_btn.pack()

        compile_btn = Button(self.command_label, text="Compile", command = self.compiler.compile)
        compile_btn.pack()

        exit_btn = Button(self.command_label, text="Exit", command=self.exit)
        exit_btn.pack()

        #elf.hierarchy_label.pack()

    def stop_playing(self):
        if self.compiled == False:
            self.playing = False
            self.scene_win.fill((0, 0, 0))
            for obj in self.gameObjects_lst:
                obj.return_to_scene_pos()
                if obj.img != None:
                    obj.draw()
                print(obj.name + str(obj.scene_pos_x) + str(obj.pos_x))

            pygame.display.update()



    def editor_input_while_play(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.stop_playing()
            if event.type == pygame.QUIT:
                if self.compiled == True:
                    self.exit()


    def draw_objs(self):
        for x in self.gameObjects_lst:
            if x.img != None:
                x.draw()


    def play(self):
        x = 0
        self.playing = True
        while self.playing:
            self.scene_win.fill((255, 255, 255))
            self.editor_input_while_play()
            if len(self.gameObjects_lst) != 0:

                self.gameObjects_lst[x].my_components_work()

                if self.gameObjects_lst[x].has_input:
                    self.gameObjects_lst[x].input()
                self.draw_objs()
                #pygame.display.update()

                if((x + 1) <= (len(self.gameObjects_lst) - 1)):
                    x += 1
                else:
                    x = 0

                #print(x)

                pygame.display.update()
                pygame.display.flip()
            self.clock.tick(60)


    def create_new_gameObject(self):
        new_o = o("New GameObject", 100, 100, self.scene_win)
        print(new_o.name)
        if new_o.img != None:
            new_o.draw()
            pygame.display.update()
        self.gameObjects_lst.append(new_o)
        self.create_slot_for_new_gameObject(new_o)


    def create_slot_for_new_gameObject(self, GameObject):
        self.new_gameObject_btn = Button(self.hierarchy_label, text = GameObject.name, command = lambda: self.open_gameObject_in_inspector(GameObject))
        self.new_gameObject_btn.pack()
        self.gameObjects_btns_lst.append(self.new_gameObject_btn)

    def open_gameObject_in_inspector(self, GameObject):
        self.inspector_label_is_in_use = True
        self.update_inspector_label()
        name_entry = Entry(self.inspector_label)
        pos_x_entry = Entry(self.inspector_label)
        pos_y_entry = Entry(self.inspector_label)

        name_entry.insert(0, str(GameObject.name))
        pos_x_entry.insert(0, str(GameObject.pos_x))
        pos_y_entry.insert(0, str(GameObject.pos_y))

        set_img_btn = Button(self.inspector_label, text = "Set Img", command = GameObject.set_img)
        apply_btn = Button(self.inspector_label, text = "Apply", command = lambda: self.apply_new_settings(GameObject,name_entry.get(), pos_x_entry.get(), pos_y_entry.get()))
        add_component = Button(self.inspector_label, text="Add Component", command = lambda: self.add_component(GameObject))








        name_entry.pack()
        pos_x_entry.pack()
        pos_y_entry.pack()
        apply_btn.pack()
        set_img_btn.pack()
        add_component.pack()

        for component in GameObject.components_lst:
            b = Button(self.inspector_label, text=component.name, command = lambda: GameObject.edit_component(component))
            b.pack()


    def add_component(self, GameObject):
        self.w = Toplevel()
        self.w.title("New Component")

        rb_btn = Button(self.w, text="Rigidbody", command = lambda: self.apply_new_component(Rigidbody(GameObject, 4), GameObject))
        rb_btn.pack()
        bx_btn = Button(self.w, text="Box Collider", command = lambda: self.apply_new_component(BoxCollider(GameObject, self.gameObjects_lst), GameObject))
        bx_btn.pack()
        movement_btn = Button(self.w, text="Movement", command = lambda: self.give_movement(GameObject))
        movement_btn.pack()

        self.w.mainloop()

    def give_movement(self, GameObject):
        GameObject.has_movement = True
        self.w.destroy()
        self.update_inspector_label()

    def apply_new_component(self, component, GameObject):
        GameObject.add_component(component)
        self.w.destroy()
        self.inspector_label_is_in_use = True
        self.update_inspector_label()





    def apply_new_settings(self, GameObject ,name, pos_x, pos_y):
        GameObject.name = name
        GameObject.pos_x = int(pos_x)
        GameObject.pos_y = int(pos_y)

        i = 0
        for x in range(0, len(self.gameObjects_lst)):
            if self.gameObjects_lst[x] == GameObject:
                i = x

        self.gameObjects_btns_lst[i].configure(text=GameObject.name)

        self.scene_win.fill((0, 0, 0))
        for obj in self.gameObjects_lst:
            if obj.img != None:
                obj.draw()
                obj.set_scene_pos()

        pygame.display.update()



    def update_inspector_label(self):
        if self.inspector_label_is_in_use == True:
            self.inspector_label.destroy()
            self.inspector_label = Label(self.back_win)
            self.inspector_label.grid(row=0, column=0, padx=200)
            self.inspector_label.place(x=725, y=0)

            self.inspector_label_is_in_use = False


    def exit(self):
        self.playing = False
        #self.saver.save()
        pygame.quit()
        sys.exit()







