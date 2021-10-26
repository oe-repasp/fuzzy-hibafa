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
### show FTA with menu button
my_menu.add_cascade(label="Show FFTA Graph",command=fuzzyfta_plot)

### show a submenu with relations operations
my_menu.add_cascade(label="Relations operations",menu=submenu_relations)
submenu_relations.add_command(label="Print operations to main window",command=partial(show_relations,root))
submenu_relations.add_command(label="Calculate relations",command=relation_calculate_values)

### show submenu to print events as trapezoid member functions
my_menu.add_cascade(label="Draw grahp",menu=submenu_draw)
for mi in dict_events.keys():
    submenu_item=mi+" => "+dict_events[mi]['event_title']
    submenu_draw.add_command(label=submenu_item,command=partial(draw_fuzzy_trapezoid,mi))

### add exit button
my_menu.add_cascade(label="Quit",command=root.quit)
