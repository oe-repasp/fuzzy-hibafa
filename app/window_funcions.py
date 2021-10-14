import app.db
from app.diagram_networkx import *
from app.window import *
from mariadb import *

def plot():
    plt.show()



def get_event_desc_by_id(event_id):
    cursor = app.db.conn.cursor(dictionary=True)
    cursor.execute("""select description from events where id= (%s) """ % (event_id))
    row_desc = cursor.fetchall()
    return row_desc[0]

def get_event_value_by_id(event_id):
    cursor = app.db.conn.cursor(dictionary=True)
    cursor.execute("""select value from events where id= (%s) """ % (event_id))
    row_val = cursor.fetchall()
    return row_val[0]


def get_relation_members_by_id(r_id):
    cursor=app.db.conn.cursor(dictionary=True)
    cursor.execute("""select members from relations where id= (%s) """ % (r_id))
    row_members=cursor.fetchall()
    return row_members[0]

def get_relation_gate_by_id(r_id):
    cursor=app.db.conn.cursor(dictionary=True)
    cursor.execute("""select logicgate from relations where id= (%s) """ % (r_id))
    row_gate=cursor.fetchall()
    return row_gate[0]

def show_relations():
    # toprint_event_desc,toprint_event_value=get_event_by_id(2)
    array_relation_ids=[]
    for i in array_relations:
        rel_id=i[0][1:]
        array_relation_ids.append(rel_id)
    #print(array_relation_ids)
    for i in array_relation_ids:
        array_relation_members=get_relation_members_by_id(i)
        toprint_rel_id=i
        toprint_rel_gate=get_relation_gate_by_id(i)["logicgate"]
        list_rel_members=get_relation_members_by_id(i)["members"]
        toprint=[]
        toprint.append("relation")
        toprint.append(i)
        toprint.append(":")

        #print("rel_id:",toprint_rel_id,"gate:",toprint_rel_gate,"members:",list_rel_members)
        for m in list_rel_members.split(","):
            #print("m=",m)
            if m[0]=="e":
                eventid_to_get=int(m[1:])
                # print("get:",eventid_to_get)
                dict_event=get_event_desc_by_id(eventid_to_get)
                toprint.append(dict_event["description"])
                toprint.append(str.upper(toprint_rel_gate))
            if m[0]=="r":
                toprint.append("relation")
                toprint.append(m[1])
                toprint.append(str.upper(toprint_rel_gate))


        del toprint[-1]
        print(toprint)


