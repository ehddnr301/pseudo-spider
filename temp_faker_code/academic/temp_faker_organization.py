



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "continent": fake.continent(),
            "homepage": fake.url(),
            "name": fake.company(),
            "oid": random.randint(1, 10000)
        }
        data.append(record)
    return data
