



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "address_id": _ + 1,
            "line_1_number_building": fake.building_number() + " " + fake.street_name(),
            "town_city": fake.city(),
            "zip_postcode": fake.zipcode(),
            "state_province_county": fake.state(),
            "country": fake.country()
        }
        data.append(record)
    
    return data
