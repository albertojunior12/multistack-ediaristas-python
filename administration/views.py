from django.shortcuts import render, redirect

from administration.forms import ServiceForm
from administration.models import Service


def service_create(request):
    if request.method == "POST":
        service_form = ServiceForm(request.POST)
        if service_form.is_valid():
            service_form.save()
            return redirect('service_list')
    else:
        service_form = ServiceForm()
    return render(request, 'service/service_form.html', {'service_form': service_form})


def service_list(request):
    services = Service.objects.all()
    return render(request, 'service/service_list.html', {'services': services})


def service_edit(request, id):
    service = Service.objects.get(id=id)
    service_form = ServiceForm(request.POST or None, instance=service)
    if service_form.is_valid():
        service_form.save()
        return redirect('service_list')
    return render(request, 'service/service_form.html', {'service_form': service_form})