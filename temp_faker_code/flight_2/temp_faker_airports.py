



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "City": fake.city(),
            "AirportCode": fake.unique.lexify(text='???'),
            "AirportName": fake.company() + " Airport",
            "Country": fake.country(),
            "CountryAbbrev": fake.country_code()
        }
        data.append(record)
    return data
