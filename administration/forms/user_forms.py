from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.is_superuser = True
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class EditUserForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email']
