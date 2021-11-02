
from app.diagram_networkx import *
from app.window import *
from app.dataimport import *
import pprint




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
        label = Label(window, text=to_show)
        label.pack()









def draw_fuzzy_trapezoid(e_id):
    event_to_display=e_id
    x1 = dict_events[event_to_display]['x1']
    x2 = dict_events[event_to_display]['x2']
    x3 = dict_events[event_to_display]['x3']
    x4 = dict_events[event_to_display]['x4']
    import numpy as np
    import matplotlib.pyplot as plt
    import skfuzzy as fuzz
    import mplcursors
    left_border=min(float(x1), float(x2), float(x3), float(x4))
    right_border=max(float(x1), float(x2), float(x3), float(x4))
    support_lenght=right_border-left_border
    border_offset=support_lenght/10
    text_start=left_border+0.3*support_lenght
    left_border = left_border - border_offset
    right_border = right_border + border_offset
    x = np.arange(left_border,right_border,0.001*border_offset)
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
    axis_y=1.8
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
    plottext="x1:"+str(x1)+"\nx2:"+str(x2)+"\nx3:"+str(x3)+"\nx4:"+str(x4)
    plt.annotate(plottext,xy=(text_start,1.2),horizontalalignment="left")
    plt.show()

def relation_calculate_tree():
    array_available_nodes = []
    for e in dict_events.keys():
        array_available_nodes.append(e)

    summary_events_relations=len(dict_events.keys())+len(dict_relations.keys())

    while len(array_available_nodes) < summary_events_relations:
        for r in dict_relations.keys():
            missing_elements = 0
            for rm in dict_relations[r]['members']:

                if rm in array_available_nodes:
                    #print("r:",r,"rm:",rm,"=> ok")
                    pass
                else:
                    #print("r:",r,"rm:",rm,"=> hiba")
                    missing_elements += 1
            #print("relation:",r,"number of missing elemenst:",missing_elements)
            #print("########################")
            if  missing_elements==0:
                if r in array_available_nodes:
                    pass
                else:
                    array_available_nodes.append(r)

    #print("availablenodes:",array_available_nodes)
    # for i in array_available_nodes:
    #     if i[0]=='r':
    #         actual_logic_gate=dict_relations[i]['logicgate']
    #         print("R:",i,"gate:",actual_logic_gate)
    # print("---BEGIN DICT EVENTS---")
    # pprint.pprint(dict_events)
    # print("---END DICT EVENTS---")
    # print("---BEGIN DICT RELATIONS---")
    # pprint.pprint(dict_relations)
    # print("---END DICT RELATIONS---")
    for a in array_available_nodes:
        if a[0]=="r":
            evaluate_relation(a)

    print("---BEGIN DICT EVENTS AFTER CALCULATED THE TREE---")
    pprint.pprint(dict_events)
    print("---END DICT EVENTS AFTER CALCULATED THE TREE---")



def evaluate_relation(relnumber):
    relation_to_evaluate=relnumber
    gate=dict_relations[relation_to_evaluate]['logicgate']
    relation_members=dict_relations[relation_to_evaluate]['members']
    #print("Running evaluation logic for a gate type of:",gate)
    ### logic gate is AND
    if gate=="and":
        #print("runnging gate login AND for relation ",relation_to_evaluate )
        x1 = 1
        x2 = 1
        x3 = 1
        x4 = 1
        #### calc x1 from members
        for m in relation_members:
            m=float(dict_events[m]['x1'])
            x1 = x1 * m
        #print("X1 calculated value:",x1)

        for m in relation_members:
            m=float(dict_events[m]['x2'])
            x2 = x2 * m
        #print("X2 calculated value:",x2)

        #### calc x3 from members
        for m in relation_members:
            m=float(dict_events[m]['x3'])
            x3 = x3 * m
        #print("X3 calculated value:",x3)

        for m in relation_members:
            m=float(dict_events[m]['x4'])
            x4 = x4 * m
        #print("X1 calculated value:",x4)

        dict_events[relation_to_evaluate]={}
        dict_events[relation_to_evaluate]['event_title'] = relation_to_evaluate
        dict_events[relation_to_evaluate]['x1'] = x1
        dict_events[relation_to_evaluate]['x2'] = x2
        dict_events[relation_to_evaluate]['x3'] = x3
        dict_events[relation_to_evaluate]['x4'] = x4

    ### logic gate is OR
    if gate == "or":
        # print("runnging gate login OR for relation ", relation_to_evaluate)
        #### calc x1 from members
        h1 = 1
        h2 = 1
        h3 = 1
        h4 = 1
        ### calc X1
        for m in relation_members:
            m = float(dict_events[m]['x1'])
            s = 1 - m
            #print("s:",s)
            h1= h1 * s
        x1= 1 - h1
        #print("X1 calculated value:", x1)

        ### calc X2
        for m in relation_members:
            m = float(dict_events[m]['x2'])
            s = 1 - m
            #print("s:",s)
            h2= h2 * s
        x2= 1 - h2
        #print("X2 calculated value:", x2)

        ### calc X3
        for m in relation_members:
            m = float(dict_events[m]['x3'])
            s = 1 - m
            #print("s:",s)
            h3= h3 * s
        x3= 1 - h3
        #print("X3 calculated value:", x3)

        ### calc X4
        for m in relation_members:
            m = float(dict_events[m]['x4'])
            s = 1 - m
            #print("s:",s)
            h4= h4 * s
        x4= 1 - h4
        #print("X4 calculated value:", x4)


        dict_events[relation_to_evaluate] = {}
        dict_events[relation_to_evaluate]['event_title'] = relation_to_evaluate
        dict_events[relation_to_evaluate]['x1'] = x1
        dict_events[relation_to_evaluate]['x2'] = x2
        dict_events[relation_to_evaluate]['x3'] = x3
        dict_events[relation_to_evaluate]['x4'] = x4


def draw_top_event():

    x1 = dict_events['r1']['x1']
    x2 = dict_events['r1']['x2']
    x3 = dict_events['r1']['x3']
    x4 = dict_events['r1']['x4']
    import numpy as np
    import matplotlib.pyplot as plt
    import skfuzzy as fuzz
    import mplcursors
    left_border = min(float(x1), float(x2), float(x3), float(x4))
    right_border = max(float(x1), float(x2), float(x3), float(x4))
    support_lenght = right_border - left_border
    border_offset = support_lenght / 10
    left_border = left_border - border_offset
    right_border = right_border + border_offset
    text_start = left_border + 0.3 * support_lenght
    x = np.arange(left_border, right_border, 0.000001*border_offset)
    mfx = fuzz.trapmf(x, [float(x1), float(x2), float(x3), float(x4)])
    plt.figure().clear()
    plt.cla()
    plt.close()
    plt.clf()
    plt.plot(x, mfx, 'k')
    plt.ylabel('Fuzzy membership')
    plt.xlabel('Universe variable (arb)')
    diag_title = "Visualization of fuzzy TOP event: " + main_node_title
    plt.title(diag_title)
    # plt.ylim(-0.1, 1.1)
    axis_x = right_border
    axis_y = 1.8
    plt.axis([left_border, axis_x, -0.5, axis_y])
    x_number_list1 = np.array([float(x2), float(x2)])
    y_number_list1 = np.array([0, 1])
    plt.plot(x_number_list1, y_number_list1, linestyle='dotted')
    x_number_list2 = np.array([float(x3), float(x3)])
    y_number_list2 = np.array([0, 1])
    plt.plot(x_number_list2, y_number_list2, linestyle='dashed')
    plt.scatter(x_number_list1, y_number_list1, s=30)
    plt.scatter(x_number_list2, y_number_list2, s=30)
    plt.scatter(float(x1), 0, s=30)
    plt.scatter(float(x4), 0, s=30)
    mplcursors.cursor(hover=True)
    plottext = "x1:" + str(x1) + "\nx2:" + str(x2) + "\nx3:" + str(x3) + "\nx4:" + str(x4)
    plt.annotate(plottext, xy=(text_start, 1.2), horizontalalignment="left")
    plt.show()




