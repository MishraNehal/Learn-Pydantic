from pydantic import BaseModel, EmailStr, model_validator  # Importing required modules/libraries
from typing import List, Dict  # Importing required modules/libraries

class Patient(BaseModel):  # Defining a Pydantic model (data schema)

    name: str  # Code execution or logic here
    email: EmailStr  # Code execution or logic here
    age: int  # Code execution or logic here
    weight: float  # Code execution or logic here
    married: bool  # Code execution or logic here
    allergies: List[str]  # Code execution or logic here
    contact_details: Dict[str, str]  # Code execution or logic here

    @model_validator(mode='after')  # Assigning a value or defining a field
    def validate_emergency_contact(cls, model):  # Defining a function or validator method
        if model.age > 60 and 'emergency' not in model.contact_details:  # Code execution or logic here
            raise ValueError('Patients older than 60 must have an emergency contact')  # Code execution or logic here
        return model  # Code execution or logic here



def update_patient_data(patient: Patient):  # Defining a function or validator method

    print(patient.name)  # Code execution or logic here
    print(patient.age)  # Code execution or logic here
    print(patient.allergies)  # Code execution or logic here
    print(patient.married)  # Code execution or logic here
    print('updated')  # Code execution or logic here

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}  # Assigning a value or defining a field

patient1 = Patient(**patient_info)   # Assigning a value or defining a field

update_patient_data(patient1)  # Code execution or logic here