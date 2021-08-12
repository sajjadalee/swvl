from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):

    """Generate custom response for the Exceptions with error codes"""

    handlers = {
        'ValidationError' : _handle_generic_error,
        'Http404' : _handle_generic_error,
        'PermissionDenied' : _handle_generic_error,
        'NotAuthenticated' : _handle_authentication_error
    }

    response = exception_handler(exc, context)

    if response is not None:
        # import pdb
        # pdb.set_trace()
        if "GroupNotifyView" in str(context['view']) and response.status_code==404:
            response.status_code = 400
            response.data = {'Error' : 'Invalid UUID',
                             'status_code' : 400}
            return response
        response.data['status_code'] = response.status_code

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return response


def _handle_authentication_error(exc, context, response):

    """Throw this exception when user is not authenticated"""

    response.data = {
        'error' : 'Please login to proceed',
        'status_code' : response.status_code
    }
    return response


def _handle_generic_error(exc, context, response):
    """Handling all generic error responses"""
    return response