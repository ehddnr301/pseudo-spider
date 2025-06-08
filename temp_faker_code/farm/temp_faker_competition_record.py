



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        record = {
            "Competition_ID": random.randint(1, 1000),
            "Farm_ID": random.randint(1, 100),
            "Rank": random.randint(1, 10)
        }
        data.append(record)
    return data
