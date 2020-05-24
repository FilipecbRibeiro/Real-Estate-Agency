from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.receive_form_inquiry,name='contact')
]
