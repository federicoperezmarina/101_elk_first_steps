from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

resp = es.info()
print(resp)

