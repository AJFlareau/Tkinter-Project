from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk

def openfileR():
    clearlist2()
    f = open("Readme.txt", "r")
    for line in f:
        name = line[0:-1]
        lisbox1.insert(END, name)
    f.close()
    findsize()
   
def openfileW():
    f = open("Readme.txt", 'w')
    names = listbox1.get(0, END)
    for i in names:
        f.write(i+"\n")


def buttonpress():
    entrytext = entry1.get()
    print entrytext
    tkMessageBox.showinfo("Error", "Add new contact")   


root = Tk() #gives us a blank canvas object to work with
root.title("The Book of Random Contacts")

button1 = Button(root, text="Enter", bg="white", command=buttonpress)
button1.grid(row=5, column=1)

entry1 = Entry(root)
entry1.grid(row=6, column=1)


label1 = Label(root, text="Contacts", bg="grey", anchor=W)
label1.grid(row=1, column=0, sticky=W)

image = Image.open("Logo.png")
image = image.resize((1560,246))
photo = ImageTk.PhotoImage(image)

scrollbar = Scrollbar(root, orient=VERTICAL)
listbox1 = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox1.yview)
scrollbar.grid(row=9, column=0, rowspan=10)
listbox1.grid(row=8, column=0, columnspan=7, sticky=SW, rowspan=4)


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Save", command=openfileW)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)


logo = Label(root, image=photo)
logo.image = photo
logo.grid(row=0, column=0) 

mainloop() #causes the windows to display on the screen until program closes