from diagrams import Cluster, Diagram, Edge
from diagrams.elastic.elasticsearch import Elasticsearch
from diagrams.onprem.database import Postgresql
from diagrams.azure.web import Search
from diagrams.azure.database import SQLDatabases, DatabaseForPostgresqlServers, CosmosDb
from diagrams.aws.database import Aurora
from diagrams.aws.analytics import AmazonOpensearchService
from diagrams.custom import Custom

node_attr = {
    "fontsize":"20"
}
graph_attr = {
    "fontsize":"28"
}

with Diagram("", show=False, direction="TB", node_attr=node_attr):
    with Cluster("On-Premises", graph_attr=graph_attr):
        with Cluster("Commercial Platforms", graph_attr=graph_attr):
            closed_source = [Custom("\nPinecone", "./custom_logos/pinecone.png")]

        with Cluster("Open Source Platforms", graph_attr=graph_attr):
            Elasticsearch("\nElasticsearch") - Edge(style="invis") - Postgresql("\nPostgreSQL")
            Custom("\nQdrant", "./custom_logos/qdrant.png") - Edge(style="invis") - Custom("\nMilvus", "./custom_logos/milvus.png")
            Custom("\nChromaDB", "./custom_logos/chromadb.png") - Edge(style="invis") - Custom("\nWeaviate", "./custom_logos/weaviate.png")

    with Cluster("Cloud", graph_attr=graph_attr):
        with Cluster("Azure", graph_attr=graph_attr):
            SQLDatabases("\nAzure SQL\nDatabase") - Edge(style="invis") - DatabaseForPostgresqlServers("\nPostgreSQL")
            CosmosDb("\nCosmos DB") - Edge(style="invis") - Search("\nAI Search")
        with Cluster("AWS", graph_attr=graph_attr):
            Aurora("\nAurora") - Edge(style="invis") - AmazonOpensearchService("\nOpenSearch")
        