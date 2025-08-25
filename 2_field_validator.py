from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator  # Importing required modules/libraries
from typing import List, Dict, Optional, Annotated  # Importing required modules/libraries

class Patient(BaseModel):  # Defining a Pydantic model (data schema)

    name: str  # Code execution or logic here
    email: EmailStr  # Code execution or logic here
    age: int  # Code execution or logic here
    weight: float  # Code execution or logic here
    married: bool  # Code execution or logic here
    allergies: List[str]  # Code execution or logic here
    contact_details: Dict[str, str]  # Code execution or logic here

    @field_validator('email')  # Code execution or logic here
    @classmethod  # Code execution or logic here
    def email_validator(cls, value):  # Defining a function or validator method

        valid_domains = ['hdfc.com', 'icici.com']  # Assigning a value or defining a field
        # abc@gmail.com  # Code execution or logic here
        domain_name = value.split('@')[-1]  # Assigning a value or defining a field

        if domain_name not in valid_domains:  # Code execution or logic here
            raise ValueError('Not a valid domain')  # Code execution or logic here

        return value  # Code execution or logic here
    
    @field_validator('name')  # Code execution or logic here
    @classmethod  # Code execution or logic here
    def transform_name(cls, value):  # Defining a function or validator method
        return value.upper()  # Code execution or logic here
    
    @field_validator('age', mode='after')  # Assigning a value or defining a field
    @classmethod  # Code execution or logic here
    def validate_age(cls, value):  # Defining a function or validator method
        if 0 < value < 100:  # Code execution or logic here
            return value  # Code execution or logic here
        else:  # Code execution or logic here
            raise ValueError('Age should be in between 0 and 100')  # Code execution or logic here


def update_patient_data(patient: Patient):  # Defining a function or validator method

    print(patient.name)  # Code execution or logic here
    print(patient.age)  # Code execution or logic here
    print(patient.allergies)  # Code execution or logic here
    print(patient.married)  # Code execution or logic here
    print('updated')  # Code execution or logic here

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}  # Assigning a value or defining a field

patient1 = Patient(**patient_info) # validation -> type coercion  # Assigning a value or defining a field

update_patient_data(patient1)  # Code execution or logic here