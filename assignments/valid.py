import re
# All the validation functions use .match to determine the status
def validate_phone_number(phone):
# This pattern is tailored to accept inputs like (xxx)-xxx-xxxx, xxx.xxx.xxxx, (xxx).xxx.xxxx, or xxxxxxxxx
    if re.match(r"^\(?\d{3}\)?[\s\-.]?\d{3}[\s\-.]?\d{4}$", phone):
        print("The phone number is valid")
    else:
        print("The phone number is invalid")


def validate_ssn(number):
# This pattern is tailored to only accept inputs like xxx-xx-xxxx
    if re.match(r"^\d{3}-\d{2}-\d{4}$", number):
        print("The SSN is valid")
    else:
        print("The SSN is invalid")

def validate_zip_code(code):
# This pattern is tailored to accept zip codes that have 5 digits and a dash with 4 more digits if inputted
    if re.match(r"^\d{5}(-\d{4})?$", code):
        print("The zip code is valid")
    else:
        print("The zip code is invalid")

def main():
# Capture the phone number, ssn, and zip code
    phone_number = input("Enter a phone number: ")
    ssn = input("Enter a SSN: ")
    zip_code = input("Enter a zip code: ")
# Use the functions to determine whether the inputs are valid
    validate_phone_number(phone_number)
    validate_ssn(ssn)
    validate_zip_code(zip_code)
# Run the whole thing
if __name__ == '__main__':
    main()