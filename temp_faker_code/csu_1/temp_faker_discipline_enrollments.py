



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "Campus": random.randint(1, 10),
            "Discipline": random.randint(1, 20),
            "Year": fake.date_time_this_year().year,
            "Undergraduate": random.randint(0, 100),
            "Graduate": random.randint(0, 100)
        }
        data.append(record)
    
    return data
