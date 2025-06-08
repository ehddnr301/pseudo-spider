


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Singer_ID": _ + 1,
            "Name": fake.name(),
            "Birth_Year": fake.year(),
            "Net_Worth_Millions": round(random.uniform(1, 100), 2),
            "Citizenship": fake.country()
        }
        data.append(record)
    return data
