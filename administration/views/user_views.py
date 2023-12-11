from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from administration.forms.user_forms import CreateUserForm, EditUserForm


def user_create(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('user_list')
    else:
        user_form = CreateUserForm()
    return render(request, 'users/user_form.html', {'user_form': user_form})


def user_list(request):
    User = get_user_model()
    users = User.objects.filter(is_superuser=True)
    return render(request, 'users/user_list.html', {'users': users})


def user_edit(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)
    user_form = EditUserForm(request.POST or None, instance=user)
    if user_form.is_valid():
        user_form.save()
        return redirect('user_list')
    return render(request, 'users/user_form.html', {'user_form': user_form})
