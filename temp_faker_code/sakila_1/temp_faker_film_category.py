


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        film_id = random.randint(1, 65535)  # SMALLINT UNSIGNED
        category_id = random.randint(0, 255)  # TINYINT UNSIGNED
        last_update = fake.date_time_this_year()  # TIMESTAMP
        data.append({
            "film_id": film_id,
            "category_id": category_id,
            "last_update": last_update
        })
    return data
