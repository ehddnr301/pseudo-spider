



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Host_ID": _ + 1,
            "Name": fake.name(),
            "Nationality": fake.country(),
            "Age": str(random.randint(18, 80))
        }
        data.append(record)
    return data
