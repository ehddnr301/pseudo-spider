



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "address_id": _ + 1,
            "address_content": fake.street_address(),
            "city": fake.city(),
            "zip_postcode": fake.zipcode(),
            "state_province_county": fake.state(),
            "country": fake.country(),
            "other_address_details": fake.sentence()
        }
        data.append(record)
    
    return data
