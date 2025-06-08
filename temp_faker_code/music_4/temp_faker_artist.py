


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Artist_ID": _ + 1,
            "Artist": fake.name(),
            "Age": random.randint(18, 70),
            "Famous_Title": fake.sentence(nb_words=3),
            "Famous_Release_date": fake.date_time_this_year().strftime("%Y-%m-%d")
        }
        data.append(record)
    return data
