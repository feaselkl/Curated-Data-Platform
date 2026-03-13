import os
from diagrams import Cluster, Diagram
from diagrams.azure.analytics import Databricks
from diagrams.azure.database import DataLake, SQLDatawarehouse
from diagrams.aws.analytics import Redshift
from diagrams.aws.storage import S3
from diagrams.gcp.storage import Storage
from diagrams.gcp.analytics import BigQuery
from diagrams.custom import Custom

_dir = os.path.dirname(os.path.abspath(__file__))

node_attr = {
    "fontsize":"20"
}
graph_attr = {
    "fontsize":"28"
}

with Diagram("", show=False, direction="TB", node_attr=node_attr,
             filename=os.path.join(_dir, "..", "presentation", "assets", "image", "02b_ModernDWPlayers")):
    with Cluster("Azure", graph_attr=graph_attr):
        azdatalake = DataLake("\nData Lake\nStorage Gen2")
        databricks = Databricks("\nDatabricks")
        fabric = Custom("\nFabric", os.path.join(_dir, "custom_logos", "fabric.png"))
        snowflake = Custom("\nSnowflake", os.path.join(_dir, "custom_logos", "snowflake.png"))
        azdatalake >> databricks
        azdatalake >> fabric
        azdatalake >> snowflake
    with Cluster("AWS", graph_attr=graph_attr):
        s3 = S3("\nS3")
        databricks = Databricks("\nDatabricks")
        redshift = Redshift("\nRedshift")
        snowflake = Custom("\nSnowflake", os.path.join(_dir, "custom_logos", "snowflake.png"))
        s3 >> databricks
        s3 >> redshift
        s3 >> snowflake
    with Cluster("GCP", graph_attr=graph_attr):
        gcs = Storage("\nGCS")
        databricks = Databricks("\nDatabricks")
        bigquery = BigQuery("\nBigQuery")
        snowflake = Custom("\nSnowflake", os.path.join(_dir, "custom_logos", "snowflake.png"))
        gcs >> databricks
        gcs >> bigquery
        gcs >> snowflake
        