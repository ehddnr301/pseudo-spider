



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Club_ID": _ + 1,
            "name": fake.company(),
            "Region": fake.city(),
            "Start_year": str(fake.date_time_this_year().year)
        }
        data.append(record)
    return data
