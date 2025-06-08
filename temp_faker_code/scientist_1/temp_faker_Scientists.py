



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "SSN": random.randint(100000000, 999999999),
            "Name": fake.name()[:30]
        }
        data.append(record)
    return data
