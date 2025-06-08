



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "InvoiceId": _ + 1,
            "CustomerId": random.randint(1, 1000),
            "InvoiceDate": fake.date_time_this_year(),
            "BillingAddress": fake.street_address(),
            "BillingCity": fake.city(),
            "BillingState": fake.state(),
            "BillingCountry": fake.country(),
            "BillingPostalCode": fake.zipcode(),
            "Total": round(random.uniform(10.00, 1000.00), 2)
        }
        data.append(record)
    return data
