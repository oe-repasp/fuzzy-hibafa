import networkx as nx
import matplotlib.pyplot as plt
from db import conn
import mariadb



### init new graph
G = nx.Graph()

pointquery=conn.cursor()
query_nodes_elements="select id,event_id from elements"
pointquery.execute(query_nodes_elements)

array_points_events=pointquery.fetchall()

array_points=[]

for i in array_points_events:
    element_id=i[0]
    event_id=i[1]
    array_points.append([element_id,event_id])


print(array_points)



