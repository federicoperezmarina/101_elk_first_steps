# Elasticsearch
Here we have some examples to learn how to use elasticsearch

## Table of Contents
* [Elasticsearch with docker](#elasticsearch-with-docker)
* [How to connect](#how-to-connect)
* [Index document](#index-document)
* [Get document](#get-document)
* [Refresh index](#refresh-index)
* [Search document](#search-document)
* [Update document](#update-document)
* [Delete document](#delete-document) 

## Elasticsearch with docker
This is the Dockerfile that we want to use to build the image of elasticsearch.
```sh
FROM elasticsearch:7.17.5

COPY . .

USER root:root

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    pip3 install elasticsearch

USER elasticsearch:root
```

In the second step we show how to build the image having the dockerfile
```sh
docker build -t elasticsearch_7 .
```

In the third step we are going to run the the docker build image
```sh
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch_7
```

Output:
```sh
{"type": "server", "timestamp": "2022-08-13T21:38:46,065Z", "level": "INFO", "component": "o.e.n.Node", "cluster.name": "docker-cluster", "node.name": "0d5e6362fc25", "message": "version[7.17.5], pid[8], build[default/docker/8d61b4f7ddf931f219e3745f295ed2bbc50c8e84/2022-06-23T21:57:28.736740635Z], OS[Linux/5.10.47-linuxkit/amd64], JVM[Oracle Corporation/OpenJDK 64-Bit Server VM/18.0.1.1/18.0.1.1+2-6]" }
{"type": "server", "timestamp": "2022-08-13T21:38:46,074Z", "level": "INFO", "component": "o.e.n.Node", "cluster.name": "docker-cluster", "node.name": "0d5e6362fc25", "message": "JVM home [/usr/share/elasticsearch/jdk], using bundled JDK [true]" }
{"type": "server", "timestamp": "2022-08-13T21:38:46,076Z", "level": "INFO", "component": "o.e.n.Node", "cluster.name": "docker-cluster", "node.name": "0d5e6362fc25", "message": "JVM arguments [-Xshare:auto, -Des.networkaddress.cache.ttl=60, -Des.networkaddress.cache.negative.ttl=10, -XX:+AlwaysPreTouch, -Xss1m, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djna.nosys=true, -XX:-OmitStackTraceInFastThrow, -XX:+ShowCodeDetailsInExceptionMessages, -Dio.netty.noUnsafe=true, -Dio.netty.noKeySetOptimization=true, -Dio.netty.recycler.maxCapacityPerThread=0, -Dio.netty.allocator.numDirectArenas=0, -Dlog4j.shutdownHookEnabled=false, -Dlog4j2.disable.jmx=true, -Dlog4j2.formatMsgNoLookups=true, -Djava.locale.providers=SPI,COMPAT, --add-opens=java.base/java.io=ALL-UNNAMED, -Djava.security.manager=allow, -XX:+UseG1GC, -Djava.io.tmpdir=/tmp/elasticsearch-11754709223291658995, -XX:+HeapDumpOnOutOfMemoryError, -XX:+ExitOnOutOfMemoryError, -XX:HeapDumpPath=data, -XX:ErrorFile=logs/hs_err_pid%p.log, -Xlog:gc*,gc+age=trace,safepoint:file=logs/gc.log:utctime,pid,tags:filecount=32,filesize=64m, -Des.cgroups.hierarchy.override=/, -Xms992m, -Xmx992m, -XX:MaxDirectMemorySize=520093696, -XX:G1HeapRegionSize=4m, -XX:InitiatingHeapOccupancyPercent=30, -XX:G1ReservePercent=15, -Des.path.home=/usr/share/elasticsearch, -Des.path.conf=/usr/share/elasticsearch/config, -Des.distribution.flavor=default, -Des.distribution.type=docker, -Des.bundled_jdk=true]" }
{"type": "server", "timestamp": "2022-08-13T21:38:48,909Z", "level": "INFO", "component": "o.e.p.PluginsService", "cluster.name": "docker-cluster", "node.name": "0d5e6362fc25", "message": "loaded module [aggs-matrix-stats]" }
...
```

## How to connect
This is an example to learn how to connect to elasticsearch.
File: [elastic_first_connection.py](elastic_first_connection.py)

Code:
```python
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

resp = es.info()
print(resp)
```

How to run the code:
```sh
python elastic_first_connection.py
```

Output:
```sh
{'name': '0d5e6362fc25', 'cluster_name': 'docker-cluster', 'cluster_uuid': '8zVf_MuGTLGbUyFQFjALYQ', 'version': {'number': '7.17.5', 'build_flavor': 'default', 'build_type': 'docker', 'build_hash': '8d61b4f7ddf931f219e3745f295ed2bbc50c8e84', 'build_date': '2022-06-23T21:57:28.736740635Z', 'build_snapshot': False, 'lucene_version': '8.11.1', 'minimum_wire_compatibility_version': '6.8.0', 'minimum_index_compatibility_version': '6.0.0-beta1'}, 'tagline': 'You Know, for Search'}
```

## Index document

## Get document

## Refresh index

## Search document

## Update document

## Delete document
