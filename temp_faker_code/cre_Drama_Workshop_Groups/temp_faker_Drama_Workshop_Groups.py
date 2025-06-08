



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Workshop_Group_ID": _ + 1,
            "Address_ID": random.randint(1, 100),
            "Currency_Code": fake.currency_code(),
            "Marketing_Region_Code": fake.bothify(text='??-###'),
            "Store_Name": fake.company(),
            "Store_Phone": fake.phone_number(),
            "Store_Email_Address": fake.email(),
            "Other_Details": fake.sentence()
        }
        data.append(record)
    return data
