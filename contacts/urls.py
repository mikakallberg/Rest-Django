""" Url path for active chats """
from django.urls import path
from contacts import views


urlpatterns = [
    path('contacts/', views.ContactList.as_view()),
    path('contacts/<int:pk>/', views.ContactDetailList.as_view()),
]