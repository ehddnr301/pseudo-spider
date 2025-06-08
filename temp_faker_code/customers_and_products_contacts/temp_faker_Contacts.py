



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "contact_id": _ + 1,
            "customer_id": random.randint(1, 1000),
            "gender": random.choice(['M', 'F']),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "contact_phone": fake.phone_number()
        }
        data.append(record)
    return data
