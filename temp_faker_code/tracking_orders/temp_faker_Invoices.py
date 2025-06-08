


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    fake_data = []
    for _ in range(num_records):
        invoice = {
            "invoice_number": random.randint(1, 1000),
            "invoice_date": fake.date_time_this_year(),
            "invoice_details": fake.sentence(nb_words=10)
        }
        fake_data.append(invoice)
    return fake_data
