from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('authentication:index')
        
        messages.error(request, 'Login inválido')
    
    return render(
        request,
        'authentication/index.html',
        {
            'form': form
        }
    )

def logout_view(request):
    auth.logout(request)
    return redirect('authentication:index')