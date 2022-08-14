from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

resp = es.search(index="starwars-characters", query={"match_all": {}})

#print(resp)

print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print("%(name)s" % hit["_source"])