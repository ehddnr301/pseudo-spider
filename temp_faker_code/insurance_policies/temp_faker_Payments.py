


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Payment_ID": _ + 1,
            "Settlement_ID": random.randint(1, 100),
            "Payment_Method_Code": fake.word(),
            "Date_Payment_Made": fake.date_time_this_year().date(),
            "Amount_Payment": random.randint(1, 10000)
        }
        data.append(record)
    return data
