from tkinter import *
from login import *
import globalVar as gl

if __name__ == '__main__':
    root = Tk()
    root.title('单线通讯')
    login(root)
    root.mainloop()