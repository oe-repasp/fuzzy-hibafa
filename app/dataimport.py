import configparser
from pathlib import Path

graphdata=configparser.ConfigParser()
graphdata.read('app\data.ini')


sections=graphdata.sections()


#
# for s in sections:
#     for k in graphdata[s]:
#         print(graphdata[s][k])
#
dict_events_raw={}

for e in graphdata['events']:
    dict_events_raw[e]=(graphdata['events'][e])

dict_events={}
for k in dict_events_raw.keys():
    lista=str.split(dict_events_raw[k],",")
    temp_event_title=lista[0]
    temp_event_title=temp_event_title[2:]
    temp_event_title = temp_event_title[:-1]
    temp_4th=lista[4]
    temp_4th=temp_4th[:-1]
    lista[0]=temp_event_title
    lista[4]=temp_4th
    dict_events[k]={"event_title":temp_event_title}
    dict_events[k]['x1']=lista[1]
    dict_events[k]['x2']=lista[2]
    dict_events[k]['x3']=lista[3]
    dict_events[k]['x4']=lista[4]



### create a temp dictionary for relations data
dict_relations_raw={}
### create a dictionary for the final relations data
dict_relations={}

### get all relations id from ini file's relations section
for r in graphdata['relations']:
    dict_relations_raw[r]=(graphdata['relations'][r])

### get relations from section relations
for k in dict_relations_raw.keys():
    list_temp_events=str.split(dict_relations_raw[k],",")
    list_event_members=[]
    for l in list_temp_events:
        list_event_members.append(l)
    list_event_members[0]=list_event_members[0][1:]
    list_event_members[-1]=list_event_members[-1][:-1]

    logicgate=list_event_members.pop()
    dict_relations[k]={"relation_id":k}
    dict_relations[k]['members']=list_event_members
    dict_relations[k]['logicgate']=logicgate




#print(dict_relations_raw)