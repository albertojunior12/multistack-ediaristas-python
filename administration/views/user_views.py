from django.shortcuts import render, redirect

from administration.forms.user_forms import UserForm


def user_create(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserForm()
    return render(request, 'users/user_form.html', {'user_form': user_form})
