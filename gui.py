#from . import verify
import tkinter
from tkinter import messagebox
import re

class Login(object):
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("单线交流")
        self.root.geometry('500x300')
 #运行代码时记得添加一个gif图片文件，不然是会出错的
        self.canvas = tkinter.Canvas(self.root, height=200, width=500)#创建画布
        self.image_file = tkinter.PhotoImage(file='1.png')#加载图片文件
        self.image = self.canvas.create_image(0,0, anchor='nw', image=self.image_file)#将图片置于画布上
        self.canvas.pack(side='top')#放置画布（为上端）

        #创建一个`label`名为`Account: `
        self.label_link = tkinter.Label(self.root, text='link')
        #创建一个`label`名为`Password: `
        self.label_password = tkinter.Label(self.root, text='password ')
        self.label_port = tkinter.Label(self.root, text='port')


        # 创建一个账号输入框,并设置尺寸
        self.input_link = tkinter.Entry(self.root, width=15)
        self.input_port = tkinter.Entry(self.root, width=7)
        # 创建一个密码输入框,并设置尺寸
        self.input_password = tkinter.Entry(self.root, show='😄', width=29)

        # 创建一个登录系统的按钮
        self.login_button = tkinter.Button(self.root, command = self.backstage_interface, text = "ENTER", width=10)

    # 完成布局
    def gui_arrang(self):
        self.label_link.place(x=60, y= 170)
        self.label_port.place(x=250, y=170)
        self.label_password.place(x=60, y= 195)
        self.input_link.place(x=135, y=170)
        self.input_port.place(x=290, y=170)
        self.input_password.place(x=135, y=195)
        self.login_button.place(x=140, y=235)

    def gui_arrang2(self):
        self.info = tkinter.Label(self.root, text='Login success!')
        self.info.place(x=140, y=235)

    def match(self, string, pattern):
        return re.search(pattern, string)
    # 进行登录信息验证
    def backstage_interface(self):
        link = self.input_link.get()
        port = self.input_port.get()
        password = self.input_password.get()

        link_pat = re.compile('^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$')
        port_pat = re.compile('^(102[4-9]|10[3-9]\d|1[1-9]\d\d|[2-9]\d{3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$') #正则匹配1024~65535

        #if (self.match(link_pat, link) and self.match(port_pat, port)):
         #   verifyResult = verify.verifyAccountData(link, port, password)
        verifyResult = True
        if verifyResult:
            self.root.destroy()

            self.root.geometry('500x300')
            self.canvas = tkinter.Canvas(self.root, height=200, width=500)  # 创建画布
            self.image_file = tkinter.PhotoImage(file='1.png')  # 加载图片文件
            self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)  # 将图片置于画布上
            self.canvas.pack(side='top')  # 放置画布（为上端）
            self.gui_arrang2()
        else:
            tkinter.messagebox.showinfo(title='影视资源管理系统', message='该账号不存在请重新输入!')


def main():
    # 初始化对象
    L = Login()
    # 进行布局
    L.gui_arrang()
    # 主程序执行
    tkinter.mainloop()


if __name__ == '__main__':
    main()