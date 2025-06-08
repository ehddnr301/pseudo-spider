


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Climber_ID": random.randint(1, 1000),
            "Name": fake.name(),
            "Country": fake.country(),
            "Time": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "Points": round(random.uniform(0, 100), 2),
            "Mountain_ID": random.randint(1, 100)
        }
        data.append(record)
    return data
