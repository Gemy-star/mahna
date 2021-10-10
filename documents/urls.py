from django.urls import path
from . import views

urlpatterns = [
    path('professions/all', views.AllProfessionDocuments.as_view(), name='all-professions'),
    path('professions/add', views.AddProfession.as_view(), name='add-professions'),
    path('professions/update/<int:pk>', views.UpdateProfession.as_view(), name='update-professions'),
    path('applicants/all', views.AllApplicantsDocuments.as_view(), name='all-applicants'),
    path('applicants/add', views.AddApplicant.as_view(), name='add-applicant'),
    path('applicants/update/<int:pk>', views.UpdateApplicant.as_view(), name='update-applicant'),
    path('proof/add/', views.AddProof.as_view(), name='add-proof'),
    path('floor/add/', views.AddFloor.as_view(), name='add-floor'),
    path('Licenses/all', views.AllLicenses.as_view(), name='all-licenses'),
    path('Licenses/add', views.AddLicenses.as_view(), name='add-licenses'),
    path('Licenses/update/<int:pk>', views.UpdateLicenses.as_view(), name='update-licenses'),
    path('location/add/', views.AddLocation.as_view(), name='add-location'),
    path('locations/all', views.AllLocations.as_view(), name='all-locations'),

]
