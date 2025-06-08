



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Pilot_Id": _ + 1,
            "Name": fake.name(),
            "Age": random.randint(18, 65)
        }
        data.append(record)
    return data
