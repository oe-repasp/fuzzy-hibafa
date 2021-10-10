from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.aws.network import Route53

with Diagram("Fuzzy Fault Tree Analysis", show=True):
    level0 = Route53("Main event")
    level1 = Custom("and","..\pict\logic_and.png")

    # with Cluster("LEVEL 1 Events"):
    #     svc_group = [ECS("event1"),
    #                  ECS("event2"),
    #                  ECS("event3")]
    #
    # with Cluster("DB Cluster"):
    #     db_main = RDS("userdb")
    #     db_main - [RDS("userdb ro")]

    level1 >> level0
    svc_group >> level1