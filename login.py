from tkinter import *
from tkinter.messagebox import *
from clientCheck import *
import globalVar as gl
from mainPage import *
import hashlib



#实现密码求散列的功能
def sha256(s):
    return hashlib.sha256(str(s).encode('utf-8')).hexdigest()
class login(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 220))  # 设置窗口大小
        self.addr = StringVar()
        self.port = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='addr: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.addr).grid(row=1, column=1, stick=E)
        Label(self.page, text='port: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.port).grid(row=2, column=1, stick=E)
        Label(self.page, text='pass: ').grid(row=3, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=3, column=1, stick=E)
        Button(self.page, text='login', command=self.loginCheck).grid(row=4, stick=W, pady=10)
        Button(self.page, text='exit', command=self.page.quit).grid(row=4, column=1, stick=E)

    def loginCheck(self):
        gl._init()

        addr = self.addr.get()
        port = self.port.get()
        password = self.password.get()

        addr_pat = re.compile('^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$')
        port_pat = re.compile('^(102[4-9]|10[3-9]\d|1[1-9]\d\d|[2-9]\d{3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$')  # 正则匹配1024~65535
        #因为会对password进行sha256 所以不用限制密码的长度 客户端同理
        if (re.match(addr_pat, addr) and re.match(port_pat, port)):
            K = loginCheck(addr, port, sha256(password))
            if (K):
                gl.set_value('addr', addr)
                gl.set_value('port', port)
                gl.set_value('password', password)
                _Xa = gl.get_value('_Xa')
                _Q = gl.get_value('q')
                K = str(pow(int(K), _Xa, _Q))[:16].rjust(16, '0')
                gl.set_value('key', K)
                self.page.destroy()
                mainPage(self.root)
            else:
                showinfo(title='错误', message='地址|端口|密码：输入错误')
        else:
            showinfo(title='错误', message='请输入合法的地址和端口(>1023)')