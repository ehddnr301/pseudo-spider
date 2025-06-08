



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "common_name": fake.word(),
            "protein_name": fake.word(),
            "divergence_from_human_lineage": random.uniform(0, 1),
            "accession_number": fake.word(),
            "sequence_length": random.uniform(100, 1000),
            "sequence_identity_to_human_protein": fake.word(),
            "Institution_id": fake.word()
        }
        data.append(record)
    return data
