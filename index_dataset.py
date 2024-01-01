from elasticsearch import Elasticsearch
import pandas as pd

# Define the list of categories
categories = [
    "vegetarian", "vegan", "seafood", "meat", "grill", "pasta", "holiday",
    "dessert", "drink", "beverage", "lunch", "breakfast", "dinner", "appetizer", "snack"
]

# Elasticsearch connection
es = Elasticsearch(hosts=["http://127.0.0.1:9200"])

# Create an index for each category
for category in categories:
    index_name = f'{category}_index'
    index_body = {
        "mappings": {
            "properties": {
                "name": {"type": "text"},
                "description": {"type": "text"},
                "ingredients": {"type": "text"}
            }
        }
    }
    es.indices.create(index=index_name, body=index_body)

# Load data from a DataFrame (e.g., CSV)
data_df = pd.read_csv('processed_recipes.csv')

# Categorize data into respective indexes based on tags
for index, row in data_df.iterrows():
    for category in categories:
        if category in row['tags']:
            doc = {
                'name': row['name'] if not pd.isna(row['name']) else '',
                'description': row['description'] if not pd.isna(row['description']) else '',
                'ingredients': row['ingredients'] if not pd.isna(row['ingredients']) else '',
            }
           # print(doc)
            es.index(index=f'{category}_index', body=doc)

