from django.urls import path
from django.urls import reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    #Post Views
    path('register/', views.user_register, name ='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('landing/', views.landing, name='landing'),
    path('logout/', views.logout_request, name='logout'),
    path('password_reset/',
        auth_views.PasswordResetView.as_view(success_url=reverse_lazy('user:password_reset_done')),
        name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('user:password_reset_complete')),
        name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
    path('profile/', views.edit, name='edit')

]
