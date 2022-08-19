import csv
from os.path import abspath, join, dirname, exists
import tqdm
import urllib3
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk

CHUNK_SIZE = 16384

def create_index(client):
    """Creates an index in Elasticsearch if one isn't already there."""
    client.indices.create(
        index="starwars-characters",
        body={
            "settings": {"number_of_shards": 1},
            "mappings": {
                "properties": {
                    "name": {"type": "text"},
                    "heigh": {"type": "text"},
                    "mass": {"type": "text"},
                    "hair_color": {"type": "text"},
                    "skin_color": {"type": "text"},
                    "eye_color": {"type": "text"},
                    "birth_year": {"type": "text"},
                    "gender": {"type": "text"},
                    "species": {"type": "text"}
                }
            },
        },
        ignore=400,
    )


def generate_actions():
    """Reads the file through csv.DictReader() and for each row
    yields a single document. This function is passed into the bulk()
    helper to create many documents in sequence.
    """
    with open('resources/starwars-characters.csv', mode="r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            doc = {
	            "name": row["name"],
	            "heigh": row["heigh"],
	            "mass": row["mass"],
	            "hair_color": row["hair_color"],
	            "skin_color": row["skin_color"],
	            "eye_color": row["eye_color"],
	            "birth_year": row["birth_year"],
	            "gender": row["gender"],
	            "species": row["species"],
            }

            yield doc


def main():

    client = Elasticsearch(
        "http://localhost:9200"
    )

    print("Creating an index...")
    create_index(client)
    exit(1)

    number_of_docs = 87

    print("Indexing documents...")
    progress = tqdm.tqdm(unit="docs", total=number_of_docs)
    successes = 0
    for ok, action in streaming_bulk(
        client=client, index="starwars-characters", actions=generate_actions(),
    ):
        progress.update(1)
        successes += ok
    print("Indexed %d/%d documents" % (successes, number_of_docs))


if __name__ == "__main__":
    main()