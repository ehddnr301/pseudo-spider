


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Employee_ID": fake.uuid4(),
            "Year_awarded": str(fake.date_time_this_year().year),
            "Bonus": round(random.uniform(1000, 10000), 2)
        }
        data.append(record)
    return data
