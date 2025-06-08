



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "EmployeeId": _ + 1,
            "LastName": fake.last_name(),
            "FirstName": fake.first_name(),
            "Title": fake.job(),
            "ReportsTo": random.choice([None, random.randint(1, num_records)]),
            "BirthDate": fake.date_time_this_year(),
            "HireDate": fake.date_time_this_year(),
            "Address": fake.address(),
            "City": fake.city(),
            "State": fake.state(),
            "Country": fake.country(),
            "PostalCode": fake.zipcode(),
            "Phone": fake.phone_number(),
            "Fax": fake.phone_number(),
            "Email": fake.email()
        }
        data.append(record)
    return data
