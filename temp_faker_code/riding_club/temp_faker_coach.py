



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Coach_ID": fake.unique.random_int(min=1, max=1000),
            "Coach_name": fake.name(),
            "Gender": random.choice(['Male', 'Female']),
            "Club_ID": fake.random_int(min=1, max=100),
            "Rank": fake.random_int(min=1, max=10)
        }
        data.append(record)
    return data
