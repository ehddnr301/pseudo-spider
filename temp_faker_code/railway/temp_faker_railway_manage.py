



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Railway_ID": random.randint(1, 1000),
            "Manager_ID": random.randint(1, 1000),
            "From_Year": str(fake.date_time_this_year().year)
        }
        data.append(record)
    return data
