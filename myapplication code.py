from tkinter import *
from tkinter import ttk
    
window = Tk()
window.title('Homework of Programming')
window.geometry('1400x700')
window.config(bg="#09112e")

label = ttk.Label(master = window, text = 'Home work of Programming',font=('Arial',20,'bold'),foreground='green')
label.pack()
frame = ttk.Frame(window,width=130,height=50)
frame.pack(padx=10,pady=10)
text =Text(frame,highlightthickness=0,width=130,height=50)
text.grid(row=0,column=0,sticky='nsew')
text_scrollbar = ttk.Scrollbar(frame,command=text.yview)
text_scrollbar.grid(row=0,column=1,sticky="ns")
text.configure(yscrollcommand=text_scrollbar.set)
#button = ttk.Button(master =  window,text = "fibnocci")
#button.pack()
def builtin ():
    text.delete('1.0','end')
    with open("C:\\Users\\Abuzar\\Desktop\\builtin.txt",'r') as f:
        data = f.read()
    text.insert(INSERT,data)

def fib ():
    text.delete('1.0','end')
    with open("C:\\Users\\Abuzar\\Desktop\\fibnocci.txt",'r') as f:
        data = f.read()
    text.insert(INSERT,data)

def fac ():
    text.delete('1.0','end')
    with open("C:\\Users\\Abuzar\\Desktop\\factorial.txt",'r') as f:
        data = f.read()
    text.insert(INSERT,data)

def class1 ():
    text.delete('1.0','end')
    with open("C:\\Users\\Abuzar\\Desktop\\class.txt",'r') as f:
        data = f.read()
    text.insert(INSERT,data)

   
btn = Button(window,text='builtin function',font=('Bold',15),fg="white",bd=0,bg="black",
                                        command= builtin)
btn.place(x=10,y=50) 
btn1 = Button(window,text='fibnocci',font=('Bold',15),fg="white",bd=0,bg="black",
                                        command= fib)                                      
btn1.place(x=10,y=100,)
btn2 = Button(window,text='factorial',font=('Bold',15),fg="white",bd=0,bg="black",
                                command= fac)
                              
btn2.place(x=10,y=150)

btn3 = Button(window,text='class',font=('Bold',15),fg="white",bd=0,bg="black",
                                        command= class1)
btn3.place(x=10,y=200) 

menu = Menu(window)
file_menu = Menu(menu,tearoff=False)
file_menu.add_command(label='built in function',command=builtin)
file_menu.add_separator()
file_menu.add_command(label='fibnocci sequence',command=fib)
file_menu.add_separator()
file_menu.add_command(label='factorial',command=fac)
file_menu.add_separator()
file_menu.add_command(label='class',command=class1)

menu.add_cascade(label='Menu',menu=file_menu)
window.configure(menu=menu)

window.mainloop()

