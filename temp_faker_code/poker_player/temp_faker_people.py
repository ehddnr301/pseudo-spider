


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "People_ID": _ + 1,
            "Nationality": fake.country(),
            "Name": fake.name(),
            "Birth_Date": fake.date_time_this_year().strftime("%Y-%m-%d"),
            "Height": round(random.uniform(1.5, 2.0), 2)
        }
        data.append(record)
    return data
