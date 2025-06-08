


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Body_Builder_ID": fake.random_int(min=1, max=1000),
            "People_ID": fake.random_int(min=1, max=1000),
            "Snatch": round(fake.random_number(digits=3) * random.uniform(0.5, 1.5), 2),
            "Clean_Jerk": round(fake.random_number(digits=3) * random.uniform(0.5, 1.5), 2),
            "Total": round(fake.random_number(digits=3) * random.uniform(0.5, 1.5), 2)
        }
        data.append(record)
    return data
