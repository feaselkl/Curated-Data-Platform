from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.database import Mssql, Mysql, MariaDB, Oracle, Postgresql
from diagrams.azure.database import SQLDatabases, SQLManagedInstances, SQLServers, DatabaseForMysqlServers, DatabaseForMariadbServers, DatabaseForPostgresqlServers
from diagrams.aws.database import RDS, Aurora, Database

node_attr = {
    "fontsize":"20"
}
graph_attr = {
    "fontsize":"28"
}

with Diagram("", show=False, direction="TB", node_attr=node_attr):
    with Cluster("On-Premises", graph_attr=graph_attr):
        with Cluster("Commercial Platforms", graph_attr=graph_attr):
            closed_source = [Oracle(""), Mssql("")]


        with Cluster("Open Source Platforms", graph_attr=graph_attr):
            with Cluster(""):
                mysql = Mysql("")
                mysql >> Edge(style="invis") >> [MariaDB("MariaDB")]
            open_source = [mysql, Postgresql("PostgreSQL")]

    with Cluster("Cloud", graph_attr=graph_attr):
        with Cluster("Azure", graph_attr=graph_attr):
            with Cluster("SQL Server", graph_attr=graph_attr):
                SQLDatabases("\nAzure SQL\nDatabase") - Edge(style="invis") - SQLManagedInstances("\n\nSQL\nManaged\nInstances") - Edge(style="invis") - SQLServers("\nSQL Server\n(IaaS)")
            with Cluster("Other", graph_attr=graph_attr):
                DatabaseForMysqlServers("\nMySQL") - Edge(style="invis") - DatabaseForMariadbServers("\nMariaDB") - Edge(style="invis") - DatabaseForPostgresqlServers("\nPostgreSQL")
        with Cluster("AWS", graph_attr=graph_attr):
            RDS("\n\nRelational\nDatabase\nServices") - Edge(style="invis") - Aurora("\nAurora") - Edge(style="invis") - Database("\nDatabases\n(IaaS)")
        