



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": fake.random_int(min=1, max=1000),
            "msid": fake.random_int(min=1, max=1000),
            "aid": fake.random_int(min=1, max=1000),
            "role": fake.random_int(min=1, max=10)
        }
        data.append(record)
    return data
