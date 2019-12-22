from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile,asksaveasfile
import os
def newfile():
    global file
    root.title("untitled")
    file=None
    textarea.delete(1.0,END)

def savefile():
   global file
   if file==None:
    file=asksaveasfile(initialdir="Untitled.txt",defaultextension=".txt",title="Select file",filetypes=(("text files","*.txt"),("all files","*.*")))
    if file=="":
        file=None
    else:
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()
        root.title(os.path.basename(file))
   else:
       f = open(file, "w")
       f.write(textarea.get(1.0, END))
       f.close()




def openfile():
    global file

    file=askopenfile(defaultextension=".txt",filetypes=[("all files","*.*"),("text files","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file))
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()
def quitapp():
    root.destroy()

def cuttext():
    textarea.event_generate("<<Cut>>")


def copytext():
    textarea.event_generate("<<Copy>>")

def pastetext():
    textarea.event_generate("<<Paste>>")

def about():
    messagebox.showinfo("Notepad","All copyrights are reserved")
root=Tk()
root.title("Untitled-notepad")
root.geometry("720x1080")

textarea=Text(root,font="lucida 15")
textarea.pack(fill=BOTH,expand=True)
file=None

#menu bar of a notepad
mymenu=Menu(root)
filemenu=Menu(mymenu,tearoff=0)
filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="Save",command=savefile)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Exit",command=quitapp)
mymenu.add_cascade(label="File" ,menu=filemenu)

#edit menu

editmenu=Menu(mymenu,tearoff=0)
editmenu.add_command(label="cut",command=cuttext)
editmenu.add_command(label="copy",command=copytext)
editmenu.add_command(label="paste" ,command=pastetext)
mymenu.add_cascade(label="Edit" ,menu=editmenu)

#about and help

helpmenu=Menu(mymenu,tearoff=0)
helpmenu.add_command(label="About us",command=about)
mymenu.add_cascade(label="Help",menu=helpmenu)

root.config(menu=mymenu)

#addding scroll bar to text

scroll=Scrollbar(textarea)
scroll.pack(side=RIGHT ,fill=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)

root.mainloop()