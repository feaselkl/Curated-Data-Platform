from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.database import Mssql, Oracle
from diagrams.onprem.inmemory import Redis, Memcached, Hazelcast
from diagrams.azure.database import SQLDatabases, CacheForRedis
from diagrams.azure.storage import BlobStorage
from diagrams.aws.database import RDS, Elasticache
from diagrams.aws.storage import S3

node_attr = {
    "fontsize":"20"
}
graph_attr = {
    "fontsize":"28"
}

with Diagram("", show=False, direction="TB", node_attr=node_attr):
    with Cluster("On-Premises", graph_attr=graph_attr):
        with Cluster("Relational Database", graph_attr=graph_attr):
            relational = [Mssql(""), Oracle("")]
        with Cluster("Cache", graph_attr=graph_attr):
            cache = [Redis("\nRedis"), [Memcached("\nMemcached")], Hazelcast("\nHazelcast")]

    with Cluster("Cloud", graph_attr=graph_attr):
        with Cluster("Azure", graph_attr=graph_attr):
                azure = [SQLDatabases("\nSQL DB")] >> CacheForRedis("\nRedis") >> BlobStorage("\nBlob Storage")
        with Cluster("AWS", graph_attr=graph_attr):
            aws = [RDS("\nRDS")] >> Elasticache("\nElasticache") >> S3("\nS3")
        