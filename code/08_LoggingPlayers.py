from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.logging import Loki
from diagrams.onprem.aggregator import Fluentd
from diagrams.elastic.elasticsearch import Logstash, Elasticsearch, Kibana
from diagrams.onprem.search import Solr
from diagrams.onprem.database import Influxdb, Clickhouse
from diagrams.onprem.monitoring import Grafana,  Prometheus, Thanos, Splunk
from diagrams.azure.analytics import LogAnalyticsWorkspaces
from diagrams.aws.management import Cloudwatch

node_attr = {
    "fontsize":"20"
}
graph_attr = {
    "fontsize":"28"
}

with Diagram("", show=False, node_attr=node_attr):
    with Cluster("Log Aggregation", graph_attr=graph_attr):
        logstash = Logstash("\nLogstash")
        fluentd = Fluentd("\nFluentd")
        loki = Loki("\nLoki")
        logstash - Edge(style="invis") - fluentd - Edge(style="invis") - loki
    
    with Cluster("Monitoring", graph_attr=graph_attr):
        prometheus = Prometheus("\nPrometheus")
        thanos = Thanos("\nThanos")
        splunk = Splunk("\nSplunk")
        prometheus - Edge(style="invis") - splunk - Edge(style="invis") - thanos

    with Cluster("Storage", graph_attr=graph_attr):
        with Cluster("Logs", graph_attr = graph_attr):
            elasticsearch = Elasticsearch("\nElasticsearch")
            clickhouse = Clickhouse("\nClickHouse")
            elasticsearch - Edge(style="invis") - clickhouse

        with Cluster("Metrics", graph_attr = graph_attr):
            influx = Influxdb("\nInfluxDB")
            prometheus2 = Prometheus("\nPrometheus")
            prometheus2 - Edge(style="invis") - influx

        loki >> elasticsearch
        thanos >> prometheus2

    with Cluster("Visualization", graph_attr=graph_attr):
        kibana = Kibana("\nKibana")
        grafana = Grafana("\nGrafana")
        influx >> kibana
        clickhouse >> grafana

    with Cluster("Cloud", graph_attr=graph_attr):
        with Cluster("Azure", graph_attr=graph_attr):
            azlog = LogAnalyticsWorkspaces("\nLog Analytics")
        with Cluster("AWS", graph_attr=graph_attr):
            awslog = Cloudwatch("\nCloudwatch")

    grafana - Edge(style="invis") - awslog
    kibana - Edge(style="invis") - azlog