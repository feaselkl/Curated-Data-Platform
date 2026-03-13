import os
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.database import Mssql, Oracle
from diagrams.onprem.inmemory import Redis, Memcached, Hazelcast
from diagrams.azure.database import SQLDatabases, CacheForRedis
from diagrams.azure.storage import BlobStorage
from diagrams.aws.database import RDS, Elasticache
from diagrams.aws.storage import S3
from diagrams.custom import Custom

_dir = os.path.dirname(os.path.abspath(__file__))

node_attr = {
    "fontsize":"20"
}
graph_attr = {
    "fontsize":"28"
}

with Diagram("", show=False, direction="TB", node_attr=node_attr,
             filename=os.path.join(_dir, "..", "presentation", "assets", "image", "04_KeyValuePlayers")):
    with Cluster("On-Premises", graph_attr=graph_attr):
        with Cluster("Relational Database", graph_attr=graph_attr):
            relational = [Mssql(""), Oracle("")]
        with Cluster("Cache", graph_attr=graph_attr):
            cache = [Redis("\nRedis"), Custom("\nValkey", os.path.join(_dir, "custom_logos", "valkey-logo-og.png")), Memcached("\nMemcached"), Hazelcast("\nHazelcast")]

    with Cluster("Cloud", graph_attr=graph_attr):
        with Cluster("Azure", graph_attr=graph_attr):
                azure = BlobStorage("\nBlob Storage") >> SQLDatabases("\nSQL DB") >> CacheForRedis("\nRedis")
        with Cluster("AWS", graph_attr=graph_attr):
            aws = S3("\nS3") >> RDS("\nRDS") >> Elasticache("\nElasticache")

