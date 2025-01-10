from django.db import connection
from django.contrib.auth.models import User
from .models import Question
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        # Vulnerable raw SQL query
        #query = f"SELECT * FROM auth_user WHERE username = '{username}' AND password = '{password}'"
        #cursor = connection.cursor()
        #cursor.execute(query)
        #user = cursor.fetchone()

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('polls:index')
        else:
            error = "Invalid username or password"
    
    return render(request, 'polls/login.html', {'error': error})

comments = []

@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if question.user != request.user:
        return HttpResponseForbidden("You do not have permission to access this resource.")
    global comments
    if request.method == "POST":
        comment = request.POST.get("comment", "")
        comments.append(comment)  
    return render(request, 'polls/detail.html', {'question': question, 'comments': comments})


def index(request):
    return render(request, 'polls/index.html')