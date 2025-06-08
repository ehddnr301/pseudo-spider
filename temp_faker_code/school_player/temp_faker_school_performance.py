


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "School_Id": random.randint(1, 1000),
            "School_Year": fake.date_time_this_year().strftime("%Y"),
            "Class_A": fake.word(),
            "Class_AA": fake.word()
        }
        data.append(record)
    return data
