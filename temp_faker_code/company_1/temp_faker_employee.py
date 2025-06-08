



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Fname": fake.first_name(),
            "Minit": fake.random_letter().upper(),
            "Lname": fake.last_name(),
            "Ssn": fake.unique.random_int(min=100000000, max=999999999),
            "Bdate": fake.date_time_this_year().date().isoformat(),
            "Address": fake.address().replace("\n", ", "),
            "Sex": random.choice(["M", "F"]),
            "Salary": fake.random_int(min=30000, max=120000),
            "Super_ssn": fake.random_int(min=100000000, max=999999999),
            "Dno": fake.random_int(min=1, max=5)
        }
        data.append(record)
    return data
