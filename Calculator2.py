import re
import tkinter as tk
from tkinter import ttk
class calculator:
    def __init__(self):
        self.win=tk.Tk()
        self.win.title("Calculator")
        self.string=tk.StringVar()
        self.string1=tk.StringVar()
        self.label()
        self.buttons()
        self.numbers=0
        self.expression=''
        self.flag=0
        self.expression1=''
        self.numflag=0
        self.rat=0
    def label(self):
        self.Frame = tk.LabelFrame(self.win)
        self.Frame.grid(column=0,row=0)
        self.Table1=tk.Entry(self.Frame,width=30,textvariable=self.string1)
        self.Table1.grid(column=0,row=0)
        self.Table=tk.Entry(self.Frame,width=30,textvariable=self.string)
        self.Table.grid(column=0,row=1)
    def Button(self,value):
        if value=="+" or value=="-" or value=="*" or value=="/":
            if self.numflag == 0:
                self.expression += self.string.get()
                self.numbers = eval(self.expression)
                self.string.set(self.numbers)
                self.expression +=str(value)
                self.string1.set(self.expression)
                self.numflag = 1
            else:
                self.temp = list(str(self.expression))
                self.temp.pop(-1)
                self.expression = "".join(self.temp)
                self.expression +=str(value)
                self.string1.set(self.expression)
            self.expression1 = '0'
            self.flag=0
        elif value=='?':
            self.string.set(str(int(self.string.get())*-1))
        elif value=='.':
            if self.flag==0 and self.expression1!='0':
                self.string.set(str(self.string.get())+'.')
                self.flag=1
            elif self.flag==0 and self.expression1=='0':
                self.expression1+='.'
                self.string.set(str(self.expression1))
                self.flag=1
        elif value=='=':
            self.temp = list(self.string1.get())
            if re.search('[0-9]', self.temp[-1]):
                self.string.set(eval(self.string1.get()))
            else:
                self.temp.pop(-1)
                self.string1.set(str(self.string1.get()) + str(eval(str("".join(self.temp)))))
                self.string.set(eval(self.string1.get()))
            self.string1.set(self.string1.get() + '=')
            self.rat = 1
        elif value=='clear':
            self.temp=list(self.string1.get())
            try:
                if self.temp[-1]=='=':
                    self.string1.set('')
                    self.expression=''
                else:
                    self.temp = list(self.string.get())
                    try:
                        self.temp.pop(-1)
                    except IndexError:
                        pass
                    self.string.set("".join(self.temp))
            except IndexError:
                self.temp=list(self.string.get())
                try:
                    self.temp.pop(-1)
                except IndexError:
                    pass
                self.string.set("".join(self.temp))
        else:
            if self.expression1 != '0':
                self.string.set(self.string.get() + value)
            else:
                self.string.set(str(value))
                self.expression1 += str(value)
            self.numflag = 0
    def buttons(self):
        self.Frame1=tk.LabelFrame(self.win)
        self.Frame1.grid(column=0,row=1,sticky=tk.W)
        a=tk.Button(self.Frame1,text='7',width=6,height=2,bg='silver',command=lambda:self.Button("7"))
        a.grid(column=0,row=0,sticky=tk.W)
        a.bind_all('<Key>', self.BuClick)
        b=tk.Button(self.Frame1,text='8',width=6,height=2,bg='silver',command=lambda:self.Button("8"))
        b.grid(column=1,row=0,sticky=tk.W)
        b.bind_all('<Key>', self.BuClick)
        c=tk.Button(self.Frame1,text='9',width=6,height=2,bg='silver',command=lambda:self.Button("9"))
        c.grid(column=2,row=0,sticky=tk.W)
        c.bind_all('<Key>', self.BuClick)
        d=tk.Button(self.Frame1,text='/',width=6,height=2,bg='silver',command=lambda:self.Button("/"))
        d.grid(column=3,row=0,sticky=tk.W)
        d.bind_all('<Key>', self.BuClick)
        e=tk.Button(self.Frame1,text='4',width=6,height=2,bg='silver',command=lambda:self.Button("4"))
        e.grid(column=0,row=1,sticky=tk.W)
        e.bind_all('<Key>', self.BuClick)
        f=tk.Button(self.Frame1,text='5',width=6,height=2,bg='silver',command=lambda:self.Button("5"))
        f.grid(column=1,row=1,sticky=tk.W)
        f.bind_all('<Key>', self.BuClick)
        g=tk.Button(self.Frame1,text='6',width=6,height=2,bg='silver',command=lambda:self.Button("6"))
        g.grid(column=2,row=1,sticky=tk.W)
        g.bind_all('<Key>', self.BuClick)
        h=tk.Button(self.Frame1,text='X',width=6,height=2,bg='silver',command=lambda:self.Button("*"))
        h.grid(column=3,row=1,sticky=tk.W)
        h.bind_all('<Key>', self.BuClick)
        i=tk.Button(self.Frame1,text='1',width=6,height=2,bg='silver',command=lambda:self.Button("1"))
        i.grid(column=0,row=2,sticky=tk.W)
        i.bind_all('<Key>', self.BuClick)
        j=tk.Button(self.Frame1,text='2',width=6,height=2,bg='silver',command=lambda:self.Button("2"))
        j.grid(column=1,row=2,sticky=tk.W)
        j.bind_all('<Key>', self.BuClick)
        k=tk.Button(self.Frame1,text='3',width=6,height=2,bg='silver',command=lambda:self.Button("3"))
        k.grid(column=2,row=2,sticky=tk.W)
        k.bind_all('<Key>', self.BuClick)
        l=tk.Button(self.Frame1,text='-',width=6,height=2,bg='silver',command=lambda:self.Button("-"))
        l.grid(column=3,row=2,sticky=tk.W)
        l.bind_all('<Key>', self.BuClick)
        m=tk.Button(self.Frame1,text='+/-',width=6,height=2,bg='silver',command=lambda:self.Button("?"))
        m.grid(column=0,row=3,sticky=tk.W)
        m.bind_all('<Key>', self.BuClick)
        n=tk.Button(self.Frame1,text='0',width=6,height=2,bg='silver',command=lambda:self.Button("0"))
        n.grid(column=1,row=3,sticky=tk.W)
        n.bind_all('<Key>', self.BuClick)
        o=tk.Button(self.Frame1,text='.',width=6,height=2,bg='silver',command=lambda:self.Button("."))
        o.grid(column=2,row=3,sticky=tk.W)
        o.bind_all('<Key>', self.BuClick)
        p=tk.Button(self.Frame1,text='+',width=6,height=2,bg='silver',command=lambda:self.Button("+"))
        p.grid(column=3,row=3,sticky=tk.W)
        p.bind_all('<Key>', self.BuClick)
        self.Frame2=tk.LabelFrame(self.win)
        self.Frame2.grid(column=0,row=2)
        q=tk.Button(self.Frame2,text="=",width=6,height=2,bg='silver',command=lambda:self.Button("="))
        q.grid(column=1,row=0)
        r=tk.Button(self.Frame2,text='Clear',width=21,height=2,bg='silver',command=lambda:self.Button("clear"))
        r.grid(column=0,row=0)
    def BuClick(self,event):
        if re.search('[0-9]',event.keysym):
            if self.rat==1:
                self.string.set('')
                self.string1.set('')
                self.expression1=''
            if self.expression1!='0':
                self.string.set(self.string.get()+str(event.keysym))
            else:
                self.string.set(str(event.keysym))
                self.expression1+=str(event.keysym)
            self.numflag=0
            self.rat=0
        if event.keysym=='slash':
            if self.numflag==0:
                self.expression+=self.string.get()
                self.numbers = eval(self.expression)
                self.string.set(self.numbers)
                self.expression += "/"
                self.string1.set(self.expression)
                self.numflag=1
            else:
                self.temp=list(str(self.expression))
                self.temp.pop(-1)
                self.expression="".join(self.temp)
                self.expression += "/"
                self.string1.set(self.expression)
            self.expression1='0'
        elif event.keysym=='asterisk':
            if self.numflag==0:
                self.expression += self.string.get()
                self.numbers = eval(self.expression)
                self.string.set(self.numbers)
                self.expression += "*"
                self.string1.set(self.expression)
                self.numflag=1
            else:
                self.temp = list(str(self.expression))
                self.temp.pop(-1)
                self.expression = "".join(self.temp)
                self.expression += "*"
                self.string1.set(self.expression)
            self.expression1 = '0'
        elif event.keysym=='minus':
            if self.numflag==0:
                self.expression += self.string.get()
                self.numbers = eval(self.expression)
                self.string.set(self.numbers)
                self.expression += "-"
                self.string1.set(self.expression)
                self.numflag=1
            else:
                self.temp = list(str(self.expression))
                self.temp.pop(-1)
                self.expression = "".join(self.temp)
                self.expression += "-"
                self.string1.set(self.expression)
            self.expression1 = '0'
        elif event.keysym=='plus':
            if self.numflag==0:
                self.expression += self.string.get()
                self.numbers = eval(self.expression)
                self.string.set(self.numbers)
                self.expression += "+"
                self.string1.set(self.expression)
                self.numflag=1
            else:
                self.temp = list(str(self.expression))
                self.temp.pop(-1)
                self.expression = "".join(self.temp)
                self.expression += "+"
                self.string1.set(self.expression)
            self.expression1 = '0'
        if event.keysym=='period':
            if self.flag==0 and self.expression1!='0':
                self.string.set(str(self.string.get())+'.')
                self.flag=1
            elif self.flag==0 and self.expression1=='0':
                self.expression1+='.'
                self.string.set(str(self.expression1))
                self.flag=1
        elif event.keysym!='period' and not re.search('[0-9]',event.keysym):
            self.flag=0
        if event.keysym=='Return':
            self.temp=list(self.string1.get())
            if re.search('[0-9]',self.temp[-1]):
               self.string.set(eval(self.string1.get()))
            else:
                self.temp.pop(-1)
                self.string1.set(str(self.string1.get())+str(eval(str("".join(self.temp)))))
                self.string.set(eval(self.string1.get()))
            self.string1.set(self.string1.get() + '=')
            self.rat=1
        if event.keysym=='BackSpace':
            self.temp=list(self.string1.get())
            try:
                if self.temp[-1]=='=':
                    self.string1.set('')
                    self.expression=''
                else:
                    self.temp = list(self.string.get())
                    try:
                        self.temp.pop(-1)
                    except IndexError:
                        pass
                    self.string.set("".join(self.temp))
            except IndexError:
                self.temp=list(self.string.get())
                try:
                    self.temp.pop(-1)
                except IndexError:
                    pass
                self.string.set("".join(self.temp))

if __name__=="__main__":
    a=calculator()
    a.win.mainloop()
'''slash
asterisk
minus
plus
Return
period'''