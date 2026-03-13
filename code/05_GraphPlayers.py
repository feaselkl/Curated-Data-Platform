import os
from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.onprem.database import Neo4J
from diagrams.azure.database import CosmosDb
from diagrams.aws.database import Neptune

_dir = os.path.dirname(os.path.abspath(__file__))

node_attr = {
    "fontsize":"20"
}
graph_attr = {
    "fontsize":"28"
}

with Diagram("", show=False, direction="TB", node_attr=node_attr,
             filename=os.path.join(_dir, "..", "presentation", "assets", "image", "05_GraphPlayers")):
    with Cluster("On-Premises", graph_attr=graph_attr):
         onprem = [Neo4J("\nNeo4J")]

    with Cluster("Cloud", graph_attr=graph_attr):
        with Cluster("Azure", graph_attr=graph_attr):
                fabric = Custom("\nFabric\n(preview)", os.path.join(_dir, "custom_logos", "fabric.png"))
                azure = [CosmosDb("\nCosmos DB"), fabric]
        with Cluster("AWS", graph_attr=graph_attr):
            aws = [Neptune("\nNeptune")]
        