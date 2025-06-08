



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Driver_ID": _ + 1,
            "Name": fake.name(),
            "Party": fake.word(),
            "Home_city": fake.city(),
            "Age": random.randint(18, 70)
        }
        data.append(record)
    return data
