



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Campus": random.randint(1, 10),
            "Year": fake.date_time_this_year().year,
            "TotalEnrollment_AY": random.randint(1000, 5000),
            "FTE_AY": random.randint(500, 2000)
        }
        data.append(record)
    return data
