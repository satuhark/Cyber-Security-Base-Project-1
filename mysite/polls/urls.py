from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.index, name='index'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('trigger-error/', views.trigger_error, name='trigger_error'),
]