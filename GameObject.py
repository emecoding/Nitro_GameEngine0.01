import pygame
from tkinter import filedialog
from tkinter import *
from Rigidbody import Rigidbody

class GameObject():
    def __init__(self, name, pos_x, pos_y, screen):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.scene_pos_x = self.pos_x
        self.scene_pos_y = self.pos_y

        self.scale_x = 32
        self.scale_y = 32

        self.img = None
        self.has_img = False
        self.has_movement = False
        self.screen = screen

        self.has_input = True
        self.img_source = ""

        self.components_lst = []
        self.Rect = pygame.Rect(self.pos_x, self.pos_y, self.scale_x, self.scale_x)

    def set_img(self):
        file = filedialog.askopenfilename(title="Select Image",
                                          filetypes=(("png", "*.png*"), ("all files", "**")))
        print(file)


        new_img = pygame.image.load(file)
        self.img_source = file


        new_img = pygame.transform.scale(new_img, (self.scale_x, self.scale_y))
        self.img = new_img
        self.has_img = True
        self.draw()
        pygame.display.update()


    def add_component(self, new_component):
        self.components_lst.append(new_component)


    def edit_component(self, component_to_edit):
        print(component_to_edit.name)


    def draw(self):
        self.Rect = pygame.Rect(self.pos_x, self.pos_y, self.scale_x, self.scale_x)
        self.screen.blit(self.img, (self.pos_x, self.pos_y))
        #pygame.display.update()


    def my_components_work(self):
        self.Rect = pygame.Rect(self.pos_x, self.pos_y, self.scale_x, self.scale_x)
        for component in self.components_lst:
            component.work()

    def set_scene_pos(self):
        self.scene_pos_x = self.pos_x
        self.scene_pos_y = self.pos_y

    def return_to_scene_pos(self):
        self.pos_x = self.scene_pos_x
        self.pos_y = self.scene_pos_y


    def move_with_collisions(self):
        bx = None
        for c in self.components_lst:
            if c.name == "BoxCollider":
                bx = c
            else:
                bx = None

        self.has_movement = True
        if bx != None:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                if bx.is_collided_left == False:
                    self.pos_x -= 10

            if keys[pygame.K_d]:
                if bx.is_collided_right == False:
                    self.pos_x += 10
        else:
            self.move()



    def move(self):
        self.has_movement = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.pos_x -= 10

        if keys[pygame.K_d]:
            self.pos_x += 10


    def input(self):
        self.has_input = True
        if self.has_movement:
            self.move_with_collisions()




