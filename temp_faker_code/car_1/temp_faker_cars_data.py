


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Id": _ + 1,
            "MPG": str(random.uniform(10, 40)),
            "Cylinders": random.randint(3, 8),
            "Edispl": round(random.uniform(1.0, 6.0), 1),
            "Horsepower": str(random.randint(50, 300)),
            "Weight": random.randint(1500, 5000),
            "Accelerate": round(random.uniform(5.0, 15.0), 1),
            "Year": fake.date_time_this_year().year
        }
        data.append(record)
    return data
