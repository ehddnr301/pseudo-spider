


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Customer_Event_Note_ID": fake.random_int(min=1, max=1000),
            "Customer_Event_ID": fake.random_int(min=1, max=1000),
            "service_type_code": fake.lexify(text='?????'),
            "resident_id": fake.random_int(min=1, max=1000),
            "property_id": fake.random_int(min=1, max=1000),
            "date_moved_in": fake.date_time_this_year()
        }
        data.append(record)
    return data
