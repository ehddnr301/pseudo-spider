



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "eid": random.randint(1, 999999999),
            "aid": random.randint(1, 999999999)
        }
        data.append(record)
    return data
