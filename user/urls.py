from django.urls import path
from user.views import login_request 
urlpatterns = [
    path('login/', login_request, name='login'),
    
]