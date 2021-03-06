from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def landing_page(request):
    return render(request, 'car_renter/application/app.html', {'landing_page': True})


def registration_page(request):
    return render(request, 'car_renter/application/app.html', {'registration_page': True})


@login_required
def renter_panel(request):
    return render(request, 'car_renter/application/app.html', {'renter_panel': True})


@login_required
def user_panel(request):
    return render(request, 'car_renter/application/app.html', {'user_panel': True})


@login_required
def rent_panel(request):
    return render(request, 'car_renter/application/app.html', {'rent_panel': True})


@login_required
def map_panel(request):
    return render(request, 'car_renter/application/app.html', {'map_panel': True})

