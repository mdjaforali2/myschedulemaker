# views.py in time_management_app

from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_GET
from django.urls import reverse
from .models import Task
from .forms import TaskForm

def home(request):
    return render(request, 'time_management_app/home.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'time_management_app/login.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'time_management_app/signup.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'time_management_app/add_task.html', {'form': form})

@login_required
@require_GET
def previous_week(request):
    current_date_str = request.session.get('current_date')
    
    if not current_date_str:
        return HttpResponseBadRequest("Current date not found in session.")
    
    try:
        current_date = datetime.strptime(current_date_str, '%Y-%m-%d').date()
    except ValueError:
        return HttpResponseBadRequest("Invalid date format in session.")
    
    new_date = current_date - timedelta(days=7)
    return redirect(reverse('task_list') + f'?date={new_date}')

@login_required
@require_GET
def next_week(request):
    current_date_str = request.session.get('current_date')
    
    if not current_date_str:
        return HttpResponseBadRequest("Current date not found in session.")
    
    try:
        current_date = datetime.strptime(current_date_str, '%Y-%m-%d').date()
    except ValueError:
        return HttpResponseBadRequest("Invalid date format in session.")
    
    new_date = current_date + timedelta(days=7)
    return redirect(reverse('task_list') + f'?date={new_date}')




# views.py in time_management_app

from django.http import HttpResponseBadRequest
from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from datetime import time, timedelta

@login_required
def task_list(request):
    hours = []

    # Generate hours from 6 am to 5 am (next day), excluding Noon and Midnight
    for hour in range(6, 30):
        current_hour = hour % 24  # Ensure the hours wrap around for the next day
        if current_hour != 0 and current_hour != 12:  # Exclude Midnight and Noon
            hours.append(time(hour=current_hour, minute=0))

    date_param = request.GET.get('date') or request.session.get('current_date')
    try:
        if date_param:
            current_date = timezone.datetime.strptime(date_param, '%Y-%m-%d').date()
        else:
            current_date = timezone.now().date()
    except ValueError:
        return HttpResponseBadRequest("Invalid date format")

    request.session['current_date'] = current_date.strftime('%Y-%m-%d')

    # days = [current_date + timedelta(days=i) for i in range(7)]
    # formatted_days = [day.strftime('%A, %B %d') for day in days]


    tasks = Task.objects.filter(user=request.user)  # Replace with your actual filter conditions

    # Adjust the starting point to Monday
    start_of_week = current_date - timedelta(days=current_date.weekday())

    # Add days to the current_date starting from Monday
    days_to_add = 7  # You can modify this value based on your requirement
    days = [start_of_week + timedelta(days=i) for i in range(days_to_add)]
    formatted_days = [day.strftime('%A') for day in days]

    # Zip days and formatted_days for the inner loop in the template
    days_and_formatted_days = zip(formatted_days, days)

    context = {
        'formatted_days': formatted_days,
        'hours': hours,
        'tasks': tasks,
        'days_and_formatted_days': days_and_formatted_days,
    }

    print(tasks)
    return render(request, 'time_management_app/task_list.html', context)