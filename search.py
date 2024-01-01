from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=["http://127.0.0.1:9200"])

# Define the category
category = "dessert"

# Define the search query
search_query = {
    "query": {
        "match": {
            "description": "milk"
        }
    }
}

# Execute the search query in the specified category index
response = es.search(index=f'{category}_index', body=search_query)

# Print the search results
for hit in response['hits']['hits']:
    print(hit['_source'])



######  ALL INDEXES ######
#all_indices = es.indices.get_alias(index="*")

# Print the list of indices
#print(all_indices.keys())