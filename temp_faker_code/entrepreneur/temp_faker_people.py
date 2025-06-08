


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "People_ID": _ + 1,
            "Name": fake.name(),
            "Height": round(random.uniform(1.5, 2.0), 2),
            "Weight": round(random.uniform(50.0, 100.0), 2),
            "Date_of_Birth": fake.date_time_this_year().strftime("%Y-%m-%d")
        }
        data.append(record)
    return data
