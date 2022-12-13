from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm


class CreateAccountView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'users/createAccount.html'

class ViewAccountView(generic.DetailView):
	model = CustomUser
	template_name = 'users/viewAccount.html'
	success_url = reverse_lazy('login')

class AllAccountsView(generic.DetailView):
	# model = CustomUser
	template_name = 'users/viewAllAccounts.html'
	success_url = reverse_lazy('login')