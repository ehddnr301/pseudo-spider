



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Location_Code": fake.bothify(text='???-######')[:15],
            "Location_Name": fake.city(),
            "Location_Description": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
