


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Exhibition_ID": _ + 1,
            "Year": fake.year(),
            "Theme": fake.word(),
            "Artist_ID": random.randint(1, 100),
            "Ticket_Price": round(random.uniform(5.0, 100.0), 2)
        }
        data.append(record)
    return data
