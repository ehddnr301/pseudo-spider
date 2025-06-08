



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Marketing_Region_Code": fake.bothify(text='??-#####'),
            "Marketing_Region_Name": fake.city(),
            "Marketing_Region_Descriptrion": fake.sentence(),
            "Other_Details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
