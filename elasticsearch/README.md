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
docker run --name my_elasticsearch_7 -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch_7
```

Output:
```sh
{"type": "server", "timestamp": "2022-08-13T21:38:46,065Z", "level": "INFO", "component": "o.e.n.Node", "cluster.name": "docker-cluster", "node.name": "0d5e6362fc25", "message": "version[7.17.5], pid[8], build[default/docker/8d61b4f7ddf931f219e3745f295ed2bbc50c8e84/2022-06-23T21:57:28.736740635Z], OS[Linux/5.10.47-linuxkit/amd64], JVM[Oracle Corporation/OpenJDK 64-Bit Server VM/18.0.1.1/18.0.1.1+2-6]" }
{"type": "server", "timestamp": "2022-08-13T21:38:46,074Z", "level": "INFO", "component": "o.e.n.Node", "cluster.name": "docker-cluster", "node.name": "0d5e6362fc25", "message": "JVM home [/usr/share/elasticsearch/jdk], using bundled JDK [true]" }
{"type": "server", "timestamp": "2022-08-13T21:38:46,076Z", "level": "INFO", "component": "o.e.n.Node", "cluster.name": "docker-cluster", "node.name": "0d5e6362fc25", "message": "JVM arguments [-Xshare:auto, -Des.networkaddress.cache.ttl=60, -Des.networkaddress.cache.negative.ttl=10, -XX:+AlwaysPreTouch, -Xss1m, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djna.nosys=true, -XX:-OmitStackTraceInFastThrow, -XX:+ShowCodeDetailsInExceptionMessages, -Dio.netty.noUnsafe=true, -Dio.netty.noKeySetOptimization=true, -Dio.netty.recycler.maxCapacityPerThread=0, -Dio.netty.allocator.numDirectArenas=0, -Dlog4j.shutdownHookEnabled=false, -Dlog4j2.disable.jmx=true, -Dlog4j2.formatMsgNoLookups=true, -Djava.locale.providers=SPI,COMPAT, --add-opens=java.base/java.io=ALL-UNNAMED, -Djava.security.manager=allow, -XX:+UseG1GC, -Djava.io.tmpdir=/tmp/elasticsearch-11754709223291658995, -XX:+HeapDumpOnOutOfMemoryError, -XX:+ExitOnOutOfMemoryError, -XX:HeapDumpPath=data, -XX:ErrorFile=logs/hs_err_pid%p.log, -Xlog:gc*,gc+age=trace,safepoint:file=logs/gc.log:utctime,pid,tags:filecount=32,filesize=64m, -Des.cgroups.hierarchy.override=/, -Xms992m, -Xmx992m, -XX:MaxDirectMemorySize=520093696, -XX:G1HeapRegionSize=4m, -XX:InitiatingHeapOccupancyPercent=30, -XX:G1ReservePercent=15, -Des.path.home=/usr/share/elasticsearch, -Des.path.conf=/usr/share/elasticsearch/config, -Des.distribution.flavor=default, -Des.distribution.type=docker, -Des.bundled_jdk=true]" }
{"type": "server", "timestamp": "2022-08-13T21:38:48,909Z", "level": "INFO", "component": "o.e.p.PluginsService", "cluster.name": "docker-cluster", "node.name": "0d5e6362fc25", "message": "loaded module [aggs-matrix-stats]" }
...
```

Now we are able to enter into the running image in order to execute some examples
```sh
docker exec -it my_elasticsearch_7 /bin/bash
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
python3 elastic_first_connection.py
```

We can avoid the first lines of the output because we haven't configured the security, so that's the reason for the message.

Output:
```sh
elastic_first_connection.py:5: ElasticsearchWarning: Elasticsearch built-in security features are not enabled. Without authentication, your cluster could be accessible to anyone. See https://www.elastic.co/guide/en/elasticsearch/reference/7.17/security-minimal-setup.html to enable security.
  resp = es.info()

{'name': '0d5e6362fc25', 'cluster_name': 'docker-cluster', 'cluster_uuid': '8zVf_MuGTLGbUyFQFjALYQ', 'version': {'number': '7.17.5', 'build_flavor': 'default', 'build_type': 'docker', 'build_hash': '8d61b4f7ddf931f219e3745f295ed2bbc50c8e84', 'build_date': '2022-06-23T21:57:28.736740635Z', 'build_snapshot': False, 'lucene_version': '8.11.1', 'minimum_wire_compatibility_version': '6.8.0', 'minimum_index_compatibility_version': '6.0.0-beta1'}, 'tagline': 'You Know, for Search'}
```

## Index document
This example is trying to explain how to index a document in elasticsearch index.
File: [elastic_index_document.py](elastic_index_document.py)

Code:
```python
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

document = {
    "name": "Luke Skywalker",
    "height": "172",
    "mass": "77",
    "hair_color": "blond",
    "skin_color": "fair",
    "eye_color": "blue",
    "birth_year": "19BBY",
    "gender": "male",
    "homeworld": "https://swapi.dev/api/planets/1/",
    "films": [
        "https://swapi.dev/api/films/2/",
        "https://swapi.dev/api/films/6/",
        "https://swapi.dev/api/films/3/",
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/7/"
    ],
    "species": [
        "https://swapi.dev/api/species/1/"
    ],
    "vehicles": [
        "https://swapi.dev/api/vehicles/14/",
        "https://swapi.dev/api/vehicles/30/"
    ],
    "starships": [
        "https://swapi.dev/api/starships/12/",
        "https://swapi.dev/api/starships/22/"
    ],
    "created": "2014-12-09T13:50:51.644000Z",
    "edited": "2014-12-20T21:17:56.891000Z",
    "url": "https://swapi.dev/api/people/1/",
    'timestamp': datetime.now(),
}

resp = es.index(index="starwars-characters", id=1, document=document)
print(resp['result'])
```

How to run the code:
```sh
python3 elastic_index_document.py
```

Output:
```sh
created
```

## Get document
In this section we are going to get a document from an index of elasticsearch.
File: [elasticsearch_get_document.py](elasticsearch_get_document.py)

Code:
```python
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

resp = es.get(index="starwars-characters", id=1)
print(resp)
```

How to run the code:
```sh
python3 elastic_get_document.py
```

Output:
```sh
{'_index': 'starwars-characters', '_type': '_doc', '_id': '1', '_version': 1, '_seq_no': 0, '_primary_term': 1, 'found': True, '_source': {'name': 'Luke Skywalker', 'height': '172', 'mass': '77', 'hair_color': 'blond', 'skin_color': 'fair', 'eye_color': 'blue', 'birth_year': '19BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/1/', 'films': ['https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/6/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/7/'], 'species': ['https://swapi.dev/api/species/1/'], 'vehicles': ['https://swapi.dev/api/vehicles/14/', 'https://swapi.dev/api/vehicles/30/'], 'starships': ['https://swapi.dev/api/starships/12/', 'https://swapi.dev/api/starships/22/'], 'created': '2014-12-09T13:50:51.644000Z', 'edited': '2014-12-20T21:17:56.891000Z', 'url': 'https://swapi.dev/api/people/1/', 'timestamp': '2022-08-16T14:55:26.117959'}}
```

## Refresh index
In this section we are going to refresh an index of elasticsearch
File: [elastic_refresh_index.py](elastic_refresh_index.py)

Code:
```python
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

res = es.indices.refresh(index="starwars-characters")
print(res)
```

How to run the code:
```sh
python3 elastic_refresh_index.py
```

Output:
```sh
{'_shards': {'total': 2, 'successful': 1, 'failed': 0}}
```

## Search document
In this section we are going to search in a index of elasticsearch
File: [elastic_search_document.py](elastic_search_document.py)

Code:
```python
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

resp = es.search(index="starwars-characters", query={"match_all": {}})

#print(resp)

print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print("%(name)s" % hit["_source"])
```

How to run the code:
```sh
python3 elastic_search_document.py
```

Output:
```sh
Got 1 Hits:
Luke Skywalker
```

## Update document
In this section we are going to update a document from index in elasticsearch
File: [elastic_update_document.py](elastic_update_document.py)

Code:
```python
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

document = {
    "name": "Luke Skywalker (the best)",
    "height": "172",
    "mass": "77",
    "hair_color": "blond",
    "skin_color": "fair",
    "eye_color": "blue",
    "birth_year": "19BBY",
    "gender": "male",
    "homeworld": "https://swapi.dev/api/planets/1/",
    "films": [
        "https://swapi.dev/api/films/2/",
        "https://swapi.dev/api/films/6/",
        "https://swapi.dev/api/films/3/",
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/7/"
    ],
    "species": [
        "https://swapi.dev/api/species/1/"
    ],
    "vehicles": [
        "https://swapi.dev/api/vehicles/14/",
        "https://swapi.dev/api/vehicles/30/"
    ],
    "starships": [
        "https://swapi.dev/api/starships/12/",
        "https://swapi.dev/api/starships/22/"
    ],
    "created": "2014-12-09T13:50:51.644000Z",
    "edited": "2014-12-20T21:17:56.891000Z",
    "url": "https://swapi.dev/api/people/1/",
    'timestamp': datetime.now(),
}

resp = es.update(index="starwars-characters", id=1, body={"doc":document})
print(resp['result'])
```

How to run the code:
```sh
python3 elastic_update_document.py
```

Output:
```sh
Got 1 Hits:
Luke Skywalker
```

## Delete document
In this section we are going to delete a document in index of elasticsearch
File: [elastic_delete_document.py](elastic_delete_document.py)

Code:
```python
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

resp = es.delete(index="starwars-characters", id=1)

print(resp['result'])
```

How to run the code:
```sh
python3 elastic_delete_document.py
```

Output:
```sh
deleted
```
