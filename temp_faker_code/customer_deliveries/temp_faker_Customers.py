



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "customer_id": _ + 1,
            "payment_method": random.choice(['credit_card', 'debit_card', 'paypal']),
            "customer_name": fake.name(),
            "customer_phone": fake.phone_number(),
            "customer_email": fake.email(),
            "date_became_customer": fake.date_time_this_year()
        }
        data.append(record)
    return data
