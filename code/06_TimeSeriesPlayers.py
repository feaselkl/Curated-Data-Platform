import os
from diagrams import Cluster, Diagram
from diagrams.onprem.database import InfluxDB
from diagrams.azure.analytics import DataExplorerClusters
from diagrams.aws.database import Timestream
from diagrams.custom import Custom

_dir = os.path.dirname(os.path.abspath(__file__))

node_attr = {
    "fontsize":"20"
}
graph_attr = {
    "fontsize":"28"
}

with Diagram("", show=False, direction="TB", node_attr=node_attr,
             filename=os.path.join(_dir, "..", "presentation", "assets", "image", "06_TimeSeriesPlayers")):
    with Cluster("On-Premises", graph_attr=graph_attr):
        influx = InfluxDB("\nInfluxDB")
        timescale = Custom("\nTimescaleDB", os.path.join(_dir, "custom_logos", "timescale.png"))

    with Cluster("Cloud", graph_attr=graph_attr):
        with Cluster("Azure", graph_attr=graph_attr):
                azure = [DataExplorerClusters("\nData\nExplorer*")]
        with Cluster("AWS", graph_attr=graph_attr):
            aws = [Timestream("\nTimestream")]
        