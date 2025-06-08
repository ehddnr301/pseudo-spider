


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "mailshot_id": _ + 1,
            "product_category": fake.word()[:15],
            "mailshot_name": fake.sentence(nb_words=6)[:80],
            "mailshot_start_date": fake.date_time_this_year(),
            "mailshot_end_date": fake.date_time_this_year()
        }
        data.append(record)
    return data
