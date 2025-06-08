



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "Record_ID": random.randint(1, 1000),
            "Pilot_ID": random.randint(1, 100),
            "Aircraft_ID": random.randint(1, 50),
            "Date": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
        }
        data.append(record)
    
    return data
