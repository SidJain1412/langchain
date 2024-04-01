from elasticsearch import Elasticsearch

# Setup Elasticsearch
# This shows how to set it up for a cloud hosted version

# Password for the 'elastic' user generated by Elasticsearch
ELASTIC_PASSWORD = "..."

# Found in the 'Manage Deployment' page
CLOUD_ID = "..."

# Create the client instance
db = Elasticsearch(cloud_id=CLOUD_ID, basic_auth=("elastic", ELASTIC_PASSWORD))

customers = [
    {"firstname": "Jennifer", "lastname": "Walters"},
    {"firstname": "Monica", "lastname": "Rambeau"},
    {"firstname": "Carol", "lastname": "Danvers"},
    {"firstname": "Wanda", "lastname": "Maximoff"},
    {"firstname": "Jennifer", "lastname": "Takeda"},
]
for i, customer in enumerate(customers):
    db.create(index="customers", document=customer, id=i)
