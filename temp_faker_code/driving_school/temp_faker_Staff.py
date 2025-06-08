



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "staff_id": _ + 1,
            "staff_address_id": random.randint(1, 100),
            "nickname": fake.first_name(),
            "first_name": fake.first_name(),
            "middle_name": fake.first_name(),
            "last_name": fake.last_name(),
            "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=65),
            "date_joined_staff": fake.date_time_this_year(),
            "date_left_staff": fake.date_time_this_year() 
        }
        data.append(record)
    return data
