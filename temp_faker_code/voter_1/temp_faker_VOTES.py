



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "vote_id": _ + 1,
            "phone_number": fake.random_int(min=1000000000, max=9999999999),
            "state": fake.state_abbr(),
            "contestant_number": fake.random_int(min=1, max=100),
            "created": fake.date_time_this_year()
        }
        data.append(record)
    return data
