



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "address_id": _ + 1,
            "line_1_number_building": fake.building_number() + " " + fake.street_name(),
            "city": fake.city(),
            "zip_postcode": fake.zipcode(),
            "state_province_county": fake.state(),
            "country": fake.country()
        }
        data.append(record)
    return data
