CREATE TABLE patients(
	patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE 	NOT NULL,
    gender VARCHAR(10) NOT NULL,
    address TEXT,
    phone_number VARCHAR(10) NOT NULL
);

CREATE TABLE providers (
	provider_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL
); 

CREATE TABLE medications (
	medication_id INT PRIMARY KEY AUTO_INCREMENT,
    medication_name TEXT NOT NULL, 
    dosage VARCHAR(20) NOT NULL, 
    route_of_administration TEXT NOT NULL
);

CREATE TABLE prescriptions (
	prescription_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    medication_id INT,
    provider_id INT,
    prescribed_date DATE NOT NULL,
    FOREIGN KEY (medication_id) REFERENCES medications(medication_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id)
);
