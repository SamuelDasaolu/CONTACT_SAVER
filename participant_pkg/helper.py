def get_name() -> str:
    # Name Collection and Validation
    while True:
        name = input(" \n Enter Participant Name: ").title()
        if name.strip() and len(name.strip().split()) == 2:
            break
        print(' \n Name cannot be empty and must be of format: FirstName LastName e.g John Smith')
           
    return name


def get_age() -> int:
    # Age Collection and Validation
    while True:
        age = input('Enter Participant Age: ')
        if age and age.isdigit() and int(age) > 0:
            break # Age is valid
        print(' \n Age must be a non-zero positive integer')
        
    return int(age)


def get_phone() -> str:
    # Phone Collection and Verification
    while True:
        phone_number = input("Enter Phone Number: ")
        if phone_number:
            if (phone_number.strip().startswith('+') or phone_number.strip().isdigit()) and len(phone_number) >= 10:
                break
            print(" \n Invalid Phone Number Entered \n Phone Number can only be of Forms: \n 0********* or +************* \n And is at least 10 digits")
        print(" \n Phone Number cannot be Empty")
    
    return phone_number


def get_track() -> str:
    # Track Collection and verification
    while True:
        track = input("Enter Participant Track: ")
        if track:
            break
        print('Response is invalid')
        
    return track
    