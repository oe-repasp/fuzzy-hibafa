
from app.diagram_networkx import *
from app.window import *
from app.dataimport import *


def plot():
    plt.show()

def show_relations():
    for r in dict_relations.keys():
        relation_name=r
        rel_elements=dict_relations[r]['members']
        rel_logic=dict_relations[r]['logicgate']
        to_print=[]
        for i in rel_elements:
            if i[0]=="e":
                to_print.append(dict_events[i]['event_title'])
                to_print.append(rel_logic)
            if i[0]=="r":
                to_print.append("Relation")
                to_print.append(i)
                to_print.append(rel_logic)
        to_print.pop()
        to_show="relation "+relation_name+" is: "
        print(to_show)
        for p in to_print:
            print(p+" ",end="")
        print(" ")




