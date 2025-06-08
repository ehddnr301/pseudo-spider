



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Region_ID": random.randint(1, 1000),
            "Region_name": fake.city(),
            "Date": fake.date_time_this_year().isoformat(),
            "Label": fake.word(),
            "Format": fake.word(),
            "Catalogue": fake.word()
        }
        data.append(record)
    return data
