# Assignment:
# Create a custom exception InvalidAgeError. 
# Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# Define the custom exception
class InvalidAgeError(Exception):
    """Raised when the age is below 18"""
    pass

def check_age(age):
    """Check if age is 18 or older"""
    if age < 18:
        raise InvalidAgeError(f"Age {age} is below minimum required age (18)")
    print(f"Age {age} is valid!")

# Test cases
try:
    check_age(20)  
except InvalidAgeError as e:
    print(f"Error: {e}")

try:
    check_age(15)  
except InvalidAgeError as e:
    print(f"Error: {e}")
