


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ID": _ + 1,
            "NAME": fake.company(),
            "FOOD_TYPE": random.choice(['Italian', 'Chinese', 'Mexican', 'Indian', 'American']),
            "CITY_NAME": fake.city(),
            "RATING": round(random.uniform(1, 5), 1)
        }
        data.append(record)
    return data
