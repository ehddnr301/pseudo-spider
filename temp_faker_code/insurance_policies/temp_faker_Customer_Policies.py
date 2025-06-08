


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Policy_ID": fake.random_int(min=1, max=1000),
            "Customer_ID": fake.random_int(min=1, max=1000),
            "Policy_Type_Code": fake.lexify(text='?????'),
            "Start_Date": fake.date_time_this_year().date(),
            "End_Date": fake.date_time_this_year().date()
        }
        data.append(record)
    return data
