



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        address_id = random.randint(1, 1000)
        address_details = fake.address()
        data.append({
            "address_id": address_id,
            "address_details": address_details
        })
    return data
