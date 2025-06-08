



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Race_ID": random.randint(1, 1000),
            "Name": fake.catch_phrase(),
            "Class": fake.word(),
            "Date": fake.date_time_this_year().isoformat(),
            "Track_ID": fake.uuid4()
        }
        data.append(record)
    return data
