


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Settlement_ID": random.randint(1, 1000),
            "Claim_ID": random.randint(1, 100),
            "Effective_Date": fake.date_time_this_year().date(),
            "Settlement_Amount": round(random.uniform(1000, 50000), 2)
        }
        data.append(record)
    return data
