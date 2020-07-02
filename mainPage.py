from tkinter import *
from view import *
import globalVar as gl

class mainPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (300, 220))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.Rpage = recevieFrame(self.root)  # 创建不同Frame
        self.Apage = aboutFrame(self.root)

        self.Rpage.pack()  # 默认收发信息的页面

        menubar = Menu(self.root)
        menubar.add_command(label='收发信息', command=self.recevieData)
        menubar.add_command(label='关于', command=self.aboutData)
        self.root['menu'] = menubar  # 设置菜单栏

    def recevieData(self):
        self.Rpage.pack()
        self.Apage.pack_forget()

    def aboutData(self):
        self.Rpage.pack_forget()
        self.Apage.pack()