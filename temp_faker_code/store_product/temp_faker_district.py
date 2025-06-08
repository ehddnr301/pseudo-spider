


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "District_ID": _ + 1,
            "District_name": fake.city(),
            "Headquartered_City": fake.city(),
            "City_Population": round(random.uniform(10000, 1000000), 2),
            "City_Area": round(random.uniform(10, 500), 2)
        }
        data.append(record)
    return data
