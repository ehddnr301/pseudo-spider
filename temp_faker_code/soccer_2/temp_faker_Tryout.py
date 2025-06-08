



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "pID": fake.random_int(min=1, max=99999),
            "cName": fake.name()[:20],
            "pPos": fake.word()[:8],
            "decision": random.choice(['W', 'L', 'D'])
        }
        data.append(record)
    return data
