



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        record = {
            "asset_id": random.randint(1, 1000),
            "part_id": random.randint(1, 1000)
        }
        data.append(record)
    return data
