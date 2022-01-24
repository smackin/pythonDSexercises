def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    return phrase[::-1]

my_phrase = reverse_string("Its a good day to have a good day")

print (my_phrase)