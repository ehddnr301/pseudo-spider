



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "catalog_level_number": random.randint(1, 100),
            "catalog_id": random.randint(1, 1000),
            "catalog_level_name": fake.word()[:50]
        }
        data.append(record)
    return data
