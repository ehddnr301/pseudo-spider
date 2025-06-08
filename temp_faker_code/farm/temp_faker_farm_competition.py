



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Competition_ID": _ + 1,
            "Year": fake.date_time_this_year().year,
            "Theme": fake.catch_phrase(),
            "Host_city_ID": random.randint(1, 100),
            "Hosts": fake.company()
        }
        data.append(record)
    return data
