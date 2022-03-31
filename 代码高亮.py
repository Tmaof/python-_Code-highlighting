
# -*- coding: utf-8 -*-
# @Date    : 2022-3-27
# @Author  : tian maofu
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.formatters.rtf import RtfFormatter
from pygments.lexers import guess_lexer
import os
import pyperclip
import time
import sys,io

class codelight():
    def __init__(self):
        self.codestyle = 'default'

        # 将一个浏览器驱动放到程序根目录下,用户就不用配置浏览器驱动了
        outpath = os.getcwd()
        self.dirverfilename_chome = outpath + '\\chromedriver.exe'
        self.dirverfilename_edge=outpath + '\\msedgedriver.exe'
        self.dirverfilename=self.dirverfilename_edge
        self.start_onlineget=False
        #标识,防止多次响应键盘快捷键
        self.runing_eventhandler=False
        #代码高亮文本框(bool
        self.text_box=False


    # 网络得到
    def getcodelight_byonline(self):
        # 浏览器
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.keys import Keys
        import time

        #ctrl+,c
        self.ctrl_c()

        #删除
        self.backspace()

        # 从剪切版获取文本
        wenben_str=self.getcode()

        # 创建浏览器驱动
        #选择浏览器
        if self.dirverfilename == self.dirverfilename_chome:
            options = webdriver.ChromeOptions()
            prefs = {"profile.managed_default_content_settings.images": 2}  # 设置浏览器禁止加载图片
            options.add_experimental_option("prefs", prefs)
            # options.add_argument('--headless')# 关闭窗口后,无法复制
            options.add_argument('window-size=300x400')
            options.add_argument('--disable-gpu')  # 禁用显卡
            options.add_argument("--user-agent=Mozilla/5.0 HAHA")  # 替换UA

            chrome=webdriver.Chrome(chrome_options=options,service=Service(r'{}'.format(self.dirverfilename)))  # r 代表\号不转写,转义
            chrome.implicitly_wait(10)
            # options.add_argument('window-size=300x200')好像不行,用如下方法
            chrome.set_window_size(300, 400)
            # chrome.minimize_window()
            print("分辨率", chrome.get_window_size())

            # 网址
            chrome.get("https://highlightcode.com/")

            # 输入文本
            # time.sleep(0.5)
            element_textedit = chrome.find_element(By.ID, "textarea")
            element_textedit.clear()
            element_textedit.send_keys(wenben_str)

            # 点击
            time.sleep(0.1)
            element = chrome.find_element(By.CSS_SELECTOR, "div>button")
            element.click()

            # 跳转标签页
            time.sleep(0.3)  # 间隔太短,复制为空
            for handle in chrome.window_handles:
                # 先切换到该窗口
                chrome.switch_to.window(handle)
                # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
                if '复制即可' in chrome.title:
                    # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
                    break

            # 复制到剪切版
            # key_down(value, element=None) ——按下某个键盘上的键
            # key_up(value, element=None) ——松开某个键
            time.sleep(0.3)  # 间隔太短,复制为空
            element = chrome.find_element(By.CSS_SELECTOR, 'body > app-root > app-render > pre')
            action = ActionChains(chrome)
            action.key_down(Keys.CONTROL, element).send_keys("a").key_up(Keys.CONTROL, element).perform()  # ctrl+a
            # 如果不加元素element,也可以复制,不过格式不全
            '''
        不全的格式
            MainWindow::~MainWindow()
        {
            delete ui;
        }
        应该的格式
        1.
        MainWindow::~MainWindow()
        2.{
        3.    delete ui;
        4.}
            '''
            time.sleep(0.3)  # 间隔太短,复制为空
            action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()  # ctrl+c
            print('已复制')
            chrome.quit()

        else:
            from selenium.webdriver.edge.service import Service
            options = webdriver.EdgeOptions()
            prefs = {"profile.managed_default_content_settings.images": 2}  # 设置浏览器禁止加载图片
            options.add_experimental_option("prefs", prefs)
            # options.add_argument('--headless')# 关闭窗口后,无法复制
            options.add_argument('window-size=300x400')
            options.add_argument('--disable-gpu')  # 禁用显卡
            options.add_argument("--user-agent=Mozilla/5.0 HAHA")  # 替换UA

            edge = webdriver.Edge(options=options,service=Service(r'{}'.format(self.dirverfilename)))  # r 代表\号不转写,转义
            edge.implicitly_wait(10)
            # options.add_argument('window-size=300x200')好像不行,用如下方法
            edge.set_window_size(300, 400)
            # edge.minimize_window()
            print("分辨率", edge.get_window_size())

            # 网址
            edge.get("https://highlightcode.com/")

            # 输入文本
            # time.sleep(0.5)
            element_textedit = edge.find_element(By.ID, "textarea")
            element_textedit.clear()
            element_textedit.send_keys(wenben_str)

            # 点击
            time.sleep(0.1)
            element = edge.find_element(By.CSS_SELECTOR, "div>button")
            element.click()

            # 跳转标签页
            time.sleep(0.3)  # 间隔太短,复制为空
            for handle in edge.window_handles:
                # 先切换到该窗口
                edge.switch_to.window(handle)
                # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
                if '复制即可' in edge.title:
                    # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
                    break

            # 复制到剪切版
            # key_down(value, element=None) ——按下某个键盘上的键
            # key_up(value, element=None) ——松开某个键
            time.sleep(0.3)  # 间隔太短,复制为空
            element = edge.find_element(By.CSS_SELECTOR, 'body > app-root > app-render > pre')
            action = ActionChains(edge)
            action.key_down(Keys.CONTROL, element).send_keys("a").key_up(Keys.CONTROL, element).perform()  # ctrl+a
            # 如果不加元素element,也可以复制,不过格式不全
            '''
        不全的格式
            MainWindow::~MainWindow()
        {
            delete ui;
        }
        应该的格式
        1.
        MainWindow::~MainWindow()
        2.{
        3.    delete ui;
        4.}
            '''
            time.sleep(0.3)  # 间隔太短,复制为空
            action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()  # ctrl+c
            print('已复制')
            edge.quit()


        #粘贴:
        self.ctrl_v()

    #本地生成:
    # 将剪切板的文本(代码)转换成 高亮的 html文件 或者 rtf文件(word可度)
    # 再将文本读到剪切版

    # 函数1,获取剪切板代码
    def getcode(self):
        # 从剪切版获取文本
        code = pyperclip.paste()  # 从剪切版获取文本
        code = '''{}'''.format(code)
        #print(code)
        return code

        # 需要高亮的语言
        # 手动
        # lexer = PythonLexer()
        # lexer = get_lexer_by_name("python")#(二选一即可)
        # 自动判断语言
        # lexer = guess_lexer(code)

    # 两种方式获取高亮代码

    # 1 转换成html文件
    # 函数2
    def tohtml(self, code):
        # 自动判断语言
        lexer = guess_lexer(code)

        # 输出文件名,outfilename
        outpath = os.getcwd()
        outfilename = outpath + '\\temp.html'
        outcss = outpath + "\\temp.css"

        # 指定高亮风格,结合下拉框
        formatter = HtmlFormatter(style=self.codestyle)
        #其他参数:noclasses,nowrap,https://pygments.org/docs/formatters/
        if self.text_box==True:
            formatter.linenos = True

        # 获取css
        cssfile = open(outcss, "w")
        css = formatter.get_style_defs('.highlight')


        # print(css)
        cssfile.writelines(css)

        # 获取html
        htmlfile = open(outfilename, "w",encoding='utf-8')  # 直接打开一个文件，如果文件不存在则创建文件,
        # html = highlight(code, lexer,HtmlFormatter(), htmlfile)#可以直接写入,但我们需要链接css到html中,因此自己写
        html = highlight(code, lexer, formatter)
        htmlfile.write('<link rel="stylesheet" href="temp.css" type="text/css" /> \n')  # 把str写到文件中，write()并不会在str后加上一个换行符
        htmlfile.writelines(html)
        #print(html)

        # 关闭文件
        htmlfile.close()  # 关闭文件。python会在一个文件不用后自动关闭文件，不过这一功能没有保证，最好还是养成自己关闭的习惯。 如果一个文件在关闭后还对其进行操作会产生ValueError
        cssfile.close()
        return outfilename  # 返回文件的字符路径,不是htmlfile文件

    '''
    # 2 转换成rtf文件
    # 函数3
    def totrf(self, code):
        # 自动判断语言
        lexer = guess_lexer(code)

        # 输出文件名,outfilename
        outpath = os.getcwd()
        outfilename = outpath + '\\temp.rtf'
        trffile = open(outfilename, 'w')  # 打开输入文件

        trf = highlight(code, lexer, RtfFormatter(), trffile)  # 参数:代码,语言,格式,输出文件

        # 关闭
        trffile.close()

        return outfilename  # 返回文件的字符路径,不是htmlfile文件
    '''
    # 函数4,复制html中的文本
    def get_htmlText(self, htmlfile):
        # 浏览器
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.keys import Keys
        import time
        import os

        # 创建浏览器驱动
        # options.add_argument('--headless')# 关闭窗口后,无法复制
        if self.dirverfilename==self.dirverfilename_chome:
            chrome = webdriver.Chrome(service=Service(r'{}'.format(self.dirverfilename)))  # r 代表\号不转写,转义
            chrome.implicitly_wait(10)

            chrome.set_window_size(300, 400)
            # chrome.minimize_window()
            print("分辨率", chrome.get_window_size())

            # 网址,html文件
            chrome.get(htmlfile)

            # 复制文本
            action = ActionChains(chrome)
            action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()  # ctrl+a
            action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()  # ctrl+c

        else:
            edge=webdriver.Edge(service=Service(r'{}'.format(self.dirverfilename_edge)))
            edge.implicitly_wait(10)

            edge.set_window_size(300,400)
            edge.get(htmlfile)
            action=ActionChains(edge)
            action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()  # ctrl+a
            action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()  # ctrl+c

    '''
    # 函数5,插入光标,函数6将用到
    def doClick(self):
        import win32con
        import win32api,win32gui
        import pyautogui
        #获取窗口句柄:有一些窗口不能正常得到句柄

        # wdname = u'Microsoft Word 文档'
        # hwnd = win32gui.FindWindow(0, wdname)  # 父句柄
        # hwnd1 = win32gui.FindWindowEx(None,None,None, '网易有道词典')  # 子句柄FindWindowEx

        # 窗口大小
        # windowRec = win32gui.GetClientRect(hwnd1)  # 目标子句柄窗口的大小
        # print('windowRec',windowRec)#(676, 254, 1006, 724)#这个坐标不对

        #点击,无语了,不是我想要的点击
        #size = windowRec
        # sizew=size[2]
        # sizeh=size[3]
        # sizew=int(sizew/2)
        # sizeh=int(sizeh/2)
        # long_position = win32api.MAKELONG(340,170 )  # 模拟鼠标指针 传送到指定坐标 #long_position = win32api.MAKELONG(size[2]/2, size[3]/2)  # 模拟鼠标指针 传送到指定坐标
        # win32api.SendMessage(hwnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)  # 模拟鼠标按下
        # win32api.SendMessage(hwnd1, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)  # 模拟鼠标弹起

        # 点击#上面的坐标不对,只好,将文档窗口最大化,点击屏幕中间了
        # posx=windowRec[0]
        # posy=windowRec[1]
        # sizew=windowRec[2]
        # sizeh=windowRec[3]
        # sizew=int(sizew/2)
        # sizeh=int(sizeh/2)
        # pyautogui.click(posx, posy)
        # print('已点击')

        #最大化后点击
        pinmupos=pyautogui.size()#屏幕大小
        print('pinmupos', pinmupos)
        posx=pinmupos.width/2;print(posx) #pinmupos.width()/2 不对
        posy=pinmupos.height/2;print(posy)
        pyautogui.click(posx,posy)


    #函数6,复制rtf文件,#必须将word 程序窗口最大化,并且此方法使光标改变了,之后不好再原word中直接复制
    def get_rtfText_1(self,rtffile):
        from win32com.client import DispatchEx
        from win32com.client import Dispatch
        import win32api

        # 打开word应用程序
        word = Dispatch('Word.Application')#此方法不能指定程序,有一些word程序打开rtf文件后,不能直接复制,就需要移动光标
        #word = DispatchEx('Word.Application') # 启动独立的进程
        word.Visible = 1  # 0后台运行,不显示
        word.DisplayAlerts = 0  # 不警告

        #打开文档
        doc = word.Documents.Open(FileName=rtffile, Encoding='gbk')

        #必须将word 程序窗口最大化
        #插入光标,不像html文件打开那样,可以直接复制
        #self.doClick()

        # 复制ctrl+a,ctrl+c
        ob.ctrl_a_c()

        #关闭
        doc.Close()
        word.Quit()

    # 函数7
    def get_rtfText_2(slef,rtffile):
        import win32api

        outpath=os.getcwd()
        rtfexefile=r'F:\1\金山文档\金山文档.exe'
        # rtfexefile=outpath+'\\wordpad.exe'
        print(rtfexefile)
        # 打开记事本程序，获得其句柄
        win32api.ShellExecute(0, 'open', rtfexefile,'F:/temp.rtf', '', 0)
        print(rtffile)

                #如何关闭


    #函数8,rtf文件转pdf
    def wordTopdf(self,doc_name, pdf_name):
        """
        :word文件转pdf
        :param doc_name word文件名称
        :param pdf_name 转换后pdf文件名称
        """
        import os
        import sys
        from win32com import client
        # pip install win32com
        try:
            word = client.DispatchEx("Word.Application")#后台进程
            if os.path.exists(pdf_name):
                os.remove(pdf_name)
            worddoc = word.Documents.Open(doc_name, ReadOnly=1)
            worddoc.SaveAs(pdf_name, FileFormat=17)
            worddoc.Close()
            word.Quit()
            return pdf_name
        except:
            return 1
'''
    def ctrl_c(self):
        import win32api
        import win32con
        #win32api.keybd_event(0x11, win32api.MapVirtualKey(0x11, 0), win32con.KEYEVENTF_KEYUP, 0)#必须先释放ctrl ,因为快捷键有ctrl,人的释放可能太慢了,
        time.sleep(0.3)#此处必须休眠,不然不能复制
        win32api.keybd_event(0x11, win32api.MapVirtualKey(0x11, 0), 0, 0)
        win32api.keybd_event(0x43, win32api.MapVirtualKey(0x43, 0), 0, 0)
        time.sleep(0.2)#此处必须休眠,不然不能复制
        win32api.keybd_event(0x43, win32api.MapVirtualKey(0x43, 0), win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x11, win32api.MapVirtualKey(0x11, 0), win32con.KEYEVENTF_KEYUP, 0)



    def ctrl_a_c(self):
        # 复制ctrl+a,ctrl+c
        # 模拟按键 ctrl:0x11,a:0x41,c:0x43
        import win32api
        import win32con
        win32api.keybd_event(0x11, win32api.MapVirtualKey(0x11, 0), 0, 0)
        win32api.keybd_event(0x41, win32api.MapVirtualKey(0x41, 0), 0, 0)

        win32api.keybd_event(0x41, win32api.MapVirtualKey(0x41, 0), win32con.KEYEVENTF_KEYUP, 0)

        win32api.keybd_event(0x43, win32api.MapVirtualKey(0x43, 0), 0, 0)

        win32api.keybd_event(0x11, win32api.MapVirtualKey(0x11, 0), win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x43, win32api.MapVirtualKey(0x43, 0), win32con.KEYEVENTF_KEYUP, 0)

    def backspace(self):
        import win32api
        import win32con
        win32api.keybd_event(0x08, win32api.MapVirtualKey(0x08, 0), win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x08, win32api.MapVirtualKey(0x08, 0), 0, 0)
        win32api.keybd_event(0x08, win32api.MapVirtualKey(0x08, 0), win32con.KEYEVENTF_KEYUP, 0)

    def ctrl_v(self):
        import win32api
        import win32con
        win32api.keybd_event(0x11, win32api.MapVirtualKey(0x11, 0), win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x56, win32api.MapVirtualKey(0x56, 0), win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x11, win32api.MapVirtualKey(0x11, 0), 0, 0)
        win32api.keybd_event(0x56, win32api.MapVirtualKey(0x56, 0), 0, 0)
        win32api.keybd_event(0x11, win32api.MapVirtualKey(0x11, 0), win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x56, win32api.MapVirtualKey(0x56, 0), win32con.KEYEVENTF_KEYUP, 0)

    def getcodelight_byself(self):
        ob.ctrl_c()
        # time.sleep(0.7)#不用休眠

        #print('deleter')
        # 删除选中文本
        ob.backspace()

        #print('html')
        # 从剪切板得到代码
        code = ob.getcode()
        # rtffile=ob.totrf(code)#生成rtf
        # ob.get_rtfText_2(rtffile)
        htmlfile = ob.tohtml(code)
        ob.get_htmlText(htmlfile)

        # 粘贴新代码
        ob.ctrl_v()

    # 快捷键函数
    def eventhandler(self):
        self.runing_eventhandler = True
        if self.start_onlineget==True:
            self.getcodelight_byonline()#网络获取
        else:
            self.getcodelight_byself()
        #print(' def eventhandler(self):')



class mytimer:
    def __init__(self, ):
        self.timerstop = False
        self.miaoshu = 0
        self.shurumiaoshu = None

    def start(self):
        def fun_timer():
            self.miaoshu += 1
            # print('self.timerstop=', self.timerstop)
            # print('当前秒数:', self.miaoshu)
            if self.timerstop == True:
                return 'timeout'
            if self.miaoshu == self.shurumiaoshu:
                # wanttodo:x
                ob.runing_eventhandler = False
                return 'timeout'

            # wanttodo:
            #print('Hello Timer!')
            global timer
            timer = threading.Timer(1, fun_timer)
            timer.start()

        timer = threading.Timer(1, fun_timer)
        timer.start()

    def stop(self):
        self.timerstop = True


'''
#监听键盘事件线程,暂时不用
import threading
class MyThread(threading.Thread):
    def __init__(self,kuijianjie):
        super(MyThread, self).__init__()  # 重构run函数必须写
        self.kuijianjie = 1
        self.kuijianjie=kuijianjie

    def run(self):
        from pynput import keyboard
        def on_activate_h():
            print('<ctrl>+<alt> pressed')
            eventhandler()#调用函数,时会重复监听,所以可以添加标识符,不要重复调用eventhandler()
            return False

        def on_activate_i():
            print('<ctrl>+/ pressed')
            eventhandler()
            return False
        def esc():
            print('<esc> pressed')
            return False
        
        def esc_shift():
            print('<esc>+<shift> pressed')
            return False

        with keyboard.GlobalHotKeys({
            '<ctrl>+<alt>': on_activate_h,
            '<ctrl>+/': on_activate_i,
            '<esc>': esc,
            '<esc>+<shift>': esc_shift}) as h:
            h.join()

        
'''


if __name__ == '__main__':
    # 实例化
    ob = codelight()

    #窗口
    from tkinter import *
    root = Tk()
    def destroy():
        root.destroy()

    root.wm_attributes('-topmost', 1)#置顶
    root.title("MaofU代码高亮")
    root.geometry('200x280')
    root.protocol('WM_DELETE_WINDOW',destroy )

    #按钮
    #btn = Button(root, text='快捷键ctrl+f')
    #btn.bind_all('<Control-f>', eventhandler)
    #btn.pack()#不显示

    # 上面的快捷键不能全局
    # 采用监听
    # mythread = MyThread(1)
    # mythread.start()#不能退出
    def run():
        print('test')
        from pynput import keyboard

        def on_activate_ctrl_x():
            #不能添加函数,键盘多次监听
            if ob.runing_eventhandler==False:#调用函数时会重复监听,所以可以添加标识符,不要重复调用eventhandler()
                ob.runing_eventhandler = True
                ob.eventhandler()
                # 标识，两秒后再把标识==false
                mytim = mytimer()
                mytim.start()
                mytim.shurumiaoshu = 3
                print('x,e+<alt> pressed')
            else:
                return

        def esc():
            print('<esc> pressed')
            root.destroy()

        with keyboard.GlobalHotKeys({
            'x+<alt>': on_activate_ctrl_x,'e+<alt>': on_activate_ctrl_x,'<alt>+w': esc}) as h:
            h.join()

    import threading
    thread=threading.Thread(target=run)
    thread.setDaemon(True)#守护线程
    thread.start()

    #下拉框,获得方式,网络和本地
    from tkinter.ttk import *
    def getcodelightway(arg):
        if comb_getway.current()==0:
            ob.start_onlineget=True
        else:
            ob.start_onlineget=False

    comb_getway = Combobox(root, textvariable=StringVar(), values=['网络抓取', '本地生成'])
    comb_getway.place(relx=0, rely=0.6, relwidth=1)
    comb_getway.bind('<<ComboboxSelected>>', getcodelightway)  # 事件

    #高亮风格
    def calc(arg):#处理函数
        dic ={0: 'default', 1: 'emacs', 2: 'friendly', 3:'colorful',4:'autumn',5:'murphy',6:'manni',7:'monokai',8:'perldoc',9:'pastie',10:'borland',11:'trac',12:'native',13:'fruity',14:'bw',15:'vim',16:'vs',17:'tango',18:'rrt',19:'xcode',20:'igor',
              21:'paraiso-light',22:'paraiso-dark',23:'lovelace',24:'algol',25:'algol_nu',26:'arduino',27:'rainbow_dash',28:'abap'}
        var = dic[comb.current()]
        ob.codestyle=var
        print(ob.codestyle)

    #下拉框,代码风格
    var = StringVar()
    comb = Combobox(root, textvariable=var, values=['default', 'emacs', 'friendly', 'colorful','autumn','murphy','manni','monokai','perldoc','pastie',
'borland' ,"trac",
"native",
"fruity",
"bw",
"vim",
"vs",
"tango",
"rrt",
"xcode",
"igor",

"paraiso-light",
"paraiso-dark",
"lovelace",
"algol",
"algol_nu",
"arduino",
"rainbow_dash",
"abap"
])
    comb.place(relx=0, rely=0.7, relwidth=1)
    comb.bind('<<ComboboxSelected>>', calc)#事件


    #下拉框,浏览器
    def selectdiver(arg):
        if comb_dirver.current()==0:
            ob.dirverfilename=ob.dirverfilename_chome
        else:
            ob.dirverfilename=ob.dirverfilename_edge


    var_dirver = StringVar()
    comb_dirver = Combobox(root, textvariable=var_dirver, values=['谷歌chome浏览器','微软edge浏览器'])
    comb_dirver.place(relx=0, rely=0.8, relwidth=1)
    comb_dirver.bind('<<ComboboxSelected>>', selectdiver)  # 事件

    #下拉框,高亮文本框
    def sel_textbox(arg):
        if comb_textbox.current()==0:
            ob.text_box=True
        else:
            ob.text_box=False

    comb_textbox = Combobox(root, textvariable=StringVar(), values=['开启高亮文本框', '不开启高亮文本框'])
    comb_textbox.place(relx=0, rely=0.9, relwidth=1)
    comb_textbox.bind('<<ComboboxSelected>>',sel_textbox )  # 事件

    # 标签
    lb = Label(root,text='下拉框1:选择获取方式(默认本地)\n下拉框2:选择高亮风格\n下拉框3:选择浏览器(默认edge)\n下拉框4:代码高亮文本框(默认不开启)(文本框可以在word,csdn等中调整)\n(请保持程序根目录下的浏览器驱动与你的浏览器版本一致,更换时,驱动名字要与之前的一致)\n\n'
                    '快捷键执行:(alt+x,alt+e)(程序可最小化)\n快捷退出:alt+w\n1.程序工作时,请保持光标在需要工作的位置2.粘贴地方不同,文本格式不同',
               font=("楷体", 13))
    lb.place(relx=0, rely=0.1)
    lb.pack()

    # 设置label标签
    link =Label(root,text='更多帮助点击这里呀!!!!!!!!',font=('楷体', 13))
    link.place(relx=0, rely=0.5)
    # 此处必须注意，绑定的事件函数中必须要包含event参数
    import webbrowser
    def open_url(event):
        webbrowser.open("https://blog.csdn.net/qq_62595450?spm=1000.2115.3001.5343", new=0)
    # 绑定label单击事件
    link.bind("<Button-1>", open_url)

    root.mainloop()

    # #下拉框,快捷键,不能全局,改用键盘监听。
    # def kuaijianjie(arg):
    #     if comb_kuai.current()==0:
    #         # btn.bind_all('<Control-f>',eventhandler)
    #         mythread.kuijianjie=0
    #     if comb_kuai.current()==1:
    #         # btn.bind_all('<Alt-x>', eventhandler)
    #         mythread.kuijianjie = 1
    #     if comb_kuai.current()==2:
    #         # btn.bind_all('<Alt-b>', eventhandler)
    #         mythread.kuijianjie = 2
    # var_kuai = StringVar()
    # comb_kuai = Combobox(root, textvariable=var_kuai, values=['ctrl+f', 'alt+x','alt+b'])
    # comb_kuai.place(relx=0, rely=0.8, relwidth=1)
    # comb_kuai.bind('<<ComboboxSelected>>', kuaijianjie)  # 事件




#说明:为实现复制trf文件内容,我写了   def get_rtfText_1(self,rtffile):    def get_rtfText_2(self,rtffile):
#两个函数,利用Word软件打开rtf,并复制,可是问题在于并不能直接复制(因为光标没在word中),因此还想了去移动光标,可是还是存在许多问题
#
#精疲力尽后,突然想到可以用浏览器打开pdf,所以将rtf文件转换为pdf再打开就好了
#好吧,用浏览器打开pdf也不能直接复制,放弃了
#新发现,浏览器打开pdf复制的文本粘贴到word中,并没有保留格式,所以这条路走不通

#为什么使用rtf文件呢? 因为我发现 有时候 复制的html文件粘贴后 格式不对,因此用了 rtf文件

#注意,浏览器要与浏览器驱动版本差不多

# 其他,查看支持的风格
'''

from pygments.styles import STYLE_MAP

for key in STYLE_MAP.keys():
    print(key)
    
"""    
default
emacs
friendly
colorful
autumn
murphy
manni
monokai
perldoc

pastie
borland

trac
native
fruity
bw
vim
vs
tango
rrt
xcode
igor

paraiso-light
paraiso-dark
lovelace
algol
algol_nu
arduino
rainbow_dash
abap
"""



类 RtfFormatter
短名称
rtf

文件名
*.rtf

将标记格式化为 RTF 标记。此格式化程序会自动输出包含颜色信息和其他有用内容的完整 RTF 文档。非常适合复制和粘贴到Microsoft（R）Word（R）文档中。

请注意，和选项将被忽略。RTF 格式本身是 ASCII，但由于使用了转义序列，因此可以正确处理 unicode 字符。encodingoutencoding

0.6 版中的新功能。

接受的其他选项：

风格
要使用的样式可以是字符串或 Style 子类（默认：）。'default'

字体
使用的字体系列，例如 。默认为一些应该具有固定宽度的通用字体。Bitstream Vera Sans

字体大小
所用字体的大小。大小以半点为单位指定。默认值为 24 个半点，字体大小为 12。

2.0 版中的新功能。
'''
