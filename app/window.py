from tkinter import *
from app.window_funcions import *

root=Tk()
root.title("Fuzzy Fault Tree Analysis")
root.geometry("500x250")




my_menu=Menu(root)
root.config(menu=my_menu)



file_menu=Menu(my_menu)
my_menu.add_cascade(label="Show FTA Graph",command=plot)
my_menu.add_cascade(label="Show relations",command=show_relations)
my_menu.add_cascade(label="Quit",command=root.quit)
