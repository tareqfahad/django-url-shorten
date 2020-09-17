from django.urls import path 
from . import views
app_name = 'redirect'

urlpatterns = [
    path('<str:target>/' , views.redirect , name='redirect')
]