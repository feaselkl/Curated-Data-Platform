import os
from diagrams import Cluster, Diagram
from diagrams.onprem.database import Mongodb, Couchbase
from diagrams.azure.database import CosmosDb
from diagrams.aws.database import Dynamodb

_dir = os.path.dirname(os.path.abspath(__file__))

node_attr = {
    "fontsize":"20"
}
graph_attr = {
    "fontsize":"28"
}

with Diagram("", show=False, direction="TB", node_attr=node_attr,
             filename=os.path.join(_dir, "..", "presentation", "assets", "image", "03_DocumentPlayers")):
    with Cluster("On-Premises", graph_attr=graph_attr):
        onprem = [Mongodb("\nMongoDB"), Couchbase("\nCouchbase")]

    with Cluster("Cloud", graph_attr=graph_attr):
        with Cluster("Azure", graph_attr=graph_attr):
                azure = [CosmosDb("\nCosmos DB")]
        with Cluster("AWS", graph_attr=graph_attr):
            aws = [Dynamodb("\nDynamoDB")]
        