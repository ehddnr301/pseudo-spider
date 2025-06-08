


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "name": fake.word(),
            "Height": round(random.uniform(1000, 8000), 2),
            "Prominence": round(random.uniform(100, 3000), 2),
            "Range": fake.word(),
            "Country": fake.country()
        }
        data.append(record)
    return data
