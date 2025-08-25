from pydantic import BaseModel  # Importing required modules/libraries

class Address(BaseModel):  # Defining a Pydantic model (data schema)

    city: str  # Code execution or logic here
    state: str  # Code execution or logic here
    pin: str  # Code execution or logic here

class Patient(BaseModel):  # Defining a Pydantic model (data schema)

    name: str  # Code execution or logic here
    gender: str = 'Male'  # Assigning a value or defining a field
    age: int  # Code execution or logic here
    address: Address  # Code execution or logic here

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}  # Assigning a value or defining a field

address1 = Address(**address_dict)  # Assigning a value or defining a field

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}  # Assigning a value or defining a field

patient1 = Patient(**patient_dict)  # Assigning a value or defining a field

temp = patient1.model_dump(exclude_unset=True)  # Assigning a value or defining a field

print(temp)  # Code execution or logic here
print(type(temp))  # Code execution or logic here