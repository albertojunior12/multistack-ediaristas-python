from django.urls import path
from django.urls.base import reverse_lazy
from django.contrib.auth import views as auth_view

from administration.views.service_views import service_create, service_list, service_edit
from administration.views.user_views import user_create, user_list, user_edit

urlpatterns = [
    path('services/create/', service_create, name='service_create'),
    path('services/list/', service_list, name='service_list'),
    path('services/edit/<int:id>/', service_edit, name='service_edit'),
    path('users/create/', user_create, name='user_create'),
    path('users/list/', user_list, name='user_list'),
    path('users/edit/<int:id>/', user_edit, name='user_edit'),
    path('authentication/login/', auth_view.LoginView.as_view(), name='login'),
    path('authentication/logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('change-password/',
         auth_view.PasswordChangeView.as_view(success_url=reverse_lazy('service_list')), name='change_password'),
    path('password-reset/', auth_view.PasswordResetView.as_view(), name='reset_password'),
    path('password-reset/success/', auth_view.PasswordResetDoneView.as_view(), name='reset_password_success'),
    path('password-reset/<str:uidb64>/<str:token>/', auth_view.PasswordResetConfirmView.as_view(),
         name='reset_password_confirm'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(), name='reset_password_done'),
]
