from django.urls import path
from .views import CreateAccountView
from .views import ViewAccountView
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/', ViewAccountView.as_view(), name='viewAccount'),
]
