class InvalidAPIArgumentsException(Exception):
    """ Invalid api arguments """
    def __str__(self):
        return ''


class APIServiceEndedException(Exception):
    """ The api service is ended. """
    def __str__(self):
        return 'The api service is ended.'

