from tkinter import filedialog

class FilePicker:
    def __init__(self):
        self.path = ""
    
    def run(self):
        self.path = filedialog.askopenfilename()
        return self.path
    