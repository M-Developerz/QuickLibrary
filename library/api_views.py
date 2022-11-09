from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return JsonResponse(data={'message': 'Hello World'}, status=200)