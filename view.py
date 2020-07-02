from tkinter import *
import clientTrans

class recevieFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.Rmessege = clientTrans.RC()
        self.message = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='留言信息 : ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.message).grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.message).insert(0, self.Rmessege)
        Button(self, text='修改', command=self.update).grid(row=3, stick=W, pady=10)

    def update(self):
        newMessege = self.message.get()
        while True:
            try:
                if clientTrans.trans(newMessege):
                    break
            except:
                clientTrans.trans(newMessege)

class aboutFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.about = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='''
        此程序是王硕做了一晚上做出来的
        虽然很垃圾
        但是因为垃圾只能出垃圾
        所以只能垃圾
        ''').pack()