


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        year = fake.date_time_this_year().year
        url = fake.url()
        data.append({
            "year": year,
            "url": url
        })
    return data
