from django.urls import path

from administration.views import service_create, service_list, service_edit

urlpatterns = [
    path('services/create/', service_create, name='service_create'),
    path('services/list/', service_list, name='service_list'),
    path('services/edit/<int:id>/', service_edit, name='service_edit'),
]
