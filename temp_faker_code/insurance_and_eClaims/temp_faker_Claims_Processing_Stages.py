



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Claim_Stage_ID": _ + 1,
            "Next_Claim_Stage_ID": random.randint(1, 10),
            "Claim_Status_Name": fake.word(),
            "Claim_Status_Description": fake.sentence()
        }
        data.append(record)
    return data
