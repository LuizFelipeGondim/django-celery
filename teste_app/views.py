from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts


def teste_view(request):
    form = GenerateRandomUserForm(request.POST)

   
    
    context = {
        'form':form,
    }

    return render(request, 'teste.html', context)

        