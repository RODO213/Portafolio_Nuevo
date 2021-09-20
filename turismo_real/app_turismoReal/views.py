from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def vista1(request):
    return HttpResponse("hola buenos dias")


def home(request):
    return render(request, 'htmls/index.html')

def menu(request):
    return render(request, 'incluide/menu.html')

def login(request):
    return render(request, 'htmls/login.html')

def registro(request):
    return render(request, 'htmls/registro.html')

