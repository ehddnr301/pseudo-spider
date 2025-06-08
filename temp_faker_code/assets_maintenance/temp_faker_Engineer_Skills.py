



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "engineer_id": fake.random_int(min=1, max=1000),
            "skill_id": fake.random_int(min=1, max=100)
        }
        data.append(record)
    return data
