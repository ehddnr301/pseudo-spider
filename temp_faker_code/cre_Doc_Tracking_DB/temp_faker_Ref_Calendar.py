



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        record = {
            "Calendar_Date": fake.date_time_this_year(),
            "Day_Number": random.randint(1, 31)
        }
        data.append(record)
    return data
