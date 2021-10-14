import app.db
from app.diagram_networkx import *
from app.window import *

def plot():
    plt.show()

def get_event_by_id(event_id):
    cursor = app.db.conn.cursor(dictionary=True)
    query_event_descriptions = "select id as ev_id,description as ev_desc,value as ev_val from events"
    cursor.execute(query_event_descriptions)
    rows_events = cursor.fetchall()
    dict_events = {}
    for ev in rows_events:
        f_event_id=ev["ev_id"]
        f_event_desc=ev["ev_desc"]
        f_event_value=ev["ev_val"]
        dict_events[f_event_id]=[f_event_desc,f_event_value]
    return dict_events[event_id]
    # print("dict_events")
    # print(dict_events)

def command_new():
    pass

def display_tfa_graph():
    pass


def display_elements():
    pass

def show_relations():
    toprint_event_desc,toprint_event_value=get_event_by_id(2)
    print("desc=",toprint_event_desc," value=",toprint_event_value)
    #
    #
    #
    # print("array_relations")
    # print(array_relations)
    # for i in array_relations:
    #     relation_id=i[0]
    #     member_list=i[1].split(",")
    #     logic_gate=i[2]
    #
    # rel_text_in_main_win=Label(master=app.window.root,text="123",font=("Courier New",10))
    # rel_text_in_main_win.pack()
    #
