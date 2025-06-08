



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    fake_data = []
    for _ in range(num_records):
        record = {
            "address_id": _ + 1,
            "line_1": fake.street_address(),
            "line_2": fake.secondary_address(),
            "line_3": fake.street_name(),
            "city": fake.city(),
            "zip_postcode": fake.zipcode(),
            "state_province_county": fake.state(),
            "country": fake.country(),
            "other_address_details": fake.sentence()
        }
        fake_data.append(record)
    return fake_data
