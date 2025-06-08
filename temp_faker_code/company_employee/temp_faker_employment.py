



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Company_ID": random.randint(1, 100),
            "People_ID": random.randint(1, 1000),
            "Year_working": random.randint(1, 30)
        }
        data.append(record)
    return data
