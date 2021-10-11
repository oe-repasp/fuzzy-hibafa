import networkx as nx
import matplotlib.pyplot as plt
from app.db import conn




### init new graph
G = nx.DiGraph()
labeldict={}
G.add_node("main",color="green")
labeldict["main"]="main"

#### get event points
pointquery=conn.cursor()
query_nodes_elements="select id,event_id from elements"
pointquery.execute(query_nodes_elements)

array_points_events=pointquery.fetchall()

array_points=[]


for i in array_points_events:
    element_id="e"+str(i[0])
    event_id=i[1]
    array_points.append([element_id,event_id])
    G.add_node(element_id)
    labeldict[element_id]= element_id


### get relations points

relationquery=conn.cursor()
query_relations_elements="select * from relations"
relationquery.execute(query_relations_elements)
array_points_relations=relationquery.fetchall()

array_relations=[]
for i in array_points_relations:
    relation_id="r"+str(i[0])
    relation_members=i[1]
    relation_logic=i[2]
    array_relations.append([relation_id,relation_members,relation_logic])
    if i[2]=="or":
        G.add_node(relation_id,color="red")
        labeldict[relation_id] = relation_id+"V"
    if i[2]=="and":
        G.add_node(relation_id, color="yellow")
        labeldict[relation_id] = relation_id+"&"



colored_dict = nx.get_node_attributes(G, 'color')

default_color = 'lightblue'
color_seq = [colored_dict.get(node, default_color) for node in G.nodes()]



print(array_relations)
for i in array_relations:
    relation_id=i[0]
    members=i[1]
    logic_gate=i[2]
    member_list=members.split(",")
    for m in member_list:
        G.add_edge(m,relation_id,lenght="100")

#pos=nx.spring_layout(G,scale=100,weight="100")
pos=nx.planar_layout(G,scale=3)
#print(list(G.nodes))
print(list(G.edges))
#print(labeldict)
nx.draw(G,pos, labels=labeldict, with_labels = True,node_color=color_seq,font_size=10,node_size=300)
