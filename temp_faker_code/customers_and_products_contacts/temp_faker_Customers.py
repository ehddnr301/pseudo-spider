



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "customer_id": random.randint(1, 1000),
            "payment_method_code": fake.random_element(elements=("CREDIT", "DEBIT", "CASH")),
            "customer_number": fake.unique.random_int(min=1000000000, max=9999999999),
            "customer_name": fake.name(),
            "customer_address": fake.address(),
            "customer_phone": fake.phone_number(),
            "customer_email": fake.email()
        }
        data.append(record)
    return data
