import re
from django.core.exceptions import ValidationError


def phone_validators(value):
    pattern = r'^\+?(48)?\d{9}$'
    if not re.match(pattern,value):
        raise ValidationError('Phone number must be entered in the format +48 _ _ _ _ _ _ _ _ _')