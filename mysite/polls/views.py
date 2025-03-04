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
        
        # Vulnerable raw SQL query start
        # query = f"SELECT * FROM auth_user WHERE username = '{username}' AND password = '{password}'"
        # print(f"Executing query: {query}")
        # cursor = connection.cursor()
        # cursor.execute(query)
        # user = cursor.fetchone()
        
        #if user:
            #request.session['user_id'] = user[0]
            #return redirect('polls:index')
        #else:
            #error = "Invalid username or password"
        
        # Vulnerable raw SQL query end
        

        # Authenticate user start
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('polls:index')
        else:
            error = "Invalid username or password"
        # Authenticate user end
    
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