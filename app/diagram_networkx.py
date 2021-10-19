import networkx as nx
import matplotlib.pyplot as plt





### init new graph
G = nx.DiGraph()
labeldict={}
## adding main event
G.add_node("main",color="lightgreen",pos=(0,0))

labeldict["main"]="main"
#G.add_edge("r1","main")

#### get event points
from app.dataimport import dict_events

array_nodes=[]
for k in dict_events.keys():
    event_id=dict_events[k]['event_title']
    G.add_node(k)
    labeldict[k]=k

#### get event points
from app.dataimport import dict_relations

for r in dict_relations.keys():
    relation_id=dict_relations[r]['relation_id']
    if dict_relations[r]['logicgate']=="or":
        G.add_node(r,color="red")
        labeldict[r]=r
    if dict_relations[r]['logicgate']=="and":
        G.add_node(r,color="yellow")
        labeldict[r]=r



for rel in dict_relations.keys():
    for member in dict_relations[rel]['members']:
        G.add_edge(member,rel)

### add edge from R1 to main
G.add_edge("r1","main")




colored_dict = nx.get_node_attributes(G, 'color')

default_color = 'lightblue'
color_seq = [colored_dict.get(node, default_color) for node in G.nodes()]
pos=nx.planar_layout(G,scale=5)
nx.draw(G,pos, labels=labeldict, with_labels = True,node_color=color_seq,font_size=10,node_size=300)

# nx.draw(G,pos, labels=labeldict, with_labels = True,font_size=10,node_size=300)
plt.title('Fuzzy Fault Tree')


#
# print("labeldict:",labeldict)
# print("G nodes:",G.nodes)



