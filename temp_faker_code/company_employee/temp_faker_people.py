



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "People_ID": _ + 1,
            "Age": random.randint(18, 80),
            "Name": fake.name(),
            "Nationality": fake.country(),
            "Graduation_College": fake.company()
        }
        data.append(record)
    
    return data
