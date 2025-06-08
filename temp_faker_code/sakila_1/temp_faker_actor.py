



from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "actor_id": random.randint(1, 65535),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "last_update": fake.date_time_this_year()
        }
        data.append(record)
    return data
