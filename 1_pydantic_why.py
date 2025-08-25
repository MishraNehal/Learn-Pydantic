from pydantic import BaseModel, EmailStr, AnyUrl, Field  # Importing required modules/libraries
from typing import List, Dict, Optional, Annotated  # Importing required modules/libraries

class Patient(BaseModel):  # Defining a Pydantic model (data schema)

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]  # Assigning a value or defining a field
    email: EmailStr  # Code execution or logic here
    linkedin_url: AnyUrl  # Code execution or logic here
    age: int = Field(gt=0, lt=120)  # Assigning a value or defining a field
    weight: Annotated[float, Field(gt=0, strict=True)]  # Assigning a value or defining a field
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]  # Assigning a value or defining a field
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]  # Assigning a value or defining a field
    contact_details: Dict[str, str]  # Code execution or logic here


def update_patient_data(patient: Patient):  # Defining a function or validator method

    print(patient.name)  # Code execution or logic here
    print(patient.age)  # Code execution or logic here
    print(patient.allergies)  # Code execution or logic here
    print(patient.married)  # Code execution or logic here
    print('updated')  # Code execution or logic here

patient_info = {'name':'nitish', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '30', 'weight': 75.2,'contact_details':{'phone':'2353462'}}  # Assigning a value or defining a field

patient1 = Patient(**patient_info)  # Assigning a value or defining a field

update_patient_data(patient1)  # Code execution or logic here