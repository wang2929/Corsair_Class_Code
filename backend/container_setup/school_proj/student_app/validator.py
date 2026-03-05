import re
from django.core.exceptions import ValidationError

def validate_name_format(name):
    error_msg = "Name must be in the format \"First Middle Initial. Last\""
    regex = r"[A-Z][a-z]+\s[A-Z]\.\s[A-Z][a-z]+"
    good_name = re.match(regex, name)
    if good_name:
        return name
    else:
        raise ValidationError(error_msg, params={ 'name': name })

def validate_school_email(email):
    error_msg = "Invalid school email format. Please use an email ending with \"@school.com\"."
    regex = r".+@school\.com$"
    email_list = email.split('@')
    email_list[-1] = email_list[-1].lower()
    email = '@'.join(email_list)
    good_email = re.match(regex, email)
    if good_email:
        return email
    else:
        raise ValidationError(error_msg, params={ 'email': email })

def validate_combination(combo):
    error_msg = "Combination must be in the format \"12-12-12\""
    regex = r"[0-9]{2}-[0-9]{2}-[0-9]{2}"
    good_combo = re.match(regex, combo)
    if good_combo:
        return combo
    else:
        raise ValidationError(error_msg, params={ 'combination': combo })

def validate_locker_number_low(val):
    error_msg = "Ensure this value is greater than or equal to 1."
    good_number = val >= 1
    if good_number:
        return val
    else:
        raise ValidationError(error_msg, params={ 'locker number': val })

def validate_locker_number_high(val):
    error_msg = "Ensure this value is less than or equal to 200."
    good_number = val <= 200
    if good_number:
        return val
    else:
        raise ValidationError(error_msg, params={ 'locker number': val })