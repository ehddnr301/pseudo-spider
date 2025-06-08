


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        representative = {
            "Representative_ID": fake.random_int(min=1, max=1000),
            "Name": fake.name(),
            "State": fake.state(),
            "Party": random.choice(["Democrat", "Republican", "Independent"]),
            "Lifespan": fake.date_time_this_year().strftime("%Y-%m-%d")
        }
        data.append(representative)
    return data
