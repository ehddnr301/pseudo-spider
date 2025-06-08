



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "document_id": _ + 1,
            "document_status_code": fake.random_element(elements=("Pending", "Approved", "Rejected")),
            "document_type_code": fake.random_element(elements=("Invoice", "Receipt", "Contract")),
            "shipping_agent_code": fake.random_element(elements=("AgentA", "AgentB", "AgentC")),
            "receipt_date": fake.date_time_this_year(),
            "receipt_number": fake.uuid4(),
            "other_details": fake.sentence()
        }
        data.append(record)
    return data
