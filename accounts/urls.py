from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('manager/add', views.RegisterManager.as_view(), name='register-manager'),
    path('accountant/add', views.RegisterAccountant.as_view(), name='register-accountant'),
    path('resident/add', views.RegisterResident.as_view(), name='register-resident'),
    path('control', views.EmployeeControl.as_view(), name='employee-control'),

]
