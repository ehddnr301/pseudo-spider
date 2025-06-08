



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "customer_id": random.randint(1, 1000),
            "customer_first_name": fake.first_name(),
            "customer_last_name": fake.last_name(),
            "customer_address": fake.address(),
            "customer_phone": fake.phone_number(),
            "customer_email": fake.email(),
            "other_customer_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    
    return data
