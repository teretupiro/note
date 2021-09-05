from tkinter import*
from tkinter import filedialog as fd

def new_window():
    window=Toplevel(root)
    window.title('Настройки')
    window.geometry('500x500')
    Entx=Entry(window)
    Enty=Entry(window)
    Entx.place(x=0,y=0)
    Enty.place(x=0,y=20)

    def change():
       x=Entx.get()
       y=Enty.get()
       root.geometry(x + 'x' + y)
    Button(window,text='CHANGE',command=change).pack()





def inserttext():
    filename=fd.askopenfilename()
    f=open(filename)
    s=f.read()
    t.insert(1.0,s)
    f.close()


def extracttext():
    filename=fd.asksaveasfile(
    filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")))
    try:
     f=open(filename,'w')
     s=t.get(1.0,END)
     f.write(s)
     f.close
    except:
        print('file not save')

root=Tk()
root.title('Note')


mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть",command=inserttext)
filemenu.add_command(label="Сохранить...",command=extracttext)
filemenu.add_command(label='Настройки',command=new_window)
filemenu.add_command(label="Выход")
mainmenu.add_cascade(label='File',menu=filemenu)

t=Text()
t.pack()


root.mainloop()
