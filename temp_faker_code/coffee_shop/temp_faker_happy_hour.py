



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "HH_ID": _ + 1,
            "Shop_ID": random.randint(1, 100),
            "Month": fake.date_time_this_year().strftime("%B"),
            "Num_of_shaff_in_charge": random.randint(1, 10)
        }
        data.append(record)
    return data
