# Pydantic Study Material

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pydantic](https://img.shields.io/badge/Pydantic-%3E=2.0-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Description
This repository contains Python scripts that demonstrate various features of Pydantic. Each script is thoroughly commented, providing detailed, line-by-line explanations to help you understand how Pydantic works and how it can be used effectively in data validation, serialization, and more.

## Installation
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run any of the Python scripts, simply use:
```bash
python <script_name>.py
```
For example:
```bash
python 1_pydantic_why.py
```

## What is Pydantic?
Pydantic is a data validation and settings management library using Python type annotations. It validates the data and provides clear error messages, enabling you to write safer and more maintainable code. It is particularly useful in modern Python applications where type safety and data integrity are paramount.

## Files Included
- **1_pydantic_why.py**: Demonstrates Pydantic field validations, constraints, and annotations.
- **3_model_validator.py**: Showcases model validators to enforce custom logic after model initialization.
- **6_serialization.py**: Illustrates how to perform model serialization and control data representation.
- **requirements.txt**: Specifies project dependencies.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
