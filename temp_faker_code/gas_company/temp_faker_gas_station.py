



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Station_ID": _ + 1,
            "Open_Year": random.randint(2000, 2023),
            "Location": fake.city(),
            "Manager_Name": fake.name(),
            "Vice_Manager_Name": fake.name(),
            "Representative_Name": fake.name()
        }
        data.append(record)
    return data
