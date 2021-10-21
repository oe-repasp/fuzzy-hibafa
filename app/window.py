from tkinter import *
from app.window_funcions import *
from app.dataimport import *
from functools import partial
root=Tk()
root.title("Fuzzy Fault Tree Analysis")
root.geometry("500x250")




my_menu=Menu(root)
submenu_draw=Menu(root)
submenu_relations=Menu(root)
root.config(menu=my_menu)



file_menu=Menu(my_menu)
my_menu.add_cascade(label="Show FTA Graph",command=plot)
# my_menu.add_cascade(label="Show relations",command=partial(show_relations,root))

my_menu.add_cascade(label="Relations operations",menu=submenu_relations)
submenu_relations.add_command(label="Print operations to main window",command=partial(show_relations,root))

my_menu.add_cascade(label="Draw grahp",menu=submenu_draw)
for mi in dict_events.keys():
    submenu_item=mi+" => "+dict_events[mi]['event_title']
    submenu_draw.add_command(label=submenu_item,command=partial(draw_fuzzy_trapezoid,mi))

my_menu.add_cascade(label="Quit",command=root.quit)
