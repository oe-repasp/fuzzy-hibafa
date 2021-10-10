from typing import List

from diagrams import Cluster, Diagram
from diagrams.custom import Custom


with Diagram("Fuzzy Fault Tree Analysis", show=True):
    level0 = Custom("Main event","..\pict\main_event.png")
    level1gate = Custom("AND","..\pict\logic_and.png")
    level2gate = Custom("OR","..\pict\logic-or.png")

    with Cluster("LEVEL 1 Events"):
        level1 = [
            Custom("Event 1","..\pict\event_1.png"),
            Custom("Event 2","..\pict\event_2.png"),
            Custom("Event 3","..\pict\event_3.png")]

    with Cluster("LEVEL 2 Events"):
        level2 = [
            Custom("Event 4","..\pict\event_4.png"),
            Custom("Event 5","..\pict\event_5.png")]

    level2 >> level2gate >> level1 >> level1gate >> level0


