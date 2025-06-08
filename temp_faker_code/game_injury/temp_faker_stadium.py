


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "name": fake.company(),
            "Home_Games": random.randint(1, 20),
            "Average_Attendance": round(random.uniform(1000, 50000), 2),
            "Total_Attendance": round(random.uniform(10000, 1000000), 2),
            "Capacity_Percentage": round(random.uniform(50, 100), 2)
        }
        data.append(record)
    return data
