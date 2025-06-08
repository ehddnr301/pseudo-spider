


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Document_ID": fake.random_int(min=1, max=1000),
            "Location_Code": fake.bothify(text='??###???????', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
            "Date_in_Location_From": fake.date_time_this_year(),
            "Date_in_Locaton_To": fake.date_time_this_year() 
        }
        data.append(record)
    return data
