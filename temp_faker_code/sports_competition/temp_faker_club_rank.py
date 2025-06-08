



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Rank": random.uniform(1, 100),
            "Club_ID": random.randint(1, 1000),
            "Gold": random.uniform(0, 100),
            "Silver": random.uniform(0, 100),
            "Bronze": random.uniform(0, 100),
            "Total": random.uniform(0, 300)
        }
        data.append(record)
    return data
