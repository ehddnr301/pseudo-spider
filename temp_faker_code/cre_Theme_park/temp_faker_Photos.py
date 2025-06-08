


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Photo_ID": _ + 1,
            "Tourist_Attraction_ID": random.randint(1, 100),
            "Name": fake.name(),
            "Description": fake.sentence(),
            "Filename": fake.file_name(),
            "Other_Details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
