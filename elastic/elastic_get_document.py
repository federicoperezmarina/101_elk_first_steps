from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

resp = es.get(index="starwars-characters", id=1)
print(resp)