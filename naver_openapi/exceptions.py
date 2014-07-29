class InvalidAPIArgumentsException(Exception):
    """ Invalid API arguments. """
    def __str__(self):
        return 'Invalid API arguments.'


class APIServiceEndedException(Exception):
    """ The api service is ended. """
    def __str__(self):
        return 'The api service is ended.'

