import pygame


class BoxCollider():
    def __init__(self, GameObject, lst):
        self.GameObject = GameObject
        self.name = "BoxCollider"
        self.lst = lst
        self.is_collided_left = False
        self.is_collided_right = False
        self.is_collided_top = False
        self.is_collided_bottom = False

    def work(self):
        for obj in self.lst:
            if obj != self.GameObject:

                can_continue = False
                for x in obj.components_lst:
                    if x.name == self.name:
                        can_continue = True
                    else:
                        can_continue = False

                if can_continue:
                    if self.GameObject.Rect.colliderect(obj.Rect):
                        print("Collided with " + obj.name)
                        if self.GameObject.Rect.right >= obj.Rect.left:
                            if self.GameObject.Rect.right <= obj.Rect.right:
                                self.is_collided_right = True
                            else:
                                self.is_collided_right = False
                        else:
                            self.is_collided_right = False

                        if self.GameObject.Rect.left <= obj.Rect.right:
                            if self.GameObject.Rect.left >= obj.Rect.left:
                                self.is_collided_left = True
                            else:
                                self.is_collided_left = False
                        else:
                            self.is_collided_left = False

                        if self.GameObject.Rect.bottom >= obj.Rect.top:
                            if self.GameObject.Rect.bottom <= obj.Rect.bottom:
                                self.is_collided_bottom = True
                            else:
                                self.is_collided_bottom = False
                        else:
                            self.is_collided_bottom = False

                        if self.GameObject.Rect.top <= obj.Rect.bottom:
                            if self.GameObject.Rect.top >= obj.Rect.top:
                                self.is_collided_top = True
                            else:
                                self.is_collided_top = False
                        else:
                            self.is_collided_top = False


                        print(str(self.is_collided_left) + ", " + self.name)
                        print(str(self.is_collided_right) + ", " + self.name)
                else:
                    self.is_collided_left = False
                    self.is_collided_top = False
                    self.is_collided_bottom = False
                    self.is_collided_right = False
