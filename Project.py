from editor import editor

class project():
    def __init__(self, name, is_old_project, old_project_file):
        self.name = name

        self.is_old_project = is_old_project
        self.old_project_file = old_project_file

        self.editor = editor(self, self.is_old_project, self.old_project_file)





