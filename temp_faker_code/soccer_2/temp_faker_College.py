



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "cName": fake.unique.company()[:20],
            "state": fake.state_abbr(),
            "enr": random.randint(0, 99999)
        }
        data.append(record)
    return data
