



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "staff_id": random.randint(1, 255),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "address_id": random.randint(1, 65535),
            "picture": None,
            "email": fake.email(),
            "store_id": random.randint(1, 255),
            "active": random.choice([True, False]),
            "username": fake.user_name(),
            "password": fake.password(),
            "last_update": fake.date_time_this_year()
        }
        data.append(record)
    return data
