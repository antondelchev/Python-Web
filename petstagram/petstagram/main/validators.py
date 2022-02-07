from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters.')
    # or:
    # if not all(ch.isalpha() for ch in value)
    #   raise ValidationError('Value must contain only letters.')
