


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "constructorResultsId": fake.random_int(min=1, max=1000),
            "raceId": fake.random_int(min=1, max=100),
            "constructorId": fake.random_int(min=1, max=100),
            "points": round(fake.random_number(digits=2) * random.uniform(0.1, 1.0), 2),
            "status": fake.random_element(elements=("Finished", "Retired", "Disqualified"))
        }
        data.append(record)
    return data
