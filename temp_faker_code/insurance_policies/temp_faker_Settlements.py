


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "Settlement_ID": i + 1,
            "Claim_ID": random.randint(1, 1000),
            "Date_Claim_Made": fake.date_time_this_year().date(),
            "Date_Claim_Settled": fake.date_time_this_year().date(),
            "Amount_Claimed": random.randint(1000, 10000),
            "Amount_Settled": random.randint(1000, 10000),
            "Customer_Policy_ID": random.randint(1, 500)
        }
        data.append(record)
    return data
