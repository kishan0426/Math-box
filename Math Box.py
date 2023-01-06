def square():
    try:
        sq = int(entry.get())
    except:
        ValueError
    for s in range(1,sq + 1):
        sqres = s ** s
        listbox.insert(END, (s,'**',s,"=",sqres))
    entry.delete(0,END)
    entry.focus()


def cube():
    try:
        cb = int(entry.get())
    except:
        ValueError
    for c in range(1, cb + 1):
        cbres = c * c * c
        listbox.insert(END, (c,'*',c,'*',c,"=",cbres))
    entry.delete(0,END)
    entry.focus()

def multiply():
    try:
        mul = int(entry.get())
    except:
        ValueError
    for m in range(1, mul + 1):
        multiply = m * mul
        listbox.insert(END, (m,'*',mul,"=",multiply))
    entry.delete(0, END)
    entry.focus()

def factor():
    try:
        fact = int(entry.get())
    except:
        ValueError
    for f in range(1, fact + 1):
        res = fact % f
        if res == 0:
            listbox.insert(END, (f))
    entry.delete(0, END)
    entry.focus()


def prime():
    try:
        prm = int(entry.get())
    except:
        ValueError
    l = []
    for p in range(2, prm + 1):
        if prm % p == 0:
            l.append(p)
    if len(l) <= 1:
        listbox.insert(END, (p,"is prime"))
    else:
        listbox.insert(END, (p," is not prime"))
    entry.delete(0, END)
    entry.focus()




def clearbox():
    entry.delete(0,END)
    listbox.delete(0,END)
    entry.focus()


from tkinter import *

window = Tk()

window.geometry("480x240")
window.title("MATHS-IS-FUN")
# window.wm_iconbitmap("stripes.ico")
window.configure(background = "blue")
window.iconbitmap("")


label1 = Label(window,text="MATH BOX ",font=('Courier', 40, 'bold'),wrap=400)
# label1.place(x = 20, y = 30,width = 20,height=25)
label1.grid(row = 0,column=0,columnspan=4,padx=(600,500))
# label1.pack(padx=10,pady=10)

label2 = Label(window,text = "Enter the number :-",font=('Courier',20,'bold'),wrap=400)
label2.grid(row = 1,column = 0,columnspan = 3,padx = (100,200))
# label2.pack()
label3 = Label(window,text = "Result :-",font=('Courier',20,'bold'),wrap=400)
label3.grid(row = 2,column = 0,columnspan = 3,padx = (100,200))

entry = Entry(text = 0, width=10,font=('Courier',20))
entry.grid(row = 1,column = 2,columnspan = 3,padx = (200,200))
entry.focus()

# entry1 = Entry(text = 0, width= 5, font=('Courier',20))
# entry1.grid(row = 1, column = 4,columnspan = 3, padx = (200,200))
# entry1.focus()

listbox = Listbox(font=('Courier',20))
listbox.grid(row = 2,column = 2,columnspan = 3,padx = (200,200))
scroll = Scrollbar(window, orient = "vertical")
listbox.config(yscrollcommand=scroll.set)
scroll.config(command = listbox.yview)


button1 = Button(text="Find square", command=square,font=('Courier',20,'bold'),wrap=400)
button1.grid(row = 3,column=0,columnspan=3,padx=(10,10))
button2 = Button(text="Find cube", command = cube,font=('Courier',20,'bold'),wrap=400)
button2.grid(row = 4, column = 0,columnspan = 3,padx=(10,10))
button3 = Button(text="Find multiplication", command=multiply,font=('Courier',20,'bold'),wrap=400)
button3.grid(row = 3, column = 1,columnspan = 3,padx=(20,20))
button4 = Button(text="Find factors", command=factor,font=('Courier',20,'bold'),wrap=400)
button4.grid(row = 4, column = 1,columnspan = 3,padx=(20,20))
button5 = Button(text="Find Prime Numbers", command=prime,font=('Courier',20,'bold'),wrap=400)
button5.grid(row = 3, column = 3,columnspan = 3,padx=(30,30))
button6 = Button(text="Wipe", command=clearbox,font=('Courier',20,'bold'),wrap=400)
button6.grid(row = 4, column = 2,columnspan = 3,padx=(30,30))


window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=2)
window.rowconfigure(2,weight=3)
window.rowconfigure(3,weight=4)
window.rowconfigure(4,weight=5)
window.mainloop()


