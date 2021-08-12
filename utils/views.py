
from django.http import JsonResponse

def error_404(request, exception):
    response = JsonResponse(data={'message' : 'invalid endpoint', 'status_code' : 404 })
    response.status_code = 404
    return response

def error_500(request):
    response = JsonResponse(data={'message' : 'Error occured on the server side', 'status_code' : 500 })
    response.status_code = 500
    return response