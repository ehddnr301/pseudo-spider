



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Journal_ID": _ + 1,
            "Date": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "Theme": fake.sentence(),
            "Sales": random.randint(100, 1000)
        }
        data.append(record)
    return data
