


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Template_ID": fake.random_int(min=1, max=1000),
            "Version_Number": fake.random_int(min=1, max=10),
            "Template_Type_Code": fake.lexify(text='?????'),
            "Date_Effective_From": fake.date_time_this_year(),
            "Date_Effective_To": fake.date_time_this_year(),
            "Template_Details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
