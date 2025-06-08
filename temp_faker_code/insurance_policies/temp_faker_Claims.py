


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Claim_ID": _ + 1,
            "Policy_ID": random.randint(1000, 9999),
            "Date_Claim_Made": fake.date_time_this_year().date(),
            "Date_Claim_Settled": fake.date_time_this_year().date(),
            "Amount_Claimed": random.randint(1000, 50000),
            "Amount_Settled": random.randint(1000, 50000)
        }
        data.append(record)
    return data
