


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ID": _ + 1,
            "Music_Festival": fake.catch_phrase(),
            "Date_of_ceremony": fake.date_time_this_year().strftime("%Y-%m-%d"),
            "Category": fake.word(),
            "Volume": random.randint(1, 100),
            "Result": fake.word()
        }
        data.append(record)
    return data
