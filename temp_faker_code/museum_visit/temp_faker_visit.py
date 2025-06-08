


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Museum_ID": random.randint(1, 100),
            "visitor_ID": fake.uuid4(),
            "Num_of_Ticket": random.randint(1, 10),
            "Total_spent": round(random.uniform(10.0, 100.0), 2)
        }
        data.append(record)
    return data
