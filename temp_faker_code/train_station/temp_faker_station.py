



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Station_ID": _ + 1,
            "Name": fake.city(),
            "Annual_entry_exit": round(random.uniform(100000, 1000000), 2),
            "Annual_interchanges": round(random.uniform(10000, 500000), 2),
            "Total_Passengers": round(random.uniform(50000, 2000000), 2),
            "Location": fake.address(),
            "Main_Services": fake.word(),
            "Number_of_Platforms": random.randint(1, 10)
        }
        data.append(record)
    return data
