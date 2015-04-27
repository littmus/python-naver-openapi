import warnings
from naver_openapi.exceptions import *

def deprecated(func):

    def new_func(*args, **kwargs):
        warnings.warn("%s : This api is no longer serviced." % func.__name__,
                        category=DeprecationWarning)

        raise APIServiceEndedException

    return new_func

