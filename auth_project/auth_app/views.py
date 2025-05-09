from django.shortcuts import render ,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .midialwere import auth, guest
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        initial_data = {'username':'','email':'','password1':'','password2':''}
        form = UserCreationForm(initial = initial_data)
    return render(request, 'auth/register.html', {'form': form})
@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todo_list')
    else:
        initial_data = {'username':'','password':''}
        form = AuthenticationForm(initial = initial_data)
    return render(request, 'auth/login.html', {'form': form})
    
@auth
def todo_list(request):
    todos = Todo.objects.filter(user=request.user).order_by('-id')
    return render(request, 'dashboard.html', {'todos': todos})

@login_required
def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(user=request.user,title=title, description=description)


    return redirect('todo_list')

@login_required
def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

@login_required
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.delete()
    return redirect('todo_list')


@login_required
def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)  # Ensure the todo belongs to the logged-in user
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo.title = title
        todo.description = description
        todo.save()
        return redirect('todo_list')
    return render(request, 'edit_todo.html', {'todo': todo})

def logout_view(request):
    logout(request)
    return redirect('login')

