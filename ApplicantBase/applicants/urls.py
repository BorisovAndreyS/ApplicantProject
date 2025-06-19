
from django.urls import path
from django.views.generic import TemplateView
from .views import ApplicantAddView, ApplicantListView, ApplicantsDetailView


urlpatterns = [
    path('', ApplicantListView.as_view(), name='index'),
    path('add/', ApplicantAddView.as_view(), name='ApplicantAdd'),
    path('applicants/', ApplicantListView.as_view(), name='Applicants_list'),
    path('<int:pk>/', ApplicantsDetailView.as_view(), name='DetailView')
]