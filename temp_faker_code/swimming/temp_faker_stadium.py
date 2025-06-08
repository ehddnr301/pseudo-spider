



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ID": _ + 1,
            "name": fake.company() + " Stadium",
            "Capacity": random.randint(10000, 100000),
            "City": fake.city(),
            "Country": fake.country(),
            "Opening_year": fake.date_time_this_year().year
        }
        data.append(record)
    return data
