



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "customer_id": _ + 1,
            "customer_type_code": random.choice(['Individual', 'Business']),
            "address_line_1": fake.street_address(),
            "address_line_2": fake.secondary_address(),
            "town_city": fake.city(),
            "state": fake.state(),
            "email_address": fake.email(),
            "phone_number": fake.phone_number()
        }
        data.append(record)
    return data
