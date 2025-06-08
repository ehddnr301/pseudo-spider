


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Market_ID": _ + 1,
            "District": fake.city(),
            "Num_of_employees": random.randint(1, 100),
            "Num_of_shops": round(random.uniform(1, 50), 2),
            "Ranking": random.randint(1, 10)
        }
        data.append(record)
    return data
