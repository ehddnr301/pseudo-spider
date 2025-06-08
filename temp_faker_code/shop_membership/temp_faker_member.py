



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Member_ID": _ + 1,
            "Card_Number": fake.credit_card_number(),
            "Name": fake.name(),
            "Hometown": fake.city(),
            "Level": random.randint(1, 10)
        }
        data.append(record)
    return data
