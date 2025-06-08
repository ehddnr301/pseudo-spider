


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "property_id": random.randint(1, 1000),
            "feature_id": random.randint(1, 100),
            "property_feature_description": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
