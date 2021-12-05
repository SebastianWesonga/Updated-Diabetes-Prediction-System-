from django.shortcuts import redirect, render
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User, UserManager
from .forms import LoginForm,UserRegistrationForm, ProfileEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from services.models import Service
from services.forms import ServiceForm
from django.shortcuts import get_object_or_404


# Create your views here.
@login_required()
#if user has successfully been authenticated run this
def dashboard(request):
    if request.method=='POST':
        service_form = ServiceForm(request.POST)
        if service_form.is_valid():
            cd = service_form.cleaned_data
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
            return redirect('user:landing')

    else:
        service_form = ServiceForm()

    return render(request,
            'account/dashboard.html',{'service_form':service_form})


def user_register(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      user = authenticate(request, username=cd['username'],password=cd['password'])

      if user is not None:
        login(request,user)
        return redirect('user:dashboard')
      else:
        messages.error(request, "Your Account Does Not Exist")

    else:
      messages.error(request,"Invalid Login")
  else:
    form = LoginForm()

  if request.method == 'POST':
    register_form = UserRegistrationForm(request.POST)
    if register_form.is_valid():
      new_user = register_form.save(commit=False)
      new_user.set_password(register_form.cleaned_data['password'])
      new_user.save()
      Profile.objects.create(user=new_user)
      login(request, new_user)
      messages.success(request,"Account Successfully Created")
      return redirect('user:dashboard')
  else:
    register_form=UserRegistrationForm()
  return render(request, 'account/register.html', {'form':form,'register_form':register_form})


def logout_request(request):
  logout(request)
  messages.info(request, "You Have Successfully Logged Out.")
  return redirect("user:register")

@login_required()
#if user has successfully been authenticated run this
def edit(request):
    username = request.user.username
    user = User.objects.get(username=username)
    current_profile = Profile.objects.get( user=user)
    service = Service.objects.all()
    services = service.filter(user=user)
    if request.method=='POST':
        edit_form = ProfileEditForm(instance=current_profile,
                data=request.POST, files=request.FILES)
        if edit_form.is_valid():
            edit_form.save()
    else:
        edit_form = ProfileEditForm(instance=current_profile)

    return render(request, 'account/profile.html',{'edit_form':edit_form, 'services':services})

@login_required
def about(request):
    return render(request, 'account/about.html')

@login_required
def landing(request):
    return render(request, 'account/landing.html')


