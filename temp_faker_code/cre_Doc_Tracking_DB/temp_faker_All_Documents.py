



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Document_ID": random.randint(1, 10000),
            "Date_Stored": fake.date_time_this_year(),
            "Document_Type_Code": fake.lexify(text='?????'),
            "Document_Name": fake.sentence(nb_words=6),
            "Document_Description": fake.sentence(nb_words=10),
            "Other_Details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
