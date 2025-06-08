



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "individual_id": _ + 1,
            "individual_first_name": fake.first_name(),
            "individual_middle_name": fake.first_name(),
            "inidividual_phone": fake.phone_number(),
            "individual_email": fake.email(),
            "individual_address": fake.address(),
            "individual_last_name": fake.last_name()
        }
        data.append(record)
    return data
