



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    treatments = []
    
    for _ in range(num_records):
        treatment = {
            "treatment_id": _ + 1,
            "dog_id": random.randint(1, 100),
            "professional_id": random.randint(1, 50),
            "treatment_type_code": fake.random_element(elements=("VACC", "CHECK", "SURG")),
            "date_of_treatment": fake.date_time_this_year(),
            "cost_of_treatment": round(random.uniform(10.0, 500.0), 4)
        }
        treatments.append(treatment)
    
    return treatments
