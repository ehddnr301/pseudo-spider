



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "party_id": random.randint(1, 1000),
            "address_id": random.randint(1, 1000),
            "date_address_from": fake.date_time_this_year(),
            "address_type_code": fake.word()[:15],
            "date_address_to": fake.date_time_this_year() 
        }
        data.append(record)
    return data
