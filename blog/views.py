from http.client import HTTPResponse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello firned, welcome to my first website")