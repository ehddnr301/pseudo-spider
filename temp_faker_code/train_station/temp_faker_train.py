



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Train_ID": random.randint(1, 1000),
            "Name": fake.name(),
            "Time": fake.date_time_this_year().strftime("%H:%M"),
            "Service": fake.word()
        }
        data.append(record)
    return data
