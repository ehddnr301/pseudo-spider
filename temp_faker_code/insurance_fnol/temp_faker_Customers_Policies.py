


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Customer_ID": fake.random_int(min=1, max=1000),
            "Policy_ID": fake.random_int(min=1, max=1000),
            "Date_Opened": fake.date_time_this_year().date(),
            "Date_Closed": fake.date_time_this_year().date()
        }
        data.append(record)
    return data
