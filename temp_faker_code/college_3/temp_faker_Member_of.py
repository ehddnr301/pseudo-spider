


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "FacID": fake.random_int(min=1, max=100),
            "DNO": fake.random_int(min=1, max=50),
            "Appt_Type": fake.random_element(elements=("Checkup", "Consultation", "Follow-up", "Emergency"))
        }
        data.append(record)
    return data
