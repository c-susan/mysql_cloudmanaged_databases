import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from faker import Faker
import numpy as np

# Load environment variables
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
#DB_PORT = int(os.getenv("DB_PORT", 3306))
#DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}'
engine = create_engine(
        connection_string,
        connect_args=connect_args,
)


# Create a database engine
# db_engine = create_engine(conn_string, echo=False)
fake = Faker()

departments = ['Pediatric', 'Orthopedics', 'Neurology', 'Cardiology', 'Oncology']
medications = ['Ibuprofen', 'Amoxicillin', 'Tylenol', 'Omeprazole', 'Metoprolol']

def insert_fake_data(engine, num_patients=100, num_providers=20, num_medications=5, num_prescriptions=100):
    # Start a connection
    with engine.connect() as connection:
        # Insert fake data into patients
        for _ in range(num_patients):
            first_name = fake.first_name()
            last_name = fake.last_name()
            date_of_birth = fake.date_of_birth(minimum_age=10, maximum_age=90)
            gender = np.random.choice(["M", "F"], p=[0.5, 0.5])
            address = fake.address().replace('\n', ', ')
            phone_number = fake.phone_number()
            connection.execute(f"""
                INSERT INTO patients (first_name, last_name,
                                date_of_birth, gender, address, phone_number)
                VALUES ('{first_name}', '{last_name}', '{date_of_birth}', '{gender}',
                '{address}', '{phone_number}') 
            """)
        
        # Insert fake data into the providers table
        for _ in range(num_providers):
            first_name = fake.first_name()
            last_name = fake.last_name()
            department = np.random.choice(departments)
            connection.execute(f"""
                INSERT INTO providers (first_name, last_name, department)
                VALUES ('{first_name}', '{last_name}', '{department}')
            """)
                   
        # Insert fake data into the medications table
        for medication in medications:
            dosage = np.random.choice(['20mg', '40mg', '60mg'], p=[0.5, 0.5])
            route_of_administration = 'Oral'
            connection.execute(f"""
                INSERT INTO medications (medication_name, dosage, route_of_administration)
                VALUES ('{medication}', '{dosage}', '{route_of_administration}')
            """)

        # Fetch all patient IDs and medication IDs
            patient_ids = [row[0] for row in connection.execute("SELECT patient_id FROM patients").fetchall()] 
            medication_ids = [row[0] for row in connection.execute("SELECT medication_id FROM medications").fetchall()] 
            provider_ids = [row[0] for row in connection.execute("SELECT provider_id FROM providers").fetchall()] 

        # Insert fake data into the prescriptions table
        for _ in range(num_prescriptions):        
            patient_id = np.random.choice(patient_ids)
            medication_id = np.random.choice(medication_ids)
            provider_id = np.random.choice(provider_ids)
            prescribed_date = fake.date_between(start_date="-5y", end_date="today")
            connection.execute(f"""
                INSERT INTO prescriptions (patient_id, medication_id, provider_id, prescribed_date) 
                VALUES ({patient_id}, {medication_id}, {provider_id}, '{prescribed_date}'
            """)


if __name__ == "__main__":
    insert_fake_data(engine)
    print("Fake data insertion complete!")