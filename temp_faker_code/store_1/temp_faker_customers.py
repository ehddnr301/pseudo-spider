



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "company": fake.company(),
            "address": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            "country": fake.country(),
            "postal_code": fake.zipcode(),
            "phone": fake.phone_number(),
            "fax": fake.phone_number(),
            "email": fake.email(),
            "support_rep_id": random.randint(1, 10)  # Assuming support_rep_id is between 1 and 10
        }
        data.append(record)
    
    return data
