
from app.diagram_networkx import *
from app.window import *
from app.dataimport import *


def fuzzyfta_plot():
    plt.show()
    plt.close()

def show_relations(window):
    for r in dict_relations.keys():
        relation_name=r
        rel_elements=dict_relations[r]['members']
        rel_logic=dict_relations[r]['logicgate']
        to_print=[]
        print(r)
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
        for p in to_print:
            to_show=to_show + p + " "
        to_show=to_show+(" ")
        # print(to_show)
        label=Label(window,text=to_show)
        label.pack()







def draw_fuzzy_trapezoid(e_id):
    event_to_display=e_id
    x1=dict_events[event_to_display]['x1']
    x2 = dict_events[event_to_display]['x2']
    x3 = dict_events[event_to_display]['x3']
    x4 = dict_events[event_to_display]['x4']
    import numpy as np
    import matplotlib.pyplot as plt
    import skfuzzy as fuzz
    import mplcursors
    left_border=min(float(x1), float(x2), float(x3), float(x4))-3
    right_border=max(float(x1), float(x2), float(x3), float(x4))+3
    x = np.arange(left_border,right_border,0.01)
    mfx = fuzz.trapmf(x, [float(x1), float(x2), float(x3), float(x4)])
    plt.figure().clear()
    plt.cla()
    plt.close()
    plt.clf()
    plt.plot(x, mfx, 'k')
    plt.ylabel('Fuzzy membership')
    plt.xlabel('Universe variable (arb)')
    diag_title="Visualization of fuzzy event: "+e_id+" "+dict_events[e_id]['event_title']
    plt.title(diag_title)
    # plt.ylim(-0.1, 1.1)
    axis_x=right_border
    axis_y=1.5
    plt.axis([left_border, axis_x, -0.5, axis_y])
    x_number_list1 = np.array([float(x2),float(x2)])
    y_number_list1 = np.array([0,1])
    plt.plot(x_number_list1,y_number_list1,linestyle='dotted')
    x_number_list2 = np.array([float(x3), float(x3)])
    y_number_list2 = np.array([0, 1])
    plt.plot(x_number_list2, y_number_list2, linestyle='dashed')
    plt.scatter(x_number_list1,y_number_list1,s=30)
    plt.scatter(x_number_list2, y_number_list2, s=30)
    plt.scatter(float(x1),0,s=30)
    plt.scatter(float(x4),0,s=30)
    mplcursors.cursor(hover=True)
    plt.show()

def relation_calculate_values():
    dict_calc={}
    for e in dict_events.keys():
        list_e_values=[]
        list_e_values.append(dict_events[e]['x1'])
        list_e_values.append(dict_events[e]['x2'])
        list_e_values.append(dict_events[e]['x3'])
        list_e_values.append(dict_events[e]['x4'])
        dict_calc[e]=list_e_values
    for i in dict_relations.keys():
        # print(dict_relations[i]['members'])
        for m in dict_relations[i]['members']:
            # print("member",m)
            if m[0]=="r":
                if m in dict_calc.keys():
                    print("ok:",m)
                else:
                    print("nemok",m)


    print("---")
    print("full dict_calc:")
    print(dict_calc)
