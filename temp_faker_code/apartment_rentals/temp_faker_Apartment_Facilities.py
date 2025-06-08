



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "apt_id": random.randint(1, 1000),
            "facility_code": fake.bothify(text='???-######')
        }
        data.append(record)
    
    return data
