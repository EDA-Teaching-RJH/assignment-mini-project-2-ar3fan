# Reflection

## Introduction
This project is a Car Service Tracker written in Python. The aim of the project is to help store vehicle information and service records in a simple and organised way. The program demonstrates key programming concepts covered in the module, including object-oriented programming, file handling, regular expressions, libraries, and testing.

## Object-Oriented Programming
I used object-oriented programming to structure the program into classes. The `Vehicle` class stores general vehicle details such as registration, make, model, and year. The `Car` class inherits from `Vehicle` and adds mileage, which demonstrates inheritance. I also created a `ServiceRecord` class to represent individual service entries, and a `ServiceTracker` class to manage collections of vehicles and service records. This helped make the code more organised and easier to extend.

## File Handling
I used file handling to save and load vehicle data using a CSV file. This means the data can still be accessed after the program closes. The `save_vehicles()` function writes vehicle data into `vehicles.csv`, and the `load_vehicles()` function reads it back into the program. I used Python’s `csv` library and `with open(...)` to handle files safely.

## Regular Expressions
I used regular expressions to validate vehicle registration input. This ensures that the registration follows a fixed format before it is accepted into the program. If the format is invalid, the program raises an error. This improved the reliability of user input and helped demonstrate input validation techniques.

## Libraries and Modules
My project uses Python libraries such as `csv` for file handling and `re` for regular expressions. I also separated the program into multiple Python files, such as `vehicle.py`, `tracker.py`, `service_record.py`, and `validators.py`, which reflects the use of modules and improves code organisation.

## Testing
I created tests in `test_validators.py` using `pytest`. These tests check valid, invalid, and empty registration inputs. This helped confirm that the validation function works correctly and showed that I can test my code using multiple conditions and edge cases.

## Challenges
One challenge I faced was duplicate vehicle entries appearing when the CSV file was loaded and saved multiple times. I fixed this by checking the data more carefully and cleaning the CSV file. Another challenge was connecting multiple classes together in a clear way, but using separate classes made the overall structure easier to manage.

## Conclusion
Overall, this project helped me apply the concepts taught in the later part of the module in a practical way. It improved my understanding of Python classes, inheritance, file handling, validation, testing, and modular code design. If I continued developing the project, I would add a menu system, searching features, and saving service records to file as well.