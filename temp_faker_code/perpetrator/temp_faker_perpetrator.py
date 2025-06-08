



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "Perpetrator_ID": _ + 1,
            "People_ID": random.randint(1, 100),
            "Date": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "Year": fake.year(),
            "Location": fake.city(),
            "Country": fake.country(),
            "Killed": random.randint(0, 100),
            "Injured": random.randint(0, 100)
        }
        data.append(record)
    
    return data
