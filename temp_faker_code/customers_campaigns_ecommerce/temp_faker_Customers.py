



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    fake_data = []
    for _ in range(num_records):
        record = {
            "customer_id": _ + 1,
            "payment_method": random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer']),
            "customer_name": fake.name(),
            "customer_phone": fake.phone_number(),
            "customer_email": fake.email(),
            "customer_address": fake.address(),
            "customer_login": fake.user_name(),
            "customer_password": fake.password(length=10)
        }
        fake_data.append(record)
    return fake_data
