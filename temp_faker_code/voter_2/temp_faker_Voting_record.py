


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "StuID": fake.random_int(min=1000, max=9999),
            "Registration_Date": fake.date_time_this_year().strftime("%Y-%m-%d"),
            "Election_Cycle": fake.word(),
            "President_Vote": fake.random_int(min=0, max=100),
            "Vice_President_Vote": fake.random_int(min=0, max=100),
            "Secretary_Vote": fake.random_int(min=0, max=100),
            "Treasurer_Vote": fake.random_int(min=0, max=100),
            "Class_President_Vote": fake.random_int(min=0, max=100),
            "Class_Senator_Vote": fake.random_int(min=0, max=100)
        }
        data.append(record)
    return data
