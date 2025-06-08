



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Budget_Type_Code": fake.lexify(text='?????'),
            "Budget_Type_Description": fake.sentence(nb_words=6)
        }
        data.append(record)
    return data
