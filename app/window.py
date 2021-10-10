from tkinter import *
from app.window_funcions import *

root=Tk()
root.title("Fuzzy Fault Tree Analysis")
root.geometry("500x500")



my_menu=Menu(root)
root.config(menu=my_menu)



file_menu=Menu(my_menu)
my_menu.add_cascade(label="Show FTA Graph",command=plot)
#my_menu.add_cascade(label="Display graph",command=display_tfa_graph)
my_menu.add_cascade(label="Quit",command=root.quit)
#file_menu.add_command(label="New..",command=command_new)
#file_menu.add_command(label="Quit program",command=root.quit)
