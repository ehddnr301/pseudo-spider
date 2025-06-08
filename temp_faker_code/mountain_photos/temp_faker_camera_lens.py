


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "brand": fake.company(),
            "name": fake.word(),
            "focal_length_mm": round(random.uniform(10.0, 300.0), 1),
            "max_aperture": round(random.uniform(1.4, 22.0), 1)
        }
        data.append(record)
    return data
