


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Manufacturer_ID": random.randint(1, 1000),
            "Open_Year": fake.date_time_this_year().year + random.uniform(0, 1),
            "Name": fake.company(),
            "Num_of_Factories": random.randint(1, 100),
            "Num_of_Shops": random.randint(1, 100)
        }
        data.append(record)
    return data
