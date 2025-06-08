


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "thing_id": fake.random_int(min=1, max=1000),
            "Date_and_Time": fake.date_time_this_year(),
            "Location_Code": fake.bothify(text='???-######', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        }
        data.append(record)
    return data
