



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Document_ID": fake.unique.random_int(min=1, max=10000),
            "Budget_Type_Code": fake.lexify(text='?????'),
            "Document_Details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
