


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "Customer_Event_ID": i + 1,
            "customer_id": random.randint(1, 100),
            "date_moved_in": fake.date_time_this_year(),
            "property_id": random.randint(1, 50),
            "resident_id": random.randint(1, 100),
            "thing_id": random.randint(1, 100)
        }
        data.append(record)
    return data
