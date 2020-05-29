#Simple Calculator
#hsmakkar
#use Line 183 only once,Could Create Error
#Idea from https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/
#Added Functionality
#Design Based on Android Vanilla Skin

import tkinter
from tkinter import *
import math

class calc:
    
    def repl(self):
        self.expresssion=self.e.get()
        self.newtext=self.expresssion.replace('x','*')
        
    def equals(self):
        self.repl()
        try:
            self.value=eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0,'ERROR')
        else:
            self.e.delete(0,END)
            self.e.insert(0,self.value)
            
    def sqr(self):
        self.repl()
        try:
            self.value=eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0,'ERROR')
            
        else:
            self.val=math.pow(self.value, 2)
            self.e.delete(0,END)
            self.e.insert(0,self.val)
            
            
    def tn(self):
        self.repl()
        try:
            self.value=eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0, 'ERROR')
        else:
            self.val=math.tan(self.value)
            self.e.delete(0,END)
            self.e.insert(0,self.val)
    
    def cs(self):
        self.repl()
        try:
            self.value=eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0, 'ERROR')
        else:
            self.val=math.cos(self.value)
            self.e.delete(0,END)
            self.e.insert(0,self.val)
            
    def sn(self):
        self.repl()
        try:
            self.value=eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0, 'ERROR')
        else:
            self.val=math.sin(self.value)
            self.e.delete(0,END)
            self.e.insert(0,self.val)
            
    def sqrt(self):
        self.repl()
        try:
            self.value=eval(self.newtext)
        except SyntaxError or NameError:
            sefl.e.delete(0,END)
            self.e.insert(0,'ERROR')
        else:
            self.val=math.pow(self.value, 0.5)
            self.e.delete(0,END)
            self.e.insert(0,self.val)
            
    def lg(self):
        self.repl()
        try:
            self.value=eval(self.newtext)
        except SyntaxError or NameError:
            sefl.e.delete(0,END)
            self.e.insert(0,'ERROR')
        else:
            self.val=math.log10(self.value)
            self.e.delete(0,END)
            self.e.insert(0,self.val)
            
    
    def clearall(self):
        self.e.delete(0,END)
        
        
    def  clear1(self):
        self.txt=self.e.get()[:-1]
        self.e.delete(0,END)
        self.e.insert(0,self.txt)
    
    def close(self):
        self.destroy()
        
    def action(self,arg):
        self.e.insert(END,arg)
        
    def __init__(self,master):
        master.title('Calculator')
        master.geometry()
        self.e=Entry(master)
        self.e.grid(row=0,column=0,columnspan=10,ipady=25)
        
        Button(master,text='7',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action(7)).grid(row=1,column=0)
        Button(master,text='8',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action(8)).grid(row=1,column=1)
        Button(master,text='9',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action(9)).grid(row=1,column=2)
        Button(master,text='4',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action(4)).grid(row=2,column=0)
        Button(master,text='5',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action(5)).grid(row=2,column=1)
        Button(master,text='6',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action(6)).grid(row=2,column=2)
        Button(master,text='1',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action(1)).grid(row=3,column=0)
        Button(master,text='2',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action(2)).grid(row=3,column=1)
        Button(master,text='3',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action(3)).grid(row=3,column=2)
        Button(master,text='.',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action('.')).grid(row=4,column=0)
        Button(master,text='0',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action(0)).grid(row=4,column=1)
        Button(master,text='DEL',fg='black',bg='white',width=5,
               height=3,command=lambda:self.clear1()).grid(row=4,column=2)
        Button(master,text='+',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action('+')).grid(row=1,column=3)
        Button(master,text='-',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action('-')).grid(row=2,column=3)
        Button(master,text='x',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action('x')).grid(row=3,column=3)
        Button(master,text='/',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action('/')).grid(row=4,column=3)
        Button(master,text='(',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action('(')).grid(row=1,column=4)
        Button(master,text=')',fg='black',bg='white',width=5,
               height=3,command=lambda:self.action(')')).grid(row=2,column=4)
        Button(master,text='Sqr',fg='black',bg='white',width=5,
               height=3,command=lambda:self.sqr()).grid(row=3,column=4)
        Button(master,text='Sqrt',fg='black',bg='white',width=5,
               height=3,command=lambda:self.sqrt()).grid(row=4,column=4)
        Button(master,text='Tan',fg='black',bg='white',width=5,
               height=3,command=lambda:self.tn()).grid(row=1,column=5)
        Button(master,text='Sin',fg='black',bg='white',width=5,
               height=3,command=lambda:self.sn()).grid(row=2,column=5)
        Button(master,text='Cos',fg='black',bg='white',width=5,
               height=3,command=lambda:self.cs()).grid(row=3,column=5)
        Button(master,text='Log10',fg='black',bg='white',width=5,
               height=3,command=lambda:self.lg()).grid(row=4,column=5)
        Button(master,text='=',fg='white',bg='orange',width=5,
               height=3,command=lambda:self.equals()).grid(row=1,column=6)
        Button(master,text='AC',fg='black',bg='white',width=5,
               height=3,command=lambda:self.clearall()).grid(row=2,column=6)





        
root=Tk()
Button(root,text='EXIT',fg='white',bg='black',width=5,
       height=3,command=lambda:root.destroy()).grid(row=3,column=6)
obj=calc(root)
root.mainloop()

    