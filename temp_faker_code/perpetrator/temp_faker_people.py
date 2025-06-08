



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "People_ID": _ + 1,
            "Name": fake.name(),
            "Height": round(random.uniform(1.5, 2.0), 2),
            "Weight": round(random.uniform(50, 100), 2),
            "Home Town": fake.city()
        }
        data.append(record)
    
    return data
