


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "City_ID": _ + 1,
            "City": fake.city(),
            "Hanzi": fake.word(),
            "Hanyu_Pinyin": fake.word(),
            "Regional_Population": random.randint(100000, 10000000),
            "GDP": round(random.uniform(10000.0, 1000000.0), 2)
        }
        data.append(record)
    return data
