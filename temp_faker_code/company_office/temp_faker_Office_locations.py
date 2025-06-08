



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "building_id": random.randint(1, 100),
            "company_id": random.randint(1, 100),
            "move_in_year": fake.date_time_this_year().year
        }
        data.append(record)
    return data
