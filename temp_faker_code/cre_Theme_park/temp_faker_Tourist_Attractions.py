



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Tourist_Attraction_ID": _ + 1,
            "Attraction_Type_Code": fake.lexify(text='?????'),
            "Location_ID": random.randint(1, 100),
            "How_to_Get_There": fake.sentence(),
            "Name": fake.name(),
            "Description": fake.sentence(),
            "Opening_Hours": fake.time(),
            "Other_Details": fake.sentence()
        }
        data.append(record)
    return data
