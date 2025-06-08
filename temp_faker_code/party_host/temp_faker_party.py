



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Party_ID": _ + 1,
            "Party_Theme": fake.word(),
            "Location": fake.city(),
            "First_year": str(fake.date_time_this_year().year),
            "Last_year": str(fake.date_time_this_year().year),
            "Number_of_hosts": random.randint(1, 100)
        }
        data.append(record)
    return data
