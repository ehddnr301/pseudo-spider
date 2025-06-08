



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Role_Code": fake.bothify(text='???-######', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
            "Role_Name": fake.job(),
            "Role_Description": fake.sentence()
        }
        data.append(record)
    return data
