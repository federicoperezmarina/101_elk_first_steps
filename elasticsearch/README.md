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


## How to connect
This is an example to learn how to connect to elasticsearch
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
