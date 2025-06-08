



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Essn": random.randint(10000, 99999),
            "Dependent_name": fake.name(),
            "Sex": random.choice(['M', 'F']),
            "Bdate": fake.date_time_this_year().strftime('%Y-%m-%d'),
            "Relationship": random.choice(['Child', 'Spouse', 'Parent', 'Sibling'])
        }
        data.append(record)
    return data
