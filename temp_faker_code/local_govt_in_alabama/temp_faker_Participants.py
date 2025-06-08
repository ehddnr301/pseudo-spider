



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "Participant_ID": i + 1,
            "Participant_Type_Code": fake.lexify(text='?????'),
            "Participant_Details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
