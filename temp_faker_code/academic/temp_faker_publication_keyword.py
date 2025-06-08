



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        record = {
            "pid": random.randint(1, 1000),
            "kid": random.randint(1, 100)
        }
        data.append(record)
    return data
