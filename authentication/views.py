from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from authentication.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('authentication:home')
        
        #messages.error(request, 'Login inválido')
    return render(request, 'authentication/index.html', {'form': form})


@login_required(login_url='authentication:index')
def home(request):
    return render(request, 'authentication/home.html')


@login_required(login_url='authentication:index')
def logout_view(request):
    auth.logout(request)
    return redirect('authentication:index')


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('authentication:index')
    return render(request, 'authentication/register.html', {'form': form})





@login_required(login_url='authentication:index')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    if request.method != 'POST':
        return render(
            request,
            'authentication/user_update.html',
            {
                'form': form
            }
        )
    form = RegisterUpdateForm(data=request.POST, instance=request.user)
    if not form.is_valid():
        return render(
            request,
            'authentication/user_update.html',
            {
                'form': form
            }
        )
    form.save()
    messages.success(request, 'Usuário editado com sucesso!')
    return redirect('authentication:home')



@login_required(login_url='authentication:index')
def user_delete(request):
    form = AuthenticationForm(request)
    print(f'USUARIA AQUIII {form.get_user()}')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            user.delete()
            messages.success(request, 'Usuário delatado com sucesso!')
            return redirect('authentication:index')
        
    return render(request, 'authentication/user_delete.html', {'form': form})