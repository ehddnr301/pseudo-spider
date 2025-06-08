


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        resident_id = random.randint(1, 1000)
        property_id = random.randint(1, 1000)
        date_moved_in = fake.date_time_this_year()
        date_moved_out = fake.date_time_this_year() if random.choice([True, False]) else datetime.now()
        other_details = fake.sentence() 
        
        record = {
            "resident_id": resident_id,
            "property_id": property_id,
            "date_moved_in": date_moved_in,
            "date_moved_out": date_moved_out,
            "other_details": other_details
        }
        data.append(record)
    return data
