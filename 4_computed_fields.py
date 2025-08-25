from pydantic import BaseModel, EmailStr, computed_field  # Importing required modules/libraries
from typing import List, Dict  # Importing required modules/libraries

class Patient(BaseModel):  # Defining a Pydantic model (data schema)

    name: str  # Code execution or logic here
    email: EmailStr  # Code execution or logic here
    age: int  # Code execution or logic here
    weight: float # kg  # Code execution or logic here
    height: float # mtr  # Code execution or logic here
    married: bool  # Code execution or logic here
    allergies: List[str]  # Code execution or logic here
    contact_details: Dict[str, str]  # Code execution or logic here

    @computed_field  # Code execution or logic here
    @property  # Code execution or logic here
    def bmi(self) -> float:  # Defining a function or validator method
        bmi = round(self.weight/(self.height**2),2)  # Assigning a value or defining a field
        return bmi  # Code execution or logic here



def update_patient_data(patient: Patient):  # Defining a function or validator method

    print(patient.name)  # Code execution or logic here
    print(patient.age)  # Code execution or logic here
    print(patient.allergies)  # Code execution or logic here
    print(patient.married)  # Code execution or logic here
    print('BMI', patient.bmi)  # Code execution or logic here
    print('updated')  # Code execution or logic here

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'height': 1.72, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}  # Assigning a value or defining a field

patient1 = Patient(**patient_info)   # Assigning a value or defining a field

update_patient_data(patient1)  # Code execution or logic here