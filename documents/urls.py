from django.urls import path
from . import views

urlpatterns = [
    path('professions/all', views.AllProfessionDocuments.as_view(), name='all-professions'),
    path('professions/add', views.AddProfession.as_view(), name='add-professions'),
    path('professions/update/<int:pk>', views.UpdateProfession.as_view(), name='update-professions')

]
