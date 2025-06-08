


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "coupon_id": random.randint(1, 1000),
            "date_issued": fake.date_time_this_year(),
            "coupon_amount": round(random.uniform(1, 1000), 4)
        }
        data.append(record)
    return data
