
from app.diagram_networkx import *
from app.window import *
from app.dataimport import *


def plot():
    plt.show()
    plt.close()

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




def draw_fuzzy_trapezoid(e_id):
    event_to_display=e_id
    x1=dict_events[event_to_display]['x1']
    x2 = dict_events[event_to_display]['x2']
    x3 = dict_events[event_to_display]['x3']
    x4 = dict_events[event_to_display]['x4']
    import numpy as np
    import matplotlib.pyplot as plt
    import skfuzzy as fuzz
    left_border=min(float(x1), float(x2), float(x3), float(x4))-3
    right_border=max(float(x1), float(x2), float(x3), float(x4))+3
    x = np.arange(left_border,right_border,0.01)
    mfx = fuzz.trapmf(x, [float(x1), float(x2), float(x3), float(x4)])
    plt.figure().clear()
    plt.close()
    plt.cla()
    plt.clf()
    plt.plot(x, mfx, 'k')
    plt.ylabel('Fuzzy membership')
    plt.xlabel('Universe variable (arb)')
    plt.ylim(-0.1, 1.1)
    plt.show()

