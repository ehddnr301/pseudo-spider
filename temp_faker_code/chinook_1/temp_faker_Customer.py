



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "CustomerId": _ + 1,
            "FirstName": fake.first_name(),
            "LastName": fake.last_name(),
            "Company": fake.company(),
            "Address": fake.address().replace("\n", ", "),
            "City": fake.city(),
            "State": fake.state(),
            "Country": fake.country(),
            "PostalCode": fake.zipcode(),
            "Phone": fake.phone_number(),
            "Fax": fake.phone_number(),
            "Email": fake.email(),
            "SupportRepId": random.randint(1, 10)  # Assuming SupportRepId is a foreign key to another table
        }
        data.append(record)
    return data
