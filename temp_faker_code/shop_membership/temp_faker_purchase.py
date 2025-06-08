



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Member_ID": fake.random_int(min=1, max=1000),
            "Branch_ID": fake.random_element(elements=("A", "B", "C", "D")),
            "Year": str(fake.date_time_this_year().year),
            "Total_pounds": round(random.uniform(1.0, 1000.0), 2)
        }
        data.append(record)
    return data
