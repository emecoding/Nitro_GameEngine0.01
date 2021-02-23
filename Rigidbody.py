import pygame

class Rigidbody():
    def __init__(self, GameObject ,gravity):
        self.name = "Rigidbody"
        self.gravity = gravity

        self.attributes_lst = [self.gravity]

        self.obj = GameObject

    def work(self):
        if self.obj != None:
            bx = None
            for x in self.obj.components_lst:
                if x.name == "BoxCollider":
                    bx = x
                else:
                    bx = None

            if bx != None:
                if bx.is_collided_bottom == False:
                    self.obj.pos_y += self.gravity
            #("Working!" + self.obj.name + ", " + self.name)
            #print(self.gravity)


    def change_gravity(self, new_gravity):
        self.gravity = int(new_gravity)