from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Service
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .forms import ServiceForm
# Create your views here.

def service_add(request):
    if request.method=='POST':
        service_form = ServiceForm(request.POST)
        if service_form.is_valid():
            cd = feed_form.cleaned_data
            username = request.user.username
            user = User.objects.get(username=username)
            pregnacies = cd['pregnacies']
            glucose = cd['glucose']
            blood_pressure = cd['blood_pressure']
            skin_thickness = cd['skin_thickness']
            insulin = cd['insulin']
            bmi = cd['bmi']
            diabetes_pedigree = cd['diabetes_pedigree']
            age = cd['age']
            Service.objects.create(user=user, pregnacies=pregnacies, glucose =
                    glucose, blood_pressure = blood_pressure, skin_thickness =
                    skin_thickness, insulin = insulin, bmi = bmi,
                    diabetes_pedigree = diabetes_pedigree, age=age)
    else:
        service_form = ServiceForm()



        return render(request,
            'account/landing.html',{'service_form':service_form})
@login_required
def landing(request):
    return render(request, 'account/landing.html')


