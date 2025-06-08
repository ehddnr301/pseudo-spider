



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "address_id": random.randint(1, 65535),
            "address": fake.street_address(),
            "address2": fake.secondary_address(),
            "district": fake.city(),
            "city_id": random.randint(1, 65535),
            "postal_code": fake.zipcode(),
            "phone": fake.phone_number(),
            "last_update": fake.date_time_this_year()
        }
        data.append(record)
    return data
