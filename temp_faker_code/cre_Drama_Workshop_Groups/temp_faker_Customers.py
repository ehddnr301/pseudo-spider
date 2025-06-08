



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    fake_data = []
    for _ in range(num_records):
        record = {
            "Customer_ID": fake.uuid4(),
            "Address_ID": random.randint(1, 1000),
            "Customer_Name": fake.name(),
            "Customer_Phone": fake.phone_number(),
            "Customer_Email_Address": fake.email(),
            "Other_Details": fake.text(max_nb_chars=255)
        }
        fake_data.append(record)
    return fake_data
