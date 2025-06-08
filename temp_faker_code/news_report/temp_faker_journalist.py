



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        journalist = {
            "journalist_ID": _ + 1,
            "Name": fake.name(),
            "Nationality": fake.country(),
            "Age": str(random.randint(25, 60)),
            "Years_working": random.randint(1, 35)
        }
        data.append(journalist)
    return data
