



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Train_ID": random.randint(1, 1000),
            "Train_Num": fake.bothify(text='??###'),
            "Name": fake.company(),
            "From": fake.city(),
            "Arrival": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "Railway_ID": random.randint(1, 100)
        }
        data.append(record)
    return data
