



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Branch_ID": _ + 1,
            "Name": fake.company(),
            "Open_year": str(fake.date_time_this_year().year),
            "Address_road": fake.street_address(),
            "City": fake.city(),
            "membership_amount": str(random.randint(1, 100))
        }
        data.append(record)
    return data
