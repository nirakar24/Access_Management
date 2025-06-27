from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User

# Create your views here.

def group_required(group_name):
    def in_group(user):
        return user.is_authenticated and user.groups.filter(name=group_name).exists()
    return user_passes_test(in_group)

@login_required
def view1(request):
    if not request.user.groups.filter(name='Group 1').exists():
        return HttpResponseForbidden(b'You are not allowed to view this page.')
    return render(request, 'view1.html')

@login_required
def view2(request):
    if not request.user.groups.filter(name='Group 2').exists():
        return HttpResponseForbidden(b'You are not allowed to view this page.')
    return render(request, 'view2.html')

@login_required
def view3(request):
    if not request.user.groups.filter(name='Group 3').exists():
        return HttpResponseForbidden(b'You are not allowed to view this page.')
    return render(request, 'view3.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def signup_view(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        group_id = request.POST['group']
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'groups': groups, 'error': 'Username already exists'})
        user = User.objects.create_user(username=username, password=password)
        group = Group.objects.get(id=group_id)
        user.groups.add(group)
        user.save()
        return redirect('login')
    return render(request, 'signup.html', {'groups': groups})

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'dashboard.html', {
        'username': request.user.username,
        'groups': user_groups,
    })

def logout_view(request):
    logout(request)
    return redirect('home')
