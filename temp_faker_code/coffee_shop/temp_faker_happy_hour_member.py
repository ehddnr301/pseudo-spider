



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "HH_ID": random.randint(1, 1000),
            "Member_ID": random.randint(1, 1000),
            "Total_amount": round(random.uniform(10.0, 500.0), 2)
        }
        data.append(record)
    
    return data
