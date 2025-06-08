



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        address_id = i + 1
        address_details = fake.address().replace('\n', ', ')
        data.append({
            "address_id": address_id,
            "address_details": address_details
        })
    return data
