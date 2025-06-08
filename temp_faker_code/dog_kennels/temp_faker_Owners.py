



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "owner_id": _ + 1,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "street": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            "zip_code": fake.zipcode(),
            "email_address": fake.email(),
            "home_phone": fake.phone_number(),
            "cell_number": fake.phone_number()
        }
        data.append(record)
    return data
