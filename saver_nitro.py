
import sqlite3
import os

class saver():
    def __init__(self, obj_lst, file_name, obj_table_name, is_old_project, is_compiled):
        self.obj_lst = obj_lst
        self.file_name = file_name
        self.obj_table_name = obj_table_name
        self.dir_name = "/home/eme/" + self.file_name + "_project/"
        self.file = self.dir_name + self.file_name
        self.is_compiled = is_compiled
        self.compile_state_int = 0 #0 = no, 1 = yes

        if self.is_compiled:
            self.compile_state_int = 1
        else:
            self.compile_state_int = 0

        #print(self.file)
        self.is_old_project = is_old_project
        if self.is_old_project == False:
            self.create_new_objs_table_if_not_found()
            self.create_project_state_table_if_not_found()


    def create_project_state_table_if_not_found(self):
        try:
            self.conn = sqlite3.connect(self.file)
            self.cursor = self.conn.cursor()
            query = 'CREATE TABLE IF NOT EXISTS project_state (is_compiled INTEGER);'
            self.cursor.execute(query)
            self.conn.commit()
            self.conn.close()
        except sqlite3.Error as e:
            print("Error came out! ", e)


    def compile_table(self):
        try:
            self.conn = sqlite3.connect(self.file)
            self.cursor = self.conn.cursor()
            query = 'INSERT INTO project_state(is_compiled)VALUES(' + str(1) + ');'
            self.cursor.execute(query)
            self.conn.commit()
            self.conn.close()
        except sqlite3.Error as e:
            print("Error came out! ", e)




    def create_new_objs_table_if_not_found(self):
        try:
            os.mkdir(self.dir_name)
            self.conn = sqlite3.connect(self.file)
            self.cursor = self.conn.cursor()
            print(self.obj_table_name)
            self.cursor.execute('CREATE TABLE IF NOT EXISTS ' + self.obj_table_name + '(name text UNIQUE, pos_x REAL, pos_y REAL, img_source text, scale_x REAL, scale_y REAL);')
            self.conn.commit()
            self.conn.close()
        except sqlite3.Error as e:
            print("Error came out! ", e)

    def save(self, is_compiled):
        self.is_compiled = is_compiled

        self.conn = sqlite3.connect(self.file)
        self.cursor = self.conn.cursor()
        for obj in self.obj_lst:
            query = ""
            if obj.img != None:
                query = 'INSERT INTO ' + self.obj_table_name + "(name, pos_x, pos_y, img_source, scale_x, scale_y)VALUES('" + obj.name + "'," + str(obj.pos_x) + "," + str(obj.pos_y) + ",'" + str(obj.img_source) + "'," + str(obj.scale_x) + "," + str(obj.scale_y) + ");"
            else:
                query = 'INSERT INTO ' + self.obj_table_name + "(name, pos_x, pos_y, img_source, scale_x, scale_y)VALUES('" + obj.name + "'," + str(obj.pos_x) + "," + str(obj.pos_y) + ", 'None'," + str(obj.scale_x) + "," + str(obj.scale_y) + ");"
            print(query)
            self.cursor.execute(query)

        self.conn.commit()
        self.conn.close()