from django.shortcuts import render, redirect
from .models import Users
# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        Users(
            email = request.POST.get('email'),
            password = request.POST.get('password')
        ).save()

        return redirect('index')
    else:
        return render(request, 'signup.html')
def login(request):
    if request.method == 'POST':
        try:
            user = Users.objects.get(
                email=request.POST.get('email'), 
                password=request.POST.get('password')
            )
            request.session['id'] = user.id
            request.session['name'] = user.name
            request.session['email'] = user.email
            return redirect('index')
        except Users.DoesNotExist:
            return render(request, 'login.html', {'msg': 'Invalid username or password'})
    return render(request, 'login.html')
