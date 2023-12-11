from django.urls import path

from administration.views.service_views import service_create, service_list, service_edit
from administration.views.user_views import user_create

urlpatterns = [
    path('services/create/', service_create, name='service_create'),
    path('services/list/', service_list, name='service_list'),
    path('services/edit/<int:id>/', service_edit, name='service_edit'),
    path('users/create/', user_create, name='user_create'),
]
