import networkx as nx
import matplotlib.pyplot as plt
from app.db import conn




### init new graph
G = nx.DiGraph()
labeldict={}
## adding main event
G.add_node("main",color="green")
labeldict["main"]="main"

#### get event points
pointquery=conn.cursor(dictionary=True)
query_nodes_elements="select id as id,event_id as event_id from elements"
pointquery.execute(query_nodes_elements)

array_points_events=pointquery.fetchall()

array_points=[]


for i in array_points_events:
    element_id="e"+str(i["id"])
    event_id=i["event_id"]
    array_points.append([element_id,event_id])
    G.add_node(element_id)
    labeldict[element_id]= element_id


### get relations points

relationquery=conn.cursor(dictionary=True)
query_relations_elements="select id as relation_id,members as relation_members,logicgate as relation_logic from relations"
relationquery.execute(query_relations_elements)
array_points_relations=relationquery.fetchall()
# print("array_point_relations")
# print(array_points_relations)
array_relations=[]
for i in array_points_relations:
    relation_id="r"+str(i["relation_id"])
    relation_members=i["relation_members"]
    relation_logic=i["relation_logic"]
    array_relations.append([relation_id,relation_members,relation_logic])
    if i["relation_logic"]=="or":
        G.add_node(relation_id,color="red")
        labeldict[relation_id] = relation_id+"V"
    if i["relation_logic"]=="and":
        G.add_node(relation_id, color="yellow")
        labeldict[relation_id] = relation_id+"&"



colored_dict = nx.get_node_attributes(G, 'color')

default_color = 'lightblue'
color_seq = [colored_dict.get(node, default_color) for node in G.nodes()]
#
print("array_relations")
print(array_relations)
print("---")
for i in array_relations:
    relation_id=i[0]
    members=i[1]
    logic_gate=i[2]
    member_list=members.split(",")
    for m in member_list:
        #print(m,relation_id)
        G.add_edge(m,relation_id,lenght="100")

### ez random csinalja a graph-ot, ne hasznald:
#pos=nx.spring_layout(G,scale=100,weight="100")

### ez jol rendezi el a graph-ot az ablakban
pos=nx.planar_layout(G,scale=5)
# print("G-nodes:")
# print(list(G.nodes))
# print("G:edges")
# print(list(G.edges))
#print(labeldict)
nx.draw(G,pos, labels=labeldict, with_labels = True,node_color=color_seq,font_size=10,node_size=300)
# nx.draw(G,pos, labels=labeldict, with_labels = True,font_size=10,node_size=300)
plt.title('Fuzzy Fault Tree')
