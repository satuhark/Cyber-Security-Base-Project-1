from django.db import connection
from django.contrib.auth.models import User
from .models import Question, Comment
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


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
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
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
    
    if request.method == "POST":
        comment_text = request.POST.get("comment", "")
        if comment_text:
            comment = Comment.objects.create(
                question=question,
                user=request.user,
                text=comment_text
            )
    
    comments = Comment.objects.filter(question=question)
    return render(request, 'polls/detail.html', {'question': question, 'comments': comments})


def index(request):
    return render(request, 'polls/index.html')

def trigger_error(request):
    result = 1 / 0 
    return HttpResponse("This won't be reached.")
