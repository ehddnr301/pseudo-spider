


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Channel_ID": fake.random_int(min=1, max=100),
            "Program_ID": fake.random_int(min=1, max=100),
            "Time_of_day": fake.date_time_this_year().strftime("%H:%M:%S")
        }
        data.append(record)
    return data
