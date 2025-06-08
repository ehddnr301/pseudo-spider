



from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "customer_id": random.randint(1, 65535),
            "store_id": random.randint(1, 255),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "address_id": random.randint(1, 65535),
            "active": random.choice([True, False]),
            "create_date": fake.date_time_this_year(),
            "last_update": fake.date_time_this_year()
        }
        data.append(record)
    return data
