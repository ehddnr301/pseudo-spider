



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Conductor_ID": _ + 1,
            "Name": fake.name(),
            "Age": random.randint(25, 65),
            "Nationality": fake.country(),
            "Year_of_Work": random.randint(1, 40)
        }
        data.append(record)
    return data
