



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "LOCATION_ID": random.randint(1, 9999),
            "STREET_ADDRESS": fake.street_address(),
            "POSTAL_CODE": fake.zipcode(),
            "CITY": fake.city(),
            "STATE_PROVINCE": fake.state(),
            "COUNTRY_ID": fake.country_code()
        }
        data.append(record)
    
    return data
