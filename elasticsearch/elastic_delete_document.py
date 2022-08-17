from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

resp = es.delete(index="starwars-characters", id=1)

print(resp['result'])