from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'gen_pwd/home.html')

def about(request):
    return render(request, 'gen_pwd/about.html')

def password(request):
    character=list("abcdedfghijklmnopqrstuvwxyz")
    thepassword=" "
    length=int(request.GET.get("length",12))
    if request.GET.get("uppercase"):
        character.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("number"):
        character.extend(list("0123456789"))
    if request.GET.get("special character"):
        character.extend(list("!@#$%^&*"))
    for i in range(length):
        thepassword+=random.choice(character)
    return render(request, 'gen_pwd/password.html',{"password": thepassword})