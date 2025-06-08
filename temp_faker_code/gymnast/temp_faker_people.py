


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "People_ID": _ + 1,
            "Name": fake.name(),
            "Age": round(random.uniform(18, 80), 1),
            "Height": round(random.uniform(150, 200), 1),
            "Hometown": fake.city()
        }
        data.append(record)
    return data
