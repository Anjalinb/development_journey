class Editor:
    def open(self):
        print("editor open method")

    def execute(self):
        print("execute traditional way python module_name.py")

class Vscode(Editor):
    def open(self):
        print("open with code .")

vs_instance=Vscode()
vs_instance.open()
