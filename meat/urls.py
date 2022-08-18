from django.urls import path
from meat.views import meats, list_of_meats, update_meats, delete_meats, form_meat




urlpatterns = [
    path('meat/', list_of_meats, name='meat'),
    path('create-meat/', form_meat, name = 'create_meat'),
    path('update-meats/<int:pk>/', update_meats, name= 'update-meats'),
    path('delete-meats/<int:pk>/', delete_meats, name='delete_meats'),
]
