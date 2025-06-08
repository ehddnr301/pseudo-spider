



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Name": fake.name(),
            "Phone_ID": random.randint(1, 1000),
            "Memory_in_G": random.choice([16, 32, 64, 128, 256]),
            "Carrier": fake.company(),
            "Price": round(random.uniform(100, 1000), 2)
        }
        data.append(record)
    return data
