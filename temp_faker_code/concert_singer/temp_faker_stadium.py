



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Stadium_ID": _ + 1,
            "Location": fake.city(),
            "Name": fake.company() + " Stadium",
            "Capacity": random.randint(10000, 100000),
            "Highest": random.randint(10000, 100000),
            "Lowest": random.randint(1000, 10000),
            "Average": random.randint(10000, 100000)
        }
        data.append(record)
    return data
