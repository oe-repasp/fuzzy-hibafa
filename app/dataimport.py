import configparser
from pathlib import Path

graphdata=configparser.ConfigParser()
graphdata.read('data.ini')


sections=graphdata.sections()


#
# for s in sections:
#     for k in graphdata[s]:
#         print(graphdata[s][k])
#
dict_events_raw={}

for e in graphdata['events']:
    dict_events_raw[e]=(graphdata['events'][e])

print(dict_events_raw)
print("--- raw end")
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



print(dict_events)



