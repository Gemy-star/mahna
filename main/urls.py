from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('admin',  login_required(views.AdminPage.as_view()), name='admin-page'),
    path('dataEntry',  login_required(views.DataEntryPage.as_view()), name='dataEntry-page'),
    path('resident',  login_required(views.ResidentPage.as_view()), name='resident-page'),
    path('manager',  login_required(views.ManagerPage.as_view()), name='manager-page'),
]
