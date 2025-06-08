


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Furniture_ID": _ + 1,
            "Name": fake.word(),
            "Num_of_Component": random.randint(1, 10),
            "Market_Rate": round(random.uniform(50.0, 500.0), 2)
        }
        data.append(record)
    return data
