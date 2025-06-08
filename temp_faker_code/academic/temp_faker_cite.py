



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        record = {
            "cited": random.randint(1, 1000),
            "citing": random.randint(1, 1000)
        }
        data.append(record)
    return data
