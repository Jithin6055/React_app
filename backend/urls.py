from django.urls import path
from . import views 

urlpatterns = [
    path('questions',views.getquestions,name='getquestions'),
    path('question/<str:pk>',views.getquestion,name='getquestion'),
]