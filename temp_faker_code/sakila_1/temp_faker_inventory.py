


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "inventory_id": random.randint(1, 16777215),  # MEDIUMINT UNSIGNED
            "film_id": random.randint(1, 65535),          # SMALLINT UNSIGNED
            "store_id": random.randint(1, 255),           # TINYINT UNSIGNED
            "last_update": fake.date_time_this_year()     # TIMESTAMP
        }
        data.append(record)
    return data
