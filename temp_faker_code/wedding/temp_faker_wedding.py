



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Church_ID": random.randint(1, 100),
            "Male_ID": random.randint(1, 100),
            "Female_ID": random.randint(1, 100),
            "Year": fake.date_time_this_year().year
        }
        data.append(record)
    return data
