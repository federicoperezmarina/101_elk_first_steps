from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

res = es.indices.refresh(index="starwars-characters")
print(res)