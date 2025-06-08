



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "Manager_ID": _ + 1,
            "Name": fake.name(),
            "Country": fake.country(),
            "Working_year_starts": fake.date_time_this_year().strftime("%Y-%m-%d"),
            "Age": random.randint(25, 60),
            "Level": random.randint(1, 5)
        }
        data.append(record)
    
    return data
