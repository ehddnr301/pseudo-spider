



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Employee_ID": _ + 1,
            "Role_Code": fake.lexify(text='?????'),
            "Employee_Name": fake.name(),
            "Gender_MFU": random.choice(['M', 'F']),
            "Date_of_Birth": fake.date_time_this_year(),
            "Other_Details": fake.sentence()
        }
        data.append(record)
    return data
