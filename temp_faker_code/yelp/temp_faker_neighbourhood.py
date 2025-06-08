


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "business_id": fake.uuid4(),
            "neighbourhood_name": fake.city()
        }
        data.append(record)
    return data
