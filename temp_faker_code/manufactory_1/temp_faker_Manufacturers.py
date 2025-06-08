



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Code": _ + 1,
            "Name": fake.company(),
            "Headquarter": fake.city(),
            "Founder": fake.name(),
            "Revenue": round(random.uniform(100000.0, 10000000.0), 2)
        }
        data.append(record)
    return data
