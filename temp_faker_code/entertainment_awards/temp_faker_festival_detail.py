



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Festival_ID": _ + 1,
            "Festival_Name": fake.word().capitalize(),
            "Chair_Name": fake.name(),
            "Location": fake.city(),
            "Year": fake.date_time_this_year().year,
            "Num_of_Audience": random.randint(100, 10000)
        }
        data.append(record)
    return data
