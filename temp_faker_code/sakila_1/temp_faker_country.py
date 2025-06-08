



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "country_id": random.randint(1, 65535),
            "country": fake.country()[:50],
            "last_update": fake.date_time_this_year()
        }
        data.append(record)
    return data
