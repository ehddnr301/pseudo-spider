



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "individual_id": random.randint(1, 1000),
            "organization_id": random.randint(1, 1000),
            "date_contact_from": fake.date_time_this_year(),
            "date_contact_to": fake.date_time_this_year()
        }
        data.append(record)
    return data
